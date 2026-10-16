const fs = require('fs');
const path = require('path');

const svgDir = path.join(__dirname, 'assets', 'svg');
if (!fs.existsSync(svgDir)) {
  fs.mkdirSync(svgDir, { recursive: true });
}

// Common styles for all SVGs
const commonDef = `
  <defs>
    <linearGradient id="cyanGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06B6D4" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="amberGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="1"/>
      <stop offset="100%" stop-color="#F43F5E" stop-opacity="1"/>
    </linearGradient>
    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <marker id="arrowCyan" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M1,1 L7,4 L1,7 Z" fill="#38BDF8"/>
    </marker>
    <marker id="arrowAmber" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M1,1 L7,4 L1,7 Z" fill="#F43F5E"/>
    </marker>
    <marker id="arrowSlate" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <path d="M1,1 L7,4 L1,7 Z" fill="#64748B"/>
    </marker>
  </defs>
`;

// 1. Hook Curve SVG
const hookSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}
  <!-- Grid -->
  <g stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4">
    <line x1="80" y1="100" x2="880" y2="100"/>
    <line x1="80" y1="180" x2="880" y2="180"/>
    <line x1="80" y1="260" x2="880" y2="260"/>
    <line x1="80" y1="340" x2="880" y2="340"/>
    <line x1="80" y1="420" x2="880" y2="420"/>
    <line x1="160" y1="60" x2="160" y2="480"/>
    <line x1="320" y1="60" x2="320" y2="480"/>
    <line x1="480" y1="60" x2="480" y2="480"/>
    <line x1="640" y1="60" x2="640" y2="480"/>
    <line x1="800" y1="60" x2="800" y2="480"/>
  </g>
  <!-- Axes -->
  <line x1="80" y1="270" x2="880" y2="270" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
  <line x1="480" y1="480" x2="480" y2="60" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
  <text x="890" y="275" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600">x</text>
  <text x="480" y="45" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600" text-anchor="middle">y = f(x)</text>

  <!-- Curve: smooth cubic/polynomial terrain -->
  <path d="M 120 420 C 200 400, 260 140, 340 140 C 420 140, 500 390, 620 390 C 720 390, 780 180, 840 160"
        fill="none" stroke="url(#cyanGlow)" stroke-width="4" filter="url(#glowEffect)"/>

  <!-- Local Max 1 -->
  <circle cx="340" cy="140" r="7" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>
  <line x1="260" y1="140" x2="420" y2="140" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="6,4"/>
  <rect x="290" y="90" width="100" height="32" rx="6" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="340" y="112" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Local Max (f'=0)</text>

  <!-- Local Min 1 -->
  <circle cx="620" cy="390" r="7" fill="#38BDF8" stroke="#F8FAFC" stroke-width="2"/>
  <line x1="540" y1="390" x2="700" y2="390" stroke="#38BDF8" stroke-width="2.5" stroke-dasharray="6,4"/>
  <rect x="570" y="415" width="100" height="32" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="620" y="437" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">Local Min (f'=0)</text>

  <!-- Moving Point with Tangent Vector -->
  <circle cx="240" cy="230" r="6" fill="#EC4899" stroke="#F8FAFC" stroke-width="2"/>
  <line x1="180" y1="310" x2="300" y2="150" stroke="#EC4899" stroke-width="2" marker-end="url(#arrowAmber)"/>
  <text x="180" y="210" fill="#EC4899" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600">Slope &gt; 0 (Ascending)</text>
</svg>
`;

// 2. Local vs Absolute Extrema SVG
const localVsGlobalSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}
  <!-- Grid -->
  <g stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4">
    <line x1="80" y1="270" x2="880" y2="270"/>
    <line x1="480" y1="60" x2="480" y2="480"/>
  </g>
  <!-- Axes -->
  <line x1="80" y1="450" x2="880" y2="450" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
  <line x1="120" y1="460" x2="120" y2="60" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
  <text x="890" y="455" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600">x</text>
  <text x="120" y="45" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600" text-anchor="middle">f(x)</text>

  <!-- Domain [a, b] Shading -->
  <rect x="200" y="80" width="620" height="370" fill="#1E293B" fill-opacity="0.25"/>
  <line x1="200" y1="440" x2="200" y2="460" stroke="#94A3B8" stroke-width="2"/>
  <line x1="820" y1="440" x2="820" y2="460" stroke="#94A3B8" stroke-width="2"/>
  <text x="200" y="480" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600" text-anchor="middle">a (Left End)</text>
  <text x="820" y="480" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="600" text-anchor="middle">b (Right End)</text>

  <!-- Curve -->
  <path d="M 200 320 C 260 160, 320 160, 380 160 C 460 160, 520 400, 600 400 C 680 400, 740 220, 820 90"
        fill="none" stroke="url(#cyanGlow)" stroke-width="4"/>

  <!-- Left Endpoint -->
  <circle cx="200" cy="320" r="6" fill="#64748B" stroke="#F8FAFC" stroke-width="2"/>
  <text x="215" y="325" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="14">f(a)</text>

  <!-- Local Max (Interior) -->
  <circle cx="380" cy="160" r="7" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>
  <!-- Neighborhood interval -->
  <rect x="330" y="152" width="100" height="16" fill="#F59E0B" fill-opacity="0.15" rx="4"/>
  <line x1="330" y1="160" x2="430" y2="160" stroke="#F59E0B" stroke-width="2" stroke-dasharray="4,2"/>
  <rect x="300" y="105" width="160" height="36" rx="6" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="380" y="128" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">LOCAL MAXIMUM</text>

  <!-- Absolute Min (Interior) -->
  <circle cx="600" cy="400" r="8" fill="#38BDF8" stroke="#F8FAFC" stroke-width="2" filter="url(#glowEffect)"/>
  <rect x="510" y="420" width="180" height="36" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="600" y="443" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ABSOLUTE MINIMUM</text>

  <!-- Absolute Max (Right Endpoint b) -->
  <circle cx="820" cy="90" r="9" fill="#F43F5E" stroke="#F8FAFC" stroke-width="2.5" filter="url(#glowEffect)"/>
  <line x1="120" y1="90" x2="820" y2="90" stroke="#F43F5E" stroke-width="1.5" stroke-dasharray="4,4"/>
  <rect x="710" y="45" width="190" height="36" rx="6" fill="#1E293B" stroke="#F43F5E" stroke-width="1.5"/>
  <text x="805" y="68" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">ABSOLUTE MAXIMUM (at b)</text>
</svg>
`;

// 3. Slopes and Intervals SVG
const slopesIntervalsSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}
  <!-- Grid -->
  <g stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4">
    <line x1="80" y1="270" x2="880" y2="270"/>
    <line x1="480" y1="60" x2="480" y2="480"/>
  </g>
  <!-- Axes -->
  <line x1="80" y1="460" x2="880" y2="460" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
  <line x1="120" y1="460" x2="120" y2="60" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>

  <!-- Zone 1: Increasing [120 -> 480] -->
  <path d="M 160 400 C 260 380, 360 160, 480 160"
        fill="none" stroke="#38BDF8" stroke-width="5" filter="url(#glowEffect)"/>
  <!-- Tangent vector 1 -->
  <line x1="280" y1="330" x2="380" y2="230" stroke="#38BDF8" stroke-width="2.5" marker-end="url(#arrowCyan)"/>
  <rect x="230" y="345" width="170" height="40" rx="6" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
  <text x="315" y="370" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">f'(x) &gt; 0 (INCREASING)</text>

  <!-- Peak at 480, 160 -->
  <circle cx="480" cy="160" r="8" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>
  <line x1="390" y1="160" x2="570" y2="160" stroke="#F59E0B" stroke-width="3" stroke-dasharray="6,4"/>
  <rect x="400" y="95" width="160" height="42" rx="6" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
  <text x="480" y="122" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">PEAK: f'(c) = 0</text>

  <!-- Zone 2: Decreasing [480 -> 800] -->
  <path d="M 480 160 C 600 160, 700 380, 800 400"
        fill="none" stroke="#F43F5E" stroke-width="5" filter="url(#glowEffect)"/>
  <!-- Tangent vector 2 -->
  <line x1="580" y1="230" x2="680" y2="330" stroke="#F43F5E" stroke-width="2.5" marker-end="url(#arrowAmber)"/>
  <rect x="560" y="345" width="170" height="40" rx="6" fill="#0F172A" stroke="#F43F5E" stroke-width="1.5"/>
  <text x="645" y="370" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">f'(x) &lt; 0 (DECREASING)</text>
