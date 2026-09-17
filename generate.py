# -*- coding: utf-8 -*-
"""
Static site generator for Lari Creative Studio.
Run: python3 generate.py
Outputs a fully-linked multi-page static site into ./site
"""
import os
import html
from data import (
    BRAND, SERVICES, SERVICES_BY_SLUG, BUNDLES, RETAINER_TERMS, PREMIUM_OPTIONS,
    COURSES, COURSES_BY_SLUG, GUIDE_BUNDLES, WORK_PROJECTS, WORK_BY_SLUG,
    JOURNAL_ARTICLES, JOURNAL_BY_SLUG, FAQS, ACADEMY_FAQS,
    KEY_DIFFERENTIATORS, FIVE_YEAR_ROADMAP, FOUNDER,
)

OUT = os.path.join(os.path.dirname(__file__), "site")


def w(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def R(depth):
    """Root-relative prefix for a page `depth` directories deep."""
    return "../" * depth


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------

def logo_img(r, size=34):
    return f'<img class="brand-mark" src="{r}assets/img/logo-mark.png" alt="Lari Creative Studio monogram" width="{size}" height="{size}" style="width:{size}px; height:{size}px; border-radius:50%;">'


def ph_block(ratio="4x3", label="Photography placeholder"):
    return f'<div class="ph-block ph-{ratio}"><span class="ph-block-label">{esc(label)}</span></div>'


NAV_ITEMS_SIMPLE = [
    ("work/", "Work"),
    ("pricing/", "Pricing"),
    ("about/", "About"),
    ("journal/", "Journal"),
    ("contact/", "Contact"),
]


def build_nav(depth, active=""):
    r = R(depth)
    services_links = "\n".join(
        f'<li><a href="{r}services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES
    )
    li = []
    li.append(f'<li class="{"is-active" if active=="home" else ""}"><a class="nav-link" href="{r}index.html">Home</a></li>')
    li.append(f'<li class="{"is-active" if active=="work" else ""}"><a class="nav-link" href="{r}work/">Work</a></li>')
    li.append(f'''<li class="has-dropdown {"is-active" if active=="services" else ""}">
      <a class="nav-link" href="{r}services/">Services</a>
      <ul class="dropdown">
        {services_links}
        <li><a class="dropdown-all" href="{r}services/">All Services &amp; Pricing</a></li>
      </ul>
    </li>''')
    li.append(f'<li class="{"is-active" if active=="pricing" else ""}"><a class="nav-link" href="{r}pricing/">Pricing</a></li>')
    li.append(f'''<li class="has-dropdown {"is-active" if active=="academy" else ""}">
      <a class="nav-link" href="{r}academy/">Academy</a>
      <ul class="dropdown">
        <li><a href="{r}academy/">Browse Courses</a></li>
        <li><a href="{r}academy/register/">Register</a></li>
        <li><a href="{r}academy/signin/">Sign In</a></li>
        <li><a class="dropdown-all" href="{r}academy/dashboard/">Student Dashboard</a></li>
      </ul>
    </li>''')
    li.append(f'<li class="{"is-active" if active=="about" else ""}"><a class="nav-link" href="{r}about/">About</a></li>')
    li.append(f'<li class="{"is-active" if active=="journal" else ""}"><a class="nav-link" href="{r}journal/">Journal</a></li>')
    li.append(f'<li class="{"is-active" if active=="contact" else ""}"><a class="nav-link" href="{r}contact/">Contact</a></li>')
    return "\n".join(li)


def build_mobile_nav(depth):
    r = R(depth)
    services_links = "\n".join(
        f'<li><a href="{r}services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES
    )
    return f'''
    <a href="{r}index.html">Home</a>
    <a href="{r}work/">Work</a>
    <a href="{r}services/">Services</a>
    <ul class="mobile-sub">{services_links}</ul>
    <a href="{r}pricing/">Pricing</a>
    <a href="{r}academy/">Academy</a>
    <ul class="mobile-sub">
      <li><a href="{r}academy/register/">Register</a></li>
      <li><a href="{r}academy/signin/">Sign In</a></li>
      <li><a href="{r}academy/dashboard/">Student Dashboard</a></li>
    </ul>
    <a href="{r}about/">About</a>
    <a href="{r}journal/">Journal</a>
    <a href="{r}contact/">Contact</a>
    '''


def build_footer(depth):
    r = R(depth)
    services_col = "\n".join(f'<li><a href="{r}services/{s["slug"]}/">{esc(s["name"])}</a></li>' for s in SERVICES[:7])
    return f'''
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col footer-brand">
          <div class="brand" style="margin-bottom:18px;">
            {logo_img(r, 30)}
            <span class="brand-word">Lari<br><small>Creative Studio</small></span>
          </div>
          <p style="max-width:280px;">{esc(BRAND["positioning"])}</p>
          <p style="max-width:280px;">"{esc(BRAND["tagline"])}"</p>
        </div>
        <div class="footer-col">
          <h5>Explore</h5>
          <ul>
            <li><a href="{r}work/">Work</a></li>
            <li><a href="{r}services/">Services</a></li>
            <li><a href="{r}pricing/">Pricing</a></li>
            <li><a href="{r}academy/">Academy</a></li>
            <li><a href="{r}about/">About</a></li>
            <li><a href="{r}journal/">Journal</a></li>
            <li><a href="{r}contact/">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Services</h5>
          <ul>{services_col}</ul>
        </div>
        <div class="footer-col">
          <h5>Connect</h5>
          <ul>
            <li><a href="{esc(BRAND['instagram'])}">Instagram</a></li>
            <li><a href="{esc(BRAND['linkedin'])}">LinkedIn</a></li>
            <li><a href="{esc(BRAND['facebook'])}">Facebook</a></li>
            <li><a href="{esc(BRAND['youtube'])}">YouTube</a></li>
            <li><a href="{esc(BRAND['whatsapp_link'])}">WhatsApp</a></li>
            <li><a href="mailto:{esc(BRAND['email'])}">{esc(BRAND['email'])}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 {esc(BRAND["name"])}. All rights reserved.</span>
        <div class="footer-legal">
          <a href="{r}privacy/">Privacy Policy</a>
          <a href="{r}terms/">Terms &amp; Conditions</a>
          <a href="{r}client-gallery/">Client Gallery</a>
          <a href="{r}faq/">FAQ</a>
        </div>
      </div>
    </div>
  </footer>'''


def page(title, description, depth, body, active="", body_class="", extra_head=""):
    r = R(depth)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)} | {esc(BRAND["name"])}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="https://www.laricreativestudio.com/{'' if depth==0 else ''}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(BRAND['name'])}">
<link rel="icon" href="{r}assets/img/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
{extra_head}
</head>
<body class="{body_class}" data-root-prefix="{r}">
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{r}index.html" aria-label="{esc(BRAND['name'])} home">
      {logo_img(r)}
      <span class="brand-word">Lari<br><small>Creative Studio</small></span>
    </a>
    <ul class="nav-desktop">
      {build_nav(depth, active)}
    </ul>
    <a class="btn btn-primary nav-cta" href="{r}contact/">Start a Project</a>
    <button class="nav-toggle" aria-label="Open menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg></button>
  </div>
</header>

<div class="mobile-menu">
  <div class="mobile-menu-top">
    <a class="brand" href="{r}index.html">{logo_img(r, 28)}<span class="brand-word">Lari</span></a>
    <button class="mobile-menu-close" aria-label="Close menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></button>
  </div>
  <nav class="mobile-nav">{build_mobile_nav(depth)}</nav>
  <div class="mobile-menu-cta"><a class="btn btn-primary btn-block" href="{r}contact/">Start a Project</a></div>
</div>

