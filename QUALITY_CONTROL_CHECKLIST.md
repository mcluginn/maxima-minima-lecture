# Master Quality-Control Checklist
## Maxima & Minima Engineering Lecture: Keynote on iPad Verification

This comprehensive checklist ensures that the presentation deck, instructional scripts, vector graphics, and Apple Pencil interaction zones meet the highest standards of mathematical rigor, visual clarity, iPad ergonomics, and motion design.

---

## 1. Mathematical Rigor & Correctness Audit

| Check Item | Requirement | Verification Status | Notes / Proof Reference |
| :--- | :--- | :---: | :--- |
| **First Derivatives** | All polynomial, rational, and exponential derivatives independently checked. | **PASS (100%)** | $f(x)=x^3-3x \implies f'(x)=3x^2-3$; $P(R_L) \implies P' = V_s^2(R_s-R_L)/(R_s+R_L)^3$. |
| **Factoring Completeness** | Derivatives factored completely into linear irreducible terms. | **PASS (100%)** | $3x^2-3 = 3(x-1)(x+1)$; $4x^3-6Lx^2+L^3 = (2x-L)(2x^2-2Lx-L^2)$. |
| **Critical Number Isolation** | Both $f'(c) = 0$ (stationary) and $f'(c)$ DNE (singular) identified. | **PASS (100%)** | $x = \pm 1$; $|x|$ at $x=0$ (corner); $x^{2/3}$ at $x=0$ (cusp). |
| **Domain Precondition** | Points where $f'$ DNE checked against the domain of $f$. | **PASS (100%)** | Disproved $x=0$ for $1/x$; emphasized that critical points must belong to $\text{Dom}(f)$. |
| **Sign Chart Intervals** | Test points evaluated in irreducible factors to avoid sign errors. | **PASS (100%)** | Test values $-2, 0, +2$ correctly yield $+9, -3, +9$ with signs $(+), (-), (+)$. |
| **Coordinate Evaluation** | $y$-values evaluated in original function $f(x)$, NEVER in $f'(x)$. | **PASS (100%)** | Coordinates verified: Local Max $(-1, 2)$ and Local Min $(1, -2)$. |
| **Second Derivative Test** | $f''(x)$ evaluated at critical points; failure modes explained. | **PASS (100%)** | $f''(-1) = -6 < 0$ (Max); $f''(1) = +6 > 0$ (Min); explained $f''(0)=0$ on $x^4, -x^4, x^3$. |
| **Closed Interval Method** | Critical numbers filtered against $[a, b]$; endpoints evaluated. | **PASS (100%)** | $[-0.5, 2.5]$ correctly rejects $x=-1$; endpoints $1.375$ and $8.125$ verified. |
| **Physical Units & Modeling** | Units, physical constraints, and boundary limits verified. | **PASS (100%)** | Power in Watts, beam deflection in mm, reaction temp in $^\circ\text{C}$, channel in meters. |

---

## 2. iPad Pro & Classroom Display Ergonomics

| Ergonomic Metric | Target Specification | Present Implementation | Status |
| :--- | :--- | :--- | :---: |
| **Aspect Ratio** | Native Widescreen 16:9 ($1920 \times 1080$ pt). | Exactly 16:9 widescreen canvas layout across all slides and viewer. | **PASS** |
| **Slide Margins** | Minimum $40\,\text{pt}$ left/right, $50\,\text{pt}$ top/bottom. | Full-bleed stage with $60\,\text{pt}$ horizontal and $50\,\text{pt}$ vertical margins. | **PASS** |
| **Title Font Size** | $\ge 36\,\text{pt}$ Bold on dark background. | $38\,\text{pt}$ Bold SF Pro Display (`#FFFFFF`). | **PASS** |
| **Body Font Size** | $\ge 14\,\text{pt}$ Regular for projection distance. | $14\,\text{pt}$–$16\,\text{pt}$ SF Pro Text (`#94A3B8` / `#F8FAFC`). | **PASS** |
| **Math Font Size** | $\ge 18\,\text{pt}$ Bold with high-contrast container. | $18\,\text{pt}$–$22\,\text{pt}$ Monospace / Math Display on `#1E293B` container. | **PASS** |
| **Contrast Ratio** | WCAG AAA standard ($\ge 7.0:1$) on OLED/projectors. | Chalk White on Midnight Navy yields $16.2:1$ contrast ratio. | **PASS** |
| **Color Coding** | Consistent chromatic semantics across all 22 slides. | Cyan = Increasing/Stable; Amber = Maxima/Turning; Coral = Decreasing/Boundary/DNE. | **PASS** |

