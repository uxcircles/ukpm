#!/usr/bin/env python3
"""Generate the UKPM Property Management static pages.

Shared header / footer live here; each page's body is a function below.
Run from the repo root:  python3 _build/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://uxcircles.github.io/ukpm/"
OFFICIAL = "https://ukpm.uk/"
CSS_V = 1
JS_V = 1

PHONE = "+44 7459 845827"
TEL = "+447459845827"
WA = "447459845827"
FB = "https://www.facebook.com/Online-Property-Management-105652351804203"
PRS_NO = "PRS036281"
LOAN_PDF = "https://ukpm.uk/loanApplicationform.pdf"

NAV = [
    ("landlords.html", "業主服務"),
    ("buying.html", "買樓及睇樓"),
    ("mortgage.html", "物業貸款"),
    ("home-services.html", "保險 · 水電煤 · 裝修"),
    ("about.html", "關於我們"),
]

SERVICES = [
    # (href, icon, title, text)
    ("landlords.html#rental", "key", "物業出租", "找可靠本地代理、拍照刊登、安排睇樓、審查租客、登記按金。"),
    ("landlords.html#management", "home", "物業管理", "代你回覆租客、跟進維修、證書到期前提醒並安排更新。"),
    ("buying.html#buy", "doc", "物業買賣", "安排合資格測量師驗樓及買賣律師，手續一條龍。"),
    ("buying.html#viewing", "eye", "遙距睇屋", "同事親身到場，可即場視像，附詳細書面報告。"),
    ("mortgage.html", "pound", "物業貸款", "專門處理未有英國信貸記錄、身在海外的買家。"),
    ("home-services.html#insurance", "shield", "保險服務", "自住、出租及商業物業保險，協助處理索償。"),
    ("home-services.html#utilities", "bolt", "水電煤寬頻", "煤氣、電力、寬頻、電話一個賬戶處理。"),
    ("home-services.html#renovation", "tool", "裝修工程", "香港師傅加本地團隊，大小工程都可報價。"),
]

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-check" viewBox="0 0 24 24"><path d="M20 6 9 17l-5-5"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M5 4h3.5l1.8 4.5-2.3 1.4a11 11 0 0 0 6.1 6.1l1.4-2.3L20 15.5V19a1.5 1.5 0 0 1-1.6 1.5A16.5 16.5 0 0 1 3.5 5.6 1.5 1.5 0 0 1 5 4Z"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path d="M12 2.2A9.7 9.7 0 0 0 3.6 16.8L2.3 21.7l5-1.3A9.7 9.7 0 1 0 12 2.2Zm0 17.7a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1 1 12 19.9Zm4.4-6c-.2-.1-1.4-.7-1.7-.8-.2-.1-.4-.1-.5.1l-.8 1c-.1.2-.3.2-.5.1a6.6 6.6 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.5-.4h-.5a.9.9 0 0 0-.6.3 2.7 2.7 0 0 0-.8 2c0 1.2.9 2.3 1 2.5.1.2 1.7 2.6 4.1 3.7 1.5.7 2.1.7 2.9.6.5-.1 1.4-.6 1.6-1.1.2-.6.2-1 .1-1.1l-.4-.3Z"/></symbol>
  <symbol id="i-ext" viewBox="0 0 24 24"><path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/></symbol>
  <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6L12 3Z"/><path d="m8.8 12 2.2 2.2 4.2-4.4"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
  <symbol id="i-home" viewBox="0 0 24 24"><path d="M3.5 11 12 4l8.5 7"/><path d="M5.5 9.5V20h13V9.5"/><path d="M10 20v-5.5h4V20"/></symbol>
  <symbol id="i-key" viewBox="0 0 24 24"><circle cx="8" cy="15" r="4"/><path d="m10.8 12.2 8.7-8.7M16.5 6.5l2.5 2.5M14 9l2 2"/></symbol>
  <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4V5Z"/><path d="M8 9.5h8M8 12.5h5"/></symbol>
  <symbol id="i-pound" viewBox="0 0 24 24"><path d="M16.5 6.5A3.8 3.8 0 0 0 9 7.5V19M6 19h12M6.5 12.5h7"/></symbol>
  <symbol id="i-tool" viewBox="0 0 24 24"><path d="M14.5 6.5a4 4 0 0 0 5 5L12 19a2.1 2.1 0 0 1-3-3l7.5-7.5"/><path d="M14.5 6.5 17 4l3 3-2.5 2.5"/></symbol>
  <symbol id="i-doc" viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6V3Z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></symbol>
  <symbol id="i-eye" viewBox="0 0 24 24"><path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.6a3.5 3.5 0 0 1 0 6.8M18.5 14a6.5 6.5 0 0 1 3 6"/></symbol>
  <symbol id="i-bolt" viewBox="0 0 24 24"><path d="M13 3 5 13.5h6L10 21l8-10.5h-6L13 3Z"/></symbol>
  <symbol id="i-video" viewBox="0 0 24 24"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10.5 5-3v9l-5-3"/></symbol>
  <symbol id="i-bell" viewBox="0 0 24 24"><path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15L6 16Z"/><path d="M10 20.5a2 2 0 0 0 4 0"/></symbol>
  <symbol id="i-download" viewBox="0 0 24 24"><path d="M12 4v11M7 10.5l5 5 5-5M5 20h14"/></symbol>
  <symbol id="i-fb" viewBox="0 0 24 24"><path d="M14 8.5V6.8c0-.8.2-1.3 1.4-1.3H17V2.6A21 21 0 0 0 14.6 2.5C12.2 2.5 10.6 4 10.6 6.6v1.9H8v3.2h2.6V21.5H14v-9.8h2.6l.4-3.2H14Z"/></symbol>
</svg>"""

