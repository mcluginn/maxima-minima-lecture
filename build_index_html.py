"""
build_index_html.py
Builds the definitive, seamless, Keynote-grade presentation player.
No video borders, no player chrome, smooth 0.4s cinematic crossfades,
automatic playback on slide arrival, and seamless Apple Pencil inking.
"""

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5, maximum-scale=5.0, user-scalable=yes">
  <title>Maxima & Minima — Motion-Based Engineering Calculus</title>
  <style>
    :root {
      --bg: #0B0F19;
      --card-bg: rgba(19, 27, 46, 0.7);
      --card-border: rgba(51, 65, 85, 0.5);
      --cyan: #38BDF8;
      --amber: #F59E0B;
      --coral: #F43F5E;
      --green: #22C55E;
      --text: #F8FAFC;
      --muted: #94A3B8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      background-color: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      min-height: 100vh;
      width: 100%;
      display: flex;
      flex-direction: column;
      user-select: none;
      -webkit-user-select: none;
      -webkit-touch-callout: none;
      touch-action: pan-x pan-y pinch-zoom;
      overscroll-behavior: none !important;
      -webkit-tap-highlight-color: transparent;
    }

    /* Minimalist Top Control Bar */
    header {
      height: 52px;
      background: rgba(11, 15, 25, 0.9);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid rgba(51, 65, 85, 0.4);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 100;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 13.5px;
      font-weight: 600;
      letter-spacing: 0.3px;
    }
    .badge {
      background: rgba(56, 189, 248, 0.12);
      color: var(--cyan);
      border: 1px solid rgba(56, 189, 248, 0.35);
      padding: 3px 8px;
      border-radius: 5px;
      font-size: 10.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .controls {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    button, select {
      background: rgba(19, 27, 46, 0.8);
      border: 1px solid var(--card-border);
      color: var(--text);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12.5px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      touch-action: manipulation;
    }
    button:hover, select:hover { background: #1E293B; border-color: var(--cyan); color: var(--cyan); }
    button.active { background: rgba(56, 189, 248, 0.25); border-color: var(--cyan); color: var(--cyan); font-weight: 600; }
    button.danger:hover { border-color: var(--coral); color: var(--coral); }
    select { outline: none; }

    /* Main Presentation Canvas (16:9 Widescreen) */
    .main-stage {
      flex: 1;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 12px;
      background: radial-gradient(circle at 50% 30%, rgba(19, 27, 46, 0.5) 0%, #0B0F19 80%);
      touch-action: pinch-zoom;
      overscroll-behavior: none;
      overflow: hidden;
    }
    .slide-container {
      width: 100%;
      max-width: 1360px;
      height: 100%;
      max-height: 765px;
      aspect-ratio: 16 / 9;
      background: var(--bg);
      border-radius: 12px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.85);
      border: 1px solid rgba(51, 65, 85, 0.3);
      touch-action: pinch-zoom;
      transform-origin: center center;
      transition: transform 0.12s ease-out;
    }
    .slide-container.drawing-locked * {
      user-select: none !important;
      -webkit-user-select: none !important;
    }

    /* Seamless Keynote-Style Slide Crossfade */
    .slide {
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.4s;
      padding: 32px 44px;
      display: flex;
      flex-direction: column;
      z-index: 1;
    }
    .slide.active {
      opacity: 1;
      visibility: visible;
      z-index: 2;
    }

    /* Slide Header */
    .slide-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
      border-bottom: 1px solid rgba(51, 65, 85, 0.3);
      padding-bottom: 12px;
    }
    .slide-top .meta {
      font-size: 11px;
      font-weight: 700;
      color: var(--cyan);
      text-transform: uppercase;
      letter-spacing: 1.2px;
      margin-bottom: 4px;
    }
    .slide-top h1 {
      font-size: 24px;
      font-weight: 700;
      color: var(--text);
      letter-spacing: -0.3px;
    }
    .slide-num {
      font-size: 13px;
      font-weight: 600;
      color: var(--muted);
      background: rgba(19, 27, 46, 0.6);
      padding: 4px 10px;
      border-radius: 6px;
      border: 1px solid var(--card-border);
    }

    /* Slide Content Layouts */
    .slide-body {
      flex: 1;
      display: grid;
      gap: 24px;
      height: calc(100% - 60px);
    }
    .grid-video {
      grid-template-columns: 2fr 1fr;
    }
    .grid-equal {
      grid-template-columns: 1fr 1fr;
    }
    .grid-full {
      grid-template-columns: 1fr;
    }

    /* Seamless Video Integration */
    .seamless-video-canvas {
      position: relative;
      width: 100%;
      height: 100%;
      background: #000;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid rgba(51, 65, 85, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }
    .seamless-video-canvas video {
      width: 100%;
      height: 100%;
      object-fit: contain;
      display: block;
      pointer-events: none;
    }
    .play-pause-indicator {
      position: absolute;
      bottom: 14px;
      right: 14px;
      background: rgba(11, 15, 25, 0.75);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(56, 189, 248, 0.4);
      color: var(--cyan);
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 600;
      opacity: 0.85;
      transition: opacity 0.2s;
    }
    .seamless-video-canvas:hover .play-pause-indicator {
      opacity: 1;
    }

    /* Information Cards */
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 24px;
      backdrop-filter: blur(12px);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }
    .card.cyan-border { border-color: rgba(56, 189, 248, 0.4); }
    .card.amber-border { border-color: rgba(245, 158, 11, 0.4); }
    .card.coral-border { border-color: rgba(244, 63, 94, 0.4); }
    .card.green-border { border-color: rgba(34, 197, 94, 0.4); }

    /* Inking Overlay Canvas (Apple Pencil Compatible) */
    #pencilCanvas {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      z-index: 60;
      pointer-events: none;
      touch-action: pinch-zoom;
    }
    #pencilCanvas.active {
      pointer-events: auto;
      cursor: crosshair;
    }

    /* Native-Grade Apple PencilKit Floating Palette (Replica of iPadOS PKToolPicker) */
    .pencilkit-toolbar {
      position: absolute;
      bottom: 22px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(255, 255, 255, 0.97);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      border-radius: 9999px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45), 0 0 0 1px rgba(0, 0, 0, 0.08);
      padding: 6px 16px;
      display: flex;
      align-items: center;
      gap: 8px;
      z-index: 100;
      touch-action: none !important;
      user-select: none;
      -webkit-user-select: none;
      transition: opacity 0.2s, transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .pencilkit-toolbar.hidden {
      display: none;
    }
    .pencilkit-handle {
      position: absolute;
      top: 3px;
      left: 50%;
      transform: translateX(-50%);
      width: 32px;
      height: 3.5px;
      background: #D1D5DB;
      border-radius: 2px;
      cursor: grab;
    }
    .pk-circle-btn {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #F1F5F9;
      border: 1px solid #E2E8F0;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: #475569;
      font-size: 14px;
      padding: 0;
      transition: all 0.15s;
    }
    .pk-circle-btn:hover {
      background: #E2E8F0;
      color: #0F172A;
    }
    .pk-circle-btn:disabled {
      opacity: 0.3;
      cursor: not-allowed;
      pointer-events: none;
    }
    .pk-divider {
      width: 1px;
      height: 22px;
      background: #E2E8F0;
      margin: 0 2px;
    }
    .pk-tool {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 38px;
      height: 48px;
      border-radius: 10px;
      cursor: pointer;
      border: 2px solid transparent;
      background: transparent;
      color: #475569;
      font-size: 18px;
      padding: 0;
      transition: all 0.15s ease;
      position: relative;
    }
    .pk-tool:hover {
      background: #F8FAFC;
    }
    .pk-tool.active {
      background: #EFF6FF;
      border-color: #3B82F6;
      color: #1D4ED8;
      transform: translateY(-4px);
      box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
    .pk-tool-sub {
      font-size: 8.5px;
      font-weight: 700;
      letter-spacing: 0.2px;
      color: inherit;
      margin-top: 1px;
      text-transform: uppercase;
    }
    .pk-size-wrap {
      position: relative;
      display: flex;
      align-items: center;
    }
    .pk-size-btn {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 3px 10px;
      background: #F1F5F9;
      border: 1px solid #E2E8F0;
      border-radius: 9999px;
      cursor: pointer;
      font-size: 11px;
      font-weight: 700;
      color: #334155;
      height: 32px;
      transition: all 0.15s;
    }
    .pk-size-btn:hover, .pk-size-btn.active {
      background: #E2E8F0;
      border-color: #CBD5E1;
      color: #0F172A;
    }
    .pk-size-dot-preview {
      display: inline-block;
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #007AFF;
      box-shadow: 0 0 0 1px rgba(0,0,0,0.15);
      transition: width 0.15s, height 0.15s, background-color 0.15s;
    }
    .pk-size-popover {
      position: absolute;
      bottom: calc(100% + 14px);
      left: 50%;
      transform: translateX(-50%);
      background: rgba(255, 255, 255, 0.98);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      border-radius: 18px;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.28), 0 0 0 1px rgba(0, 0, 0, 0.08);
      padding: 14px 16px;
      width: 230px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      z-index: 120;
      touch-action: auto !important;
      user-select: none;
      -webkit-user-select: none;
      animation: pkPopIn 0.16s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .pk-size-popover.hidden {
      display: none !important;
    }
    .pk-size-popover::after {
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      border-width: 7px;
      border-style: solid;
      border-color: rgba(255, 255, 255, 0.98) transparent transparent transparent;
    }
    @keyframes pkPopIn {
      from { opacity: 0; transform: translateX(-50%) translateY(6px) scale(0.96); }
      to { opacity: 1; transform: translateX(-50%) translateY(0) scale(1); }
    }
    .pk-size-presets {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #F8FAFC;
      border-radius: 12px;
      padding: 5px 8px;
      border: 1px solid #E2E8F0;
    }
    .pk-preset-circle {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: transparent;
      border: 2px solid transparent;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      padding: 0;
      transition: all 0.15s;
    }
    .pk-preset-circle span {
      display: block;
      border-radius: 50%;
      background: #64748B;
      transition: all 0.15s;
    }
    .pk-preset-circle:hover {
      background: #E2E8F0;
    }
    .pk-preset-circle.active {
      background: #EFF6FF;
      border-color: #3B82F6;
    }
    .pk-preset-circle.active span {
      background: #1D4ED8;
      transform: scale(1.15);
    }
    .pk-stroke-preview-box {
      height: 28px;
      background: #F1F5F9;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 10px;
    }
    .pk-swatch {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      cursor: pointer;
      border: 2px solid #FFFFFF;
      box-shadow: 0 0 0 1px rgba(0,0,0,0.2);
      transition: transform 0.15s, box-shadow 0.15s;
      position: relative;
    }
    .pk-swatch.active {
      transform: scale(1.25);
      box-shadow: 0 0 0 2px #0284C7, 0 3px 6px rgba(0,0,0,0.25);
    }
    .pk-badge-palm {
      display: flex;
      align-items: center;
      gap: 5px;
      padding: 5px 10px;
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-radius: 9999px;
      font-size: 11px;
      font-weight: 700;
      color: #166534;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }
    .pk-badge-palm.off {
      background: #FEF2F2;
      border-color: #FECACA;
      color: #991B1B;
    }
    .pk-color-picker-wrap {
      position: relative;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: conic-gradient(red, yellow, lime, aqua, blue, magenta, red);
      cursor: pointer;
      box-shadow: 0 0 0 1px rgba(0,0,0,0.2);
    }
    .pk-color-picker-wrap input[type="color"] {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      opacity: 0;
      cursor: pointer;
    }

    /* Bottom Control Strip */
    footer {
      height: 54px;
      background: rgba(11, 15, 25, 0.95);
      border-top: 1px solid rgba(51, 65, 85, 0.4);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 100;
    }
    .progress-bar {
      flex: 1;
      height: 4px;
      background: rgba(51, 65, 85, 0.4);
      border-radius: 2px;
      margin: 0 20px;
      overflow: hidden;
    }
    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--cyan), var(--amber));
      width: 4.5%;
      transition: width 0.3s ease;
    }

    /* Floating Teleprompter */
    .teleprompter {
      position: absolute;
      right: 24px;
      bottom: 70px;
      width: 360px;
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid rgba(56, 189, 248, 0.4);
      border-radius: 10px;
      padding: 16px;
      z-index: 90;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
      display: none;
      backdrop-filter: blur(16px);
    }
    .teleprompter h4 {
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--cyan);
      margin-bottom: 8px;
    }
    .teleprompter div {
      font-size: 13px;
      line-height: 1.5;
      color: #cbd5e1;
    }
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <span class="badge">Calculus</span>
      <span>Maxima & Minima // Motion-Based Lecture</span>
    </div>

    <div class="controls">
      <select id="sceneNav" title="Jump to Slide">
        <option value="0">01. 🚀 Title & Overview</option>
        <option value="1">02. 🧭 Lecture Trajectory</option>
        <option value="2">03. 🏔️ Terrain Exploration Hook</option>
        <option value="3">04. 📍 Local vs. Absolute Extrema</option>
        <option value="4">05. 📈 The Cubic Landscape f(x)=x³-3x</option>
        <option value="5">06. 📐 Dynamic Tangent Telemetry</option>
        <option value="6">07. ⚠️ Singularities (Corners & Cusps)</option>
        <option value="7">08. 🛑 The Critical Trap: Inflection Terraces</option>
        <option value="8">09. ⚡ Algebraic Factoring Morph</option>
        <option value="9">10. 📊 First Derivative Sign Chart</option>
        <option value="10">11. 🎯 Exact Coordinate Verification</option>
        <option value="11">12. 🔄 Second Derivative Concavity</option>
        <option value="12">13. ⚖️ 1st vs 2nd Test Comparison Matrix</option>
        <option value="13">14. 📦 Closed Interval EVT</option>
        <option value="14">15. 🔌 Circuit Maximum Power Transfer</option>
        <option value="15">16. 🔢 Optimization 1: Number Exceeding Square</option>
        <option value="16">17. 🌊 Optimization 2: Riverbank Fencing</option>
        <option value="17">18. 📦 Optimization 3: Open-Top Box Volume</option>
        <option value="18">19. 🚌 Optimization 4: Tour Bus Revenue</option>
        <option value="19">20. 📐 Optimization 5: Trapezoidal Gutter</option>
        <option value="20">21. 🎯 Active Challenge & Exit Ticket</option>
        <option value="21">22. 📚 References & Acknowledgements</option>
      </select>

      <div style="display: flex; align-items: center; gap: 6px;">
        <button id="drawBtn" title="Toggle Apple Pencil Inking">✍️ Apple Pencil</button>
      </div>

      <!-- Quick Slide Zoom Controls -->
      <div style="display: flex; align-items: center; gap: 4px; background: rgba(19, 27, 46, 0.85); border: 1px solid var(--card-border); border-radius: 6px; padding: 2px 6px;">
        <button id="zoomOutBtn" title="Zoom Out Slide" style="padding: 3px 8px; font-size: 13px; border: none; background: transparent; cursor: pointer;">🔍−</button>
        <button id="zoomResetBtn" title="Reset Zoom to 100%" style="padding: 3px 6px; font-size: 11px; font-weight: 700; border: none; background: transparent; color: var(--cyan); cursor: pointer;"><span id="zoomDisplay">100%</span></button>
        <button id="zoomInBtn" title="Zoom In Slide" style="padding: 3px 8px; font-size: 13px; border: none; background: transparent; cursor: pointer;">+</button>
      </div>

      <a href="maxima_minima_lecture.pptx" download style="text-decoration:none;">
        <button style="background: rgba(34, 197, 94, 0.15); border-color: rgba(34, 197, 94, 0.4); color: var(--green);" title="Download Keynote/PowerPoint Deck">📥 Keynote (.pptx)</button>
      </a>

      <button id="notesBtn" title="Toggle Lecturer Teleprompter">📋 Notes</button>
      <button id="fsBtn" title="Fullscreen Presentation">⛶ Fullscreen</button>
    </div>
  </header>

  <div class="main-stage">
    <div class="slide-container" id="stageContainer">
      <canvas id="pencilCanvas"></canvas>

      <!-- Floating Apple PencilKit Toolbar (Exact Replica of iPadOS PKToolPicker) -->
      <div id="pencilKitToolbar" class="pencilkit-toolbar hidden">
        <div class="pencilkit-handle" title="Drag to reposition toolbar"></div>
        <button class="pk-circle-btn" id="pkUndoBtn" title="Undo (Apple Pencil)" disabled>↺</button>
        <button class="pk-circle-btn" id="pkRedoBtn" title="Redo (Apple Pencil)" disabled>↻</button>
        <div class="pk-divider"></div>
        <button class="pk-tool active" id="toolPen" title="Fine Monoline Pen">
          <span>✒️</span>
          <span class="pk-tool-sub">Pen</span>
        </button>
        <button class="pk-tool" id="toolPencil" title="Graphite Pencil">
          <span>✏️</span>
          <span class="pk-tool-sub">Pencil</span>
        </button>
        <button class="pk-tool" id="toolHighlighter" title="Translucent Highlighter">
          <span>🖍️</span>
          <span class="pk-tool-sub">Marker</span>
        </button>
        <button class="pk-tool" id="toolEraser" title="Stroke Eraser">
          <span>🧽</span>
          <span class="pk-tool-sub">Eraser</span>
        </button>
        <button class="pk-circle-btn danger" id="pkClearBtn" title="Clear Slide Ink" style="width:28px;height:28px;font-size:12px;margin-left:2px;">🗑️</button>
        <div class="pk-divider"></div>

        <!-- Stroke Size Selector & Popover -->
        <div class="pk-size-wrap">
          <button class="pk-size-btn" id="pkSizeBtn" title="Pen Stroke Thickness (Tap to adjust size)">
            <span class="pk-size-dot-preview" id="pkSizeDotPreview"></span>
            <span class="pk-size-label" id="pkSizeLabel">3.0 px</span>
          </button>
          <div class="pk-size-popover hidden" id="pkSizePopover">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:11px; font-weight:700; color:#475569; text-transform:uppercase; letter-spacing:0.5px;">Stroke Size</span>
              <span id="pkSizeValueDisplay" style="font-size:12px; font-weight:800; color:#007AFF;">3.0 px</span>
            </div>
            <div class="pk-size-presets">
              <button class="pk-preset-circle" data-size="1.5" title="Hairline (1.5px)"><span style="width:4px; height:4px;"></span></button>
              <button class="pk-preset-circle active" data-size="3" title="Standard (3px)"><span style="width:7px; height:7px;"></span></button>
              <button class="pk-preset-circle" data-size="5" title="Medium (5px)"><span style="width:11px; height:11px;"></span></button>
              <button class="pk-preset-circle" data-size="8" title="Thick (8px)"><span style="width:15px; height:15px;"></span></button>
              <button class="pk-preset-circle" data-size="14" title="Marker (14px)"><span style="width:20px; height:20px;"></span></button>
            </div>
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:10px; color:#64748B; font-weight:700;">1</span>
              <input type="range" id="pkSizeSlider" min="1" max="25" step="0.5" value="3" style="flex:1; accent-color:#007AFF; cursor:pointer;">
              <span style="font-size:10px; color:#64748B; font-weight:700;">25</span>
            </div>
            <div class="pk-stroke-preview-box">
              <div id="pkStrokePreviewLine" style="height:3px; background:#007AFF; border-radius:9999px; width:80%; transition:height 0.1s, background-color 0.15s;"></div>
            </div>
          </div>
        </div>

        <div class="pk-divider"></div>
        <div class="pk-swatch" style="background:#0F172A;" data-color="#0F172A" title="Ink Black"></div>
        <div class="pk-swatch active" style="background:#007AFF;" data-color="#007AFF" title="Apple Blue"></div>
        <div class="pk-swatch" style="background:#34C759;" data-color="#34C759" title="Apple Green"></div>
        <div class="pk-swatch" style="background:#FF9500;" data-color="#FF9500" title="Apple Amber"></div>
        <div class="pk-swatch" style="background:#FF3B30;" data-color="#FF3B30" title="Apple Red"></div>
        <div class="pk-swatch" style="background:#FFFFFF; box-shadow:0 0 0 1px #CBD5E1;" data-color="#FFFFFF" title="Chalk White"></div>
        <div class="pk-color-picker-wrap" title="Custom Color Palette">
          <input type="color" id="pkCustomColor" value="#38BDF8">
        </div>
        <div class="pk-divider"></div>
        <div class="pk-badge-palm" id="pkPalmBadge" title="Tap to toggle: Strict Apple Pencil (Palm Rejected) vs Touch Inking">
          <span> Palm Rejection: ON</span>
        </div>
        <button class="pk-circle-btn" id="pkZoomResetBtn" title="Reset Zoom to 100%" style="width:28px;height:28px;font-size:10px;font-weight:700;">100%</button>
        <button class="pk-circle-btn" id="pkCloseBtn" title="Close Pencil Toolbar" style="width:26px;height:26px;font-size:11px;">✕</button>
      </div>

      <!-- SLIDE 1: Title -->
      <div class="slide active" data-title="Title Slide">
        <div class="slide-top">
          <div class="meta">Differential Calculus for Engineering</div>
          <div class="slide-num">Slide 01 / 22</div>
        </div>
        <div class="slide-body grid-full">
          <div class="card cyan-border" style="justify-content: center; align-items: center; text-align: center; padding: 40px;">
            <div style="font-size: 13px; font-weight: 700; color: var(--cyan); letter-spacing: 2px; margin-bottom: 12px;">CALCULUS IN MOTION</div>
            <h1 style="font-size: 40px; color: #fff; line-height: 1.2; margin-bottom: 14px;">Maxima & Minima</h1>
            <h3 style="font-size: 20px; color: var(--amber); margin-bottom: 24px; font-weight: 500;">Kinematic Visual Storytelling & Engineering Optimization</h3>
            <p style="max-width: 720px; color: var(--muted); font-size: 15px; line-height: 1.6;">
              Experience differential calculus through continuous vector animations.
              Watch equations physically morph, tangent vectors rotate in real time, and concavity bowls verify extrema.
            </p>
            <div style="margin-top: 32px; display: flex; gap: 14px; flex-wrap: wrap; justify-content: center;">
              <button onclick="showSlide(2)" style="background: rgba(56, 189, 248, 0.25); border-color: var(--cyan); color: var(--cyan); font-weight: 700; padding: 10px 22px; font-size: 14px;">
                🚀 Begin Lecture: Terrain Hook ➔
              </button>
              <button onclick="showSlide(8)" style="background: rgba(245, 158, 11, 0.2); border-color: var(--amber); color: var(--amber); font-weight: 700; padding: 10px 22px; font-size: 14px;">
                ⚡ Algebraic Morphing (Slide 09) ➔
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 2: Roadmap -->
      <div class="slide" data-title="Lecture Trajectory">
        <div class="slide-top">
          <div><div class="meta">Pedagogical Arc</div><h1>Lecture Trajectory: From Kinetic Intuition to Optimization</h1></div>
          <div class="slide-num">Slide 02 / 22</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="card cyan-border">
            <h2 style="color: var(--cyan); font-size: 17px; margin-bottom: 8px;">01. Visual Motion & Critical Points</h2>
            <p style="color: var(--muted); font-size: 13.5px; line-height: 1.5; margin-bottom: 14px;">
              Terrain exploration hook, moving tangent vectors, instantaneous slope freezing m = 0, and singularities (corners & cusps).
            </p>
            <h2 style="color: var(--amber); font-size: 17px; margin-bottom: 8px;">02. First Derivative Test & Sign Charts</h2>
            <p style="color: var(--muted); font-size: 13.5px; line-height: 1.5;">
              Factoring transformations, number line interval sampling, and direction transitions across critical thresholds.
            </p>
          </div>
          <div class="card coral-border">
            <h2 style="color: var(--coral); font-size: 17px; margin-bottom: 8px;">03. Second Derivative & Concavity</h2>
            <p style="color: var(--muted); font-size: 13.5px; line-height: 1.5; margin-bottom: 14px;">
              Curvature rate f''(x), concavity bowls (cap vs. cup), and the stationary inflection terrace counterexample g(x) = x³.
            </p>
            <h2 style="color: var(--green); font-size: 17px; margin-bottom: 8px;">04. Applied Engineering Optimization</h2>
            <p style="color: var(--muted); font-size: 13.5px; line-height: 1.5;">
              Extreme Value Theorem, geometric fencing, container volume, revenue maximization, and hydraulic gutter design.
            </p>
          </div>
        </div>
      </div>

      <!-- SLIDE 3: Hook Hill Video -->
      <div class="slide" data-title="Terrain Exploration Hook" data-notes="Play video clip. Ask students: As the exploration probe traverses this mountain range, what exact instantaneous property characterizes the true summits and lowest valleys?">
        <div class="slide-top">
          <div><div class="meta">Phase 1 // Visual Motion</div><h1>Terrain Exploration: Peaks & Valleys</h1></div>
          <div class="slide-num">Slide 03 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/Scene01_HookHill_frame.png">
              <source src="media/videos/clips/Scene01_HookHill.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">PEDAGOGICAL HOOK</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Where do true summits occur?</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              Notice the moving elevation probe. On the ascent, slope is positive. On the descent, slope is negative.
              At the exact apex, vertical motion freezes.
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px; text-transform: uppercase;">Central Question</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Does every horizontal point form a peak or valley?</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 4: Local vs Absolute Video -->
      <div class="slide" data-title="Local vs Absolute Extrema">
        <div class="slide-top">
          <div><div class="meta">Topological Definitions // Extrema</div><h1>Local vs. Absolute Extrema</h1></div>
          <div class="slide-num">Slide 04 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/Scene02_LocalVsAbsolute_frame.png">
              <source src="media/videos/clips/Scene02_LocalVsAbsolute.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card coral-border">
            <h3 style="color: var(--coral); margin-bottom: 8px;">NEIGHBORHOOD CRITERIA</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Open Ball vs. Global Domain</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Local:</strong> Winning against immediate neighbors in (c - δ, c + δ).<br>
              • <strong>Absolute:</strong> The highest value across the entire domain D.
            </p>
            <div style="background: rgba(244, 63, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(244, 63, 94, 0.3);">
              <div style="color: var(--coral); font-weight: 700; font-size: 11px; text-transform: uppercase;">Crucial Exam Fact</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Interval endpoints cannot be local extrema under standard calculus conventions.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 5: The Cubic Landscape -->
      <div class="slide" data-title="The Cubic Landscape">
        <div class="slide-top">
          <div><div class="meta">Worked Model // Trajectory</div><h1>The Cubic Landscape: f(x) = x³ - 3x</h1></div>
          <div class="slide-num">Slide 05 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene1_TheFunction_frame.png">
              <source src="media/videos/clips/SignatureScene1_TheFunction.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">CURVE GEOMETRY</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Symmetry & Exploration</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              As the moving tracer traverses x ∈ [-2.2, 2.2], notice how the curve reaches a local peak, dives through the origin, and bottoms out.
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">ODD SYMMETRY</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">f(-x) = -f(x): local peak at (-1, 2) is mirrored by trough at (1, -2).</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 6: Dynamic Tangent Telemetry -->
      <div class="slide" data-title="Dynamic Tangent Telemetry">
        <div class="slide-top">
          <div><div class="meta">Instantaneous Velocity // Rotating Tangent</div><h1>Dynamic Tangent Telemetry & Derivative f'(x)</h1></div>
          <div class="slide-num">Slide 06 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene2_TheTangent_frame.png">
              <source src="media/videos/clips/SignatureScene2_TheTangent.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">TANGENT ROTATION</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Instantaneous Slope: m = 3x² - 3</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Ascending:</strong> m &gt; 0 (Cyan)<br>
              • <strong>Crest (x = -1):</strong> m = 0 (Amber Level)<br>
              • <strong>Descending:</strong> m &lt; 0 (Coral)<br>
              • <strong>Trough (x = +1):</strong> m = 0 (Amber Level)
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">DERIVATIVE ZERO CONDITION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Horizontal tangent line f'(c) = 0 signals candidate turning point.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 7: Singularities DNE -->
      <div class="slide" data-title="Singularities (Corners & Cusps)">
        <div class="slide-top">
          <div><div class="meta">Non-Differentiable Extrema // Boundary Conditions</div><h1>Singularities: When Derivatives Fail to Exist</h1></div>
          <div class="slide-num">Slide 07 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/Scene03_SingularitiesDNE_frame.png">
              <source src="media/videos/clips/Scene03_SingularitiesDNE.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card coral-border">
            <h3 style="color: var(--coral); margin-bottom: 8px;">SHARP TURNING POINTS</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">f'(c) Does Not Exist</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>f(x) = |x|:</strong> Corner at x = 0. Left slope = -1, right slope = +1. Valid global minimum!<br><br>
              • <strong>g(x) = x^(2/3):</strong> Cusp at x = 0. Slopes approach ±∞. Valid global minimum!
            </p>
            <div style="background: rgba(244, 63, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(244, 63, 94, 0.3);">
              <div style="color: var(--coral); font-weight: 700; font-size: 11px;">FORMAL DEFINITION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Critical number: f'(c) = 0 OR f'(c) DNE (with c in domain).</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 8: The Critical Point Trap -->
      <div class="slide" data-title="The Critical Point Trap">
        <div class="slide-top">
          <div><div class="meta">Necessary vs. Sufficient // Counterexample</div><h1>The Critical Trap: f'(c) = 0 Without Extrema</h1></div>
          <div class="slide-num">Slide 08 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene7_Counterexample_frame.png">
              <source src="media/videos/clips/SignatureScene7_Counterexample.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">STATIONARY INFLECTION</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">g(x) = x³ &nbsp;at&nbsp; x = 0</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • g'(x) = 3x² ⟹ g'(0) = 0 (Tangent is horizontal).<br>
              • Slope is positive for x &lt; 0 AND positive for x &gt; 0.<br>
              • No sign reversal occurs: <strong>NO EXTREMUM</strong>.
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">LOGICAL IMPLICATION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">f'(c) = 0 is a NECESSARY condition for smooth extrema, NOT a SUFFICIENT one!</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 9: Algebraic Factoring Morph -->
      <div class="slide" data-title="Algebraic Factoring Morph">
        <div class="slide-top">
          <div><div class="meta">Equation Transformation // Symbolic Morph</div><h1>Algebraic Factoring: Zeroes of the Derivative</h1></div>
          <div class="slide-num">Slide 09 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene3_EquationMorph_frame.png">
              <source src="media/videos/clips/SignatureScene3_EquationMorph.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">FACTORIZATION</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Isolating Critical Numbers</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Step 1:</strong> f'(x) = 3x² - 3<br>
              • <strong>Step 2:</strong> Factor common 3: 3(x² - 1)<br>
              • <strong>Step 3:</strong> Difference of squares: 3(x - 1)(x + 1) = 0<br>
              • <strong>Roots:</strong> <strong>x = -1</strong> and <strong>x = +1</strong>
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">PROJECTION TO GEOMETRY</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Roots partition the real line into three distinct sign domains.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 10: First Derivative Sign Chart -->
      <div class="slide" data-title="First Derivative Sign Chart">
        <div class="slide-top">
          <div><div class="meta">First Derivative Test // Sign Chart</div><h1>First Derivative Test: Dynamic Sign Partitioning</h1></div>
          <div class="slide-num">Slide 10 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene4_DerivativeTest_frame.png">
              <source src="media/videos/clips/SignatureScene4_DerivativeTest.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">INTERVAL SAMPLING</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Tracking Sign Transitions</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>x &lt; -1:</strong> f'(-2) = +9 &gt; 0 ⟹ <strong>Increasing ↗</strong><br>
              • <strong>-1 &lt; x &lt; 1:</strong> f'(0) = -3 &lt; 0 ⟹ <strong>Decreasing ↘</strong><br>
              • <strong>x &gt; 1:</strong> f'(2) = +9 &gt; 0 ⟹ <strong>Increasing ↗</strong><br><br>
              <strong>Transitions:</strong><br>
              (+) to (-) at x = -1 ⟹ <strong>Local Maximum</strong><br>
              (-) to (+) at x = +1 ⟹ <strong>Local Minimum</strong>
            </p>
          </div>
        </div>
      </div>

      <!-- SLIDE 11: Exact Coordinate Verification -->
      <div class="slide" data-title="Exact Coordinate Verification">
        <div class="slide-top">
          <div><div class="meta">Extrema Coordinates // Function Evaluation</div><h1>Coordinate Verification: Exact Extrema</h1></div>
          <div class="slide-num">Slide 11 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene5_ExtremaReveal_frame.png">
              <source src="media/videos/clips/SignatureScene5_ExtremaReveal.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">COORDINATE VERIFICATION</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Evaluating the Original Function</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>f(-1)</strong> = (-1)³ - 3(-1) = -1 + 3 = <strong>+2</strong><br>
              ⟹ Local Maximum: <strong>(-1, 2)</strong><br><br>
              • <strong>f(1)</strong> = (1)³ - 3(1) = 1 - 3 = <strong>-2</strong><br>
              ⟹ Local Minimum: <strong>(1, -2)</strong>
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">CRUCIAL REMINDER</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">f' gives the location; f gives the height!</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 12: Second Derivative Concavity -->
      <div class="slide" data-title="Second Derivative & Concavity">
        <div class="slide-top">
          <div><div class="meta">Second Derivative // Curvature Bending</div><h1>Second Derivative Test & Concavity Bending</h1></div>
          <div class="slide-num">Slide 12 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene6_SecondDerivative_frame.png">
              <source src="media/videos/clips/SignatureScene6_SecondDerivative.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">CURVATURE RATE</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">f''(x) = 6x</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>x = -1:</strong> f''(-1) = -6 &lt; 0 (Concave Down ∩)<br>
              Slopes are decreasing ⟹ Traps a <strong>LOCAL MAX</strong>.<br><br>
              • <strong>x = 1:</strong> f''(1) = +6 &gt; 0 (Concave Up ∪)<br>
              Slopes are increasing ⟹ Holds a <strong>LOCAL MIN</strong>.
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">INFLECTION TRANSITION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">At x = 0, f''(0) = 0: concavity flips from ∩ to ∪!</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 13: Test Comparison Matrix -->
      <div class="slide" data-title="1st vs 2nd Test Comparison">
        <div class="slide-top">
          <div><div class="meta">Comparative Analysis // Decision Logic</div><h1>Extrema Decision Matrix: 1st vs. 2nd Test</h1></div>
          <div class="slide-num">Slide 13 / 22</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="card cyan-border">
            <h2 style="color: var(--cyan); font-size: 18px; margin-bottom: 14px;">FIRST DERIVATIVE TEST</h2>
            <div style="font-size: 13px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Scope:</strong> Universal. Handles smooth turning points AND sharp singularities (corners/cusps).</p>
              <p style="margin-top: 8px;"><strong style="color: #fff;">Mechanism:</strong> Tracks sign flip of f'(x) across x = c.</p>
              <p style="margin-top: 8px;"><strong style="color: #fff;">Outcomes:</strong></p>
              <ul style="padding-left: 20px; color: var(--text);">
                <li>(+) to (-) ⟹ Local Maximum</li>
                <li>(-) to (+) ⟹ Local Minimum</li>
                <li>No change ⟹ Neither (Inflection Terrace)</li>
              </ul>
              <p style="margin-top: 12px; color: var(--cyan); font-weight: 600;">Verdict: 100% dependable; always available.</p>
            </div>
          </div>
          <div class="card amber-border">
            <h2 style="color: var(--amber); font-size: 18px; margin-bottom: 14px;">SECOND DERIVATIVE TEST</h2>
            <div style="font-size: 13px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Scope:</strong> Restricted. Requires f'(c) = 0 and f''(c) to exist.</p>
              <p style="margin-top: 8px;"><strong style="color: #fff;">Mechanism:</strong> Computes instantaneous curvature f''(c) at a single point.</p>
              <p style="margin-top: 8px;"><strong style="color: #fff;">Outcomes:</strong></p>
              <ul style="padding-left: 20px; color: var(--text);">
                <li>f''(c) &lt; 0 ⟹ Concave Down ⟹ Local Max</li>
                <li>f''(c) &gt; 0 ⟹ Concave Up ⟹ Local Min</li>
                <li>f''(c) = 0 ⟹ <span style="color: var(--coral); font-weight: 700;">INCONCLUSIVE!</span></li>
              </ul>
              <p style="margin-top: 12px; color: var(--amber); font-weight: 600;">Verdict: Fast when derivatives are simple; fragile.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 14: Closed Interval EVT -->
      <div class="slide" data-title="Closed Interval EVT">
        <div class="slide-top">
          <div><div class="meta">Optimization Theory // Closed Domain</div><h1>Closed Interval Method & Candidate Matrix</h1></div>
          <div class="slide-num">Slide 14 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/Scene04_ClosedIntervalMethod_frame.png">
              <source src="media/videos/clips/Scene04_ClosedIntervalMethod.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">CANDIDATE EVALUATION</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Domain: [-0.5, 2.5]</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • Left Endpoint: f(-0.5) = 1.375<br>
              • Interior Critical: f(1.0) = -2.000 ⟹ <strong>ABS MIN</strong><br>
              • Right Endpoint: f(2.5) = <strong>8.125</strong> ⟹ <strong>ABS MAX</strong>
            </p>
            <div style="background: rgba(34, 197, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(34, 197, 94, 0.3);">
              <div style="color: var(--green); font-weight: 700; font-size: 11px;">KEY TAKEAWAY</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">x = -1 is discarded because -1 ∉ [-0.5, 2.5]!</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 15: Maximum Power Transfer -->
      <div class="slide" data-title="Engineering: Maximum Power Transfer">
        <div class="slide-top">
          <div><div class="meta">Engineering Application // Circuits</div><h1>Maximum Power Transfer Theorem</h1></div>
          <div class="slide-num">Slide 15 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/Scene05_MaxPowerTransfer_frame.png">
              <source src="media/videos/clips/Scene05_MaxPowerTransfer.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">CIRCUIT OPTIMIZATION</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">P(R_L) = V_th² * R_L / (R_th + R_L)²</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              Applying the Quotient Rule to dP/dR_L = 0 yields:<br>
              (R_th + R_L)² - 2*R_L*(R_th + R_L) = 0<br>
              ⟹ <strong>R_Load = R_Source</strong>
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">IMPEDANCE MATCHING</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Delivers peak power efficiency across antennas, audio amplifiers, and sensors.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 16: Optimization 1 Number Exceeding Square -->
      <div class="slide" data-title="Optimization 1: Number Exceeding Square">
        <div class="slide-top">
          <div><div class="meta">Applied Optimization // Modeling</div><h1>Optimization 1: Number Exceeding its Square</h1></div>
          <div class="slide-num">Slide 16 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem1_NumberOptimization_frame.png">
              <source src="media/videos/clips/MathalinoProblem1_NumberOptimization.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">PROBLEM ANALYSIS</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">What number exceeds its square by maximum amount?</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Objective:</strong> f(x) = x - x²<br>
              • <strong>Derivative:</strong> f'(x) = 1 - 2x = 0 ⟹ <strong>x = 1/2</strong><br>
              • <strong>Concavity:</strong> f''(x) = -2 &lt; 0 ⟹ <strong>Strict Maximum</strong><br>
              • <strong>Max Excess:</strong> f(1/2) = 1/2 - 1/4 = <strong>1/4</strong> (0.25)
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">MODELING WORKFLOW</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Translating natural language into an analytical objective function.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 17: Optimization 2 Riverbank Fencing -->
      <div class="slide" data-title="Optimization 2: Riverbank Fencing">
        <div class="slide-top">
          <div><div class="meta">Applied Optimization // Geometric Constraints</div><h1>Optimization 2: Riverbank Fencing Design</h1></div>
          <div class="slide-num">Slide 17 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem2_RiverbankLot_frame.png">
              <source src="media/videos/clips/MathalinoProblem2_RiverbankLot.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">GEOMETRIC CONSTRAINT</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Least fencing for fixed area along a river</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Constraint:</strong> Area A = xy ⟹ x = A / y<br>
              • <strong>Fence Perimeter:</strong> P = x + 2y = A/y + 2y<br>
              • <strong>Differentiation:</strong> dP/dy = -A/y² + 2 = 0 ⟹ 2y² = A<br>
              • <strong>Optimal Proportions:</strong> 2y² = xy ⟹ <strong>y = ½x</strong> (Width = ½ Length)
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">NATURAL BOUNDARY REDUCTION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">With 1 natural boundary (river), the optimal rectangular ratio shifts from 1:1 to 2:1.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 18: Optimization 3 Open-Top Box -->
      <div class="slide" data-title="Optimization 3: Open-Top Box Volume">
        <div class="slide-top">
          <div><div class="meta">Applied Optimization // Domain Feasibility</div><h1>Optimization 3: Open-Top Box Volume Maximization</h1></div>
          <div class="slide-num">Slide 18 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem3_OpenTopBox_frame.png">
              <source src="media/videos/clips/MathalinoProblem3_OpenTopBox.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">CONTAINER DESIGN</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Cardboard 15" × 24": Maximize Folded Volume</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Volume:</strong> V(x) = 4x³ - 78x² + 360x<br>
              • <strong>Criticals:</strong> 12(x - 3)(x - 10) = 0 ⟹ x = 3, 10<br>
              • <strong>Domain Feasibility:</strong> 0 &lt; x &lt; 7.5'' ⟹ <span style="color: var(--coral); font-weight: 700;">Discard x = 10''</span><br>
              • <strong>Max Volume:</strong> V(3) = 18 × 9 × 3 = <strong>486 in³</strong>
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">PHYSICAL DOMAIN CHECK</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">x = 10 produces negative width 15 - 20 = -5'', showing why domain check is critical.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 19: Optimization 4 Tour Bus Revenue -->
      <div class="slide" data-title="Optimization 4: Tour Bus Revenue">
        <div class="slide-top">
          <div><div class="meta">Applied Optimization // Revenue Economics</div><h1>Optimization 4: Tour Bus Yield Management & Revenue</h1></div>
          <div class="slide-num">Slide 19 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem4_TourBusRevenue_frame.png">
              <source src="media/videos/clips/MathalinoProblem4_TourBusRevenue.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">PRICE ELASTICITY</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">80-Seat Tour Bus: Balancing Fare vs. Demand</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Price per Seat:</strong> p(x) = 350 + 12.5x<br>
              • <strong>Seats Sold:</strong> q(x) = 80 - 2x<br>
              • <strong>Revenue Function:</strong> R(x) = 28,000 + 300x - 25x²<br>
              • <strong>Calculus Solution:</strong> dR/dx = 300 - 50x = 0 ⟹ <strong>x = 6</strong><br>
              • <strong>Optimal Metrics:</strong> Fare = <strong>P425/seat</strong>, <strong>68 seats</strong> ⟹ <strong>P28,900</strong>
            </p>
            <div style="background: rgba(34, 197, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(34, 197, 94, 0.3);">
              <div style="color: var(--green); font-weight: 700; font-size: 11px;">REVENUE MAXIMIZATION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Balancing unit price increases against volume loss.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 20: Optimization 5 Trapezoidal Gutter -->
      <div class="slide" data-title="Optimization 5: Trapezoidal Gutter">
        <div class="slide-top">
          <div><div class="meta">Applied Optimization // Hydraulic Engineering</div><h1>Optimization 5: Trapezoidal Gutter Hydraulic Capacity</h1></div>
          <div class="slide-num">Slide 20 / 22</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem5_TrapezoidalGutter_frame.png">
              <source src="media/videos/clips/MathalinoProblem5_TrapezoidalGutter.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card coral-border">
            <h3 style="color: var(--coral); margin-bottom: 8px;">HYDRAULIC GEOMETRY</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">14" Tin Strip at 45°: Maximize Cross-Section Area</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Strip Width:</strong> a + 2s = 14 ⟹ s = (14 - a)/2<br>
              • <strong>Gutter Depth:</strong> h = s sin 45° = (14 - a) / (2√2)<br>
              • <strong>Area:</strong> A(a) = ah + h² = (14a - a²)/(2√2) + (14 - a)²/8<br>
              • <strong>Derivative:</strong> dA/da = (7 - a)/√2 + (a - 14)/4 = 0<br>
              • <strong>Optimal Base:</strong> a = 14(√2 - 1)/(2√2 - 1) ≈ <strong>3.17 inches</strong> (slants s ≈ 5.41")
            </p>
            <div style="background: rgba(244, 63, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(244, 63, 94, 0.3);">
              <div style="color: var(--coral); font-weight: 700; font-size: 11px;">CIVIL & MECHANICAL FLOW</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Closed-form radical solution for peak open-channel fluid flow.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 21: Practice Challenge & Exit Ticket -->
      <div class="slide" data-title="Practice Problem & Exit Ticket">
        <div class="slide-top">
          <div><div class="meta">Active Learning // Exit Challenge</div><h1>Practice Challenge & Verification Key</h1></div>
          <div class="slide-num">Slide 21 / 22</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">ENGINEERING CHALLENGE</h3>
            <p style="color: #fff; font-size: 14px; margin-bottom: 12px;">Analyze the structural displacement curve:</p>
            <div style="background: #0B0F19; padding: 10px; border-radius: 6px; border: 1px solid var(--card-border); color: var(--cyan); font-weight: 700; font-size: 15px; margin-bottom: 16px;">
              f(x) = 2x³ - 3x² - 12x + 5 &nbsp; on &nbsp; [-2, 4]
            </div>
            <ol style="color: var(--muted); font-size: 13px; line-height: 1.6; padding-left: 20px;">
              <li>Find f'(x) and factor completely.</li>
              <li>Find all critical numbers within [-2, 4].</li>
              <li>Use 2nd Derivative Test to classify local extrema.</li>
              <li>Evaluate the EVT candidate table.</li>
              <li>Determine the Global Extrema coordinates.</li>
            </ol>
          </div>
          <div class="card cyan-border" style="background: #0F172A;">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">STEP-BY-STEP SOLUTION KEY</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: var(--amber);">1. Derivative:</strong> f'(x) = 6x² - 6x - 12 = 6(x - 2)(x + 1)</p>
              <p><strong style="color: var(--amber);">2. Criticals:</strong> x = -1 & x = 2 (both in domain)</p>
              <p><strong style="color: var(--amber);">3. Concavity:</strong> f''(x) = 12x - 6<br>
                • f''(-1) = -18 &lt; 0 ⟹ Local Max at (-1, 12)<br>
                • f''(2) = +18 &gt; 0 ⟹ Local Min at (2, -15)
              </p>
              <p><strong style="color: var(--amber);">4. Candidate Table:</strong><br>
                f(-2) = 1 &nbsp;|&nbsp; f(-1) = 12 &nbsp;|&nbsp; f(2) = -15 &nbsp;|&nbsp; f(4) = 37
              </p>
              <p style="margin-top: 8px; color: #fff; font-weight: 700;">
                🏆 Global Max: <span style="color: var(--green);">(4, 37)</span> [Endpoint]<br>
                📉 Global Min: <span style="color: var(--coral);">(2, -15)</span> [Interior Critical]
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 22: References & Academic Acknowledgements -->
      <div class="slide" data-title="References & Acknowledgements">
        <div class="slide-top">
          <div><div class="meta">Curriculum Bibliography // Academic Citations</div><h1>Curriculum References & Academic Acknowledgements</h1></div>
          <div class="slide-num">Slide 22 / 22</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">PRIMARY PROBLEM SOURCE: MATHALINO</h3>
            <p style="color: var(--muted); font-size: 12.5px; line-height: 1.5; margin-bottom: 12px;">
              The authentic engineering optimization problems featured in this lecture are curated from Mathalino Reviewer (mathalino.com):
            </p>
            <div style="font-size: 12px; line-height: 1.6; color: var(--text);">
              <p>• <strong style="color: var(--cyan);">Problem 1 (Number Optimization):</strong><br>
              <a href="https://mathalino.com/reviewer/differential-calculus/01-04-number-problems-in-maxima-and-minima" target="_blank" style="color: var(--muted); text-decoration: underline;">01-04 Number Problems in Maxima and Minima</a></p>
              
              <p style="margin-top: 8px;">• <strong style="color: var(--cyan);">Problem 10 (Riverbank Fencing):</strong><br>
              <a href="https://mathalino.com/reviewer/differential-calculus/09-11-rectangular-lot-problems-in-maxima-and-minima" target="_blank" style="color: var(--muted); text-decoration: underline;">09-11 Rectangular Lot Problems in Maxima and Minima</a></p>
              
              <p style="margin-top: 8px;">• <strong style="color: var(--cyan);">Problem 16 (Open-Top Box):</strong><br>
              <a href="https://mathalino.com/reviewer/differential-calculus/15-17-box-open-at-the-top" target="_blank" style="color: var(--muted); text-decoration: underline;">15-17 Box Open at the Top</a></p>
              
              <p style="margin-top: 8px;">• <strong style="color: var(--cyan);">Problem 03 (Tour Bus Revenue):</strong><br>
              <a href="https://mathalino.com/reviewer/differential-calculus/03-maximum-revenue-tour-bus-80-seats" target="_blank" style="color: var(--muted); text-decoration: underline;">03 Maximum Revenue Tour Bus 80 Seats</a></p>
              
              <p style="margin-top: 8px;">• <strong style="color: var(--cyan);">Problem 42 (Trapezoidal Gutter):</strong><br>
              <a href="https://mathalino.com/reviewer/differential-calculus/41-42-maxima-and-minima-problem-involving-a-trapezoidal-gutter" target="_blank" style="color: var(--muted); text-decoration: underline;">41-42 Trapezoidal Gutter Problems</a></p>
            </div>
          </div>

          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">CALCULUS TEXTS & ANIMATION FOUNDATIONS</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--muted);">
              <p style="margin-top: 6px;"><strong style="color: #fff;">James Stewart, Calculus: Early Transcendentals (9th Ed.)</strong><br>
              Core mathematical framework: Fermat's Theorem, Extreme Value Theorem (EVT), First and Second Derivative Tests.</p>
              
              <p style="margin-top: 12px;"><strong style="color: #fff;">3Blue1Brown (Grant Sanderson), Essence of Calculus</strong><br>
              Kinematic visual storytelling, continuous geometric transformations, and dynamic tangent vector rotations.</p>
              
              <p style="margin-top: 12px;"><strong style="color: #fff;">Engineering Principles</strong><br>
              Maximum Power Transfer Theorem (Jacobi's Law, 1840) and hydraulic trapezoidal open-channel flow efficiency.</p>
              
              <p style="margin-top: 12px;"><strong style="color: #fff;">Platform & Apple Pencil Inking</strong><br>
              Full native Apple PencilKit support in Keynote on iPad (`.pptx`) and browser PointerEvents in Safari (`index.html`).</p>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- Floating Teleprompter -->
    <div class="teleprompter" id="teleprompter">
      <h4>Lecturer Teleprompter</h4>
      <div id="notesContent">Opening lecture notes...</div>
    </div>
  </div>

  <footer>
    <button id="prevBtn">◀ Previous</button>
    <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
    <span id="slideIndicator" style="font-weight: 600; color: var(--muted); min-width: 90px; text-align: center;">01 / 22</span>
    <button id="nextBtn">Next ▶</button>
  </footer>

  <script>
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;
    const progressFill = document.getElementById('progressFill');
    const slideIndicator = document.getElementById('slideIndicator');
    const teleprompter = document.getElementById('teleprompter');
    const notesContent = document.getElementById('notesContent');
    const sceneNav = document.getElementById('sceneNav');

    function playSlideVideo(slideEl) {
      const vid = slideEl.querySelector('video');
      if (vid) {
        vid.currentTime = 0;
        const playPromise = vid.play();
        if (playPromise !== undefined) {
          playPromise.catch(() => {
            // Autoplay policy handled silently
          });
        }
      }
    }

    function pauseSlideVideo(slideEl) {
      const vid = slideEl.querySelector('video');
      if (vid) {
        vid.pause();
      }
    }

    function toggleVideoPlayback(container) {
      const vid = container.querySelector('video');
      const indicator = container.querySelector('.play-pause-indicator');
      if (!vid) return;
      if (vid.paused) {
        vid.play();
        if (indicator) indicator.textContent = 'Playing (Tap to Pause)';
      } else {
        vid.pause();
        if (indicator) indicator.textContent = 'Paused (Tap to Play)';
      }
    }

    // Per-Slide Annotation Persistence Layers
    const slideInkLayers = {};

    function saveCurrentSlideInk() {
      if (!canvas || canvas.width === 0 || canvas.height === 0) return;
      const offscreen = document.createElement('canvas');
      offscreen.width = canvas.width;
      offscreen.height = canvas.height;
      const offCtx = offscreen.getContext('2d');
      offCtx.drawImage(canvas, 0, 0);
      slideInkLayers[currentSlide] = offscreen;
    }

    function restoreSlideInk(slideIndex) {
      if (!canvas || !ctx) return;
      const dpr = Math.max(window.devicePixelRatio || 1, 2);
      ctx.save();
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      if (slideInkLayers[slideIndex]) {
        ctx.drawImage(slideInkLayers[slideIndex], 0, 0);
      }
      ctx.restore();
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function showSlide(index) {
      if (index < 0 || index >= slides.length) return;

      // 1. Save annotations on the outgoing slide
      saveCurrentSlideInk();

      // 2. Clear undo/redo for incoming slide
      undoStack = [];
      redoStack = [];
      updateHistoryButtons();

      // 3. Pause old slide video
      pauseSlideVideo(slides[currentSlide]);
      slides[currentSlide].classList.remove('active');

      currentSlide = index;
      // Zoom position stays anchored where user set it

      // 4. Activate new slide
      const newSlide = slides[currentSlide];
      newSlide.classList.add('active');

      // 5. Restore annotations for this slide (or leave fresh & clean)
      restoreSlideInk(currentSlide);

      // Update progress & indicator
      progressFill.style.width = `${((currentSlide + 1) / slides.length) * 100}%`;
      slideIndicator.textContent = `${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;

      // Update dropdown
      sceneNav.value = String(currentSlide);

      // Update Teleprompter
      const notes = newSlide.getAttribute('data-notes');
      if (notes) {
        notesContent.textContent = notes;
      } else {
        notesContent.textContent = `Slide ${currentSlide + 1}: ${newSlide.getAttribute('data-title') || ''}`;
      }

      // Autoplay video
      playSlideVideo(newSlide);
    }

    // Navigation Events
    document.getElementById('prevBtn').addEventListener('click', () => showSlide(currentSlide - 1));
    document.getElementById('nextBtn').addEventListener('click', () => showSlide(currentSlide + 1));

    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        showSlide(currentSlide + 1);
        e.preventDefault();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        showSlide(currentSlide - 1);
        e.preventDefault();
      } else if (e.key === 'f' || e.key === 'F') {
        toggleFullscreen();
      } else if (e.key === 'd' || e.key === 'D') {
        toggleDrawing();
      } else if (e.key === '[' || e.key === '{') {
        if (typeof setStrokeSize === 'function') {
          setStrokeSize(currentStrokeSize - (currentStrokeSize <= 3 ? 0.5 : 1));
          showToast(`🖊 Stroke: ${currentStrokeSize % 1 === 0 ? currentStrokeSize.toFixed(0) : currentStrokeSize.toFixed(1)} px`);
        }
      } else if (e.key === ']' || e.key === '}') {
        if (typeof setStrokeSize === 'function') {
          setStrokeSize(currentStrokeSize + (currentStrokeSize < 3 ? 0.5 : 1));
          showToast(`🖊 Stroke: ${currentStrokeSize % 1 === 0 ? currentStrokeSize.toFixed(0) : currentStrokeSize.toFixed(1)} px`);
        }
      }
    });

    sceneNav.addEventListener('change', (e) => {
      showSlide(parseInt(e.target.value, 10));
    });

    // Teleprompter toggle
    const notesBtn = document.getElementById('notesBtn');
    notesBtn.addEventListener('click', () => {
      if (teleprompter.style.display === 'block') {
        teleprompter.style.display = 'none';
        notesBtn.classList.remove('active');
      } else {
        teleprompter.style.display = 'block';
        notesBtn.classList.add('active');
      }
    });

    // Fullscreen toggle
    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(() => {});
      } else {
        document.exitFullscreen().catch(() => {});
      }
    }
    document.getElementById('fsBtn').addEventListener('click', toggleFullscreen);

    // ==========================================
    // Retina HiDPI Apple PencilKit Inking Engine
    // ==========================================
    const canvas = document.getElementById('pencilCanvas');
    const ctx = canvas.getContext('2d');
    const pencilKitToolbar = document.getElementById('pencilKitToolbar');
    const drawBtn = document.getElementById('drawBtn');
    const pkPalmBadge = document.getElementById('pkPalmBadge');
    const pkUndoBtn = document.getElementById('pkUndoBtn');
    const pkRedoBtn = document.getElementById('pkRedoBtn');

    let isDrawingMode = false;
    let isDrawing = false;
    let activePointerId = null;
    let currentTool = 'pen'; // 'pen', 'pencil', 'highlighter', 'eraser'
    let currentColor = '#007AFF'; // Apple Blue default
    let currentStrokeSize = 3.0; // Stroke size in px
    let palmRejectionEnabled = true; // Strict Apple Pencil hardware filter

    let undoStack = [];
    let redoStack = [];
    const MAX_HISTORY = 20;

    let canvasDisplayWidth = 1360;
    let canvasDisplayHeight = 765;
    let lastPoint = null;

    function resizeCanvas() {
      const rect = stageContainer.getBoundingClientRect();
      const dpr = Math.max(window.devicePixelRatio || 1, 2);
      
      canvasDisplayWidth = stageContainer.offsetWidth || 1360;
      canvasDisplayHeight = stageContainer.offsetHeight || 765;

      const targetWidth = Math.round(canvasDisplayWidth * dpr);
      const targetHeight = Math.round(canvasDisplayHeight * dpr);

      if (canvas.width !== targetWidth || canvas.height !== targetHeight) {
        let tempCanvas = null;
        if (canvas.width > 0 && canvas.height > 0) {
          tempCanvas = document.createElement('canvas');
          tempCanvas.width = canvas.width;
          tempCanvas.height = canvas.height;
          tempCanvas.getContext('2d').drawImage(canvas, 0, 0);
        }

        canvas.width = targetWidth;
        canvas.height = targetHeight;
        canvas.style.width = canvasDisplayWidth + 'px';
        canvas.style.height = canvasDisplayHeight + 'px';

        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        ctx.imageSmoothingEnabled = true;
        ctx.imageSmoothingQuality = 'high';

        if (tempCanvas) {
          ctx.save();
          ctx.setTransform(1, 0, 0, 1, 0, 0);
          ctx.drawImage(tempCanvas, 0, 0, targetWidth, targetHeight);
          ctx.restore();
        } else if (slideInkLayers[currentSlide]) {
          ctx.save();
          ctx.setTransform(1, 0, 0, 1, 0, 0);
          ctx.drawImage(slideInkLayers[currentSlide], 0, 0, targetWidth, targetHeight);
          ctx.restore();
        }
      }
    }
    window.addEventListener('resize', resizeCanvas);
    setTimeout(resizeCanvas, 150);

    function pushUndoState() {
      try {
        if (undoStack.length >= MAX_HISTORY) undoStack.shift();
        const snap = document.createElement('canvas');
        snap.width = canvas.width;
        snap.height = canvas.height;
        snap.getContext('2d').drawImage(canvas, 0, 0);
        undoStack.push(snap);
        redoStack = [];
        updateHistoryButtons();
      } catch (e) {}
    }

    function updateHistoryButtons() {
      pkUndoBtn.disabled = undoStack.length === 0;
      pkRedoBtn.disabled = redoStack.length === 0;
    }

    function undo() {
      if (undoStack.length === 0) return;
      try {
        const snap = document.createElement('canvas');
        snap.width = canvas.width;
        snap.height = canvas.height;
        snap.getContext('2d').drawImage(canvas, 0, 0);
        redoStack.push(snap);

        const prevState = undoStack.pop();
        const dpr = Math.max(window.devicePixelRatio || 1, 2);
        ctx.save();
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(prevState, 0, 0);
        ctx.restore();
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        updateHistoryButtons();
      } catch (e) {}
    }

    function redo() {
      if (redoStack.length === 0) return;
      try {
        const snap = document.createElement('canvas');
        snap.width = canvas.width;
        snap.height = canvas.height;
        snap.getContext('2d').drawImage(canvas, 0, 0);
        undoStack.push(snap);

        const nextState = redoStack.pop();
        const dpr = Math.max(window.devicePixelRatio || 1, 2);
        ctx.save();
        ctx.setTransform(1, 0, 0, 1, 0, 0);
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.drawImage(nextState, 0, 0);
        ctx.restore();
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        updateHistoryButtons();
      } catch (e) {}
    }

    pkUndoBtn.addEventListener('click', undo);
    pkRedoBtn.addEventListener('click', redo);

    function toggleDrawing(force) {
      isDrawingMode = (typeof force === 'boolean') ? force : !isDrawingMode;
      if (isDrawingMode) {
        drawBtn.classList.add('active');
        canvas.classList.add('active');
        stageContainer.classList.add('drawing-locked');
        pencilKitToolbar.classList.remove('hidden');
        resizeCanvas();
      } else {
        drawBtn.classList.remove('active');
        canvas.classList.remove('active');
        stageContainer.classList.remove('drawing-locked');
        pencilKitToolbar.classList.add('hidden');
      }
    }

    drawBtn.addEventListener('click', () => toggleDrawing());
    document.getElementById('pkCloseBtn').addEventListener('click', () => toggleDrawing(false));

    // Tool switching
    const tools = {
      pen: document.getElementById('toolPen'),
      pencil: document.getElementById('toolPencil'),
      highlighter: document.getElementById('toolHighlighter'),
      eraser: document.getElementById('toolEraser')
    };

    function setTool(toolName) {
      if (currentTool === toolName) {
        toggleSizePopover();
        return;
      }
      currentTool = toolName;
      Object.values(tools).forEach(btn => btn.classList.remove('active'));
      if (tools[toolName]) tools[toolName].classList.add('active');
    }

    tools.pen.addEventListener('click', () => setTool('pen'));
    tools.pencil.addEventListener('click', () => setTool('pencil'));
    tools.highlighter.addEventListener('click', () => setTool('highlighter'));
    tools.eraser.addEventListener('click', () => setTool('eraser'));

    // Stroke Size Management & Apple-style Popover
    const pkSizeBtn = document.getElementById('pkSizeBtn');
    const pkSizePopover = document.getElementById('pkSizePopover');
    const pkSizeLabel = document.getElementById('pkSizeLabel');
    const pkSizeDotPreview = document.getElementById('pkSizeDotPreview');
    const pkSizeValueDisplay = document.getElementById('pkSizeValueDisplay');
    const pkSizeSlider = document.getElementById('pkSizeSlider');
    const pkStrokePreviewLine = document.getElementById('pkStrokePreviewLine');

    function toggleSizePopover(force) {
      if (!pkSizePopover) return;
      const willOpen = (typeof force === 'boolean') ? force : pkSizePopover.classList.contains('hidden');
      if (willOpen) {
        pkSizePopover.classList.remove('hidden');
        if (pkSizeBtn) pkSizeBtn.classList.add('active');
      } else {
        pkSizePopover.classList.add('hidden');
        if (pkSizeBtn) pkSizeBtn.classList.remove('active');
      }
    }

    if (pkSizeBtn) {
      pkSizeBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleSizePopover();
      });
    }

    function setStrokeSize(size) {
      currentStrokeSize = Math.max(1, Math.min(25, parseFloat(size) || 3.0));
      const displayStr = (currentStrokeSize % 1 === 0 ? currentStrokeSize.toFixed(0) : currentStrokeSize.toFixed(1)) + ' px';

      if (pkSizeLabel) pkSizeLabel.textContent = displayStr;
      if (pkSizeValueDisplay) pkSizeValueDisplay.textContent = displayStr;
      if (pkSizeSlider) pkSizeSlider.value = currentStrokeSize;

      if (pkSizeDotPreview) {
        const dotD = Math.min(16, Math.max(4, Math.round(currentStrokeSize * 1.5)));
        pkSizeDotPreview.style.width = `${dotD}px`;
        pkSizeDotPreview.style.height = `${dotD}px`;
        pkSizeDotPreview.style.backgroundColor = currentColor;
      }

      if (pkStrokePreviewLine) {
        pkStrokePreviewLine.style.height = `${Math.max(1.5, Math.min(20, currentStrokeSize))}px`;
        pkStrokePreviewLine.style.backgroundColor = currentColor;
      }

      document.querySelectorAll('.pk-preset-circle').forEach(btn => {
        const s = parseFloat(btn.getAttribute('data-size'));
        if (Math.abs(s - currentStrokeSize) < 0.3) {
          btn.classList.add('active');
        } else {
          btn.classList.remove('active');
        }
      });
    }

    if (pkSizeSlider) {
      pkSizeSlider.addEventListener('input', (e) => {
        setStrokeSize(e.target.value);
      });
    }

    document.querySelectorAll('.pk-preset-circle').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const size = parseFloat(btn.getAttribute('data-size'));
        setStrokeSize(size);
      });
    });

    function updatePreviewColors() {
      if (pkSizeDotPreview) pkSizeDotPreview.style.backgroundColor = currentColor;
      if (pkStrokePreviewLine) pkStrokePreviewLine.style.backgroundColor = currentColor;
    }

    // Dismiss popover on outside tap
    document.addEventListener('pointerdown', (e) => {
      if (pkSizePopover && !pkSizePopover.classList.contains('hidden')) {
        if (!e.target.closest('#pkSizePopover') && !e.target.closest('#pkSizeBtn') && !e.target.closest('.pk-tool')) {
          toggleSizePopover(false);
        }
      }
    });

    // Color Swatches
    document.querySelectorAll('.pk-swatch').forEach(swatch => {
      swatch.addEventListener('click', () => {
        document.querySelectorAll('.pk-swatch').forEach(s => s.classList.remove('active'));
        swatch.classList.add('active');
        currentColor = swatch.getAttribute('data-color');
        updatePreviewColors();
        if (currentTool === 'eraser') setTool('pen');
      });
    });

    const customColorInput = document.getElementById('pkCustomColor');
    customColorInput.addEventListener('input', (e) => {
      currentColor = e.target.value;
      updatePreviewColors();
      document.querySelectorAll('.pk-swatch').forEach(s => s.classList.remove('active'));
      if (currentTool === 'eraser') setTool('pen');
    });

    // Clear slide ink
    document.getElementById('pkClearBtn').addEventListener('click', () => {
      pushUndoState();
      delete slideInkLayers[currentSlide];
      const dpr = Math.max(window.devicePixelRatio || 1, 2);
      ctx.save();
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.restore();
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    });

    // Palm Rejection Toggle
    pkPalmBadge.addEventListener('click', () => {
      palmRejectionEnabled = !palmRejectionEnabled;
      if (palmRejectionEnabled) {
        pkPalmBadge.classList.remove('off');
        pkPalmBadge.innerHTML = '<span> Palm Rejection: ON</span>';
      } else {
        pkPalmBadge.classList.add('off');
        pkPalmBadge.innerHTML = '<span>👆 Touch Inking: ON</span>';
      }
    });

    function hexToRgba(hex, alpha) {
      let c;
      if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)) {
        c = hex.substring(1).split('');
        if (c.length === 3) c = [c[0], c[0], c[1], c[1], c[2], c[2]];
        c = '0x' + c.join('');
        return 'rgba(' + [(c >> 16) & 255, (c >> 8) & 255, c & 255].join(',') + ',' + alpha + ')';
      }
      return hex;
    }

    function getPointerPos(e) {
      const rect = canvas.getBoundingClientRect();
      return {
        x: (e.clientX - rect.left) * (canvasDisplayWidth / rect.width),
        y: (e.clientY - rect.top) * (canvasDisplayHeight / rect.height)
      };
    }

    function isAllowedPointer(e) {
      if (!isDrawingMode) return false;
      if (palmRejectionEnabled) {
        return e.pointerType === 'pen' || e.pointerType === 'mouse';
      }
      return true;
    }

    function applyToolStyle(e) {
      const pressure = (e.pressure && e.pressure > 0) ? e.pressure : 0.5;
      const baseSize = currentStrokeSize;
      const scale = baseSize / 3.0;

      if (currentTool === 'eraser') {
        ctx.globalCompositeOperation = 'destination-out';
        ctx.lineWidth = Math.max(8, 28 * scale);
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
      } else if (currentTool === 'highlighter') {
        ctx.globalCompositeOperation = 'source-over';
        ctx.strokeStyle = hexToRgba(currentColor, 0.35);
        ctx.lineWidth = Math.max(8, 22 * scale);
        ctx.lineCap = 'square';
        ctx.lineJoin = 'miter';
      } else if (currentTool === 'pencil') {
        ctx.globalCompositeOperation = 'source-over';
        ctx.strokeStyle = hexToRgba(currentColor, 0.85);
        ctx.lineWidth = Math.max(0.8, (1.6 + pressure * 2.2) * scale);
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
      } else { // 'pen' (crisp, vector smooth monoline / pressure response)
        ctx.globalCompositeOperation = 'source-over';
        ctx.strokeStyle = currentColor;
        ctx.lineWidth = Math.max(0.8, baseSize * (0.75 + pressure * 0.5));
        ctx.lineCap = 'round';
        ctx.lineJoin = 'round';
      }
    }

    function onPointerDown(e) {
      if (!isDrawingMode) return;
      if (!isAllowedPointer(e)) {
        e.preventDefault();
        return;
      }
      if (pkSizePopover && !pkSizePopover.classList.contains('hidden')) {
        toggleSizePopover(false);
      }
      isDrawing = true;
      activePointerId = e.pointerId;
      try { canvas.setPointerCapture(e.pointerId); } catch (err) {}

      pushUndoState();
      const pos = getPointerPos(e);
      lastPoint = pos;
      applyToolStyle(e);

      ctx.beginPath();
      ctx.moveTo(pos.x, pos.y);
      ctx.arc(pos.x, pos.y, Math.max(1, (ctx.lineWidth || currentStrokeSize) / 2), 0, Math.PI * 2);
      ctx.fill();
      ctx.beginPath();
      ctx.moveTo(pos.x, pos.y);
      e.preventDefault();
    }

    function onPointerMove(e) {
      if (!isDrawing || !isDrawingMode) return;
      if (activePointerId !== null && e.pointerId !== activePointerId) {
        e.preventDefault();
        return;
      }
      const pos = getPointerPos(e);
      if (!lastPoint) { lastPoint = pos; return; }

      applyToolStyle(e);
      // Midpoint Bezier quadratic smoothing for vector-grade line curvature
      const midX = (lastPoint.x + pos.x) / 2;
      const midY = (lastPoint.y + pos.y) / 2;

      ctx.quadraticCurveTo(lastPoint.x, lastPoint.y, midX, midY);
      ctx.stroke();

      lastPoint = pos;
      e.preventDefault();
    }

    function onPointerUp(e) {
      if (!isDrawing) return;
      if (activePointerId !== null && e.pointerId !== activePointerId) return;
      isDrawing = false;
      activePointerId = null;
      lastPoint = null;
      try { canvas.releasePointerCapture(e.pointerId); } catch (err) {}
      ctx.closePath();
      e.preventDefault();
    }

    canvas.addEventListener('pointerdown', onPointerDown);
    canvas.addEventListener('pointermove', onPointerMove);
    canvas.addEventListener('pointerup', onPointerUp);
    canvas.addEventListener('pointercancel', onPointerUp);

    // ==========================================
    // Slide Zoom & Two-Finger Pinch-Zoom Engine
    // ==========================================
    let currentZoom = 1.0;
    let panX = 0, panY = 0;
    let initialPinchDistance = null;
    let initialZoom = 1.0;
    let pinchMidX = 0, pinchMidY = 0;
    let isPinching = false;

    function applyZoom(zoomFactor, resetPan = false) {
      currentZoom = Math.min(Math.max(zoomFactor, 1.0), 3.5);
      if (resetPan || currentZoom <= 1.01) {
        panX = 0;
        panY = 0;
        currentZoom = 1.0;
      } else {
        const maxPanX = ((currentZoom - 1) * (canvasDisplayWidth || 1360) * 0.45) / currentZoom;
        const maxPanY = ((currentZoom - 1) * (canvasDisplayHeight || 765) * 0.45) / currentZoom;
        panX = Math.max(-maxPanX, Math.min(maxPanX, panX));
        panY = Math.max(-maxPanY, Math.min(maxPanY, panY));
      }
      stageContainer.style.transform = `scale(${currentZoom}) translate(${panX}px, ${panY}px)`;
      const zoomDisplay = document.getElementById('zoomDisplay');
      if (zoomDisplay) zoomDisplay.textContent = `${Math.round(currentZoom * 100)}%`;
      const zoomResetBtn = document.getElementById('zoomResetBtn');
      if (zoomResetBtn) {
        if (currentZoom > 1.0) {
          zoomResetBtn.style.color = '#38BDF8';
          zoomResetBtn.style.fontWeight = '800';
        } else {
          zoomResetBtn.style.color = 'var(--cyan)';
          zoomResetBtn.style.fontWeight = '700';
        }
      }
    }

    function resetZoom() {
      stageContainer.style.transition = 'transform 0.25s cubic-bezier(0.16, 1, 0.3, 1)';
      applyZoom(1.0, true);
    }

    document.getElementById('zoomInBtn').addEventListener('click', () => {
      stageContainer.style.transition = 'transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)';
      applyZoom(currentZoom + 0.25);
    });
    document.getElementById('zoomOutBtn').addEventListener('click', () => {
      stageContainer.style.transition = 'transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)';
      applyZoom(currentZoom - 0.25);
    });
    document.getElementById('zoomResetBtn').addEventListener('click', resetZoom);
    const pkZoomResetBtn = document.getElementById('pkZoomResetBtn');
    if (pkZoomResetBtn) pkZoomResetBtn.addEventListener('click', resetZoom);

    function getPinchDistance(e) {
      if (!e.touches || e.touches.length < 2) return null;
      const dx = e.touches[0].clientX - e.touches[1].clientX;
      const dy = e.touches[0].clientY - e.touches[1].clientY;
      return Math.hypot(dx, dy);
    }

    // Touch Gestures: Smooth Two-Finger Pinch-to-Zoom & Pan
    stageContainer.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches.length === 2) {
        isPinching = true;
        stageContainer.style.transition = 'none'; // Zero lag during pinch
        initialPinchDistance = getPinchDistance(e);
        initialZoom = currentZoom;
        pinchMidX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
        pinchMidY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
        e.preventDefault();
      }
    }, { passive: false });

    stageContainer.addEventListener('touchmove', (e) => {
      if (e.touches && e.touches.length === 2 && isPinching) {
        const dist = getPinchDistance(e);
        if (initialPinchDistance && dist) {
          const scaleMultiplier = dist / initialPinchDistance;
          const targetZoom = initialZoom * scaleMultiplier;

          // Two-finger pan while zoomed in
          const midX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
          const midY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
          if (targetZoom > 1.05) {
            panX += (midX - pinchMidX) / targetZoom;
            panY += (midY - pinchMidY) / targetZoom;
          }
          pinchMidX = midX;
          pinchMidY = midY;

          applyZoom(targetZoom);
        }
        e.preventDefault();
      } else if (e.touches && e.touches.length === 1) {
        if (isDrawingMode && palmRejectionEnabled) {
          e.preventDefault();
        }
      }
    }, { passive: false });

    stageContainer.addEventListener('touchend', (e) => {
      if (!e.touches || e.touches.length < 2) {
        isPinching = false;
        initialPinchDistance = null;
        stageContainer.style.transition = 'transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)';
      }
    });

    // =========================================================================
    // Multi-Tap Hotkeys:
    // When zoomed in: Double-Tap ZOOMS OUT to 100%!
    // When at 100%: Double-Tap advances to NEXT SLIDE, Triple-Tap to PREVIOUS!
    // =========================================================================
    let tapCount = 0;
    let tapTimeout = null;
    let touchStartX = 0, touchStartY = 0, touchStartTime = 0;
    const TAP_THRESHOLD_MS = 320;
    const TAP_MOVE_LIMIT = 15;

    function showToast(message) {
      let toast = document.getElementById('slideToast');
      if (!toast) {
        toast = document.createElement('div');
        toast.id = 'slideToast';
        toast.style.cssText = `
          position: fixed;
          top: 66px;
          left: 50%;
          transform: translateX(-50%);
          background: rgba(15, 23, 42, 0.94);
          backdrop-filter: blur(16px);
          -webkit-backdrop-filter: blur(16px);
          border: 1px solid rgba(56, 189, 248, 0.6);
          color: #38BDF8;
          padding: 8px 20px;
          border-radius: 20px;
          font-size: 13.5px;
          font-weight: 700;
          letter-spacing: 0.3px;
          z-index: 999;
          box-shadow: 0 10px 30px rgba(0,0,0,0.6);
          pointer-events: none;
          opacity: 0;
          transition: opacity 0.2s cubic-bezier(0.16, 1, 0.3, 1), transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
        `;
        document.body.appendChild(toast);
      }
      toast.textContent = message;
      toast.style.opacity = '1';
      toast.style.transform = 'translateX(-50%) translateY(0px)';
      clearTimeout(toast._timer);
      toast._timer = setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(-50%) translateY(-10px)';
      }, 1300);
    }

    function processTapGesture(target) {
      if (target.closest('header') || target.closest('#pencilKitToolbar') || target.closest('button') || target.closest('select')) {
        return;
      }

      tapCount++;
      if (tapTimeout) clearTimeout(tapTimeout);

      if (tapCount === 3) {
        // TRIPLE TAP -> PREVIOUS SLIDE!
        tapCount = 0;
        showSlide(currentSlide - 1);
        showToast(`⏮ Slide ${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')} (Triple Tap)`);
        return;
      }

      tapTimeout = setTimeout(() => {
        if (tapCount === 2) {
          if (currentZoom > 1.05) {
            // IF ZOOMED IN -> DOUBLE TAP ZOOMS OUT TO 100%!
            resetZoom();
            showToast('🔍 Zoom Reset (100%)');
          } else {
            // IF AT 100% -> DOUBLE TAP ADVANCES TO NEXT SLIDE!
            showSlide(currentSlide + 1);
            showToast(`⏭ Slide ${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')} (Double Tap)`);
          }
        }
        tapCount = 0;
      }, TAP_THRESHOLD_MS);
    }

    stageContainer.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches.length === 1) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        touchStartTime = Date.now();
      }
    }, { passive: true });

    stageContainer.addEventListener('touchend', (e) => {
      if (e.changedTouches && e.changedTouches.length === 1) {
        const dx = Math.abs(e.changedTouches[0].clientX - touchStartX);
        const dy = Math.abs(e.changedTouches[0].clientY - touchStartY);
        const dt = Date.now() - touchStartTime;
        if (dx < TAP_MOVE_LIMIT && dy < TAP_MOVE_LIMIT && dt < 320) {
          // In drawing mode, only fingers trigger slide changes so Apple Pencil can write freely
          if (!isDrawingMode || (e.changedTouches[0].touchType !== 'stylus')) {
            processTapGesture(e.target);
          }
        }
      }
    }, { passive: true });

    let clickStartX = 0, clickStartY = 0, clickStartTime = 0;
    stageContainer.addEventListener('pointerdown', (e) => {
      if (e.pointerType === 'mouse') {
        clickStartX = e.clientX;
        clickStartY = e.clientY;
        clickStartTime = Date.now();
      }
    });

    stageContainer.addEventListener('pointerup', (e) => {
      if (e.pointerType === 'mouse' && !isDrawingMode) {
        const dx = Math.abs(e.clientX - clickStartX);
        const dy = Math.abs(e.clientY - clickStartY);
        const dt = Date.now() - clickStartTime;
        if (dx < TAP_MOVE_LIMIT && dy < TAP_MOVE_LIMIT && dt < 320) {
          processTapGesture(e.target);
        }
      }
    });

    // Initialize pen stroke size & swatches
    if (typeof setStrokeSize === 'function') setStrokeSize(3.0);
    if (typeof updatePreviewColors === 'function') updatePreviewColors();

    // Initial load
    showSlide(0);
  </script>
</body>
</html>
"""

def main():
    for filepath in ["index.html", "public/index.html", "presentation/player.html"]:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(HTML_TEMPLATE)
        print(f"Updated {filepath}")

if __name__ == "__main__":
    main()
