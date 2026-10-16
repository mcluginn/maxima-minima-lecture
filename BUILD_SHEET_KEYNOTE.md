# Master Keynote Build Sheet: Maxima & Minima Engineering Lecture

## 1. Project Overview & Platform Specification

- **Target Presentation Environment:** Apple Keynote on iPad (iPad Pro 11" / 12.9" / 13" M-series & Apple Pencil Pro / Gen 2).
- **Canvas Aspect Ratio:** Widescreen 16:9 ($1920 \times 1080$ points native resolution).
- **Target Audience:** Undergraduate Engineering Students (Mechanical, Electrical, Civil, Aerospace, Chemical).
- **Lecture Duration:** 45–60 Minutes (22 Slides).
- **Core Design Ethos:** 3Blue1Brown mathematical elegance meets high-end dark aerospace/engineering UI. Non-linear, lecturer-controlled progression with deliberate Apple Pencil live-annotation staging.

---

## 2. Design System & Global Master Styles

### 2.1 Color Palette & Keynote Color Swatches
To ensure visual consistency, enter these exact RGB / Hex values into the Keynote Color Palette on iPad or Mac:

| Role | Color Name | Hex Code | RGB (0–255) | Keynote Visual Utility |
| :--- | :--- | :--- | :--- | :--- |
| **Canvas Canvas** | Midnight Navy | `#0B0F19` | `11, 15, 25` | Deep, non-reflective background for OLED/Mini-LED |
| **Card Container** | Dark Slate | `#111827` | `17, 24, 39` | Foreground cards with 1px border `rgba(255,255,255,0.08)` |
| **Subtle Fill** | Deep Slate | `#1E293B` | `30, 41, 59` | Equation block backgrounds, table header bars |
| **Primary Accent** | Electric Cyan | `#38BDF8` | `56, 189, 248` | Function curves, increasing intervals, stable states |
| **Secondary Accent** | Neon Amber | `#F59E0B` | `245, 158, 11` | Critical points, stationary lines, local maxima |
| **Alert / Warning** | Vivid Coral | `#F43F5E` | `244, 63, 94` | Decreasing intervals, absolute maxima, DNE singularities |
| **Grid / Axes** | Muted Steel | `#334155` | `51, 65, 85` | Coordinate axes, tick marks, reference grid lines |
| **Text Primary** | Pure Chalk White | `#F8FAFC` | `248, 250, 252` | Primary mathematical expressions, titles |
| **Text Secondary** | Muted Silver | `#94A3B8` | `148, 163, 184` | Explanations, coordinate pairs, sub-bullets |

### 2.2 Typography Scale & Keynote Text Hierarchy
All text layers must use system-native sans-serif fonts to prevent font-substitution artifacts when transferring between Mac and iPad:

1. **Title / Slide Heading:** `SF Pro Display`, Bold (700/800), $38\,\text{pt}$, Line Spacing $1.15$, Character Spacing $-0.02\,\text{em}$, Pure Chalk White (`#F8FAFC`).
2. **Slide Subtitle / Hook:** `SF Pro Text`, Regular (400), $18\,\text{pt}$, Line Spacing $1.35$, Muted Silver (`#94A3B8`).
3. **Card Headings:** `SF Pro Display`, Semibold (600), $18\,\text{pt}$–$20\,\text{pt}$, Electric Cyan or Neon Amber.
4. **Display Equations (LaTeX / MathBox):** `SF Pro Text` Bold or `New Computer Modern Sans`, $20\,\text{pt}$–$24\,\text{pt}$, Pure Chalk White on `#1E293B` container.
5. **Body Explanations:** `SF Pro Text`, Regular (400), $14\,\text{pt}$–$15\,\text{pt}$, Line Spacing $1.45$.
6. **Graph Coordinates & Captions:** `SF Pro Text`, Medium (500), $12\,\text{pt}$–$13\,\text{pt}$.

### 2.3 iPad Ergonomics & Apple Pencil Annotation Clearance
To prevent the lecturer's hand and Apple Pencil from occluding pre-rendered equations or graph legends:
- **Right-Handed Lecturer Rule:** On calculation-heavy slides, reserve the **right 45% of the slide** ($X = 1040$ to $1860$, $Y = 160$ to $980$) as an open **Scratchpad Zone**.
- **Visual Styling of Scratchpad Zone:** A rounded rectangle ($r = 12\,\text{pt}$), background `rgba(15, 23, 42, 0.45)`, with a $1.5\,\text{pt}$ dashed border (`#334155`) and an ambient dot-grid pattern (spacing $24\,\text{pt}$, dot radius $1.5\,\text{pt}$, color `#475569` at 20% opacity).
- **Badge:** Include a subtle top-right pill tag: `APPLE PENCIL SCRATCHPAD` in $10\,\text{pt}$ Cyan text.

---

## 3. Keynote Magic Move Setup Guide

### 3.1 Object Matching Rules
Keynote Magic Move smoothly interpolates position, rotation, scale, color, and opacity between consecutive slides **if and only if** objects share identical identifiers or layer structures:
1. **The `+` Prefix Syntax:** For any shape or text element that must morph seamlessly across slides, prefix its name in the Keynote Object List with a double plus `+` (e.g. `+tangent_line`, `+curve_cubic`, `+sign_chart_bar`, `+formula_box`).
2. **Anchor Points:** Ensure vector curves do not change their point count if you want smooth path deformation. If path point count changes, use **Magic Move by Object** with **Dissolve Unmatched Objects** enabled.
3. **Transition Settings:**
   - **Transition:** Magic Move
   - **Duration:** $1.20\,\text{s}$ (instructional sweet spot: fast enough not to drag, slow enough for visual comprehension)
   - **Acceleration / Easing:** *Ease Both* (smooth cubic-bezier acceleration and deceleration)
   - **Match By:** *Object* (preferred over text match to prevent unexpected letter scramble)

---

## 4. Slide-by-Slide Detailed Keynote Build Sheet

Below is the definitive, object-level build sheet for all 22 slides. Every build, transition, coordinate block, and lecturer pause is explicitly specified.

---

### Slide 01: The Geometry of Turning Points (Opening Hook)
- **Slide Dimensions:** $1920 \times 1080$ pt
- **Slide Theme:** Dark Midnight Canvas (`#0B0F19`)
- **Keynote Slide Transition:** None (First slide) $\to$ Magic Move ($1.2\,\text{s}$) to Slide 02

#### Layer Hierarchy (Back to Front)
1. `bg_base` (Rectangle, $1920 \times 1080$, Fill `#0B0F19`)
2. `header_bar` (Group: 56pt top banner, `#38BDF8` unit badge, title text)
3. `graph_container` (Card, $X=60, Y=140, W=920, H=860$, Fill `#111827`, Stroke 1pt `#1E293B`)
   - `+grid_system` (Group of coordinate lines and axes)
   - `+curve_terrain` (Editable Vector Bezier Path, Stroke 4pt `#38BDF8`, glow filter)
   - `+probe_particle` (Circle, $r=7$, Fill `#EC4899`, Stroke 2pt `#F8FAFC`, at $X=300, Y=560$)
   - `+tangent_slope_vector` (Line with arrow head, length $140\,\text{pt}$, Angle $-45^\circ$, Stroke 2.5pt `#EC4899`)
   - `+local_max_marker` (Circle, $r=8$, Fill `#F59E0B`, at $(X=400, Y=340)$)
   - `+local_min_marker` (Circle, $r=8$, Fill `#38BDF8`, at $(X=680, Y=680)$)
4. `right_panel` (Card, $X=1020, Y=140, W=840, H=860$, Fill `#111827`)
   - `title_text`: "Differential Calculus: Maxima & Minima" ($36\,\text{pt}$)
   - `math_box_1`: "State Model: $y = f(x) \in C^1[a, b]$" ($X=1060, Y=260$)
   - `math_box_2`: "Stationary: $f'(x) = 0$" ($X=1060, Y=360$)
   - `math_box_3`: "Singular: $f'(x)$ Does Not Exist" ($X=1060, Y=460$)
   - `scratchpad_zone_01`: ($X=1060, Y=560, W=760, H=400$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Base layout + graph + curve | Appears with slide | — | On Slide Load |
| **1** | `+probe_particle` & `+tangent_slope_vector` | Action: Move & Rotate | Move along curve to peak $(X=400, Y=340)$, rotate line to $0^\circ$ (horizontal). Duration: $2.5\,\text{s}$, Easing: Ease Out | **Click 1** |
| **2** | `+local_max_marker` & label | Build In: Scale | Scale from 0% to 100%, Duration $0.5\,\text{s}$, Bounce | With Build 1 (after $2.2\,\text{s}$) |
| **3** | `math_box_2` ($f'(x)=0$) | Build In: Wipe (Left to Right) | Duration: $0.6\,\text{s}$, Ease Both | **Click 2** |
| **4** | `math_box_3` ($f'$ DNE) | Build In: Wipe (Left to Right) | Duration: $0.6\,\text{s}$, Ease Both | **Click 3** |
| **PAUSE**| **Lecturer Apple Pencil Pause** | — | Lecturer sketches tangent vector at arbitrary point, writes $\Delta y / \Delta x$ in scratchpad. | **Live Pause** |

---

### Slide 02: Lecture Architecture & The Central Question
- **Transition In:** Magic Move ($1.2\,\text{s}$) from Slide 01. `header_bar` stays anchored.
- **Visual Design:** 2-column layout. Left column holds the 4 Pillars; Right column holds the Socratic reflection card and live annotation area.

#### Layer Hierarchy & Key Objects
- `col_left_card` ($X=60, Y=140, W=880, H=860$, Fill `#111827`, Stroke Cyan `#38BDF8` at 30% opacity)
  - `pillar_1` (Group: Badge "01", Title "The Geometry of Turning", Description)
  - `pillar_2` (Group: Badge "02", Title "The Classification Engines", Description)
  - `pillar_3` (Group: Badge "03", Title "Boundary Constraints", Description)
  - `pillar_4` (Group: Badge "04", Title "Physical Optimization Modeling", Description)
- `col_right_card` ($X=980, Y=140, W=880, H=860$, Fill `#111827`)
  - `socratic_quote_box`: "If $f'(x) = 0$, does a turning point definitely occur?"
  - `scratchpad_zone_02`: ($X=1020, Y=340, W=800, H=620$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Col Left & Col Right cards | Magic Move | Morphs into place from Slide 01 | Automatic |
| **1** | `pillar_1` | Build In: Move In (From Left) | Duration: $0.5\,\text{s}$, Ease Out | **Click 1** |
| **2** | `pillar_2` | Build In: Move In (From Left) | Duration: $0.5\,\text{s}$, Ease Out | **Click 2** |
| **3** | `pillar_3` | Build In: Move In (From Left) | Duration: $0.5\,\text{s}$, Ease Out | **Click 3** |
| **4** | `pillar_4` | Build In: Move In (From Left) | Duration: $0.5\,\text{s}$, Ease Out | **Click 4** |
| **PAUSE**| **Socratic Discussion Pause** | — | Lecturer writes student hypotheses in scratchpad: "Is zero slope sufficient?" | **Live Pause** |

---

### Slide 03: Intuitive Meaning: Peaks, Troughs & Equilibrium
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$, Ease Both)
- **Visual Design:** 3 equal vertical cards highlighting multi-disciplinary engineering manifestations.

#### Layer Hierarchy & Key Objects
- `card_mech` ($X=60, Y=180, W=560, H=820$, Cyan theme: Mechanical/Potential Energy $U(x)$, $F = -dU/dx$)
- `card_elec` ($X=680, Y=180, W=560, H=820$, Amber theme: Circuit Impedance Matching $dP/dR_L = 0$)
- `card_chem` ($X=1300, Y=180, W=560, H=820$, Coral theme: Chemical Reaction Kinetics vs Catalyst Decay)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | 3 Column Cards (Base) | Build In: Dissolve | Duration: $0.4\,\text{s}$ | Automatic |
| **1** | `card_mech` formulas & bowl icon | Build In: Scale Up (90% to 100%) | Duration: $0.5\,\text{s}$, Ease Both | **Click 1** |
| **2** | `card_elec` formulas & impedance icon | Build In: Scale Up (90% to 100%) | Duration: $0.5\,\text{s}$, Ease Both | **Click 2** |
| **3** | `card_chem` formulas & yield curve | Build In: Scale Up (90% to 100%) | Duration: $0.5\,\text{s}$, Ease Both | **Click 3** |
| **PAUSE**| **Apple Pencil Analogy Pause** | — | Lecturer sketches a marble at the bottom of a bowl vs inverted bowl. | **Live Pause** |

---

### Slide 04: Local vs. Absolute (Global) Extrema
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** Left side: Vector graph of continuous function on $[a, b]$ with interior peak, interior valley, and high right boundary. Right side: Formal $\epsilon$-$\delta$ neighborhood definition and scratchpad.

#### Layer Hierarchy & Key Objects
- `vector_graph_04` ($X=60, Y=140, W=920, H=860$, contains `assets/svg/04_local_vs_global.svg`)
  - `+curve_bounded`
  - `+pt_left_endpoint`: $A(a, f(a))$ at $X=200, Y=420$
  - `+pt_local_max`: $B(c_1, f(c_1))$ with neighborhood bracket $(c_1-\delta, c_1+\delta)$
  - `+pt_absolute_min`: $C(c_2, f(c_2))$ at $X=600, Y=700$
  - `+pt_absolute_max`: $D(b, f(b))$ at $X=820, Y=220$
- `right_card_04` ($X=1020, Y=140, W=840, H=860$)
  - `def_local_box`: Definition of Local Maximum: $\exists \delta > 0 \text{ s.t. } f(c) \ge f(x) \;\forall x \in (c-\delta, c+\delta)$
  - `def_global_box`: Definition of Absolute Maximum: $f(c) \ge f(x) \;\forall x \in D$
  - `scratchpad_zone_04` ($X=1060, Y=520, W=760, H=440$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Graph + Base definitions | Appears with slide | — | On Slide Load |
| **1** | `+pt_local_max` & bracket highlight | Build In: Scale (Pulse) | Duration: $0.6\,\text{s}$ | **Click 1** |
| **2** | `+pt_absolute_max` (at endpoint $b$) | Build In: Scale + Glow | Duration: $0.6\,\text{s}$, Amber glow | **Click 2** |
| **3** | `def_global_box` reveal | Build In: Move In (Bottom) | Duration: $0.5\,\text{s}$, Ease Both | **Click 3** |
| **PAUSE**| **Lecturer Annotation Pause** | — | Lecturer writes in scratchpad: "Can a point be both local AND absolute? YES (if interior). Can an endpoint be local? (By standard open-interval convention: No; by relative topology: Yes)". | **Live Pause** |

---

### Slide 05: The Sign of the Derivative: Rise & Fall
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** The curve from Slide 04 morphs into an ascending and descending curve colored in two distinct chromatic zones (Cyan for $f'>0$, Coral for $f'<0$).

#### Layer Hierarchy & Key Objects
- `vector_graph_05` ($X=60, Y=140, W=920, H=860$, contains `assets/svg/05_slopes_and_intervals.svg`)
  - `+zone_increasing` (Path segment in glowing Cyan `#38BDF8`, slope arrow upward)
  - `+zone_decreasing` (Path segment in glowing Coral `#F43F5E`, slope arrow downward)
  - `+summit_pt` (Amber circle at apex $(X=480, Y=260)$)
- `right_card_05` ($X=1020, Y=140, W=840, H=860$)
  - `mvt_box`: "Mean Value Theorem Connection:"
  - `mvt_formula`: $\frac{f(x_2) - f(x_1)}{x_2 - x_1} = f'(c) > 0 \implies f(x_2) > f(x_1)$
  - `scratchpad_zone_05` ($X=1060, Y=500, W=760, H=460$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Graph with zone colors | Magic Move | Morphs from Slide 04 | Automatic |
| **1** | `+zone_increasing` tangent arrow | Action: Pulse | Duration: $0.6\,\text{s}$, Cyan glow | **Click 1** |
| **2** | `+zone_decreasing` tangent arrow | Action: Pulse | Duration: $0.6\,\text{s}$, Coral glow | **Click 2** |
| **3** | `mvt_formula` card | Build In: Wipe (Left to Right) | Duration: $0.7\,\text{s}$, Ease Both | **Click 3** |
| **PAUSE**| **Mean Value Theorem Sketch Pause** | — | Lecturer uses Apple Pencil in scratchpad to sketch secant line chord connecting $x_1$ and $x_2$, proving why slope dictates direction. | **Live Pause** |

---

### Slide 06: Fermat's Theorem on Stationary Points
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** High-precision geometric visualization of tangent lines converging from positive slope to zero slope as the point approaches the peak.

#### Layer Hierarchy & Key Objects
- `vector_graph_06` ($X=60, Y=140, W=920, H=860$, contains `assets/svg/06_tangent_to_stationary.svg`)
  - `+converging_tangent_1` ($m = +2.5$, dashed gray line)
  - `+converging_tangent_2` ($m = +0.8$, solid slate line)
  - `+horizontal_tangent` ($m = 0$, glowing amber line `#F59E0B`, width 3.5pt)
  - `+apex_circle` (Amber circle at apex $(X=480, Y=210)$)
- `right_card_06` ($X=1020, Y=140, W=840, H=860$)
  - `fermat_theorem_box`: Fermat's Theorem Statement (1636)
  - `fermat_proof_idea`: One-sided derivative limits squeeze the slope to zero.
  - `scratchpad_zone_06` ($X=1060, Y=480, W=760, H=480$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Graph + Parabola | Appears on slide | — | On Slide Load |
| **1** | `+converging_tangent_1` & `_2` | Build In: Draw Line | Duration: $0.8\,\text{s}$, Ease Out | **Click 1** |
| **2** | `+horizontal_tangent` & `+apex_circle` | Build In: Scale Up + Glow | Duration: $0.7\,\text{s}$, Amber glow | **Click 2** |
| **3** | `fermat_theorem_box` text | Build In: Move In (From Right) | Duration: $0.5\,\text{s}$ | **Click 3** |
| **PAUSE**| **One-Sided Limits Proof Pause** | — | Lecturer writes in scratchpad: $\lim_{h \to 0^+} \frac{f(c+h)-f(c)}{h} \le 0$ and $\lim_{h \to 0^-} \frac{f(c+h)-f(c)}{h} \ge 0 \implies f'(c) = 0$. | **Live Pause** |

---

### Slide 07: Critical Numbers: The Complete Definition
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$, Ease Both)
- **Visual Design:** 2 wide comparative cards: Condition 1 ($f'(c) = 0$, Stationary) vs Condition 2 ($f'(c)$ DNE, Singular).

#### Layer Hierarchy & Key Objects
- `card_cond1` ($X=60, Y=180, W=880, H=400$, Cyan border, Stationary Points definition, smooth polynomial examples)
- `card_cond2` ($X=980, Y=180, W=880, H=400$, Coral border, Singular Points definition, non-differentiable examples)
- `bottom_warning_card` ($X=60, Y=620, W=1800, H=380$, Fill `#111827`, Precondition Warning: "$c$ MUST belong to the domain of $f$!")

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Header + Base cards | Dissolve | Duration: $0.4\,\text{s}$ | On Slide Load |
| **1** | `card_cond1` content | Build In: Move In (From Left) | Duration: $0.6\,\text{s}$, Ease Out | **Click 1** |
| **2** | `card_cond2` content | Build In: Move In (From Right) | Duration: $0.6\,\text{s}$, Ease Out | **Click 2** |
| **3** | `bottom_warning_card` | Build In: Scale (95% to 100%) | Duration: $0.5\,\text{s}$, Coral border pulse | **Click 3** |
| **PAUSE**| **Domain Check Demonstration** | — | Lecturer writes $f(x) = 1/x$. $f'(x) = -1/x^2 \ne 0$. Does $x=0$ have $f'$ DNE? Yes! BUT is $x=0$ a critical number? NO, because $0 \notin \text{Domain}(f)$. | **Live Pause** |

---

### Slide 08: When the Derivative Fails to Exist (DNE)
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** Side-by-side dual graph card displaying Case A (The Corner: $f(x) = |x|$) and Case B (The Cusp: $f(x) = x^{2/3}$).

#### Layer Hierarchy & Key Objects
- `vector_graph_08` ($X=60, Y=140, W=1800, H=600$, contains `assets/svg/07_cusp_and_corner_dne.svg`)
  - Panel A: Corner graph of $|x|$, left slope $-1$, right slope $+1$, sharp vertex at $(0, 0)$.
  - Panel B: Cusp graph of $x^{2/3}$, tangents becoming vertical ($m \to \pm\infty$), sharp apex at $(0, 0)$.
- `annotation_tray_08` ($X=60, Y=760, W=1800, H=260$, dual scratchpad boxes with Apple Pencil clearance)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Dual graph container | Appears with slide | — | On Slide Load |
| **1** | Panel A: Corner slopes & vertex highlight | Build In: Trace Vector Path | Duration: $0.7\,\text{s}$ | **Click 1** |
| **2** | Panel B: Cusp tangents & vertex highlight | Build In: Trace Vector Path | Duration: $0.7\,\text{s}$ | **Click 2** |
| **3** | DNE summary banners | Build In: Move In (Bottom) | Duration: $0.5\,\text{s}$ | **Click 3** |
| **PAUSE**| **Derivative Computation Pause** | — | Lecturer writes in scratchpad: $f'(x) = \frac{2}{3}x^{-1/3} = \frac{2}{3\sqrt[3]{x}}$. At $x=0$, division by zero $\implies f'(0)$ is undefined, yet $0 \ge 0$ for all $x$, so $(0, 0)$ is an absolute minimum! | **Live Pause** |

---

### Slide 09: The Necessary vs. Sufficient Trap: $f(x) = x^3$
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** Highlighting the classic misconception. Graph of $f(x) = x^3$ near the origin with a horizontal tangent line at $x=0$, but no extremum.

#### Layer Hierarchy & Key Objects
- `vector_graph_09` ($X=60, Y=140, W=920, H=860$, contains `assets/svg/08_stationary_inflection_cubic.svg`)
  - `+cubic_curve` (S-shaped curve in Cyan `#38BDF8`)
  - `+horizontal_tangent_origin` (Amber dashed line through $(0, 0)$)
  - `+slope_tag_left`: $x < 0 \implies f'(x) = 3x^2 > 0$ [Ascending]
  - `+slope_tag_right`: $x > 0 \implies f'(x) = 3x^2 > 0$ [Ascending]
- `right_card_09` ($X=1020, Y=140, W=840, H=860$)
  - `trap_alert_box`: Red warning banner: "Critical Misconception Alert"
  - `trap_derivation`: $f'(x) = 3x^2 \implies f'(0) = 0$.
  - `trap_takeaway`: "A horizontal tangent is a stationary point, but NOT necessarily an extremum!"
  - `scratchpad_zone_09` ($X=1060, Y=540, W=760, H=420$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Graph + Cubic curve | Appears with slide | — | On Slide Load |
| **1** | `+horizontal_tangent_origin` | Build In: Draw Line | Duration: $0.6\,\text{s}$, Amber glow | **Click 1** |
| **2** | `+slope_tag_left` & `+slope_tag_right` | Build In: Scale Up | Duration: $0.5\,\text{s}$ | **Click 2** |
| **3** | `trap_alert_box` & text | Build In: Shake / Pulse | Duration: $0.6\,\text{s}$, Coral border | **Click 3** |
| **PAUSE**| **Socratic Misconception Check** | — | Lecturer writes in scratchpad: "Is $f'(c) = 0$ a sufficient condition? NO! It is only necessary for differentiable extrema. What else do we need? A SIGN CHANGE!" | **Live Pause** |

---

### Slide 10: The First Derivative Test (FDT) & The Visual Sign Chart
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** 3 styled vertical diagnostic cards showing the 3 fundamental sign-change behaviors of $f'(x)$ across a critical value $c$.

#### Layer Hierarchy & Key Objects
- Full slide visual container holding `assets/svg/09_first_derivative_sign_chart.svg`:
  - `card_fdt_max`: $(+) \to (-)$ transition $\implies$ Local Maximum (Peak icon)
  - `card_fdt_min`: $(-) \to (+)$ transition $\implies$ Local Minimum (Valley icon)
  - `card_fdt_terrace`: $(+) \to (+)$ or $(-) \to (-)$ $\implies$ Neither / Terrace point (Inflection)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Header + 3 column frames | Dissolve | Duration: $0.4\,\text{s}$ | On Slide Load |
| **1** | `card_fdt_max` (Number line + mountain) | Build In: Move In (Bottom) | Duration: $0.6\,\text{s}$, Ease Both | **Click 1** |
| **2** | `card_fdt_min` (Number line + valley) | Build In: Move In (Bottom) | Duration: $0.6\,\text{s}$, Ease Both | **Click 2** |
| **3** | `card_fdt_terrace` (Number line + terrace) | Build In: Move In (Bottom) | Duration: $0.6\,\text{s}$, Ease Both | **Click 3** |
| **PAUSE**| **Apple Pencil Finger-Trace Pause** | — | Lecturer traces an ascending path $(+)$, pauses at peak $(0)$, then descends $(-)$ to cement the physical intuition of a summit. | **Live Pause** |

---

### Slide 11: Master Worked Example (Part 1: Finding & Factoring)
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** 2-column layout. Left side: The algebraic derivation pipeline for $f(x) = x^3 - 3x$. Right side: Large scratchpad for live student calculation.

#### Layer Hierarchy & Key Objects
- `col_left_11` ($X=60, Y=140, W=880, H=860$, Fill `#111827`, Cyan accent)
  - `header_problem`: "Master Worked Example: $f(x) = x^3 - 3x$"
  - `step1_deriv`: "Step 1: Compute First Derivative" $\implies f'(x) = 3x^2 - 3$
  - `step2_factor`: "Step 2: Factor Completely" $\implies f'(x) = 3(x^2 - 1) = 3(x - 1)(x + 1)$
  - `step3_crit`: "Step 3: Solve $f'(x) = 0$" $\implies x = -1, \; x = +1$
- `col_right_11` ($X=980, Y=140, W=880, H=860$, Dedicated Scratchpad Zone with dot grid)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Header + Problem Statement | Appears on slide | — | On Slide Load |
| **1** | `step1_deriv` card | Build In: Wipe (Left to Right) | Duration: $0.5\,\text{s}$ | **Click 1** |
| **2** | `step2_factor` card | Build In: Wipe (Left to Right) | Duration: $0.6\,\text{s}$ | **Click 2** |
| **3** | `step3_crit` card | Build In: Wipe (Left to Right) | Duration: $0.6\,\text{s}$, Amber glow | **Click 3** |
| **PAUSE**| **Live Factoring & Interval Setup** | — | Lecturer uses Apple Pencil on right scratchpad to draw the real line $\mathbb{R}$, place vertical tick marks at $-1$ and $+1$, and define the 3 test intervals: $(-\infty, -1)$, $(-1, 1)$, and $(1, \infty)$. | **Live Pause** |

---

### Slide 12: Master Worked Example (Part 2: Sign Chart to 2D Graph Morph)
- **Transition In:** Magic Move ($1.2\,\text{s}$) from Slide 11. The critical numbers $x = -1, +1$ smoothly travel into the graph axes and table headers!
- **Visual Design:** Left side: Synchronized dual graph ($f(x)$ cubic aligned vertically above $f'(x)$ parabola). Right side: Sign chart table and coordinate evaluations.

#### Layer Hierarchy & Key Objects
- `vector_graph_12` ($X=60, Y=140, W=920, H=860$, contains `assets/svg/10_worked_example_cubic.svg`)
  - `+curve_fx_cubic` (Cubic curve $f(x)$ in Cyan `#38BDF8`)
  - `+curve_fprime_parabola` (Parabola $f'(x) = 3x^2 - 3$ in Amber dashed line)
  - `+sync_line_neg1` (Vertical dashed line at $x = -1$ linking $f'(-1)=0$ to Local Max at $(-1, 2)$)
  - `+sync_line_pos1` (Vertical dashed line at $x = +1$ linking $f'(1)=0$ to Local Min at $(1, -2)$)
- `right_card_12` ($X=1020, Y=140, W=840, H=860$)
  - `table_sign_chart`: 3-column table showing test points $x = -2, 0, +2$, sign of $f'$, and physical behavior.
  - `eval_max_box`: $f(-1) = (-1)^3 - 3(-1) = +2 \implies \mathbf{(-1, 2)}$ LOCAL MAX
  - `eval_min_box`: $f(1) = (1)^3 - 3(1) = -2 \implies \mathbf{(1, -2)}$ LOCAL MIN
  - `scratchpad_zone_12` ($X=1060, Y=620, W=760, H=340$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Graph axes + Table headers | Magic Move | Morphs from Slide 11 | Automatic |
| **1** | `table_sign_chart` rows | Build In: Wipe (Top to Bottom) | Duration: $0.7\,\text{s}$ | **Click 1** |
| **2** | `+sync_line_neg1` & `eval_max_box` | Build In: Draw Line + Scale | Duration: $0.6\,\text{s}$, Amber glow | **Click 2** |
| **3** | `+sync_line_pos1` & `eval_min_box` | Build In: Draw Line + Scale | Duration: $0.6\,\text{s}$, Cyan glow | **Click 3** |
| **PAUSE**| **Geometric Synchronization Pause** | — | Lecturer highlights the vertical alignment: where $f'$ crosses the zero line, the tangent to $f$ is horizontal. Emphasize that $f$ values come from original $f(x)$, NOT $f'(x)$! | **Live Pause** |

---

### Slide 13: Concavity & The Second Derivative ($f''(x)$)
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** Side-by-side comparative cards: Left: Concave Down ($f'' < 0$, slopes decreasing, tangents above curve, traps a Maximum). Right: Concave Up ($f'' > 0$, slopes increasing, tangents below curve, traps a Minimum).

#### Layer Hierarchy & Key Objects
- Full slide visual container holding `assets/svg/11_second_derivative_concavity.svg`:
  - Panel Left: Concave Down (Amber theme, inverted cup, tangents lying above curve).
  - Panel Right: Concave Up (Cyan theme, upright cup, tangents lying below curve).
- `bottom_tray_13` ($X=60, Y=760, W=1800, H=260$, formulas and Apple Pencil scratchpad)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Visual container + Headings | Dissolve | Duration: $0.4\,\text{s}$ | On Slide Load |
| **1** | Panel Left: Concave Down tangents | Build In: Trace Vector Path | Duration: $0.7\,\text{s}$, Amber glow | **Click 1** |
| **2** | Panel Right: Concave Up tangents | Build In: Trace Vector Path | Duration: $0.7\,\text{s}$, Cyan glow | **Click 2** |
| **3** | Summary conclusion cards | Build In: Move In (Bottom) | Duration: $0.5\,\text{s}$ | **Click 3** |
| **PAUSE**| **Mnemonic & Bending Pause** | — | Lecturer writes in scratchpad: "Second derivative is the ACCELERATION of the curve: $f''(x) = \frac{d}{dx}[f'(x)]$. If velocity decreases, you are rounding a crest." | **Live Pause** |

---

### Slide 14: The Second Derivative Test & Comparison Matrix
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** Left card: Applying SDT to $f(x) = x^3 - 3x$ ($f''(x) = 6x$). Right card: The Failure Modes of SDT and FDT vs SDT Decision Matrix.

#### Layer Hierarchy & Key Objects
- `col_left_14` ($X=60, Y=140, W=880, H=860$, Fill `#111827`, Amber accent)
  - `sdt_computation`: $f''(x) = \frac{d}{dx}[3x^2 - 3] = 6x$
  - `sdt_eval_neg1`: $f''(-1) = 6(-1) = -6 < 0 \implies \mathbf{LOCAL\;MAX}$ at $(-1, 2)$
  - `sdt_eval_pos1`: $f''(1) = 6(1) = +6 > 0 \implies \mathbf{LOCAL\;MIN}$ at $(1, -2)$
- `col_right_14` ($X=980, Y=140, W=880, H=860$, Fill `#111827`)
  - `sdt_failure_box`: What if $f''(c) = 0$? (Test Inconclusive!)
  - `counter_examples_row`: $x^4$ (Min), $-x^4$ (Max), $x^3$ (Neither), all have $f''(0) = 0$.
  - `scratchpad_zone_14` ($X=1020, Y=480, W=800, H=480$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Base cards & Headings | Appears with slide | — | On Slide Load |
| **1** | `sdt_computation` & `_eval_neg1` | Build In: Wipe (Left to Right) | Duration: $0.6\,\text{s}$ | **Click 1** |
| **2** | `sdt_eval_pos1` | Build In: Wipe (Left to Right) | Duration: $0.6\,\text{s}$ | **Click 2** |
| **3** | `sdt_failure_box` & counterexamples | Build In: Move In (From Right) | Duration: $0.6\,\text{s}$, Coral border | **Click 3** |
| **PAUSE**| **Test Selection Guidance Pause** | — | Lecturer writes in scratchpad: "Rule of Thumb: If $f'(x)$ is easy to differentiate again, SDT is fast! If $f'(x)$ required a hideous quotient rule, stick with the First Derivative Test." | **Live Pause** |

---

### Slide 15: Absolute Extrema on Closed Intervals (Endpoint Traps)
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** Left side: Graph of $f(x) = x^3 - 3x$ restricted to closed domain $[-0.5, 2.5]$. Right side: The 3-Step Candidate Evaluation Table.

#### Layer Hierarchy & Key Objects
- `vector_graph_15` ($X=60, Y=140, W=920, H=860$, contains `assets/svg/12_closed_interval_endpoints.svg`)
  - Shaded domain region $[-0.5, 2.5]$
  - Excluded interior point $x = -1$ marked with red cross
  - Interior critical candidate $x = 1 \implies f(1) = -2$
  - Boundary endpoints: $x = -0.5 \implies f(-0.5) = 1.375$; $x = 2.5 \implies f(2.5) = 8.125$
- `right_card_15` ($X=1020, Y=140, W=840, H=860$)
  - `evt_protocol_box`: Extreme Value Theorem 3-step algorithm
  - `candidate_table`: Rows for $x = -1$ (Excluded), $-0.5$, $1$, $2.5$
  - `verdict_banner`: ABS MAX = $8.125$ at $x = 2.5$; ABS MIN = $-2$ at $x = 1$
  - `scratchpad_zone_15` ($X=1060, Y=620, W=760, H=340$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Graph + Table base | Appears with slide | — | On Slide Load |
| **1** | Domain shading & Red X on $x=-1$ | Build In: Dissolve + Scale | Duration: $0.6\,\text{s}$, Coral stroke | **Click 1** |
| **2** | Interior candidate evaluation ($x=1$) | Build In: Wipe (Left to Right) | Duration: $0.5\,\text{s}$, Cyan glow | **Click 2** |
| **3** | Endpoint evaluation ($x=-0.5, 2.5$) | Build In: Wipe (Left to Right) | Duration: $0.6\,\text{s}$, Coral glow | **Click 3** |
| **PAUSE**| **Engineering Danger Discussion** | — | Lecturer circles $x = 2.5$ with Apple Pencil: "Notice that $f'(2.5) = 3(2.5)^2 - 3 = 15.75 \ne 0$! The absolute peak has a steep slope! If you only tested $f'=0$, you would miss the structural failure point!" | **Live Pause** |

---

### Slide 16: Engineering Optimization Application: Maximum Power Transfer
- **Transition In:** Magic Move ($1.2\,\text{s}$)
- **Visual Design:** Left card: Thevenin Equivalent circuit diagram with source $V_s$, internal resistance $R_s$, and variable load resistor $R_L$. Right card: Power characteristic curve $P(R_L)$ and calculus derivation.

#### Layer Hierarchy & Key Objects
- `vector_graph_16` ($X=60, Y=140, W=920, H=860$, contains `assets/svg/13_engineering_max_power.svg`)
  - Circuit schematic (Thevenin source + load)
  - Power curve $P(R_L) = \frac{V_s^2 R_L}{(R_s + R_L)^2}$ peaking at $R_L = R_s$
- `right_card_16` ($X=1020, Y=140, W=840, H=860$)
  - `power_formula_box`: $P(R_L) = I^2 R_L = \frac{V_s^2 R_L}{(R_s + R_L)^2}$
  - `deriv_quotient_box`: $\frac{dP}{dR_L} = V_s^2 \frac{(R_s + R_L)^2(1) - R_L \cdot 2(R_s + R_L)}{(R_s + R_L)^4} = V_s^2 \frac{R_s - R_L}{(R_s + R_L)^3}$
  - `impedance_match_box`: $\frac{dP}{dR_L} = 0 \implies \mathbf{R_L = R_s}$ (Impedance Matching!)
  - `scratchpad_zone_16` ($X=1060, Y=580, W=760, H=380$)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Circuit diagram & Graph base | Appears with slide | — | On Slide Load |
| **1** | `power_formula_box` | Build In: Wipe (Left to Right) | Duration: $0.5\,\text{s}$ | **Click 1** |
| **2** | `deriv_quotient_box` | Build In: Wipe (Left to Right) | Duration: $0.7\,\text{s}$ | **Click 2** |
| **3** | `impedance_match_box` & peak glow | Build In: Scale Up + Amber Glow | Duration: $0.6\,\text{s}$ | **Click 3** |
| **PAUSE**| **Real-World Application Pause** | — | Lecturer writes in scratchpad: "Why is this vital? Audio speakers ($8\,\Omega$), RF antennas ($50\,\Omega$), and solar PV Maximum Power Point Tracking (MPPT) all operate on this exact calculus result!" | **Live Pause** |

---

### Slide 17: Guided Practice: Sheet Metal Packaging Optimization
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** Progressive disclosure. Problem statement on left; Hints 1, 2, 3 revealed sequentially as students work through their algebra.

#### Layer Hierarchy & Key Objects
- `col_left_17` ($X=60, Y=140, W=880, H=860$, Fill `#111827`, Amber accent)
  - `problem_statement`: Sheet $12 \times 12\,\text{cm}$, cut corner squares of size $x$. Fold to maximize volume $V(x) = x(12 - 2x)^2$.
  - `hint_1_box`: Domain is $x \in [0, 6]$. Expanded: $V(x) = 4(x^3 - 12x^2 + 36x)$.
  - `hint_2_box`: Derivative: $V'(x) = 12(x^2 - 8x + 12) = 12(x - 2)(x - 6)$.
  - `hint_3_box`: Critical points in $(0, 6)$: $x = 2$. Compare $V(0)=0$, $V(6)=0$, $V(2) = 128\,\text{cm}^3$.
- `col_right_17` ($X=980, Y=140, W=880, H=860$, Full Apple Pencil active scratchpad)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Problem statement + Sheet diagram | Appears on slide | — | On Slide Load |
| **1** | `hint_1_box` (Model & Domain) | Build In: Move In (Bottom) | Duration: $0.5\,\text{s}$ | **Click 1** |
| **2** | `hint_2_box` (Derivative & Factor) | Build In: Move In (Bottom) | Duration: $0.5\,\text{s}$ | **Click 2** |
| **3** | `hint_3_box` (Extrema & Comparison) | Build In: Move In (Bottom) | Duration: $0.5\,\text{s}$, Amber glow | **Click 3** |
| **PAUSE**| **3-Minute Student Solve Pause** | — | Lecturer circulates room or observes student engagement; writes folded box dimensions in scratchpad: Length $= 8\,\text{cm}$, Width $= 8\,\text{cm}$, Height $= 2\,\text{cm}$. | **Live Pause** |

---

### Slide 18: Independent Engineering Challenge: Beam Deflection
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** High-level engineering problem: A simply supported beam of length $L$ under uniform load $w_0$ has deflection $y(x) = \frac{w_0}{24EI}(x^4 - 2Lx^3 + L^3x)$ on $[0, L]$.

#### Layer Hierarchy & Key Objects
- `col_left_18` ($X=60, Y=140, W=880, H=860$, Fill `#111827`, Coral accent)
  - `beam_diagram`: Beam schematic with support pins at $x = 0$ and $x = L$, uniform load arrows.
  - `beam_equation`: $y(x) = k(x^4 - 2Lx^3 + L^3x)$
  - `beam_tasks`: Tasks 1, 2, 3 (Differentiate, prove symmetry at $x = L/2$, find $y_{\max}$).
  - `solution_reveal_card`: Hidden until final lecturer tap.
- `col_right_18` ($X=980, Y=140, W=880, H=860$, Full Apple Pencil active scratchpad)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Beam diagram + Equation | Appears on slide | — | On Slide Load |
| **1** | `solution_reveal_card` (First stage) | Build In: Wipe (Left to Right) | $y'(x) = k(4x^3 - 6Lx^2 + L^3)$ | **Click 1** |
| **2** | `solution_reveal_card` (Final answer) | Build In: Scale Up + Amber Glow | $y_{\max} = \frac{5 w_0 L^4}{384 E I}$ at $x = L/2$ | **Click 2** |
| **PAUSE**| **Midpoint Symmetry Analysis** | — | Lecturer writes in scratchpad: Factor $(2x - L)$ out of the cubic; show that the remaining quadratic roots are $x = \frac{1 \pm \sqrt{3}}{2}L$, which lie outside the beam $[0, L]$. Midpoint is the sole interior extremum! | **Live Pause** |

---

### Slide 19: The Engineering Optimization Protocol (Flowchart)
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** Complete algorithmic flowchart mapping the 4-step decision tree from physical equation to final engineering verdict, accompanied by the Extrema Test Selection Matrix.

#### Layer Hierarchy & Key Objects
- Full slide visual container holding `assets/svg/14_optimization_flowchart.svg`:
  - Step 1: Model & Physical Domain $[a, b]$
  - Step 2: Differentiate & Find Critical Numbers ($f'=0$ or DNE)
  - Step 3: Classify (FDT Sign Chart vs SDT Curvature)
  - Step 4: Evaluate Boundaries & Compare All Candidates
  - Bottom Matrix: FDT (Universal) vs SDT (Fast Shortcut)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Complete Flowchart | Appears with slide | — | On Slide Load |
| **1** | Flowchart Steps 1 & 2 Highlight | Action: Pulse | Duration: $0.6\,\text{s}$, Cyan border | **Click 1** |
| **2** | Flowchart Step 3 Highlight | Action: Pulse | Duration: $0.6\,\text{s}$, Amber border | **Click 2** |
| **3** | Flowchart Step 4 Highlight | Action: Pulse | Duration: $0.6\,\text{s}$, Coral border | **Click 3** |
| **PAUSE**| **Flowchart Summary Pause** | — | Lecturer advises students to capture a screenshot on iPad for their exam summary cheat sheet. | **Live Pause** |

---

### Slide 20: Conceptual Exit Ticket & Diagnostic Quiz
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** 3 interactive diagnostic question cards targeting common calculus misconceptions. Answers revealed one by one on lecturer tap.

#### Layer Hierarchy & Key Objects
- `q_card_1` ($X=60, Y=180, W=560, H=780$, Question: "If $f'(3) = 0$, is $x=3$ definitely an extremum?")
- `q_card_2` ($X=680, Y=180, W=560, H=780$, Question: "If $f'(c) = 0$ and $f''(c) = 0$, what does SDT conclude?")
- `q_card_3` ($X=1300, Y=180, W=560, H=780$, Question: "Can an absolute maximum occur where $f'(x) \ne 0$?")

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | 3 Question Cards (Questions only) | Dissolve | Duration: $0.4\,\text{s}$ | On Slide Load |
| **1** | Card 1 Answer Reveal | Build In: Move In (Bottom) | "NO! e.g. $(x-3)^3$" (Coral) | **Click 1** |
| **2** | Card 2 Answer Reveal | Build In: Move In (Bottom) | "INCONCLUSIVE! Must use FDT." (Amber) | **Click 2** |
| **3** | Card 3 Answer Reveal | Build In: Move In (Bottom) | "YES! Endpoints & Singularities." (Cyan) | **Click 3** |
| **PAUSE**| **Class Poll Pause** | — | Lecturer polls students before revealing each answer box. | **Live Pause** |

---

### Slide 21: Full Reference Solutions & Derivation Appendix
- **Transition In:** Dissolve ($0.5\,\text{s}$)
- **Visual Design:** Dense, high-contrast, clean 2-column reference card displaying uncompressed mathematical proofs and algebraic steps for all practice problems.

#### Layer Hierarchy & Key Objects
- `ref_card_left`: Complete packaging box derivation, factoring proof, and boundary values.
- `ref_card_right`: Complete beam deflection derivation, quotient factorization, and structural deflection constant proof.

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Both reference cards | Dissolve | All content visible immediately | On Slide Load |
| **PAUSE**| **Reference Note** | — | Lecturer notes that these full derivations are in the distributed PDF notes. | **Live Pause** |

---

### Slide 22: Closing Synthesis & Next Horizon
- **Transition In:** Push (Right to Left, $0.8\,\text{s}$)
- **Visual Design:** Left card: Today's single-variable mastery summary. Right card: Sneak peek into multivariable engineering calculus ($\nabla f = \mathbf{0}$, Hessian matrices, Saddle points).

#### Layer Hierarchy & Key Objects
- `col_left_22` ($X=60, Y=180, W=880, H=780$, Fill `#111827`, Cyan border, 5 Key Single-Variable Takeaways)
- `col_right_22` ($X=980, Y=180, W=880, H=780$, Fill `#111827`, Amber border, Multivariable Horizons preview)

#### Build Sequence & Triggers
| Step | Object | Animation Type | Parameters / Timing | Trigger |
| :--- | :--- | :--- | :--- | :--- |
| **0** | Both summary cards | Dissolve | Duration: $0.5\,\text{s}$ | On Slide Load |
| **1** | Next Horizon Items | Build In: Wipe (Left to Right) | Gradient vector $\nabla f = \mathbf{0}$ | **Click 1** |
| **2** | Final Lecture Adjournment | Build In: Scale Up + Glow | "Class Dismissed // Practice Set Available on Portal" | **Click 2** |

---

## 5. Keynote Export & iPad Presentation Best Practices

1. **AirPlay vs Direct USB-C:** For zero latency when writing with Apple Pencil, connect the iPad to the lecture hall projector via a high-bandwidth USB-C to HDMI cable ($4\text{K}@60\text{Hz}$), rather than AirPlay mirroring.
2. **Keynote Presenter Display Settings:** In Keynote for iPad settings, configure the iPad screen to show **Current Slide + Notes + Scratchpad Tool**, while the projector screen displays only the clean **Current Slide**.
3. **Pencil Tool Selection:** Use the Keynote native Pen tool set to **$3\,\text{pt}$ width** with `#38BDF8` Cyan or `#F59E0B` Amber ink for optimal visibility against the dark background.
4. **Instant Shape Recognition:** In Keynote on iPad, holding the Apple Pencil down at the end of a stroke automatically snaps rough drawings into perfect geometric arrows, circles, and coordinate axes.
