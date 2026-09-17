# -*- coding: utf-8 -*-
"""
Lari Creative Studio — site content data.
Sourced from: LARI Service Catalogue & Pricing Guide (2026, v02),
Social Media Brand & Launch Playbook (2026), Bundle & Pricing Copy,
and the supplied brand kit images.
"""

BRAND = {
    "name": "Lari Creative Studio",
    "tagline": "Building Brands. Creating Experiences. Driving Growth.",
    "positioning": "Creative · Digital · Technology · Strategy",
    "location": "Lagos, Nigeria",
    "location_line": "Lagos, Nigeria — working with clients worldwide",
    "email": "hello@laricreativestudio.com",
    "whatsapp_display": "+234 801 234 5678",
    "whatsapp_link": "https://wa.me/2348012345678",
    "phone": "+234 801 234 5678",
    "instagram": "https://instagram.com/laricreativestudio",
    "linkedin": "https://linkedin.com/company/laricreativestudio",
    "facebook": "https://facebook.com/laricreativestudio",
    "youtube": "https://youtube.com/@laricreativestudio",
}

# ---------------------------------------------------------------------------
# SERVICES — the 10 official service lines, each with the verified 3-tier
# pricing structure from the Pricing Guide (2026, v02).
# ---------------------------------------------------------------------------

