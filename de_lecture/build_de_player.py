import os

DE_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=3.0, user-scalable=yes">
  <title>Applications of Differential Equations // MATHalino Lecture Deck</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0B0F19;
      --card-bg: #0F172A;
      --card-border: #1E293B;
      --text: #F8FAFC;
      --muted: #94A3B8;
      --cyan: #38BDF8;
      --amber: #F59E0B;
      --coral: #F43F5E;
      --green: #10B981;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      touch-action: pan-x pan-y;
    }

    /* Top Control Bar */
    header {
      height: 52px;
      background: rgba(11, 15, 25, 0.95);
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
      gap: 12px;
    }
    .brand-tag {
      font-size: 11px;
      font-weight: 700;
      color: var(--cyan);
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 3px 8px;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }
    .brand-title {
      font-size: 14px;
      font-weight: 700;
      color: var(--text);
    }
    .controls {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    button, select {
      background: #1E293B;
      border: 1px solid #334155;
      color: var(--text);
      font-family: inherit;
      font-size: 12.5px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }
    button:hover { background: #334155; border-color: var(--cyan); }
    button.active { background: rgba(56, 189, 248, 0.2); border-color: var(--cyan); color: var(--cyan); }

    /* Main Stage */
    .main-stage {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 16px;
    }
    .slide-container {
      position: relative;
      width: 100%;
      max-width: 1360px;
      aspect-ratio: 16 / 9;
      background: var(--card-bg);
      border-radius: 12px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
      overflow: hidden;
      border: 1px solid var(--card-border);
      transform-origin: center center;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .slide {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      padding: 24px 32px;
      display: none;
      flex-direction: column;
      opacity: 0;
      transition: opacity 0.25s ease;
      overflow: hidden;
    }
    .slide.active {
      display: flex;
      opacity: 1;
    }
    .slide-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
      border-bottom: 1px solid rgba(51, 65, 85, 0.35);
      padding-bottom: 10px;
    }
    .slide-top .meta {
      font-size: 11px;
      color: var(--cyan);
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 3px;
    }
    .slide-top h1 {
      font-size: 22px;
      font-weight: 800;
      color: #fff;
      line-height: 1.25;
    }
    .slide-top .slide-num {
      font-size: 13px;
      font-weight: 700;
      color: var(--muted);
      background: #1E293B;
      padding: 4px 10px;
      border-radius: 6px;
    }

    .slide-body {
      flex: 1;
      display: grid;
      gap: 20px;
      overflow: hidden;
    }
    .grid-equal { grid-template-columns: 1.15fr 0.85fr; }
    .grid-full { grid-template-columns: 1fr; }

    .card {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 16px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
    }
    .card.cyan-border { border-color: rgba(56, 189, 248, 0.4); }
    .card.amber-border { border-color: rgba(245, 158, 11, 0.4); }
    .card.green-border { border-color: rgba(16, 185, 129, 0.4); }

    /* Video & Media Container */
    .video-container {
      position: relative;
      width: 100%;
      height: 100%;
      background: #000;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid rgba(51, 65, 85, 0.5);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .video-container video, .video-container img {
      width: 100%;
      height: 100%;
      object-fit: contain;
    }
    .play-pause-indicator {
      position: absolute;
      bottom: 12px;
      right: 12px;
      background: rgba(0, 0, 0, 0.7);
      color: #fff;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 600;
      pointer-events: none;
    }

    /* Inking Overlay Canvas (Apple Pencil Compatible) */
    #pencilCanvas {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      z-index: 60;
      pointer-events: none;
      touch-action: pinch-zoom;
    }
    #pencilCanvas.active {
      pointer-events: auto;
      cursor: crosshair;
    }

    /* Native-Grade Apple PencilKit Floating Palette */
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
    .pencilkit-toolbar.hidden { display: none; }
    .pencilkit-handle {
      position: absolute;
      top: 3px; left: 50%;
      transform: translateX(-50%);
      width: 32px; height: 3.5px;
      background: #D1D5DB;
      border-radius: 2px;
      cursor: grab;
    }
    .pk-circle-btn {
      width: 32px; height: 32px;
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
    .pk-circle-btn:hover { background: #E2E8F0; color: #0F172A; }
    .pk-circle-btn:disabled { opacity: 0.3; cursor: not-allowed; pointer-events: none; }
    .pk-divider { width: 1px; height: 22px; background: #E2E8F0; margin: 0 2px; }

    .pk-tool {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      width: 38px; height: 48px;
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
    .pk-tool:hover { background: #F8FAFC; }
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

    /* Pen Size Selector & Popover */
    .pk-size-wrap { position: relative; display: flex; align-items: center; }
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
      width: 6px; height: 6px;
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
    .pk-size-popover.hidden { display: none !important; }
    .pk-size-popover::after {
      content: '';
      position: absolute;
      top: 100%; left: 50%;
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
      width: 32px; height: 32px;
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
    .pk-preset-circle:hover { background: #E2E8F0; }
    .pk-preset-circle.active { background: #EFF6FF; border-color: #3B82F6; }
    .pk-preset-circle.active span { background: #1D4ED8; transform: scale(1.15); }
    .pk-stroke-preview-box {
      height: 28px;
      background: #F1F5F9;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 0 10px;
    }

    /* Swatches */
    .pk-swatch {
      width: 20px; height: 20px;
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
    .pk-badge-palm.off { background: #FEF2F2; border-color: #FECACA; color: #991B1B; }
    .pk-color-picker-wrap {
      position: relative;
      width: 20px; height: 20px;
      border-radius: 50%;
      background: conic-gradient(red, yellow, lime, aqua, blue, magenta, red);
      cursor: pointer;
      box-shadow: 0 0 0 1px rgba(0,0,0,0.2);
    }
    .pk-color-picker-wrap input[type="color"] {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      opacity: 0; cursor: pointer;
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
      width: 4.76%;
      transition: width 0.3s ease;
    }

    /* Floating Teleprompter */
    .teleprompter {
      position: absolute;
      right: 24px; bottom: 70px;
      width: 380px; max-height: 240px;
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(16px);
      border: 1px solid var(--cyan);
      border-radius: 10px;
      padding: 14px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
      display: none;
      z-index: 150;
      color: #fff;
      font-size: 13px;
      line-height: 1.5;
      overflow-y: auto;
    }
    .teleprompter h4 { color: var(--cyan); font-size: 12px; font-weight: 700; margin-bottom: 6px; text-transform: uppercase; }

    /* On-screen Toast */
    .toast {
      position: absolute;
      top: 70px; left: 50%;
      transform: translateX(-50%);
      background: rgba(15, 23, 42, 0.95);
      color: #fff;
      padding: 8px 18px;
      border-radius: 9999px;
      font-size: 13px;
      font-weight: 700;
      border: 1px solid var(--cyan);
      box-shadow: 0 8px 24px rgba(0,0,0,0.5);
      z-index: 200;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.25s, transform 0.25s;
    }
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <span class="brand-tag">MATHalino DE Review</span>
      <span class="brand-title">Elementary Applications of Differential Equations</span>
      <a href="index.html" style="text-decoration:none; margin-left: 8px;">
        <span class="brand-tag" style="background: rgba(56, 189, 248, 0.15); border-color: rgba(56, 189, 248, 0.4); color: #38BDF8; cursor: pointer;" title="Switch to Maxima & Minima Lecture">📈 Maxima & Minima ➔</span>
      </a>
    </div>
    <div class="controls">
      <select id="sceneNav" title="Jump to Scene">
        <option value="0">01. Lecture Title & Scope</option>
        <option value="1">02. 4-Step Modeling Blueprint</option>
        <option value="2">03. Separation of Variables Engine</option>
        <option value="3">04. Newton's Cooling: Physical Intuition</option>
        <option value="4">05. Newton's Cooling: Derivation Morph</option>
        <option value="5">06. Problem 01: Thermometer After 6 Min</option>
        <option value="6">07. Problem 01: Resolution & Ratio Insight</option>
        <option value="7">08. Problem 02: Time to Within Half Degree</option>
        <option value="8">09. Problem 02: Logarithmic Resolution</option>
        <option value="9">10. Thermal Modeling Live Whiteboard</option>
        <option value="10">11. Chemical Conversion & Nuclear Decay</option>
        <option value="11">12. Stochastic Atoms vs Continuum Calculus</option>
        <option value="12">13. Problem 01: Radium Half-Life Setup</option>
        <option value="13">14. Problem 01: Century-Scale Resolution</option>
        <option value="14">15. Problem 02: 90% Dissipation Setup</option>
        <option value="15">16. Problem 02: Threshold Resolution</option>
        <option value="16">17. Extension: Velocity of Escape from Earth</option>
        <option value="17">18. Escape Velocity Analytical Resolution</option>
        <option value="18">19. Master Comparative Modeling Matrix</option>
        <option value="19">20. Lecture Summary & Live Q&A</option>
        <option value="20">21. Curriculum References & MATHalino Citations</option>
      </select>
      <button id="drawBtn" title="Toggle Apple Pencil Inking (D)">🖊 Inking</button>
      <button id="notesBtn" title="Toggle Lecturer Teleprompter">📝 Notes</button>
      <button id="zoomInBtn" title="Zoom In (+)">🔍 +</button>
      <button id="zoomOutBtn" title="Zoom Out (-)">🔍 -</button>
      <a href="Differential_Equations_Lecture.pptx" download style="text-decoration:none;">
        <button style="background: rgba(34, 197, 94, 0.15); border-color: rgba(34, 197, 94, 0.4); color: #10B981;" title="Download Keynote/PowerPoint Deck">📥 Keynote (.pptx)</button>
      </a>
      <a href="Differential_Equations_Lecture.pdf" download style="text-decoration:none;">
        <button style="background: rgba(244, 63, 94, 0.15); border-color: rgba(244, 63, 94, 0.4); color: #FB7185;" title="Download PDF Backup for GoodNotes / Notability / iPad">📄 PDF Backup</button>
      </a>
      <button id="fsBtn" title="Toggle Fullscreen (F)">⛶ Fullscreen</button>
    </div>
  </header>

  <div class="main-stage">
    <div class="slide-container" id="stageContainer">
      <canvas id="pencilCanvas"></canvas>

      <!-- Floating Apple PencilKit Toolbar -->
      <div id="pencilKitToolbar" class="pencilkit-toolbar hidden">
        <div class="pencilkit-handle" title="Drag toolbar"></div>
        <button class="pk-circle-btn" id="pkUndoBtn" title="Undo" disabled>↺</button>
        <button class="pk-circle-btn" id="pkRedoBtn" title="Redo" disabled>↻</button>
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
        <div class="pk-color-picker-wrap" title="Custom Palette">
          <input type="color" id="pkCustomColor" value="#38BDF8">
        </div>
        <div class="pk-divider"></div>
        <div class="pk-badge-palm" id="pkPalmBadge" title="Strict Apple Pencil Hardware Filter">
          <span> Palm Rejection: ON</span>
        </div>
        <button class="pk-circle-btn" id="pkZoomResetBtn" title="Reset Zoom" style="width:28px;height:28px;font-size:10px;font-weight:700;">100%</button>
        <button class="pk-circle-btn" id="pkCloseBtn" title="Close Toolbar" style="width:26px;height:26px;font-size:11px;">✕</button>
      </div>

      <!-- SLIDE 1: Title -->
      <div class="slide active" data-title="Lecture Title & Scope" data-notes="Welcome class. Today we explore elementary applications of first-order differential equations using authentic engineering problems from MATHalino. Notice how rates of change define future trajectories.">
        <div class="slide-top">
          <div><div class="meta">Differential Equations // Engineering Review</div><h1>Applications of First-Order Differential Equations</h1></div>
          <div class="slide-num">01 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene01_IntroDE.mp4" poster="frames/Scene01_IntroDE.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">DYNAMIC PHYSICAL MODELING</h3>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 12px;">
              Differential equations describe physical phenomena through rates of change rather than static algebraic snapshots.
            </p>
            <div style="font-size: 12.5px; line-height: 1.6; color: #fff;">
              <p>• <strong style="color: var(--amber);">Rate vs State:</strong> The derivative dy/dt expresses how fast a system evolves based on its present state.</p>
              <p>• <strong style="color: var(--amber);">Authentic Source:</strong> All problems derive directly from MATHalino Engineering Review.</p>
              <p>• <strong style="color: var(--amber);">Key Topics:</strong> Newton's Cooling, Chemical Conversion/Decay, and Earth Escape Velocity.</p>
            </div>
            <div style="margin-top: auto; padding: 10px; background: rgba(56, 189, 248, 0.1); border-radius: 6px; border: 1px dashed var(--cyan);">
              <span style="font-size: 11px; font-weight: 700; color: var(--cyan);"> Apple Pencil Annotation Ready: Use side pane for live class notes</span>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 2: 4-Step Blueprint -->
      <div class="slide" data-title="4-Step Modeling Blueprint" data-notes="Walk through the 4 universal steps: 1) Formulate physical rate law. 2) Write the differential equation with proportionality constant k. 3) Separate variables and integrate. 4) Apply initial conditions to evaluate C.">
        <div class="slide-top">
          <div><div class="meta">Mathematical Framework // Universal Protocol</div><h1>The 4-Step Mathematical Modeling Blueprint</h1></div>
          <div class="slide-num">02 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene02_ModelingBlueprint.mp4" poster="frames/Scene02_ModelingBlueprint.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">THE MODELING LIFECYCLE</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">1. Physical Law:</strong> Identify the physical rate mechanism (e.g. conduction, decay, gravitation).</p>
              <p><strong style="color: #fff;">2. Differential Equation:</strong> Introduce parameter k with appropriate sign (+ growth, - decay).</p>
              <p><strong style="color: #fff;">3. Separation & Integration:</strong> Group variables dy/g(y) = h(t)dt and integrate analytically.</p>
              <p><strong style="color: #fff;">4. Initial Value Problem (IVP):</strong> Use initial conditions y(0) = y₀ to determine constant C.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 3: Separation of Variables -->
      <div class="slide" data-title="Separation of Variables Engine" data-notes="Master the algebraic mechanism of separating differentials. Highlight how Leibniz differentials dy and dt are grouped across equality.">
        <div class="slide-top">
          <div><div class="meta">Calculus Engine // Analytical Integration</div><h1>Separation of Variables Mathematical Engine</h1></div>
          <div class="slide-num">03 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene03_SeparationVariables.mp4" poster="frames/Scene03_SeparationVariables.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">ALGEBRAIC MECHANICS</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Form:</strong> dy/dt = g(y) · h(t)</p>
              <p><strong style="color: #fff;">Separated:</strong> dy / g(y) = h(t) dt</p>
              <p><strong style="color: #fff;">Integration:</strong> ∫ dy / g(y) = ∫ h(t) dt + C</p>
              <p style="margin-top: 8px; color: var(--amber);">Notice that constant C can be expressed in convenient forms like ln C₁ to simplify exponential extraction.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 4: Newton's Cooling Physical Intuition -->
      <div class="slide" data-title="Newton's Law: Physical Intuition" data-notes="Explain why dT/dt is proportional to (T - Ts). When T > Ts, body cools. Point out that the curve approaches Ts asymptotically and never crosses it.">
        <div class="slide-top">
          <div><div class="meta">Thermal Physics // Newton's Law of Cooling</div><h1>Physical Intuition & The Cooling Law</h1></div>
          <div class="slide-num">04 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/NewtonCoolingPrototype.mp4" poster="frames/NewtonCoolingPrototype.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">THERMAL DRIVING FORCE</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Governing Law:</strong> dT/dt = -k(T - Ts)</p>
              <p><strong style="color: #fff;">Driving Potential:</strong> Temperature gap (T - Ts) drives the heat transfer rate.</p>
              <p><strong style="color: #fff;">Asymptotic Approach:</strong> As T approaches Ts, dT/dt → 0. The ambient air temperature Ts = 10°F is an unreachable lower asymptote under pure conduction/convection.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 5: Newton's Cooling Analytical Derivation -->
      <div class="slide" data-title="Newton's Law: Analytical Derivation" data-notes="Step through each line of the derivation. Emphasize how initial condition evaluates C1 as the initial temperature difference (T0 - Ts).">
        <div class="slide-top">
          <div><div class="meta">Mathematical Derivation // Equation Morphing</div><h1>Continuous Derivation: Newton's Law of Cooling</h1></div>
          <div class="slide-num">05 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene04_NewtonCoolingLaw.mp4" poster="frames/Scene04_NewtonCoolingLaw.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">STEP-BY-STEP DERIVATION</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--text);">
              <p>1. dT / (T - Ts) = -k dt</p>
              <p>2. ln(T - Ts) = -kt + ln C₁</p>
              <p>3. T - Ts = C₁ e^(-kt)</p>
              <p>4. At t = 0, T = T₀ ⟹ C₁ = T₀ - Ts</p>
              <p style="margin-top: 6px; color: var(--green); font-weight: 700;">⟹ T(t) = Ts + (T₀ - Ts) e^(-kt)</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 6: Mathalino Problem 01 Setup -->
      <div class="slide" data-title="Mathalino Problem 01: Thermometer Reading" data-notes="State MATHalino Problem 01 data: Inside at 70°F, outside at 10°F. After 3 min, T = 25°F. What is reading after 6 min? Ask class to deduce e^(-3k) = 1/4.">
        <div class="slide-top">
          <div><div class="meta">MATHalino Problem 01 // Heat Transfer</div><h1>Thermometer Reading After 6 Minutes of Being Outside</h1></div>
          <div class="slide-num">06 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene05_CoolingProblem1_Thermometer6Min.mp4" poster="frames/Scene05_CoolingProblem1_Thermometer6Min.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">GIVEN DATA & PARAMETER MATCHING</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--muted);">
              <p>• Initial inside reading: <strong style="color: #fff;">T₀ = 70°F</strong></p>
              <p>• Outside air temperature: <strong style="color: var(--cyan);">Ts = 10°F</strong></p>
              <p>• Intermediate reading at 3 min: <strong style="color: #fff;">T(3) = 25°F</strong></p>
              <p>• Required: <strong style="color: var(--green);">Thermometer reading at t = 6 min</strong></p>
              <div style="margin-top: 10px; padding: 8px; background: rgba(245, 158, 11, 0.1); border-radius: 6px;">
                <span style="color: var(--amber); font-weight: 700;">Model: T(t) = 10 + 60 e^(-kt)</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 7: Problem 01 Exact Resolution -->
      <div class="slide" data-title="Problem 01 Resolution & Ratio Insight" data-notes="Demonstrate the constant ratio drop over equal 3-minute intervals. 60 -> 15 -> 3.75. Final T = 10 + 3.75 = 13.75°F. Verified against MATHalino.">
        <div class="slide-top">
          <div><div class="meta">Solution Key // Ratio Invariance</div><h1>Problem 01 Resolution & Interval Ratio Invariance</h1></div>
          <div class="slide-num">07 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container">
            <img src="frames/Scene05_CoolingProblem1_Thermometer6Min.png" alt="Cooling Problem 1 Resolution">
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">ANALYTICAL RESOLUTION</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--text);">
              <p>1. At t = 3: 25 = 10 + 60 e^(-3k) ⟹ 15/60 = 1/4 = e^(-3k)</p>
              <p>2. Model base: T(t) = 10 + 60 (1/4)^(t/3)</p>
              <p>3. At t = 6: T(6) = 10 + 60 (1/4)^2 = 10 + 3.75</p>
              <p style="margin-top: 10px; color: var(--green); font-size: 16px; font-weight: 800;">🏆 T(6) = 13.75°F</p>
              <p style="margin-top: 6px; color: var(--muted); font-size: 11.5px;">Physical Ratio Insight: In every 3-minute window, the excess temperature drops by exactly 75% (remaining 1/4).</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 8: Mathalino Problem 02 Setup -->
      <div class="slide" data-title="Mathalino Problem 02: Half Degree Drop" data-notes="Present MATHalino Problem 02 data: T0 = 75°F, Ts = 20°F, T(4) = 30°F. Target: within 0.5° of air ⟹ T = 20.5°F.">
        <div class="slide-top">
          <div><div class="meta">MATHalino Problem 02 // Transcendental Solution</div><h1>Time to Drop Within Half Degree of Air Temperature</h1></div>
          <div class="slide-num">08 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene06_CoolingProblem2_HalfDegree.mp4" poster="frames/Scene06_CoolingProblem2_HalfDegree.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">PROBLEM CONDITIONS</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--muted);">
              <p>• Initial reading: <strong style="color: #fff;">T₀ = 75°F</strong></p>
              <p>• Ambient air: <strong style="color: var(--cyan);">Ts = 20°F</strong></p>
              <p>• At 4 minutes: <strong style="color: #fff;">T(4) = 30°F</strong></p>
              <p>• Target: <strong style="color: var(--amber);">Within 0.5°F of Ts ⟹ T = 20.5°F</strong></p>
              <p style="margin-top: 8px; color: #fff;">Model: T(t) = 20 + 55 e^(-kt)</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 9: Problem 02 Logarithmic Resolution -->
      <div class="slide" data-title="Problem 02 Logarithmic Resolution" data-notes="Show how ln(1/110) = -ln 110 and ln(2/11) = ln 2 - ln 11 cancel negative signs to yield t ≈ 11.029 minutes.">
        <div class="slide-top">
          <div><div class="meta">Logarithmic Resolution // Exact Calculation</div><h1>Problem 02 Resolution & Logarithmic Solution</h1></div>
          <div class="slide-num">09 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container">
            <img src="frames/Scene06_CoolingProblem2_HalfDegree.png" alt="Cooling Problem 2 Resolution">
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">EXACT LOGARITHMIC DERIVATION</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--text);">
              <p>1. At t = 4: 30 = 20 + 55 e^(-4k) ⟹ e^(-4k) = 10/55 = 2/11</p>
              <p>2. Model: T(t) = 20 + 55 (2/11)^(t/4)</p>
              <p>3. Set T = 20.5: 0.5 = 55 (2/11)^(t/4) ⟹ 1/110 = (2/11)^(t/4)</p>
              <p>4. t = 4 ln(1/110) / ln(2/11)</p>
              <p style="margin-top: 10px; color: var(--green); font-size: 16px; font-weight: 800;">⏱ t ≈ 11.029 minutes</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 10: Live Whiteboard -->
      <div class="slide" data-title="Thermal Modeling Live Whiteboard" data-notes="Use this slide as a live whiteboard with Apple Pencil. Ask students what happens when an object is colder than ambient (heating problem).">
        <div class="slide-top">
          <div><div class="meta">Live Teaching Pause // Apple Pencil Inking</div><h1>Thermal Modeling Live Derivation Board</h1></div>
          <div class="slide-num">10 / 21</div>
        </div>
        <div class="slide-body grid-full">
          <div class="card cyan-border" style="background: rgba(15, 23, 42, 0.4); border: 2px dashed rgba(56, 189, 248, 0.5); justify-content: center; align-items: center; text-align: center;">
            <h2 style="color: var(--cyan); margin-bottom: 10px;"> Apple Pencil Live Teaching Canvas</h2>
            <p style="color: var(--muted); max-width: 650px; font-size: 14px; line-height: 1.6;">
              This slide is equipped with high-resolution vector inking and zero background drag. Use your Apple Pencil to sketch warming scenarios (T₀ &lt; Ts) or work through student-generated variations.
            </p>
            <div style="margin-top: 20px; display: flex; gap: 12px;">
              <span style="font-size: 12px; color: var(--amber); background: rgba(245, 158, 11, 0.15); padding: 6px 12px; border-radius: 6px; font-weight: 700;">Try: dT/dt = -k(T - 85) with T₀ = 40°F</span>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 11: Chemical Conversion & Decay -->
      <div class="slide" data-title="Chemical Conversion & Decay" data-notes="Introduce simple chemical conversion and radioactive decay: dx/dt = -kx. The negative sign represents continuous dissipation of reactant.">
        <div class="slide-top">
          <div><div class="meta">Chemical Kinetics // Nuclear Decay</div><h1>Simple Chemical Conversion & Radioactive Decay</h1></div>
          <div class="slide-num">11 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene07_ChemicalConversion_Decay.mp4" poster="frames/Scene07_ChemicalConversion_Decay.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">FIRST-ORDER DECAY MODEL</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Physical Law:</strong> Rate of change of unconverted substance is proportional to the unconverted amount present.</p>
              <p><strong style="color: #fff;">Equation:</strong> dx/dt = -kx (k &gt; 0)</p>
              <p><strong style="color: #fff;">Separated:</strong> dx / x = -k dt ⟹ ln x = -kt + C</p>
              <p><strong style="color: var(--green);">Solution:</strong> x(t) = x₀ e^(-kt)</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 12: Stochastic Atoms vs Continuum Calculus -->
      <div class="slide" data-title="Stochastic Atoms vs Continuum Calculus" data-notes="Discuss the bridge between discrete quantum decay and macroscopic deterministic ODEs. Law of Large Numbers makes the exponential model exact.">
        <div class="slide-top">
          <div><div class="meta">Physical Foundation // Particle Kinetics</div><h1>Stochastic Atoms vs Continuum Calculus</h1></div>
          <div class="slide-num">12 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/RadioactiveDecayPrototype.mp4" poster="frames/RadioactiveDecayPrototype.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">THE LAW OF LARGE NUMBERS</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Individual Particles:</strong> Each nucleus decays independently with constant probability per unit time.</p>
              <p><strong style="color: #fff;">Macroscopic Ensemble:</strong> With ~10²³ atoms, individual randomness averages out into a deterministic continuous curve x(t) = x₀ e^(-kt).</p>
              <p><strong style="color: var(--amber);">Half-Life:</strong> The time required for 50% of the sample to transform is strictly constant regardless of initial mass.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 13: Radium Problem 01 Setup -->
      <div class="slide" data-title="Mathalino Decay 01: Radium Half-Life" data-notes="Present MATHalino Radium Problem 01: 1.1% decomposes in 25 years. Remind students that 1.1% decomposed means 98.9% remains!">
        <div class="slide-top">
          <div><div class="meta">MATHalino Problem 01 // Nuclear Decay</div><h1>Radium Decomposition & Half-Life Determination</h1></div>
          <div class="slide-num">13 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene08_RadiumProblem1_HalfLife.mp4" poster="frames/Scene08_RadiumProblem1_HalfLife.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">GIVEN CONDITIONS</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--muted);">
              <p>• In 25 years, approximately <strong style="color: var(--coral);">1.1%</strong> of radium decomposes.</p>
              <p>• Remaining fraction: <strong style="color: #fff;">x(25) = (100% - 1.1%)x₀ = 0.989 x₀</strong></p>
              <p>• Required: <strong style="color: var(--green);">Time for one-half of original amount to decompose (x = 0.5 x₀)</strong></p>
              <p style="margin-top: 8px; color: var(--cyan);">Model: x(t) = x₀ (0.989)^(t/25)</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 14: Radium Problem 01 Resolution -->
      <div class="slide" data-title="Radium Half-Life Resolution" data-notes="Solve for t = 25 ln(0.5) / ln(0.989) ≈ 1566.65 years. Emphasize how a 25-year sample accurately calibrates a multi-millennium geological clock.">
        <div class="slide-top">
          <div><div class="meta">Solution Key // Century-Scale Half-Life</div><h1>Radium Half-Life Analytical Resolution</h1></div>
          <div class="slide-num">14 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container">
            <img src="frames/Scene08_RadiumProblem1_HalfLife.png" alt="Radium Problem Resolution">
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">LOGARITHMIC RESOLUTION</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--text);">
              <p>1. At t = 25: 0.989 x₀ = x₀ e^(-25k) ⟹ e^(-k) = (0.989)^(1/25)</p>
              <p>2. Set x = 0.5 x₀: 0.5 = (0.989)^(t/25) ⟹ 0.5^25 = 0.989^t</p>
              <p>3. t = 25 ln(0.5) / ln(0.989) = 25(-0.69315) / (-0.01106)</p>
              <p style="margin-top: 10px; color: var(--green); font-size: 16px; font-weight: 800;">🏆 t ≈ 1,566.65 years</p>
              <p style="margin-top: 6px; color: var(--muted); font-size: 11.5px;">Verified against MATHalino official engineering solution.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 15: Decay Problem 02 Setup -->
      <div class="slide" data-title="Mathalino Decay 02: 90% Dissipation" data-notes="Present MATHalino Problem 02: Half-life = 38 hours. When 90% is dissipated, exactly 10% (0.1 x0) remains!">
        <div class="slide-top">
          <div><div class="meta">MATHalino Problem 02 // Threshold Dissipation</div><h1>Time to Dissipate 90% of a Radioactive Substance</h1></div>
          <div class="slide-num">15 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene09_DecayProblem2_90Percent.mp4" poster="frames/Scene09_DecayProblem2_90Percent.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">GIVEN CONDITIONS</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--muted);">
              <p>• Half-life: <strong style="color: var(--green);">t₁/₂ = 38 hours</strong></p>
              <p>• Dissipation target: <strong style="color: var(--amber);">90% dissipated ⟹ 10% remaining</strong></p>
              <p>• Target equation: <strong style="color: #fff;">0.10 x₀ = x₀ (0.5)^(t/38)</strong></p>
              <p style="margin-top: 8px; color: var(--amber);">Question: How many half-lives does this represent?</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 16: Decay Problem 02 Resolution -->
      <div class="slide" data-title="Problem 02 Threshold Resolution" data-notes="Solve for t = 38 ln(0.1) / ln(0.5) ≈ 126.23 hours. Notice 3 half-lives (114 hr) leaves 12.5%, so 126.23 hr is physically sound.">
        <div class="slide-top">
          <div><div class="meta">Solution Key // Milestone Verification</div><h1>Problem 02 Threshold Resolution & Milestone Check</h1></div>
          <div class="slide-num">16 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container">
            <img src="frames/Scene09_DecayProblem2_90Percent.png" alt="Decay Problem 2 Resolution">
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">ANALYTICAL RESOLUTION</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--text);">
              <p>1. Model: x(t) = x₀ (0.5)^(t/38)</p>
              <p>2. Set x = 0.10 x₀: 0.10 = (0.5)^(t/38)</p>
              <p>3. t = 38 ln(0.10) / ln(0.50) = 38(-2.3026) / (-0.6931)</p>
              <p style="margin-top: 10px; color: var(--green); font-size: 16px; font-weight: 800;">⏱ t ≈ 126.23 hours</p>
              <p style="margin-top: 6px; color: var(--muted); font-size: 11.5px;">Milestone Check: 1 HL (38h) = 50%, 2 HL (76h) = 25%, 3 HL (114h) = 12.5%, 3.32 HL (126.2h) = 10%.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 17: Escape Velocity Extension -->
      <div class="slide" data-title="Escape Velocity from Earth" data-notes="Transition to MATHalino index engineering application: Velocity of Escape from Earth. Explain variable gravity and the chain rule a = v dv/dr.">
        <div class="slide-top">
          <div><div class="meta">Engineering Physics // Spaceflight Kinematics</div><h1>Velocity of Escape from Earth (MATHalino Index)</h1></div>
          <div class="slide-num">17 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene10_EscapeVelocity.mp4" poster="frames/Scene10_EscapeVelocity.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">VARIABLE GRAVITATIONAL ACCELERATION</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Newtonian Gravity:</strong> F = -m g R² / r²</p>
              <p><strong style="color: #fff;">Kinematic Chain Rule:</strong> a = dv/dt = (dv/dr)(dr/dt) = v (dv/dr)</p>
              <p><strong style="color: #fff;">Separated DE:</strong> v dv = -g R² r^(-2) dr</p>
              <p style="margin-top: 8px; color: var(--amber);">Notice this models escape from a planetary potential well using basic separation of variables!</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 18: Escape Velocity Analytical Resolution -->
      <div class="slide" data-title="Escape Velocity Resolution" data-notes="Integrate to infinity to derive v_esc = sqrt(2gR) ≈ 11.18 km/s (6.95 mi/s). Explain connection to mechanical energy conservation.">
        <div class="slide-top">
          <div><div class="meta">Solution Key // Planetary Mechanics</div><h1>Escape Velocity Analytical Resolution</h1></div>
          <div class="slide-num">18 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container">
            <img src="frames/Scene10_EscapeVelocity.png" alt="Escape Velocity Resolution">
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">INTEGRATION TO INFINITY</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--text);">
              <p>1. ∫ v dv = -g R² ∫ r^(-2) dr ⟹ (1/2)v² = g R² / r + C</p>
              <p>2. At r ➔ ∞, v ≥ 0 ⟹ C ≥ 0</p>
              <p>3. At surface r = R: (1/2) v_esc² = g R</p>
              <p style="margin-top: 10px; color: var(--green); font-size: 16px; font-weight: 800;">🚀 v_esc = √(2gR) ≈ 11.18 km/s (6.95 mi/s)</p>
              <p style="margin-top: 6px; color: var(--muted); font-size: 11.5px;">Approx. 25,000 mph. Derived strictly from first-order differential equations.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 19: Comparative Synthesis -->
      <div class="slide" data-title="Comparative Modeling Matrix" data-notes="Summarize all 3 models side-by-side. Highlight the unity of first-order differential equations across physical systems.">
        <div class="slide-top">
          <div><div class="meta">Comparative Synthesis // Engineering Matrix</div><h1>Master Comparative Modeling Matrix</h1></div>
          <div class="slide-num">19 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="video-container" onclick="toggleVideoPlayback(this)">
            <video src="videos/Scene11_SynthesisComparison.mp4" poster="frames/Scene11_SynthesisComparison.png" loop playsinline></video>
            <div class="play-pause-indicator">Playing (Tap to Pause)</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">UNIFIED MATHEMATICAL STRUCTURE</h3>
            <div style="font-size: 12px; line-height: 1.6; color: var(--muted);">
              <p>• <strong style="color: var(--cyan);">Cooling:</strong> dT/dt = -k(T - Ts) ⟹ Thermal Asymptote</p>
              <p>• <strong style="color: var(--green);">Decay:</strong> dx/dt = -kx ⟹ Invariant Half-Life Dissipation</p>
              <p>• <strong style="color: var(--amber);">Escape:</strong> v dv/dr = -gR²/r² ⟹ Potential Well Escape</p>
              <p style="margin-top: 10px; color: #fff;">Every model relies on translating empirical rates into separable differential forms.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 20: Summary & Live Q&A -->
      <div class="slide" data-title="Lecture Summary & Live Q&A" data-notes="Review examination tips: always verify remaining fraction vs dissipated fraction, check units, and test asymptotic endpoints.">
        <div class="slide-top">
          <div><div class="meta">Review & Discussion // Apple Pencil Board</div><h1>Lecture Summary & Examination Review</h1></div>
          <div class="slide-num">20 / 21</div>
        </div>
        <div class="slide-body grid-full">
          <div class="card cyan-border" style="padding: 24px;">
            <h3 style="color: var(--cyan); margin-bottom: 12px;">ENGINEERING TAKEAWAYS & CHECKLIST</h3>
            <div style="font-size: 13.5px; line-height: 1.7; color: var(--text);">
              <p>1. <strong style="color: var(--amber);">Sign of Rate Constant:</strong> Decay systems must carry a negative sign; verify that k &gt; 0.</p>
              <p>2. <strong style="color: var(--amber);">Remaining vs Dissipated:</strong> If a problem states '90% dissipated', the ODE operates on the 10% remaining.</p>
              <p>3. <strong style="color: var(--amber);">Asymptotic Limits:</strong> Physical bounds prevent cooling below ambient Ts under pure convection.</p>
              <p>4. <strong style="color: var(--amber);">Logarithmic Algebra:</strong> ln(A/B) = ln A - ln B; negative terms naturally cancel in positive physical durations.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 21: References & Acknowledgements -->
      <div class="slide" data-title="References & Acknowledgements" data-notes="Credit MATHalino Reviewer for primary problem data, Stewart Calculus, and Boyce & DiPrima ODEs.">
        <div class="slide-top">
          <div><div class="meta">Curriculum Bibliography // Academic Citations</div><h1>Curriculum References & Academic Acknowledgements</h1></div>
          <div class="slide-num">21 / 21</div>
        </div>
        <div class="slide-body grid-equal">
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">PRIMARY SOURCE: MATHALINO</h3>
            <p style="color: var(--muted); font-size: 12.5px; line-height: 1.5; margin-bottom: 12px;">
              All authentic engineering problems and numerical values in this lecture are curated from MATHalino Engineering Review:
            </p>
            <div style="font-size: 12px; line-height: 1.6; color: var(--text);">
              <p>• <a href="https://mathalino.com/reviewer/applications" target="_blank" style="color: var(--cyan); text-decoration: underline;">Elementary Applications Index</a></p>
              <p>• <a href="https://mathalino.com/reviewer/elementary-differential-equations/newton-s-law-cooling" target="_blank" style="color: var(--cyan); text-decoration: underline;">Newton's Law of Cooling</a></p>
              <p>• <a href="https://mathalino.com/reviewer/elementary-differential-equations/theremometer-reading-after-6-minutes-being-outside" target="_blank" style="color: var(--cyan); text-decoration: underline;">Cooling Problem 01: Thermometer Reading After 6 Min</a></p>
              <p>• <a href="https://mathalino.com/reviewer/elementary-differential-equations/02-time-thermometer-reading-drop-within-half-degree-air" target="_blank" style="color: var(--cyan); text-decoration: underline;">Cooling Problem 02: Drop to Within Half Degree of Air</a></p>
              <p>• <a href="https://mathalino.com/reviewer/elementary-differential-equations/simple-chemical-conversion" target="_blank" style="color: var(--cyan); text-decoration: underline;">Simple Chemical Conversion</a></p>
              <p>• <a href="https://mathalino.com/reviewer/elementary-differential-equations/01-half-life-decomposing-radium" target="_blank" style="color: var(--cyan); text-decoration: underline;">Decay Problem 01: Radium Half-Life</a></p>
              <p>• <a href="https://mathalino.com/reviewer/elementary-differential-equations/02-time-dissipite-90-certain-radioactive-substance" target="_blank" style="color: var(--cyan); text-decoration: underline;">Decay Problem 02: 90% Dissipation of Radioactivity</a></p>
            </div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">CALCULUS TEXTS & ANIMATION FOUNDATIONS</h3>
            <div style="font-size: 12.5px; line-height: 1.6; color: var(--muted);">
              <p><strong style="color: #fff;">Boyce & DiPrima, Elementary Differential Equations</strong><br>
              Separable equations, initial value problems, and exponential growth/decay kinetics.</p>
              <p style="margin-top: 10px;"><strong style="color: #fff;">James Stewart, Calculus: Early Transcendentals (9th Ed.)</strong><br>
              Thermal conduction and differential modeling foundations.</p>
              <p style="margin-top: 10px;"><strong style="color: #fff;">3Blue1Brown (Grant Sanderson), Essence of Calculus</strong><br>
              Visual storytelling and continuous mathematical transformations.</p>
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
    <span id="slideIndicator" style="font-weight: 600; color: var(--muted); min-width: 90px; text-align: center;">01 / 21</span>
    <button id="nextBtn">Next ▶</button>
  </footer>

  <div class="toast" id="toast">Feedback Toast</div>

  <script>
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;
    const progressFill = document.getElementById('progressFill');
    const slideIndicator = document.getElementById('slideIndicator');
    const teleprompter = document.getElementById('teleprompter');
    const notesContent = document.getElementById('notesContent');
    const sceneNav = document.getElementById('sceneNav');
    const stageContainer = document.getElementById('stageContainer');
    const toast = document.getElementById('toast');

    function showToast(msg) {
      if (!toast) return;
      toast.textContent = msg;
      toast.style.opacity = '1';
      toast.style.transform = 'translateX(-50%) translateY(0)';
      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(-50%) translateY(-10px)';
      }, 1400);
    }

    function playSlideVideo(slideEl) {
      const vid = slideEl.querySelector('video');
      if (vid) {
        vid.currentTime = 0;
        const playPromise = vid.play();
        if (playPromise !== undefined) {
          playPromise.catch(() => {});
        }
      }
    }

    function pauseSlideVideo(slideEl) {
      const vid = slideEl.querySelector('video');
      if (vid) vid.pause();
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

    // Per-Slide Inking Persistence
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

      saveCurrentSlideInk();
      undoStack = [];
      redoStack = [];
      updateHistoryButtons();

      pauseSlideVideo(slides[currentSlide]);
      slides[currentSlide].classList.remove('active');

      currentSlide = index;

      const newSlide = slides[currentSlide];
      newSlide.classList.add('active');

      restoreSlideInk(currentSlide);

      progressFill.style.width = `${((currentSlide + 1) / slides.length) * 100}%`;
      slideIndicator.textContent = `${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;

      sceneNav.value = String(currentSlide);

      const notes = newSlide.getAttribute('data-notes');
      if (notes) {
        notesContent.textContent = notes;
      } else {
        notesContent.textContent = `Slide ${currentSlide + 1}: ${newSlide.getAttribute('data-title') || ''}`;
      }

      playSlideVideo(newSlide);
    }

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
    let currentTool = 'pen';
    let currentColor = '#007AFF';
    let currentStrokeSize = 3.0;
    let palmRejectionEnabled = true;

    let undoStack = [];
    let redoStack = [];
    const MAX_HISTORY = 20;

    let canvasDisplayWidth = 1360;
    let canvasDisplayHeight = 765;
    let lastPoint = null;

    function resizeCanvas() {
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

    document.addEventListener('pointerdown', (e) => {
      if (pkSizePopover && !pkSizePopover.classList.contains('hidden')) {
        if (!e.target.closest('#pkSizePopover') && !e.target.closest('#pkSizeBtn') && !e.target.closest('.pk-tool')) {
          toggleSizePopover(false);
        }
      }
    });

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
      } else {
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
    // Slide Zoom & Pinch-Zoom Engine
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
        panX = 0; panY = 0; currentZoom = 1.0;
      } else {
        const maxPanX = ((currentZoom - 1) * (canvasDisplayWidth || 1360) * 0.45) / currentZoom;
        const maxPanY = ((currentZoom - 1) * (canvasDisplayHeight || 765) * 0.45) / currentZoom;
        panX = Math.max(-maxPanX, Math.min(maxPanX, panX));
        panY = Math.max(-maxPanY, Math.min(maxPanY, panY));
      }
      stageContainer.style.transform = `scale(${currentZoom}) translate(${panX}px, ${panY}px)`;
      const zoomResetBtn = document.getElementById('zoomResetBtn');
      if (zoomResetBtn) {
        zoomResetBtn.textContent = `${Math.round(currentZoom * 100)}%`;
        zoomResetBtn.style.color = currentZoom > 1.05 ? 'var(--cyan)' : 'var(--text)';
      }
      const pkZoomResetBtn = document.getElementById('pkZoomResetBtn');
      if (pkZoomResetBtn) {
        pkZoomResetBtn.textContent = `${Math.round(currentZoom * 100)}%`;
        pkZoomResetBtn.style.color = currentZoom > 1.05 ? '#0284C7' : '#475569';
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
      return Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
    }

    stageContainer.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches.length === 2) {
        isPinching = true;
        stageContainer.style.transition = 'none';
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
          const targetZoom = initialZoom * (dist / initialPinchDistance);
          const midX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
          const midY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
          panX += (midX - pinchMidX) * 0.7;
          panY += (midY - pinchMidY) * 0.7;
          pinchMidX = midX; pinchMidY = midY;
          applyZoom(targetZoom);
        }
        e.preventDefault();
      }
    }, { passive: false });

    stageContainer.addEventListener('touchend', (e) => {
      if (!e.touches || e.touches.length < 2) {
        isPinching = false;
        initialPinchDistance = null;
        stageContainer.style.transition = 'transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)';
      }
    });

    // ==========================================
    // Multi-Tap Hotkeys
    // Zoomed in: Double-Tap ZOOMS OUT to 100%!
    // At 100%: Double-Tap advances, Triple-Tap goes back!
    // ==========================================
    let tapCount = 0;
    let tapTimeout = null;
    const TAP_THRESHOLD_MS = 280;

    function processTapGesture(target) {
      if (target.closest('header') || target.closest('#pencilKitToolbar') || target.closest('button') || target.closest('select')) {
        return;
      }
      tapCount++;
      if (tapTimeout) clearTimeout(tapTimeout);

      if (tapCount === 3) {
        showSlide(currentSlide - 1);
        showToast(`⏮ Slide ${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')} (Triple Tap)`);
        tapCount = 0;
        return;
      }

      tapTimeout = setTimeout(() => {
        if (tapCount === 2) {
          if (currentZoom > 1.05) {
            resetZoom();
            showToast('🔍 Zoom Reset (100%)');
          } else {
            showSlide(currentSlide + 1);
            showToast(`⏭ Slide ${String(currentSlide + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')} (Double Tap)`);
          }
        }
        tapCount = 0;
      }, TAP_THRESHOLD_MS);
    }

    let touchStartX = 0, touchStartY = 0, touchStartTime = 0;
    const TAP_MOVE_LIMIT = 10;

    stageContainer.addEventListener('touchstart', (e) => {
      if (e.touches && e.touches.length === 1) {
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
        touchStartTime = Date.now();
      }
    }, { passive: true });

    stageContainer.addEventListener('touchend', (e) => {
      if (e.changedTouches && e.changedTouches.length === 1 && !isPinching) {
        const dx = Math.abs(e.changedTouches[0].clientX - touchStartX);
        const dy = Math.abs(e.changedTouches[0].clientY - touchStartY);
        const dt = Date.now() - touchStartTime;
        if (dx < TAP_MOVE_LIMIT && dy < TAP_MOVE_LIMIT && dt < 320) {
          if (!isDrawingMode || (e.changedTouches[0].touchType !== 'stylus')) {
            processTapGesture(e.target);
          }
        }
      }
    }, { passive: true });

    if (typeof setStrokeSize === 'function') setStrokeSize(3.0);
    if (typeof updatePreviewColors === 'function') updatePreviewColors();

    showSlide(0);
  </script>
</body>
</html>
"""

def main():
    targets = [
        "differential_equations.html",
        "public/differential_equations.html",
        "presentation/de_player.html",
    ]
    for t in targets:
        with open(t, "w", encoding="utf-8") as f:
            f.write(DE_HTML_TEMPLATE)
        print(f"Updated interactive DE player: {t}")

if __name__ == "__main__":
    main()