<main id="main">
{body}
</main>
{build_footer(depth)}
<script src="{r}assets/js/main.js"></script>
</body>
</html>'''


def breadcrumb(depth, trail):
    """trail: list of (label, root_relative_path_or_None)"""
    r = R(depth)
    parts = []
    for label, path in trail:
        if path:
            parts.append(f'<a href="{r}{path}">{esc(label)}</a>')
        else:
            parts.append(esc(label))
    return f'<div class="breadcrumb">{" <span>/</span> ".join(parts)}</div>'


def buy_button(item_type, slug, title, price, label, classes="btn btn-primary"):
    return (
        f'<button type="button" class="{classes}" data-buy-type="{esc(item_type)}" '
        f'data-buy-slug="{esc(slug)}" data-buy-title="{esc(title)}" '
        f'data-buy-ngn="{esc(price["ngn"])}" data-buy-usd="{esc(price["usd"])}" '
        f'data-buy-gbp="{esc(price["gbp"])}" data-buy-eur="{esc(price["eur"])}">{esc(label)}</button>'
    )


def payment_modal_html():
    return '''
    <div class="payment-modal" aria-hidden="true">
      <div class="payment-modal-inner">
        <button class="payment-modal-close" type="button" aria-label="Close">&times;</button>
        <span class="eyebrow">Checkout — Demo</span>
        <h3 data-pm-title style="margin-bottom:6px;">Item</h3>
        <p class="form-note" style="margin-bottom:20px;">One-time payment — access unlocks immediately after payment is confirmed.</p>
        <div class="field" style="margin-bottom:18px;">
          <label for="pm-currency">Pay in</label>
          <select id="pm-currency" data-pm-currency>
            <option value="ngn">Nigerian Naira (NGN)</option>
            <option value="usd">US Dollar (USD)</option>
            <option value="gbp">British Pound (GBP)</option>
            <option value="eur">Euro (EUR)</option>
          </select>
        </div>
        <div class="payment-item-price" data-pm-amount style="margin-bottom:22px;">—</div>
        <button class="btn btn-primary btn-block" type="button" data-pm-confirm>Pay Now (Demo)</button>
        <p class="form-note" style="margin-top:16px;">Demo checkout only — no real charge is made. A production build would connect this to a payment processor supporting Naira, USD, GBP and EUR (e.g. Paystack or Flutterwave for local cards, Stripe for international).</p>
      </div>
    </div>'''


def section_head(eyebrow, heading, lede=None, center=False):
    cls = "section-head center" if center else "section-head"
    lede_html = f'<p class="lede">{esc(lede)}</p>' if lede else ""
    return f'<div class="{cls}"><span class="eyebrow">{esc(eyebrow)}</span><h2>{esc(heading)}</h2>{lede_html}</div>'


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------

def build_home():
    depth = 0
    r = R(depth)

    hero = f'''
    <section class="hero">
      <div class="hero-media">{ph_block("21x9", "Hero — architectural exterior at dusk, Lagos")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        <span class="eyebrow">{esc(BRAND["positioning"])}</span>
        <h1>We build brands.<br>We design experiences.<br>We drive growth.</h1>
        <p class="hero-sub">A full-service creative studio in Lagos working across branding, web, photography, video, marketing, consulting, AI automation and training — for ambitious businesses everywhere.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="{r}work/">Explore Our Work</a>
          <a class="btn btn-outline" href="{r}contact/">Start a Project</a>
        </div>
      </div>
    </section>'''

    intro = f'''
    <section>
      <div class="container split">
        <div class="split-copy">
          {section_head("Lari Creative Studio", "One studio, ten disciplines, a single standard.")}
          <p>Most businesses juggle a designer, a developer, a photographer and a marketer who've never spoken to each other. We built Lari to close that gap — strategy, design, technology and storytelling under one roof, so the brand, the site and the content all pull in the same direction.</p>
          <p>Every engagement runs through the same three-tier structure — Essential, Professional, Enterprise — so a first-time founder and an enterprise client are held to the same standard of craft, just at different scale.</p>
          <a class="btn btn-ghost" href="{r}about/">About the Studio</a>
        </div>
        <div class="split-media">{ph_block("4x3", "Studio workspace, design review in progress")}</div>
      </div>
    </section>'''

    # Services grid (all 10)
    cards = []
    for i, s in enumerate(SERVICES, start=1):
        cards.append(f'''
        <a class="service-card" href="{r}services/{s["slug"]}/">
          <div>{ph_block("3x2", s["name"] + " — representative work")}</div>
          <div class="service-card-body">
            <div class="service-card-num">0{i}</div>
            <h3>{esc(s["name"])}</h3>
            <p>{esc(s["short"])}</p>
            <span class="service-card-link">Explore service</span>
          </div>
        </a>''')
    services_section = f'''
    <section class="on-ivory-dim">
      <div class="container">
        <div class="section-head-row">
          {section_head("What We Do", "Ten disciplines. One accountable team.")}
          <a class="btn btn-ghost" href="{r}services/">View All Services</a>
        </div>
        <div class="card-grid cols-4">{"".join(cards)}</div>
      </div>
    </section>'''

    # Featured work (asymmetric)
    featured_slugs = ["dusk-crowds-beneath-the-footbridge", "geometry-of-the-city", "the-new-terminal", "new-collection-still-life", "shine-on-stage", "market-hours"]
    work_cards = []
    for slug in featured_slugs:
        p = WORK_BY_SLUG[slug]
        ratio = {"feature": "16x9", "portrait": "3x4", "landscape": "16x9", "small": "4x3", "full": "21x9"}.get(p["size"], "4x3")
        work_cards.append(f'''
        <div class="work-card size-{p['size']}">
          <a href="{r}work/{p['slug']}/">
            {ph_block(ratio, p['title'] + " — " + p['category'])}
            <div class="work-card-overlay">
              <span class="work-card-cat">{esc(p['category'])}</span>
              <span class="work-card-title">{esc(p['title'])}</span>
              <span class="work-card-meta">{esc(p['location'])} · {esc(p['year'])}</span>
            </div>
          </a>
        </div>''')
    work_section = f'''
    <section>
      <div class="container">
        <div class="section-head-row">
          {section_head("Selected Work", "A considered collection of moments, stories and visual perspectives.")}
          <a class="btn btn-ghost" href="{r}work/">View All Work</a>
        </div>
        <div class="work-grid">{"".join(work_cards)}</div>
      </div>
    </section>'''

    statement = f'''
    <section class="on-dark" style="padding:0;">
      <div style="position:relative;">
        {ph_block("21x9", "Full-width cinematic statement image")}
        <div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; text-align:center; background:rgba(7,22,36,0.45);">
          <div style="max-width:640px; padding:24px;">
            <h2 style="color:var(--ivory);">Every project has a story.</h2>
            <p class="lede" style="margin:0 auto;">We build with intention — balancing strategy, craft and follow-through, across every discipline we practise.</p>
          </div>
        </div>
      </div>
    </section>'''

    steps = [
        ("Discover", "Understand the business, the audience and the objective — whatever the discipline."),
        ("Plan", "Develop the strategy, scope and creative direction before any work begins."),
        ("Create", "Execute with deliberate attention to craft, whether that's a logo, a shoot or a workflow."),
        ("Deliver", "Ship polished, client-ready work, with training and support built in."),
    ]
    step_html = "".join(f'<div class="step"><div class="step-num">0{i}</div><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(steps, 1))
    approach = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("The Lari Approach", "From brief to brand.")}
        <div class="steps">{step_html}</div>
      </div>
    </section>'''

    trust = f'''
    <section>
      <div class="container text-center">
        {section_head("Trusted Across Industries", "Working with startups, corporations, NGOs and government agencies.", center=True)}
        <p class="lede" style="margin:0 auto;">Our tiered structure serves freelancers and churches at the Essential level up to banks, universities and government agencies at the Enterprise level — without diluting the standard of work.</p>
      </div>
    </section>'''

    academy_promo = f'''
    <section class="on-dark">
      <div class="container split">
        <div class="split-copy">
          {section_head("Lari Academy", "Learn the exact process we use with clients.")}
          <p>Self-paced courses across every service we offer — branding, web design, UI/UX, photography, video, social content, marketing, consulting, AI automation and running your own workshops.</p>
          <a class="btn btn-primary" href="{r}academy/">Explore the Academy</a>
        </div>
        <div class="split-media">{ph_block("4x3", "Student working through an Academy course")}</div>
      </div>
    </section>'''

    journal_cards = "".join(_journal_card(a, r) for a in JOURNAL_ARTICLES[:3])
    journal_section = f'''
    <section>
      <div class="container">
        <div class="section-head-row">
          {section_head("From the Journal", "Ideas on brand, design and growth.")}
          <a class="btn btn-ghost" href="{r}journal/">Read the Journal</a>
        </div>
        <div class="card-grid">{journal_cards}</div>
      </div>
    </section>'''

    final_cta = f'''
    <section class="cta-band">
      <div class="container">
        <span class="eyebrow">Start a Project</span>
        <h2>Let's build something worth remembering.</h2>
        <p class="lede">Tell us about your business, your brand, or the story you need told.</p>
        <div class="hero-ctas"><a class="btn btn-primary" href="{r}contact/">Start a Project</a><a class="btn btn-outline" href="{r}pricing/">View Pricing</a></div>
      </div>
    </section>'''

    body = hero + intro + services_section + work_section + statement + approach + trust + academy_promo + journal_section + final_cta
    w("index.html", page(
        "Building Brands, Experiences & Growth",
        "Lari Creative Studio is a full-service creative agency in Lagos — branding, web design, photography, video, marketing, consulting, AI automation and training.",
        depth, body, active="home",
    ))


def _journal_card(a, r):
    return f'''
    <a class="article-card" href="{r}journal/{a['slug']}/">
      {ph_block("4x3", a['title'])}
      <span class="article-cat">{esc(a['category'])}</span>
      <h3>{esc(a['title'])}</h3>
      <p class="article-excerpt">{esc(a['excerpt'])}</p>
      <div class="article-meta">{esc(a['date'])} · {esc(a['read_time'])}</div>
    </a>'''


# ---------------------------------------------------------------------------
# SERVICES
# ---------------------------------------------------------------------------

def build_services_index():
    depth = 1
    r = R(depth)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "Services hero — studio at work")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Services", None)])}
        <span class="eyebrow">What We Do</span>
        <h1>Services</h1>
        <p class="hero-sub">Ten disciplines, each run through the same three-tier structure — Essential, Professional, Enterprise — so you invest at exactly the level your business needs.</p>
      </div>
    </section>'''
    cards = []
    for i, s in enumerate(SERVICES, 1):
        cards.append(f'''
        <a class="service-card" href="{r}services/{s['slug']}/">
          <div>{ph_block("3x2", s['name'])}</div>
          <div class="service-card-body">
            <div class="service-card-num">0{i}</div>
            <h3>{esc(s['name'])}</h3>
            <p>{esc(s['short'])}</p>
            <span class="service-card-link">View pricing &amp; details</span>
          </div>
        </a>''')
    grid = f'<section><div class="container"><div class="card-grid cols-4">{"".join(cards)}</div></div></section>'
    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Not sure which service fits?</h2>
        <p class="lede">Every project starts with a free discovery call — we'll recommend the right service and tier.</p>
        <div class="hero-ctas"><a class="btn btn-primary" href="{r}contact/">Book a Discovery Call</a><a class="btn btn-outline" href="{r}pricing/">See Bundles &amp; Pricing</a></div>
      </div>
    </section>'''
    w("services/index.html", page(
        "Services", "All ten Lari Creative Studio service lines — branding, web, UI/UX, photography, video, social, marketing, consulting, AI automation and training.",
        depth, hero + grid + cta, active="services",
    ))