SERVICES = [
    {
        "slug": "brand-identity-logo-design",
        "name": "Brand Identity & Logo Design",
        "icon": "mark",
        "short": "Distinctive visual identities that give a business a recognizable, professional presence.",
        "hero_desc": "A logo isn't a brand. We build the full visual system behind it — identity, guidelines and the discipline to use them consistently.",
        "why": "A considered identity is the first thing a client, partner or lender judges you by. It sets the ceiling for how seriously your business is taken before anyone reads a word.",
        "included_summary": "Logo concepts, colour and type systems, brand guidelines, and — from Professional up — full stationery and a comprehensive guide.",
        "ideal_for": ["Startups building a first identity", "Businesses overdue for a rebrand", "Organisations that need a documented brand system"],
        "process": [
            ("Discovery", "A structured questionnaire and (from Professional) a strategy session to understand audience, positioning and competitors."),
            ("Concepts", "Multiple logo directions explored, narrowed to the strongest concept."),
            ("Refinement", "Revision rounds to sharpen the mark, palette and type pairing."),
            ("Guidelines", "A brand guide documenting correct usage — from a basic one-pager to a full enterprise system."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦150,000 – ₦400,000",
                "ideal": "Startups, freelancers, first-time brands",
                "includes": ["Discovery questionnaire", "3 logo concepts", "2 revision rounds", "Primary logo", "Secondary logo", "Icon version", "Colour palette", "Typography selection", "Basic brand guide"],
            },
            {
                "name": "Professional",
                "price": "₦500,000 – ₦1,500,000",
                "ideal": "Growing businesses ready to formalise their identity",
                "includes": ["Everything in Essential", "Brand strategy session", "Brand positioning", "Visual identity system", "Stationery design", "Business cards", "Letterhead", "Email signature", "Social media kit", "Comprehensive brand guidelines"],
            },
            {
                "name": "Enterprise",
                "price": "₦2,000,000+",
                "ideal": "Corporations, institutions, multi-division organisations",
                "includes": ["Everything in Professional", "Full brand audit", "Naming consultation (where applicable)", "Brand architecture", "Packaging design", "Signage concepts", "Presentation templates", "Marketing collateral", "Employer branding assets", "Brand implementation support"],
            },
        ],
        "addons": [("Additional Logo Concept", "₦30,000–₦100,000"), ("Brand Style Guide", "₦150,000–₦500,000"), ("Brand Naming Consultation", "₦200,000–₦1,000,000"), ("Packaging Design (per SKU)", "₦150,000–₦600,000")],
        "gallery_projects": ["geometry-of-the-city", "the-quiet-office"],
    },
    {
        "slug": "website-design-development",
        "name": "Website Design & Development",
        "icon": "grid",
        "short": "Custom, responsive websites built to convert visitors into clients — from single-page brand sites to enterprise portals.",
        "hero_desc": "A site that looks considered and loads fast, built around what your visitors actually came to do.",
        "why": "Your website is doing sales and first impressions at once, at every hour, without you in the room. It has to hold up to that job.",
        "included_summary": "Fully responsive builds on WordPress or custom architecture, with SEO, analytics and support baked in from the start.",
        "ideal_for": ["Small businesses needing a first professional site", "Growing companies needing custom pages and booking systems", "Enterprises needing portals, CRM/ERP integration and multi-language support"],
        "process": [
            ("Discovery", "A consultation to map goals, sitemap and required integrations."),
            ("Design", "Page-by-page UI design, reviewed and refined with you."),
            ("Build", "Development, CMS setup, integrations and on-page SEO."),
            ("Launch & support", "Testing, go-live, training and a post-launch support window."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦250,000 – ₦600,000",
                "ideal": "Startups, small businesses, personal brands, freelancers, churches, NGOs, small schools",
                "includes": ["Discovery consultation (30–60 min)", "Up to 5 designed pages", "Responsive design (desktop/tablet/mobile)", "WordPress CMS setup", "Premium theme configuration", "Basic contact form", "Google Maps integration", "WhatsApp chat integration", "Basic on-page SEO", "Social media links", "Basic speed optimisation", "SSL configuration", "Basic security setup", "One revision round", "Basic training (1 hour)", "30 days post-launch support"],
            },
            {
                "name": "Professional",
                "price": "₦700,000 – ₦2,000,000",
                "ideal": "Growing companies, medium-sized businesses, professional firms, restaurants, schools, churches",
                "includes": ["Everything in Essential", "Up to 20 custom-designed pages", "Custom UI/UX design", "Blog/news section", "Service and portfolio pages", "Testimonials and case studies", "Newsletter integration", "Appointment/booking system", "Advanced contact forms", "Payment gateway integration", "Live chat integration", "Google Analytics & Search Console", "Enhanced SEO", "Performance optimisation", "Security hardening", "Backup automation", "Three revision rounds", "Admin training (2–3 hours)", "90 days support"],
            },
            {
                "name": "Enterprise",
                "price": "₦2,500,000+",
                "ideal": "Corporations, universities, government agencies, banks, healthcare organisations, large NGOs",
                "includes": ["Everything in Professional", "Unlimited pages (within scope)", "Fully custom UI/UX", "Enterprise-grade architecture", "Custom portals and dashboards", "Membership systems", "CRM integrations", "ERP integrations", "API integrations", "Multi-language support", "Advanced user roles", "Custom workflows", "High-performance optimisation", "Advanced security implementation", "Dedicated project manager", "Staff training sessions", "Six months technical support"],
            },
        ],
        "addons": [("Extra Web Page", "₦50,000–₦150,000"), ("Blog Setup", "₦80,000–₦250,000"), ("Online Booking System", "₦150,000–₦500,000"), ("Membership Portal", "₦500,000–₦2,000,000"), ("Payment Gateway Setup", "₦100,000–₦300,000"), ("Monthly Website Care Plan", "₦75,000–₦500,000")],
        "gallery_projects": ["the-new-terminal", "market-hours"],
    },
    {
        "slug": "ui-ux-design",
        "name": "UI/UX Design",
        "icon": "layers",
        "short": "Research-driven interface design that turns complex products into intuitive experiences.",
        "hero_desc": "Interfaces designed around how people actually behave, not how a sitemap looks in a meeting.",
        "why": "A confusing product loses people before they ever judge whether it's useful. Good UX is the difference between a feature existing and a feature being used.",
        "included_summary": "Wireframes through to full design systems, prototypes and developer-ready handoff.",
        "ideal_for": ["Founders validating a new product", "Teams needing a documented design system", "Enterprises running full UX research and accessibility programmes"],
        "process": [
            ("Discover", "A workshop and user research to understand real usage."),
            ("Structure", "Wireframes and flows mapping the experience."),
            ("Design", "High-fidelity interface design and an interactive prototype."),
            ("Handoff", "Developer-ready specs, components and documentation."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦200,000 – ₦500,000",
                "ideal": "A single product or feature that needs a clear interface",
                "includes": ["Discovery workshop", "User research", "Wireframes", "One interface design", "Mobile responsiveness", "Interactive prototype", "Design handoff"],
            },
            {
                "name": "Professional",
                "price": "₦600,000 – ₦2,000,000",
                "ideal": "Products with multiple flows and a growing team",
                "includes": ["Everything in Essential", "Multiple user flows", "Dashboard design", "Design system", "Component library", "UX improvements", "Usability review", "Developer collaboration"],
            },
            {
                "name": "Enterprise",
                "price": "₦2,500,000+",
                "ideal": "Multi-platform products needing ongoing design support",
                "includes": ["Everything in Professional", "Product strategy workshops", "Full UX research", "User testing", "Accessibility compliance", "Enterprise design system", "Multi-platform experiences", "Continuous design support"],
            },
        ],
        "addons": [],
        "gallery_projects": ["the-new-terminal"],
    },
    {
        "slug": "photography",
        "name": "Photography",
        "icon": "aperture",
        "short": "Professional imagery for brands, products, teams and events.",
        "hero_desc": "Photography that captures character, atmosphere and detail — not just documentation.",
        "why": "Every touchpoint your business has online lives or dies on its imagery. Flat, generic photos undercut everything else you've built.",
        "included_summary": "Half-day to multi-day productions, professionally edited and delivered with the right usage licence for your needs.",
        "ideal_for": ["Brands needing a professional image library", "Teams needing corporate headshots", "Organisations needing ongoing visual content"],
        "process": [
            ("Consult", "A pre-shoot conversation on style, locations and shot list."),
            ("Shoot", "On-location or studio production with creative direction."),
            ("Edit", "Professional colour grading and retouching."),
            ("Deliver", "High-resolution files via an online gallery, licensed for your use."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦120,000 – ₦350,000",
                "ideal": "A single half-day shoot",
                "includes": ["Pre-shoot consultation", "Half-day session", "Professional editing", "High-resolution images", "Online gallery", "Personal usage licence"],
            },
            {
                "name": "Professional",
                "price": "₦400,000 – ₦1,000,000",
                "ideal": "Brand and commercial shoots needing more coverage",
                "includes": ["Everything in Essential", "Full-day shoot", "Multiple locations", "Creative direction", "Advanced retouching", "Drone photography (where applicable)", "Commercial usage licence"],
            },
            {
                "name": "Enterprise",
                "price": "₦1,500,000+",
                "ideal": "Ongoing corporate or campaign photography",
                "includes": ["Everything in Professional", "Multi-day production", "Production planning", "Lighting crew", "Makeup coordination (optional)", "Full image library", "Priority delivery", "Ongoing visual content partnership"],
            },
        ],
        "addons": [("Extra Shooting Hour", "₦50,000–₦150,000"), ("Drone Coverage", "₦200,000–₦800,000"), ("Same-Day Delivery", "₦100,000–₦300,000"), ("Premium Retouching (per image)", "₦5,000–₦20,000")],
        "gallery_projects": ["dusk-crowds-beneath-the-footbridge", "familiar-faces", "new-collection-still-life"],
    },
    {
        "slug": "videography-documentary-production",
        "name": "Videography & Documentary Production",
        "icon": "frame",
        "short": "Compelling video content, from short promos to full documentary productions.",
        "hero_desc": "Video built around a real story, shot and cut with the same care as a broadcast production.",
        "why": "Video holds attention longer than any other format online — but only if it's made with a clear story, not just footage.",
        "included_summary": "From a single-camera promo through to multi-day documentary shoots with a full crew.",
        "ideal_for": ["Brands needing a promo or launch film", "Companies needing interview-led content", "Organisations commissioning a full documentary"],
        "process": [
            ("Story", "Scripting or interview planning around the core narrative."),
            ("Shoot", "Single or multi-camera production, on-location or in-studio."),
            ("Edit", "Colour grading, motion graphics and sound design."),
            ("Deliver", "Master file plus cut-downs for social platforms."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦350,000 – ₦800,000",
                "ideal": "A short promo or social film",
                "includes": ["Half-day filming", "One videographer", "HD/4K recording", "Basic editing", "Licensed background music", "1–3 minute final video"],
            },
            {
                "name": "Professional",
                "price": "₦900,000 – ₦3,000,000",
                "ideal": "Brand films with interviews and multiple setups",
                "includes": ["Everything in Essential", "Full-day production", "Multiple cameras", "Interviews", "Motion graphics", "Colour grading", "Subtitles", "Social media versions", "3–10 minute production"],
            },
            {
                "name": "Enterprise",
                "price": "₦3,500,000+",
                "ideal": "Full documentary and multi-day productions",
                "includes": ["Everything in Professional", "Documentary production", "Multi-day filming", "Production crew", "Drone cinematography", "Script development", "Storyboarding", "Voice-over production", "Long-form editing", "Distribution-ready deliverables"],
            },
        ],
        "addons": [("Additional Highlight Video", "₦150,000–₦500,000"), ("Voice-over Recording", "₦100,000–₦500,000"), ("Motion Graphics Package", "₦250,000–₦1,000,000")],
        "gallery_projects": ["shine-on-stage"],
    },
    {
        "slug": "social-media-content-creation",
        "name": "Social Media Content Creation",
        "icon": "pulse",
        "short": "Consistent, on-brand content that keeps a business visible and engaged with its audience.",
        "hero_desc": "A content system, not a scramble every week — planned, shot and captioned to a calendar.",
        "why": "Sporadic posting reads as an afterthought. Consistency is what actually builds an audience that converts.",
        "included_summary": "Monthly retainers covering graphics, short-form video, captions and reporting.",
        "ideal_for": ["Brands that need a steady content calendar", "Businesses without an in-house creative team", "Companies running always-on campaigns"],
        "process": [
            ("Plan", "A monthly planning session to set themes and calendar."),
            ("Produce", "Graphics and short-form video shot and edited on-brand."),
            ("Publish", "Captions written and scheduled to the calendar."),
            ("Review", "Monthly analytics and adjustments."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦200,000 / month",
                "ideal": "A foundational, consistent presence",
                "includes": ["12 branded graphics", "4 short videos", "Content calendar", "Caption writing", "Monthly planning session"],
            },
            {
                "name": "Professional",
                "price": "₦500,000 / month",
                "ideal": "Growing brands needing more volume and strategy",
                "includes": ["20 graphics", "8 reels/videos", "Professional photography session", "Hashtag research", "Community engagement guidance", "Monthly analytics report"],
            },
            {
                "name": "Enterprise",
                "price": "₦1,500,000+ / month",
                "ideal": "Organisations running multiple campaigns",
                "includes": ["Unlimited content within agreed scope", "Multiple campaigns", "Dedicated content strategist", "Monthly production days", "Paid advertising coordination", "Comprehensive reporting", "Quarterly strategy review"],
            },
        ],
        "addons": [],
        "retainer": True,
        "gallery_projects": ["shine-on-stage", "familiar-faces"],
    },
    {
        "slug": "digital-marketing-seo",
        "name": "Digital Marketing & SEO",
        "icon": "compass",
        "short": "Data-driven campaigns that turn visibility into measurable business growth.",
        "hero_desc": "Marketing measured against enquiries and conversions, not vanity numbers.",
        "why": "Traffic without a conversion path is a cost centre. Marketing has to be built with a funnel and a way to prove it worked.",
        "included_summary": "SEO, paid platforms, email and conversion tracking, structured into monthly retainers.",
        "ideal_for": ["Local businesses needing to be found on Google", "Growing companies running multi-channel campaigns", "Enterprises needing dedicated account management"],
        "process": [
            ("Audit", "A review of current SEO, ads and analytics."),
            ("Strategy", "A channel plan matched to budget and goals."),
            ("Execute", "Campaigns launched and optimised."),
            ("Report", "Monthly performance reporting and iteration."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦250,000 / month",
                "ideal": "Businesses starting their marketing engine",
                "includes": ["SEO basics", "Google Business Profile optimisation", "One advertising platform", "Monthly performance report"],
            },
            {
                "name": "Professional",
                "price": "₦600,000 / month",
                "ideal": "Businesses ready for multi-channel campaigns",
                "includes": ["Everything in Essential", "Multi-channel campaigns", "Advanced SEO", "Email marketing", "Conversion tracking", "Landing page optimisation"],
            },
            {
                "name": "Enterprise",
                "price": "₦2,000,000+ / month",
                "ideal": "Organisations needing dedicated strategic support",
                "includes": ["Everything in Professional", "Dedicated account manager", "Marketing strategy workshops", "Cross-platform campaigns", "Advanced analytics", "Quarterly business reviews"],
            },
        ],
        "addons": [("Monthly Analytics Report", "₦75,000–₦250,000"), ("Google Ads Campaign Setup", "₦150,000–₦500,000"), ("Email Newsletter Design", "₦80,000–₦250,000"), ("Landing Page for Campaign", "₦200,000–₦700,000")],
        "retainer": True,
        "gallery_projects": ["market-hours"],
    },
    {
        "slug": "business-brand-consulting",
        "name": "Business & Brand Consulting",
        "icon": "beacon",
        "short": "Strategic guidance for businesses looking to grow, reposition, or professionalise.",
        "hero_desc": "An outside, structured view of your business — and a plan you can actually act on.",
        "why": "Founders are often too close to their own business to see clearly what's holding growth back. A structured outside review shortens that path.",
        "included_summary": "From a single strategy session through to ongoing executive advisory.",
        "ideal_for": ["Founders needing a clear-eyed review", "Growing teams needing structured planning support", "Organisations undergoing digital transformation"],
        "process": [
            ("Review", "A structured audit of the business and its goals."),
            ("Plan", "A written action plan with clear priorities."),
            ("Support", "Ongoing sessions to implement and adjust."),
            ("Measure", "Regular reviews against agreed milestones."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦100,000 / session",
                "ideal": "A single, focused strategy session",
                "includes": ["90-minute consultation", "Business review", "Action plan", "Written recommendations"],
            },
            {
                "name": "Professional",
                "price": "₦600,000 / month",
                "ideal": "Ongoing strategic support",
                "includes": ["Weekly strategy meetings", "Brand development", "Growth planning", "Marketing guidance", "Website and customer journey review"],
            },
            {
                "name": "Enterprise",
                "price": "₦3,000,000+ / month",
                "ideal": "Executive-level, organisation-wide advisory",
                "includes": ["Executive advisory", "Leadership workshops", "Digital transformation planning", "Ongoing strategic support", "Department collaboration", "Long-term implementation guidance"],
            },
        ],
        "addons": [],
        "retainer": True,
        "gallery_projects": [],
    },
    {
        "slug": "ai-automation-solutions",
        "name": "AI Automation Solutions",
        "icon": "circuit",
        "short": "Helping businesses automate repetitive tasks, improve customer experience, and increase operational efficiency.",
        "hero_desc": "Practical automation — chatbots, workflows and integrations — scoped to what your team actually repeats every day.",
        "why": "Most businesses lose hours a week to the same manual steps. The right automation gives that time back without adding headcount.",
        "included_summary": "From a first chatbot and WhatsApp automation through to department-wide, multi-system transformation.",
        "ideal_for": ["Small businesses wanting their first automation win", "Growing teams automating CRM and lead workflows", "Enterprises running department-wide digital transformation"],
        "process": [
            ("Assess", "A process assessment to find the highest-impact automations."),
            ("Build", "Chatbots, workflows and integrations implemented and tested."),
            ("Train", "Staff training and documentation."),
            ("Support", "A support window, with optional ongoing retainer plans."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦500,000 – ₦1,500,000",
                "price_intl": "$1,000 – $3,000",
                "ideal": "Small businesses, restaurants, schools, churches, SMEs, online stores, startups",
                "includes": ["Business process assessment", "AI opportunity discovery session", "AI chatbot installation", "Website chat integration", "FAQ automation", "WhatsApp Business automation", "Basic email automation", "Contact form automation", "Appointment scheduling automation", "Basic CRM connection", "Staff training (2 hours)", "Documentation", "30 days support"],
            },
            {
                "name": "Professional",
                "price": "₦2,000,000 – ₦6,000,000",
                "price_intl": "$4,000 – $12,000",
                "ideal": "Growing teams automating multiple workflows",
                "includes": ["Everything in Essential", "Workflow analysis", "Advanced workflow automation", "CRM integration", "AI email assistant", "Lead qualification automation", "AI customer support", "Automated follow-ups", "Google Workspace integration", "Microsoft 365 integration", "Internal approval workflows", "Reporting dashboard", "90 days support"],
            },
            {
                "name": "Enterprise",
                "price": "₦8,000,000 – ₦50,000,000+",
                "price_intl": "$15,000 – $100,000+",
                "ideal": "Organisations running full digital transformation",
                "includes": ["Complete digital transformation assessment", "AI strategy consulting", "Department-wide automation", "Multi-system integration (ERP/CRM)", "HR automation", "Finance automation", "AI knowledge base", "AI call assistant", "AI customer support centre", "Predictive analytics", "Custom AI solutions", "Executive & staff training", "Dedicated project manager", "Priority support", "Ongoing optimisation"],
            },
        ],
        "addons": [("AI Chatbot Expansion", "₦300,000–₦1,500,000"), ("Additional Workflow Automation", "₦200,000–₦1,000,000"), ("AI Prompt Library for Team", "₦150,000–₦500,000"), ("AI Staff Training Session", "₦200,000–₦800,000")],
        "retainer_plans": [("Basic Support", "₦100,000/month", "$200/month"), ("Professional Support", "₦300,000/month", "$600/month"), ("Enterprise Support", "₦1,000,000+/month", "$2,000+/month")],
        "gallery_projects": [],
    },
    {
        "slug": "training-creative-workshops",
        "name": "Training & Creative Workshops",
        "icon": "torch",
        "short": "Practical, hands-on training programs for individuals, teams, and organisations building creative and digital skills.",
        "hero_desc": "Skills training built around real tools and real portfolios, not generic slides.",
        "why": "Teams and individuals learn fastest by building something real, with feedback from people who do the work professionally.",
        "included_summary": "From a one-day workshop through to multi-day bootcamps and customised corporate training.",
        "ideal_for": ["Students and beginners", "Freelancers building a portfolio", "Companies and institutions training staff at scale"],
        "process": [
            ("Assess", "Understand the participant's level and goals (or, for corporate training, a needs assessment)."),
            ("Curriculum", "A curriculum built around practical exercises."),
            ("Train", "Hands-on sessions with mentorship and feedback."),
            ("Certify", "A certificate and, where relevant, a follow-up session."),
        ],
        "tiers": [
            {
                "name": "Essential",
                "price": "₦50,000 – ₦150,000 / participant",
                "price_intl": "$100 – $300",
                "ideal": "Students, beginners, freelancers",
                "includes": ["1–2 day duration", "Training materials", "Workbook", "Practical exercises", "Certificate", "Q&A session", "Topics: WordPress, Canva, Photography, Branding, AI Tools, UI Design"],
            },
            {
                "name": "Professional",
                "price": "₦250,000 – ₦800,000",
                "price_intl": "$500 – $1,500",
                "ideal": "Learners wanting a full bootcamp experience",
                "includes": ["3–5 day duration", "Hands-on projects", "Templates", "Resources", "Certificate", "Mentorship", "Portfolio review", "Community access"],
            },
            {
                "name": "Enterprise",
                "price": "₦1,000,000 – ₦8,000,000",
                "price_intl": "$2,000 – $15,000",
                "ideal": "Companies, NGOs, banks, schools, government agencies",
                "includes": ["Training needs assessment", "Customised curriculum", "On-site or virtual training", "Staff handbook", "Practical sessions", "Assessments", "Certificate", "Follow-up session"],
            },
        ],
        "addons": [("Individual Coaching — 1 Hour", "₦30,000–₦75,000"), ("Individual Coaching — Half Day", "₦100,000–₦250,000"), ("Mentorship Program (8–12 weeks)", "₦300,000–₦1,500,000"), ("Online Courses", "₦20,000–₦150,000"), ("Corporate Retainer (monthly)", "₦500,000–₦5,000,000/mo")],
        "gallery_projects": [],
    },
]

