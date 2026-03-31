html_file = r'd:/eonix_systems/Development/eonix_systems_website/about.html'

new_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta
      name="description"
      content="Eonix Systems is an engineering-first hardware company building intelligent power infrastructure for embedded and robotic systems."
    />
    <meta property="og:title" content="About Us | Eonix Systems" />
    <meta
      property="og:description"
      content="We design systems that are predictable, observable, and safe — not just functional. Learn about our engineering philosophy."
    />
    <title>About Us | Eonix Systems</title>

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Outfit:wght@500;600;700&display=swap"
      rel="stylesheet"
    />

    <link rel="stylesheet" href="css/base.css?v=20" />
    <link rel="stylesheet" href="css/layout.css?v=20" />
    <link rel="stylesheet" href="css/nav.css?v=20" />
    <link rel="stylesheet" href="css/animations.css?v=20" />
    <link rel="stylesheet" href="css/footer.css?v=20" />
    <link rel="stylesheet" href="css/about.css?v=20" />
    <link rel="stylesheet" href="css/home.css?v=20" />
    <link rel="icon" href="assets/EONIX SYSTEMS LOGO .png" type="image/png" />
  </head>

  <body>
    <!-- NAVBAR -->
    <nav class="nav-root">
      <div class="nav-inner">
        <div class="nav-logo">
          <a href="index.html">
            <img src="assets/EONIX%20SYSTEMS%20LOGO.png" alt="Eonix Systems logo" />
          </a>
        </div>
        <div class="nav-links">
          <a class="nav-link" href="index.html">Home</a>
          <a class="nav-link" href="ecosystem.html">Ecosystem</a>
          <a class="nav-link" href="product.html">Product</a>
          <a class="nav-link nav-active" href="about.html">About</a>
          <a class="nav-link" href="contact.html">Contact</a>
        </div>
        <button class="nav-toggle" aria-label="Toggle navigation">
          <span></span><span></span><span></span>
        </button>
      </div>
    </nav>

    <main class="page-wrapper" style="overflow: visible;">
      
      <!-- SECTION 1: HERO -->
      <section class="home-root page-section hero-animated-grid" style="padding-top: 180px; min-height: 60vh; padding-bottom: 80px;">
        <div class="home-hero-inner reveal reveal-scale" style="text-align: center;">
          <h1 class="home-title" style="margin-bottom: 32px; font-size: 4.5rem;">
            Engineering Infrastructure<br>for <span class="text-accent glow-text">Real Systems</span>
          </h1>
          <p class="manifesto-lead reveal" style="--delay: 200ms;">
            Eonix Systems is an engineering-first hardware company building intelligent power infrastructure for embedded and robotic systems.
          </p>
          <p class="manifesto-lead reveal" style="--delay: 400ms; margin-top: 16px;">
            We design systems that are predictable, observable, and safe — not just functional.
          </p>
        </div>
      </section>

      <!-- SECTION 2: THE PROBLEM -->
      <section class="manifesto-section page-section reveal">
        <div class="manifesto-container">
            <h2 class="manifesto-title text-center reveal">The Problem Isn’t Complexity.<br><span class="text-red-glow">It’s Fragmentation.</span></h2>
            
            <p class="manifesto-p reveal" style="--delay: 100ms;">Modern embedded systems are not limited by capability — they are limited by how they are built.</p>
            
            <div class="problem-list reveal" style="--delay: 300ms;">
                <p>Power is treated as an afterthought.</p>
                <p>Communication is inconsistent.</p>
                <p>Debugging is blind.</p>
                <p>Failure modes are unpredictable.</p>
            </div>
            
            <p class="manifesto-p emphasize text-red-glow reveal" style="--delay: 500ms; margin-top: 40px;">What should be a system becomes a collection of disconnected parts.</p>
        </div>
      </section>

      <!-- SECTION 3: ORIGIN STORY -->
      <section class="manifesto-section page-section">
        <div class="manifesto-container">
            <h2 class="manifesto-title text-center reveal">Where Eonix Began</h2>
            
            <p class="manifesto-p reveal" style="--delay: 100ms;">Eonix did not start as a business idea.</p>
            <p class="manifesto-p reveal text-red" style="--delay: 200ms; font-weight: 500;">It started as a repeated failure pattern.</p>
            
            <p class="manifesto-p reveal" style="--delay: 300ms; margin-top: 32px;">While building robots and embedded systems, the same issue appeared across projects: power systems were improvised.</p>
            
            <p class="manifesto-p reveal" style="--delay: 400ms;">Regulators, fuses, and wiring stitched together with no telemetry, no visibility, and limited protection.</p>
            
            <p class="manifesto-p reveal" style="--delay: 500ms;">When something failed, there was no answer why.</p>
            
            <p class="manifesto-p reveal" style="--delay: 600ms;">Debugging meant probing rails manually, replacing burnt components, and hoping the next iteration survived.</p>
            
            <div class="reveal mt-64 text-center" style="--delay: 800ms;">
                <p class="manifesto-p" style="margin-bottom: 8px;">This was not a one-off problem.</p>
                <p class="manifesto-p text-accent text-bold glow-text" style="font-size: 1.5rem;">It was systemic.</p>
            </div>
        </div>
      </section>

      <!-- SECTION 4: BREAKPOINT -->
      <section class="manifesto-section page-section bg-gradient-dark pt-80 pb-80">
        <div class="manifesto-container text-center">
            <h2 class="manifesto-title reveal">The Realization</h2>
            
            <p class="manifesto-p reveal" style="--delay: 100ms;">Machines have evolved.</p>
            <p class="manifesto-p reveal text-red-glow" style="--delay: 200ms;">Their electrical backbone has not.</p>
            
            <div class="realization-stack mt-48 reveal" style="--delay: 400ms;">
                <span>Control systems are intelligent.</span>
                <span>Sensors are advanced.</span>
                <span>Software is complex.</span>
            </div>
            
            <p class="manifesto-p text-bold text-accent glow-text mt-48 reveal" style="--delay: 600ms; font-size: 1.6rem;">But power — the foundation — is still primitive.</p>
        </div>
      </section>

      <!-- SECTION 5: THE IDEA -->
      <section class="manifesto-section page-section">
        <div class="manifesto-container wide">
            <h2 class="manifesto-title text-center reveal">Power Infrastructure Should Be Intelligent</h2>
            
            <div class="feature-trio mt-64">
                <div class="f-block premium-lift reveal" style="--delay: 100ms;">
                    <h4>[ Monitor ]</h4>
                    <p>Real-time telemetry for voltage, current, and system health.</p>
                </div>
                <div class="f-block premium-lift reveal" style="--delay: 200ms;">
                    <h4>[ Protect ]</h4>
                    <p>Hardware-level safeguards that act before damage occurs.</p>
                </div>
                <div class="f-block premium-lift reveal" style="--delay: 300ms;">
                    <h4>[ Communicate ]</h4>
                    <p>Active reporting of faults and system state.</p>
                </div>
            </div>
        </div>
      </section>

      <!-- SECTION 6: WHAT EONIX BUILDS -->
      <section class="manifesto-section page-section">
        <div class="manifesto-container text-center">
            <h2 class="manifesto-title reveal" style="font-size: 2.4rem;">The Electrical Backbone for<br>Autonomous Machines</h2>
            
            <p class="manifesto-p reveal mt-32" style="--delay: 100ms;">Eonix builds a modular, system-level power infrastructure for embedded and robotic machines.</p>
            
            <p class="manifesto-p reveal text-accent" style="--delay: 200ms; font-weight: 500;">Each module is designed to operate as part of a larger system — not in isolation.</p>
            
            <div class="check-list mt-64">
                <div class="check-item reveal" style="--delay: 300ms;">
                    <span class="check-icon">✓</span> Electrically safe by design
                </div>
                <div class="check-item reveal" style="--delay: 400ms;">
                    <span class="check-icon">✓</span> Fully instrumented with real-time telemetry
                </div>
                <div class="check-item reveal" style="--delay: 500ms;">
                    <span class="check-icon">✓</span> Configurable through software
                </div>
                <div class="check-item reveal" style="--delay: 600ms;">
                    <span class="check-icon">✓</span> Built for system-level integration
                </div>
            </div>
        </div>
      </section>

      <!-- SECTION 7: ENGINEERING PHILOSOPHY -->
      <section class="manifesto-section page-section bg-gradient-dark pt-80 pb-80">
        <div class="manifesto-container">
            <h2 class="manifesto-title text-center reveal">Built the Hard Way. On Purpose.</h2>
            
            <div class="text-center mt-48">
                <p class="manifesto-p reveal" style="--delay: 100ms;">We do not optimize for convenience.</p>
                <p class="manifesto-p text-accent glow-text text-bold reveal" style="font-size: 1.6rem; --delay: 200ms;">We optimize for correctness.</p>
                
                <p class="manifesto-p mt-32 reveal" style="--delay: 300ms;">Every decision is made with system behavior, safety, and predictability in mind.</p>
            </div>
            
            <div class="check-list-centered mt-64">
                <div class="check-item-card premium-lift reveal" style="--delay: 400ms;">
                    <span class="check-icon">✓</span> Hardware safety over feature count
                </div>
                <div class="check-item-card premium-lift reveal" style="--delay: 500ms;">
                    <span class="check-icon">✓</span> Deterministic behavior over convenience
                </div>
                <div class="check-item-card premium-lift reveal" style="--delay: 600ms;">
                    <span class="check-icon">✓</span> Clear architecture over abstraction
                </div>
                <div class="check-item-card premium-lift reveal" style="--delay: 700ms;">
                    <span class="check-icon">✓</span> Real telemetry over assumptions
                </div>
            </div>
        </div>
      </section>

      <!-- SECTION 8: FINAL STATEMENT -->
      <section class="manifesto-section page-section text-center" style="margin-bottom: 80px;">
        <div class="manifesto-container">
            <h2 class="home-title reveal" style="font-size: 3.5rem;">This Is Not Hobby Hardware</h2>
            
            <p class="manifesto-p reveal mt-48" style="--delay: 100ms;">Eonix is built for engineers designing systems that must work outside the lab.</p>
            
            <div class="realization-stack mt-32 reveal" style="--delay: 200ms; display: flex; justify-content: center; gap: 40px;">
                <span class="text-accent" style="font-size: 1.4rem;">Robotics.</span>
                <span class="text-accent" style="font-size: 1.4rem;">Automation.</span>
                <span class="text-accent" style="font-size: 1.4rem;">Real-world machines.</span>
            </div>
            
            <p class="manifesto-p text-red-glow text-bold mt-64 reveal" style="font-size: 1.6rem; --delay: 400ms;">If failure is not an option, neither is guesswork.</p>
        </div>
      </section>

      <!-- SECTION 9: FINAL CTA -->
      <section class="page-section cta-grand text-center" style="padding: 100px 24px; border-top: 1px solid rgba(255,255,255,0.05);">
        <h2 class="home-title" style="font-size: 3.5rem; margin-bottom: 40px;">Build Systems That Actually Work</h2>
        <div class="hero-actions" style="justify-content: center;">
            <a href="ecosystem.html" class="btn btn-primary btn-glow">
              Explore Ecosystem <span class="arrow">→</span>
            </a>
            <a href="product.html" class="btn btn-secondary">
              View Products
            </a>
        </div>
      </section>

    </main>

    <footer class="footer-root">
      <div class="footer-inner">
        <div class="footer-left">
          <p class="footer-brand">Eonix Systems</p>
          <p class="footer-tagline">Power. Intelligent. Protected.</p>
        </div>
        <div class="footer-right">
          <a class="footer-link" href="ecosystem.html">Ecosystem</a>
          <a class="footer-link" href="product.html">Product</a>
          <a class="footer-link" href="contact.html">Contact</a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 Eonix Systems Pvt. Ltd. All rights reserved.</p>
        <!-- Keep existing socials formatting -->
      </div>
    </footer>

    <!-- Scripts -->
    <script src="js/scroll-reveal.js?v=20"></script>
    <script src="js/nav.js?v=20"></script>
  </body>
</html>
"""

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Updated about.html")