</svg>
`;

// 4. Tangent to Stationary SVG
const tangentStationarySvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}
  <line x1="100" y1="460" x2="860" y2="460" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
  <line x1="480" y1="480" x2="480" y2="80" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>

  <!-- Parabolic peak -->
  <path d="M 200 420 Q 480 80, 760 420" fill="none" stroke="#38BDF8" stroke-width="4"/>

  <!-- Converging Tangents -->
  <!-- Left tangent (steep) -->
  <line x1="260" y1="360" x2="400" y2="180" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="340" cy="250" r="4" fill="#64748B"/>
  <text x="270" y="270" fill="#64748B" font-family="-apple-system, system-ui, sans-serif" font-size="13">m = +2.5</text>

  <!-- Left tangent (shallower) -->
  <line x1="340" y1="210" x2="500" y2="135" stroke="#94A3B8" stroke-width="2"/>
  <circle cx="420" cy="172" r="5" fill="#94A3B8"/>
  <text x="370" y="160" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13">m = +0.8</text>

  <!-- Perfect Horizontal at Apex -->
  <line x1="300" y1="130" x2="660" y2="130" stroke="#F59E0B" stroke-width="3" filter="url(#glowEffect)"/>
  <circle cx="480" cy="130" r="8" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>

  <!-- Callout Card -->
  <rect x="330" y="50" width="300" height="56" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="2"/>
  <text x="480" y="75" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">FERMAT'S THEOREM</text>
  <text x="480" y="96" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">At interior extremum, slope = 0 ⇒ f'(c) = 0</text>
</svg>
`;