SERVICES_BY_SLUG = {s["slug"]: s for s in SERVICES}

BUNDLES = [
    {"name": "Brand Launch Bundle", "combo": "Brand Identity + Website (matching tier)", "discount": "10% off combined price"},
    {"name": "Visual Content Bundle", "combo": "Photography + Videography (same shoot day)", "discount": "15% off combined price"},
    {"name": "Growth Bundle", "combo": "Website (Professional) + Social Media + Digital Marketing", "discount": "12% off, 3-month commitment required"},
    {"name": "Full-Service Launch", "combo": "Brand Identity + Website + Photography + Social Media (1st month)", "discount": "18% off combined price"},
]

RETAINER_TERMS = [
    "Minimum commitment: 3 consecutive months, billed monthly.",
    "Early termination before the 3-month minimum: remaining balance due at 50%, and any onboarding discount is forfeited.",
    "Renewal incentive: clients renewing for a second consecutive term receive one complimentary add-on from the relevant service category.",
]

PREMIUM_OPTIONS = [
    ("Priority Project Queue", "+15–25% of project fee"),
    ("Express Delivery", "+25–50% of project fee"),
    ("Dedicated Project Manager", "₦250,000–₦1,000,000/project"),
    ("Monthly Strategy Review", "₦100,000–₦500,000"),
    ("Quarterly Business Review", "₦300,000–₦1,500,000"),
]