def build_service_detail(s):
    depth = 2
    r = R(depth)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", s['name'] + " — hero image")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Services", "services/"), (s['name'], None)])}
        <span class="eyebrow">Service</span>
        <h1>{esc(s['name'])}</h1>
        <p class="hero-sub">{esc(s['hero_desc'])}</p>
        <div class="hero-ctas"><a class="btn btn-primary" href="{r}contact/?service={s['slug']}">Request a Quote</a></div>
      </div>
    </section>'''

    intro = f'''
    <section>
      <div class="container split">
        <div class="split-copy">
          {section_head("Why it matters", "Why " + s['name'].lower() + " matters")}
          <p>{esc(s['why'])}</p>
          <h4 style="margin-top:28px;">Ideal for</h4>
          <ul style="display:flex; flex-direction:column; gap:10px; margin-top:14px;">
            {"".join(f'<li style="padding-bottom:10px; border-bottom:1px solid var(--line-on-light);">— {esc(x)}</li>' for x in s['ideal_for'])}
          </ul>
        </div>
        <div class="split-media">{ph_block("4x3", s['name'] + " in progress")}</div>
      </div>
    </section>'''

    step_html = "".join(f'<div class="step"><div class="step-num">0{i}</div><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(s['process'], 1))
    process = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("Our Process", "How we deliver " + s['name'].lower())}
        <div class="steps">{step_html}</div>
      </div>
    </section>'''

    tiers_html = []
    for i, t in enumerate(s["tiers"]):
        featured = " is-featured" if i == 1 else ""
        price_intl = f'<div class="tier-ideal">International: {esc(t["price_intl"])}</div>' if t.get("price_intl") else ""
        tiers_html.append(f'''
        <div class="tier{featured}">
          <div class="tier-name">{esc(t['name'])}</div>
          <div class="tier-price">{esc(t['price'])}</div>
          {price_intl}
          <div class="tier-ideal">Ideal for: {esc(t['ideal'])}</div>
          <ul>{"".join(f'<li>{esc(x)}</li>' for x in t['includes'])}</ul>
          <a class="btn {"btn-primary" if i==1 else "btn-ghost"} btn-block" href="{r}contact/?service={s['slug']}&amp;tier={t['name'].lower()}">Request {esc(t['name'])} Quote</a>
        </div>''')
    pricing = f'''
    <section id="pricing">
      <div class="container">
        {section_head("Pricing", s['name'] + " — three tiers", "All prices are starting points; every project begins with a free discovery call to confirm an exact quote.")}
        <div class="tier-grid">{"".join(tiers_html)}</div>
      </div>
    </section>'''

    addons_html = ""
    if s.get("addons"):
        rows = "".join(f'<tr><td>{esc(n)}</td><td>{esc(p)}</td></tr>' for n, p in s["addons"])
        addons_html = f'''
        <section class="on-ivory-dim">
          <div class="container">
            {section_head("Optional Add-ons", "Extend any package")}
            <table class="pricing-table"><thead><tr><th>Add-on</th><th>Price</th></tr></thead><tbody>{rows}</tbody></table>
          </div>
        </section>'''

    retainer_html = ""
    if s.get("retainer"):
        rows = "".join(f'<li>{esc(t)}</li>' for t in RETAINER_TERMS)
        retainer_html = f'''
        <section>
          <div class="container">
            {section_head("Retainer Terms", "How the monthly engagement works")}
            <ul style="display:flex; flex-direction:column; gap:12px; max-width:720px;">{"".join(f'<li style="padding-bottom:12px; border-bottom:1px solid var(--line-on-light);">— {esc(t)}</li>' for t in RETAINER_TERMS)}</ul>
          </div>
        </section>'''

    retainer_plans_html = ""
    if s.get("retainer_plans"):
        rows = "".join(f'<tr><td>{esc(n)}</td><td>{esc(ng)}</td><td>{esc(us)}</td></tr>' for n, ng, us in s["retainer_plans"])
        retainer_plans_html = f'''
        <section class="on-ivory-dim">
          <div class="container">
            {section_head("Post-Implementation Support Plans", "Ongoing AI retainer plans")}
            <table class="pricing-table"><thead><tr><th>Plan</th><th>Nigeria</th><th>International</th></tr></thead><tbody>{rows}</tbody></table>
          </div>
        </section>'''

    gallery_html = ""
    if s.get("gallery_projects"):
        cards = []
        for slug in s["gallery_projects"]:
            p = WORK_BY_SLUG.get(slug)
            if not p:
                continue
            cards.append(f'''<a class="work-card size-portrait" href="{r}work/{p['slug']}/">
              {ph_block("3x4", p['title'])}
              <div class="work-card-overlay"><span class="work-card-cat">{esc(p['category'])}</span><span class="work-card-title">{esc(p['title'])}</span></div>
            </a>''')
        gallery_html = f'''
        <section>
          <div class="container">
            {section_head("Related Work", "See it in practice")}
            <div class="work-grid">{"".join(cards)}</div>
          </div>
        </section>'''

    faq_items = "".join(f'''
        <div class="faq-item">
          <button class="faq-q"><span>{esc(q)}</span><span class="faq-icon">+</span></button>
          <div class="faq-a"><div class="faq-a-inner">{esc(a2)}</div></div>
        </div>''' for q, a2 in FAQS[:4])
    faq = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("Frequently Asked", "Common questions")}
        <div class="faq-list">{faq_items}</div>
      </div>
    </section>'''

    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Ready to start your {esc(s['name'].lower())} project?</h2>
        <p class="lede">Book a free discovery call and we'll recommend the right tier for your budget and timeline.</p>
        <div class="hero-ctas"><a class="btn btn-primary" href="{r}contact/?service={s['slug']}">Request a Quote</a></div>
      </div>
    </section>'''

    body = hero + intro + process + pricing + addons_html + retainer_html + retainer_plans_html + gallery_html + faq + cta
    w(f"services/{s['slug']}/index.html", page(
        s['name'], s['short'], depth, body, active="services",
    ))


# ---------------------------------------------------------------------------
# PRICING (bundles + full overview)
# ---------------------------------------------------------------------------

