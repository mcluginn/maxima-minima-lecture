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
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
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
    body {
      background-color: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      overflow: hidden;
      height: 100vh;
      display: flex;
      flex-direction: column;
      user-select: none;
      -webkit-user-select: none;
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
    }

    /* Seamless Keynote-Style Slide Crossfade */
    .slide {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      padding: 24px 36px;
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transform: scale(0.99);
      transition: opacity 0.4s cubic-bezier(0.4, 0, 0.2, 1), transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 10;
    }
    .slide.active {
      opacity: 1;
      pointer-events: auto;
      transform: scale(1.0);
      z-index: 20;
    }

    .slide-top {
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      border-bottom: 1px solid rgba(51, 65, 85, 0.35);
      padding-bottom: 8px;
    }
    .slide-top .meta { font-size: 11px; font-weight: 700; color: var(--cyan); text-transform: uppercase; letter-spacing: 1.5px; }
    .slide-top h1 { font-size: 23px; font-weight: 700; color: #fff; margin-top: 3px; letter-spacing: -0.2px; }
    .slide-top .slide-num { font-size: 13px; color: var(--muted); font-weight: 600; font-variant-numeric: tabular-nums; }

    .slide-body {
      flex: 1;
      display: grid;
      gap: 20px;
      overflow: hidden;
    }
    .grid-video { grid-template-columns: 1.85fr 1fr; }
    .grid-master { grid-template-columns: 2.2fr 1fr; }
    .grid-annotate { grid-template-columns: 1fr 1fr; }
    .grid-equal { grid-template-columns: 1fr 1fr; }
    .grid-full { grid-template-columns: 1fr; }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 20px;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      backdrop-filter: blur(8px);
    }
    .card.cyan-border { border-color: rgba(56, 189, 248, 0.45); }
    .card.amber-border { border-color: rgba(245, 158, 11, 0.45); }
    .card.coral-border { border-color: rgba(244, 63, 94, 0.45); }
    .card.green-border { border-color: rgba(34, 197, 94, 0.45); }

    /* Seamless Edge-to-Edge Video Canvas: ZERO UGLY BORDERS */
    .seamless-video-canvas {
      position: relative;
      width: 100%;
      height: 100%;
      background: #0B0F19;
      border-radius: 8px;
      overflow: hidden;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .seamless-video-canvas video {
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #0B0F19;
      pointer-events: none; /* Allows click-to-pause on container */
    }
    .play-pause-indicator {
      position: absolute;
      top: 14px;
      right: 14px;
      background: rgba(11, 15, 25, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 20px;
      padding: 4px 10px;
      font-size: 11px;
      color: var(--muted);
      backdrop-filter: blur(8px);
      opacity: 0;
      transition: opacity 0.25s ease;
      pointer-events: none;
    }
    .seamless-video-canvas:hover .play-pause-indicator { opacity: 1; }

    img.frame-ref { width: 100%; height: 100%; object-fit: contain; border-radius: 8px; }

    /* Apple Pencil Drawing Canvas Overlay */
    #pencilCanvas {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 50;
    }
    #pencilCanvas.drawing-active { pointer-events: auto; cursor: crosshair; }

    /* Teleprompter Drawer */
    .teleprompter {
      position: absolute;
      bottom: 56px;
      right: 16px;
      width: 380px;
      max-height: 280px;
      background: rgba(19, 27, 46, 0.95);
      border: 1px solid var(--cyan);
      border-radius: 10px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.7);
      padding: 16px;
      z-index: 90;
      backdrop-filter: blur(12px);
      display: none;
      overflow-y: auto;
      font-size: 13px;
      line-height: 1.5;
    }
    .teleprompter h4 { color: var(--amber); margin-bottom: 8px; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; }

    .color-dot {
      width: 17px;
      height: 17px;
      border-radius: 50%;
      cursor: pointer;
      border: 2px solid transparent;
      transition: transform 0.15s ease;
    }
    .color-dot.active { transform: scale(1.25); border-color: #fff; }

    /* Footer Navigation */
    footer {
      height: 46px;
      background: rgba(11, 15, 25, 0.9);
      border-top: 1px solid rgba(51, 65, 85, 0.4);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      font-size: 13px;
    }
    .progress-bar {
      flex: 1;
      height: 4px;
      background: rgba(30, 41, 59, 0.8);
      margin: 0 20px;
      border-radius: 2px;
      overflow: hidden;
    }
    .progress-fill { height: 100%; background: var(--cyan); width: 0%; transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <span class="badge">Seamless Mode</span>
      <span>Calculus: Maxima & Minima</span>
    </div>

    <div class="controls">
      <!-- Quick Scene Dropdown -->
      <select id="sceneNav" title="Jump to any scene">
        <option value="0">01. Title & Overview</option>
        <option value="1">02. 4-Phase Roadmap</option>
        <option value="2">03. 🎬 Scene 1: Terrain Hook</option>
        <option value="3">04. ✍️ Scene 1: Terrain Slope Workspace</option>
        <option value="4">05. 🎬 Scene 2: Local vs Absolute Extrema</option>
        <option value="5">06. ✍️ Scene 2: Neighborhood Test Workspace</option>
        <option value="6">07. 🌟 MASTER SEQUENCE (Full Continuous Story)</option>
        <option value="7">08. 🎬 Scene 7: The Cubic Curve Landscape</option>
        <option value="8">09. 🎬 Scene 8: Dynamic Tangent Telemetry</option>
        <option value="9">10. ✍️ Scene 8: Power Rule Derivation Workspace</option>
        <option value="10">11. 🎬 Scene 10: Singularities (Corners & Cusps)</option>
        <option value="11">12. ✍️ Scene 10: Singularity Limits DNE Workspace</option>
        <option value="12">13. 🎬 Scene 12: Critical Trap g(x)=x³ Terrace</option>
        <option value="13">14. ✍️ Scene 12: Necessary vs Sufficient Workspace</option>
        <option value="14">15. 🎬 Scene 14: Equation Factoring Morph</option>
        <option value="15">16. 🎬 Scene 15: First Derivative Sign Chart</option>
        <option value="16">17. ✍️ Scene 16: Sign Chart Table Workspace</option>
        <option value="17">18. 🎬 Scene 17: Extrema Coordinates Reveal</option>
        <option value="18">19. 🎬 Scene 18: Second Derivative Concavity</option>
        <option value="19">20. ⚖️ 1st vs 2nd Test Comparison Matrix</option>
        <option value="20">21. 🎬 Scene 21: Closed Interval EVT</option>
        <option value="21">22. 🎬 Scene 22: Max Power Transfer Circuit</option>
        <option value="22">23. 🎯 Active Challenge & Exit Ticket</option>
        <option value="23">24. 📐 Mathalino 1: Number Exceeding Square</option>
        <option value="24">25. 📐 Mathalino 10: Riverbank Fencing</option>
        <option value="25">26. 📐 Mathalino 16: Open-Top Box Fold</option>
        <option value="26">27. 📐 Mathalino 03: Tour Bus Maximum Revenue</option>
        <option value="27">28. 📐 Mathalino 42: Trapezoidal Gutter Capacity</option>
      </select>

      <div style="display: flex; align-items: center; gap: 6px;">
        <button id="drawBtn" title="Toggle Apple Pencil Inking">✍️ Draw</button>
        <div class="color-dot active" style="background: #38BDF8;" data-color="#38BDF8" title="Cyan"></div>
        <div class="color-dot" style="background: #F59E0B;" data-color="#F59E0B" title="Amber"></div>
        <div class="color-dot" style="background: #F43F5E;" data-color="#F43F5E" title="Coral"></div>
        <div class="color-dot" style="background: #FFFFFF;" data-color="#FFFFFF" title="White"></div>
        <button id="clearInkBtn" class="danger" title="Clear Ink">Clear</button>
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

      <!-- SLIDE 1: Title -->
      <div class="slide active" data-title="Title Slide">
        <div class="slide-top">
          <div class="meta">Differential Calculus for Engineering</div>
          <div class="slide-num">Slide 01 / 28</div>
        </div>
        <div class="slide-body grid-full">
          <div class="card cyan-border" style="justify-content: center; align-items: center; text-align: center; padding: 40px;">
            <div style="font-size: 13px; font-weight: 700; color: var(--cyan); letter-spacing: 2px; margin-bottom: 12px;">CALCULUS IN MOTION</div>
            <h1 style="font-size: 40px; color: #fff; line-height: 1.2; margin-bottom: 14px;">Maxima & Minima</h1>
            <h3 style="font-size: 20px; color: var(--amber); margin-bottom: 24px; font-weight: 500;">Kinematic Visual Storytelling & Engineering Optimization</h3>
            <p style="max-width: 720px; color: var(--muted); font-size: 15px; line-height: 1.6;">
              Experience differential calculus through continuous 3Blue1Brown-inspired vector animations.
              Watch equations physically morph, tangent vectors rotate in real time, and concavity bowls verify extrema.
            </p>
            <div style="margin-top: 32px; display: flex; gap: 14px; flex-wrap: wrap; justify-content: center;">
              <button onclick="showSlide(6)" style="background: rgba(56, 189, 248, 0.25); border-color: var(--cyan); color: var(--cyan); font-weight: 700; padding: 10px 22px; font-size: 14px;">
                🌟 Watch Full Master Sequence (Continuous Movie) ➔
              </button>
              <button onclick="showSlide(14)" style="background: rgba(245, 158, 11, 0.2); border-color: var(--amber); color: var(--amber); font-weight: 700; padding: 10px 22px; font-size: 14px;">
                ⚡ Jump to Equation Morphing (Slide 15) ➔
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 2: Roadmap -->
      <div class="slide" data-title="Lecture Trajectory">
        <div class="slide-top">
          <div><div class="meta">Pedagogical Arc</div><h1>Lecture Trajectory: From Kinetic Intuition to Proof</h1></div>
          <div class="slide-num">Slide 02 / 28</div>
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
            <h2 style="color: var(--green); font-size: 17px; margin-bottom: 8px;">04. Closed-Interval Optimization</h2>
            <p style="color: var(--muted); font-size: 13.5px; line-height: 1.5;">
              Extreme Value Theorem on [a, b], candidate matrix evaluation, and circuit Maximum Power Transfer Theorem.
            </p>
          </div>
        </div>
      </div>

      <!-- SLIDE 3: Hook Hill Video -->
      <div class="slide" data-title="Terrain Exploration Hook" data-notes="Play video clip. Ask students: As the exploration probe traverses this mountain range, what exact instantaneous property characterizes the true summits and lowest valleys?">
        <div class="slide-top">
          <div><div class="meta">Phase 1 // Visual Motion</div><h1>Terrain Exploration: Peaks & Valleys</h1></div>
          <div class="slide-num">Slide 03 / 28</div>
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

      <!-- SLIDE 4: Hook Hill Annotation -->
      <div class="slide" data-title="Terrain Slope Workspace">
        <div class="slide-top">
          <div><div class="meta">Live Annotation // Apple Pencil Scratchpad</div><h1>Tangent Equilibrium & Slope Incline</h1></div>
          <div class="slide-num">Slide 04 / 28</div>
        </div>
        <div class="slide-body grid-annotate">
          <div class="card" style="padding: 10px; align-items: center; justify-content: center;">
            <img class="frame-ref" src="media/frames/Scene01_HookHill_frame.png" alt="Terrain Frame">
          </div>
          <div class="card cyan-border" style="background: #0F172A;">
            <h3 style="color: var(--cyan); font-size: 13px; margin-bottom: 8px;">APPLE PENCIL SCRATCHPAD</h3>
            <p style="color: #fff; font-weight: 600; font-size: 14px; margin-bottom: 12px;">Live Student Derivation Prompts:</p>
            <ul style="color: var(--muted); font-size: 13px; line-height: 1.6; padding-left: 18px;">
              <li>✍️ Draw tangent vectors at x = -2.5 (ascent), x = -1.2 (crest), and x = 0 (descent).</li>
              <li>✍️ Write the instantaneous slope inequality: f'(x) &gt; 0 vs. f'(x) = 0 vs. f'(x) &lt; 0.</li>
              <li>✍️ Circle the Local Maximum vs. the Global Mountain Peak.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- SLIDE 5: Local vs Absolute Video -->
      <div class="slide" data-title="Local vs Absolute Extrema">
        <div class="slide-top">
          <div><div class="meta">Phase 1 // Topological Foundations</div><h1>Local Extrema vs. Absolute Boundaries</h1></div>
          <div class="slide-num">Slide 05 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/Scene02_LocalVsAbsolute_frame.png">
              <source src="media/videos/clips/Scene02_LocalVsAbsolute.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">TOPOLOGICAL DISTINCTION</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Neighborhood vs. Global Supremum</p>
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

      <!-- SLIDE 6: Local vs Absolute Annotation -->
      <div class="slide" data-title="Neighborhood Test Workspace">
        <div class="slide-top">
          <div><div class="meta">Live Annotation // Apple Pencil Scratchpad</div><h1>The Neighborhood Test & Boundary Caps</h1></div>
          <div class="slide-num">Slide 06 / 28</div>
        </div>
        <div class="slide-body grid-annotate">
          <div class="card" style="padding: 10px; align-items: center; justify-content: center;">
            <img class="frame-ref" src="media/frames/Scene02_LocalVsAbsolute_frame.png" alt="Extrema Frame">
          </div>
          <div class="card amber-border" style="background: #0F172A;">
            <h3 style="color: var(--amber); font-size: 13px; margin-bottom: 8px;">APPLE PENCIL SCRATCHPAD</h3>
            <p style="color: #fff; font-weight: 600; font-size: 14px; margin-bottom: 12px;">Formalizing the Neighborhood:</p>
            <ul style="color: var(--muted); font-size: 13px; line-height: 1.6; padding-left: 18px;">
              <li>✍️ Draw the open interval (c - δ, c + δ) around x = c₁.</li>
              <li>✍️ Show why x = b cannot contain a two-sided ball inside domain [a, b].</li>
              <li>✍️ Compare numerical elevations: Local Max (elevation 2.0) vs Global Max at x = b (elevation 3.5).</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- SLIDE 7: MASTER SEQUENCE (THE FULL CONTINUOUS 3BLUE1BROWN MOVIE) -->
      <div class="slide" data-title="🌟 MASTER SEQUENCE (Continuous Movie)" data-notes="This is the seamless 24-second master transformation of f(x) = x³ - 3x. It flows uninterrupted across function tracing, dynamic slope telemetry, algebraic factoring morph, drop lines, and concavity verification!">
        <div class="slide-top">
          <div><div class="meta" style="color: var(--amber);">Continuous Mathematical Journey // 3Blue1Brown Style</div><h1>Unified Master Transformation: f(x) = x³ - 3x</h1></div>
          <div class="slide-num">Slide 07 / 28</div>
        </div>
        <div class="slide-body grid-master">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureSequenceMaster_frame.png">
              <source src="media/videos/clips/SignatureSequenceMaster.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap anywhere to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <span class="badge" style="background: rgba(245, 158, 11, 0.2); color: var(--amber); border-color: var(--amber); margin-bottom: 10px;">🌟 UNIFIED MASTER SEQUENCE</span>
            <h3 style="color: #fff; font-size: 15px; font-weight: 700; margin-bottom: 8px;">The Complete Kinematic Story</h3>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 12px;">
              Watch the entire sequence flow seamlessly without interruption:
            </p>
            <div style="font-size: 12px; line-height: 1.6; color: var(--text);">
              <p><strong>1. Kinetic Trajectory:</strong> Curve draws; probe traverses peaks.</p>
              <p style="margin-top: 4px;"><strong>2. Slope Telemetry:</strong> Tangent freezes horizontal at x = -1 and x = +1.</p>
              <p style="margin-top: 4px;"><strong>3. Equation Morphing:</strong> 3x² - 3 ➔ 3(x-1)(x+1) ➔ x = ±1.</p>
              <p style="margin-top: 4px;"><strong>4. Concavity Verification:</strong> f''(-1) = -6 (∩) & f''(1) = +6 (∪).</p>
            </div>
            <div style="margin-top: 16px;">
              <button onclick="replayCurrentVideo()" style="background: var(--amber); color: #000; font-weight: 700; width: 100%; justify-content: center; padding: 8px;">
                🔁 Replay Master Sequence
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 8: Signature Scene 1 Video -->
      <div class="slide" data-title="The Cubic Function Curve">
        <div class="slide-top">
          <div><div class="meta">Signature Sequence // Deep Dive</div><h1>The Cubic Function: f(x) = x³ - 3x</h1></div>
          <div class="slide-num">Slide 08 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene1_TheFunction_frame.png">
              <source src="media/videos/clips/SignatureScene1_TheFunction.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">MATHEMATICAL MODEL</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Kinetic Trajectory Tracking</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              The point moves continuously across the cubic manifold. Observe how the curve transitions from climbing to falling to climbing again.
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">SYMMETRY NOTE</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">f(-x) = -x³ + 3x = -f(x) (Origin symmetry guarantees inverted extrema).</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 9: Signature Scene 2 Video -->
      <div class="slide" data-title="Dynamic Tangent Telemetry">
        <div class="slide-top">
          <div><div class="meta">Signature Sequence // Deep Dive</div><h1>Dynamic Tangent Line & Slope Telemetry</h1></div>
          <div class="slide-num">Slide 09 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene2_TheTangent_frame.png">
              <source src="media/videos/clips/SignatureScene2_TheTangent.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">DERIVATIVE VELOCITY</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Real-Time Slope Readout</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              As the point glides along the curve, the tangent vector rotates dynamically:
              <br>• <strong>Cyan:</strong> m &gt; 0 (climbing)
              <br>• <strong>Amber:</strong> m = 0 (horizontal freeze)
              <br>• <strong>Coral:</strong> m &lt; 0 (descending)
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">TURNING POINT CONDITION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">f'(x) = 0 indicates momentary equilibrium.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 10: Signature Scene 2 Annotation -->
      <div class="slide" data-title="Power Rule Derivation Workspace">
        <div class="slide-top">
          <div><div class="meta">Live Annotation // Apple Pencil Scratchpad</div><h1>Derivative Derivation & Instantaneous Velocity</h1></div>
          <div class="slide-num">Slide 10 / 28</div>
        </div>
        <div class="slide-body grid-annotate">
          <div class="card" style="padding: 10px; align-items: center; justify-content: center;">
            <img class="frame-ref" src="media/frames/SignatureScene2_TheTangent_frame.png" alt="Tangent Frame">
          </div>
          <div class="card cyan-border" style="background: #0F172A;">
            <h3 style="color: var(--cyan); font-size: 13px; margin-bottom: 8px;">APPLE PENCIL SCRATCHPAD</h3>
            <p style="color: #fff; font-weight: 600; font-size: 14px; margin-bottom: 12px;">Step-by-Step Power Rule:</p>
            <ul style="color: var(--muted); font-size: 13px; line-height: 1.6; padding-left: 18px;">
              <li>✍️ Compute f'(x) = d/dx [x³ - 3x] = 3x² - 3.</li>
              <li>✍️ Evaluate f'(0) = -3: Why is descent steepest at the y-intercept?</li>
              <li>✍️ Set f'(x) = 0: Solve 3x² - 3 = 0  =&gt;  x² = 1  =&gt;  x = ±1.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- SLIDE 11: Singularities DNE Video -->
      <div class="slide" data-title="Singularities (Corners & Cusps)">
        <div class="slide-top">
          <div><div class="meta">Singularities // Critical Points</div><h1>When Derivatives Fail: Corners & Cusps</h1></div>
          <div class="slide-num">Slide 11 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/Scene03_SingularitiesDNE_frame.png">
              <source src="media/videos/clips/Scene03_SingularitiesDNE.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card coral-border">
            <h3 style="color: var(--coral); margin-bottom: 8px;">NON-DIFFERENTIABLE EXTREMA</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Corners (|x|) and Cusps (x^(2/3))</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              Calculus is not just about smooth derivatives. In engineering impact and fracture mechanics, corners and cusps form extreme stress concentrations.
            </p>
            <div style="background: rgba(244, 63, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(244, 63, 94, 0.3);">
              <div style="color: var(--coral); font-weight: 700; font-size: 11px;">CRITICAL NUMBER DEFINITION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">c in Dom(f) where f'(c) = 0 OR f'(c) DNE!</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 12: Singularities Annotation -->
      <div class="slide" data-title="Singularity Limits DNE Workspace">
        <div class="slide-top">
          <div><div class="meta">Live Annotation // Apple Pencil Scratchpad</div><h1>Difference Quotient Singularity Proof</h1></div>
          <div class="slide-num">Slide 12 / 28</div>
        </div>
        <div class="slide-body grid-annotate">
          <div class="card" style="padding: 10px; align-items: center; justify-content: center;">
            <img class="frame-ref" src="media/frames/Scene03_SingularitiesDNE_frame.png" alt="Singularities Frame">
          </div>
          <div class="card amber-border" style="background: #0F172A;">
            <h3 style="color: var(--amber); font-size: 13px; margin-bottom: 8px;">APPLE PENCIL SCRATCHPAD</h3>
            <p style="color: #fff; font-weight: 600; font-size: 14px; margin-bottom: 12px;">Rigorous Singularity Limits:</p>
            <ul style="color: var(--muted); font-size: 13px; line-height: 1.6; padding-left: 18px;">
              <li>✍️ Evaluate lim (h→0⁻) |h|/h = -1 vs. lim (h→0⁺) |h|/h = +1.</li>
              <li>✍️ For f(x) = x^(2/3), derive f'(x) = 2 / (3 * x^(1/3)). Show f'(0) division by zero.</li>
              <li>✍️ State clearly why (0, 0) is a valid, indisputable Global Minimum.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- SLIDE 13: Signature Scene 7 Video Counterexample -->
      <div class="slide" data-title="Critical Trap g(x)=x³ Terrace">
        <div class="slide-top">
          <div><div class="meta">Counterexample // The Critical Trap</div><h1>The Critical Trap: g(x) = x³ Inflection Terrace</h1></div>
          <div class="slide-num">Slide 13 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene7_Counterexample_frame.png">
              <source src="media/videos/clips/SignatureScene7_Counterexample.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">THE CRITICAL POINT TRAP</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Zero Derivative != Automatic Extremum</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              At x = 0, the tangent line of g(x) = x³ becomes completely horizontal (g'(0) = 0).
              Yet the curve never turns around! It pauses and keeps ascending.
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">LOGICAL STATUS</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">f'(c) = 0 is a NECESSARY candidate condition, but NOT SUFFICIENT!</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 14: Counterexample Annotation -->
      <div class="slide" data-title="Necessary vs Sufficient Workspace">
        <div class="slide-top">
          <div><div class="meta">Live Annotation // Apple Pencil Scratchpad</div><h1>Logical Implication: Necessary vs. Sufficient</h1></div>
          <div class="slide-num">Slide 14 / 28</div>
        </div>
        <div class="slide-body grid-annotate">
          <div class="card" style="padding: 10px; align-items: center; justify-content: center;">
            <img class="frame-ref" src="media/frames/SignatureScene7_Counterexample_frame.png" alt="Counterexample Frame">
          </div>
          <div class="card cyan-border" style="background: #0F172A;">
            <h3 style="color: var(--cyan); font-size: 13px; margin-bottom: 8px;">APPLE PENCIL SCRATCHPAD</h3>
            <p style="color: #fff; font-weight: 600; font-size: 14px; margin-bottom: 12px;">Logical Directionality:</p>
            <ul style="color: var(--muted); font-size: 13px; line-height: 1.6; padding-left: 18px;">
              <li>✍️ Write Fermat's Theorem: Local Extremum at c (diff'able) ⟹ f'(c) = 0.</li>
              <li>✍️ Strike through the false converse: f'(c) = 0 ⇏ Local Extremum.</li>
              <li>✍️ Analyze g'(x) = 3x²: For x &lt; 0, 3x² &gt; 0. For x &gt; 0, 3x² &gt; 0. No sign change!</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- SLIDE 15: Signature Scene 3 Video Morphing -->
      <div class="slide" data-title="Equation Factoring Morph">
        <div class="slide-top">
          <div><div class="meta">Signature Sequence // TransformMatchingTex</div><h1>Algebraic Morphing: Factoring the Derivative</h1></div>
          <div class="slide-num">Slide 15 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene3_EquationMorph_frame.png">
              <source src="media/videos/clips/SignatureScene3_EquationMorph.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">CONTINUOUS MORPH</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">TransformMatchingTex In Action</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              Watch LaTeX equations reshape continuously from polynomial difference into linear factors, then drop coordinate dashed lines directly onto the curve's x-axis:
              <br><br>
              <strong>1.</strong> f'(x) = 3x² - 3<br>
              <strong>2.</strong> ➔ 3(x² - 1)<br>
              <strong>3.</strong> ➔ 3(x - 1)(x + 1) = 0<br>
              <strong>4.</strong> ➔ Critical roots at x = -1 and x = +1
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">CRITICAL NUMBERS</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">x = -1 (left turning point) & x = +1 (right turning point).</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 16: Signature Scene 4 Video Sign Chart -->
      <div class="slide" data-title="First Derivative Test Sign Chart">
        <div class="slide-top">
          <div><div class="meta">First Derivative Test // Interval Signs</div><h1>First Derivative Test: Dynamic Sign Chart</h1></div>
          <div class="slide-num">Slide 16 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/SignatureScene4_DerivativeTest_frame.png">
              <source src="media/videos/clips/SignatureScene4_DerivativeTest.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">INTERVAL DYNAMICS</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Sign Alternation & Trapped Extrema</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>(-∞, -1):</strong> f'(x) &gt; 0  ↗ Curve climbs<br>
              • <strong>(-1, 1):</strong> f'(x) &lt; 0  ↘ Curve descends<br>
              • <strong>(1, ∞):</strong> f'(x) &gt; 0  ↗ Curve climbs
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">CONCLUSION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">(+ to -) traps Local Max; (- to +) traps Local Min.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 17: Signature Scene 4 Annotation -->
      <div class="slide" data-title="Sign Chart Table Workspace">
        <div class="slide-top">
          <div><div class="meta">Live Annotation // Apple Pencil Scratchpad</div><h1>Constructing the Derivative Sign Table</h1></div>
          <div class="slide-num">Slide 17 / 28</div>
        </div>
        <div class="slide-body grid-annotate">
          <div class="card" style="padding: 10px; align-items: center; justify-content: center;">
            <img class="frame-ref" src="media/frames/SignatureScene4_DerivativeTest_frame.png" alt="Sign Chart Frame">
          </div>
          <div class="card cyan-border" style="background: #0F172A;">
            <h3 style="color: var(--cyan); font-size: 13px; margin-bottom: 8px;">APPLE PENCIL SCRATCHPAD</h3>
            <p style="color: #fff; font-weight: 600; font-size: 14px; margin-bottom: 12px;">Factored Test Matrix 3(x-1)(x+1):</p>
            <ul style="color: var(--muted); font-size: 13px; line-height: 1.6; padding-left: 18px;">
              <li>✍️ Draw columns: x &lt; -1 | x = -1 | -1 &lt; x &lt; 1 | x = 1 | x &gt; 1.</li>
              <li>✍️ Test x = -2: 3(-3)(-1) = +9 &gt; 0 (↗).</li>
              <li>✍️ Test x = 0: 3(-1)(+1) = -3 &lt; 0 (↘).</li>
              <li>✍️ Test x = +2: 3(+1)(+3) = +9 &gt; 0 (↗).</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- SLIDE 18: Signature Scene 5 Video Extrema Reveal -->
      <div class="slide" data-title="Extrema Coordinates Reveal">
        <div class="slide-top">
          <div><div class="meta">Extrema Coordinates // Function Evaluation</div><h1>Exact Extrema Coordinates: (-1, 2) & (1, -2)</h1></div>
          <div class="slide-num">Slide 18 / 28</div>
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

      <!-- SLIDE 19: Signature Scene 6 Video Second Derivative -->
      <div class="slide" data-title="Second Derivative & Concavity">
        <div class="slide-top">
          <div><div class="meta">Second Derivative // Curvature Bending</div><h1>Second Derivative Test & Concavity Bending</h1></div>
          <div class="slide-num">Slide 19 / 28</div>
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

      <!-- SLIDE 20: Test Comparison Matrix -->
      <div class="slide" data-title="1st vs 2nd Test Comparison">
        <div class="slide-top">
          <div><div class="meta">Comparative Analysis // Decision Logic</div><h1>Extrema Decision Matrix: 1st vs. 2nd Test</h1></div>
          <div class="slide-num">Slide 20 / 28</div>
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

      <!-- SLIDE 21: Scene 04 Video Closed Interval -->
      <div class="slide" data-title="Closed Interval EVT">
        <div class="slide-top">
          <div><div class="meta">Optimization Theory // Closed Domain</div><h1>Closed Interval Method & Candidate Matrix</h1></div>
          <div class="slide-num">Slide 21 / 28</div>
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

      <!-- SLIDE 22: Scene 05 Video Engineering App -->
      <div class="slide" data-title="Engineering: Maximum Power Transfer">
        <div class="slide-top">
          <div><div class="meta">Engineering Application // Circuits</div><h1>Maximum Power Transfer Theorem</h1></div>
          <div class="slide-num">Slide 22 / 28</div>
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

      <!-- SLIDE 23: Practice Challenge & Exit Ticket -->
      <div class="slide" data-title="Practice Problem & Exit Ticket">
        <div class="slide-top">
          <div><div class="meta">Active Learning // Exit Challenge</div><h1>Practice Challenge & Verification Key</h1></div>
          <div class="slide-num">Slide 23 / 28</div>
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

      <!-- SLIDE 24: Mathalino Problem 1 Number Optimization -->
      <div class="slide" data-title="Mathalino 1: Number Optimization" data-notes="Mathalino Problem 1. Source: mathalino.com. Walk through defining x, objective f(x) = x - x², critical number x = 1/2, and second derivative f''(x) = -2 proving maximum excess 1/4.">
        <div class="slide-top">
          <div><div class="meta">Mathalino Reviewer // Number Optimization</div><h1>Mathalino Prob 1: Number Exceeding its Square</h1></div>
          <div class="slide-num">Slide 24 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem1_NumberOptimization_frame.png">
              <source src="media/videos/clips/MathalinoProblem1_NumberOptimization.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">SOURCE: MATHALINO PROB 1</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">What number exceeds its square by maximum amount?</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Objective:</strong> f(x) = x - x²<br>
              • <strong>Derivative:</strong> f'(x) = 1 - 2x = 0 ⟹ <strong>x = 1/2</strong><br>
              • <strong>Concavity:</strong> f''(x) = -2 &lt; 0 ⟹ <strong>Strict Maximum</strong><br>
              • <strong>Max Excess:</strong> f(1/2) = 1/2 - 1/4 = <strong>1/4</strong> (0.25)
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">MODELING FOUNDATION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Translating natural language into an analytical objective function.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 25: Mathalino Problem 10 Riverbank Lot -->
      <div class="slide" data-title="Mathalino 10: Riverbank Fencing" data-notes="Mathalino Problem 10. Source: mathalino.com. Area A = xy is constant. Perimeter P = x + 2y. Differentiating dP/dy = -A/y² + 2 = 0 yields 2y² = A = xy => width y is half of length x.">
        <div class="slide-top">
          <div><div class="meta">Mathalino Reviewer // Geometric Constraints</div><h1>Mathalino Prob 10: Riverbank Fencing Optimization</h1></div>
          <div class="slide-num">Slide 25 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem2_RiverbankLot_frame.png">
              <source src="media/videos/clips/MathalinoProblem2_RiverbankLot.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card cyan-border">
            <h3 style="color: var(--cyan); margin-bottom: 8px;">SOURCE: MATHALINO PROB 10</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Least fencing for fixed area along a river</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Constraint:</strong> Area A = xy ⟹ x = A / y<br>
              • <strong>Fence Perimeter:</strong> P = x + 2y = A/y + 2y<br>
              • <strong>Differentiation:</strong> dP/dy = -A/y² + 2 = 0 ⟹ 2y² = A<br>
              • <strong>Optimal Proportions:</strong> 2y² = xy ⟹ <strong>y = ½x</strong> (Width = ½ Length)
            </p>
            <div style="background: rgba(56, 189, 248, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(56, 189, 248, 0.3);">
              <div style="color: var(--cyan); font-weight: 700; font-size: 11px;">BOUNDARY REDUCTION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">With 1 natural boundary (river), the optimal rectangular ratio shifts from 1:1 to 2:1.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 26: Mathalino Problem 16 Open-Top Box -->
      <div class="slide" data-title="Mathalino 16: Open-Top Box" data-notes="Mathalino Problem 16. Source: mathalino.com. Sheet 15'' x 24''. Cut corner x. Volume V(x) = (24-2x)(15-2x)x = 4x³ - 78x² + 360x. V'(x)=0 gives x=3 or x=10. Domain (0, 7.5) rejects x=10. V_max = 486 in³.">
        <div class="slide-top">
          <div><div class="meta">Mathalino Reviewer // Domain Feasibility</div><h1>Mathalino Prob 16: Open-Top Box Optimization</h1></div>
          <div class="slide-num">Slide 26 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem3_OpenTopBox_frame.png">
              <source src="media/videos/clips/MathalinoProblem3_OpenTopBox.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card amber-border">
            <h3 style="color: var(--amber); margin-bottom: 8px;">SOURCE: MATHALINO PROB 16</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">Cardboard 15" × 24": Maximize Folded Volume</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Volume:</strong> V(x) = 4x³ - 78x² + 360x<br>
              • <strong>Criticals:</strong> 12(x - 3)(x - 10) = 0 ⟹ x = 3, 10<br>
              • <strong>Domain Feasibility:</strong> 0 &lt; x &lt; 7.5'' ⟹ <span style="color: var(--coral); font-weight: 700;">Discard x = 10''</span><br>
              • <strong>Max Volume:</strong> V(3) = 18 × 9 × 3 = <strong>486 in³</strong>
            </p>
            <div style="background: rgba(245, 158, 11, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(245, 158, 11, 0.3);">
              <div style="color: var(--amber); font-weight: 700; font-size: 11px;">EXTRANEOUS CRITICAL DISCOVERY</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">x = 10 produces a negative width 15 - 20 = -5'', highlighting why domain check is critical.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 27: Mathalino Problem 03 Tour Bus Revenue -->
      <div class="slide" data-title="Mathalino 03: Tour Bus Revenue" data-notes="Mathalino Problem 03. Source: mathalino.com. Base fare P350, increments P12.50, passenger drop 2 per step. R(x) = (350+12.5x)(80-2x) = 28000 + 300x - 25x². dR/dx = 300 - 50x = 0 => x = 6. Fare = P425, Passengers = 68, Max Revenue = P28,900 (Option C).">
        <div class="slide-top">
          <div><div class="meta">Mathalino Reviewer // Applied Economics</div><h1>Mathalino Prob 03: Tour Bus Maximum Revenue</h1></div>
          <div class="slide-num">Slide 27 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem4_TourBusRevenue_frame.png">
              <source src="media/videos/clips/MathalinoProblem4_TourBusRevenue.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card green-border">
            <h3 style="color: var(--green); margin-bottom: 8px;">SOURCE: MATHALINO PROB 03</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">80-Seat Tour Bus: Balancing Fare vs. Demand</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Price per Seat:</strong> p(x) = 350 + 12.5x<br>
              • <strong>Seats Sold:</strong> q(x) = 80 - 2x<br>
              • <strong>Revenue Function:</strong> R(x) = 28,000 + 300x - 25x²<br>
              • <strong>Calculus Solution:</strong> dR/dx = 300 - 50x = 0 ⟹ <strong>x = 6</strong><br>
              • <strong>Optimal Metrics:</strong> Fare = <strong>P425/seat</strong>, <strong>68 seats</strong> ⟹ <strong>P28,900</strong> [Option C]
            </p>
            <div style="background: rgba(34, 197, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(34, 197, 94, 0.3);">
              <div style="color: var(--green); font-weight: 700; font-size: 11px;">REVENUE MAXIMIZATION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Exact verification of Mathalino Multiple-Choice Reviewer Option C.</div>
            </div>
          </div>
        </div>
      </div>

      <!-- SLIDE 28: Mathalino Problem 42 Trapezoidal Gutter -->
      <div class="slide" data-title="Mathalino 42: Trapezoidal Gutter" data-notes="Mathalino Problem 42. Source: mathalino.com. 14'' tin strip bent at 45°. Base a, slants s = (14-a)/2, height h = (14-a)/(2√2). Cross-section Area A = ah + h². Setting dA/da = 0 yields base a = 14(√2 - 1)/(2√2 - 1) ≈ 3.17 inches.">
        <div class="slide-top">
          <div><div class="meta">Mathalino Reviewer // Hydraulic Engineering</div><h1>Mathalino Prob 42: Trapezoidal Gutter Capacity</h1></div>
          <div class="slide-num">Slide 28 / 28</div>
        </div>
        <div class="slide-body grid-video">
          <div class="seamless-video-canvas" onclick="toggleVideoPlayback(this)">
            <video autoplay muted playsinline preload="auto" poster="media/frames/MathalinoProblem5_TrapezoidalGutter_frame.png">
              <source src="media/videos/clips/MathalinoProblem5_TrapezoidalGutter.mp4" type="video/mp4">
            </video>
            <div class="play-pause-indicator">Tap to Pause / Play</div>
          </div>
          <div class="card coral-border">
            <h3 style="color: var(--coral); margin-bottom: 8px;">SOURCE: MATHALINO PROB 42</h3>
            <p style="color: #fff; font-size: 14px; font-weight: 600; margin-bottom: 12px;">14" Tin Strip at 45°: Maximize Cross-Section Area</p>
            <p style="color: var(--muted); font-size: 13px; line-height: 1.5; margin-bottom: 14px;">
              • <strong>Strip Width:</strong> a + 2s = 14 ⟹ s = (14 - a)/2<br>
              • <strong>Gutter Depth:</strong> h = s sin 45° = (14 - a) / (2√2)<br>
              • <strong>Area:</strong> A(a) = ah + h² = (14a - a²)/(2√2) + (14 - a)²/8<br>
              • <strong>Derivative:</strong> dA/da = (7 - a)/√2 + (a - 14)/4 = 0<br>
              • <strong>Optimal Base:</strong> a = 14(√2 - 1)/(2√2 - 1) ≈ <strong>3.17 inches</strong> (slants s ≈ 5.41")
            </p>
            <div style="background: rgba(244, 63, 94, 0.1); padding: 10px; border-radius: 6px; border: 1px solid rgba(244, 63, 94, 0.3);">
              <div style="color: var(--coral); font-weight: 700; font-size: 11px;">CIVIL & HYDRAULIC OPTIMIZATION</div>
              <div style="color: #fff; font-size: 12px; margin-top: 4px;">Exact closed-form radical solution for open-channel fluid flow.</div>
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
    <span id="slideIndicator" style="font-weight: 600; color: var(--muted); min-width: 90px; text-align: center;">01 / 28</span>
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
        vid.muted = true; // Essential for seamless mobile Safari / Chrome autoplay
        const p = vid.play();
        if (p !== undefined) {
          p.catch(e => console.log('Autoplay hint:', e));
        }
      }
    }

    function toggleVideoPlayback(container) {
      const vid = container.querySelector('video');
      if (vid) {
        if (vid.paused) {
          vid.play();
        } else {
          vid.pause();
        }
      }
    }

    function replayCurrentVideo() {
      const activeSlide = slides[currentSlide];
      const vid = activeSlide.querySelector('video');
      if (vid) {
        vid.currentTime = 0;
        vid.play();
      }
    }

    function showSlide(index) {
      if (index < 0 || index >= slides.length) return;
      slides[currentSlide].classList.remove('active');
      
      // Pause any running videos
      document.querySelectorAll('video').forEach(v => v.pause());

      currentSlide = index;
      slides[currentSlide].classList.add('active');

      const total = slides.length;
      progressFill.style.width = ((currentSlide + 1) / total * 100) + '%';
      slideIndicator.textContent = `${String(currentSlide + 1).padStart(2, '0')} / ${total}`;
      if (sceneNav) sceneNav.value = currentSlide;

      // Update teleprompter notes
      const notes = slides[currentSlide].getAttribute('data-notes') || 'No specific notes for this slide.';
      notesContent.textContent = notes;

      // Seamlessly trigger video playback on slide arrival
      playSlideVideo(slides[currentSlide]);
    }

    document.getElementById('prevBtn').addEventListener('click', () => showSlide(currentSlide - 1));
    document.getElementById('nextBtn').addEventListener('click', () => showSlide(currentSlide + 1));

    if (sceneNav) {
      sceneNav.addEventListener('change', (e) => {
        showSlide(parseInt(e.target.value, 10));
      });
    }

    // Keyboard Navigation (Space / Right Arrow = Next, Left Arrow = Previous)
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
        showSlide(currentSlide + 1);
      } else if (e.key === 'ArrowLeft') {
        showSlide(currentSlide - 1);
      }
    });

    // Teleprompter toggle
    const notesBtn = document.getElementById('notesBtn');
    notesBtn.addEventListener('click', () => {
      const isVisible = teleprompter.style.display === 'block';
      teleprompter.style.display = isVisible ? 'none' : 'block';
      notesBtn.classList.toggle('active', !isVisible);
    });

    // Fullscreen toggle
    const fsBtn = document.getElementById('fsBtn');
    fsBtn.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => alert(err.message));
        fsBtn.textContent = '✕ Exit';
      } else {
        document.exitFullscreen();
        fsBtn.textContent = '⛶ Fullscreen';
      }
    });

    // Canvas / Apple Pencil Inking Engine
    const canvas = document.getElementById('pencilCanvas');
    const ctx = canvas.getContext('2d');
    const drawBtn = document.getElementById('drawBtn');
    const clearInkBtn = document.getElementById('clearInkBtn');
    let isDrawingMode = false;
    let isDrawing = false;
    let currentColor = '#38BDF8';

    function resizeCanvas() {
      const container = document.getElementById('stageContainer');
      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    drawBtn.addEventListener('click', () => {
      isDrawingMode = !isDrawingMode;
      canvas.classList.toggle('drawing-active', isDrawingMode);
      drawBtn.classList.toggle('active', isDrawingMode);
      drawBtn.textContent = isDrawingMode ? '🛑 Inking' : '✍️ Draw';
    });

    clearInkBtn.addEventListener('click', () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    });

    document.querySelectorAll('.color-dot').forEach(dot => {
      dot.addEventListener('click', () => {
        document.querySelectorAll('.color-dot').forEach(d => d.classList.remove('active'));
        dot.classList.add('active');
        currentColor = dot.getAttribute('data-color');
      });
    });

    function getPointerPos(e) {
      const rect = canvas.getBoundingClientRect();
      const clientX = e.touches ? e.touches[0].clientX : e.clientX;
      const clientY = e.touches ? e.touches[0].clientY : e.clientY;
      return {
        x: (clientX - rect.left) * (canvas.width / rect.width),
        y: (clientY - rect.top) * (canvas.height / rect.height)
      };
    }

    function startDraw(e) {
      if (!isDrawingMode) return;
      isDrawing = true;
      const pos = getPointerPos(e);
      ctx.beginPath();
      ctx.moveTo(pos.x, pos.y);
      ctx.strokeStyle = currentColor;
      ctx.lineWidth = 3;
      ctx.lineCap = 'round';
      ctx.lineJoin = 'round';
      e.preventDefault();
    }

    function draw(e) {
      if (!isDrawing || !isDrawingMode) return;
      const pos = getPointerPos(e);
      ctx.lineTo(pos.x, pos.y);
      ctx.stroke();
      e.preventDefault();
    }

    function stopDraw(e) {
      if (!isDrawing) return;
      isDrawing = false;
      ctx.closePath();
    }

    canvas.addEventListener('mousedown', startDraw);
    canvas.addEventListener('mousemove', draw);
    canvas.addEventListener('mouseup', stopDraw);

    canvas.addEventListener('touchstart', startDraw, { passive: false });
    canvas.addEventListener('touchmove', draw, { passive: false });
    canvas.addEventListener('touchend', stopDraw);

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