# ---------------------------------------------------------------------------
# ACADEMY — one course track per service line, plus the flagship
# self-study guide product (Starter live, Professional/Ultimate marked
# "Coming Soon" per the internal sequencing note: only Starter is fully
# buildable today).
# ---------------------------------------------------------------------------

# Course prices are scoped from the verified "Online Courses" add-on line in
# the Pricing Guide's Additional Training Options table (₦20,000–₦150,000 /
# $50–$300), applied per individual course rather than a bundle, with GBP/EUR
# computed at the same USD ratio used for the Core Guide bundle pricing below.
COURSES = [
    {
        "slug": "brand-strategy-identity-design",
        "service_slug": "brand-identity-logo-design",
        "title": "Brand Strategy & Identity Design",
        "level": "Beginner → Intermediate",
        "duration": "6 modules · self-paced",
        "summary": "Build a complete brand identity from positioning through to a usable guideline document.",
        "outcomes": ["Define a brand's positioning and audience", "Design a logo system that works at every size", "Choose a colour and type system with intent", "Assemble a brand guideline document"],
        "curriculum": ["Positioning & audience", "Logo concepts & construction", "Colour & type systems", "Applying identity to collateral", "Writing brand guidelines", "Presenting to a client"],
        "price": {"ngn": "₦35,000", "usd": "$45", "gbp": "£37", "eur": "€42"},
    },
    {
        "slug": "responsive-website-design-wordpress",
        "service_slug": "website-design-development",
        "title": "Responsive Website Design with WordPress",
        "level": "Beginner",
        "duration": "8 modules · self-paced",
        "summary": "Plan, design and launch a responsive WordPress site from a blank domain.",
        "outcomes": ["Structure a sitemap and information architecture", "Build responsive pages with a modern theme", "Set up forms, SEO basics and analytics", "Launch and hand off a site with confidence"],
        "curriculum": ["Planning & sitemaps", "WordPress fundamentals", "Responsive page design", "Forms & integrations", "On-page SEO basics", "Speed & security", "Analytics setup", "Launch checklist"],
        "price": {"ngn": "₦25,000", "usd": "$32", "gbp": "£26", "eur": "€30"},
    },
    {
        "slug": "ui-ux-fundamentals",
        "service_slug": "ui-ux-design",
        "title": "UI/UX Design Fundamentals",
        "level": "Beginner → Intermediate",
        "duration": "7 modules · self-paced",
        "summary": "Go from wireframe to a working prototype using a real product brief.",
        "outcomes": ["Run a lightweight user research pass", "Wireframe and map user flows", "Design a small component library", "Prototype and test with real users"],
        "curriculum": ["Discovery & research basics", "Wireframing", "User flows", "Visual design & components", "Prototyping", "Usability testing", "Developer handoff"],
        "price": {"ngn": "₦35,000", "usd": "$45", "gbp": "£37", "eur": "€42"},
    },
    {
        "slug": "professional-photography-fundamentals",
        "service_slug": "photography",
        "title": "Professional Photography Fundamentals",
        "level": "Beginner",
        "duration": "6 modules · self-paced",
        "summary": "Learn the technical and creative fundamentals behind a professional shoot.",
        "outcomes": ["Understand light, composition and exposure", "Direct a subject with confidence", "Edit and colour-grade a shoot", "Build a client-ready delivery workflow"],
        "curriculum": ["Camera & exposure fundamentals", "Composition & light", "Directing people", "Location & studio setups", "Editing workflow", "Delivering to clients"],
        "price": {"ngn": "₦25,000", "usd": "$32", "gbp": "£26", "eur": "€30"},
    },
    {
        "slug": "video-production-storytelling",
        "service_slug": "videography-documentary-production",
        "title": "Video Production & Storytelling",
        "level": "Intermediate",
        "duration": "7 modules · self-paced",
        "summary": "Plan, shoot and edit a short brand film from script to final cut.",
        "outcomes": ["Write a simple script or interview outline", "Shoot with intentional camera movement", "Edit a paced, well-structured cut", "Colour grade and mix sound"],
        "curriculum": ["Story & scripting", "Camera & lighting on location", "Interviews", "Editing structure & pacing", "Colour grading", "Sound design", "Exporting for platforms"],
        "price": {"ngn": "₦45,000", "usd": "$58", "gbp": "£48", "eur": "€54"},
    },
    {
        "slug": "social-media-content-systems",
        "service_slug": "social-media-content-creation",
        "title": "Social Media Content Systems",
        "level": "Beginner",
        "duration": "5 modules · self-paced",
        "summary": "Build a repeatable content calendar and production system for any brand.",
        "outcomes": ["Plan a monthly content calendar", "Batch-produce graphics and short video", "Write captions that match a brand voice", "Read basic analytics to improve output"],
        "curriculum": ["Content pillars & calendars", "Batch production", "Caption writing & voice", "Hashtag & discovery basics", "Reading analytics"],
        "price": {"ngn": "₦25,000", "usd": "$32", "gbp": "£26", "eur": "€30"},
    },
    {
        "slug": "digital-marketing-seo-essentials",
        "service_slug": "digital-marketing-seo",
        "title": "Digital Marketing & SEO Essentials",
        "level": "Beginner → Intermediate",
        "duration": "6 modules · self-paced",
        "summary": "Set up a marketing engine that you can measure and improve month over month.",
        "outcomes": ["Set up a Google Business Profile properly", "Run a first paid campaign on one platform", "Understand core on-page SEO", "Track conversions, not just traffic"],
        "curriculum": ["SEO fundamentals", "Google Business Profile", "Paid platform basics", "Email marketing basics", "Conversion tracking", "Monthly reporting"],
        "price": {"ngn": "₦35,000", "usd": "$45", "gbp": "£37", "eur": "€42"},
    },
    {
        "slug": "brand-consulting-growth-strategy",
        "service_slug": "business-brand-consulting",
        "title": "Brand & Growth Strategy for Founders",
        "level": "Intermediate",
        "duration": "5 modules · self-paced",
        "summary": "Structure a growth plan for your own business the way a consultant would.",
        "outcomes": ["Run a structured business review", "Identify the highest-leverage priorities", "Write a one-page action plan", "Set up a review cadence"],
        "curriculum": ["Structured business review", "Positioning & differentiation", "Prioritisation frameworks", "Writing an action plan", "Review cadence & accountability"],
        "price": {"ngn": "₦45,000", "usd": "$58", "gbp": "£48", "eur": "€54"},
    },
    {
        "slug": "ai-automation-for-business",
        "service_slug": "ai-automation-solutions",
        "title": "AI Automation for Business",
        "level": "Beginner → Intermediate",
        "duration": "6 modules · self-paced",
        "summary": "Identify and build practical automations for a real business, without needing to code.",
        "outcomes": ["Find the highest-impact tasks to automate", "Set up a chatbot and WhatsApp automation", "Connect basic CRM and email workflows", "Document and hand off an automation"],
        "curriculum": ["Finding automation opportunities", "Chatbots & WhatsApp automation", "Email & form automation", "CRM connections", "Testing & documentation", "Handoff & maintenance"],
        "price": {"ngn": "₦35,000", "usd": "$45", "gbp": "£37", "eur": "€42"},
    },
    {
        "slug": "train-the-trainer-creative-workshops",
        "service_slug": "training-creative-workshops",
        "title": "Train the Trainer: Running Creative Workshops",
        "level": "Intermediate",
        "duration": "4 modules · self-paced",
        "summary": "Design and deliver a hands-on creative workshop that people actually finish.",
        "outcomes": ["Structure a curriculum around outcomes, not slides", "Design practical exercises with feedback loops", "Facilitate a session with mixed skill levels", "Build a completion certificate learners value"],
        "curriculum": ["Curriculum design", "Practical exercise design", "Facilitation techniques", "Assessment & certification"],
        "price": {"ngn": "₦45,000", "usd": "$58", "gbp": "£48", "eur": "€54"},
    },
]