def build_pricing():
    depth = 1
    r = R(depth)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "Pricing hero")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Pricing", None)])}
        <span class="eyebrow">Investment</span>
        <h1>Pricing &amp; Bundles</h1>
        <p class="hero-sub">Every service runs through the same three-tier structure. Combine services for a bundle discount, or book a free discovery call for an exact quote.</p>
      </div>
    </section>'''

    rows = ""
    for s in SERVICES:
        e = s["tiers"][0]["price"]
        p = s["tiers"][1]["price"]
        ent = s["tiers"][2]["price"]
        rows += f'<tr><td><a href="{r}services/{s["slug"]}/">{esc(s["name"])}</a></td><td>{esc(e)}</td><td>{esc(p)}</td><td>{esc(ent)}</td></tr>'
    overview = f'''
    <section>
      <div class="container">
        {section_head("Quick Reference", "Starting prices by service")}
        <div style="overflow-x:auto;">
        <table class="pricing-table">
          <thead><tr><th>Service</th><th>Essential</th><th>Professional</th><th>Enterprise</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>
        </div>
        <p class="form-note">All figures from the 2026 Service Catalogue &amp; Pricing Guide (v02). Prices are starting points — final quote after a free discovery call.</p>
      </div>
    </section>'''

    bundle_cards = "".join(f'''
      <div class="bundle-card">
        <div class="bundle-name">{esc(b['name'])}</div>
        <p>{esc(b['combo'])}</p>
        <span class="bundle-discount">{esc(b['discount'])}</span>
      </div>''' for b in BUNDLES)
    bundles = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("Multi-Service Bundles", "Combine services, save on the combined price")}
        <div class="bundle-grid">{bundle_cards}</div>
      </div>
    </section>'''

    retainer_items = "".join(f'<li style="padding-bottom:12px; border-bottom:1px solid var(--line-on-light);">— {esc(t)}</li>' for t in RETAINER_TERMS)
    premium_rows = "".join(f'<tr><td>{esc(n)}</td><td>{esc(p)}</td></tr>' for n, p in PREMIUM_OPTIONS)
    terms_section = f'''
    <section>
      <div class="container split">
        <div class="split-copy">
          {section_head("Retainer Commitment Terms", "For social media, marketing & consulting retainers")}
          <ul style="display:flex; flex-direction:column; gap:12px;">{retainer_items}</ul>
        </div>
        <div class="split-media">
          {section_head("Premium Service Options", "For speed and dedicated support")}
          <table class="pricing-table"><tbody>{premium_rows}</tbody></table>
        </div>
      </div>
    </section>'''

    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Need something tailored?</h2>
        <p class="lede">Every organisation has unique goals — contact us for a customised proposal.</p>
        <a class="btn btn-primary" href="{r}contact/">Start a Project</a>
      </div>
    </section>'''

    body = hero + overview + bundles + terms_section + cta
    w("pricing/index.html", page(
        "Pricing & Bundles", "Full pricing reference for every Lari Creative Studio service, plus multi-service bundle discounts and retainer terms.",
        depth, body, active="pricing",
    ))


# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------

def build_about():
    depth = 1
    r = R(depth)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "About hero — founder / studio portrait")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("About", None)])}
        <span class="eyebrow">About</span>
        <h1>About Lari Creative Studio</h1>
        <p class="hero-sub">Creative thinking. Visual storytelling. Digital possibility.</p>
      </div>
    </section>'''

    who = f'''
    <section>
      <div class="container split">
        <div class="split-copy">
          {section_head("Who We Are", "A multidisciplinary creative, digital and technology studio")}
          <p>Lari Creative Studio is a full-service creative agency based in Lagos, working with startups, growing companies, corporations and government agencies across Nigeria, West Africa and internationally.</p>
          <p>We combine strategy, design, technology and storytelling across ten service lines — brand identity, web design, UI/UX, photography, videography, social content, digital marketing, business consulting, AI automation and training. Photography and visual storytelling are one part of a broader creative capability, not the whole of it.</p>
        </div>
        <div class="split-media">{ph_block("4x3", "Studio team at work")}</div>
      </div>
    </section>'''

    philosophy = f'''
    <section class="on-ivory-dim">
      <div class="container split reverse">
        <div class="split-media">{ph_block("4x3", "Design process — sketches and reviews")}</div>
        <div class="split-copy">
          {section_head("Our Philosophy", "A logo isn't a brand.")}
          <p>Great design should grow businesses, not just decorate them. We tie every creative decision — a colour, a layout, a shot — back to a business outcome, and we say so plainly rather than dressing it up in jargon.</p>
          <p>We sound like a senior creative partner advising a client: confident without arrogance, clear without hype.</p>
        </div>
      </div>
    </section>'''

    values = [
        ("Craft over decoration", "Every deliverable is held to a professional standard, not just a passable one."),
        ("Clarity over jargon", "We explain technical decisions in plain language, and tie creative work to outcomes."),
        ("Consistency over one-offs", "Our tiered structure and documented process mean quality doesn't depend on which day you called."),
        ("Growth over vanity", "We measure success in enquiries, conversions and retained clients — not just how something looks."),
    ]
    values_html = "".join(f'<div class="step"><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for t, d in values)
    values_section = f'''
    <section>
      <div class="container">
        {section_head("Our Values", "What we hold ourselves to")}
        <div class="steps">{values_html}</div>
      </div>
    </section>'''

    methodology = [
        ("Discover", "Understand the business, the audience and the objective."),
        ("Define", "Turn that understanding into a clear brief, scope and strategy."),
        ("Create", "Execute with deliberate attention to craft."),
        ("Deliver", "Ship polished, client-ready work with training and support."),
        ("Grow", "Track results and return with the next stage of the relationship."),
    ]
    method_html = "".join(f'<div class="step"><div class="step-num">0{i}</div><h4>{esc(t)}</h4><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(methodology, 1))
    method_section = f'''
    <section class="on-dark">
      <div class="container">
        {section_head("Our Methodology", "Discover · Define · Create · Deliver · Grow")}
        <div class="steps">{method_html}</div>
      </div>
    </section>'''

    why = f'''
    <section class="on-ivory-dim">
      <div class="container text-center">
        {section_head("Why Clients Work With Us", "Full-service capability, transparent pricing", center=True)}
        <p class="lede" style="margin:0 auto;">One team accountable for the whole chain — strategy, identity, web, content, marketing and increasingly, AI — under a transparent, tiered pricing structure that scales from a first logo to full digital transformation.</p>
      </div>
    </section>'''

    diff_items = "".join(f'<li style="padding-bottom:12px; border-bottom:1px solid var(--line-on-light);">— {esc(d)}</li>' for d in KEY_DIFFERENTIATORS)
    differentiators = f'''
    <section>
      <div class="container split reverse">
        <div class="split-media">{ph_block("4x3", "Studio positioning — strategy session")}</div>
        <div class="split-copy">
          {section_head("Market Position", "A strategic partner, not a low-cost vendor")}
          <p>We compete on value, professionalism and full-service capability rather than price alone — serving freelancers and churches at the Essential level, up to banks, universities and government agencies at the Enterprise level, without diluting our positioning.</p>
          <h4 style="margin-top:24px;">Key Differentiators</h4>
          <ul style="display:flex; flex-direction:column; gap:10px; margin-top:14px;">{diff_items}</ul>
        </div>
      </div>
    </section>'''

    roadmap_html = "".join(
        f'<div class="step"><div class="step-num" style="font-size:28px; letter-spacing:0.04em;">{esc(yr)}</div><h4>{esc(title)}</h4><p>{esc(desc)}</p></div>'
        for yr, title, desc in FIVE_YEAR_ROADMAP
    )
    roadmap = f'''
    <section class="on-dark">
      <div class="container">
        {section_head("Our Roadmap", "The five-year plan")}
        <div class="steps">{roadmap_html}</div>
        <p class="lede" style="margin-top:32px;">A strategic planning tool, not a public commitment — the milestones we're building toward as the studio grows from a project-based practice into a full, education-inclusive ecosystem.</p>
      </div>
    </section>'''

    founder = f'''
    <section class="on-ivory-dim">
      <div class="container split">
        <div class="split-media"><img src="{r}{FOUNDER["photo"]}" alt="{esc(FOUNDER["name"])}, {esc(FOUNDER["title"])} of {esc(BRAND["name"])}" style="width:100%; height:auto; display:block; border:1px solid var(--line-on-light);"></div>
        <div class="split-copy">
          {section_head(FOUNDER["title"], FOUNDER["name"])}
          <p>{esc(FOUNDER["bio"])}</p>
        </div>
      </div>
    </section>'''

    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Let's build something worth remembering.</h2>
        <div class="hero-ctas"><a class="btn btn-primary" href="{r}contact/">Start a Project</a><a class="btn btn-outline" href="{r}work/">See Our Work</a></div>
      </div>
    </section>'''

    body = hero + who + differentiators + philosophy + values_section + method_section + roadmap + founder + why + cta
    w("about/index.html", page(
        "About", "Lari Creative Studio is a multidisciplinary creative, digital and technology studio based in Lagos, Nigeria — working with clients worldwide.",
        depth, body, active="about",
    ))


# ---------------------------------------------------------------------------
# WORK
# ---------------------------------------------------------------------------

def build_work_index():
    depth = 1
    r = R(depth)
    categories = sorted(set(s for p in WORK_PROJECTS for s in p["services"]))
    filter_btns = '<button class="filter-btn is-active" data-filter="all">All</button>' + "".join(
        f'<button class="filter-btn" data-filter="{c}">{esc(SERVICES_BY_SLUG[c]["name"])}</button>' for c in categories
    )
    cards = []
    for p in WORK_PROJECTS:
        ratio = {"feature": "16x9", "portrait": "3x4", "landscape": "16x9", "small": "4x3", "full": "21x9"}.get(p["size"], "4x3")
        cards.append(f'''
        <div class="work-card size-{p['size']}" data-filter-item="{','.join(p['services'])}">
          <a href="{r}work/{p['slug']}/">
            {ph_block(ratio, p['title'])}
            <div class="work-card-overlay">
              <span class="work-card-cat">{esc(p['category'])}</span>
              <span class="work-card-title">{esc(p['title'])}</span>
              <span class="work-card-meta">{esc(p['location'])} · {esc(p['year'])}</span>
            </div>
          </a>
        </div>''')
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "Work index hero")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Work", None)])}
        <span class="eyebrow">Selected Work</span>
        <h1>Work</h1>
        <p class="hero-sub">Stories, people, places and brands — captured and built with intention.</p>
      </div>
    </section>'''
    grid = f'''
    <section>
      <div class="container">
        <div class="filter-bar">{filter_btns}</div>
        <div class="work-grid">{"".join(cards)}</div>
      </div>
    </section>'''
    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Have a project like this in mind?</h2>
        <a class="btn btn-primary" href="{r}contact/">Discuss a Project</a>
      </div>
    </section>'''
    w("work/index.html", page(
        "Work", "A story-led portfolio of Lari Creative Studio case studies spanning branding, web, photography, video and marketing.",
        depth, hero + grid + cta, active="work",
    ))


def build_work_detail(p):
    depth = 2
    r = R(depth)
    idx = WORK_PROJECTS.index(p)
    related = [WORK_PROJECTS[(idx + i) % len(WORK_PROJECTS)] for i in (1, 2, 3)]
    related_html = "".join(f'''
      <a class="work-card size-portrait" href="{r}work/{rp['slug']}/">
        {ph_block("3x4", rp['title'])}
        <div class="work-card-overlay"><span class="work-card-cat">{esc(rp['category'])}</span><span class="work-card-title">{esc(rp['title'])}</span></div>
      </a>''' for rp in related)

    gallery_imgs = "".join(
        f'<a href="#" data-lightbox-trigger data-caption="{esc(p["title"])} — image {i}">{ph_block("4x3", p["title"] + " — gallery image " + str(i))}</a>'
        for i in range(1, 7)
    )

    services_links = ", ".join(f'<a href="{r}services/{sl}/">{esc(SERVICES_BY_SLUG[sl]["name"])}</a>' for sl in p["services"]) or "—"

    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", p['title'] + " — hero image")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Work", "work/"), (p['title'], None)])}
        <span class="eyebrow">{esc(p['category'])}</span>
        <h1>{esc(p['title'])}</h1>
        <p class="hero-sub">{esc(p['desc'])}</p>
      </div>
    </section>'''

    meta = f'''
    <section style="padding-top:56px; padding-bottom:56px;">
      <div class="container">
        <div class="steps">
          <div class="step"><h4>Category</h4><p>{esc(p['category'])}</p></div>
          <div class="step"><h4>Location</h4><p>{esc(p['location'])}</p></div>
          <div class="step"><h4>Year</h4><p>{esc(p['year'])}</p></div>
          <div class="step"><h4>Services</h4><p>{services_links}</p></div>
        </div>
      </div>
    </section>'''

    story = f'''
    <section class="on-ivory-dim">
      <div class="container split">
        <div class="split-copy">
          {section_head("The Story", "Approach")}
          <p>{esc(p['desc'])} The brief called for a considered, editorial treatment — every choice of location, framing and pacing was made in service of the story, not just to fill a page.</p>
          <p>Placeholder photography stands in for the finished set below; each frame is labelled so real photography can be dropped in without touching the layout.</p>
        </div>
        <div class="split-media">{ph_block("3x4", p['title'] + " — behind the scenes")}</div>
      </div>
    </section>'''

    gallery = f'''
    <section>
      <div class="container">
        {section_head("Gallery", "Selected images")}
        <div class="card-grid">{gallery_imgs}</div>
      </div>
    </section>'''

    credits = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("Credits", "Project team")}
        <table class="pricing-table"><tbody>
          <tr><td>Creative Direction</td><td>Lari Creative Studio</td></tr>
          <tr><td>Services</td><td>{services_links}</td></tr>
          <tr><td>Location</td><td>{esc(p['location'])}</td></tr>
        </tbody></table>
      </div>
    </section>'''

    related_section = f'''
    <section>
      <div class="container">
        {section_head("Related Work", "More from the studio")}
        <div class="work-grid">{related_html}</div>
      </div>
    </section>'''

    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Discuss a project like this</h2>
        <a class="btn btn-primary" href="{r}contact/">Discuss a Project</a>
      </div>
    </section>'''

    lightbox_html = '''
    <div class="lightbox">
      <button class="lightbox-close" aria-label="Close">&times;</button>
      <button class="lightbox-prev" aria-label="Previous">&#8249;</button>
      <div class="lightbox-img-wrap"></div>
      <div class="lightbox-caption"></div>
      <button class="lightbox-next" aria-label="Next">&#8250;</button>
    </div>'''

    body = hero + meta + story + gallery + credits + related_section + cta + lightbox_html
    w(f"work/{p['slug']}/index.html", page(
        p['title'], p['desc'], depth, body, active="work",
    ))


# ---------------------------------------------------------------------------
# JOURNAL
# ---------------------------------------------------------------------------

def build_journal_index():
    depth = 1
    r = R(depth)
    cards = "".join(_journal_card(a, r) for a in JOURNAL_ARTICLES)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "Journal hero")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Journal", None)])}
        <span class="eyebrow">Journal</span>
        <h1>The Lari Journal</h1>
        <p class="hero-sub">Ideas on photography, branding, design, technology and business — from the studio floor.</p>
      </div>
    </section>'''
    grid = f'<section><div class="container"><div class="card-grid">{cards}</div></div></section>'
    w("journal/index.html", page(
        "Journal", "Editorial articles on photography, branding, design, technology and business from Lari Creative Studio.",
        depth, hero + grid, active="journal",
    ))


def build_journal_article(a):
    depth = 2
    r = R(depth)
    idx = JOURNAL_ARTICLES.index(a)
    more = [JOURNAL_ARTICLES[(idx + i) % len(JOURNAL_ARTICLES)] for i in (1, 2, 3)]
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", a['title'])}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Journal", "journal/"), (a['title'], None)])}
        <span class="eyebrow">{esc(a['category'])}</span>
        <h1>{esc(a['title'])}</h1>
        <p class="hero-sub">{esc(a['date'])} · {esc(a['read_time'])}</p>
      </div>
    </section>'''
    body_paragraphs = a.get("body") or [a["excerpt"]]
    first_half = body_paragraphs[:1]
    rest = body_paragraphs[1:]
    first_html = "".join(f"<p>{esc(p)}</p>" for p in first_half)
    image_html = ph_block("16x9", a['title'] + " — editorial image")
    rest_html = "".join(f"<p>{esc(p)}</p>" for p in rest)
    body_copy = f'''
    <section>
      <div class="container" style="max-width:760px;">
        {first_html}
        {image_html}
        {rest_html}
      </div>
    </section>'''
    more_html = "".join(_journal_card(m, r) for m in more)
    more_section = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("More From the Journal", "Continue reading")}
        <div class="card-grid">{more_html}</div>
      </div>
    </section>'''
    w(f"journal/{a['slug']}/index.html", page(
        a['title'], a['excerpt'], depth, hero + body_copy + more_section, active="journal",
    ))


# ---------------------------------------------------------------------------
# ACADEMY
# ---------------------------------------------------------------------------

def build_academy_index():
    depth = 1
    r = R(depth)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "Academy hero — student at work")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Academy", None)])}
        <span class="eyebrow">Lari Academy</span>
        <h1>Learn the process we use with clients.</h1>
        <p class="hero-sub">Self-paced courses across every service we offer — from your first brand identity to running AI automation for a business.</p>
        <div class="hero-ctas"><a class="btn btn-primary" href="{r}academy/register/">Create Free Account</a><a class="btn btn-outline" href="#courses">Browse Courses</a></div>
      </div>
    </section>'''

    guide_cards = []
    for g in GUIDE_BUNDLES:
        badge = ""
        if g["key"] == "professional":
            badge = '<span class="guide-badge soon">Coming Soon</span>'
        elif g["key"] == "ultimate":
            badge = '<span class="guide-badge soon">Coming Soon</span>'
        elif g["key"] == "starter":
            badge = '<span class="guide-badge">Available Now</span>'
        rec_cls = " is-recommended" if g["key"] == "professional" else ""
        includes = "".join(f"<li>{esc(i)}</li>" for i in g["includes"])
        cta_html = (
            buy_button("guide", g["key"], g["name"] + " — " + g["subtitle"],
                       {"ngn": g["price_ngn"], "usd": g["price_usd"], "gbp": g["price_gbp"], "eur": g["price_eur"]},
                       "Get the Guide", classes="btn btn-primary btn-block")
            if g["available"] else
            f'<button class="btn btn-ghost btn-block" disabled>Coming Soon</button>'
        )
        guide_cards.append(f'''
        <div class="guide-card{rec_cls}">
          {badge}
          <div class="guide-name">{esc(g['name'])}</div>
          <div class="guide-subtitle">{esc(g['subtitle'])}</div>
          <div class="guide-price">{esc(g['price_ngn'])}</div>
          <div class="guide-price-alt">{esc(g['price_usd'])} · {esc(g['price_gbp'])} · {esc(g['price_eur'])}</div>
          <ul>{includes}</ul>
          <div class="guide-best">{esc(g['best_for'])}</div>
          {cta_html}
        </div>''')
    guides_section = f'''
    <section>
      <div class="container">
        {section_head("The Core Guide", "Start with the flagship self-study system")}
        <div class="guide-grid">{"".join(guide_cards)}</div>
      </div>
    </section>'''

    course_cards = []
    for c in COURSES:
        svc = SERVICES_BY_SLUG[c["service_slug"]]
        course_cards.append(f'''
        <div class="course-card">
          <div class="course-track">{esc(svc['name'])}</div>
          <h3>{esc(c['title'])}</h3>
          <p>{esc(c['summary'])}</p>
          <div class="course-meta-row"><span>{esc(c['level'])}</span><span>{esc(c['duration'])}</span></div>
          <a class="btn btn-ghost btn-block" href="{r}academy/courses/{c['slug']}/">View Course</a>
        </div>''')
    courses_section = f'''
    <section id="courses" class="on-ivory-dim">
      <div class="container">
        {section_head("All Courses", "One course track per service line")}
        <div class="card-grid">{"".join(course_cards)}</div>
      </div>
    </section>'''

    how = f'''
    <section>
      <div class="container">
        {section_head("How It Works", "Register once, learn at your own pace")}
        <div class="steps">
          <div class="step"><div class="step-num">01</div><h4>Register</h4><p>Create a free account in under a minute.</p></div>
          <div class="step"><div class="step-num">02</div><h4>Pay per course</h4><p>Enrol in any course with a one-time payment — pay in Naira, US Dollars, Pounds or Euros.</p></div>
          <div class="step"><div class="step-num">03</div><h4>Learn</h4><p>Course access unlocks immediately after payment — work through it at your own pace.</p></div>
          <div class="step"><div class="step-num">04</div><h4>Track progress</h4><p>Your dashboard tracks progress toward each course's certificate.</p></div>
        </div>
      </div>
    </section>'''

    faq_items = "".join(f'''
        <div class="faq-item"><button class="faq-q"><span>{esc(q)}</span><span class="faq-icon">+</span></button><div class="faq-a"><div class="faq-a-inner">{esc(a2)}</div></div></div>'''
        for q, a2 in (list(ACADEMY_FAQS) + [FAQS[5]]))
    faq_section = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("Academy FAQ", "Common questions")}
        <div class="faq-list">{faq_items}</div>
      </div>
    </section>'''

    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Start learning today.</h2>
        <div class="hero-ctas"><a class="btn btn-primary" href="{r}academy/register/">Create Free Account</a><a class="btn btn-outline" href="{r}academy/signin/">Sign In</a></div>
      </div>
    </section>'''

    body = hero + guides_section + courses_section + how + faq_section + cta + payment_modal_html()
    w("academy/index.html", page(
        "Academy", "Lari Academy — self-paced courses across branding, web design, UI/UX, photography, video, social content, marketing, consulting, AI automation and training.",
        depth, body, active="academy",
    ))


