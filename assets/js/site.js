/* Green Spring Marketing
   Motion is additive. Everything is readable and usable with JS off, and every
   effect is disabled under prefers-reduced-motion. */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var root = document.documentElement;

  /* ---- hero entrance ------------------------------------------------- */
  function start() { document.body.classList.add('loaded'); }
  var heroImg = document.querySelector('.hero__media img');
  if (heroImg && !heroImg.complete) {
    heroImg.addEventListener('load', start, { once: true });
    heroImg.addEventListener('error', start, { once: true });
    setTimeout(start, 1800);
  } else {
    requestAnimationFrame(start);
  }

  /* ---- reveal on enter ----------------------------------------------- */
  var revealables = document.querySelectorAll('.rv, .map, .cap, .found__in, .rule');
  if (!('IntersectionObserver' in window) || reduced) {
    revealables.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.12 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---- nav condense + scroll progress -------------------------------- */
  var nav = document.getElementById('nav');
  var progress = document.getElementById('progress');
  var fill = document.getElementById('fill');
  var track = document.getElementById('track');
  var stmtMedia = document.getElementById('stmtMedia');
  var ticking = false;

  function frame() {
    var y = window.pageYOffset;
    var docH = document.documentElement.scrollHeight - window.innerHeight;

    if (nav) nav.classList.toggle('stuck', y > 24);
    if (progress && docH > 0) {
      progress.style.transform = 'scaleX(' + Math.min(1, y / docH) + ')';
    }

    /* the rule beside the method list fills as you read down it */
    if (fill && track) {
      var r = track.getBoundingClientRect();
      var vh = window.innerHeight;
      var p = (vh * 0.62 - r.top) / r.height;
      fill.style.height = Math.max(0, Math.min(1, p)) * 100 + '%';
    }

    /* a little counter-drift on the leaf so the band feels alive */
    if (stmtMedia && !reduced) {
      var s = stmtMedia.getBoundingClientRect();
      if (s.bottom > 0 && s.top < window.innerHeight) {
        var mid = (s.top + s.height / 2 - window.innerHeight / 2) / window.innerHeight;
        stmtMedia.style.transform = 'translate3d(0,' + (mid * -22).toFixed(2) + 'px,0)';
      }
    }
    ticking = false;
  }

  function onScroll() {
    if (!ticking) { ticking = true; requestAnimationFrame(frame); }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  frame();

  /* ---- counters ------------------------------------------------------- */
  var counters = document.querySelectorAll('.count');
  function runCount(el) {
    var to = parseInt(el.getAttribute('data-to'), 10) || 0;
    if (reduced) { el.textContent = to; return; }
    var dur = 1500, t0 = null;
    function step(t) {
      if (t0 === null) t0 = t;
      var p = Math.min(1, (t - t0) / dur);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(to * eased);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { runCount(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(runCount);
  }

  /* ---- mobile menu ---------------------------------------------------- */
  var burger = document.getElementById('burger');
  var menu = document.getElementById('menu');
  function closeMenu() {
    document.body.classList.remove('menu-open');
    if (burger) {
      burger.setAttribute('aria-expanded', 'false');
      burger.setAttribute('aria-label', 'Open menu');
    }
  }
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') closeMenu();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeMenu();
    });
  }

  /* ---- shared nav and footer ------------------------------------------
     The nav and footer markup is byte identical on every page, so links are
     written page-qualified (index.html#services). Here they are collapsed to
     a plain hash when they already point at the current page, which keeps the
     smooth scroll, and the current page is marked for the reader. */
  (function () {
    var here = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav a[href], .menu a[href], .foot a[href]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (!href || href.charAt(0) === '#' || /^(https?:|mailto:|tel:)/.test(href)) return;
      var parts = href.split('#');
      var page = parts[0];
      if (page !== here) return;
      a.setAttribute('href', parts[1] ? '#' + parts[1] : '#top');
      if (!parts[1]) a.setAttribute('aria-current', 'page');
    });
  })();

  /* ---- current section in the nav ------------------------------------- */
  var sections = ['capabilities', 'approach', 'method', 'team']
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);
  if (sections.length && 'IntersectionObserver' in window) {
    var links = {};
    document.querySelectorAll('.nav__link').forEach(function (a) {
      links[a.getAttribute('href').slice(1)] = a;
    });
    var visible = [];
    var sio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        var i = visible.indexOf(e.target.id);
        if (e.isIntersecting && i === -1) visible.push(e.target.id);
        if (!e.isIntersecting && i !== -1) visible.splice(i, 1);
      });
      Object.keys(links).forEach(function (id) { links[id].removeAttribute('aria-current'); });
      var top = visible[visible.length - 1];
      if (top && links[top]) links[top].setAttribute('aria-current', 'true');
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { sio.observe(s); });
  }
})();