COURSES_BY_SLUG = {c["slug"]: c for c in COURSES}

# The flagship self-study product (three pricing tiers). Per the internal
# sequencing note in the Bundle & Pricing Copy doc, only "Starter" is fully
# buildable today — Professional and Ultimate are marked Coming Soon.
GUIDE_BUNDLES = [
    {
        "key": "starter",
        "name": "Starter",
        "subtitle": "Get the Complete Guide",
        "price_ngn": "₦12,000",
        "price_usd": "$15",
        "price_gbp": "£12",
        "price_eur": "€14",
        "includes": ["The full Core Guide — 9 modules, 46 pages", "Companion Workbook built into every module"],
        "best_for": "Beginners who want one complete, structured document.",
        "available": True,
    },
    {
        "key": "professional",
        "name": "Professional",
        "subtitle": "The Complete Self-Study System",
        "price_ngn": "₦25,000",
        "price_usd": "$29",
        "price_gbp": "£24",
        "price_eur": "€27",
        "includes": ["Everything in Starter", "AI Prompt Library", "Templates Pack (16 tools)", "Cheat Sheets (10 one-pagers)"],
        "best_for": "Learners who want a complete toolkit, not just a book to read.",
        "available": False,
    },
    {
        "key": "ultimate",
        "name": "Ultimate",
        "subtitle": "The Full Academy Experience",
        "price_ngn": "₦50,000",
        "price_usd": "$59",
        "price_gbp": "£48",
        "price_eur": "€55",
        "includes": ["Everything in Professional", "Swipe File Library", "Resource Vault", "Portfolio Builder", "Completion Certificate", "Future updates"],
        "best_for": "Learners who want the highest-value, most complete version.",
        "available": False,
    },
]

