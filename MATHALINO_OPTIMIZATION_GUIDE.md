# MATHALINO OPTIMIZATION LECTURE GUIDE
## Differential Calculus: Maxima & Minima Engineering Applications

This guide provides complete mathematical documentation, direct source citations, step-by-step calculus derivations, domain feasibility justifications, and an independently verified answer key for the **Mathalino Maxima and Minima Problems** integrated into the lecture presentation.

---

## 1. Master Curriculum Mapping & Source Checklist

| Lecture Slide | Scene Identifier | Problem Concept | Primary Source URL | Target Variable | Verified Optimal Solution |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Slide 16** | `MathalinoProblem1_NumberOptimization` | Number Exceeding its Square | [01-04 Number Problems](https://mathalino.com/reviewer/differential-calculus/01-04-number-problems-in-maxima-and-minima) | Number $x$ | $x = \frac{1}{2}$, $\text{Max Excess} = \frac{1}{4}$ |
| **Slide 17** | `MathalinoProblem2_RiverbankLot` | Riverbank Fencing Design | [09-11 Rectangular Lot](https://mathalino.com/reviewer/differential-calculus/09-11-rectangular-lot-problems-in-maxima-and-minima) | Dimensions $(x, y)$ | $\text{Width } y = \frac{1}{2} \times \text{Length } x$ |
| **Slide 18** | `MathalinoProblem3_OpenTopBox` | Open-Top $15'' \times 24''$ Box | [15-17 Box Open at Top](https://mathalino.com/reviewer/differential-calculus/15-17-box-open-at-the-top) | Cut depth $x$ | $x = 3''$, $V_{\max} = 486\text{ in}^3$ |
| **Slide 19** | `MathalinoProblem4_TourBusRevenue` | 80-Seat Tour Bus Revenue | [03 Maximum Revenue Tour Bus](https://mathalino.com/reviewer/differential-calculus/03-maximum-revenue-tour-bus-80-seats) | Fare increment $x$ | Fare $= \text{P}425$, $R_{\max} = \text{P}28{,}900$ |
| **Slide 20** | `MathalinoProblem5_TrapezoidalGutter` | Trapezoidal Gutter $14''$ Strip | [41-42 Trapezoidal Gutter](https://mathalino.com/reviewer/differential-calculus/41-42-maxima-and-minima-problem-involving-a-trapezoidal-gutter) | Base width $a$ | $a \approx 3.17''$, $s \approx 5.41''$ |
| **Slide 22** | *(Curriculum Bibliography)* | Full Academic Citations | [Mathalino Maxima & Minima](https://mathalino.com/reviewer/differential-calculus/application-of-maxima-and-minima) | Source References | Complete bibliographic index |

---

## 2. In-Depth Problem Derivations & Verified Answer Key

### A. Number Optimization (Mathalino Problem 1)
- **Direct Source:** [Mathalino 01-04 Number Problems](https://mathalino.com/reviewer/differential-calculus/01-04-number-problems-in-maxima-and-minima)
- **Problem Statement:** *"What number exceeds its square by the maximum amount?"*

#### Step-by-Step Derivation:
1. **Variable Definition:** Let $x \in \mathbb{R}$ be the number. Its square is $x^2$.
2. **Objective Function:** The amount by which the number exceeds its square is:
   $$f(x) = x - x^2$$
3. **Differentiation:**
   $$f'(x) = \frac{d}{dx}(x - x^2) = 1 - 2x$$
4. **Critical Number Condition:**
   $$f'(x) = 0 \implies 1 - 2x = 0 \implies x = \frac{1}{2}$$
5. **Concavity & Extrema Classification (Second Derivative Test):**
   $$f''(x) = \frac{d}{dx}(1 - 2x) = -2 < 0 \quad \forall x \in \mathbb{R}$$
   Because $f''(x) < 0$ globally, the curve is strictly concave down, confirming that $x = \frac{1}{2}$ produces a strict global maximum.
6. **Maximum Excess Value:**
   $$f\left(\frac{1}{2}\right) = \frac{1}{2} - \left(\frac{1}{2}\right)^2 = \frac{1}{2} - \frac{1}{4} = \frac{1}{4} = 0.25$$
- **Final Answer:** The number is **$\frac{1}{2}$** (or $0.5$), and the maximum excess is **$\frac{1}{4}$** (or $0.25$).

---

### B. Rectangular Lot Along a Riverbank (Mathalino Problem 10)
- **Direct Source:** [Mathalino 09-11 Rectangular Lot Problems](https://mathalino.com/reviewer/differential-calculus/09-11-rectangular-lot-problems-in-maxima-and-minima)
- **Problem Statement:** *"A rectangular field of given area is to be fenced off along the bank of a river. If no fence is needed along the river, what is the shape of the rectangle requiring the least amount of fencing?"*

#### Step-by-Step Derivation:
1. **Geometric Variables:**
   - Let $x$ be the length of the lot parallel to the straight riverbank.
   - Let $y$ be the width of the lot perpendicular to the riverbank.
2. **Area Constraint:**
   $$A = x \cdot y \implies x = \frac{A}{y} \quad (\text{where } A > 0 \text{ is constant})$$
3. **Perimeter / Fencing Objective Function:**
   Since no fencing is needed along the riverbank, only three sides are fenced (one side $x$, two sides $y$):
   $$P = x + 2y$$
4. **Single-Variable Reduction:**
   $$P(y) = \frac{A}{y} + 2y = A y^{-1} + 2y \quad \text{for } y \in (0, \infty)$$
5. **Differentiation & Critical Point:**
   $$\frac{dP}{dy} = -\frac{A}{y^2} + 2 = 0 \implies \frac{A}{y^2} = 2 \implies 2y^2 = A$$
6. **Relating Dimensions:**
   Substitute $A = xy$:
   $$2y^2 = xy \implies 2y = x \iff y = \frac{1}{2}x$$
7. **Second Derivative Verification:**
   $$\frac{d^2P}{dy^2} = \frac{2A}{y^3} > 0 \quad \text{for all } y > 0$$
   Strictly concave up, proving a unique global minimum.
- **Final Answer:** The most economical rectangle has a **width equal to half its length** ($y = \frac{1}{2}x$), or equivalently, **length along the river equal to twice the width** ($x = 2y$).

---

### C. Open-Top Box Optimization (Mathalino Problem 16)
- **Direct Source:** [Mathalino 15-17 Box Open at the Top](https://mathalino.com/reviewer/differential-calculus/15-17-box-open-at-the-top)
- **Problem Statement:** *"Find the volume of the largest box that can be made by cutting equal squares out of the corners of a piece of cardboard of dimensions 15 inches by 24 inches, and then turning up the sides."*

#### Step-by-Step Derivation:
1. **Geometric Setup:**
   - Cardboard dimensions: $24'' \text{ (length)} \times 15'' \text{ (width)}$.
   - Cut square corners of side length $x$.
   - Folded dimensions:
     - Base Length: $L(x) = 24 - 2x$
     - Base Width: $W(x) = 15 - 2x$
     - Box Height: $H(x) = x$
2. **Physical Feasibility Domain:**
   All geometric dimensions must be strictly positive:
   $$x > 0, \quad 15 - 2x > 0 \implies x < 7.5'', \quad 24 - 2x > 0 \implies x < 12''$$
   $$\text{Domain: } x \in (0, 7.5)$$
3. **Objective Volume Function:**
   $$V(x) = L(x) \cdot W(x) \cdot H(x) = (24 - 2x)(15 - 2x)x$$
   $$V(x) = (360 - 78x + 4x^2)x = 4x^3 - 78x^2 + 360x$$
4. **Differentiation:**
   $$V'(x) = 12x^2 - 156x + 360$$
5. **Critical Numbers:**
   Set $V'(x) = 0$ and divide by 12:
   $$x^2 - 13x + 30 = 0 \implies (x - 10)(x - 3) = 0$$
   $$\text{Candidates: } x = 3'' \quad \text{or} \quad x = 10''$$
6. **Domain Feasibility Screening:**
   - For $x = 10''$: $W(10) = 15 - 2(10) = -5'' < 0$. **Physically impossible!** $10 \notin (0, 7.5)$. Discarded.
   - For $x = 3''$: $x \in (0, 7.5)$. Valid candidate.
7. **Second Derivative Test:**
   $$V''(x) = 24x - 156 \implies V''(3) = 24(3) - 156 = 72 - 156 = -84 < 0$$
   Confirms an absolute maximum at $x = 3''$.
8. **Optimal Dimensions & Volume:**
   - Cut depth: $x = 3''$
   - Box Length: $24 - 2(3) = 18''$
   - Box Width: $15 - 2(3) = 9''$
   - Maximum Volume: $V_{\max} = 18 \times 9 \times 3 = \mathbf{486\text{ in}^3}$.
- **Source Note:** Mathalino Problem 15 has an erratum printing $\text{in}^2$ for volume; our lecture strictly uses the correct volumetric unit $\text{in}^3$.

---

### D. Maximum Revenue Application: 80-Seat Tour Bus (Mathalino Problem 03)
- **Direct Source:** [Mathalino 03 Maximum Revenue Tour Bus](https://mathalino.com/reviewer/differential-calculus/03-maximum-revenue-tour-bus-80-seats)
- **Problem Statement:** *"A tour bus has 80 seats. When the tour costs P28,000, all seats are sold. For each additional P1,000 charged, 2 fewer seats are sold. What is the maximum revenue the bus company can earn?"*

#### Step-by-Step Derivation:
1. **Base Parameters:**
   - Full capacity: $Q_0 = 80 \text{ seats}$.
   - Base package revenue: $\text{P}28{,}000$.
   - Base fare per passenger: $p_0 = \frac{28{,}000}{80} = \text{P}350/\text{seat}$.
2. **Rate of Change with Increments:**
   - Total package increment: $\text{P}1{,}000 \implies \Delta p = \frac{1{,}000}{80} = \text{P}12.50/\text{seat}$.
   - Passenger loss per increment: $\Delta q = -2 \text{ seats}$.
3. **Formulating Demand and Price:**
   Let $x$ be the number of $P1,000$ package rate increments:
   - Price per seat: $p(x) = 350 + 12.5x$
   - Number of seats sold: $q(x) = 80 - 2x$
4. **Revenue Function:**
   $$R(x) = p(x) \cdot q(x) = (350 + 12.5x)(80 - 2x)$$
   $$R(x) = 28{,}000 - 700x + 1000x - 25x^2 = 28{,}000 + 300x - 25x^2$$
5. **Calculus Optimization:**
   $$\frac{dR}{dx} = 300 - 50x = 0 \implies 50x = 300 \implies x = 6$$
   $$\frac{d^2R}{dx^2} = -50 < 0 \implies \text{Strict Maximum}$$
6. **Optimal Metrics:**
   - Optimal ticket price: $p(6) = 350 + 12.5(6) = 350 + 75 = \mathbf{\text{P}425/\text{seat}}$
   - Passenger count: $q(6) = 80 - 2(6) = \mathbf{68\text{ passengers}}$
   - Maximum Revenue: $R_{\max} = 425 \times 68 = \mathbf{\text{P}28{,}900}$
- **Multiple Choice Alignment:** Matches **Option C ($\text{P}28{,}900$)** on the Mathalino exam reviewer.

---

### E. Trapezoidal Gutter Carrying Capacity (Mathalino Problem 42)
- **Direct Source:** [Mathalino 41-42 Trapezoidal Gutter](https://mathalino.com/reviewer/differential-calculus/41-42-maxima-and-minima-problem-involving-a-trapezoidal-gutter)
- **Problem Statement:** *"From a strip of tin 14 inches wide, a trapezoidal gutter is to be made by bending up the sides at an angle of 45°. Find the width of the base for greatest carrying capacity."*

#### Step-by-Step Derivation:
1. **Cross-Sectional Geometry:**
   - Tin strip total width: $14''$.
   - Base width: $a$.
   - Two bent slant sides of length $s$:
     $$a + 2s = 14 \implies s = \frac{14 - a}{2}$$
   - Bend angle: $\theta = 45^\circ$.
2. **Height and Top Width:**
   - Depth (height) of gutter:
     $$h = s \sin 45^\circ = \frac{14 - a}{2} \cdot \frac{1}{\sqrt{2}} = \frac{14 - a}{2\sqrt{2}}$$
   - Horizontal projection of each slant side:
     $$w = s \cos 45^\circ = h$$
   - Top width: $b = a + 2w = a + 2h$.
3. **Trapezoid Area (Hydraulic Capacity):**
   $$A = \frac{a + b}{2} h = (a + h)h = ah + h^2$$
   Substitute $h = \frac{14 - a}{2\sqrt{2}}$ and $h^2 = \frac{(14 - a)^2}{8}$:
   $$A(a) = \frac{14a - a^2}{2\sqrt{2}} + \frac{196 - 28a + a^2}{8}$$
4. **Differentiation:**
   $$\frac{dA}{da} = \frac{14 - 2a}{2\sqrt{2}} + \frac{-28 + 2a}{8} = \frac{7 - a}{\sqrt{2}} + \frac{a - 14}{4} = 0$$
5. **Exact Analytical Solution:**
   $$\frac{7 - a}{\sqrt{2}} = \frac{14 - a}{4} \implies 4(7 - a) = \sqrt{2}(14 - a)$$
   $$28 - 4a = 14\sqrt{2} - \sqrt{2}a \implies (4 - \sqrt{2})a = 28 - 14\sqrt{2} = 14(2 - \sqrt{2})$$
   Divide both sides by $\sqrt{2}$:
   $$(2\sqrt{2} - 1)a = 14(\sqrt{2} - 1)$$
   $$a = \frac{14(\sqrt{2} - 1)}{2\sqrt{2} - 1}$$
6. **Numerical Calculation:**
   $$a = \frac{14(0.41421356)}{1.82842712} \approx \mathbf{3.17\text{ inches}}$$
   - Slant sides:
     $$s = \frac{14 - 3.17157}{2} \approx \mathbf{5.41\text{ inches}}$$
7. **Second Derivative Concavity Check:**
   $$\frac{d^2A}{da^2} = -\frac{1}{\sqrt{2}} + \frac{1}{4} \approx -0.7071 + 0.25 = -0.4571 < 0 \implies \text{Strict Maximum}$$
- **Final Answer:** The optimal base width for maximum carrying capacity is **$a \approx 3.17\text{ inches}$**, with slant side lengths of **$s \approx 5.41\text{ inches}$**.

---

## 3. Pedagogical Integration & Apple Pencil Annotation Zones

For each problem in the lecture presentation:
1. **Manim Animated Sequence:** Continuous visual transformation showing the geometric structure adapting, moving tangent vectors, critical numbers, and algebraic morphs.
2. **Matching High-Resolution Frame:** Frozen at the final optimal state with exact numerical labels and geometric diagrams.
3. **Apple Pencil Scratchpad:** Wide dedicated canvas for live derivation in Keynote or the web presentation runner, structured into:
   - *Model Setup & Constraint Isolation*
   - *Objective Function Construction*
   - *First Derivative Critical Number Search*
   - *Second Derivative / Feasibility Verification*
