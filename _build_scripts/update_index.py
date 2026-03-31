import re
import os

html_file = r'd:/eonix_systems/Development/eonix_systems_website/index.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_main = """<main class="page-wrapper">
      <!-- HERO -->
      <section class="home-root page-section hero-animated-grid">
        <div class="home-hero-inner reveal reveal-scale">
          <h1 class="home-title">
            Build Systems.<br />
            <span class="text-accent">Not Setups.</span>
          </h1>

          <p class="home-subtitle">
            A unified embedded platform where power, communication, sensing, and actuation are engineered as one system — not patched together.
          </p>

          <div class="hero-actions">
            <a class="btn-primary" href="ecosystem.html">
              Explore Ecosystem
              <span class="btn-arrow">→</span>
            </a>
            <a class="btn-secondary" href="product.html">
              View Products
              <span class="btn-arrow">→</span>
            </a>
          </div>
        </div>
      </section>

      <!-- WHY EONIX EXISTS -->
      <section class="home-problem page-section reveal reveal-scale">
        <h2 class="home-section-title">Why Eonix Exists</h2>

        <div class="connected-cards-container">
          <div class="audience-item connected-card glass-panel hover-premium reveal" style="--delay: 100ms;">
             <h3>Power Stage</h3>
             <p>Controlled, programmable power with hardware-enforced protection. Stable under real loads, not just lab conditions.</p>
          </div>
          <div class="connector-line reveal" style="--delay: 200ms;"></div>
          <div class="audience-item connected-card glass-panel hover-premium reveal" style="--delay: 300ms;">
             <h3>Sensor Stage</h3>
             <p>Structured sensing with deterministic communication. No address conflicts, no protocol chaos.</p>
          </div>
          <div class="connector-line reveal" style="--delay: 400ms;"></div>
          <div class="audience-item connected-card glass-panel hover-premium reveal" style="--delay: 500ms;">
             <h3>Actuator Stage</h3>
             <p>High-current control systems designed for real-world loads. Built for control, not just switching.</p>
          </div>
        </div>
      </section>

      <!-- BUILT FOR DEPLOYMENT -->
      <section class="home-difference page-section reveal reveal-scale">
        <h2 class="home-section-title">Built for Deployment, Not Demos</h2>

        <div class="deployment-grid">
          <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 100ms;">
            <h3>Protected Hardware</h3>
            <p>Hardware-level protection that works without firmware. Failure handling is physical, not optional.</p>
          </div>
          <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 200ms;">
            <h3>Deterministic Communication</h3>
            <p>No bus conflicts. No unpredictable behavior. System timing stays consistent as you scale.</p>
          </div>
          <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 300ms;">
            <h3>Tight Integration</h3>
            <p>Modules are designed to work together — not adapted to fit later.</p>
          </div>
          <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 400ms;">
            <h3>Real-World Ready</h3>
            <p>Built for robotics, automation, and systems that operate outside controlled environments.</p>
          </div>
        </div>
      </section>

      <!-- GAP SECTION -->
      <section class="home-gap page-section">
        <h2 class="home-section-title reveal">The Gap We’re Fixing</h2>

        <div class="gap-vs-container">
          <div class="gap-card hobby-card glass-panel hover-premium reveal reveal-left" style="--delay: 100ms;">
            <h4>Hobby Systems</h4>
            <p>Easy to start.<br>Breaks under complexity.</p>
          </div>
          <div class="gap-vs-text reveal" style="--delay: 200ms;">VS</div>
          <div class="gap-card industrial-card glass-panel hover-premium reveal reveal-right" style="--delay: 300ms;">
            <h4>Industrial Systems</h4>
            <p>Powerful.<br>Rigid, expensive, slow to adapt.</p>
          </div>
        </div>

        <div class="gap-center glass-panel hover-premium reveal reveal-scale" style="--delay: 600ms;">
          <h3 class="text-accent" style="margin-bottom: 0.5rem;">Eonix</h3>
          <p>Development-grade infrastructure for building real systems — without the cost and rigidity of industrial solutions.</p>
        </div>
      </section>

      <!-- WHO IT'S FOR -->
      <section class="home-who page-section reveal">
        <h2 class="home-section-title">Who It’s For</h2>

        <div class="who-grid">
          <div class="who-item glass-panel hover-premium reveal" style="--delay: 100ms;">
            <svg class="who-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            <h4>Robotics Teams</h4>
          </div>
          <div class="who-item glass-panel hover-premium reveal" style="--delay: 200ms;">
            <svg class="who-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="4" y="4" width="16" height="16" rx="2" ry="2"/><line x1="9" y1="9" x2="15" y2="15"/><line x1="15" y1="9" x2="9" y2="15"/></svg>
            <h4>Hardware Startups</h4>
          </div>
          <div class="who-item glass-panel hover-premium reveal" style="--delay: 300ms;">
            <svg class="who-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2v6"/><path d="M12 18v4"/><path d="M4.93 4.93l4.24 4.24"/><path d="M14.83 14.83l4.24 4.24"/><path d="M2 12h6"/><path d="M18 12h4"/><path d="M4.93 19.07l4.24-4.24"/><path d="M14.83 9.17l4.24-4.24"/></svg>
            <h4>Automation Engineers</h4>
          </div>
          <div class="who-item glass-panel hover-premium reveal" style="--delay: 400ms;">
            <svg class="who-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" y1="12" x2="9" y2="12"/></svg>
            <h4>R&D Labs</h4>
          </div>
        </div>

        <p class="who-summary text-accent glow-text reveal" style="--delay: 600ms;">
          If you're building systems that need to work outside the lab — this is for you.
        </p>
      </section>

      <!-- CLOSING CTA -->
      <section class="home-direction page-section hero-animated-grid reveal reveal-scale">
        <h2 class="home-section-title" style="margin-bottom: 2rem;">
          Start Building Real Systems
        </h2>

        <div class="hero-actions">
          <a class="btn-primary" href="product.html">
            Explore Products
            <span class="btn-arrow">→</span>
          </a>
          <a class="btn-secondary" href="ecosystem.html">
            Read Technical Architecture
            <span class="btn-arrow">→</span>
          </a>
        </div>
      </section>
    </main>"""

new_content = re.sub(r'<main class="page-wrapper">\s*<!-- HERO -->.*?</main>', new_main, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Updated index.html successfully')