# ---------------------------------------------------------------------------
# WORK — story-led case studies (kept from the earlier photography build,
# recontextualised as agency case studies spanning multiple service lines).
# ---------------------------------------------------------------------------

WORK_PROJECTS = [
    {"slug": "dusk-crowds-beneath-the-footbridge", "title": "Dusk Crowds Beneath the Footbridge", "category": "Documentary / Photography", "location": "Lagos, Nigeria", "year": "2026", "size": "feature", "desc": "A study of movement, architecture and human presence beneath the changing light of Lagos.", "services": ["photography"]},
    {"slug": "geometry-of-the-city", "title": "Geometry of the City", "category": "Architecture / Brand Identity", "location": "Lagos, Nigeria", "year": "2026", "size": "portrait", "desc": "An architectural identity project pairing structural photography with a new visual system.", "services": ["photography", "brand-identity-logo-design"]},
    {"slug": "the-quiet-office", "title": "The Quiet Office", "category": "Corporate / Brand Identity", "location": "Lagos, Nigeria", "year": "2026", "size": "landscape", "desc": "A rebrand and corporate photography library for a professional services firm.", "services": ["brand-identity-logo-design", "photography"]},
    {"slug": "the-new-terminal", "title": "The New Terminal", "category": "Website / UI-UX", "location": "Lagos, Nigeria", "year": "2026", "size": "landscape", "desc": "A full website rebuild and interface redesign for a logistics operator.", "services": ["website-design-development", "ui-ux-design"]},
    {"slug": "new-collection-still-life", "title": "New Collection, Still Life", "category": "Product Photography", "location": "Lagos, Nigeria", "year": "2026", "size": "portrait", "desc": "Clean, considered product photography for a seasonal e-commerce launch.", "services": ["photography"]},
    {"slug": "shine-on-stage", "title": "Shine on Stage", "category": "Event / Video / Social", "location": "Lagos, Nigeria", "year": "2026", "size": "small", "desc": "Live event coverage across photography, highlight video and same-week social content.", "services": ["photography", "videography-documentary-production", "social-media-content-creation"]},
    {"slug": "market-hours", "title": "Market Hours", "category": "Documentary / Digital Marketing", "location": "Lagos, Nigeria", "year": "2026", "size": "small", "desc": "A documentary photo series paired with a local SEO and Google Business overhaul.", "services": ["photography", "digital-marketing-seo"]},
    {"slug": "familiar-faces", "title": "Familiar Faces", "category": "Portrait / Social Content", "location": "Lagos, Nigeria", "year": "2026", "size": "full", "desc": "An ongoing portrait series feeding a brand's monthly social content system.", "services": ["photography", "social-media-content-creation"]},
]

