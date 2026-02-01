/* =========================
   CUSTOM SYSTEM DIAGRAM ANIMATION
   ========================= */

// Global state controller
let currentPowerState = 'AC'; // 'AC' or 'DC'

window.setPowerMode = function (mode) {
    if (mode !== 'AC' && mode !== 'DC') return;
    currentPowerState = mode;

    // Update Toggle UI
    const controls = document.getElementById('power-controls');
    if (controls) {
        controls.classList.remove('mode-ac', 'mode-dc');
        controls.classList.add(mode === 'AC' ? 'mode-ac' : 'mode-dc');
    }
};

document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("systemCanvas");
    if (!canvas) return;

    const overlay = document.querySelector(".diagram-overlay");
    const ctx = canvas.getContext("2d");
    let animationFrameId;
    let hoveredNode = null;

    // Resize
    function resize() {
        const parent = canvas.parentElement;
        canvas.width = parent.clientWidth;
        canvas.height = parent.clientHeight;
    }
    window.addEventListener("resize", resize);
    resize();

    const GRID_SIZE = 40;

    // NODES CONFIGURATION
    const NODES = [
        { id: "AC_IN", x: 0.1, y: 0.4, label: "AC SUPPLY", type: "source", w: 120 },

        // Multiline: "AC to DC" (top), "Converter" (bottom)
        { id: "ACDC", x: 0.3, y: 0.4, label: ["AC to DC", "Converter"], type: "hub", w: 120 },

        { id: "ORING", x: 0.5, y: 0.4, label: "SMART FLOW", type: "hub", w: 100 },

        // Multiline: "SMART POWER" (top), "HUB" (bottom)
        { id: "PDS", x: 0.75, y: 0.4, label: ["SMART POWER", "HUB"], type: "hub", w: 140 },

        { id: "OS", x: 0.75, y: 0.15, label: "User Interface", type: "load", w: 120 },
        { id: "LED", x: 0.93, y: 0.4, label: "LED", type: "visual-led", w: 50 },
        { id: "MOTOR", x: 0.75, y: 0.65, label: "Motor", type: "visual-motor", w: 60 },

        { id: "BMS", x: 0.3, y: 0.65, label: "BMS", type: "hub", w: 80 },
        { id: "BAT", x: 0.3, y: 0.85, label: "Battery", type: "source", w: 80 },
    ];

    const TOOLTIPS = {
        "AC_IN": "Grid Power Source.",
        "ACDC": "High-efficiency Rectification Stage.",
        "ORING": "Intelligent Power Path Arbitration.",
        "PDS": "Central Distribution & Protection Hub.",
        "OS": "Monitoring & Control Dashboard.",
        "LED": "3.3V/5V Logic Load.",
        "MOTOR": "High-Current Inductive Load.",
        "BMS": "Battery Management & Monitoring.",
        "BAT": "Energy Buffer."
    };

    // LINKS DEFINITION
    const LINKS_DEF = [
        // === MAIN AC PATH ===
        // AC Mode: AC -> Converter
        { from: "AC_IN", to: "ACDC", type: "wave", modes: ['AC'] },

        // AC Mode: Converter -> Smart Flow
        { from: "ACDC", to: "ORING", type: "power", modes: ['AC'] },

        // Smart Flow -> Hub (Common path, always drawn but logic implies source)
        { from: "ORING", to: "PDS", type: "power" },

        // === BATTERY PATH ===
        // AC Mode: Charging (Converter -> BMS -> Battery)
        { from: "ACDC", to: "BMS", type: "power", modes: ['AC'] },
        { from: "BMS", to: "BAT", type: "power", dir: 1, modes: ['AC'] }, // INTO Battery

        // DC Mode: Discharging (Battery -> BMS -> Smart Flow)
        { from: "BAT", to: "BMS", type: "power", dir: 1, modes: ['DC'] }, // OUT of Battery
        { from: "BMS", to: "ORING", type: "power", points: [[0.5, 0.65]], dir: 1, modes: ['DC'] },

        // === OUTPUTS ===
        { from: "PDS", to: "LED", type: "power" },
        { from: "PDS", to: "MOTOR", type: "power" },

        // === DATA LINKS ===
        // 1. AC Mode: ACDC -> BMS
        // We use 'modes' array to restrict visibility
        { from: "ACDC", to: "BMS", type: "data", offset: 10, dir: -1, modes: ['AC'] },

        // 2. DC Mode: BMS -> Smart Flow (Skipping ACDC)
        // Parallel Routing: Outer track. 
        // Power Path is (0.3, 0.65) -> (0.5, 0.65) -> (0.5, 0.4)
        // Data Path needs to be slightly offset (wider and lower)
        {
            from: "BMS",
            to: "ORING",
            type: "data",
            // Waypoints: [Start Offset], [Corner], [Vertical Up]
            // EQUIDISTANT FIX: 
            // Power Line corners are (0.5, 0.65).
            // Y-Gap: 0.02 (0.65 -> 0.67) ~21px on 1080p
            // X-Gap: 0.01 (0.50 -> 0.51) ~19px on 1080p (Accounts for aspect ratio)
            points: [[0.3, 0.67], [0.51, 0.67], [0.51, 0.4]],
            dir: 1,
            modes: ['DC']
        },

        // 3. Common Data Backbone (Always active for continuity, or switch based on mode?)
        // Let's keep the main bus active, but maybe logical flow suggests otherwise.
        // User asked "data path should change from bms to smart flow in the dc one instead of going through the ac-dc"
        // Previous was: ACDC -> ORING -> PDS.
        // In DC Mode: BMS -> ORING -> PDS.

        // ACDC -> ORING (Only AC)
        { from: "ACDC", to: "ORING", type: "data", offset: 10, modes: ['AC'] },

        // ORING -> PDS (Always active, carries data from whichever source)
        { from: "ORING", to: "PDS", type: "data", offset: 10 },

        // OS <-> PDS (Always active)
        { from: "OS", to: "PDS", type: "data", offset: -5, dir: 1 },
        { from: "PDS", to: "OS", type: "data", offset: 5, dir: 1 }
    ];

    let time = 0;

    // Interaction
    canvas.addEventListener("mousemove", (e) => {
        const rect = canvas.getBoundingClientRect();
        const mx = e.clientX - rect.left;
        const my = e.clientY - rect.top;

        let found = null;
        NODES.forEach(node => {
            const pos = getNodePos(node);
            const w = node.w;
            const h = 40;
            if (Math.abs(mx - pos.x) < w / 2 + 10 && Math.abs(my - pos.y) < h / 2 + 10) {
                found = node;
            }
        });

        if (found !== hoveredNode) {
            hoveredNode = found;
            updateTooltip();
        }
        canvas.style.cursor = hoveredNode ? "pointer" : "default";
    });

    function updateTooltip() {
        overlay.innerHTML = "";
        if (!hoveredNode) return;
        const text = TOOLTIPS[hoveredNode.id] || (Array.isArray(hoveredNode.label) ? hoveredNode.label.join(" ") : hoveredNode.label);

        const tip = document.createElement("div");
        tip.className = "diagram-tooltip glass-panel";
        tip.textContent = text;
        const pos = getNodePos(hoveredNode);
        Object.assign(tip.style, {
            position: "absolute",
            padding: "8px 12px",
            borderRadius: "4px",
            fontSize: "0.85rem",
            color: "#fff",
            pointerEvents: "none",
            zIndex: "100",
            whiteSpace: "nowrap"
        });

        if (pos.x > canvas.width * 0.7) {
            tip.style.right = (canvas.width - pos.x + hoveredNode.w / 2 + 15) + "px";
            tip.style.top = (pos.y - 20) + "px";
        } else {
            tip.style.left = (pos.x + hoveredNode.w / 2 + 15) + "px";
            tip.style.top = (pos.y - 20) + "px";
        }
        overlay.appendChild(tip);
    }

    function getNodePos(node) {
        return {
            x: node.x * canvas.width,
            y: node.y * canvas.height
        };
    }

    function drawLine(start, end, link, offset = 0) {
        ctx.beginPath();

        if (link.modes && !link.modes.includes(currentPowerState)) {
            return;
        }

        // WAVE
        if (link.type === 'wave') {
            ctx.strokeStyle = "rgba(255, 255, 255, 0.8)";
            ctx.lineWidth = 2;
            const dist = Math.hypot(end.x - start.x, end.y - start.y);
            const angle = Math.atan2(end.y - start.y, end.x - start.x);
            for (let i = 0; i <= dist; i += 2) {
                const x = i;
                const y = Math.sin(i * 0.1 - time * 0.005) * 5;
                const rx = start.x + x * Math.cos(angle) - y * Math.sin(angle);
                const ry = start.y + x * Math.sin(angle) + y * Math.cos(angle);
                if (i === 0) ctx.moveTo(rx, ry);
                else ctx.lineTo(rx, ry);
            }
            ctx.stroke();
            return;
        }

        let sx = start.x; let sy = start.y;
        let ex = end.x; let ey = end.y;

        if (offset !== 0) {
            if (Math.abs(ex - sx) > Math.abs(ey - sy)) { sy += offset; ey += offset; }
            else { sx += offset; ex += offset; }
        }

        ctx.moveTo(sx, sy);
        if (link.points) {
            link.points.forEach(pt => {
                let px = pt[0] * canvas.width;
                let py = pt[1] * canvas.height;
                if (offset !== 0 && Math.abs(ex - sx) > Math.abs(ey - sy)) py += offset;
                ctx.lineTo(px, py);
            });
        }
        ctx.lineTo(ex, ey);

        if (link.type === "power") {
            ctx.strokeStyle = "rgba(255, 255, 255, 0.75)";
            ctx.lineWidth = 3;
            ctx.setLineDash([12, 12]);
            const direction = link.dir || 1;
            ctx.lineDashOffset = -time * 0.01 * direction;
        } else {
            ctx.strokeStyle = "rgba(255, 59, 59, 0.9)";
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            const speed = 0.025;
            ctx.lineDashOffset = -time * speed * (link.dir || 1);
        }

        ctx.stroke();
        ctx.setLineDash([]);
    }

    function drawMotor(ctx, x, y, w) {
        ctx.beginPath(); ctx.arc(x, y, w / 2, 0, Math.PI * 2);
        ctx.fillStyle = "#111"; ctx.strokeStyle = "#888"; ctx.lineWidth = 2;
        ctx.fill(); ctx.stroke();
        const angle = time * 0.005;
        ctx.save(); ctx.translate(x, y); ctx.rotate(angle);
        ctx.fillStyle = "#ccc"; ctx.beginPath();
        for (let i = 0; i < 3; i++) {
            ctx.rotate((Math.PI * 2) / 3); ctx.rect(-4, -w / 3, 8, w / 2.2);
        }
        ctx.fill(); ctx.restore();
        ctx.beginPath(); ctx.arc(x, y, 6, 0, Math.PI * 2); ctx.fillStyle = "#fff"; ctx.fill();
        ctx.fillStyle = "#fff"; ctx.font = "12px Inter"; ctx.fillText("Motor", x, y + w / 2 + 15);
    }

    function drawLED(ctx, x, y, w) {
        const pulse = (Math.sin(time * 0.003) + 1) / 2;
        const glowOpacity = 0.2 + pulse * 2.0;
        ctx.shadowBlur = 15; ctx.shadowColor = `rgba(255, 255, 255, ${glowOpacity})`;
        ctx.beginPath(); ctx.arc(x, y, w / 3.5, 0, Math.PI * 2); ctx.fillStyle = "#ffffff"; ctx.fill();
        ctx.shadowBlur = 0;
        ctx.beginPath(); ctx.arc(x, y, w / 2.8, 0, Math.PI * 2); ctx.strokeStyle = "#444"; ctx.lineWidth = 1.5; ctx.stroke();
        ctx.fillStyle = "#fff"; ctx.font = "12px Inter"; ctx.fillText("LED", x, y + w / 2 + 15);
    }

    // State Animation Values (0.0 to 1.0)
    let acAnim = 1.0;
    let dcAnim = 0.0;

    // Modified draw function to handle lerping
    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Update Animation State
        // TWEAK HERE: Lower this value to make animation slower, increase to make faster.
        const SPEED = 0.015;
        if (currentPowerState === 'AC') {
            acAnim = Math.min(acAnim + SPEED, 1.0);
            dcAnim = Math.max(dcAnim - SPEED, 0.0);
        } else {
            acAnim = Math.max(acAnim - SPEED, 0.0);
            dcAnim = Math.min(dcAnim + SPEED, 1.0);
        }

        // Draw Grid
        ctx.strokeStyle = "rgba(255, 255, 255, 0.03)"; ctx.lineWidth = 1;
        for (let x = 0; x <= canvas.width; x += GRID_SIZE) {
            ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, canvas.height); ctx.stroke();
        }
        for (let y = 0; y <= canvas.height; y += GRID_SIZE) {
            ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(canvas.width, y); ctx.stroke();
        }

        LINKS_DEF.forEach(link => {
            const n1 = NODES.find(n => n.id === link.from);
            const n2 = NODES.find(n => n.id === link.to);
            if (!n1 || !n2) return;

            // Determine Progress based on mode
            let progress = 1.0;
            if (link.modes) {
                if (link.modes.includes('AC') && !link.modes.includes('DC')) progress = acAnim;
                else if (link.modes.includes('DC') && !link.modes.includes('AC')) progress = dcAnim;
            }

            if (progress > 0.01) {
                drawLine(getNodePos(n1), getNodePos(n2), link, link.offset, progress);
            }
        });

        NODES.forEach(node => {
            const pos = getNodePos(node);
            if (node.type === "visual-motor") { drawMotor(ctx, pos.x, pos.y, node.w); return; }
            if (node.type === "visual-led") { drawLED(ctx, pos.x, pos.y, node.w); return; }

            const w = node.w || 100;
            const h = 42;
            const isHover = (hoveredNode === node);
            ctx.fillStyle = "#0a0c0e";
            ctx.strokeStyle = isHover ? "#00a4ff" : "rgba(255, 255, 255, 0.2)";
            ctx.lineWidth = isHover ? 2 : 1;
            if (isHover) { ctx.shadowColor = "#00a4ff"; ctx.shadowBlur = 10; }
            else { ctx.shadowBlur = 0; }
            const r = 6;
            ctx.beginPath(); ctx.roundRect(pos.x - w / 2, pos.y - h / 2, w, h, r);
            ctx.fill(); ctx.stroke();

            ctx.fillStyle = "#fff";
            ctx.font = "12px Inter";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            ctx.shadowBlur = 0;

            if (Array.isArray(node.label)) {
                ctx.fillText(node.label[0], pos.x, pos.y - 7);
                ctx.fillText(node.label[1], pos.x, pos.y + 7);
            } else {
                ctx.fillText(node.label, pos.x, pos.y);
            }
        });

        time += 16;
        animationFrameId = requestAnimationFrame(draw);
    }
    draw();

    // Helper: Distance between two points
    function dist(p1, p2) { return Math.hypot(p2.x - p1.x, p2.y - p1.y); }

    function drawLine(start, end, link, offset = 0, progress = 1.0) {
        ctx.beginPath();

        // WAVE TYPE (AC Input)
        if (link.type === 'wave') {
            ctx.strokeStyle = "rgba(255, 255, 255, 0.8)";
            ctx.lineWidth = 2;
            ctx.setLineDash([]);

            const d = dist(start, end);
            const visibleDist = d * progress;
            const angle = Math.atan2(end.y - start.y, end.x - start.x);

            for (let i = 0; i <= visibleDist; i += 2) {
                const x = i;
                const y = Math.sin(i * 0.1 - time * 0.005) * 5;
                const rx = start.x + x * Math.cos(angle) - y * Math.sin(angle);
                const ry = start.y + x * Math.sin(angle) + y * Math.cos(angle);
                if (i === 0) ctx.moveTo(rx, ry);
                else ctx.lineTo(rx, ry);
            }
            ctx.stroke();
            return;
        }

        // STANDARD & POLYLINE TYPES
        let sx = start.x; let sy = start.y;
        let ex = end.x; let ey = end.y;

        // Apply Offset
        if (offset !== 0) {
            if (Math.abs(ex - sx) > Math.abs(ey - sy)) { sy += offset; ey += offset; }
            else { sx += offset; ex += offset; }
        }

        // Construct full path segments
        let points = [{ x: sx, y: sy }];
        if (link.points) {
            link.points.forEach(pt => {
                let px = pt[0] * canvas.width;
                let py = pt[1] * canvas.height;
                if (offset !== 0 && Math.abs(ex - sx) > Math.abs(ey - sy)) py += offset;
                points.push({ x: px, y: py });
            });
        }
        points.push({ x: ex, y: ey });

        // Calculate Total Length
        let totalLen = 0;
        for (let i = 0; i < points.length - 1; i++) totalLen += dist(points[i], points[i + 1]);

        // Draw Visible Portion
        let drawLen = totalLen * progress;
        let currentLen = 0;

        ctx.moveTo(points[0].x, points[0].y);

        for (let i = 0; i < points.length - 1; i++) {
            const p1 = points[i];
            const p2 = points[i + 1];
            const d = dist(p1, p2);

            if (currentLen + d < drawLen) {
                // Draw full segment
                ctx.lineTo(p2.x, p2.y);
                currentLen += d;
            } else {
                // Draw partial segment and STOP
                const remaining = drawLen - currentLen;
                const ratio = remaining / d;
                const tx = p1.x + (p2.x - p1.x) * ratio;
                const ty = p1.y + (p2.y - p1.y) * ratio;
                ctx.lineTo(tx, ty);
                break; // Stop drawing
            }
        }

        // Styling
        if (link.type === "power") {
            ctx.strokeStyle = "rgba(255, 255, 255, 0.75)";
            ctx.lineWidth = 3;
            ctx.setLineDash([12, 12]);
            const direction = link.dir || 1;
            ctx.lineDashOffset = -time * 0.01 * direction;
        } else {
            ctx.strokeStyle = `rgba(255, 59, 59, 0.9)`;
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            const speed = 0.025;
            ctx.lineDashOffset = -time * speed * (link.dir || 1);
        }

        ctx.stroke();
        ctx.setLineDash([]);
    }
});
