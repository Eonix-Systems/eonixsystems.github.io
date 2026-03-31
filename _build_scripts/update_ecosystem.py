import re

html_file = r'd:/eonix_systems/Development/eonix_systems_website/ecosystem.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_main = """<main class="page-wrapper">

        <!-- HERO SECTION -->
        <section class="home-root page-section hero-animated-grid" style="padding-top: 140px; min-height: 50vh; padding-bottom: 0px;">
            <div class="home-hero-inner reveal reveal-scale">
                <h1 class="home-title" style="margin-bottom: 24px;">
                    <span class="text-accent glow-text">System Architecture</span>,<br />
                    Not Modules.
                </h1>
                <p class="home-subtitle" style="max-width: 900px; margin-bottom: 40px;">
                    Eonix is built as a layered embedded <span class="text-accent" style="text-shadow: 0 0 8px var(--accent-glow);">system</span> — where power, communication, sensing, and actuation are engineered to operate together with predictable behavior.
                </p>
            </div>
        </section>

        <!-- SYSTEM DIAGRAM SECTION -->
        <section class="page-section" style="padding-top: 0; margin-bottom: 120px;">
            <div class="reveal reveal-scale">
                <h2 class="home-section-title" style="margin-bottom: 16px;">System Overview</h2>
                <p class="home-section-text" style="max-width: 700px; margin-bottom: 48px;">
                    A centralized architecture with unified communication and controlled power distribution.
                </p>
                <!-- DIAGRAM CONTAINER -->
                <div class="hero-diagram-container glow-hover glass-panel reveal" id="hero-diagram" style="backdrop-filter: blur(10px);">
                    <canvas id="systemCanvas"></canvas>
                    <div class="diagram-overlay"></div>
                </div>
            </div>
        </section>

        <!-- ARCHITECTURE BREAKDOWN (VERTICAL STACK) -->
        <section class="architecture-stack page-section">
            <h2 class="home-section-title reveal">Layered System Architecture</h2>
            
            <!-- CONTROL LAYER -->
            <div class="arch-layer-block">
                <div class="arch-layer-content reveal reveal-left">
                    <div class="arch-label text-accent">CONTROL LAYER</div>
                    <h3 class="arch-layer-title">System Brain</h3>
                    <p class="arch-layer-desc">
                        The Eonix Motherboard acts as the central controller, coordinating all modules, managing communication, and maintaining system state.
                    </p>
                    <ul class="arch-key-points">
                        <li>Centralized control architecture</li>
                        <li>No distributed logic chaos</li>
                        <li>USB interface to desktop system</li>
                        <li>Optional external MCU integration</li>
                    </ul>
                </div>
            </div>

            <!-- COMMUNICATION LAYER -->
            <div class="arch-layer-block arch-layer-alt">
                <div class="arch-layer-content reveal reveal-right" style="margin-left:auto;">
                    <div class="arch-label text-accent">COMMUNICATION LAYER</div>
                    <h3 class="arch-layer-title">Unified Interface — Deterministic Communication</h3>
                    <p class="arch-layer-desc">
                        All modules communicate through a structured, deterministic interface.<br> No address conflicts, no protocol collisions, no unpredictable timing.
                    </p>
                    <ul class="arch-key-points">
                        <li>Multi-node communication</li>
                        <li>Predictable system behavior</li>
                        <li>Scalable architecture</li>
                        <li>No I2C/SPI complexity at system level</li>
                    </ul>
                </div>
            </div>

            <!-- POWER LAYER -->
            <div class="arch-layer-block">
                <div class="arch-layer-content reveal reveal-left">
                    <div class="arch-label text-accent">POWER LAYER</div>
                    <h3 class="arch-layer-title">Programmable Power — Controlled Energy Flow</h3>
                    <p class="arch-layer-desc">
                        Power is treated as a controlled system, not just supply. Each rail is regulated, monitored, and protected in hardware.
                    </p>
                    <ul class="arch-key-points">
                        <li>CC/CV programmable outputs</li>
                        <li>Hardware OCP / SCP</li>
                        <li>Real-time telemetry</li>
                        <li>Stable under dynamic loads</li>
                    </ul>
                </div>
            </div>

            <!-- EXECUTION LAYER -->
            <div class="arch-layer-block arch-layer-alt">
                <div class="arch-layer-content reveal reveal-right" style="margin-left:auto;">
                    <div class="arch-label text-accent">EXECUTION LAYER</div>
                    <h3 class="arch-layer-title">Execution Layer — Sensing and Actuation</h3>
                    <p class="arch-layer-desc">
                        Sensors provide structured system input, while drivers convert electrical power into controlled physical output.
                    </p>
                    <ul class="arch-key-points">
                        <li>Sensor abstraction (no raw protocols)</li>
                        <li>High-current driver modules</li>
                        <li>Control-ready architecture</li>
                        <li>Designed for real-world loads</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- DATA FLOW SECTION -->
        <section class="page-section data-flow-section reveal">
            <h2 class="home-section-title">How the System Operates</h2>
            
            <div class="data-flow-container glass-panel reveal reveal-scale">
                <div class="flow-pipeline-wrapper">
                    <div class="flow-pipeline">
                        <div class="flow-node hover-premium"><strong>Sensors</strong><br/><span class="flow-detail">Generate structured data</span></div>
                        <div class="flow-arrow flow-animate-arrow">&#8594;</div>
                        <div class="flow-node flow-node-primary hover-premium"><strong>Motherboard</strong><br/><span class="flow-detail">Processes & routes commands</span></div>
                        <div class="flow-arrow flow-animate-arrow">&#8594;</div>
                        <div class="flow-node hover-premium"><strong>Drivers</strong><br/><span class="flow-detail">Execute control signals</span></div>
                        <div class="flow-arrow flow-animate-arrow">&#8594;</div>
                        <div class="flow-node hover-premium"><strong>Actuators</strong><br/><span class="flow-detail">Physical output</span></div>
                    </div>
                    
                    <div class="flow-power-injector">
                        <div class="power-arrow">&#8593;</div>
                        <div class="flow-node flow-node-power hover-premium"><strong>Power System</strong><br/><span class="flow-detail">Supplies stable energy across all stages</span></div>
                    </div>
                </div>
            </div>
        </section>

        <!-- WHY THIS ARCHITECTURE -->
        <section class="page-section why-arch-section">
            <h2 class="home-section-title reveal">Why This Architecture Exists</h2>
            
            <div class="why-grid">
                <div class="why-card glass-panel hover-premium reveal reveal-left">
                    <h4 class="text-accent">Problem</h4>
                    <p>Module-based systems break at integration. Power is unstable. Communication is unpredictable.</p>
                </div>
                
                <div class="why-card glass-panel hover-premium reveal reveal-scale" style="--delay: 150ms;">
                    <h4 class="text-accent">Solution</h4>
                    <p>Eonix enforces structure at every level:<br><br>Controlled power.<br>Deterministic communication.<br>Centralized coordination.</p>
                </div>
                
                <div class="why-card glass-panel hover-premium reveal reveal-right" style="--delay: 300ms; border: 1px solid var(--accent-primary); box-shadow: 0 0 20px var(--accent-dim);">
                    <h4 class="text-accent" style="font-size: 1.5rem; text-shadow: 0 0 10px var(--accent-glow);">Result</h4>
                    <p style="font-size: 1.25rem; color: #fff; font-weight: 500;">Systems that scale without breaking.</p>
                </div>
            </div>
        </section>

        <!-- DESIGN PRINCIPLES -->
        <section class="home-difference page-section reveal">
            <h2 class="home-section-title">Core Design Principles</h2>

            <div class="deployment-grid principle-grid">
                <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 100ms;">
                    <h3>Hardware-Enforced Safety</h3>
                    <p>Protection is implemented in hardware, not dependent on software.</p>
                </div>
                <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 200ms;">
                    <h3>Deterministic Behavior</h3>
                    <p>System response remains predictable under all operating conditions.</p>
                </div>
                <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 300ms;">
                    <h3>Modular but Structured</h3>
                    <p>Modules exist within a defined architecture, not as independent units.</p>
                </div>
                <div class="home-diff-item glass-panel hover-premium reveal" style="--delay: 400ms;">
                    <h3>System-Level Thinking</h3>
                    <p>Designed as a complete system, not assembled piece-by-piece.</p>
                </div>
            </div>
        </section>

        <!-- CLOSING CTA -->
        <section class="home-direction page-section hero-animated-grid reveal reveal-scale">
            <h2 class="home-section-title" style="margin-bottom: 2rem;">
                Explore the System in Detail
            </h2>

            <div class="hero-actions">
                <a class="btn-primary" href="product.html">
                    View Products
                    <span class="btn-arrow">→</span>
                </a>
                <a class="btn-secondary" href="ecosystem.html">
                    Read Technical Architecture
                    <span class="btn-arrow">→</span>
                </a>
            </div>
        </section>

    </main>"""

# Add stylesheet link
if 'css/ecosystem.css' not in content:
    content = content.replace('</head>', '    <link rel="stylesheet" href="css/ecosystem.css?v=9">\n</head>')

# Replace main
new_content = re.sub(r'<main class="page-wrapper">.*?</main>', new_main, content, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated ecosystem.html successfully")
