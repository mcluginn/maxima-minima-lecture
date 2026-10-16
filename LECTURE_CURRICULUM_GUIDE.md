# Master Curriculum & Instructional Design Guide
## Maxima & Minima: Turning Points, Curvature & Engineering Optimization

**Target Course:** Differential Calculus for Engineers (MATH 101 / ENGR 110)  
**Session Duration:** 50–60 Minutes (Adaptable to 45-minute modular schedules)  
**Primary Presentation Interface:** Apple Keynote on iPad with Apple Pencil live annotation  
**Visual & Motion Aesthetic:** 3Blue1Brown mathematical narrative meets dark-mode high-end aerospace interface  

---

## 1. Executive Pedagogical Framework

### 1.1 Course Objectives & Bloom's Taxonomy Alignment
By the conclusion of this 50-minute lecture, engineering students will be able to:

1. **Understand (Conceptual / Geometric):** Connect the vanishing of the instantaneous rate of change ($f'(x) = 0$) and derivative non-existence to the physical geometry of stationary turning points and singular stress concentrations (**Bloom Level 2**).
2. **Apply (Procedural):** Construct, compute, and interpret first derivative sign charts and second derivative curvature evaluations to unambiguously classify critical points as local maxima, local minima, or stationary inflections (**Bloom Level 3**).
3. **Analyze (Diagnostic):** Distinguish between local extrema and absolute extrema on restricted physical domains $[a, b]$, identifying when catastrophic peak loads occur at domain boundaries rather than stationary points (**Bloom Level 4**).
4. **Evaluate & Create (Engineering Synthesis):** Formulate mathematical objective functions from physical constraints (such as circuit impedance matching, beam deflection under distributed loads, and structural packaging volume) and execute the complete 4-step Optimization Protocol (**Bloom Levels 5 & 6**).

---

### 1.2 Lecture Timeline & Pacing Matrix (50-Minute Master Schedule)

```
00:00 - 03:00  [03 min]  Pillar 1: The Geometry of Turning (Slides 01 - 03)
03:00 - 08:00  [05 min]  Local vs Global Extrema & Slopes (Slides 04 - 05)
08:00 - 15:00  [07 min]  Fermat's Theorem, Critical Numbers & The Singularities (Slides 06 - 08)
15:00 - 20:00  [05 min]  The Stationary Inflection Trap & First Derivative Test (Slides 09 - 10)
20:00 - 28:00  [08 min]  Master Worked Example: f(x) = x³ - 3x Dual-Graph Morph (Slides 11 - 12)
28:00 - 34:00  [06 min]  Curvature, Concavity & Second Derivative Test (Slides 13 - 14)
34:00 - 40:00  [06 min]  Closed Intervals & The Extreme Value Theorem (Slide 15)
40:00 - 46:00  [06 min]  Engineering Optimization: Maximum Power Transfer (Slide 16)
46:00 - 52:00  [06 min]  Guided Practice, Beam Deflection & Algorithmic Map (Slides 17 - 19)
52:00 - 55:00  [03 min]  Exit Ticket Diagnostics & Next Horizons (Slides 20 - 22)
```

---

## 2. Slide-by-Slide Detailed Instructional Scripts

---

### Slide 01: The Landscape of Optimization (Opening Hook)
- **Time Allocated:** 00:00 – 02:00 (2 minutes)
- **Primary Objective:** Hook students with the physical reality of turning behavior and establish the visual visual language.
- **Visual Storyboard:** Dark midnight canvas. A continuous polynomial terrain curve glows in Electric Cyan. A glowing probe particle moves along the curve with an attached tangent vector rotating dynamically. At the summit, the tangent snaps to horizontal ($m = 0$) and pulses in Neon Amber.

#### Verbatim Lecturer Script
> "Good morning, engineers. Look at this curve on the screen. Imagine this represents the potential energy of a mechanical linkage, the voltage curve across an internal combustion sensor, or the thermal gradient along a rocket nozzle.
> 
> As our state variable moves along the trajectory, the system is continuously changing. But notice what happens at the summits and the troughs. The system hesitates. For an infinitesimal instant, the rate of change vanishes. The slope is zero.
> 
> Today, we move beyond simply computing derivatives. Today, we turn calculus into a decision-making engine. We will answer the fundamental engineering question: Where does nature pause, and how do we systematically find the points of maximum performance, maximum efficiency, or catastrophic structural failure?"

#### Socratic Prompts & Cold Calls
- *"If you are hiking along this mountain ridge in thick fog, how do you know with your feet that you have reached the exact summit without looking around?"*  
  *(Target response: Your slope flattens to zero; taking a step forward or backward both lead downhill).*

#### Apple Pencil Live Annotation Plan
- In the dedicated top-right scratchpad area, write the fundamental definition of the derivative:
  $$\lim_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = 0$$
- Draw an arrow from the moving pink particle to the summit circle $(400, 340)$, writing $\text{Slope } m = 0$.

---

### Slide 02: Lecture Architecture & The Central Question
- **Time Allocated:** 02:00 – 03:30 (1.5 minutes)
- **Primary Objective:** Provide cognitive scaffolding and set student expectations for the four core pillars.

#### Verbatim Lecturer Script
> "Before we dive into the algebra, here is our battle plan. Engineering calculus rests on four pillars today:
> 
> First, the **Geometry of Turning**: Fermat's Theorem and how horizontal tangents arise.
> Second, our **Classification Engines**: The First Derivative Test—which uses sign charts—and the Second Derivative Test, which uses curvature.
> Third, **Boundary Constraints**: Why the most dangerous trap in engineering optimization is forgetting the endpoints of a physical interval.
> And fourth, **Physical Modeling**: Applying these mathematical engines to the Maximum Power Transfer Theorem in circuit design."

#### Common Misconceptions to Address
- *Misconception:* "Every engineering problem can be solved by just taking the derivative and setting it to zero."  
- *Correction:* Remind students that physical systems are bounded (e.g. a valve cannot open past 100%; a transistor has maximum supply rail voltage). Extrema often occur at boundaries where derivatives are non-zero!

#### Apple Pencil Live Annotation Plan
- Under Pillar 3, write in vivid coral ink:
  $$\text{Interval: } x \in [a, b] \implies \text{CHECK ENDPOINTS!}$$

---

### Slide 03: Intuitive Meaning: Peaks, Troughs & Equilibrium
- **Time Allocated:** 03:30 – 05:30 (2 minutes)
- **Primary Objective:** Ground abstract mathematical extrema into mechanical, electrical, and chemical physical domains.

#### Verbatim Lecturer Script
> "Why does an engineer care about extrema? Because in physical nature, an extremum is almost always an **equilibrium state**.
> 
> In mechanical structures, conservative force is the negative gradient of potential energy: $F = -dU/dx$. If $dU/dx = 0$, net force is zero. If you are at a local minimum of energy, a perturbation brings you back—you have stable equilibrium, like a ball sitting at the bottom of a bowl. If you are at a local maximum of energy, the slightest disturbance causes an avalanche—unstable equilibrium.
> 
> In electronics, we want to maximize the power delivered to a load resistor while minimizing internal heat loss. In chemical engineering, we seek the peak reaction yield before high temperatures degrade our catalyst. Extrema are the sweet spots of the physical universe."

#### Socratic Prompts & Cold Calls
- *"What happens if a bridge design has an unstable potential energy equilibrium at its operating load?"*  
  *(Target response: Any wind gust or harmonic vibration will trigger divergence and collapse, as in the Tacoma Narrows Bridge).*

#### Apple Pencil Live Annotation Plan
- Under the Mechanical card, sketch a cross-section of a concave-up bowl with a marble at the bottom (stable) vs an inverted bowl with a marble balanced on top (unstable).

---

### Slide 04: Local vs. Absolute (Global) Extrema
- **Time Allocated:** 05:30 – 08:00 (2.5 minutes)
- **Primary Objective:** Formulate the rigorous difference between neighborhood-restricted extrema and domain-wide extrema.

#### Verbatim Lecturer Script
> "Look carefully at Slide 04. We must establish a clear legal distinction between **Local** and **Absolute** extrema.
> 
> A point $c$ is a **Local Maximum** if $f(c) \ge f(x)$ for all $x$ in some open neighborhood $(c-\delta, c+\delta)$ surrounding $c$. You are the tallest person in your immediate room.
> 
> But an **Absolute Maximum** on domain $D$ means $f(c) \ge f(x)$ for every single $x$ in the entire domain. You are the tallest person on the planet.
> 
> Now, look at the graph on the left. Point $B$ is an interior peak—it is a local maximum. But look all the way to the right at boundary point $D$, where $x = b$. Point $D$ towers over Point $B$. Point $D$ is the Absolute Maximum of the system! If an engineer only checked where the tangent was flat, they would report Point $B$ and completely miss the catastrophic maximum at Point $D$."

#### Apple Pencil Live Annotation Plan
- Around the interior peak at $x = c_1$, sketch a dashed open interval with double arrows labeled $(c_1 - \delta, c_1 + \delta)$.
- Draw a horizontal dashed line extending from the right endpoint $D$ across the screen to demonstrate that it exceeds every interior crest.

---

### Slide 05: Increasing and Decreasing Functions
- **Time Allocated:** 08:00 – 10:00 (2 minutes)
- **Primary Objective:** Connect the algebraic sign of $f'(x)$ to directional monotonicity via the Mean Value Theorem.

#### Verbatim Lecturer Script
> "How does a function climb and fall? Through the sign of its first derivative.
> 
> By the Mean Value Theorem, for any two points $x_1 < x_2$, there exists an intermediate point $c$ such that:
> $$\frac{f(x_2) - f(x_1)}{x_2 - x_1} = f'(c)$$
> Since the denominator $x_2 - x_1$ is positive, the sign of $f(x_2) - f(x_1)$ is strictly dictated by the sign of $f'(c)$.
> 
> If $f'(x) > 0$ throughout an interval, the function is strictly increasing—it ascends. If $f'(x) < 0$, the function is strictly decreasing—it descends. And therefore, if a continuous, smooth function transitions from ascending to descending, it MUST pass through zero."

#### Apple Pencil Live Annotation Plan
- In the scratchpad, draw a small secant chord connecting $(x_1, f(x_1))$ to $(x_2, f(x_2))$, writing:
  $$\Delta x > 0 \quad \text{and} \quad f'(c) > 0 \implies \Delta y > 0 \implies f(x_2) > f(x_1)$$

---

### Slide 06: Fermat's Theorem on Stationary Points
- **Time Allocated:** 10:00 – 12:30 (2.5 minutes)
- **Primary Objective:** Present Fermat's Theorem and its rigorous one-sided limit geometric proof.

#### Verbatim Lecturer Script
> "In 1636, nearly three decades before Newton and Leibniz formalized the calculus, French mathematician Pierre de Fermat stated an astonishing geometric truth:
> 
> **Fermat's Theorem:** If $f$ attains a local extremum at an interior point $c$, and if $f'(c)$ exists, then $f'(c) = 0$.
> 
> Why must this be true? Think about the derivative as the limit of the difference quotient.
> Approaching a maximum from the left, $f(c+h) - f(c) \le 0$ while $h < 0$, so the left-hand limit is $\ge 0$.
> Approaching from the right, $f(c+h) - f(c) \le 0$ while $h > 0$, so the right-hand limit is $\le 0$.
> Since $f'(c)$ exists, both one-sided limits must be identical. What is the only real number that is simultaneously greater than or equal to zero and less than or equal to zero?
> Exactly zero."

#### Socratic Prompts & Cold Calls
- *"What are the two hidden escape clauses in Fermat's theorem?"*  
  *(Target response: 1. It only applies to INTERIOR points, not boundary endpoints; 2. It requires that the derivative actually EXISTS).*

#### Apple Pencil Live Annotation Plan
- In the scratchpad area, write the squeeze argument:
  $$\lim_{h \to 0^-} \frac{f(c+h)-f(c)}{h} \ge 0 \quad \text{and} \quad \lim_{h \to 0^+} \frac{f(c+h)-f(c)}{h} \le 0 \implies f'(c) = 0$$

---

### Slide 07: Critical Numbers: The Complete Definition
- **Time Allocated:** 12:30 – 14:30 (2 minutes)
- **Primary Objective:** Deliver the comprehensive two-part definition of critical numbers and emphasize domain inclusion.

#### Verbatim Lecturer Script
> "Because extrema can occur either where the tangent is horizontal OR where the tangent fails to exist, mathematicians formulated the concept of a **Critical Number**.
> 
> Let $f$ be defined on an open interval containing $c$. Then $c$ is a critical number if:
> 1. $f'(c) = 0$ (a Stationary Point), OR
> 2. $f'(c)$ does not exist (a Singular Point).
> 
> But pay close attention to the fine print: **$c$ MUST be in the domain of $f$!**
> Consider $f(x) = 1/x$. Its derivative is $f'(x) = -1/x^2$. At $x = 0$, the derivative does not exist. Does that make $x = 0$ a critical number?
> Absolutely not! Because $f(0)$ is undefined. The function doesn't even exist at $x = 0$. Never claim an asymptote is a critical number."

#### Apple Pencil Live Annotation Plan
- In red ink on the right scratchpad, write:
  $$f(x) = \frac{1}{x} \implies 0 \notin \text{Domain}(f) \implies x=0 \text{ is NOT a critical number!}$$

---

### Slide 08: When the Derivative Fails to Exist (DNE)
- **Time Allocated:** 14:30 – 17:00 (2.5 minutes)
- **Primary Objective:** Illustrate corners and cusps, demonstrating that non-differentiable points frequently harbor extrema.

#### Verbatim Lecturer Script
> "Why do engineers care about points where derivatives fail? Because nature and structures are full of sharp corners, mechanical stops, diode switching thresholds, and impact shocks.
> 
> Look at Case A: $f(x) = |x|$. The slope to the left of the origin is strictly $-1$. The slope to the right is strictly $+1$. At $x = 0$, the two one-sided derivatives clash. The derivative does not exist. And yet, what is $(0, 0)$? It is the absolute, undisputed global minimum of the function!
> 
> Look at Case B: $f(x) = x^{2/3}$. Differentiating gives $f'(x) = \frac{2}{3x^{1/3}}$. As $x$ approaches zero, the tangent line becomes completely vertical ($m \to \pm\infty$). The derivative fails. Yet $(0, 0)$ is a sharp cusp minimum.
> 
> The lesson for your engineering career: **Never throw away points where derivatives blow up.** That is often where physical failure occurs."

#### Apple Pencil Live Annotation Plan
- Trace over the V-notch of $|x|$ with a cyan pencil.
- Write next to the cusp:
  $$\lim_{x \to 0^+} \frac{2}{3\sqrt[3]{x}} = +\infty, \quad \lim_{x \to 0^-} \frac{2}{3\sqrt[3]{x}} = -\infty \implies \text{Vertical Tangent (DNE)}$$

---

### Slide 09: The Necessary vs. Sufficient Trap: $f(x) = x^3$
- **Time Allocated:** 17:00 – 19:30 (2.5 minutes)
- **Primary Objective:** Destroy the most persistent student misconception in calculus: that $f'(c) = 0$ guarantees an extremum.

#### Verbatim Lecturer Script
> "Now we confront the single biggest trap on engineering exams.
> 
> Many students assume that if they solve $f'(x) = 0$ and find a root, they have found a maximum or minimum.
> That is dead wrong.
> 
> Look at $f(x) = x^3$.
> Let's take its derivative: $f'(x) = 3x^2$.
> Set it to zero: $3x^2 = 0 \implies x = 0$.
> At the origin, the tangent line is as flat as a billiard table: $m = 0$.
> 
> But is $(0, 0)$ a peak? No.
> Is it a valley? No.
> For $x < 0$, $(-0.1)^3 < 0$. For $x > 0$, $(+0.1)^3 > 0$.
> The derivative $f'(x) = 3x^2$ is POSITIVE for all $x \ne 0$. The curve was climbing, it stalled for an infinitesimal instant at the origin, and then it kept climbing!
> This is a **stationary inflection point** or terrace point.
> 
> Memorize this sentence: **$f'(c) = 0$ provides candidates for extrema. It does not provide guarantees.** We need a classification engine."

#### Socratic Prompts & Cold Calls
- *"Can you name another function that has a horizontal tangent without an extremum?"*  
  *(Target response: $f(x) = x^5$, or $f(x) = \sin(x) - x$).*

#### Apple Pencil Live Annotation Plan
- Draw a big red warning box in the scratchpad:
  $$\text{Stationary Point } (f'=0) \ne \text{Extremum!}$$
- Sketch the tangent line $y = 0$ cutting straight through the cubic inflection.

---

### Slide 10: The First Derivative Test (FDT) & The Visual Sign Chart
- **Time Allocated:** 19:30 – 22:30 (3 minutes)
- **Primary Objective:** Establish the First Derivative Test as the universal, fail-safe classification engine.

#### Verbatim Lecturer Script
> "Because $f'(c) = 0$ is only a candidate, we must test how the derivative behaves across the neighborhood of $c$. This is the **First Derivative Test**.
> 
> Imagine walking across the terrain from left to right:
> 
> **Case 1:** If $f'(x)$ switches from Positive $(+)$ to Negative $(-)$, you were ascending, you crested the ridge, and now you are descending. You have reached a **Local Maximum**.
> 
> **Case 2:** If $f'(x)$ switches from Negative $(-)$ to Positive $(+)$, you were descending into a canyon, hit bottom, and are now climbing out. You have reached a **Local Minimum**.
> 
> **Case 3:** If $f'(x)$ does NOT change sign—it was $(+)$ and stays $(+)$, or was $(-)$ and stays $(-)$—the function merely hesitated on a terrace. You have **Neither** a maximum nor a minimum.
> 
> The First Derivative Test is universal. It works for smooth curves, it works for corners, and it works for cusps."

#### Apple Pencil Live Annotation Plan
- Under Case 1, draw a quick mountain peak $(\nearrow \searrow)$.
- Under Case 2, draw a quick valley trough $(\searrow \nearrow)$.
- Under Case 3, draw a step terrace $(\nearrow \nearrow)$.

---

### Slide 11: Master Worked Example (Part 1: Finding & Factoring)
- **Time Allocated:** 22:30 – 25:30 (3 minutes)
- **Primary Objective:** Demonstrate algebraic rigor in differentiation, factoring, and critical number isolation on $f(x) = x^3 - 3x$.

#### Verbatim Lecturer Script
> "Let's put this machinery into practice with our canonical engineering worked example:
> $$f(x) = x^3 - 3x$$
> 
> **Step 1:** Differentiate.
> Using the power rule:
> $$f'(x) = 3x^2 - 3$$
> 
> **Step 2:** Never leave your derivative expanded! Always factor it completely into irreducible linear terms. Factoring reveals signs instantly:
> $$f'(x) = 3(x^2 - 1) = 3(x - 1)(x + 1)$$
> 
> **Step 3:** Find critical numbers.
> Since $f(x)$ is a polynomial, its derivative is defined everywhere on $\mathbb{R}$—no singular DNE points.
> Setting $f'(x) = 0$:
> $$3(x - 1)(x + 1) = 0 \implies x_1 = -1, \quad x_2 = +1$$
> 
> We have isolated two candidate critical values. Now we turn to our iPad scratchpad to build our number line."

#### Apple Pencil Live Annotation Plan
- In the right scratchpad, draw a clean horizontal number line representing the domain $\mathbb{R}$.
- Mark tick marks at $x = -1$ and $x = +1$.
- Partition the real line into 3 intervals: $(-\infty, -1)$, $(-1, 1)$, and $(1, \infty)$.

---

### Slide 12: Master Worked Example (Part 2: Sign Chart to Graph Morph)
- **Time Allocated:** 25:30 – 28:30 (3 minutes)
- **Primary Objective:** Complete the sign chart, evaluate $y$-coordinates, and link the derivative parabola roots to the cubic curve turning points.

#### Verbatim Lecturer Script
> "Now watch how the algebra transforms into geometry.
> 
> Let's test the sign of $f'(x) = 3(x-1)(x+1)$ in each interval:
> 
> 1. In $(-\infty, -1)$, pick test value $x = -2$:
>    $$f'(-2) = 3(-3)(-1) = +9 > 0 \implies \text{Increasing } \nearrow$$
> 2. In $(-1, 1)$, pick test value $x = 0$:
>    $$f'(0) = 3(-1)(+1) = -3 < 0 \implies \text{Decreasing } \searrow$$
> 3. In $(1, \infty)$, pick test value $x = +2$:
>    $$f'(+2) = 3(+1)(+3) = +9 > 0 \implies \text{Increasing } \nearrow$$
> 
> At $x = -1$, the sign shifts from $(+)$ to $(-)$. That proves a **Local Maximum**!
> What is its coordinate? Plug $-1$ back into the ORIGINAL function $f(x)$, NOT $f'(x)$!
> $$f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2 \implies \mathbf{(-1, 2)}$$
> 
> At $x = +1$, the sign shifts from $(-)$ to $(+)$. That proves a **Local Minimum**!
> $$f(1) = (1)^3 - 3(1) = 1 - 3 = -2 \implies \mathbf{(1, -2)}$$
> 
> Look at the synchronized graph on the left. The roots of the amber derivative parabola coincide precisely with the peak and trough of our cyan cubic function!"

#### Common Misconceptions to Address
- *Massive Exam Error:* Students calculate the critical number $x = -1$, and then plug it into $f'(x)$ to find the $y$-coordinate, getting $0$ instead of the true function height $2$! Warn them: *The derivative gives the slope; the original function gives the altitude.*

#### Apple Pencil Live Annotation Plan
- Draw vertical dotted lines connecting $x = -1$ on the $x$-axis down to the peak at $(-1, 2)$ and up from the root of $f'$.
- Write in large chalk-white script:
  $$\text{Coordinates require } y = f(x), \text{ NEVER } f'(x)!$$

---

### Slide 13: Concavity & The Second Derivative ($f''(x)$)
- **Time Allocated:** 28:30 – 31:00 (2.5 minutes)
- **Primary Objective:** Provide geometric meaning to $f''(x)$ as the rate of change of tangent slopes (curvature).

#### Verbatim Lecturer Script
> "Now let us introduce our second classification engine: **The Second Derivative**.
> 
> What is $f''(x)$? It is the derivative of the derivative: $\frac{d}{dx}[f'(x)]$.
> It measures the **rate of change of the tangent slope**.
> 
> Look at the left panel: **Concave Down**.
> Follow the tangent lines from left to right: the slopes start steep positive, flatten to zero at the crest, and become negative. The slopes are strictly decreasing! If a quantity is decreasing, its derivative is negative:
> $$f''(x) < 0$$
> Tangent lines lie *above* the curve. If you have a horizontal tangent line trapped inside a concave-down region, the curve has nowhere to go but down. It traps a **Local Maximum**!
> 
> Now look at the right panel: **Concave Up**.
> Slopes start negative, pass through zero, and become positive. Slopes are increasing:
> $$f''(x) > 0$$
> Tangent lines lie *below* the curve. This geometric bowl holds water and traps a **Local Minimum**."

#### Apple Pencil Live Annotation Plan
- Under Concave Down, draw an inverted umbrella or bowl: $\cap \implies \text{Max}$.
- Under Concave Up, draw a cup holding water: $\cup \implies \text{Min}$.

---

### Slide 14: The Second Derivative Test & Comparison Matrix
- **Time Allocated:** 31:00 – 34:00 (3 minutes)
- **Primary Objective:** Formalize the Second Derivative Test, verify $f(x) = x^3 - 3x$, and reveal the fatal failure mode when $f''(c) = 0$.

#### Verbatim Lecturer Script
> "This gives us the **Second Derivative Test (SDT)**:
> If $f'(c) = 0$:
> - If $f''(c) < 0 \implies$ Local Maximum.
> - If $f''(c) > 0 \implies$ Local Minimum.
> - If $f''(c) = 0 \implies$ **THE TEST FAILS COMPLETELY.**
> 
> Let's test our worked example $f(x) = x^3 - 3x$:
> $$f'(x) = 3x^2 - 3 \implies f''(x) = 6x$$
> At $x = -1$: $f''(-1) = 6(-1) = -6 < 0 \implies$ Confirms **Local Maximum** at $(-1, 2)$!
> At $x = +1$: $f''(1) = 6(+1) = +6 > 0 \implies$ Confirms **Local Minimum** at $(1, -2)$!
> 
> That took five seconds. No sign chart, no test intervals.
> But what is the danger?
> If $f''(c) = 0$, the Second Derivative Test gives zero information.
> Consider:
> - $f(x) = x^4 \implies f''(0) = 0$ (actually a Minimum).
> - $f(x) = -x^4 \implies f''(0) = 0$ (actually a Maximum).
> - $f(x) = x^3 \implies f''(0) = 0$ (Neither!).
> When the Second Derivative Test fails, you must immediately retreat to the First Derivative Test."

#### Apple Pencil Live Annotation Plan
- Write in the scratchpad:
  $$\text{SDT is a FAST SHORTCUT for polynomials; FDT is the UNIVERSAL TRUTH.}$$

---

### Slide 15: Absolute Extrema on Closed Intervals (Endpoint Traps)
- **Time Allocated:** 34:00 – 37:00 (3 minutes)
- **Primary Objective:** Teach the Closed Interval Method under the Extreme Value Theorem (EVT) and illustrate boundary dominance.

#### Verbatim Lecturer Script
> "Now we enter the realm of practical engineering reality. Physical systems never operate on an infinite domain from $-\infty$ to $+\infty$.
> A robotic arm has joint limits. A pressure vessel has relief valve limits.
> 
> **Extreme Value Theorem (EVT):** If a function $f$ is continuous on a closed, bounded interval $[a, b]$, it is guaranteed to attain both an Absolute Maximum and an Absolute Minimum.
> 
> Here is your mandatory 3-Step Closed Interval Protocol:
> 1. Find all critical numbers of $f$ in the open interval $(a, b)$.
> 2. Evaluate $f(c)$ at all valid interior critical numbers.
> 3. Evaluate $f(a)$ and $f(b)$ at the boundary endpoints!
> 
> Look at our example on the screen: $f(x) = x^3 - 3x$ on the interval $[-0.5, 2.5]$.
> - First, critical number $x = -1$ is OUTSIDE the interval! Throw it in the trash.
> - Critical number $x = 1$ is interior. $f(1) = -2$.
> - Left endpoint: $f(-0.5) = (-0.5)^3 - 3(-0.5) = 1.375$.
> - Right endpoint: $f(2.5) = (2.5)^3 - 3(2.5) = 8.125$.
> 
> Compare:
> The Absolute Minimum is $-2$ at $x = 1$.
> The Absolute Maximum is $8.125$ at the boundary $x = 2.5$!
> Notice that at $x = 2.5$, the derivative is $f'(2.5) = 15.75 \ne 0$.
> If you only looked for $f'=0$, you would miss the true peak load by more than 300%!"

#### Apple Pencil Live Annotation Plan
- On the candidate table, circle $8.125$ in bright coral ink and write $\text{ABS MAX}$.
- Circle $-2.000$ in cyan ink and write $\text{ABS MIN}$.
- Draw a big red strike-through line over $x = -1$, writing $\notin [-0.5, 2.5]$.

---

### Slide 16: Engineering Optimization Application: Maximum Power Transfer
- **Time Allocated:** 37:00 – 43:00 (6 minutes)
- **Primary Objective:** Walk through an authentic engineering derivation: The Maximum Power Transfer Theorem in circuit design.

#### Verbatim Lecturer Script
> "Let's apply our complete optimization engine to a cornerstone of electrical and renewable energy engineering: **The Maximum Power Transfer Theorem**.
> 
> You have a power source—say a solar panel array or an audio amplifier—with open-circuit Thevenin voltage $V_s$ and internal source resistance $R_s$. You connect an adjustable load resistance $R_L > 0$.
> 
> The total current flowing in the circuit is:
> $$I = \frac{V_s}{R_s + R_L}$$
> The electrical power delivered to your load resistor is:
> $$P(R_L) = I^2 R_L = \frac{V_s^2 R_L}{(R_s + R_L)^2}$$
> 
> Question: What load resistance $R_L$ extracts the maximum possible power from this source?
> 
> Let's differentiate $P$ with respect to $R_L$ using the quotient rule:
> $$\frac{dP}{dR_L} = V_s^2 \cdot \frac{(R_s + R_L)^2 \cdot (1) - R_L \cdot 2(R_s + R_L)}{(R_s + R_L)^4}$$
> Factor out $(R_s + R_L)$ from the numerator:
> $$\frac{dP}{dR_L} = V_s^2 \cdot \frac{(R_s + R_L) - 2R_L}{(R_s + R_L)^3} = V_s^2 \cdot \frac{R_s - R_L}{(R_s + R_L)^3}$$
> 
> Set the derivative to zero:
> $$V_s^2 \cdot \frac{R_s - R_L}{(R_s + R_L)^3} = 0 \implies R_s - R_L = 0 \implies \mathbf{R_L = R_s}$$
> 
> The load resistance must exactly match the source resistance! This is called **Impedance Matching**.
> At this peak, $P_{\max} = \frac{V_s^2 R_s}{(2R_s)^2} = \frac{V_s^2}{4R_s}$.
> This single calculus derivation governs the design of every antenna, audio amplifier, and solar maximum power point tracker (MPPT) on Earth."

#### Apple Pencil Live Annotation Plan
- In the right scratchpad, write out the First Derivative Test verification:
  $$\text{For } R_L < R_s \implies P' > 0 \nearrow$$
  $$\text{For } R_L > R_s \implies P' < 0 \searrow$$
  $$\implies R_L = R_s \text{ is the GLOBAL MAXIMUM!}$$

---

### Slide 17: Guided Practice: Sheet Metal Packaging Optimization
- **Time Allocated:** 43:00 – 47:00 (4 minutes)
- **Primary Objective:** Engage students in active problem-solving with progressive hints for an industrial packaging problem.

#### Verbatim Lecturer Script
> "Now it's your turn. You are manufacturing an aluminum chassis for a drone controller.
> You start with a $12\,\text{cm} \times 12\,\text{cm}$ square sheet of metal.
> You cut equal squares of side length $x$ from each corner and fold up the sides to create an open-top box.
> 
> What cut depth $x$ maximizes the internal volume of the enclosure?
> 
> Take two minutes on your tablets or notebooks.
> What is the volume formula? What is the physical domain of $x$? Go!"

*(Lecturer pauses for 90 seconds while circulating or observing).*

> "Let's reveal Hint 1:
> The base of the box has dimensions $(12 - 2x) \times (12 - 2x)$, and height $x$.
> So $V(x) = x(12 - 2x)^2 = 4x(6 - x)^2 = 4(x^3 - 12x^2 + 36x)$.
> Physical domain: $x$ cannot be negative, and $2x$ cannot exceed $12$, so $x \in [0, 6]$.
> 
> Hint 2: Differentiating:
> $V'(x) = 12(x^2 - 8x + 12) = 12(x - 2)(x - 6)$.
> 
> Critical values are $x = 2$ and $x = 6$.
> Evaluate:
> $V(0) = 0$, $V(6) = 0$.
> $V(2) = 2(12 - 4)^2 = 2(8)^2 = 128\,\text{cm}^3$.
> The optimal cut depth is exactly $x = 2\,\text{cm}$."

#### Apple Pencil Live Annotation Plan
- Sketch the unfolded $12 \times 12$ sheet with dashed corner cutouts labeled $x$ by $x$.
- Show base dimensions $12 - 2x$ on the folded 3D isometric box sketch.

---

### Slide 18: Independent Engineering Challenge: Beam Deflection
- **Time Allocated:** 47:00 – 50:00 (3 minutes)
- **Primary Objective:** Pose an advanced civil/mechanical beam deflection problem for post-lecture mastery.

#### Verbatim Lecturer Script
> "Here is an independent challenge from structural engineering.
> A simply supported bridge girder of length $L$ under uniform distributed dead weight $w_0$ has an elastic deflection curve:
> $$y(x) = \frac{w_0}{24 E I} (x^4 - 2L x^3 + L^3 x)$$
> where $E$ is Young's Modulus and $I$ is the cross-sectional moment of inertia.
> 
> Differentiating gives:
> $$y'(x) = \frac{w_0}{24 E I} (4x^3 - 6L x^2 + L^3)$$
> By factoring $(2x - L)$, you can prove that the maximum sag occurs precisely at the geometric midpoint $x = L/2$, yielding the famous structural deflection formula:
> $$y_{\max} = \frac{5 w_0 L^4}{384 E I}$$
> Full algebraic verification is in your reference appendix."

---

### Slide 19: The Engineering Optimization Protocol (Flowchart)
- **Time Allocated:** 50:00 – 52:00 (2 minutes)
- **Primary Objective:** Synthesize the entire lecture into a deterministic 4-step procedural algorithm.

#### Verbatim Lecturer Script
> "Take out your phones or take a screenshot on your iPads right now.
> This is your Master Protocol for any engineering optimization problem throughout your degree:
> 
> 1. **Model & Domain:** Express your target variable $y = f(x)$ and determine its allowable physical domain $[a, b]$.
> 2. **Critical Points:** Compute $f'(x)$. Solve $f'(x) = 0$ AND check where $f'(x)$ fails to exist. Discard any candidates outside your domain!
> 3. **Classify Extrema:** Use the First Derivative Test (sign chart) or Second Derivative Test (curvature).
> 4. **Boundary Checks:** Never forget to evaluate endpoints $f(a)$ and $f(b)$. Compare all candidate values to crown your Absolute Maximum and Absolute Minimum."

---

### Slide 20: Conceptual Exit Ticket & Diagnostic Quiz
- **Time Allocated:** 52:00 – 54:30 (2.5 minutes)
- **Primary Objective:** Conduct rapid-fire formative assessment to ensure misconceptions are extinguished before students leave.

#### Verbatim Lecturer Script
> "Before you leave, three diagnostic questions. Show of hands or call it out:
> 
> **Question 1:** If $f'(3) = 0$, does $f(x)$ definitely have a local maximum or minimum at $x = 3$?
> *Class:* 'NO!'
> *Lecturer:* 'Correct! Think of $(x-3)^3$. A flat tangent does not guarantee an extremum.'
> 
> **Question 2:** If $f'(c) = 0$ and $f''(c) = 0$, what does the Second Derivative Test conclude?
> *Class:* 'Inconclusive!'
> *Lecturer:* 'Spot on. You must fall back to the First Derivative Test.'
> 
> **Question 3:** Can an absolute maximum occur where $f'(x) \ne 0$?
> *Class:* 'YES!'
> *Lecturer:* 'Exactly! At boundaries or sharp cusps.'
> You are officially thinking like engineers."

---

### Slides 21 & 22: Reference Solutions & The Next Horizon
- **Time Allocated:** 54:30 – 55:00 (0.5 minutes)
- **Primary Objective:** Adjourn lecture, preview multivariable optimization ($\nabla f = \mathbf{0}$), and direct students to homework.

#### Verbatim Lecturer Script
> "In Slide 21, you have full reference solutions.
> And next week, we break out of the single-variable world. What happens when an aircraft wing depends on both angle of attack $\alpha$ AND velocity $v$?
> We enter **Multivariable Optimization**: where the derivative becomes the Gradient Vector $\nabla f = \mathbf{0}$, concavity becomes the Hessian Matrix, and turning points become Saddle Surfaces.
> 
> Outstanding work today. Class dismissed!"