# Clock mark taken from the UKPM logo: teal ring, black hands at 4 o'clock.
MARK = """<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="16.5" fill="none" stroke="currentColor" stroke-width="4.5"/><path d="M20 9.5V20l6.5 6.5" fill="none" stroke="var(--ink)" stroke-width="3.4" stroke-linecap="square"/><circle cx="20" cy="20" r="2.4" fill="var(--ink)"/></svg>"""


def icon(name, cls="icon"):
    fill = " icon-fill" if name in ("wa", "fb") else ""
    return f'<svg class="{cls}{fill}" aria-hidden="true"><use href="#i-{name}"/></svg>'


def ext():
    return icon("ext")


def wa_link(text="", label="WhatsApp 查詢", cls="btn btn-wa"):
    q = f"?text={text}" if text else ""
    return f'<a class="{cls}" href="https://wa.me/{WA}{q}" target="_blank" rel="noopener">{icon("wa")}{label}</a>'


def brand():
    return f"""<a class="brand" href="index.html" aria-label="UKPM Property Management 主頁">
        {MARK}
        <span class="brand-word"><span class="brand-name">UKPM</span><span class="brand-tag">Property Management</span></span>
      </a>"""


def header(active):
    items = "\n".join(
        f'          <li><a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in NAV)
    return f"""  <a class="skip" href="#main">跳到主要內容</a>
  {SPRITE}
  <div class="concept-bar" role="note">
    <div class="wrap concept-inner">
      <p><span class="concept-tag">Concept</span><span class="concept-long">網站改版概念設計，並非 <a href="{OFFICIAL}" target="_blank" rel="noopener">UKPM 官方網站</a>。</span></p>
      <a href="https://ux-circles.com/web" target="_blank" rel="noopener">Designed by <strong>UX CIRCLES</strong> {ext()}</a>
    </div>
  </div>
  <header class="site-header">
    <div class="wrap header-inner">
      {brand()}
      <nav class="nav" id="site-nav" aria-label="主選單" data-nav>
        <ul class="nav-list">
{items}
        </ul>
        <div class="nav-extra">
          {wa_link()}
          <a class="btn btn-ghost" href="tel:{TEL}">{icon("phone")}{PHONE}</a>
        </div>
      </nav>
      <div class="header-cta">
        <a class="btn btn-primary btn-sm hide-sm" href="contact.html"{" aria-current=\"page\"" if active == "contact.html" else ""}>免費諮詢</a>
        <a class="btn btn-wa btn-sm" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}<span>WhatsApp</span></a>
        <button class="burger" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="開啟選單" data-open="開啟選單" data-close="關閉選單"><span></span><span></span><span></span></button>
      </div>
    </div>
  </header>"""


def footer():
    svc = "\n".join(f'            <li><a href="{h}">{t}</a></li>' for h, _, t, _ in SERVICES)
    return f"""  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-about">
          {brand()}
          <p>由移居英國多年的香港人營運的物業管理公司。以廣東話替身在海外或英國的業主處理出租、管理、買賣及貸款。</p>
          <div class="social"><a href="{FB}" target="_blank" rel="noopener" aria-label="UKPM Facebook">{icon("fb")}</a><a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{icon("wa")}</a></div>
        </div>
        <div>
          <h4>服務</h4>
          <ul class="footer-cols">
{svc}
          </ul>
        </div>
        <div>
          <h4>聯絡</h4>
          <ul>
            <li><a href="https://wa.me/{WA}" target="_blank" rel="noopener">WhatsApp {PHONE}</a></li>
            <li><a href="contact.html">網上查詢表</a></li>
            <li><a href="about.html">關於我們</a></li>
          </ul>
          <h4>監管</h4>
          <ul>
            <li>Property Redress Scheme 會員</li>
            <li>PRS 編號 {PRS_NO}</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© <span data-year>2026</span> UKPM Property Management</p>
        <p>官方網站 <a href="{OFFICIAL}" target="_blank" rel="noopener">ukpm.uk {ext()}</a> · 改版概念設計 <a href="https://ux-circles.com/web" target="_blank" rel="noopener">UX CIRCLES {ext()}</a></p>
      </div>
    </div>
  </footer>

  <nav class="action-bar" aria-label="快速聯絡">
    <a class="is-wa" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}WhatsApp</a>
    <a href="tel:{TEL}">{icon("phone")}致電</a>
    <a href="contact.html">{icon("chat")}查詢表</a>
  </nav>"""


def page(slug, title, desc, body, active=None, preload=None):
    path = "" if slug == "index.html" else slug
    url = BASE + path
    pre = f'\n  <link rel="preload" as="image" href="{preload}" fetchpriority="high">' if preload else ""
    html = f"""<!doctype html>
<html lang="zh-Hant-HK" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex, nofollow">
  <meta name="theme-color" content="#F3F8F8">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="UKPM Property Management">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{BASE}assets/img/hero.webp">{pre}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Outfit:wght@500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css?v={CSS_V}">
  <script>document.documentElement.classList.replace('no-js','js')</script>
</head>
<body>
{header(slug if active is None else active)}

  <main id="main">
{body}
  </main>

{footer()}
  <script src="assets/js/main.js?v={JS_V}" defer></script>
</body>
</html>
"""
    (ROOT / slug).write_text(html, encoding="utf-8")
    print("wrote", slug)


def crumbs(label):
    return f"""<nav class="crumbs" aria-label="頁面位置"><ol><li><a href="index.html">主頁</a></li><li aria-current="page">{label}</li></ol></nav>"""


def page_hero(label, eyebrow, h1, lead, img=None, alt="", extra=""):
    media = f"""
        <figure class="page-hero-media"><img src="{img}" alt="{alt}" width="1200" height="900" fetchpriority="high"></figure>""" if img else ""
    return f"""    <section class="page-hero{' has-media' if img else ''}">
      <div class="wrap">
        {crumbs(label)}
        <div class="page-hero-grid">
          <div>
            <p class="eyebrow">{eyebrow}</p>
            <h1>{h1}</h1>
            <p class="lead">{lead}</p>
            <div class="btn-row">
              <a class="btn btn-primary" href="contact.html">免費諮詢 {icon("arrow")}</a>
              {wa_link(label="WhatsApp 我們", cls="btn btn-ghost")}
            </div>{extra}
          </div>{media}
        </div>
      </div>
    </section>"""


def checklist(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{icon('check')}<span>{i}</span></li>" for i in items) + "</ul>"


def faq(items, open_first=False):
    out = []
    for n, (q, a) in enumerate(items):
        o = " open" if open_first and n == 0 else ""
        out.append(f"""          <details class="faq-item"{o}>
            <summary><span>{q}</span><span class="faq-sign" aria-hidden="true"></span></summary>
            <div class="faq-body">{a}</div>
          </details>""")
    return '<div class="faq">\n' + "\n".join(out) + "\n        </div>"


def cta(h="身在海外，英國物業交給我們", p="WhatsApp 告訴我們物業所在地區和你需要的服務，同事會以廣東話回覆。查詢免費。"):
    return f"""    <section class="section">
      <div class="wrap">
        <div class="cta-band reveal">
          <div class="cta-clock" aria-hidden="true">{MARK}</div>
          <div>
            <h2>{h}</h2>
            <p>{p}</p>
          </div>
          <div class="btn-row">
            {wa_link(label="WhatsApp 查詢")}
            <a class="btn btn-light" href="contact.html">填寫查詢表</a>
          </div>
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------- pages

def index():
    cards = "\n".join(f"""          <a class="svc-card reveal" href="{h}">
            <span class="svc-icon">{icon(i)}</span>
            <h3>{t}</h3>
            <p>{x}</p>
            <span class="svc-more">了解更多 {icon("arrow")}</span>
          </a>""" for h, i, t, x in SERVICES)
    body = f"""    <section class="hero">
      <div class="wrap hero-grid">
        <div class="hero-copy">
          <p class="eyebrow"><span class="dot"></span>英國持牌物業管理公司 · {PRS_NO}</p>
          <h1>人在香港<br><span class="hl">英國物業</span>交給我們</h1>
          <p class="lead">由移居英國多年的香港人團隊，以廣東話替你處理出租、管理、買賣、貸款及大小維修。無論物業在英國哪裡，都可以幫你。</p>
          <div class="btn-row">
            <a class="btn btn-primary btn-lg" href="contact.html">免費諮詢 {icon("arrow")}</a>
            {wa_link(label="WhatsApp 查詢", cls="btn btn-ghost btn-lg")}
          </div>
          <ul class="hero-points">
            <li>{icon("chat")}廣東話溝通</li>
            <li>{icon("shield")}PRS 監管會員</li>
            <li>{icon("pin")}服務全英國</li>
          </ul>
        </div>
        <div class="hero-visual">
          <figure class="hero-photo"><img src="assets/img/hero.webp" alt="英國一排紅磚維多利亞式排屋" width="1200" height="900" fetchpriority="high"></figure>
          <div class="clocks" data-clocks aria-label="香港及英國現在時間">
            <div class="clock-row">
              <span class="clock-face" data-tz="Asia/Hong_Kong" aria-hidden="true"><i class="h"></i><i class="m"></i></span>
              <span class="clock-txt"><small>你在香港</small><strong data-time="Asia/Hong_Kong">--:--</strong></span>
            </div>
            <div class="clock-row is-uk">
              <span class="clock-face" data-tz="Europe/London" aria-hidden="true"><i class="h"></i><i class="m"></i></span>
              <span class="clock-txt"><small>我們在英國</small><strong data-time="Europe/London">--:--</strong></span>
            </div>
            <p class="clock-note">相差 <span data-diff>8</span> 小時，你休息時我們替你跟進</p>
          </div>
        </div>
      </div>
    </section>

    <section class="trust">
      <div class="wrap trust-grid">
        <div><strong>{PRS_NO}</strong><span>Property Redress Scheme 註冊編號</span></div>
        <div><strong>8 項服務</strong><span>出租、管理、買賣、貸款等一站式處理</span></div>
        <div><strong>廣東話</strong><span>香港人團隊，減少溝通誤會</span></div>
        <div><strong>全英國</strong><span>物業在哪個城市都可以服務</span></div>
      </div>
    </section>

    <section class="section" id="services">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">服務</p>
          <h2>由買樓到收租，一間公司跟到底</h2>
          <p>主要服務身在英國境外、持有或準備購入英國物業的客戶。已在英國生活、需要人幫手處理出租或自住物業問題，一樣可以找我們。</p>
        </div>
        <div class="svc-grid">
{cards}
        </div>
      </div>
    </section>

    <section class="section section-tint">
      <div class="wrap split">
        <figure class="split-media reveal"><img src="assets/img/remote.webp" alt="在家用手提電腦處理事務" width="1200" height="900" loading="lazy"></figure>
        <div class="split-copy reveal">
          <p class="eyebrow">為甚麼選 UKPM</p>
          <h2>我們走過的路，正是你準備要走的路</h2>
          <p>團隊由一班移居英國多年的「前」香港人組成，自己買過樓、租過樓、做過業主。你將來會遇到的問題，我們大多已經一一經歷過。</p>
          <ul class="why">
            <li>{icon("chat")}<div><h3>廣東話，訊息不走樣</h3><p>租約條款、維修報價、法例更新，都以你熟悉的語言講清楚。</p></div></li>
            <li>{icon("shield")}<div><h3>持牌並受監管</h3><p>Property Redress Scheme 註冊會員（{PRS_NO}），有官方渠道處理投訴。</p></div></li>
            <li>{icon("bell")}<div><h3>到期前先提醒</h3><p>煤氣、電力、EPC 等證書到期前通知你並安排更新，避免出租物業違規。</p></div></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">海外業主出租流程</p>
          <h2>四步把英國物業租出去</h2>
        </div>
        <ol class="steps">
          <li class="reveal"><span class="step-n">1</span><h3>WhatsApp 查詢</h3><p>告訴我們物業地址、現況及你的期望租金。</p></li>
          <li class="reveal"><span class="step-n">2</span><h3>證書及準備</h3><p>安排煤氣、電力、EPC 等出租必需證書，跟進執修。</p></li>
          <li class="reveal"><span class="step-n">3</span><h3>刊登及審查</h3><p>拍照刊登、安排睇樓，替租客做信貸及背景審查。</p></li>
          <li class="reveal"><span class="step-n">4</span><h3>入住及管理</h3><p>登記按金，之後由我們處理租客日常查詢及維修。</p></li>
        </ol>
      </div>
    </section>

    <section class="section section-ink">
      <div class="wrap feature">
        <div class="reveal">
          <p class="eyebrow">遙距睇屋</p>
          <h2>未到英國，都可以先睇樓</h2>
          <p>同事親身到場視察屋內及附近環境，可即場視像讓你指定要看的位置，之後交詳細書面報告：各房間評分、治安、超市、交通及最近三間中小學。</p>
          <a class="btn btn-light" href="buying.html#viewing">看收費及即時估價 {icon("arrow")}</a>
        </div>
        <div class="price-card reveal">
          <p class="price-label">明碼實價</p>
          <p class="price"><span>£15</span><small>每個物業</small></p>
          <p class="price-plus">+</p>
          <p class="price"><span>£1</span><small>每英里來回車程</small></p>
          <p class="price-note">同一天睇多個物業，車程只計一次，平均成本更低</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap split split-rev">
        <div class="split-copy reveal">
          <p class="eyebrow">物業貸款</p>
          <h2>沒有英國信貸記錄，一樣可以申請按揭</h2>
          <p>我們與多間按揭中介緊密合作，專門處理非英籍、初到英國、或以香港收入申請的個案。已試過被拒？可以再找我們的貸款專員談談。</p>
          {checklist(["可用香港收入作按揭基礎", "初到英國、剛找到工作都可以申請", "先做 DIP，了解自己可以借多少"])}
          <div class="btn-row"><a class="btn btn-primary" href="mortgage.html">按揭問答及估算 {icon("arrow")}</a></div>
        </div>
        <figure class="split-media reveal"><img src="assets/img/buy.webp" alt="英國紅磚獨立屋及前花園" width="1068" height="801" loading="lazy"></figure>
      </div>
    </section>

{cta()}"""
    page("index.html", "UKPM Property Management｜英國物業出租、管理、買賣及貸款", "香港人團隊以廣東話替海外業主處理英國物業出租、管理、買賣、按揭、保險及裝修。Property Redress Scheme 會員 PRS036281。", body, preload="assets/img/hero.webp")


def about():
    body = f"""{page_hero("關於我們", "關於 UKPM", "無論你準備移居<br>還是已身在英國", "我們希望在你人生轉變的時候，幫你面對生活上大大小小的問題。", "assets/img/street.webp", "英國城市紅磚建築街景")}

    <section class="section">
      <div class="wrap split">
        <div class="split-copy reveal">
          <p class="eyebrow">我們是誰</p>
          <h2>一班熱心幫助香港人的「前」香港人</h2>
          <p>UKPM（Online Property Management）的團隊成員都居於英國多年，具備物業買賣、出租及管理經驗，熟悉英國物業市場運作。</p>
          <p>你們將來要面對的，我們也都一一經歷過。我們希望集合這些經驗，幫助更多港人在英國安頓下來，或者安心做個海外業主。</p>
        </div>
        <div class="stat-stack reveal">
          <div class="stat"><strong>廣東話</strong><span>同聲同氣，減少錯誤訊息傳遞</span></div>
          <div class="stat"><strong>全英國</strong><span>無論物業位於英國何處都可以服務</span></div>
          <div class="stat"><strong>一站式</strong><span>出租、管理、買賣、貸款、保險、裝修</span></div>
        </div>
      </div>
    </section>

    <section class="section section-tint">
      <div class="wrap">
        <div class="reg-card reveal">
          <div class="reg-badge">{icon("shield")}</div>
          <div>
            <p class="eyebrow">監管</p>
            <h2>Property Redress Scheme 註冊會員</h2>
            <p>Property Redress Scheme（PRS）是英國政府認可的物業代理投訴處理計劃。英格蘭的出租及物業管理代理必須加入這類計劃。如對我們的服務有爭議，你可以經這個獨立渠道投訴。</p>
            <p class="reg-no">會員編號 <strong>{PRS_NO}</strong></p>
          </div>
        </div>
      </div>
    </section>

{cta("想先聽聽我們的意見？")}"""
    page("about.html", "關於我們｜UKPM Property Management", "UKPM 團隊由移居英國多年的香港人組成，熟悉英國物業市場，以廣東話服務。Property Redress Scheme 會員。", body)


def landlords():
    certs = [
        ("煤氣安全證書", "Gas Safety Certificate", "每年"),
        ("電力安全報告", "EICR", "最少每 5 年"),
        ("能源效益證書", "EPC", "每 10 年"),
        ("熱水爐保養", "Boiler Service", "建議每年"),
        ("煙霧及一氧化碳警報", "Smoke &amp; CO alarms", "每次新租約開始"),
        ("按金保障", "Deposit Protection", "收按金後 30 日內"),
    ]
    rows = "\n".join(f"""            <tr><th scope="row">{a}<small>{b}</small></th><td>{c}</td></tr>""" for a, b, c in certs)
    body = f"""{page_hero("業主服務", "業主服務 · 出租及管理", "英國物業出租<br>專業、細心、全面", "自住還是出租都可以交給我們。由搵租客、做證書，到每天回覆租客查詢，你只需要收報告。", "assets/img/flat.webp", "英國現代住宅大廈外觀")}

    <nav class="subnav" aria-label="本頁內容"><div class="wrap"><a href="#rental">物業出租</a><a href="#management">物業管理</a><a href="#compliance">出租證書</a></div></nav>

    <section class="section" id="rental">
      <div class="wrap split-even">
        <div class="reveal">
          <p class="eyebrow">物業出租</p>
          <h2>替你找可靠本地代理，安排好每一步</h2>
          <p>我們會為你物業所在地區揀選可靠、專業的地產代理，並同時安排：</p>
          {checklist(["拍照及製作樓盤廣告，刊登上網", "安排睇樓（viewing）", "審查租客信貸及背景（referencing &amp; credit check），避免租霸", "處理並登記按金（deposit register）"])}
        </div>
        <div class="panel reveal">
          <h3>我們同時安排出租必需的檢查</h3>
          {checklist(["煤氣認證 Gas Certificate", "熱水爐保養 Boiler Service", "電器認證 Electrical Certificate", "防火系統檢查 Fire alarm inspection", "能源效益證書 EPC"], "checks checks-sm")}
          <p class="panel-note">亦可安排業主保險（landlords insurance）及租金保險（rent protection），並提供最新業主須知的法律資訊。</p>
        </div>
      </div>
    </section>

    <section class="section section-tint" id="management">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">物業管理</p>
          <h2>你是業主，日常事務由我們處理</h2>
          <p>無論自住還是出租物業，我們都可以提供以下服務。</p>
        </div>
        <div class="mgmt-grid">
          <article class="mgmt reveal">{icon("tool")}<h3>裝修、維修及保養</h3><p>替你搵合適工程公司、比較報價、跟進工程，並定時匯報進度。</p></article>
          <article class="mgmt reveal">{icon("bell")}<h3>EPC 及煤氣證書</h3><p>在英國出租物業，業主有責任確保家居安全並定期更新證書。我們會在到期前提醒你，並安排更新。</p></article>
          <article class="mgmt reveal">{icon("chat")}<h3>處理租客日常查詢</h3><p>租客直接聯絡我們的專員。日常查詢、投訴，以至緊急開鎖、煤氣洩漏、漏水等突發情況，都由我們跟進。</p></article>
          <article class="mgmt reveal">{icon("shield")}<h3>保障業主權益</h3><p>按監管機構要求提供服務。有新條例或舊條例更新時，第一時間通知你，確保物業符合規定。</p></article>
        </div>
      </div>
    </section>

    <section class="section" id="compliance">
      <div class="wrap split-even">
        <div class="reveal">
          <p class="eyebrow">出租證書</p>
          <h2>英格蘭出租物業常見要求</h2>
          <p>以下是業主一般需要處理的證書及期限。我們會記錄每個物業的到期日，提前提醒並安排。</p>
          <p class="fine">只作一般參考。蘇格蘭、威爾斯及北愛爾蘭規定不同，個別物業（如 HMO）亦有額外要求。</p>
        </div>
        <div class="table-wrap reveal">
          <table class="cert-table">
            <thead><tr><th scope="col">項目</th><th scope="col">更新周期</th></tr></thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>

{cta("想把物業交給我們管理？", "告訴我們物業地址、現況和預計出租日期，我們會先替你評估需要準備甚麼。")}"""
    page("landlords.html", "業主服務：物業出租及管理｜UKPM", "替海外業主出租及管理英國物業：搵代理、審查租客、登記按金、證書提醒、處理租客查詢及維修。", body)


def buying():
    body = f"""{page_hero("買樓及睇樓", "物業買賣 · 遙距睇屋", "未到英國<br>都可以安心買樓", "由代你親身睇樓、安排驗樓，到配對買賣律師及按揭，我們替身在海外的你補上「在場」這一步。", "assets/img/buy.webp", "英國紅磚獨立屋及前花園")}

    <nav class="subnav" aria-label="本頁內容"><div class="wrap"><a href="#viewing">遙距睇屋</a><a href="#calc">收費估算</a><a href="#buy">物業買賣</a></div></nav>

    <section class="section" id="viewing">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">遙距睇屋</p>
          <h2>我們替你到場，你在螢幕前一起看</h2>
          <p>為協助海外人士在英國置業，我們提供收費睇屋服務，明碼實價。</p>
        </div>
        <ol class="steps steps-3">
          <li class="reveal"><span class="step-n">{icon("phone")}</span><h3>聯絡代理安排睇屋</h3><p>代你聯絡物業代理或業主，約好時間。</p></li>
          <li class="reveal"><span class="step-n">{icon("video")}</span><h3>到場視察，可即場視像</h3><p>資深同事親身視察屋內及附近環境，拍照拍片存檔。你可以要求檢視指定位置。</p></li>
          <li class="reveal"><span class="step-n">{icon("doc")}</span><h3>詳細書面報告</h3><p>內外相片、各房間評分及意見、治安指數、超市及交通距離、最近三間中小學距離及評級。</p></li>
        </ol>
      </div>
    </section>

    <section class="section section-tint" id="calc">
      <div class="wrap split-even">
        <div class="reveal">
          <p class="eyebrow">收費</p>
          <h2>每個物業 £15，車程每英里 £1</h2>
          <p>收費按距離計算：由公司出發至物業的來回車程每英里 £1，另加每個物業 £15。我們會盡量安排同一日視察多個物業，替你降低成本。</p>
          <p class="fine">估算只供參考，實際里數以路線為準，請 WhatsApp 我們確認。</p>
        </div>
        <form class="calc reveal" data-viewcalc aria-label="睇屋費用估算">
          <div class="field">
            <label for="vc-miles">來回車程（英里）</label>
            <input id="vc-miles" name="miles" type="number" inputmode="numeric" min="0" max="2000" step="1" value="60">
          </div>
          <div class="field">
            <label for="vc-n">當天物業數目</label>
            <div class="stepper"><button type="button" data-step="-1" aria-label="減少一個">−</button><input id="vc-n" name="n" type="number" inputmode="numeric" min="1" max="10" value="3"><button type="button" data-step="1" aria-label="增加一個">+</button></div>
          </div>
          <div class="calc-out" aria-live="polite">
            <div><small>總費用</small><strong data-total>£105</strong></div>
            <div><small>平均每個物業</small><strong data-each>£35</strong></div>
          </div>
          <p class="calc-formula" data-formula>60 英里 × £1 + 3 個物業 × £15</p>
          <a class="btn btn-wa btn-block" data-viewwa href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}WhatsApp 預約睇屋</a>
        </form>
      </div>
    </section>

    <section class="section" id="buy">
      <div class="wrap split">
        <figure class="split-media reveal"><img src="assets/img/street.webp" alt="英國城市紅磚建築街景" width="1000" height="750" loading="lazy"></figure>
        <div class="split-copy reveal">
          <p class="eyebrow">物業買賣</p>
          <h2>找到心儀物業之後</h2>
          <p>如你已找到你的安樂窩，我們可以替你安排：</p>
          <ul class="why">
            <li>{icon("home")}<div><h3>測量師驗樓</h3><p>由合資格測量師（surveyor）檢查樓宇，確保結構安全。</p></div></li>
            <li>{icon("doc")}<div><h3>買賣律師</h3><p>配對 conveyancing 律師，確保手續順利完成。</p></div></li>
            <li>{icon("pound")}<div><h3>物業貸款</h3><p>按你的收入和身份，搵最合適的按揭方案。<a href="mortgage.html">了解按揭</a></p></div></li>
          </ul>
        </div>
      </div>
    </section>

{cta("有心儀物業想我們去看看？", "把樓盤連結 WhatsApp 給我們，我們會安排睇屋時間並報價。")}"""
    page("buying.html", "買樓及遙距睇屋｜UKPM", "海外買家英國置業：遙距睇屋每個物業 £15 加每英里 £1，附詳細報告；安排測量師驗樓、買賣律師及按揭。", body)


def mortgage():
    q = [
        ("什麼是 DIP（Decision in Principle）？",
         "<p>DIP、AIP（Agreement in Principle）和 MIP（Mortgage in Principle）其實是同一樣東西，即貸款機構根據你提供的資料，以書面初步估計可以借給你多少。不同代理和銀行習慣用不同名稱，我們通常叫 DIP。</p><p>有了 DIP，你就知道自己有資格申請按揭，向賣家出價時也更有說服力。</p>"),
        ("誰需要 DIP？",
         "<p>無論是買第一個物業還是換樓，只要需要按揭，都應該先做 DIP。你出價時，地產代理通常第一樣就會問你要 DIP。它讓你清楚知道可以借多少、買得起甚麼價位。</p>"),
        ("DIP 有效期多久？我一定要接受嗎？",
         "<p>一般有效 60 至 90 日。期間如果情況有變，例如轉工或多了大額債務，要通知貸款機構。</p><p>DIP 沒有約束力，你可以自行決定是否接受。大多數貸款機構在這個階段不會查你的信貸評分，要到下一階段才會查。如你最終不接受貸款，我們的 DIP 服務免費。</p>"),
        ("人在香港，沒有英國簽證，可以做按揭嗎？",
         "<p>可以。英國容許外國人購買本地物業，自住或出租都可以，只是稅款比本地人高。按揭方面可以用香港收入作基礎，文件齊全的話成功機會很高。</p>"),
        ("初到英國，未有收入或剛找到工作，可以做按揭嗎？",
         "<p>可以。未有工作的話，只要有穩定收入來源，例如其他地方的租金收入、股息、長俸，都可以證明供款能力。</p><p>剛找到工作的話，可以用僱傭合約、最少 3 至 6 個月糧單、銀行出糧記錄，以及其他穩定收入作證明。</p>"),
        ("自住物業和出租物業，貸款上有甚麼分別？",
         "<p><strong>自住：</strong>著重個人收入及還款能力。一般最多借到年收入約 4.5 倍，貸款額最高約為樓價 75%，利率較出租物業低。</p><p><strong>出租（Buy-to-let）：</strong>貸款機構視為商業活動，著重物業價值及租金回報，例如租金與供款比例。貸款額一般不超過樓價 60%。業主本身的財政狀況亦會考慮，例如物業暫時租不出時能否繼續供款。</p>"),
        ("我可以借多少？最少要借多少？",
         "<p>收入、年齡、負債、資產、供養人數都會影響貸款額，最終以銀行批核為準。英國亦有類似香港的壓力測試。可以先用上面的估算工具了解大概範圍，再找我們做正式評估，以免交易時大失預算。</p><p>沒有最低貸款額，你可以自由選擇能力範圍內的金額。</p>"),
        ("甚麼算是收入？",
         "<p><strong>薪金收入：</strong>底薪、加班費、佣金等來自僱主的收入。自僱人士需提供報稅記錄、銀行結單等證明。</p><p><strong>被動收入：</strong>租金收入、股息、定期存款利息等穩定的經常性收入。</p>"),
        ("英國有沒有物業不能做按揭？",
         "<p>基本上沒有特定類別一定不能做按揭，但被列為 Grade I / Grade II 的歷史建築會比較困難，甚至不能上會。一般香港人買來自住的物業很少遇到這情況。</p>"),
        ("甚麼是資金來源證明（Proof of Funds）？",
         "<p>這是反洗黑錢（AML）要求的一部分，用來證明你的資金來源合法，由買方律師審核。不同律師的要求略有不同，一般需要準備這筆資金過去約半年的交易記錄。</p>"),
    ]
    body = f"""{page_hero("物業貸款", "物業貸款", "找市場上最優惠<br>最可靠的物業貸款", "自住還是投資都可以。我們與多間按揭中介緊密合作，很多時候比你直接找銀行更優惠。貨比三家，報價免費。", extra=f'''
            <p class="hero-dl"><a href="{LOAN_PDF}" target="_blank" rel="noopener">{icon("download")}下載貸款申請表（PDF）</a></p>''')}

    <section class="section section-tint">
      <div class="wrap split-even">
        <div class="reveal">
          <p class="eyebrow">粗略估算</p>
          <h2>我大概可以借多少？</h2>
          <p>用最基本的方法計算：自住最多借年收入約 4.5 倍，同時不超過樓價 75%；出租物業一般不超過樓價 60%。實際貸款額會受負債、供養人數及壓力測試影響，以銀行批核為準。</p>
          <p class="fine">只供參考，不構成任何貸款建議或批核承諾。</p>
        </div>
        <form class="calc reveal" data-loancalc aria-label="貸款額估算">
          <fieldset class="seg">
            <legend>物業用途</legend>
            <label><input type="radio" name="use" value="own" checked><span>自住</span></label>
            <label><input type="radio" name="use" value="btl"><span>出租</span></label>
          </fieldset>
          <div class="field">
            <label for="lc-price">物業售價（£）</label>
            <input id="lc-price" name="price" type="number" inputmode="numeric" min="0" step="1000" value="250000">
          </div>
          <div class="field" data-income-field>
            <label for="lc-income">家庭年收入（£）</label>
            <input id="lc-income" name="income" type="number" inputmode="numeric" min="0" step="1000" value="45000">
          </div>
          <div class="calc-out" aria-live="polite">
            <div><small>估計最高貸款</small><strong data-loan>£187,500</strong></div>
            <div><small>最少首期</small><strong data-deposit>£62,500</strong></div>
          </div>
          <p class="calc-formula" data-basis>以樓價 75% 計算</p>
          <a class="btn btn-wa btn-block" href="https://wa.me/{WA}" target="_blank" rel="noopener">{icon("wa")}找貸款專員做 DIP</a>
        </form>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">如何取得 DIP</p>
          <h2>三步了解你在英國的貸款能力</h2>
        </div>
        <ol class="steps steps-3">
          <li class="reveal"><span class="step-n">1</span><h3>填妥申請表</h3><p>讓貸款專員了解你的財政狀況，作初步審核。<a href="{LOAN_PDF}" target="_blank" rel="noopener">下載申請表</a></p></li>
          <li class="reveal"><span class="step-n">2</span><h3>與顧問通電話</h3><p>Mortgage Advisor 最少與你通一次電話，詳細解釋並協助你揀最合適的方案。</p></li>
          <li class="reveal"><span class="step-n">3</span><h3>等待銀行批核</h3><p>DIP 沒有約束力，批核後你可以自行決定是否接受。</p></li>
        </ol>
      </div>
    </section>

    <section class="section section-tint" id="faq">
      <div class="wrap faq-wrap">
        <div class="section-head">
          <p class="eyebrow">按揭問答</p>
          <h2>香港買家最常問的問題</h2>
          <p>問題不在這裡？<a href="https://wa.me/{WA}" target="_blank" rel="noopener">直接 WhatsApp 問我們</a></p>
        </div>
        {faq(q, True)}
      </div>
    </section>

{cta("已試過被拒？讓我們再看看", "未有英國信貸記錄、身在海外或收入來源較複雜，都可以先找我們的貸款專員評估。")}"""
    page("mortgage.html", "物業貸款及按揭問答｜UKPM", "專為非英籍、身在海外或未有英國信貸記錄人士安排英國物業按揭。DIP 解說、貸款額估算及常見問題。", body)


def home_services():
    ins = [
        ("自住樓宇", ["建築保險 Buildings Insurance", "財物保險 Contents Insurance"]),
        ("出租樓宇", ["建築保險 Buildings Insurance", "業主保險 Landlord Insurance", "租金保險 Rental Income"]),
        ("商業", ["建築保險 Buildings Insurance", "生意保險 Business Insurance（僱主責任、公眾及產品責任）", "公司汽車保險 Company Car Insurance"]),
    ]
    ins_cards = "\n".join(f"""          <article class="ins reveal"><h3>{t}</h3>{checklist(items, "checks checks-sm")}</article>""" for t, items in ins)
    body = f"""{page_hero("保險 · 水電煤 · 裝修", "家居服務", "保險、水電煤、裝修<br>一個 WhatsApp 搞掂", "新屋入伙、出租前執修、續保比價，這些瑣碎但重要的事，都可以交給同一班人。")}

    <nav class="subnav" aria-label="本頁內容"><div class="wrap"><a href="#insurance">保險服務</a><a href="#utilities">水電煤寬頻</a><a href="#renovation">裝修工程</a></div></nav>

    <section class="section" id="insurance">
      <div class="wrap">
        <div class="section-head">
          <p class="eyebrow">保險服務</p>
          <h2>各類物業保險，免費查詢及報價</h2>
        </div>
        <div class="ins-grid">
{ins_cards}
          <article class="ins ins-accent reveal"><h3>保險索償</h3><p>專業處理保險索償，協助你完成索償所需的程序。</p><a class="btn btn-light btn-sm" href="contact.html">查詢索償</a></article>
        </div>
      </div>
    </section>

    <section class="section section-tint" id="utilities">
      <div class="wrap split-even">
        <div class="reveal">
          <p class="eyebrow">水電煤寬頻</p>
          <h2>煤氣、電力、寬頻、電話，一個賬戶</h2>
          <p>我們推薦 Utility Warehouse（UW）。UW 1996 年成立，提供一站式家居服務，包括煤氣、電力、家居電話、寬頻、手機及保險。</p>
          <p>UW 不賣廣告，把省下的費用回饋客戶，靠口碑招徠。租樓或自置物業都適用。</p>
        </div>
        <div class="panel reveal">
          <h3>一個賬戶包括</h3>
          <ul class="chips"><li>{icon("bolt")}電力</li><li>{icon("home")}煤氣</li><li>{icon("chat")}寬頻</li><li>{icon("phone")}家居電話</li><li>{icon("phone")}手機</li><li>{icon("shield")}家居保險</li></ul>
          {wa_link(label="索取免費報價", cls="btn btn-wa btn-block")}
        </div>
      </div>
    </section>

    <section class="section" id="renovation">
      <div class="wrap split">
        <figure class="split-media reveal"><img src="assets/img/flat.webp" alt="英國現代住宅大廈外觀" width="1000" height="750" loading="lazy"></figure>
        <div class="split-copy reveal">
          <p class="eyebrow">裝修工程 · 專業團隊 誠信可靠</p>
          <h2>別讓裝修把喜事變煩事</h2>
          <p>好不容易找到理想的家，裝修卻可能帶來無數煩惱。我們的團隊由專業香港師傅及本地英國裝修工人組成，無論大小工程，都可以給你最專業的意見。</p>
          {checklist(["出租前執修及翻新", "廚房、浴室、地板及油漆", "工程報價、跟進及進度匯報"])}
          <div class="btn-row"><a class="btn btn-primary" href="contact.html">聯絡報價 {icon("arrow")}</a></div>
        </div>
      </div>
    </section>

{cta()}"""
    page("home-services.html", "保險、水電煤及裝修｜UKPM", "英國自住、出租及商業物業保險，Utility Warehouse 水電煤寬頻一個賬戶，香港師傅加本地團隊裝修工程。", body)


def contact():
    opts = ["物業出租", "物業管理", "物業買賣", "遙距睇屋", "物業貸款", "保險服務", "水電煤寬頻", "裝修工程"]
    chips = "\n".join(f'              <label class="chip-check"><input type="checkbox" name="service" value="{o}"><span>{o}</span></label>' for o in opts)
    body = f"""    <section class="page-hero">
      <div class="wrap">
        {crumbs("聯絡我們")}
        <div class="contact-grid">
          <div>
            <p class="eyebrow">聯絡我們</p>
            <h1>有任何查詢<br>WhatsApp 最快</h1>
            <p class="lead">ONLINE PROPERTY MANAGEMENT，你的英國物業專家。歡迎隨時經 WhatsApp 或查詢表聯絡，我們會盡快以廣東話回覆。</p>
            <ul class="contact-list">
              <li><span class="ci ci-wa">{icon("wa")}</span><div><small>WhatsApp / 電話</small><a href="https://wa.me/{WA}" target="_blank" rel="noopener">{PHONE}</a></div></li>
              <li><span class="ci">{icon("fb")}</span><div><small>Facebook</small><a href="{FB}" target="_blank" rel="noopener">Online Property Management</a></div></li>
              <li><span class="ci">{icon("shield")}</span><div><small>Property Redress Scheme</small><span>{PRS_NO}</span></div></li>
            </ul>
          </div>
          <form class="enquiry" data-enquiry data-wa="{WA}">
            <h2>查詢表</h2>
            <p class="form-note">填好後按「用 WhatsApp 發送」，內容會自動整理成訊息，不經任何伺服器。</p>
            <fieldset>
              <legend>想查詢的服務（可多選）</legend>
              <div class="chip-group">
{chips}
              </div>
            </fieldset>
            <div class="field-row">
              <div class="field"><label for="f-name">你的名字</label><input id="f-name" name="name" autocomplete="name" required></div>
              <div class="field"><label for="f-area">物業所在地區</label><input id="f-area" name="area" placeholder="例如 Manchester、未決定"></div>
            </div>
            <div class="field"><label for="f-where">你現在身在</label>
              <select id="f-where" name="where"><option>香港</option><option>英國</option><option>其他地方</option></select>
            </div>
            <div class="field"><label for="f-msg">想問甚麼（選填）</label><textarea id="f-msg" name="message" rows="4"></textarea></div>
            <button class="btn btn-wa btn-block btn-lg" type="submit">{icon("wa")}用 WhatsApp 發送</button>
          </form>
        </div>
      </div>
    </section>"""
    page("contact.html", "聯絡我們｜UKPM Property Management", "經 WhatsApp +44 7459 845827 或網上查詢表聯絡 UKPM，以廣東話回覆英國物業查詢。", body)


if __name__ == "__main__":
    index()
    about()
    landlords()
    buying()
    mortgage()
    home_services()
    contact()