def build_course_detail(c):
    depth = 3
    r = R(depth)
    svc = SERVICES_BY_SLUG[c["service_slug"]]
    price = c["price"]
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", c['title'])}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Academy", "academy/"), (c['title'], None)])}
        <span class="eyebrow">{esc(svc['name'])}</span>
        <h1>{esc(c['title'])}</h1>
        <p class="hero-sub">{esc(c['summary'])}</p>
        <p class="hero-sub" style="margin-top:-18px; font-weight:600; color:var(--gold-bright);">{esc(price['ngn'])} · {esc(price['usd'])} · {esc(price['gbp'])} · {esc(price['eur'])} — one-time payment</p>
        <div class="hero-ctas">
          {buy_button("course", c['slug'], c['title'], price, "Enrol in this Course")}
        </div>
      </div>
    </section>'''

    outcomes_html = "".join(f'<li style="padding-bottom:10px; border-bottom:1px solid var(--line-on-light);">— {esc(x)}</li>' for x in c["outcomes"])
    curriculum_html = "".join(f'<div class="step"><div class="step-num">0{i}</div><h4>{esc(x)}</h4></div>' for i, x in enumerate(c["curriculum"], 1))

    overview = f'''
    <section>
      <div class="container split">
        <div class="split-copy">
          {section_head("What You'll Learn", "Course outcomes")}
          <ul style="display:flex; flex-direction:column; gap:10px;">{outcomes_html}</ul>
        </div>
        <div class="split-media">
          <div class="dash-panel" style="margin:0;">
            <h3>Course details</h3>
            <table class="pricing-table"><tbody>
              <tr><td>Track</td><td>{esc(svc['name'])}</td></tr>
              <tr><td>Level</td><td>{esc(c['level'])}</td></tr>
              <tr><td>Duration</td><td>{esc(c['duration'])}</td></tr>
              <tr><td>Format</td><td>Self-paced, online</td></tr>
              <tr><td>Price</td><td>{esc(price['ngn'])} / {esc(price['usd'])} / {esc(price['gbp'])} / {esc(price['eur'])}</td></tr>
            </tbody></table>
          </div>
        </div>
      </div>
    </section>'''

    curriculum = f'''
    <section class="on-ivory-dim">
      <div class="container">
        {section_head("Curriculum", "Module by module")}
        <div class="steps">{curriculum_html}</div>
      </div>
    </section>'''

    related = f'''
    <section>
      <div class="container split">
        <div class="split-copy">
          {section_head("Want the professional version?", "This is the learning track — " + svc['name'] + " is also a service")}
          <p>If you'd rather have the studio deliver this professionally instead of doing it yourself, {esc(svc['name'])} is available at Essential, Professional and Enterprise tiers.</p>
          <a class="btn btn-ghost" href="{r}services/{svc['slug']}/">View {esc(svc['name'])} Service</a>
        </div>
        <div class="split-media">{ph_block("4x3", svc['name'])}</div>
      </div>
    </section>'''

    cta = f'''
    <section class="cta-band">
      <div class="container">
        <h2>Ready to start {esc(c['title'])}?</h2>
        <div class="hero-ctas">{buy_button("course", c['slug'], c['title'], price, "Enrol in this Course")}</div>
      </div>
    </section>'''

    body = hero + overview + curriculum + related + cta + payment_modal_html()
    w(f"academy/courses/{c['slug']}/index.html", page(
        c['title'], c['summary'], depth, body, active="academy",
    ))


def build_academy_register():
    depth = 2
    r = R(depth)
    visual = f'''
    <div class="auth-visual">
      {ph_block("3x4", "Academy — student portrait")}
      <div class="auth-visual-copy">
        <h2 style="color:var(--ivory);">Learn the exact process we use with clients.</h2>
        <p class="lede">Ten course tracks. Self-paced. Registration is free — course access is unlocked per course after a one-time payment.</p>
      </div>
    </div>'''
    form = f'''
    <div class="auth-form-side">
      <div class="auth-form-wrap">
        <div class="auth-logo brand">{logo_img(r, 30)}<span class="brand-word" style="color:var(--navy);">Lari<br><small>Creative Studio</small></span></div>
        <span class="eyebrow">Lari Academy</span>
        <h1 style="font-size:32px;">Create your account</h1>
        <p class="lede" style="margin-bottom:28px;">Free — start learning in under a minute.</p>
        <div class="auth-error"></div>
        <form data-academy-register novalidate>
          <div class="form-grid">
            <div class="field full"><label for="full_name">Full name</label><input id="full_name" name="full_name" type="text" required></div>
            <div class="field full"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
            <div class="field full"><label for="password">Password</label><input id="password" name="password" type="password" minlength="6" required></div>
          </div>
          <label class="checkbox-row" style="margin:18px 0 22px;"><input type="checkbox" required> I agree to the <a href="{r}terms/" style="color:var(--gold);">Terms</a> and <a href="{r}privacy/" style="color:var(--gold);">Privacy Policy</a>.</label>
          <button class="btn btn-primary btn-block" type="submit">Create Account</button>
        </form>
        <p class="auth-switch">Already have an account? <a href="{r}academy/signin/">Sign in</a></p>
        <p class="form-note">This registration runs entirely in your browser for demonstration — no data leaves your device. See the README for what a production build needs. Prefer to look around first? Sign in with the demo account: <strong>demo@laricreativestudio.com</strong> / <strong>demo1234</strong>.</p>
      </div>
    </div>'''
    body = f'<div class="auth-shell">{visual}{form}</div>'
    w("academy/register/index.html", page(
        "Register", "Create a free Lari Academy student account.", depth, body, active="academy",
    ))


def build_academy_signin():
    depth = 2
    r = R(depth)
    visual = f'''
    <div class="auth-visual">
      {ph_block("3x4", "Academy — returning student")}
      <div class="auth-visual-copy">
        <h2 style="color:var(--ivory);">Welcome back.</h2>
        <p class="lede">Pick up right where you left off.</p>
      </div>
    </div>'''
    form = f'''
    <div class="auth-form-side">
      <div class="auth-form-wrap">
        <div class="auth-logo brand">{logo_img(r, 30)}<span class="brand-word" style="color:var(--navy);">Lari<br><small>Creative Studio</small></span></div>
        <span class="eyebrow">Lari Academy</span>
        <h1 style="font-size:32px;">Sign in</h1>
        <p class="lede" style="margin-bottom:28px;">Access your student dashboard.</p>
        <div class="auth-error"></div>
        <form data-academy-signin novalidate>
          <div class="form-grid">
            <div class="field full"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
            <div class="field full"><label for="password">Password</label><input id="password" name="password" type="password" required></div>
          </div>
          <button class="btn btn-primary btn-block" type="submit" style="margin-top:22px;">Sign In</button>
        </form>
        <p class="auth-switch">New to Lari Academy? <a href="{r}academy/register/">Create a free account</a></p>
        <p class="form-note">This sign-in runs entirely in your browser for demonstration — no data leaves your device. To see a populated dashboard immediately, sign in with <strong>demo@laricreativestudio.com</strong> / <strong>demo1234</strong>.</p>
      </div>
    </div>'''
    body = f'<div class="auth-shell">{visual}{form}</div>'
    w("academy/signin/index.html", page(
        "Sign In", "Sign in to your Lari Academy student account.", depth, body, active="academy",
    ))


DASH_NAV = [
    ("index.html", "Overview", "grid"),
    ("my-courses.html", "My Courses", "book"),
    ("certificates.html", "Certificates", "award"),
    ("settings.html", "Settings", "gear"),
]


def dash_sidebar(depth, active_file):
    r = R(depth)
    links = "".join(
        f'<a class="{"is-active" if f == active_file else ""}" href="{r}academy/dashboard/{f}">{label}</a>'
        for f, label, _ in DASH_NAV
    )
    return f'''
    <aside class="dash-sidebar">
      <div class="dash-brand">{logo_img(r, 26)}<span class="dash-brand-word">Lari Academy</span></div>
      <nav class="dash-sidebar-nav" style="display:flex; flex-direction:column; flex:1;">
        <div class="dash-nav">{links}</div>
        <div class="dash-user">
          <strong data-user-name>Student</strong>
          <span data-user-email>—</span>
          <div class="dash-logout" role="button" data-logout style="cursor:pointer;">Sign out</div>
        </div>
      </nav>
    </aside>'''


def build_dashboard_overview():
    depth = 2
    r = R(depth)
    body = f'''
    <div class="dash-shell" data-dash-page="overview">
      {dash_sidebar(depth, "index.html")}
      <div class="dash-main">
        <div class="dash-header">
          <div><h1>Welcome back, <span data-user-name>Student</span></h1><p>Here's where you left off.</p></div>
          <a class="btn btn-primary" href="{r}academy/">Browse more courses</a>
        </div>
        <div class="stat-grid">
          <div class="stat-card"><div class="stat-num" data-stat-total>0</div><div class="stat-label">Enrolled Courses</div></div>
          <div class="stat-card"><div class="stat-num" data-stat-inprogress>0</div><div class="stat-label">In Progress</div></div>
          <div class="stat-card"><div class="stat-num" data-stat-done>0</div><div class="stat-label">Completed</div></div>
        </div>
        <div class="dash-panel">
          <h3>Continue learning</h3>
          <div data-enrolled-list></div>
        </div>
      </div>
    </div>'''
    w("academy/dashboard/index.html", page(
        "Student Dashboard", "Your Lari Academy dashboard.", depth, body, active="academy",
    ))


def build_dashboard_my_courses():
    depth = 2
    r = R(depth)
    body = f'''
    <div class="dash-shell" data-dash-page="my-courses">
      {dash_sidebar(depth, "my-courses.html")}
      <div class="dash-main">
        <div class="dash-header"><div><h1>My Courses</h1><p>Every course you've paid for and enrolled in.</p></div><a class="btn btn-primary" href="{r}academy/">Browse more courses</a></div>
        <div class="dash-panel"><div data-enrolled-list></div></div>
        <div class="dash-panel"><h3>Purchased Guides</h3><div data-guides-list></div></div>
      </div>
    </div>'''
    w("academy/dashboard/my-courses.html", page(
        "My Courses", "Your enrolled Lari Academy courses.", depth, body, active="academy",
    ))


def build_dashboard_certificates():
    depth = 2
    r = R(depth)
    body = f'''
    <div class="dash-shell" data-dash-page="certificates">
      {dash_sidebar(depth, "certificates.html")}
      <div class="dash-main">
        <div class="dash-header"><div><h1>Certificates</h1><p>Awarded when you complete a course.</p></div></div>
        <div class="dash-panel"><div data-cert-list></div></div>
      </div>
    </div>'''
    w("academy/dashboard/certificates.html", page(
        "Certificates", "Your Lari Academy certificates.", depth, body, active="academy",
    ))


def build_dashboard_settings():
    depth = 2
    r = R(depth)
    body = f'''
    <div class="dash-shell" data-dash-page="settings">
      {dash_sidebar(depth, "settings.html")}
      <div class="dash-main">
        <div class="dash-header"><div><h1>Settings</h1><p>Your account details.</p></div></div>
        <div class="dash-panel">
          <h3>Profile</h3>
          <div class="form-grid">
            <div class="field"><label>Full name</label><input type="text" data-user-name-input disabled></div>
            <div class="field"><label>Email</label><input type="text" data-user-email disabled></div>
          </div>
          <p class="form-note">Editing profile details requires a real backend — see the README. This demo account lives only in your browser's local storage.</p>
        </div>
        <div class="dash-panel">
          <h3>Account</h3>
          <button class="btn btn-outline" data-logout>Sign Out</button>
        </div>
      </div>
    </div>'''
    w("academy/dashboard/settings.html", page(
        "Settings", "Your Lari Academy account settings.", depth, body, active="academy",
    ))


# ---------------------------------------------------------------------------
# CONTACT
# ---------------------------------------------------------------------------

def build_contact():
    depth = 1
    r = R(depth)
    service_options = "".join(f'<option value="{s["slug"]}">{esc(s["name"])}</option>' for s in SERVICES)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "Contact hero")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Contact", None)])}
        <span class="eyebrow">Start a Project</span>
        <h1>Let's create something meaningful.</h1>
        <p class="hero-sub">Whether you're planning an event, building a brand, launching a campaign or automating a workflow — we'd love to hear from you.</p>
      </div>
    </section>'''

    form_section = f'''
    <section>
      <div class="container split">
        <div class="split-copy">
          <div class="form-success">Thank you — your enquiry has been noted. This is a demo form with no live backend; see the README for what a production build needs. We'll be in touch at the email you provided.</div>
          <form data-demo-form novalidate>
            <div class="form-grid">
              <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required></div>
              <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required></div>
              <div class="field"><label for="phone">Phone</label><input id="phone" name="phone" type="tel"></div>
              <div class="field"><label for="company">Company / Organisation</label><input id="company" name="company" type="text"></div>
              <div class="field"><label for="service">Project Type</label><select id="service" name="service">{service_options}</select></div>
              <div class="field"><label for="date">Preferred Date</label><input id="date" name="date" type="date"></div>
              <div class="field"><label for="location">Location</label><input id="location" name="location" type="text"></div>
              <div class="field"><label for="budget">Estimated Budget</label><input id="budget" name="budget" type="text" placeholder="e.g. ₦500,000 – ₦1,000,000"></div>
              <div class="field full"><label for="message">Tell us about your project</label><textarea id="message" name="message" required></textarea></div>
              <div class="field full"><label for="source">How did you hear about us?</label><input id="source" name="source" type="text"></div>
            </div>
            <button class="btn btn-primary" type="submit" style="margin-top:24px;">Send Project Enquiry</button>
          </form>
        </div>
        <div class="split-media">
          <div class="dash-panel" style="margin-bottom:20px;">
            <h3>Get in touch directly</h3>
            <table class="pricing-table"><tbody>
              <tr><td>Email</td><td><a href="mailto:{esc(BRAND['email'])}">{esc(BRAND['email'])}</a></td></tr>
              <tr><td>Phone</td><td>{esc(BRAND['phone'])}</td></tr>
              <tr><td>WhatsApp</td><td><a href="{esc(BRAND['whatsapp_link'])}">{esc(BRAND['whatsapp_display'])}</a></td></tr>
              <tr><td>Location</td><td>{esc(BRAND['location_line'])}</td></tr>
            </tbody></table>
          </div>
          <a class="btn btn-outline btn-block" href="{esc(BRAND['whatsapp_link'])}">Chat on WhatsApp</a>
          <div style="margin-top:20px;">{ph_block("4x3", "Map / studio location")}</div>
        </div>
      </div>
    </section>'''

    w("contact/index.html", page(
        "Contact", "Start a project with Lari Creative Studio — branding, web, photography, video, marketing, consulting, AI automation or training.",
        depth, hero + form_section, active="contact",
    ))


