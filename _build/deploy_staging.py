"""Publish the static site to the client's own server for review.

Target is a folder inside the live WordPress document root, so the script is
deliberately narrow: it uploads an allowlist of paths and nothing else, and it
refuses outright to send anything that looks like a credential, a brief, or an
email attachment. Everything the client does not need to see stays on disk.

Nothing is sent without --go. The default run prints the manifest and exits.

    python _build/deploy_staging.py           # dry run, uploads nothing
    python _build/deploy_staging.py --go      # actually uploads
    python _build/deploy_staging.py --verify  # just check what is live

Credentials come from _brief/CREDENTIALS.local.md, which is gitignored and must
never be committed. Note that DreamHost renames the server when it migrates an
account, which already happened once here (ps415190 -> vps40274), so the host is
read from that file rather than hardcoded.
"""
import argparse
import fnmatch
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

import paramiko

ROOT = Path(__file__).resolve().parent.parent
CRED = ROOT / "_brief" / "CREDENTIALS.local.md"

REMOTE_BASE = "greenspringmarketing.com"
STAGING = "new-staging"
PUBLIC_URL = f"https://greenspringmarketing.com/{STAGING}"

# Only these go up. Anything not matched here is not uploaded, full stop.
INCLUDE_FILES = ["index.html", "about.html", "approach.html", "capabilities.html",
                 "editorial.html"]
INCLUDE_DIRS = ["assets"]

# Belt and braces on top of the allowlist.
NEVER = [
    "*credential*", "*.local.md", "*.env", "*.py", "*.pyc",
    "_brief/*", "_build/*", "email/*", ".git/*", "*/portraits/*",
    # uncropped source material the client sent us; nothing on the pages
    # references it, so it has no business sitting on a public URL
    "*/from-client/*",
    # raw full-size downloads kept for re-cropping. The pages only ever load
    # the derived WebP in assets/img, so these are 22 MB nobody requests.
    "*/photos/*", "*/photos-about/*",
]


def forbidden(rel):
    low = rel.lower()
    return any(fnmatch.fnmatch(low, p) for p in NEVER)


def creds():
    if not CRED.exists():
        sys.exit(f"missing {CRED}")
    t = CRED.read_text(encoding="utf-8")

    def field(k):
        m = re.search(rf"\|\s*{k}\s*\|\s*`?([^`|]+?)`?\s*\|", t)
        if not m:
            sys.exit(f"'{k}' not found in the credentials file")
        return m.group(1).strip()

    return field("SFTP host"), field("SFTP user"), field("SFTP password")


def manifest():
    """Every file to upload, as (local path, path relative to the staging root)."""
    out = []
    for name in INCLUDE_FILES:
        p = ROOT / name
        if p.is_file():
            out.append((p, name))
    for d in INCLUDE_DIRS:
        for p in sorted((ROOT / d).rglob("*")):
            if p.is_file():
                out.append((p, p.relative_to(ROOT).as_posix()))

    kept, refused = [], []
    for p, rel in out:
        (refused if forbidden(rel) else kept).append((p, rel))
    if refused:
        print("REFUSED (matched the never-upload list):")
        for _, rel in refused:
            print(f"  {rel}")
        print()

    # the folder's own Apache config, which is not part of the site source
    kept.append((ROOT / "_build" / "staging.htaccess", ".htaccess"))
    return kept


def ensure_dir(sftp, path):
    parts, cur = path.strip("/").split("/"), ""
    for part in parts:
        cur = f"{cur}/{part}"
        try:
            sftp.stat(cur)
        except IOError:
            sftp.mkdir(cur)


def verify():
    print(f"\nchecking {PUBLIC_URL} ...")
    checks = [
        f"{PUBLIC_URL}/",
        f"{PUBLIC_URL}/about.html",
        f"{PUBLIC_URL}/assets/css/site.css",
        f"{PUBLIC_URL}/assets/img/favicon.svg",
    ]
    ok = True
    for url in checks:
        req = urllib.request.Request(url, headers={"User-Agent": "gsm-deploy-check"})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                tag = r.headers.get("X-Robots-Tag", "")
                ctype = r.headers.get("Content-Type", "").split(";")[0]
                note = "" if "noindex" in tag else "   <-- NOT noindexed"
                if not note:
                    pass
                else:
                    ok = False
                print(f"  {r.status}  {ctype:<24} {url}{note}")
        except urllib.error.HTTPError as e:
            ok = False
            print(f"  {e.code}  FAILED  {url}")
        except Exception as e:
            ok = False
            print(f"  ---  FAILED  {url}  ({e})")
    print("\nall good" if ok else "\nsomething is wrong, see above")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--go", action="store_true", help="actually upload")
    ap.add_argument("--verify", action="store_true", help="only check the live URLs")
    a = ap.parse_args()

    if a.verify:
        return 0 if verify() else 1

    host, user, pw = creds()
    files = manifest()
    total = sum(p.stat().st_size for p, _ in files)
    print(f"{len(files)} files, {total / 1024 / 1024:.1f} MB")
    print(f"target: {host}:~/{REMOTE_BASE}/{STAGING}/")
    print(f"url:    {PUBLIC_URL}/\n")

    if not a.go:
        for _, rel in files[:12]:
            print(f"  {rel}")
        if len(files) > 12:
            print(f"  ... and {len(files) - 12} more")
        print("\nDRY RUN. Nothing was uploaded. Re-run with --go to publish.")
        return 0

    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(host, username=user, password=pw, timeout=30,
              look_for_keys=False, allow_agent=False)
    s = c.open_sftp()

    home = s.normalize(".")
    base = f"{home}/{REMOTE_BASE}/{STAGING}"
    ensure_dir(s, base)

    made = set()
    for i, (p, rel) in enumerate(files, 1):
        remote = f"{base}/{rel}"
        parent = remote.rsplit("/", 1)[0]
        if parent not in made:
            ensure_dir(s, parent)
            made.add(parent)
        s.put(str(p), remote)
        if i % 10 == 0 or i == len(files):
            print(f"  {i}/{len(files)}")

    s.close()
    c.close()
    print("\nupload done")
    return 0 if verify() else 1


if __name__ == "__main__":
    sys.exit(main())