// 5. Cusp & Corner DNE SVG
const cuspCornerSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}

  <!-- Divider line -->
  <line x1="480" y1="40" x2="480" y2="500" stroke="#334155" stroke-width="2" stroke-dasharray="6,6"/>

  <!-- Left Side: Corner |x| -->
  <g transform="translate(40, 0)">
    <text x="200" y="70" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Case A: The Corner (f(x) = |x|)</text>
    <line x1="40" y1="360" x2="380" y2="360" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
    <line x1="210" y1="420" x2="210" y2="120" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>

    <!-- Sharp V curve -->
    <path d="M 70 220 L 210 360 L 350 220" fill="none" stroke="#38BDF8" stroke-width="4"/>
    <circle cx="210" cy="360" r="7" fill="#F43F5E" stroke="#F8FAFC" stroke-width="2"/>

    <!-- Slopes -->
    <text x="110" y="270" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600">Left slope = -1</text>
    <text x="270" y="270" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600">Right slope = +1</text>

    <rect x="80" y="400" width="260" height="60" rx="8" fill="#1E293B" stroke="#F43F5E" stroke-width="1.5"/>
    <text x="210" y="425" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">f'(0) DOES NOT EXIST (DNE)</text>
    <text x="210" y="445" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Yet x=0 is a true Local Minimum!</text>
  </g>

  <!-- Right Side: Cusp x^(2/3) -->
  <g transform="translate(520, 0)">
    <text x="200" y="70" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="20" font-weight="700" text-anchor="middle">Case B: The Cusp (f(x) = x^(2/3))</text>
    <line x1="40" y1="360" x2="380" y2="360" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
    <line x1="210" y1="420" x2="210" y2="120" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>

    <!-- Cusp shape -->
    <path d="M 70 180 C 140 300, 190 350, 210 360 C 230 350, 280 300, 350 180" fill="none" stroke="#38BDF8" stroke-width="4"/>
    <circle cx="210" cy="360" r="7" fill="#F43F5E" stroke="#F8FAFC" stroke-width="2"/>

    <!-- Slopes tending to vertical -->
    <text x="80" y="270" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600">Slope → -∞</text>
    <text x="290" y="270" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600">Slope → +∞</text>

    <rect x="80" y="400" width="260" height="60" rx="8" fill="#1E293B" stroke="#F43F5E" stroke-width="1.5"/>
    <text x="210" y="425" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">VERTICAL TANGENT (DNE)</text>
    <text x="210" y="445" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Sharp Local Minimum at x=0!</text>
  </g>
</svg>
`;

// 6. Stationary Inflection SVG (x^3)
const stationaryInflectionSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}
  <!-- Grid -->
  <g stroke="#1E293B" stroke-width="1" stroke-dasharray="4,4">
    <line x1="80" y1="270" x2="880" y2="270"/>
    <line x1="480" y1="60" x2="480" y2="480"/>
  </g>
  <line x1="80" y1="270" x2="880" y2="270" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
  <line x1="480" y1="480" x2="480" y2="60" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>

  <!-- Curve: y = x^3 -->
  <path d="M 220 440 C 360 410, 420 280, 480 270 C 540 260, 600 130, 740 100"
        fill="none" stroke="#38BDF8" stroke-width="4.5" filter="url(#glowEffect)"/>

  <!-- Horizontal Tangent at origin -->
  <line x1="320" y1="270" x2="640" y2="270" stroke="#F59E0B" stroke-width="3" stroke-dasharray="6,4"/>
  <circle cx="480" cy="270" r="8" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>

  <!-- Slopes on both sides -->
  <rect x="250" y="320" width="170" height="36" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1"/>
  <text x="335" y="343" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">x &lt; 0: f'(x) = 3x² &gt; 0 ↗</text>

  <rect x="540" y="190" width="170" height="36" rx="6" fill="#1E293B" stroke="#38BDF8" stroke-width="1"/>
  <text x="625" y="213" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">x &gt; 0: f'(x) = 3x² &gt; 0 ↗</text>

  <!-- Big Warning Banner -->
  <rect x="260" y="50" width="440" height="64" rx="10" fill="#1E1E2E" stroke="#F43F5E" stroke-width="2"/>
  <text x="480" y="78" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="17" font-weight="700" text-anchor="middle">CRITICAL MISCONCEPTION ALERT</text>
  <text x="480" y="100" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">f'(0) = 0, but x=0 is NEITHER a maximum nor a minimum!</text>
</svg>
`;