# ---------------------------------------------------------------------------
# CLIENT GALLERY (demo password gate)
# ---------------------------------------------------------------------------

def build_client_gallery():
    depth = 1
    r = R(depth)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "Client gallery hero")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("Client Gallery", None)])}
        <span class="eyebrow">Private Access</span>
        <h1>Client Gallery</h1>
        <p class="hero-sub">Enter your access code to view your private gallery.</p>
      </div>
    </section>'''

    gate = f'''
    <div class="password-gate">
      <div class="gate-box">
        <h3>Enter Access Code</h3>
        <p class="lede" style="margin:0 auto 24px;">Sent to you by your Lari project lead.</p>
        <form data-gate-form novalidate>
          <div class="field"><input name="access_code" type="text" placeholder="Access code" required></div>
          <div class="field-error" style="margin:10px 0;">That code didn't work — check your email for the correct link.</div>
          <button class="btn btn-primary btn-block" type="submit" style="margin-top:16px;">View Gallery</button>
        </form>
        <p class="form-note">Demo only: any non-empty code unlocks the gallery below. A production build needs a real backend to issue and check codes — see the README.</p>
      </div>
    </div>'''

    imgs = "".join(f'<a href="#" data-lightbox-trigger data-caption="Client gallery image {i}">{ph_block("4x3", "Client gallery image " + str(i))}</a>' for i in range(1, 13))
    content = f'''
    <div data-gate-content style="display:none;">
      <section>
        <div class="container">
          <div class="section-head-row">
            {section_head("Your Gallery", "Selected Images")}
            <div><button class="btn btn-ghost btn-sm">Select Favourites</button> <button class="btn btn-outline btn-sm">Download All</button></div>
          </div>
          <div class="card-grid">{imgs}</div>
        </div>
      </section>
    </div>
    <div class="lightbox">
      <button class="lightbox-close" aria-label="Close">&times;</button>
      <button class="lightbox-prev" aria-label="Previous">&#8249;</button>
      <div class="lightbox-img-wrap"></div>
      <div class="lightbox-caption"></div>
      <button class="lightbox-next" aria-label="Next">&#8250;</button>
    </div>'''

    w("client-gallery/index.html", page(
        "Client Gallery", "Private, password-protected client gallery for Lari Creative Studio clients.",
        depth, hero + gate + content, active="",
    ))


# ---------------------------------------------------------------------------
# FAQ
# ---------------------------------------------------------------------------

def build_faq():
    depth = 1
    r = R(depth)
    items = "".join(f'''
      <div class="faq-item"><button class="faq-q"><span>{esc(q)}</span><span class="faq-icon">+</span></button><div class="faq-a"><div class="faq-a-inner">{esc(a)}</div></div></div>'''
        for q, a in FAQS)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", "FAQ hero")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), ("FAQ", None)])}
        <span class="eyebrow">Support</span>
        <h1>Frequently Asked Questions</h1>
      </div>
    </section>'''
    body = f'<section><div class="container" style="max-width:820px;"><div class="faq-list">{items}</div></div></section>'
    cta = f'''
    <section class="cta-band">
      <div class="container"><h2>Still have a question?</h2><a class="btn btn-primary" href="{r}contact/">Contact Us</a></div>
    </section>'''
    w("faq/index.html", page(
        "FAQ", "Answers to common questions about Lari Creative Studio's pricing, timelines, retainers and Academy.",
        depth, hero + body + cta, active="",
    ))


