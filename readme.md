# Lari Creative Studio — Website

A full multi-page static site for Lari Creative Studio: a 10-service creative
agency (branding, web, UI/UX, photography, video, social content, digital
marketing, business consulting, AI automation, training), plus **Lari
Academy** — a self-paced learning platform with registration, sign-in and a
student dashboard.

Built from the verified 2026 Service Catalogue & Pricing Guide (v02), the
Social Media Brand & Launch Playbook, the Bundle & Pricing Copy document, the
5-Year Growth Strategy & Business Plan, and the supplied brand-kit assets.
Every price, tier, add-on, bundle discount, roadmap milestone and founder
credit on the site is taken directly from those documents — nothing is
invented.

## What's new in this pass

Three real, uploaded assets were incorporated, plus a functional change to how the Academy handles access:

1. **Real brand assets swapped in** — the header/footer/dashboard "L" monogram
   is now the actual gold-on-navy circular logo mark you supplied
   (`assets/img/logo-mark.png`), used as the favicon too. The About page's
   Founder & Creative Director section now uses your supplied name
   (**Oluwatimilehin Monilari**) and headshot
   (`assets/img/founder-oluwatimilehin-monilari.jpg`) instead of a
   placeholder block.
2. **Courses and the Core Guide are now paid, not free to access.** Every
   course has a real price (scoped from the verified "Online Courses"
   add-on line in the Pricing Guide, ₦20,000–₦150,000 / $50–$300, applied
   per individual course) shown in four currencies. Clicking "Enrol"
   or "Get the Guide" opens a demo checkout modal — a course or guide is
   only added to the student's dashboard **after** the demo payment step is
   confirmed. Registering an account is still free; course *access* is not.
3. **Multi-currency checkout** — the payment modal lets the buyer choose
   Naira, US Dollars, British Pounds or Euros, and shows the correct amount
   for whichever they pick. This is a demo (see below) but the currency
   selection and amount lookup are fully wired.

## How the demo payment flow works (and what a real one needs)

Clicking a course's "Enrol" button (or the Core Guide's "Get the Guide"
button):

- If you're not signed in, you're sent to Sign In / Register first, and
  brought back to the same item afterward (`?next=course:<slug>` or
  `?next=guide:<key>`).
- If you are signed in, a checkout modal opens showing the item, a currency
  selector (NGN/USD/GBP/EUR), and the price in that currency.
- Clicking "Pay Now (Demo)" immediately marks the item as purchased in
  `localStorage` and unlocks it on the dashboard — **no real payment is
  taken.**

To make this a real, chargeable checkout, a developer needs to:

1. Replace the "Pay Now (Demo)" handler in `assets/js/main.js` (search for
   `data-pm-confirm`) with a call to a real payment processor —
   **Paystack or Flutterwave** for Naira and local cards, **Stripe** for
   USD/GBP/EUR — and only write the purchase to the database after that
   processor confirms the charge server-side.
2. Move the "is this paid for" check server-side. Right now, gating is
   client-side (`localStorage`), which is fine for a demo but is not real
   access control — a determined visitor could bypass it in devtools.
3. Handle currency conversion server-side too, ideally with live rates
   rather than the fixed amounts baked into this demo.

Earlier additions (from the previous revision) are still in place: the
About page's "Market Position", "Key Differentiators" and "Our Roadmap"
sections (sourced from the 5-Year Growth Strategy document), full body copy
on all six Journal articles, and the pre-seeded demo account
(`demo@laricreativestudio.com` / `demo1234`) for reviewing a populated
dashboard without registering.

## How to view it

Open `index.html` directly in a browser, or serve the folder locally:

```
python3 -m http.server 8000
```

then visit `http://localhost:8000`.

## What's included (53 pages)

| Section | Pages |
|---|---|
| Home | 1 |
| Services | hub + 10 service detail pages (3-tier pricing, add-ons, process, FAQ) |
| Pricing | 1 (full pricing reference, bundles, retainer terms) |
| Work | hub + 8 story-led case studies (filterable by service) |
| About | 1 (identity, positioning, differentiators, values, methodology, 5-year roadmap, founder) |
| **Academy** | hub + 10 course pages + register + sign-in + 4 dashboard pages |
| Journal | hub + 6 articles (full body copy) |
| Contact, Client Gallery, FAQ, Privacy, Terms, 404 | 6 |

