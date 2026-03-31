import re

js_file = r'd:/eonix_systems/Development/eonix_systems_website/js/diagram.js'
with open(js_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_js = """/* =========================
   EONIX ECOSYSTEM ARCHITECTURE DIAGRAM
   Strict Hierarchical CAN Bus
   ========================= */

document.addEventListener("DOMContentLoaded", () => {
    const canvas = document.getElementById("systemCanvas");
    if (!canvas) return;
    const overlay = document.querySelector(".diagram-overlay");
    const ctx = canvas.getContext("2d");
    let hoveredNode = null;
    let time = 0;
    
    // Startup Animation State
    let loadProgress = 0; // Goes 0 -> 1 over 1.5 seconds

    // ── Sizing ────────────────────────────────────────────────
    function resize() {
        const parent = canvas.parentElement;
        const dpr = window.devicePixelRatio || 1;
        const displayWidth = Math.max(parent.clientWidth, 1000);
        const displayHeight = 700;
        canvas.style.width = displayWidth + "px";
        canvas.style.height = displayHeight + "px";
        canvas.width = displayWidth * dpr;
        canvas.height = displayHeight * dpr;
        ctx.setTransform(1, 0, 0, 1, 0, 0);
    }
    window.addEventListener("resize", resize);
    resize();

    const REF_W = 1200;
    const REF_H = 700;
    function S() { return canvas.width / REF_W; }
    function cx(x) { return x * canvas.width; }
    function cy(y) { return y * canvas.height; }

    // ── Layout Constants ──────────────────────────────────────
    const Y_TOP = 0.10;
    const Y_MB = 0.30;
    const Y_CAN = 0.50;
    const Y_MODS = 0.72;
    const Y_PWR = 0.72;
    const Y_BAT = 0.90;

    const X_TEMP = 0.10;
    const X_IMU = 0.22;
    const X_DIST = 0.34;
    const X_DRV = 0.74;
    const X_MOT = 0.90;
    const X_MB = 0.50;
    const X_MCU = 0.80;
    const X_PWR = 0.50;

    const NODES = [
        { id: "APP", x: X_MB, y: Y_TOP, label: ["Eonix Desktop App", "(User Interface)"], type: "visual-desktop", w: 105 },
        { id: "MCU", x: X_MCU, y: Y_TOP, label: ["User MCU", "(Arduino / Custom)"], type: "box", w: 130, h: 44 },
        { id: "MB", x: X_MB, y: Y_MB, label: ["EONIX", "MOTHERBOARD"], type: "box-major", w: 170, h: 50 },
        { id: "CAN", x: X_MB, y: Y_CAN, label: "", type: "can-hit", w: 850, h: 28 },
        { id: "TEMP", x: X_TEMP, y: Y_MODS, label: ["Temperature", "Sensor"], type: "box", w: 120, h: 44 },
        { id: "IMU", x: X_IMU, y: Y_MODS, label: ["IMU", "Sensor"], type: "box", w: 100, h: 44 },
        { id: "DIST", x: X_DIST, y: Y_MODS, label: ["Distance", "LiDAR"], type: "box", w: 100, h: 44 },
        { id: "DRV", x: X_DRV, y: Y_MODS, label: ["Motor Driver", "Module"], type: "box", w: 120, h: 44 },
        { id: "PWR", x: X_PWR, y: Y_PWR, label: ["EONIX POWER BLOCK", "Programmable CC/CV"], type: "box", w: 170, h: 44 },
        { id: "BAT", x: X_PWR, y: Y_BAT, label: "Battery", type: "box", w: 100, h: 40 },
        { id: "MOT", x: X_MOT, y: Y_MODS, label: "Motor", type: "visual-motor", w: 52 },
    ];

    const TIPS = {
        MB: "Central controller managing all modules and system communication.",
        PWR: "Programmable CC/CV power with hardware-level protection and telemetry.",
        TEMP: "Abstracted sensing modules with standardized output.",
        IMU: "Abstracted sensing modules with standardized output.",
        DIST: "Abstracted sensing modules with standardized output.",
        DRV: "High-current driver with fault protection and control capability.",
        CAN: "Deterministic communication backbone with no address conflicts.",
        APP: "User Interface / System Setup.",
        MCU: "External MCU integration via SPI.",
        BAT: "System Power Source.",
        MOT: "High-current physical load.",
    };

    // ── Interaction ───────────────────────────────────────────
    canvas.addEventListener("mousemove", e => {
        const rect = canvas.getBoundingClientRect();
        const dpr = window.devicePixelRatio || 1;
        const mx = (e.clientX - rect.left) * dpr;
        const my = (e.clientY - rect.top) * dpr;
        const s = S();
        let found = null;
        for (const nd of NODES) {
            if (nd.type === "visual-motor" || nd.type === "can-hit") {
                if (nd.type === "can-hit") {
                    const bx = cx(nd.x) - (nd.w * s) / 2;
                    const bw = nd.w * s;
                    const by = cy(nd.y) - (nd.h * s) / 2;
                    const bh = nd.h * s;
                    if (mx >= bx && mx <= bx + bw && my >= by && my <= by + bh) { found = nd; break; }
                }
                if (nd.type === "visual-motor") {
                    const r = (nd.w / 2) * s;
                    if (Math.hypot(mx - cx(nd.x), my - cy(nd.y)) < r + 5) { found = nd; break; }
                }
                continue;
            }
            const nw = (nd.w || 120) * s;
            const nh = (nd.h || 44) * s;
            if (Math.abs(mx - cx(nd.x)) < nw / 2 + 4 && Math.abs(my - cy(nd.y)) < nh / 2 + 4) {
                found = nd; break;
            }
        }
        if (found !== hoveredNode) { hoveredNode = found; renderTooltip(); }
        canvas.style.cursor = (found && TIPS[found.id]) ? "pointer" : "default";
    });
    canvas.addEventListener("mouseleave", () => { hoveredNode = null; renderTooltip(); });

    function renderTooltip() {
        overlay.innerHTML = "";
        if (!hoveredNode || !TIPS[hoveredNode.id]) return;
        const tip = document.createElement("div");
        tip.className = "diagram-tooltip";
        tip.innerHTML = TIPS[hoveredNode.id].replace(/\\n/g, "<br>");
        const dpr = window.devicePixelRatio || 1;
        const s = S();
        const px = cx(hoveredNode.x) / dpr;
        const py = cy(hoveredNode.y) / dpr;
        const nw = ((hoveredNode.w || 120) * s) / dpr;
        const cw = canvas.width / dpr;
        Object.assign(tip.style, {
            position: "absolute", padding: "12px 16px", borderRadius: "8px",
            fontSize: "0.9rem", lineHeight: "1.6", whiteSpace: "nowrap",
            backgroundColor: "#080a0c", border: "1px solid rgba(0,229,255,.4)",
            color: "#00e5ff", pointerEvents: "none", zIndex: "200",
            boxShadow: "0 4px 20px rgba(0,229,255,.15)"
        });
        if (px > cw * 0.55) { tip.style.right = (cw - px + nw / 2 + 10) + "px"; } 
        else { tip.style.left = (px + nw / 2 + 10) + "px"; }
        tip.style.top = (py - 24) + "px";
        overlay.appendChild(tip);
    }

    // ── Global Alpha Helpers ─────────────────────────────────
    function getAlpha(nodeIdList, isLine = false) {
        if (!hoveredNode) return 1.0;
        // If it's a line tied to the hovered node, keep it bright
        if (nodeIdList.includes(hoveredNode.id)) return 1.0;
        return 0.2; // Dim everything else heavily
    }

    // ── Drawing helpers ───────────────────────────────────────
    function drawBox(x, y, w, h, ndId, isMajor) {
        const s = S();
        const r = 8 * s;
        const bx = x - w / 2, by = y - h / 2;
        const isH = (hoveredNode && hoveredNode.id === ndId);
        
        ctx.globalAlpha = getAlpha([ndId]);
        
        ctx.beginPath();
        ctx.roundRect(bx, by, w, h, r);
        ctx.fillStyle = isMajor ? "#101520" : "#0a0c0e";
        if (isH) ctx.fillStyle = isMajor ? "#121d2b" : "#12161a"; // Brighten bg on hover
        ctx.fill();
        
        ctx.strokeStyle = isH ? "#00e5ff" : isMajor ? "rgba(0,229,255,0.6)" : "rgba(255,255,255,0.18)";
        ctx.lineWidth = (isMajor || isH ? 2 : 1) * s;
        
        if (isH || isMajor) { 
            ctx.shadowColor = "#00e5ff"; 
            ctx.shadowBlur = isH ? 20 * s : (isMajor ? 12 * s : 0); 
        }
        ctx.stroke();
        ctx.shadowBlur = 0;
    }

    function drawLabel(x, y, h, lines, ndId, isMajor) {
        const s = S();
        const isH = (hoveredNode && hoveredNode.id === ndId);
        ctx.globalAlpha = getAlpha([ndId]);
        ctx.fillStyle = "#ffffff";
        ctx.font = `${Math.max(9, (isMajor ? 15 : 12) * s)}px Inter, system-ui`;
        if (isH) { ctx.shadowColor = "#00e5ff"; ctx.shadowBlur = 5 * s; }
        ctx.textAlign = "center";
        ctx.textBaseline = "middle";
        if (Array.isArray(lines)) {
            const gap = 12 * s;
            ctx.fillText(lines[0], x, y - gap * 0.5);
            ctx.fillStyle = isMajor ? "#00e5ff" : "#aaaaaa";
            if (isH && !isMajor) ctx.fillStyle = "#fff";
            ctx.font = `${Math.max(8, (isMajor ? 12 : 10) * s)}px Inter, system-ui`;
            ctx.shadowBlur = 0;
            ctx.fillText(lines[1], x, y + gap * 0.9);
        } else {
            ctx.fillText(lines, x, y);
        }
        ctx.shadowBlur = 0;
        ctx.globalAlpha = 1.0;
    }

    function drawMotor(x, y, w, ndId) {
        const s = S();
        const r = w / 2;
        const isH = (hoveredNode && hoveredNode.id === ndId);
        ctx.globalAlpha = getAlpha([ndId]);
        
        ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2);
        ctx.fillStyle = isH ? "#1a2228" : "#111";
        ctx.strokeStyle = isH ? "#00e5ff" : "rgba(255,255,255,0.25)";
        ctx.lineWidth = (isH ? 2 : 1.5) * s;
        if (isH) { ctx.shadowColor = "#00e5ff"; ctx.shadowBlur = 12 * s; }
        ctx.fill(); ctx.stroke();
        ctx.shadowBlur = 0;
        
        // Spinning blades
        ctx.save(); ctx.translate(x, y); ctx.rotate(time * (isH ? 0.008 : 0.003));
        ctx.fillStyle = isH ? "#00e5ff" : "#ccc";
        for (let i = 0; i < 3; i++) {
            ctx.rotate((Math.PI * 2) / 3);
            ctx.beginPath();
            ctx.rect(-3 * s, -r * 0.85, 6 * s, r * 0.7);
            ctx.fill();
        }
        ctx.restore();
        
        ctx.beginPath(); ctx.arc(x, y, 5 * s, 0, Math.PI * 2);
        ctx.fillStyle = "#fff"; ctx.fill();
        
        ctx.fillStyle = "#fff";
        ctx.font = `${Math.max(8, 11 * s)}px Inter, system-ui`;
        ctx.textAlign = "center"; ctx.textBaseline = "top";
        ctx.fillText("Motor", x, y + r + 6 * s);
        ctx.globalAlpha = 1.0;
    }

    function drawDesktop(x, y, w, label, ndId) {
        const s = S();
        const mw = w * 1.4, mh = w * 0.9;
        const screenTop = y - mh / 2;
        const isH = (hoveredNode && hoveredNode.id === ndId);
        
        ctx.globalAlpha = getAlpha([ndId]);

        ctx.beginPath();
        ctx.roundRect(x - mw / 2, screenTop, mw, mh, 5 * s);
        ctx.fillStyle = isH ? "#0d1522" : "#0a0c0e";
        ctx.strokeStyle = isH ? "#00e5ff" : "rgba(255,255,255,0.28)";
        ctx.lineWidth = 1.5 * s;
        if (isH) { ctx.shadowColor = "#00e5ff"; ctx.shadowBlur = 15 * s; }
        ctx.fill(); ctx.stroke();
        ctx.shadowBlur = 0;

        const bInset = 5 * s;
        ctx.beginPath();
        ctx.roundRect(x - mw / 2 + bInset, screenTop + bInset, mw - bInset * 2, mh - bInset * 2, 3 * s);
        ctx.fillStyle = isH ? "rgba(0,229,255,0.08)" : "rgba(255,255,255,0.02)";
        ctx.fill();

        ctx.fillStyle = isH ? "#7ed4ff" : "#cdd6df";
        ctx.font = `500 ${Math.max(9, 11 * s)}px Inter, system-ui`;
        ctx.textAlign = "center"; ctx.textBaseline = "middle";
        ctx.fillText(label[0], x, y - 7 * s);
        ctx.fillStyle = isH ? "rgba(0,200,255,0.7)" : "rgba(255,255,255,0.35)";
        ctx.font = `400 ${Math.max(7, 9 * s)}px Inter, system-ui`;
        ctx.fillText(label[1], x, y + 9 * s);

        const neckW = mw * 0.12, neckH = 6 * s;
        ctx.fillStyle = "#0a0c0e";
        ctx.strokeStyle = isH ? "#00e5ff" : "rgba(255,255,255,0.28)";
        ctx.lineWidth = 1 * s;
        ctx.beginPath();
        ctx.rect(x - neckW / 2, y + mh / 2, neckW, neckH);
        ctx.fill(); ctx.stroke();

        ctx.beginPath();
        ctx.roundRect(x - mw * 0.32, y + mh / 2 + neckH, mw * 0.64, 5 * s, 2 * s);
        ctx.fill(); ctx.stroke();
        ctx.globalAlpha = 1.0;
    }

    function buildRailPts(pts, dir, gap) {
        const result = [];
        for (let i = 0; i < pts.length; i++) {
            let ox = 0, oy = 0;
            if (i > 0) {
                const pdx = pts[i][0] - pts[i-1][0];
                const pdy = pts[i][1] - pts[i-1][1];
                if (Math.abs(pdx) > Math.abs(pdy)) oy += dir * gap;
                else                                ox += dir * gap;
            }
            if (i < pts.length - 1) {
                const ndx = pts[i+1][0] - pts[i][0];
                const ndy = pts[i+1][1] - pts[i][1];
                if (Math.abs(ndx) > Math.abs(ndy)) oy += dir * gap;
                else                                ox += dir * gap;
            }
            result.push([pts[i][0] + ox, pts[i][1] + oy]);
        }
        return result;
    }

    function animatePts(pts) {
        // Return truncated points based on loadProgress. Starts from middle node typically.
        // For simplicity, just scale the total line from origin pt to end pt if simple.
        if (loadProgress >= 0.99) return pts;
        
        const newPts = [pts[0]];
        let totalLen = 0;
        const segs = [];
        for (let i = 1; i < pts.length; i++) {
            const dx = pts[i][0] - pts[i-1][0];
            const dy = pts[i][1] - pts[i-1][1];
            const d = Math.hypot(dx, dy);
            segs.push({d, dx, dy, x:pts[i-1][0], y:pts[i-1][1]});
            totalLen += d;
        }
        
        let targetLen = totalLen * loadProgress;
        for (const seg of segs) {
            if (targetLen > seg.d) {
                newPts.push([seg.x + seg.dx, seg.y + seg.dy]);
                targetLen -= seg.d;
            } else {
                const ratio = targetLen / seg.d;
                newPts.push([seg.x + seg.dx * ratio, seg.y + seg.dy * ratio]);
                break;
            }
        }
        return newPts;
    }

    function drawRail(rawPts, color, s, dir, gap) {
        const pts = animatePts(rawPts);
        if (pts.length < 2) return;
        const rpts = buildRailPts(pts, dir, gap);
        const cr = 9 * s; 
        ctx.strokeStyle = color;
        ctx.lineWidth   = 1.5 * s;
        ctx.setLineDash([6 * s, 5 * s]);
        ctx.lineDashOffset = -time * 0.022 * dir;
        ctx.beginPath();
        ctx.moveTo(rpts[0][0], rpts[0][1]);
        for (let i = 1; i < rpts.length - 1; i++) {
            // ArcTo fails if segments are too short, wrap in safe try blocks normally
            ctx.lineTo(rpts[i][0], rpts[i][1]); // simplified for robust animation
        }
        ctx.lineTo(rpts[rpts.length - 1][0], rpts[rpts.length - 1][1]);
        ctx.stroke();
        ctx.setLineDash([]);
    }

    function polyline(rawPts, color, dashScale, thick, linkNodeIds) {
        const s = S();
        ctx.globalAlpha = getAlpha(linkNodeIds, true);
        
        if (dashScale) {
            const gap = 5 * s;
            drawRail(rawPts, color, s,  1, gap);
            drawRail(rawPts, color, s, -1, gap);
        } else {
            const pts = animatePts(rawPts);
            if (pts.length < 2) return;
            ctx.beginPath();
            ctx.moveTo(pts[0][0], pts[0][1]);
            for (let i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]);
            ctx.strokeStyle = color;
            ctx.lineWidth   = (thick || 3) * s;
            ctx.setLineDash([]);
            
            // Add glow if highlighted
            if (ctx.globalAlpha > 0.5) {
                ctx.shadowColor = "rgba(0,229,255,0.55)";
                ctx.shadowBlur  = 12 * s;
            }
            ctx.stroke();
            ctx.shadowBlur = 0;
        }
        ctx.globalAlpha = 1.0;
    }

    const DATA_COLOR = "rgba(255,65,65,0.88)";
    const POWER_COLOR = "rgba(0,229,255,0.9)";

    function draw() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const s = S();

        // Load progress interpolation (0 to 1 over ~1s)
        if (loadProgress < 1) loadProgress += 0.025;
        if (loadProgress > 1) loadProgress = 1;

        // 1. Background
        ctx.fillStyle = "transparent";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        // 2. ── DATA CONNECTIONS (red dashed) ──────────────────
        const bbGap = 5 * s; 

        polyline([
            [cx(X_MB), cy(Y_MB) - 25 * s],
            [cx(X_MB), cy(Y_TOP) + 42 * s] // From MB UP to App
        ], DATA_COLOR, true, 1, ["MB", "APP"]);

        polyline([
            [cx(X_MB) + 85 * s, cy(Y_MB)], // From MB RIGHT to MCU
            [cx(X_MCU), cy(Y_MB)],
            [cx(X_MCU), cy(Y_TOP) + 22 * s]
        ], DATA_COLOR, true, 1, ["MB", "MCU"]);
        
        ctx.globalAlpha = getAlpha(["MB", "MCU"]);
        ctx.fillStyle = "#ffffff";
        ctx.font = `${Math.max(8, 10 * s)}px Inter`;
        ctx.textAlign = "center";
        ctx.fillText("SPI", cx((X_MCU + X_MB) / 2 + 0.05), cy(Y_MB) - 8 * s);
        ctx.globalAlpha = 1.0;

        polyline([
            [cx(X_MB), cy(Y_MB) + 25 * s], // From MB DOWN to CAN
            [cx(X_MB), cy(Y_CAN) - bbGap]
        ], DATA_COLOR, true, 1, ["MB", "CAN"]);

        // 4. ── CAN BUS BACKBONE ───────────────────────────────
        const canY = cy(Y_CAN);
        const canLeft = cx(0.5) - (cx(0.95)-cx(0.5)) * loadProgress;
        const canRight = cx(0.5) + (cx(0.95)-cx(0.5)) * loadProgress;
        const isCH = hoveredNode && hoveredNode.id === "CAN";
        
        ctx.globalAlpha = getAlpha(["CAN", "TEMP", "IMU", "DIST", "DRV", "MB", "PWR"]);
        const bbColor = isCH ? "#ff4141" : "rgba(255,65,65,0.80)";
        if (isCH) { ctx.shadowColor = "rgba(255,65,65,0.8)"; ctx.shadowBlur = 12 * s; }
        ctx.strokeStyle = bbColor;
        ctx.lineWidth   = 1.8 * s;
        
        ctx.beginPath();
        ctx.moveTo(canLeft, canY - bbGap);
        ctx.lineTo(canRight, canY - bbGap);
        ctx.setLineDash([8 * s, 6 * s]);
        ctx.lineDashOffset = -time * 0.022;
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(canLeft, canY + bbGap);
        ctx.lineTo(canRight, canY + bbGap);
        ctx.lineDashOffset = time * 0.022;
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.shadowBlur = 0;

        ctx.fillStyle = isCH ? "#00e5ff" : "rgba(0, 229, 255, 0.75)";
        ctx.font = `${Math.max(9, 11 * s)}px Inter, system-ui`;
        ctx.textAlign = "center"; ctx.textBaseline = "bottom";
        if (loadProgress > 0.5) {
            ctx.fillText("UNIFIED INTERFACE — Deterministic Multi-Node Communication", cx(0.50), canY - bbGap - 8 * s);
        }
        ctx.globalAlpha = 1.0;

        // 5. ── STUBS (CAN → each module) ─────────────────────
        const stubTop = canY + bbGap;
        const stubBot = cy(Y_MODS) - 22 * s;
        polyline([[cx(X_TEMP), stubTop], [cx(X_TEMP), stubBot]], DATA_COLOR, true, 1, ["CAN", "TEMP"]);
        polyline([[cx(X_IMU), stubTop], [cx(X_IMU), stubBot]], DATA_COLOR, true, 1, ["CAN", "IMU"]);
        polyline([[cx(X_DIST), stubTop], [cx(X_DIST), stubBot]], DATA_COLOR, true, 1, ["CAN", "DIST"]);
        polyline([[cx(X_DRV), stubTop], [cx(X_DRV), stubBot]], DATA_COLOR, true, 1, ["CAN", "DRV"]);
        polyline([[cx(X_PWR), stubTop], [cx(X_PWR), cy(Y_PWR) - 22 * s]], DATA_COLOR, true, 1, ["CAN", "PWR"]);

        // 6. ── POWER CONNECTIONS (solid cyan) ─────────────────
        polyline([
            [cx(X_PWR), cy(Y_PWR) + 22 * s],
            [cx(X_PWR), cy(Y_BAT) - 20 * s] // From PWR DOWN to BAT
        ], POWER_COLOR, false, 3, ["PWR", "BAT"]);

        polyline([
            [cx(X_PWR) + 85 * s, cy(Y_PWR)], // From PWR RIGHT to DRV
            [cx(X_DRV), cy(Y_PWR)]
        ], POWER_COLOR, false, 3, ["PWR", "DRV"]);
        
        ctx.globalAlpha = getAlpha(["PWR", "DRV"]);
        ctx.fillStyle = "rgba(0,229,255,0.75)";
        ctx.font = `${Math.max(8, 10 * s)}px Inter, system-ui`;
        ctx.textAlign = "center"; ctx.textBaseline = "top";
        ctx.fillText("Power Rail", cx((X_PWR + X_DRV) / 2), cy(Y_PWR) + 7 * s);
        ctx.globalAlpha = 1.0;

        polyline([
            [cx(X_DRV) + 60 * s, cy(Y_MODS)], // From DRV RIGHT to MOT
            [cx(X_MOT) - 26 * s, cy(Y_MODS)]
        ], POWER_COLOR, false, 3, ["DRV", "MOT"]);
        
        ctx.globalAlpha = getAlpha(["DRV", "MOT"]);
        ctx.fillStyle = "rgba(0,229,255,0.75)";
        ctx.font = `${Math.max(8, 10 * s)}px Inter, system-ui`;
        ctx.textAlign = "center"; ctx.textBaseline = "bottom";
        ctx.fillText("Power + Control", cx((X_DRV + X_MOT) / 2 + 0.02), cy(Y_MODS) - 5 * s);
        ctx.globalAlpha = 1.0;

        // 7. ── DRAW NODES ───────────────────
        NODES.forEach(nd => {
            const x = cx(nd.x), y = cy(nd.y);
            const w = (nd.w || 120) * s;
            const h = (nd.h || 44) * s;
            const isMajor = nd.type === "box-major";

            if (nd.type === "can-hit") return;
            if (nd.type === "visual-motor") { drawMotor(x, y, w, nd.id); return; }
            if (nd.type === "visual-desktop") { drawDesktop(x, y, w, nd.label, nd.id); return; }

            drawBox(x, y, w, h, nd.id, isMajor);
            drawLabel(x, y, h, nd.label, nd.id, isMajor);
        });

        time += 16;
        requestAnimationFrame(draw);
    }
    
    // Slight delay before drawing logic starts filling out lines
    setTimeout(() => { draw(); }, 100);
});
"""

with open(js_file, 'w', encoding='utf-8') as f:
    f.write(new_js)

print("Updated js/diagram.js successfully")