# ---------------------------------------------------------------------------
# PRIVACY / TERMS / 404
# ---------------------------------------------------------------------------

def build_legal_page(slug, title, paragraphs):
    depth = 1
    r = R(depth)
    hero = f'''
    <section class="hero hero-compact">
      <div class="hero-media">{ph_block("21x9", title)}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner">
        {breadcrumb(depth, [("Home", "index.html"), (title, None)])}
        <span class="eyebrow">Legal</span>
        <h1>{esc(title)}</h1>
      </div>
    </section>'''
    body_paras = "".join(f'<p>{esc(p) if isinstance(p, str) else p}</p>' for p in paragraphs)
    body = f'<section><div class="container" style="max-width:800px;">{body_paras}</div></section>'
    w(f"{slug}/index.html", page(title, f"{title} for {BRAND['name']}.", depth, hero + body, active=""))


def build_404():
    depth = 0
    r = R(depth)
    body = f'''
    <section class="hero hero-compact" style="min-height:100vh; align-items:center; text-align:center;">
      <div class="hero-media">{ph_block("21x9", "404 — page not found")}</div>
      <div class="hero-scrim"></div>
      <div class="container hero-inner" style="text-align:center;">
        <span class="eyebrow">404</span>
        <h1>This page wandered off.</h1>
        <p class="hero-sub" style="margin:0 auto 34px;">The page you're looking for doesn't exist, or has moved.</p>
        <div class="hero-ctas" style="justify-content:center;"><a class="btn btn-primary" href="{r}index.html">Back to Home</a><a class="btn btn-outline" href="{r}work/">See Our Work</a></div>
      </div>
    </section>'''
    w("404.html", page("Page Not Found", "This page could not be found.", depth, body, active=""))


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

