css_file = r'd:/eonix_systems/Development/eonix_systems_website/css/about.css'

new_css = """/* =========================
   ABOUT PAGE: ENGINEERING MANIFESTO
   ========================= */

/* GLOBAL SPACING overrides */
.manifesto-section {
    padding-top: 40px;
    padding-bottom: 160px; /* Massive breathing room per prompt */
}

.manifesto-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 24px;
}

.manifesto-container.wide {
    max-width: 1200px;
}

/* TYPOGRAPHY overrides */
.manifesto-title {
    font-size: 3rem;
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 56px;
    color: #fff;
    font-family: 'Outfit', sans-serif;
}

.manifesto-lead {
    font-size: 1.5rem;
    color: var(--text-secondary);
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
}

.manifesto-p {
    font-size: 1.25rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin: 0 auto 24px auto;
    max-width: 700px; /* Constrict reading width */
}

.manifesto-p.emphasize {
    font-size: 1.4rem;
    font-weight: 600;
}

.text-bold { font-weight: 600; }
.text-red { color: #ff4a4a; }
.text-red-glow {
    color: #ff4a4a;
    text-shadow: 0 0 20px rgba(255, 74, 74, 0.4);
}

/* LISTS & STACKS */
.problem-list {
    margin: 40px auto;
    max-width: 700px;
    padding-left: 20px;
    border-left: 2px solid rgba(255, 74, 74, 0.4); /* Slight red indicator */
}

.problem-list p {
    font-size: 1.2rem;
    color: #cbd5e1;
    margin-bottom: 16px;
    line-height: 1.6;
}

.realization-stack {
    display: flex;
    flex-direction: column;
    gap: 16px;
    align-items: center;
}

.realization-stack span {
    font-size: 1.3rem;
    color: #fff;
    background: rgba(255, 255, 255, 0.05);
    padding: 16px 32px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.1);
}

/* FEATURE HORIZONTAL TRIO */
.feature-trio {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
}

.f-block {
    background: rgba(10, 12, 14, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 40px 32px;
    border-radius: 12px;
    text-align: left;
}

.f-block h4 {
    font-size: 1.4rem;
    color: var(--accent-primary);
    margin-bottom: 16px;
    font-family: 'Outfit', sans-serif;
    letter-spacing: 1px;
}

.f-block p {
    font-size: 1.1rem;
    color: var(--text-secondary);
    line-height: 1.6;
    margin: 0;
}

.premium-lift {
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease, border-color 0.4s ease, background 0.4s ease;
}

.premium-lift:hover {
    transform: translateY(-8px);
    border-color: rgba(0, 229, 255, 0.5);
    box-shadow: 0 15px 35px rgba(0, 229, 255, 0.1);
    background: rgba(0, 229, 255, 0.02);
}

/* CHECKLISTS */
.check-list {
    display: flex;
    flex-direction: column;
    gap: 24px;
    max-width: 700px;
    margin: 0 auto;
    text-align: left;
}

.check-list-centered {
    display: flex;
    flex-direction: column;
    gap: 16px;
    max-width: 700px;
    margin: 0 auto;
}

.check-item {
    font-size: 1.3rem;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 16px;
}

.check-item-card {
    font-size: 1.25rem;
    color: #fff;
    background: rgba(10, 12, 14, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.05);
    padding: 24px 32px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    gap: 16px;
}

.check-icon {
    color: var(--accent-primary);
    font-weight: 700;
    text-shadow: 0 0 10px rgba(0, 229, 255, 0.8);
    font-size: 1.4rem;
}

/* BACKGROUND UTILS */
.bg-gradient-dark {
    background: linear-gradient(180deg, transparent, rgba(0, 229, 255, 0.02), transparent);
    border-top: 1px solid rgba(255, 255, 255, 0.02);
    border-bottom: 1px solid rgba(255, 255, 255, 0.02);
}

.pt-80 { padding-top: 80px; }
.pb-80 { padding-bottom: 80px; }
.mt-32 { margin-top: 32px; }
.mt-48 { margin-top: 48px; }
.mt-64 { margin-top: 64px; }

/* RESPONSIVE */
@media(max-width: 900px) {
    .feature-trio { grid-template-columns: 1fr; }
    .manifesto-title { font-size: 2.2rem !important; }
    .manifesto-p { font-size: 1.15rem; }
    .check-item { font-size: 1.1rem; }
}
"""

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(new_css)
print("Updated about.css")
