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

        <div class="sys-content who-list">
          <div class="who-list-item who-theme-robotics reveal" style="--delay: 100ms;">
            <span class="who-card-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="9" rx="2"></rect><path d="M12 4v3"></path><path d="M9 20v-4"></path><path d="M15 20v-4"></path><path d="M4 10h3"></path><path d="M17 10h3"></path><circle cx="10" cy="11" r="1"></circle><circle cx="14" cy="11" r="1"></circle><path d="M10 14h4"></path></svg>
            </span>
            <span class="who-card-title">Robotics Teams</span>
          </div>
          <div class="who-list-item who-theme-startups reveal" style="--delay: 200ms;">
            <span class="who-card-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4c2.8 1.1 5 3.3 6 6l-5 1-2-2 1-5Z"></path><path d="M10 14 4 20"></path><path d="M8 9c1.8-1.8 4-2.8 6-3"></path><path d="M9 15c-2.2.2-4.1-.1-5.5-1.5"></path><path d="M15 9c1.4 1.4 1.7 3.3 1.5 5.5"></path></svg>
            </span>
            <span class="who-card-title">Hardware Startups</span>
          </div>
          <div class="who-list-item who-theme-automation reveal" style="--delay: 300ms;">
            <span class="who-card-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3.5"></circle><path d="M12 2v3"></path><path d="M12 19v3"></path><path d="M4.9 4.9l2.1 2.1"></path><path d="M17 17l2.1 2.1"></path><path d="M2 12h3"></path><path d="M19 12h3"></path><path d="M4.9 19.1 7 17"></path><path d="M17 7l2.1-2.1"></path></svg>
            </span>
            <span class="who-card-title">Automation Engineers</span>
          </div>
          <div class="who-list-item who-theme-labs reveal" style="--delay: 400ms;">
            <span class="who-card-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M10 3v5l-5.5 9.2A2.2 2.2 0 0 0 6.4 21h11.2a2.2 2.2 0 0 0 1.9-3.3L14 8V3"></path><path d="M9 13h6"></path><path d="M8 17h8"></path></svg>
            </span>
            <span class="who-card-title">R&amp;D Labs</span>
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