All pages share one design system (`assets/css/style.css`) and one script
(`assets/js/main.js`), and are generated from `generate.py` + `data.py` so
adding a new service, course, project or article is a data change, not a
rebuild.

## Design system

- **Colours:** Midnight Navy `#0B1F33`, Heritage Gold `#C8A04D`, Ivory
  `#FAFAF7`, plus supporting navy/graphite/stone tones — matching the brand
  kit. Gold is used only as an accent (labels, borders, active states,
  buttons), never as a background field.
- **Type:** Cormorant Garamond for headings, Inter for body/UI — loaded via
  Google Fonts.
- **Motion:** one entrance animation on hero load; hover states only
  elsewhere. `prefers-reduced-motion` is respected.

## The Lari Academy — how the demo works, and what's needed to go live

Registration, sign-in and the student dashboard are **fully interactive
right now** — register, sign in, enrol in courses, log study sessions, and
see progress and certificates — but the "backend" is your own browser's
`localStorage`. There is no server, no real database, and no real password
security. A pre-seeded demo account (`demo@laricreativestudio.com` /
`demo1234`) is included so you can see a populated dashboard without
registering first.

**To make it live for real students, a developer needs to add:**

1. **Auth & database** — e.g. Supabase, Firebase Auth, or Auth0, plus a
   Postgres/Firestore database for users, enrolments and progress.
2. **Real password hashing** — passwords are currently stored in plain text
   in `localStorage`; this is fine for a demo, never for production.
3. **Course content delivery** — video hosting/streaming, lesson content,
   and a real progress-tracking model (the demo's "+20% per click" button
   in `assets/js/main.js` stands in for actual lesson completion).
4. **Certificate generation** — a PDF certificate generator, triggered at
   100% completion.
5. **Real payment processing** — see "How the demo payment flow works" above;
   this is the biggest gap between the current demo and a sellable product.

All of this logic lives in one file — `assets/js/main.js`, in the section
marked `LARI ACADEMY` — so a developer has a single, clearly-scoped place to
swap `localStorage` calls for real API calls.

### The Core Guide bundle (Starter / Professional / Ultimate)

Per the internal sequencing note in the Bundle & Pricing Copy document: **only
the Starter tier is fully buildable today.** Professional and Ultimate are
shown on the Academy page marked **"Coming Soon"** with their buttons
disabled, exactly as instructed — do not enable checkout for those two tiers
until their components (AI Prompt Library, Templates Pack, Swipe Files,
Resource Vault, Portfolio Builder, Certificate) actually exist.

## Placeholder photography

Two real images are now in use — the logo mark (`assets/img/logo-mark.png`)
and the founder's headshot (`assets/img/founder-oluwatimilehin-monilari.jpg`).
Every other image on the site is still a labelled placeholder block
(gold-bordered, navy gradient, with a caption describing the intended
photograph). To swap one in for real photography:

1. Replace the `ph_block(...)` call in `generate.py` for that spot with an
   `<img>` tag (or keep `ph_block` as a fallback and add an `<img>` before
   it).
2. Re-run `python3 generate.py` to regenerate every page.
3. Compress images (WebP where possible) before adding.

## Other flagged simplifications (demo-only, no real backend)

- **Contact form** — shows a success message on submit; does not send an
  email. Wire it to a form service (Formspree, etc.) or your own backend.
- **Client Gallery** — any non-empty code unlocks it. A real version needs
  server-side codes tied to specific clients.

## Adding content

Everything content-related lives in `data.py`:

- `SERVICES` — add a service (with its 3 tiers) and it appears in the nav,
  the Services hub, the homepage grid, and the Pricing table automatically.
- `COURSES` — add a course and it appears on the Academy hub automatically.
- `WORK_PROJECTS`, `JOURNAL_ARTICLES`, `FAQS`, `BUNDLES` — same pattern.
- `KEY_DIFFERENTIATORS`, `FIVE_YEAR_ROADMAP`, `FOUNDER` — About page content.

After editing `data.py`, run:

```
python3 generate.py
```

This regenerates the entire `site/` output from scratch.