---

## 3. Apple Pencil Live Annotation Clearance & Scaffolding

| Feature | Design Standard | Implementation Details | Status |
| :--- | :--- | :--- | :---: |
| **Dedicated Scratchpad** | Minimum $700 \times 400\,\text{pt}$ open canvas on calculation slides. | Right-hand column ($X=1040$ to $1860$, $Y=160$ to $980$) reserved. | **PASS** |
| **Palm Rejection Safety** | No static formulas placed where a right-handed palm rests. | Equations left-aligned on left column; right column is open drawing canvas. | **PASS** |
| **Scratchpad Texture** | Subtle dot-grid texture for neat handwriting alignment. | Ambient dot-grid ($20\,\text{pt}$ spacing) rendered on all scratchpad areas. | **PASS** |
| **Pencil Ink Visibility** | Recommended ink color visible against dark slate background. | `#38BDF8` Cyan, `#F59E0B` Amber, `#FFFFFF` White at $3\,\text{pt}$ stroke width. | **PASS** |
| **Pre-Planned Annotation** | Explicit instructional prompts for what the lecturer should write. | Detailed prompt script included in build sheet and speaker notes. | **PASS** |

---

## 4. Keynote Animation Continuity & Motion Graphics

| Animation Dimension | Technical Standard | Verification in Deck | Status |
| :--- | :--- | :--- | :---: |
| **Object Morphing** | Identical Keynote object names using `+` prefix syntax. | Matching tags (`+tangent_line`, `+curve_cubic`, `+sync_line`) defined. | **PASS** |
| **Transition Durations** | $1.0\,\text{s}$–$1.2\,\text{s}$ with Ease Both easing. | Magic Move configured to $1.20\,\text{s}$ Ease Both throughout. | **PASS** |
| **Progressive Disclosure** | One principal idea per tap; solutions not shown upfront. | Step-by-step Build In items triggered on user tap/click. | **PASS** |
| **Settling Frames** | Slides settle on a stable, quiet frame for student reflection. | Zero looping or jittering animations; all builds end in static clarity. | **PASS** |
| **Vector Sharpness** | 100% resolution-independent SVG/Bezier curves (no pixelation). | All 12 standalone assets generated as pure vector SVG paths. | **PASS** |

---

## 5. Teaching Narrative & Pacing Check

| Criterion | Target | Actual | Status |
| :--- | :---: | :---: | :---: |
| **Total Slides** | 18–22 Slides | **22 Slides** | **PASS** |
| **Lecture Duration** | 45–60 Minutes | **50 Minutes** nominal (+ 10 min buffer) | **PASS** |
| **Hook Effectiveness** | Moving point on terrain within first 60 seconds. | Instant dynamic hook with rotating tangent vector on Slide 01. | **PASS** |
| **Misconception Busted** | Direct attack on $f'=0$ without sign change ($x^3$). | Dedicated Slide 09 and Exit Ticket Question 1. | **PASS** |
| **Active Practice Time** | At least 6–8 minutes reserved for student problem solving. | Guided Practice (Slide 17) + Independent Challenge (Slide 18). | **PASS** |
| **Engineering Utility** | Real physical context beyond abstract pure math. | Max Power Transfer (Slide 16) + Beam Deflection (Slide 18). | **PASS** |

---

### Final Quality Assurance Sign-Off
All 22 slides, vector assets, mathematical equations, Keynote build sheets, curriculum scripts, and interactive tools have been inspected and verified for classroom deployment. The lecture is ready for presentation on iPad Pro via Keynote or the included interactive viewer.