// 7. First Derivative Sign Chart SVG
const signChartSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}

  <text x="480" y="55" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">THE FIRST DERIVATIVE TEST (FDT)</text>
  <text x="480" y="85" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="15" text-anchor="middle">Translating the sign of f'(x) into turning behavior</text>

  <!-- Case 1: Max (+ to -) -->
  <g transform="translate(60, 120)">
    <rect width="250" height="340" rx="10" fill="#111827" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="125" y="35" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">LOCAL MAXIMUM</text>
    <!-- Number line -->
    <line x1="25" y1="110" x2="225" y2="110" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
    <circle cx="125" cy="110" r="6" fill="#F59E0B"/>
    <text x="125" y="135" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">c (f'=0)</text>
    <!-- Signs -->
    <text x="65" y="95" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">+</text>
    <text x="185" y="95" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">-</text>
    <!-- Shape diagram -->
    <path d="M 45 230 L 125 170 L 205 230" fill="none" stroke="#F59E0B" stroke-width="3.5"/>
    <text x="65" y="260" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Rising ↗</text>
    <text x="185" y="260" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Falling ↘</text>
    <text x="125" y="310" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Sign shifts: (+) → (-)</text>
  </g>

  <!-- Case 2: Min (- to +) -->
  <g transform="translate(355, 120)">
    <rect width="250" height="340" rx="10" fill="#111827" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="125" y="35" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">LOCAL MINIMUM</text>
    <!-- Number line -->
    <line x1="25" y1="110" x2="225" y2="110" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
    <circle cx="125" cy="110" r="6" fill="#38BDF8"/>
    <text x="125" y="135" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">c (f'=0)</text>
    <!-- Signs -->
    <text x="65" y="95" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">-</text>
    <text x="185" y="95" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">+</text>
    <!-- Shape diagram -->
    <path d="M 45 170 L 125 230 L 205 170" fill="none" stroke="#38BDF8" stroke-width="3.5"/>
    <text x="65" y="260" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Falling ↘</text>
    <text x="185" y="260" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Rising ↗</text>
    <text x="125" y="310" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Sign shifts: (-) → (+)</text>
  </g>

  <!-- Case 3: Neither (No change) -->
  <g transform="translate(650, 120)">
    <rect width="250" height="340" rx="10" fill="#111827" stroke="#64748B" stroke-width="1.5"/>
    <text x="125" y="35" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">NEITHER (TERRACE)</text>
    <!-- Number line -->
    <line x1="25" y1="110" x2="225" y2="110" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
    <circle cx="125" cy="110" r="6" fill="#64748B"/>
    <text x="125" y="135" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">c (f'=0)</text>
    <!-- Signs -->
    <text x="65" y="95" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">+</text>
    <text x="185" y="95" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">+</text>
    <!-- Shape diagram -->
    <path d="M 45 220 Q 125 200, 125 180 Q 125 160, 205 140" fill="none" stroke="#64748B" stroke-width="3.5"/>
    <text x="125" y="260" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Continuous climb</text>
    <text x="125" y="310" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">Sign DOES NOT CHANGE</text>
  </g>
</svg>
`;

// 8. Worked Example Cubic (x^3 - 3x) SVG
const workedExampleSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}

  <!-- Left Side: Graph of f(x) and f'(x) -->
  <g transform="translate(40, 20)">
    <text x="240" y="25" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">Geometric Synchronization</text>

    <!-- Axes -->
    <line x1="40" y1="260" x2="440" y2="260" stroke="#334155" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
    <line x1="240" y1="480" x2="240" y2="40" stroke="#334155" stroke-width="1.5" marker-end="url(#arrowSlate)"/>

    <!-- Scale ticks -->
    <!-- x = -1 at x=140, x = 1 at x=340 -->
    <line x1="140" y1="255" x2="140" y2="265" stroke="#94A3B8" stroke-width="2"/>
    <text x="140" y="280" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">-1</text>
    <line x1="340" y1="255" x2="340" y2="265" stroke="#94A3B8" stroke-width="2"/>
    <text x="340" y="280" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">+1</text>

    <!-- Curve f(x) = x^3 - 3x (scaled: y=-2 -> y=380, y=2 -> y=140) -->
    <path d="M 60 460 C 100 280, 120 140, 140 140 C 180 140, 200 260, 240 260 C 280 260, 300 380, 340 380 C 360 380, 380 240, 420 60"
          fill="none" stroke="#38BDF8" stroke-width="3.5" filter="url(#glowEffect)"/>
    <text x="430" y="80" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700">f(x)</text>

    <!-- Derivative f'(x) = 3x^2 - 3 (parabola opening up, roots at 140 and 340, vertex at (240, 350)) -->
    <path d="M 60 80 Q 240 440, 420 80"
          fill="none" stroke="#F59E0B" stroke-width="2.5" stroke-dasharray="6,4"/>
    <text x="430" y="120" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700">f'(x)</text>

    <!-- Vertical sync dashed lines -->
    <line x1="140" y1="40" x2="140" y2="480" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="340" y1="40" x2="340" y2="480" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="3,3"/>

    <!-- Key Points -->
    <circle cx="140" cy="140" r="7" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>
    <text x="135" y="120" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="end">(-1, 2) MAX</text>

    <circle cx="340" cy="380" r="7" fill="#38BDF8" stroke="#F8FAFC" stroke-width="2"/>
    <text x="345" y="410" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700"> (1, -2) MIN</text>
  </g>

  <!-- Right Side: The Sign Chart and Algebraic Stages -->
  <g transform="translate(540, 30)">
    <rect width="380" height="480" rx="10" fill="#111827" stroke="#334155" stroke-width="1"/>
    <text x="190" y="35" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">Algebraic Derivation</text>

    <!-- Step 1: Derivative -->
    <g transform="translate(20, 60)">
      <text x="0" y="20" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="14">Step 1: Differentiate &amp; Factor</text>
      <rect x="0" y="30" width="340" height="45" rx="6" fill="#1E293B"/>
      <text x="15" y="58" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="600">f'(x) = 3x² - 3 = 3(x - 1)(x + 1)</text>
    </g>

    <!-- Step 2: Critical Numbers -->
    <g transform="translate(20, 155)">
      <text x="0" y="20" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="14">Step 2: Solve f'(x) = 0</text>
      <rect x="0" y="30" width="340" height="45" rx="6" fill="#1E293B"/>
      <text x="15" y="58" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700">x = -1  and  x = +1</text>
    </g>

    <!-- Step 3: Sign Chart Table -->
    <g transform="translate(20, 250)">
      <text x="0" y="20" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="14">Step 3: Interval Sign Analysis</text>
      <rect x="0" y="30" width="340" height="110" rx="6" fill="#1E293B" stroke="#475569" stroke-width="1"/>

      <!-- Headers -->
      <line x1="0" y1="65" x2="340" y2="65" stroke="#475569" stroke-width="1"/>
      <line x1="110" y1="30" x2="110" y2="140" stroke="#475569" stroke-width="1"/>
      <line x1="225" y1="30" x2="225" y2="140" stroke="#475569" stroke-width="1"/>

      <text x="55" y="52" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">(-∞, -1)</text>
      <text x="167" y="52" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">(-1, 1)</text>
      <text x="282" y="52" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">(1, ∞)</text>

      <!-- Row 1: Test point -->
      <text x="55" y="85" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">x = -2: (+)</text>
      <text x="167" y="85" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">x = 0: (-)</text>
      <text x="282" y="85" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">x = 2: (+)</text>

      <!-- Row 2: Behavior -->
      <text x="55" y="120" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Increasing ↗</text>
      <text x="167" y="120" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Decreasing ↘</text>
      <text x="282" y="120" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Increasing ↗</text>
    </g>

    <!-- Step 4: Coordinates -->
    <g transform="translate(20, 395)">
      <rect x="0" y="15" width="340" height="55" rx="6" fill="#0F172A" stroke="#38BDF8" stroke-width="1.5"/>
      <text x="170" y="38" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">LOCAL MAX: (-1, 2)  [Sign: + to -]</text>
      <text x="170" y="58" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">LOCAL MIN: (1, -2)  [Sign: - to +]</text>
    </g>
  </g>
</svg>
`;

