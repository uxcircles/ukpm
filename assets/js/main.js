(function () {
  var doc = document.documentElement;

  // Header shadow
  var header = document.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('is-scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('[data-nav]');
  if (burger && nav) {
    var setMenu = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', burger.getAttribute(open ? 'data-close' : 'data-open'));
      nav.classList.toggle('is-open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', function () { setMenu(burger.getAttribute('aria-expanded') !== 'true'); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
    window.matchMedia('(min-width: 1081px)').addEventListener('change', function (m) { if (m.matches) setMenu(false); });
  }

  // Scroll reveal
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Sub-nav highlight
  var sub = document.querySelectorAll('.subnav a');
  if (sub.length && 'IntersectionObserver' in window) {
    var map = {};
    sub.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          sub.forEach(function (a) { a.classList.remove('is-active'); });
          var a = map[en.target.id];
          if (a) a.classList.add('is-active');
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) so.observe(el); });
  }

  // Hong Kong / London clocks
  var clocks = document.querySelector('[data-clocks]');
  if (clocks) {
    var parts = function (tz) {
      var p = {};
      new Intl.DateTimeFormat('en-GB', { timeZone: tz, hour: '2-digit', minute: '2-digit', hourCycle: 'h23' })
        .formatToParts(new Date()).forEach(function (x) { p[x.type] = x.value; });
      return { h: +p.hour, m: +p.minute };
    };
    var tick = function () {
      var hk = parts('Asia/Hong_Kong'), uk = parts('Europe/London');
      [['Asia/Hong_Kong', hk], ['Europe/London', uk]].forEach(function (z) {
        var t = z[1];
        var txt = clocks.querySelector('[data-time="' + z[0] + '"]');
        if (txt) txt.textContent = (t.h < 10 ? '0' : '') + t.h + ':' + (t.m < 10 ? '0' : '') + t.m;
        var face = clocks.querySelector('[data-tz="' + z[0] + '"]');
        if (face) {
          face.querySelector('.h').style.transform = 'rotate(' + ((t.h % 12) * 30 + t.m * 0.5) + 'deg)';
          face.querySelector('.m').style.transform = 'rotate(' + (t.m * 6) + 'deg)';
        }
      });
      var diff = ((hk.h * 60 + hk.m) - (uk.h * 60 + uk.m) + 1440) % 1440 / 60;
      var d = clocks.querySelector('[data-diff]');
      if (d) d.textContent = Math.round(diff);
    };
    tick();
    setInterval(tick, 20000);
  }

  var gbp = function (n) { return '£' + Math.round(n).toLocaleString('en-GB'); };

  // Viewing cost calculator: £1 per round-trip mile + £15 per property
  var vc = document.querySelector('[data-viewcalc]');
  if (vc) {
    var miles = vc.querySelector('[name="miles"]');
    var n = vc.querySelector('[name="n"]');
    var waLink = vc.querySelector('[data-viewwa]');
    var updateV = function () {
      var m = Math.max(0, Math.min(2000, parseInt(miles.value, 10) || 0));
      var k = Math.max(1, Math.min(10, parseInt(n.value, 10) || 1));
      var total = m + 15 * k;
      vc.querySelector('[data-total]').textContent = gbp(total);
      vc.querySelector('[data-each]').textContent = gbp(total / k);
      vc.querySelector('[data-formula]').textContent = m + ' 英里 × £1 + ' + k + ' 個物業 × £15';
      waLink.href = 'https://wa.me/' + waLink.href.split('wa.me/')[1].split('?')[0] + '?text=' +
        encodeURIComponent('你好 UKPM，我想預約遙距睇屋，大約 ' + k + ' 個物業。');
    };
    vc.addEventListener('input', updateV);
    vc.querySelectorAll('[data-step]').forEach(function (b) {
      b.addEventListener('click', function () {
        n.value = Math.max(1, Math.min(10, (parseInt(n.value, 10) || 1) + +b.getAttribute('data-step')));
        updateV();
      });
    });
    vc.addEventListener('submit', function (e) { e.preventDefault(); });
    updateV();
  }

  // Loan estimator: residential = min(4.5x income, 75% LTV); buy-to-let = 60% LTV
  var lc = document.querySelector('[data-loancalc]');
  if (lc) {
    var incomeField = lc.querySelector('[data-income-field]');
    var updateL = function () {
      var own = lc.querySelector('[name="use"]:checked').value === 'own';
      var price = Math.max(0, +lc.querySelector('[name="price"]').value || 0);
      var income = Math.max(0, +lc.querySelector('[name="income"]').value || 0);
      incomeField.hidden = !own;
      var ltv = price * (own ? 0.75 : 0.60);
      var loan = ltv, basis = '以樓價 ' + (own ? '75' : '60') + '% 計算';
      if (own && income * 4.5 < ltv) { loan = income * 4.5; basis = '以年收入 4.5 倍計算（低於樓價 75%）'; }
      lc.querySelector('[data-loan]').textContent = gbp(loan);
      lc.querySelector('[data-deposit]').textContent = gbp(Math.max(0, price - loan));
      lc.querySelector('[data-basis]').textContent = basis;
    };
    lc.addEventListener('input', updateL);
    lc.addEventListener('change', updateL);
    lc.addEventListener('submit', function (e) { e.preventDefault(); });
    updateL();
  }

  // Enquiry form: compose a WhatsApp message (no server needed)
  var form = document.querySelector('[data-enquiry]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var f = new FormData(form);
      var lines = ['你好 UKPM，我想查詢：'];
      var svc = f.getAll('service');
      if (svc.length) lines.push('服務：' + svc.join('、'));
      [['name', '名字'], ['area', '物業地區'], ['where', '現在身在']].forEach(function (k) {
        var v = (f.get(k[0]) || '').toString().trim();
        if (v) lines.push(k[1] + '：' + v);
      });
      var msg = (f.get('message') || '').toString().trim();
      if (msg) lines.push('', msg);
      window.open('https://wa.me/' + form.getAttribute('data-wa') + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    });
  }

  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