WORK_BY_SLUG = {p["slug"]: p for p in WORK_PROJECTS}

# ---------------------------------------------------------------------------
# JOURNAL
# ---------------------------------------------------------------------------

JOURNAL_ARTICLES = [
    {
        "slug": "the-art-of-seeing", "category": "Photography", "title": "The Art of Seeing: Photography Beyond the Frame",
        "excerpt": "Photography is not simply about capturing what is in front of the camera — it's about observing character, atmosphere and moment.",
        "date": "March 2026", "read_time": "5 min read",
        "body": [
            "Most briefs start with a shot list. The good ones end somewhere else — a conversation about what a business actually wants a viewer to feel before they read a single word of copy.",
            "A photograph earns its place on a homepage or a wall by doing more than documenting a person, product or space. It has to carry atmosphere: the quality of the light, the moment just before or after the obvious one, the detail a faster photographer would have missed.",
            "That's the standard we hold every shoot to, corporate headshots included. Technical competence — exposure, focus, colour — is the entry fee. What separates a usable photograph from a memorable one is restraint: knowing which frame to keep, and which to leave on the card.",
        ],
    },
    {
        "slug": "finding-geometry-in-the-streets-of-lagos", "category": "Photography", "title": "Finding Geometry in the Streets of Lagos",
        "excerpt": "How structure, repetition and light turn an ordinary street into a considered photograph.",
        "date": "February 2026", "read_time": "4 min read",
        "body": [
            "Lagos rarely holds still long enough for a considered photograph — which is exactly why structure matters more here than almost anywhere else we shoot.",
            "A market awning, a stack of okada helmets, the repeating grille of a tenement building: none of it reads as \"architecture\" the way a gallery would define it, but all of it gives a frame something to organise itself around. Repetition and geometry turn chaos into composition without changing a single thing about the scene itself.",
            "This is the same instinct we bring to architectural and urban commissions — find the lines the space already has, and let them do the compositional work, rather than imposing a look the location was never going to support.",
        ],
    },
    {
        "slug": "why-great-corporate-photography-matters", "category": "Business", "title": "Why Great Corporate Photography Matters",
        "excerpt": "The image library behind your brand is doing more selling than most of your marketing copy.",
        "date": "January 2026", "read_time": "4 min read",
        "body": [
            "Nobody reads an \u201cAbout Us\u201d page as closely as they look at the photo next to it. Team headshots, office shots, event coverage — these are quietly doing more persuading than most of the copy a business spends weeks writing.",
            "Generic stock photography, or worse, a phone photo taken under office fluorescents, tells a visitor the business didn't think this mattered. A proper corporate shoot — planned lighting, consistent styling, a photographer who understands how the images will actually be used — tells them the opposite.",
            "It's also cheaper than it looks over time: one well-planned half-day session replaces a year of scrambling for a decent headshot before every press mention or LinkedIn post.",
        ],
    },
    {
        "slug": "a-logo-isnt-a-brand", "category": "Branding", "title": "A Logo Isn't a Brand",
        "excerpt": "A mark is the entry point. What actually holds a brand together is a documented, consistently-applied system.",
        "date": "April 2026", "read_time": "6 min read",
        "body": [
            "Most rebrand conversations start with \u201cwe need a new logo\u201d and end somewhere else entirely — usually a conversation about positioning, tone of voice, and how the business actually wants to be perceived.",
            "A logo is one asset. A brand is a system: a consistent visual language and voice that shows up the same way whether a customer meets it on Instagram, on an invoice, or in a boardroom. Without that system written down, consistency depends on whoever happens to be making the next asset.",
            "That's why every brand identity engagement on our side starts with discovery and, from Professional up, a full strategy session — the mark has to follow the positioning, not the other way around. A comprehensive guide is what makes the identity survive contact with everyone who isn't in the room when it was designed.",
        ],
    },
    {
        "slug": "practical-ai-automation-for-small-business", "category": "Technology", "title": "Practical AI Automation for Small Business",
        "excerpt": "You don't need a full digital transformation to get real time back — a WhatsApp bot and one workflow is often enough to start.",
        "date": "May 2026", "read_time": "5 min read",
        "body": [
            "\"AI automation\" sounds like a six-month enterprise project. For most small businesses, the first useful step is much smaller: a WhatsApp bot that answers the five questions every customer asks before a human ever needs to reply.",
            "The businesses that get the most out of automation early on aren't the ones with the biggest budget — they're the ones who can point to one repetitive task and say \"this happens every single day, and it's always the same.\" Appointment scheduling, FAQ answers, and lead capture from a contact form are the highest-leverage places to start.",
            "Our Essential AI package is built around exactly that: a chatbot, WhatsApp automation, and basic workflow connections, delivered in one to three weeks — proof the concept works before anyone commits to a larger, department-wide build.",
        ],
    },
    {
        "slug": "what-makes-a-website-actually-convert", "category": "Design", "title": "What Makes a Website Actually Convert",
        "excerpt": "It's rarely the visual polish. It's whether a visitor can tell, in five seconds, what to do next.",
        "date": "June 2026", "read_time": "5 min read",
        "body": [
            "It's rarely the visual polish that determines whether a site converts. It's whether a visitor, five seconds in, can tell what the business does and what they're meant to do next.",
            "We see the same pattern across industries: a beautifully designed homepage with no clear next step, three competing calls to action above the fold, or a contact form buried two clicks deeper than it needs to be. None of that is a design failure in the traditional sense — it's a clarity failure.",
            "Before we touch a single visual element on a project, we map the path a real visitor takes: what they need to believe, in what order, before they're ready to enquire. The layout, the copy and the calls to action all follow from that map — which is also why a Professional or Enterprise build includes analytics and conversion tracking from day one, not as an afterthought.",
        ],
    },
]