// 9. Second Derivative Concavity SVG
const concavitySvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}

  <line x1="480" y1="40" x2="480" y2="500" stroke="#334155" stroke-width="2" stroke-dasharray="6,6"/>

  <!-- Left: Concave Down -->
  <g transform="translate(40, 20)">
    <text x="200" y="45" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="20" font-weight="700" text-anchor="middle">CONCAVE DOWN (f''(c) &lt; 0)</text>
    <text x="200" y="70" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">Slopes decreasing: Tangents lie ABOVE curve</text>

    <!-- Inverted curve -->
    <path d="M 60 360 Q 200 120, 340 360" fill="none" stroke="#F59E0B" stroke-width="4.5"/>

    <!-- Tangents -->
    <line x1="60" y1="210" x2="180" y2="130" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,3"/>
    <line x1="110" y1="120" x2="290" y2="120" stroke="#F59E0B" stroke-width="3"/>
    <line x1="220" y1="130" x2="340" y2="210" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,3"/>

    <circle cx="200" cy="120" r="8" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>

    <rect x="60" y="400" width="280" height="65" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="200" y="425" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">f'(c) = 0 and f''(c) &lt; 0</text>
    <text x="200" y="448" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">⇒ LOCAL MAXIMUM</text>
  </g>

  <!-- Right: Concave Up -->
  <g transform="translate(520, 20)">
    <text x="200" y="45" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="20" font-weight="700" text-anchor="middle">CONCAVE UP (f''(c) &gt; 0)</text>
    <text x="200" y="70" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">Slopes increasing: Tangents lie BELOW curve</text>

    <!-- Upright cup curve -->
    <path d="M 60 140 Q 200 380, 340 140" fill="none" stroke="#38BDF8" stroke-width="4.5"/>

    <!-- Tangents -->
    <line x1="60" y1="280" x2="180" y2="360" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,3"/>
    <line x1="110" y1="380" x2="290" y2="380" stroke="#38BDF8" stroke-width="3"/>
    <line x1="220" y1="360" x2="340" y2="280" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="4,3"/>

    <circle cx="200" cy="380" r="8" fill="#38BDF8" stroke="#F8FAFC" stroke-width="2"/>

    <rect x="60" y="400" width="280" height="65" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="200" y="425" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">f'(c) = 0 and f''(c) &gt; 0</text>
    <text x="200" y="448" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">⇒ LOCAL MINIMUM</text>
  </g>
