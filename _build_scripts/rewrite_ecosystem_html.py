import re

html_file = r'd:/eonix_systems/Development/eonix_systems_website/ecosystem.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_main = """<main class="page-wrapper" style="overflow: visible;">

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

        <!-- INTERACTIVE ARCHITECTURE SECTION (SPLIT SCREEN) -->
        <section class="page-section architecture-interactive">
            <!-- Subtle ambient spotlight for depth -->
            <div class="interactive-ambient-glow" id="ambientGlow"></div>
            
            <div class="interactive-split">
                
                <!-- LEFT CONTENT: Scrolling Steps -->
                <div class="interactive-steps" id="scroll-steps-container">
                    
                    <div class="arch-scroll-step" data-step="1">
                        <div class="arch-label text-accent">CONTROL LAYER</div>
                        <h3 class="arch-layer-title">System Brain</h3>
                        <p class="arch-layer-desc">
                            The motherboard acts as the central controller, coordinating all modules and maintaining system state.
                        </p>
                        <ul class="arch-key-points">
                            <li data-target="MB">Centralized control architecture</li>
                            <li data-target="MB">No distributed logic chaos</li>
                            <li data-target="APP">USB interface to desktop</li>
                            <li data-target="MCU">Optional external MCU integration</li>
                        </ul>
                    </div>
                    
                    <div class="arch-scroll-step" data-step="2">
                        <div class="arch-label text-accent">COMMUNICATION LAYER</div>
                        <h3 class="arch-layer-title">Unified Interface — Deterministic Communication</h3>
                        <p class="arch-layer-desc">
                            All modules communicate through a structured interface — no conflicts, no collisions, no unpredictability.
                        </p>
                        <ul class="arch-key-points">
                            <li data-target="CAN">Multi-node communication</li>
                            <li data-target="CAN">Predictable system behavior</li>
                            <li data-target="CAN">Scalable architecture</li>
                            <li data-target="CAN">No I2C/SPI chaos</li>
                        </ul>
                    </div>
                    
                    <div class="arch-scroll-step" data-step="3">
                        <div class="arch-label text-accent">POWER LAYER</div>
                        <h3 class="arch-layer-title">Programmable Power — Controlled Energy Flow</h3>
                        <p class="arch-layer-desc">
                            Power is regulated, monitored, and protected in hardware — ensuring stable operation under real loads.
                        </p>
                        <ul class="arch-key-points">
                            <li data-target="PWR">CC/CV programmable outputs</li>
                            <li data-target="PWR">Hardware OCP / SCP</li>
                            <li data-target="PWR">Real-time telemetry</li>
                            <li data-target="DRV">Stable under dynamic loads</li>
                        </ul>
                    </div>
                    
                    <div class="arch-scroll-step" data-step="4">
                        <div class="arch-label text-accent">EXECUTION LAYER</div>
                        <h3 class="arch-layer-title">Sensing and Actuation</h3>
                        <p class="arch-layer-desc">
                            Sensors provide structured input, while drivers convert electrical power into controlled physical output.
                        </p>
                        <ul class="arch-key-points">
                            <li data-target="TEMP">Sensor abstraction (no raw protocols)</li>
                            <li data-target="DRV">High-current driver modules</li>
                            <li data-target="MB">Control-ready architecture</li>
                            <li data-target="MOT">Built for real-world loads</li>
                        </ul>
                    </div>

                </div>

                <!-- RIGHT CONTENT: Sticky Diagram -->
                <div class="interactive-diagram">
                    <div class="sticky-wrapper" id="sticky-diagram">
                        <!-- Progress Bar (Vertical) -->
                        <div class="sticky-progress-rail">
                            <div class="sticky-progress-fill" id="diagramProgressFill"></div>
                        </div>
                        
                        <div class="hero-diagram-container glass-panel" style="width: 100%; border: 1px solid rgba(0, 229, 255, 0.2); transform: scale(0.95); transform-origin: top center;">
                            <canvas id="systemCanvas"></canvas>
                            <div class="diagram-overlay"></div>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- DATA FLOW SECTION -->
        <section class="page-section data-flow-section reveal" style="margin-top: -10vh;">
            <h2 class="home-section-title">How the System Operates</h2>
            
            <div class="data-flow-container glass-panel reveal reveal-scale">
                <div class="flow-pipeline-wrapper">
                    <div class="flow-pipeline">
                        <div class="flow-node hover-premium"><strong>Sensors</strong><br /><span
                                class="flow-detail">Generate structured data</span></div>
                        <div class="flow-arrow flow-animate-arrow">&#8594;</div>
                        <div class="flow-node flow-node-primary hover-premium"><strong>Motherboard</strong><br /><span
                                class="flow-detail">Processes & routes commands</span></div>
                        <div class="flow-arrow flow-animate-arrow">&#8594;</div>
                        <div class="flow-node hover-premium"><strong>Drivers</strong><br /><span
                                class="flow-detail">Execute control signals</span></div>
                        <div class="flow-arrow flow-animate-arrow">&#8594;</div>
                        <div class="flow-node hover-premium"><strong>Actuators</strong><br /><span
                                class="flow-detail">Physical output</span></div>
                    </div>

                    <div class="flow-power-injector">
                        <div class="power-arrow">&#8593;</div>
                        <div class="flow-node flow-node-power hover-premium"><strong>Power System</strong><br /><span
                                class="flow-detail">Supplies stable energy across all stages</span></div>
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
                    <p>Eonix enforces structure at every level:<br><br>Controlled power.<br>Deterministic
                        communication.<br>Centralized coordination.</p>
                </div>

                <div class="why-card glass-panel hover-premium reveal reveal-right"
                    style="--delay: 300ms; border: 1px solid var(--accent-primary); box-shadow: 0 0 20px var(--accent-dim);">
                    <h4 class="text-accent" style="font-size: 1.5rem; text-shadow: 0 0 10px var(--accent-glow);">Result
                    </h4>
                    <p style="font-size: 1.25rem; color: #fff; font-weight: 500;">Systems that scale without breaking.
                    </p>
                </div>
            </div>
        </section>

        <!-- FINAL CTA SECTION -->
        <section class="home-direction page-section hero-animated-grid reveal reveal-scale">
            <h2 class="home-section-title" style="margin-bottom: 1rem;">
                A System That Scales Without Breaking
            </h2>
            <p class="home-section-text" style="max-width: 700px; margin-bottom: 2rem; color: var(--text-secondary);">
                Eonix enforces structure across power, communication, and control — enabling systems that remain stable as complexity increases.
            </p>

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

