# Maxima and Minima — Motion-Based Engineering Lecture

A premium, modern, motion-based differential calculus lecture presentation on **MAXIMA AND MINIMA**, specifically designed for engineering students and presented from an **iPad** using **Apple Keynote** and **Apple Pencil** for real-time live mathematical annotation.

---

## 🚀 Quick Start: How to Use This Package

This package gives you two complementary, battle-tested ways to present:

### Option 1: Native Presentation in Apple Keynote on iPad
1. Open Keynote on your Mac or iPad Pro.
2. Create a new presentation with the **Widescreen 16:9** format.
3. Follow the slide-by-slide specifications in [`BUILD_SHEET_KEYNOTE.md`](./BUILD_SHEET_KEYNOTE.md).
4. Drag and drop the 12 resolution-independent vector graphics from the [`assets/svg/`](./assets/svg/) directory directly onto your Keynote slides (Keynote natively imports SVGs as editable, sharp vector shapes).
5. Set up **Magic Move** transitions with a duration of $1.20\,\text{s}$ and *Ease Both* acceleration.
6. Connect your iPad via USB-C to the lecture hall projector, select the native Keynote Pen tool ($3\,\text{pt}$ stroke, Cyan/Amber ink), and present!

### Option 2: Instant Interactive Presentation Viewer (Browser / iPad Web App)
You can also run or practice the entire lecture immediately in any modern web browser or on your iPad via Safari:
- Open [`index.html`](./index.html) (or [`presentation.html`](./presentation.html)).
- **Interactive Features Built-In:**
  - **16:9 Cinema Canvas:** Responsive dark-mode interface (`#0B0F19`) with cyan/amber accents.
  - **Step-by-Step Builds:** Tap `▶`, hit `Space` or `Arrow Right` to reveal progressive mathematical steps.
  - **Live Apple Pencil Canvas Overlay:** Tap `✏️` (or press `C`) to activate drawing mode; sketch equations, arrows, or intervals directly on top of slides with palm rejection! Tap `🧹` for eraser or `🗑️` to clear.
  - **Speaker Notes Drawer:** Tap `📝` (or press `S`) to pull up minute-by-minute teaching explanations, Socratic prompts, and common misconceptions.
  - **Slide Navigator Grid:** Tap `⊞` (or press `G`) to instantly jump to any of the 22 slides.
  - **Fullscreen Mode:** Tap `⛶` (or press `F`).

---

## 📂 Project Architecture & Deliverables

| File | Purpose | Description |
| :--- | :--- | :--- |
| [`BUILD_SHEET_KEYNOTE.md`](./BUILD_SHEET_KEYNOTE.md) | **Master Keynote Build Sheet** | Exact coordinates, layer hierarchies, `+` Magic Move object tags, animation types, durations, and Apple Pencil clearance zones for all 22 slides. |
| [`LECTURE_CURRICULUM_GUIDE.md`](./LECTURE_CURRICULUM_GUIDE.md) | **Instructional & Pedagogical Guide** | Complete 50-minute pacing timeline, Bloom's taxonomy objectives, verbatim teaching narration scripts, Socratic questions, and student misconception interventions. |
| [`WORKED_SOLUTIONS_AND_PRACTICE.md`](./WORKED_SOLUTIONS_AND_PRACTICE.md) | **Mathematical Foundations & Practice Set** | Rigorous proofs (Fermat, EVT, Darboux, FDT), complete step-by-step worked solutions for $f(x)=x^3-3x$, and 4 engineering practice problems (Electrical, Civil, Chemical, Fluid). |
| [`QUALITY_CONTROL_CHECKLIST.md`](./QUALITY_CONTROL_CHECKLIST.md) | **Master Quality Control Audit** | 100% verified mathematical correctness checklist, iPad readability, contrast verification (WCAG AAA), and animation continuity audit. |
| [`index.html`](./index.html) / [`presentation.html`](./presentation.html) | **Interactive Web Slide Deck** | 16:9 widescreen presentation application with Apple Pencil canvas, build controls, speaker notes, and vector graphics. |
| [`assets/svg/`](./assets/svg/) | **Editable Vector Assets** | 12 high-precision standalone SVG vector graphics for graphs, sign charts, circuits, and flowcharts. |