JOURNAL_BY_SLUG = {a["slug"]: a for a in JOURNAL_ARTICLES}

FAQS = [
    ("How does the three-tier pricing structure work?", "Every service line — from branding to AI automation — is offered at Essential, Professional and Enterprise levels. Essential suits startups and small businesses, Professional suits growing companies needing more customisation, and Enterprise is fully tailored for corporations, government agencies and institutions. All prices are starting points; every project begins with a free discovery call to confirm an exact quote."),
    ("Do you work with clients outside Nigeria?", "Yes. We're based in Lagos and serve clients across Nigeria, West Africa and internationally — most of the process runs comfortably over video calls and shared documents."),
    ("Can I combine multiple services?", "Yes — combining services across disciplines qualifies for one of our bundle discounts (see the Pricing page), such as the Brand Launch Bundle or Full-Service Launch."),
    ("What's the typical timeline?", "It depends on the service and tier. Websites run 2–6 weeks (Essential) up to 12+ weeks (Enterprise); brand identity runs 1–3 weeks up to 6+ weeks; photography is usually delivered within 1–2 weeks of the shoot. Ask about Express Delivery or Priority Queue if you're on a deadline."),
    ("How do monthly retainers work?", "Retainers for social media, digital marketing and business consulting require a 3-month minimum commitment, billed monthly. Ending early before the minimum means the remaining balance is due at 50%, and any onboarding discount is forfeited. Renewing for a second term earns one complimentary add-on."),
    ("Is the Academy self-paced?", "Yes — every course is self-paced and accessible through your student dashboard once payment is confirmed. Courses cover the same ten disciplines we work in professionally, so you're learning from the same process we use with clients."),
    ("Do I need a real account to use the student dashboard?", "The registration, sign-in and dashboard experience in this build runs entirely in your browser (no live server yet) so you can click through the full flow. See the Academy page for details on what a live version would require."),
]

# Sourced from the 5-Year Growth Strategy & Business Plan document.
KEY_DIFFERENTIATORS = [
    "Full-service capability under one roof, reducing the need for clients to coordinate multiple vendors.",
    "Transparent, tiered pricing that simplifies client decision-making at every stage of growth.",
    "Early investment in AI automation capability, ahead of many local competitors.",
    "A phased growth model built around recurring revenue, not just one-off projects.",
]

FIVE_YEAR_ROADMAP = [
    ("Year 1", "Build the Foundation", "Deliver consistent quality across core creative services, build a strong portfolio, and establish SOPs, proposal templates and a referral pipeline."),
    ("Year 2", "Expand the Offering", "Launch digital marketing and business & brand consulting as standalone offerings, and introduce monthly retainer contracts."),
    ("Year 3", "Build Recurring Revenue", "Grow the retainer client base as a share of total revenue, and begin piloting AI Automation Essential packages with early-adopter clients."),
    ("Year 4", "Scale AI & Technology", "Formalise AI Automation Solutions across all three tiers and build dedicated CRM/ERP integration capability."),
    ("Year 5", "Build the Ecosystem", "Launch Lari Academy at scale — bootcamps, online courses and mentorship — and diversify revenue across creative services, AI and education."),
]

# Founder identity per the supplied brand-kit assets and founder headshot.
FOUNDER = {
    "name": "Oluwatimilehin Monilari",
    "title": "Founder & Creative Director",
    "photo": "assets/img/founder-oluwatimilehin-monilari.jpg",
    "bio": "Oluwatimilehin founded Lari Creative Studio to bring brand strategy, design and technology under one roof, so clients get one accountable team instead of a folder of disconnected vendors. That founder-led structure is why every engagement — from a first logo to an Enterprise AI build — is still held to the same standard of craft.",
}

# Academy-specific FAQ, appended after the general list on the academy page
ACADEMY_FAQS = [
    ("Do I have to pay for courses?", "Yes — creating an Academy account is free, but each course is a one-time paid enrolment (see each course page for its price). Course access unlocks as soon as payment is confirmed."),
    ("What currencies can I pay in?", "Every course and the Core Guide can be paid for in Nigerian Naira, US Dollars, British Pounds or Euros — choose your currency at checkout."),
    ("Will I get a certificate?", "The Ultimate guide tier and the Enterprise/Professional workshop tiers include a completion certificate. Self-paced Academy courses currently track progress on your dashboard; certificates for individual courses are on our roadmap."),
    ("Can my whole team enrol?", "Yes — for teams of five or more, contact us about a corporate training retainer instead of individual registrations; it includes a customised curriculum and on-site or virtual delivery."),
]