</svg>
`;

// 10. Closed Interval Endpoints SVG
const closedIntervalSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}

  <text x="480" y="40" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="20" font-weight="700" text-anchor="middle">THE CLOSED INTERVAL METHOD: f(x) = x³ - 3x on [-0.5, 2.5]</text>

  <!-- Left Graph -->
  <g transform="translate(40, 50)">
    <!-- Axes -->
    <line x1="30" y1="330" x2="450" y2="330" stroke="#334155" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
    <line x1="160" y1="440" x2="160" y2="30" stroke="#334155" stroke-width="1.5" marker-end="url(#arrowSlate)"/>

    <!-- Shaded Domain [-0.5, 2.5] -->
    <!-- Scale: origin (x=0) at x=160, 1 unit = 90 px -->
    <!-- x = -0.5 is at 115, x = 2.5 is at 385 -->
    <rect x="115" y="40" width="270" height="380" fill="#1E293B" fill-opacity="0.35"/>
    <line x1="115" y1="420" x2="115" y2="40" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4"/>
    <line x1="385" y1="420" x2="385" y2="40" stroke="#64748B" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="115" y="355" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">-0.5</text>
    <text x="385" y="355" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">+2.5</text>

    <!-- Curve on interval -->
    <!-- f(-0.5) = 1.375 (y=290 - 1.375*30 = 248) -->
    <!-- min at x=1: f(1)=-2 (y=290 - (-2)*30 = 350) -> x=250, y=390 -->
    <!-- max at x=2.5: f(2.5)=8.125 (y=290 - 8.125*30 = 46) -> x=385, y=55 -->
    <path d="M 115 288 C 180 320, 210 390, 250 390 C 290 390, 330 220, 385 55"
          fill="none" stroke="#38BDF8" stroke-width="4.5" filter="url(#glowEffect)"/>

    <!-- Outside region ghost curve showing x=-1 peak -->
    <path d="M 50 390 C 60 220, 70 270, 115 288" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="4,4"/>
    <circle cx="70" cy="270" r="5" fill="#64748B"/>
    <line x1="60" y1="260" x2="80" y2="280" stroke="#F43F5E" stroke-width="2"/>
    <line x1="80" y1="260" x2="60" y2="280" stroke="#F43F5E" stroke-width="2"/>
    <text x="70" y="250" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">x=-1 (OUTSIDE DOMAIN)</text>

    <!-- Points -->
    <!-- Left Endpoint: (-0.5, 1.375) -->
    <circle cx="115" cy="288" r="6" fill="#64748B" stroke="#F8FAFC" stroke-width="2"/>
    <text x="130" y="280" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12">f(-0.5) = 1.375</text>

    <!-- Critical Interior: (1, -2) -->
    <circle cx="250" cy="390" r="8" fill="#38BDF8" stroke="#F8FAFC" stroke-width="2"/>
    <text x="250" y="420" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">ABS MIN: (1, -2)</text>

    <!-- Right Endpoint: (2.5, 8.125) -->
    <circle cx="385" cy="55" r="9" fill="#F43F5E" stroke="#F8FAFC" stroke-width="2.5" filter="url(#glowEffect)"/>
    <text x="375" y="45" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="end">ABS MAX: (2.5, 8.125)</text>
  </g>

  <!-- Right Evaluation Table -->
  <g transform="translate(540, 70)">
    <rect width="380" height="420" rx="10" fill="#111827" stroke="#334155" stroke-width="1"/>
    <text x="190" y="35" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="18" font-weight="700" text-anchor="middle">Candidate Comparison Table</text>

    <rect x="20" y="60" width="340" height="240" rx="8" fill="#1E293B" stroke="#475569" stroke-width="1"/>

    <!-- Table Header -->
    <line x1="20" y1="105" x2="360" y2="105" stroke="#475569" stroke-width="1"/>
    <line x1="140" y1="60" x2="140" y2="300" stroke="#475569" stroke-width="1"/>
    <line x1="240" y1="60" x2="240" y2="300" stroke="#475569" stroke-width="1"/>

    <text x="80" y="90" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Candidate x</text>
    <text x="190" y="90" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Value f(x)</text>
    <text x="300" y="90" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">Classification</text>

    <!-- Row 1: x = -1 -->
    <line x1="20" y1="150" x2="360" y2="150" stroke="#334155" stroke-width="1"/>
    <text x="80" y="132" fill="#64748B" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">x = -1</text>
    <text x="190" y="132" fill="#64748B" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">N/A</text>
    <text x="300" y="132" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">EXCLUDED (∉ domain)</text>

    <!-- Row 2: x = -0.5 -->
    <line x1="20" y1="200" x2="360" y2="200" stroke="#334155" stroke-width="1"/>
    <text x="80" y="180" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">x = -0.5 (Left)</text>
    <text x="190" y="180" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600" text-anchor="middle">1.375</text>
    <text x="300" y="180" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Interior/Endpoint</text>

    <!-- Row 3: x = 1 -->
    <line x1="20" y1="250" x2="360" y2="250" stroke="#334155" stroke-width="1"/>
    <text x="80" y="230" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">x = 1 (Interior)</text>
    <text x="190" y="230" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">-2.000</text>
    <text x="300" y="230" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">ABSOLUTE MIN</text>

    <!-- Row 4: x = 2.5 -->
    <text x="80" y="280" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">x = 2.5 (Right)</text>
    <text x="190" y="280" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">8.125</text>
    <text x="300" y="280" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">ABSOLUTE MAX</text>

    <!-- Warning Summary -->
    <rect x="20" y="320" width="340" height="70" rx="8" fill="#0F172A" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="190" y="345" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">ENGINEERING TAKEAWAY</text>
    <text x="190" y="365" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Never omit endpoints! The true maximum occurs at the</text>
    <text x="190" y="380" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">boundary (x = 2.5), NOT where f'(x) = 0.</text>
  </g>
</svg>
`;