# Replace main
new_content = re.sub(r'<main class="page-wrapper(?:[^>]*)">.*?</main>', new_main, content, flags=re.DOTALL)

# Add inline scroll trigger JS specifically for the new feature before closing body tag
# The scroll logic calculates intersection
scroll_script = """
    <!-- Scroll Step Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const steps = document.querySelectorAll('.arch-scroll-step');
            window.activeDiagramStep = 0; // Global for diagram.js override
            
            // Interaction logic for intersection
            const obsv = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        // Re-activate
                        steps.forEach(s => s.classList.remove('active'));
                        entry.target.classList.add('active');
                        
                        // Set global target for diagram animation lerp loop
                        window.activeDiagramStep = parseInt(entry.target.getAttribute('data-step') || 0);
                        
                        // Shift ambient background
                        const amb = document.getElementById('ambientGlow');
                        if (amb) amb.style.top = (window.activeDiagramStep * 20) + "%";
                    }
                });
            }, {
                root: null,
                rootMargin: '-40% 0px -40% 0px', // Trigger exactly as it hits screen center
                threshold: 0
            });
            
            steps.forEach(step => obsv.observe(step));
            
            // Progress rail logic
            const container = document.getElementById('scroll-steps-container');
            const fill = document.getElementById('diagramProgressFill');
            if (container && fill) {
                window.addEventListener('scroll', () => {
                    const rect = container.getBoundingClientRect();
                    const winH = window.innerHeight;
                    const scrolledThrough = (winH/2 - rect.top) / rect.height;
                    const p = Math.max(0, Math.min(1, scrolledThrough));
                    fill.style.height = (p * 100) + "%";
                });
            }
            
            // Bullet Hover Triggers override
            const bullets = document.querySelectorAll('.arch-key-points li');
            bullets.forEach(b => {
                b.addEventListener('mouseenter', () => window.forceHoverNodeId = b.getAttribute('data-target') || null);
                b.addEventListener('mouseleave', () => window.forceHoverNodeId = null);
            });
        });
    </script>
</body>"""

new_content = re.sub(r'</body>', scroll_script, new_content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated ecosystem.html with advanced scrolling logic.")