---

## 🎨 Visual Identity & Palette

- **Background Canvas:** Midnight Navy (`#0B0F19`)
- **Card Containers:** Deep Charcoal Slate (`#111827`)
- **Primary Accent (Climbing / Increasing / Stable):** Electric Cyan (`#38BDF8`)
- **Secondary Accent (Maxima / Turning / Stationary):** Neon Amber (`#F59E0B`)
- **Alert Accent (Decreasing / Singularities / Boundaries):** Vivid Coral (`#F43F5E`)
- **Primary Typography:** Pure Chalk White (`#F8FAFC`)
- **Secondary Typography:** Muted Steel Silver (`#94A3B8`)
- **Grid & Reference Ticks:** Slate (`#334155`)

---

## ⏱️ Lecture Pacing Outline (22 Slides / 50 Minutes)

1. **Slide 01:** The Geometry of Turning Points (Opening Hook: Moving Probe & Vanishing Slope)
2. **Slide 02:** Lecture Architecture & The Central Question (The 4 Core Pillars)
3. **Slide 03:** Intuitive Meaning: Peaks, Troughs & Equilibrium (Mechanical, Electrical, Chemical)
4. **Slide 04:** Local vs. Absolute (Global) Extrema (Neighborhood vs Domain Boundaries)
5. **Slide 05:** The Sign of the Derivative: Rise & Fall (Mean Value Theorem Link)
6. **Slide 06:** Fermat's Theorem on Stationary Points (Horizontal Tangents: One-Sided Limit Proof)
7. **Slide 07:** Critical Numbers: The Complete Definition ($f'=0$ vs $f'$ DNE & Domain Precondition)
8. **Slide 08:** The Singular Points: Corners & Cusps ($f(x)=|x|$ and $f(x)=x^{2/3}$)
9. **Slide 09:** The Necessary vs. Sufficient Trap ($f(x)=x^3$: Stationary Inflection Terrace)
10. **Slide 10:** The First Derivative Test (Visual Sign Chart: $(+) \to (-)$, $(-) \to (+)$, $(+) \to (+)$)
11. **Slide 11:** Master Worked Example (Part 1: Differentiate, Factor, and Critical Numbers for $x^3-3x$)
12. **Slide 12:** Master Worked Example (Part 2: Sign Chart, Coordinates $(-1, 2)$ & $(1, -2)$, Synchronized Dual Graph)
13. **Slide 13:** Curvature & Concavity: The Second Derivative ($f''(x)$ Bending & Tangent Locations)
14. **Slide 14:** The Second Derivative Test: Verification & Limits (Evaluation on $6x$ & When SDT Fails)
15. **Slide 15:** Absolute Extrema on Closed Intervals (Extreme Value Theorem & Endpoint Traps on $[-0.5, 2.5]$)
16. **Slide 16:** Real Engineering Optimization: Maximum Power Transfer ($P(R_L) = \frac{V_s^2 R_L}{(R_s + R_L)^2} \implies R_L = R_s$)
17. **Slide 17:** Guided Practice: Sheet Metal Packaging Chassis ($V(x) = 4x(6-x)^2 \implies x=2\,\text{cm}$)
18. **Slide 18:** Independent Engineering Challenge: Beam Deflection ($y(x) = \frac{w_0}{24EI}(x^4 - 2Lx^3 + L^3x) \implies x=L/2$)
19. **Slide 19:** The Engineering Protocol: Algorithmic Decision Flowchart & Selection Matrix
20. **Slide 20:** Exit Ticket: Misconception Diagnostics (3 Rapid-Fire Concept Checks)
21. **Slide 21:** Reference Appendix: Complete Solutions & Derivation Reference
22. **Slide 22:** The Next Horizon: Multivariable Optimization ($\nabla f = \mathbf{0}$, Hessian, Saddle Points)