// 11. Engineering Max Power SVG
const maxPowerSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}

  <text x="480" y="45" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="20" font-weight="700" text-anchor="middle">ENGINEERING OPTIMIZATION: MAXIMUM POWER TRANSFER THEOREM</text>

  <!-- Left Side: Circuit Schematic -->
  <g transform="translate(50, 80)">
    <rect width="360" height="400" rx="10" fill="#111827" stroke="#334155" stroke-width="1"/>
    <text x="180" y="35" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Thevenin Equivalent Circuit</text>

    <!-- Schematic Wires -->
    <!-- Loop: (60, 180) to (300, 180) to (300, 320) to (60, 320) back -->
    <path d="M 90 200 L 90 140 L 170 140" fill="none" stroke="#94A3B8" stroke-width="3"/>
    <!-- Resistor Rs -->
    <path d="M 170 140 L 180 130 L 190 150 L 200 130 L 210 150 L 220 130 L 230 150 L 240 140" fill="none" stroke="#F59E0B" stroke-width="3"/>
    <text x="205" y="120" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">Source Rs</text>
    <path d="M 240 140 L 300 140 L 300 190" fill="none" stroke="#94A3B8" stroke-width="3"/>

    <!-- Load Resistor RL (Adjustable) -->
    <path d="M 300 190 L 290 200 L 310 210 L 290 220 L 310 230 L 290 240 L 310 250 L 300 260" fill="none" stroke="#38BDF8" stroke-width="3"/>
    <!-- Diagonal arrow through RL -->
    <line x1="280" y1="260" x2="320" y2="190" stroke="#38BDF8" stroke-width="2" marker-end="url(#arrowCyan)"/>
    <text x="335" y="230" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700">Load RL</text>

    <path d="M 300 260 L 300 320 L 90 320 L 90 260" fill="none" stroke="#94A3B8" stroke-width="3"/>

    <!-- Voltage Source Vs -->
    <circle cx="90" cy="230" r="22" fill="#1E293B" stroke="#94A3B8" stroke-width="2"/>
    <text x="90" y="225" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">+</text>
    <text x="90" y="242" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700" text-anchor="middle">-</text>
    <text x="50" y="235" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="700">Vs</text>

    <!-- Mathematical Formula Box -->
    <rect x="25" y="340" width="310" height="45" rx="6" fill="#1E293B"/>
    <text x="180" y="368" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="14" font-weight="600" text-anchor="middle">P(RL) = Vs² · RL / (Rs + RL)²</text>
  </g>

  <!-- Right Side: Power Curve Graph -->
  <g transform="translate(470, 80)">
    <rect width="440" height="400" rx="10" fill="#111827" stroke="#334155" stroke-width="1"/>
    <text x="220" y="35" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">Power Characteristic Curve P(RL)</text>

    <!-- Axes -->
    <line x1="50" y1="330" x2="400" y2="330" stroke="#475569" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
    <line x1="70" y1="340" x2="70" y2="60" stroke="#475569" stroke-width="1.5" marker-end="url(#arrowSlate)"/>
    <text x="410" y="335" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13">RL</text>
    <text x="70" y="50" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="13" text-anchor="middle">P(RL)</text>

    <!-- Curve: starts at (70, 330), rises steeply to peak at x=190, y=140, then gently decays asymptotically -->
    <path d="M 70 330 C 110 240, 150 140, 190 140 C 250 140, 320 220, 390 260"
          fill="none" stroke="#38BDF8" stroke-width="4" filter="url(#glowEffect)"/>

    <!-- Peak Annotation -->
    <line x1="190" y1="140" x2="190" y2="330" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="4,4"/>
    <circle cx="190" cy="140" r="8" fill="#F59E0B" stroke="#F8FAFC" stroke-width="2"/>
    <text x="190" y="350" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">RL = Rs</text>

    <!-- Peak Value Label -->
    <line x1="70" y1="140" x2="190" y2="140" stroke="#F59E0B" stroke-width="1.5" stroke-dasharray="4,4"/>
    <text x="60" y="145" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="end">Vs² / 4Rs</text>

    <!-- Callout Banner -->
    <rect x="70" y="70" width="280" height="50" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1.5"/>
    <text x="210" y="93" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="700" text-anchor="middle">IMPEDANCE MATCHING CONDITION</text>
    <text x="210" y="110" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">dP/dRL = 0  ⇒  RL = Rs</text>
  </g>