PRIVACY_PARAGRAPHS = [
    "Lari Creative Studio (\"we\", \"us\") respects your privacy. This placeholder policy outlines, in plain language, how information submitted through this website would typically be handled — replace it with counsel-reviewed copy before launch.",
    "Information we collect: details you submit through the contact form, discovery calls, or Academy registration (name, email, phone, project details).",
    "How we use it: to respond to enquiries, prepare proposals, deliver services, and — where you've opted in — to send occasional updates.",
    "We do not sell personal information. Academy accounts in this build are stored only in your own browser's local storage and are never transmitted anywhere.",
    "Contact us at " + BRAND["email"] + " with any privacy questions or requests to access or delete your information.",
]

TERMS_PARAGRAPHS = [
    "These placeholder Terms & Conditions govern the use of this website and engagement of Lari Creative Studio's services — replace with counsel-reviewed copy before launch.",
    "Quotations are starting points; a final scope and price are confirmed in a written proposal after a discovery call.",
    "Retainer services (social media, digital marketing, business consulting) require a 3-month minimum commitment, billed monthly. Early termination before the minimum results in 50% of the remaining balance becoming due, and forfeits any onboarding discount.",
    "All creative work remains the property of Lari Creative Studio until full payment is received, after which agreed usage rights transfer to the client as specified in the project proposal.",
    "Contact us at " + BRAND["email"] + " with any questions about these terms.",
]


def main():
    build_home()
    build_services_index()
    for s in SERVICES:
        build_service_detail(s)
    build_pricing()
    build_about()
    build_work_index()
    for p in WORK_PROJECTS:
        build_work_detail(p)
    build_journal_index()
    for a in JOURNAL_ARTICLES:
        build_journal_article(a)
    build_academy_index()
    for c in COURSES:
        build_course_detail(c)
    build_academy_register()
    build_academy_signin()
    build_dashboard_overview()
    build_dashboard_my_courses()
    build_dashboard_certificates()
    build_dashboard_settings()
    build_contact()
    build_client_gallery()
    build_faq()
    build_legal_page("privacy", "Privacy Policy", PRIVACY_PARAGRAPHS)
    build_legal_page("terms", "Terms & Conditions", TERMS_PARAGRAPHS)
    build_404()
    print("Site generated at", OUT)


if __name__ == "__main__":
    main()