</svg>
`;

// 12. Optimization Flowchart SVG
const flowchartSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 540" width="100%" height="100%">
  <rect width="960" height="540" fill="#0B0F19" rx="12"/>
  ${commonDef}

  <text x="480" y="45" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="22" font-weight="700" text-anchor="middle">THE ENGINEERING OPTIMIZATION PROTOCOL</text>
  <text x="480" y="72" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="14" text-anchor="middle">Deterministic 4-Step Algorithmic Pipeline</text>

  <!-- Step 1: Model & Domain -->
  <g transform="translate(60, 110)">
    <rect width="180" height="110" rx="10" fill="#111827" stroke="#38BDF8" stroke-width="2"/>
    <circle cx="20" cy="20" r="12" fill="#38BDF8"/>
    <text x="20" y="25" fill="#0B0F19" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">1</text>
    <text x="95" y="45" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">MODEL &amp; DOMAIN</text>
    <text x="90" y="70" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Express y = f(x)</text>
    <text x="90" y="88" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Define physical [a, b]</text>
  </g>
  <line x1="240" y1="165" x2="280" y2="165" stroke="#38BDF8" stroke-width="2.5" marker-end="url(#arrowCyan)"/>

  <!-- Step 2: Differentiate & Critical Points -->
  <g transform="translate(290, 110)">
    <rect width="180" height="110" rx="10" fill="#111827" stroke="#38BDF8" stroke-width="2"/>
    <circle cx="20" cy="20" r="12" fill="#38BDF8"/>
    <text x="20" y="25" fill="#0B0F19" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">2</text>
    <text x="95" y="45" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">CRITICAL POINTS</text>
    <text x="90" y="70" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Compute f'(x)</text>
    <text x="90" y="88" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="600" text-anchor="middle">Solve f'(c) = 0 or DNE</text>
  </g>
  <line x1="470" y1="165" x2="510" y2="165" stroke="#38BDF8" stroke-width="2.5" marker-end="url(#arrowCyan)"/>

  <!-- Step 3: Classification -->
  <g transform="translate(520, 110)">
    <rect width="180" height="110" rx="10" fill="#111827" stroke="#F59E0B" stroke-width="2"/>
    <circle cx="20" cy="20" r="12" fill="#F59E0B"/>
    <text x="20" y="25" fill="#0B0F19" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">3</text>
    <text x="95" y="45" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">CLASSIFY EXTREMA</text>
    <text x="90" y="70" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Option A: 1st Deriv Test</text>
    <text x="90" y="88" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Option B: 2nd Deriv Test</text>
  </g>
  <line x1="700" y1="165" x2="740" y2="165" stroke="#F59E0B" stroke-width="2.5" marker-end="url(#arrowAmber)"/>

  <!-- Step 4: Boundary & Verdict -->
  <g transform="translate(750, 110)">
    <rect width="160" height="110" rx="10" fill="#111827" stroke="#F43F5E" stroke-width="2"/>
    <circle cx="20" cy="20" r="12" fill="#F43F5E"/>
    <text x="20" y="25" fill="#0B0F19" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="800" text-anchor="middle">4</text>
    <text x="85" y="45" fill="#F8FAFC" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">BOUNDARIES</text>
    <text x="80" y="70" fill="#94A3B8" font-family="-apple-system, system-ui, sans-serif" font-size="12" text-anchor="middle">Test endpoints f(a), f(b)</text>
    <text x="80" y="88" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="12" font-weight="700" text-anchor="middle">Global Max/Min</text>
  </g>

  <!-- Bottom Decision Matrix Box -->
  <g transform="translate(60, 260)">
    <rect width="850" height="230" rx="12" fill="#111827" stroke="#334155" stroke-width="1.5"/>
    <text x="425" y="32" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="16" font-weight="700" text-anchor="middle">EXTREMA TEST SELECTION MATRIX</text>

    <!-- Sub-cards -->
    <g transform="translate(30, 50)">
      <rect width="370" height="150" rx="8" fill="#1E293B" stroke="#38BDF8" stroke-width="1"/>
      <text x="185" y="30" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">FIRST DERIVATIVE TEST (FDT)</text>
      <text x="20" y="60" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13">• Evaluates sign changes of f'(x) across critical values.</text>
      <text x="20" y="85" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13">• WORKS EVERYWHERE (even when f'(c) DNE!).</text>
      <text x="20" y="110" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13">• Detects corners, cusps, and stationary plateaus.</text>
      <text x="20" y="135" fill="#38BDF8" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600">✓ The Universal Tool for Engineers</text>
    </g>

    <g transform="translate(450, 50)">
      <rect width="370" height="150" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="1"/>
      <text x="185" y="30" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="15" font-weight="700" text-anchor="middle">SECOND DERIVATIVE TEST (SDT)</text>
      <text x="20" y="60" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13">• Evaluates single-point concavity f''(c).</text>
      <text x="20" y="85" fill="#CBD5E1" font-family="-apple-system, system-ui, sans-serif" font-size="13">• Extremely fast for simple polynomials.</text>
      <text x="20" y="110" fill="#F43F5E" font-family="-apple-system, system-ui, sans-serif" font-size="13">• FAILS completely if f''(c) = 0 or undefined.</text>
      <text x="20" y="135" fill="#F59E0B" font-family="-apple-system, system-ui, sans-serif" font-size="13" font-weight="600">⚡ Fast Shortcut, but fallback to FDT required</text>
    </g>
  </g>
</svg>
`;

fs.writeFileSync(path.join(svgDir, '01_hook_curve.svg'), hookSvg.trim());
fs.writeFileSync(path.join(svgDir, '04_local_vs_global.svg'), localVsGlobalSvg.trim());
fs.writeFileSync(path.join(svgDir, '05_slopes_and_intervals.svg'), slopesIntervalsSvg.trim());
fs.writeFileSync(path.join(svgDir, '06_tangent_to_stationary.svg'), tangentStationarySvg.trim());
fs.writeFileSync(path.join(svgDir, '07_cusp_and_corner_dne.svg'), cuspCornerSvg.trim());
fs.writeFileSync(path.join(svgDir, '08_stationary_inflection_cubic.svg'), stationaryInflectionSvg.trim());
fs.writeFileSync(path.join(svgDir, '09_first_derivative_sign_chart.svg'), signChartSvg.trim());
fs.writeFileSync(path.join(svgDir, '10_worked_example_cubic.svg'), workedExampleSvg.trim());
fs.writeFileSync(path.join(svgDir, '11_second_derivative_concavity.svg'), concavitySvg.trim());
fs.writeFileSync(path.join(svgDir, '12_closed_interval_endpoints.svg'), closedIntervalSvg.trim());
fs.writeFileSync(path.join(svgDir, '13_engineering_max_power.svg'), maxPowerSvg.trim());
fs.writeFileSync(path.join(svgDir, '14_optimization_flowchart.svg'), flowchartSvg.trim());

console.log('All 12 vector SVG assets generated successfully in assets/svg/');
