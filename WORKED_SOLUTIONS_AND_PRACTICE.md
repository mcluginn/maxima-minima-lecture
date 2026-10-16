# Mathematical Foundations & Engineering Practice Solutions
## Maxima & Minima: Comprehensive Derivations, Proofs & Solutions

**Course Module:** Differential Calculus for Engineers  
**Target Reference:** Complete Mathematical Companion & Verification Suite  

---

## 1. Rigorous Mathematical Foundations & Proofs

### 1.1 Proof of Fermat's Theorem on Stationary Points (1636)

**Theorem:**  
Let $f: (a, b) \to \mathbb{R}$ be a function defined on an open interval $(a, b)$. If $f$ attains a local extremum at a point $c \in (a, b)$, and if the derivative $f'(c)$ exists, then:
$$f'(c) = 0$$

**Proof (for a Local Maximum):**  
1. By definition of a local maximum, there exists an open neighborhood $(c - \delta, c + \delta) \subseteq (a, b)$ with $\delta > 0$ such that:
   $$f(x) \le f(c) \quad \forall x \in (c - \delta, c + \delta)$$
   Equivalently, for any perturbation $h$ satisfying $0 < |h| < \delta$:
   $$f(c + h) - f(c) \le 0$$

2. Since $f'(c)$ exists by hypothesis, both one-sided limits of the difference quotient must exist and be equal:
   $$f'(c) = \lim_{h \to 0^+} \frac{f(c + h) - f(c)}{h} = \lim_{h \to 0^-} \frac{f(c + h) - f(c)}{h}$$

3. **Examine the right-hand limit ($h > 0$):**  
   Since $h > 0$ and the numerator $f(c + h) - f(c) \le 0$, the quotient is non-positive:
   $$\frac{f(c + h) - f(c)}{h} \le 0$$
   Taking the limit as $h \to 0^+$:
   $$\lim_{h \to 0^+} \frac{f(c + h) - f(c)}{h} \le 0 \implies f'(c) \le 0$$

4. **Examine the left-hand limit ($h < 0$):**  
   Since $h < 0$ and the numerator $f(c + h) - f(c) \le 0$, the ratio of two non-positive numbers is non-negative:
   $$\frac{f(c + h) - f(c)}{h} \ge 0$$
   Taking the limit as $h \to 0^-$:
   $$\lim_{h \to 0^-} \frac{f(c + h) - f(c)}{h} \ge 0 \implies f'(c) \ge 0$$

5. **Squeeze Conclusion:**  
   The only real number satisfying both $f'(c) \le 0$ and $f'(c) \ge 0$ is:
   $$f'(c) = 0 \quad \blacksquare$$
*(An identical argument with inverted signs applies for a Local Minimum).*

---

### 1.2 The Extreme Value Theorem (Weierstrass Theorem) & Boundary Mechanics

**Theorem:**  
If a real-valued function $f$ is continuous on a closed, bounded interval $[a, b] \subset \mathbb{R}$, then $f$ is bounded and attains both an absolute maximum and an absolute minimum at least once on $[a, b]$. That is, there exist points $c_{\text{min}}, c_{\text{max}} \in [a, b]$ such that:
$$f(c_{\text{min}}) \le f(x) \le f(c_{\text{max}}) \quad \forall x \in [a, b]$$

**Significance for Engineering Optimization:**  
Because the interval $[a, b]$ is compact (closed and bounded in $\mathbb{R}$), an absolute extremum is guaranteed to exist. However, $c_{\text{max}}$ and $c_{\text{min}}$ can occur at:
1. An interior point where $f'(c) = 0$ (Stationary critical point),
2. An interior point where $f'(c)$ does not exist (Singular critical point, e.g. sharp corner or cusp),
3. **The boundary endpoints $x = a$ or $x = b$.**

---

### 1.3 Proof of the First Derivative Test (via Mean Value Theorem)

**Theorem:**  
Let $f$ be continuous on an open interval $I$ containing critical number $c$, and differentiable on $I \setminus \{c\}$.
1. If $f'(x) > 0$ for all $x \in (c - \delta, c)$ and $f'(x) < 0$ for all $x \in (c, c + \delta)$, then $f(c)$ is a **Local Maximum**.
2. If $f'(x) < 0$ for all $x \in (c - \delta, c)$ and $f'(x) > 0$ for all $x \in (c, c + \delta)$, then $f(c)$ is a **Local Minimum**.

**Proof of Case 1 (Local Maximum):**  
- Let $x \in (c - \delta, c)$. By the Mean Value Theorem on $[x, c]$, there exists $\xi \in (x, c)$ such that:
  $$\frac{f(c) - f(x)}{c - x} = f'(\xi)$$
  Since $\xi \in (c - \delta, c)$, we have $f'(\xi) > 0$. Because $c - x > 0$, it follows that:
  $$f(c) - f(x) = (c - x)f'(\xi) > 0 \implies f(c) > f(x)$$
- Let $x \in (c, c + \delta)$. By the Mean Value Theorem on $[c, x]$, there exists $\eta \in (c, x)$ such that:
  $$\frac{f(x) - f(c)}{x - c} = f'(\eta)$$
  Since $\eta \in (c, c + \delta)$, we have $f'(\eta) < 0$. Because $x - c > 0$, it follows that:
  $$f(x) - f(c) = (x - c)f'(\eta) < 0 \implies f(c) > f(x)$$
- Since $f(c) > f(x)$ for all $x \in (c - \delta, c + \delta) \setminus \{c\}$, $f(c)$ is a strict Local Maximum. $\blacksquare$

---

## 2. Canonical Worked Example: $f(x) = x^3 - 3x$

### 2.1 Complete Step-by-Step Derivation

**Given Function:**  
$$f(x) = x^3 - 3x, \quad x \in \mathbb{R}$$

#### Step 1: Compute First Derivative and Factor
Using the power and linearity rules:
$$f'(x) = \frac{d}{dx}[x^3 - 3x] = 3x^2 - 3$$
Factoring out the greatest common factor:
$$f'(x) = 3(x^2 - 1) = 3(x - 1)(x + 1)$$

#### Step 2: Identify All Critical Numbers
1. Stationary condition:
   $$f'(x) = 0 \implies 3(x - 1)(x + 1) = 0 \implies x = -1, \quad x = +1$$
2. Non-existence condition:
   $f'(x)$ is a polynomial and is therefore defined for all $x \in \mathbb{R}$. No singular points exist.
   **Critical Numbers:** $x_1 = -1, \; x_2 = 1$.

#### Step 3: First Derivative Sign Chart Analysis
The critical numbers partition $\mathbb{R}$ into three open test intervals: $(-\infty, -1)$, $(-1, 1)$, and $(1, \infty)$.

| Interval | Test Point ($x_{\text{test}}$) | Factors: $3 \cdot (x-1) \cdot (x+1)$ | Value of $f'(x_{\text{test}})$ | Sign of $f'(x)$ | Behavior of $f(x)$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $(-\infty, -1)$ | $x = -2$ | $3 \cdot (-3) \cdot (-1) = +9$ | $+9 > 0$ | **Positive (+)** | **Strictly Increasing ($\nearrow$)** |
| $(-1, 1)$ | $x = 0$ | $3 \cdot (-1) \cdot (+1) = -3$ | $-3 < 0$ | **Negative (-)** | **Strictly Decreasing ($\searrow$)** |
| $(1, \infty)$ | $x = +2$ | $3 \cdot (+1) \cdot (+3) = +9$ | $+9 > 0$ | **Positive (+)** | **Strictly Increasing ($\nearrow$)** |

#### Step 4: First Derivative Test Classification & Exact Coordinates
- **At $x = -1$:**  
  The derivative $f'(x)$ transitions from Positive $(+)$ on $(-\infty, -1)$ to Negative $(-)$ on $(-1, 1)$.  
  $\implies$ **Strict Local Maximum at $x = -1$**.  
  Coordinate height:
  $$f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2 \implies \mathbf{(-1, 2)}$$

- **At $x = +1$:**  
  The derivative $f'(x)$ transitions from Negative $(-)$ on $(-1, 1)$ to Positive $(+)$ on $(1, \infty)$.  
  $\implies$ **Strict Local Minimum at $x = +1$**.  
  Coordinate height:
  $$f(1) = (1)^3 - 3(1) = 1 - 3 = -2 \implies \mathbf{(1, -2)}$$

#### Step 5: Second Derivative Test Verification & Inflection Point
Differentiating $f'(x) = 3x^2 - 3$:
$$f''(x) = \frac{d}{dx}[3x^2 - 3] = 6x$$
Evaluating concavity at the critical numbers:
- At $x = -1$:
  $$f''(-1) = 6(-1) = -6 < 0 \implies \text{Concave Down } (\cap) \implies \mathbf{Local\;Maximum\;Confirmed!}$$
- At $x = +1$:
  $$f''(1) = 6(1) = +6 > 0 \implies \text{Concave Up } (\cup) \implies \mathbf{Local\;Minimum\;Confirmed!}$$
- **Inflection Point:**  
  Setting $f''(x) = 0 \implies 6x = 0 \implies x = 0$.  
  For $x < 0$, $f''(x) < 0$ (Concave Down); for $x > 0$, $f''(x) > 0$ (Concave Up).  
  Concavity changes sign across $x = 0$. The point $(0, f(0)) = \mathbf{(0, 0)}$ is a point of inflection.

---

### 2.2 Closed Interval Method on $[-0.5, 2.5]$

Evaluate $f(x) = x^3 - 3x$ on the restricted domain $D = [-0.5, 2.5]$.

1. **Filter Critical Numbers:**  
   Our critical numbers on $\mathbb{R}$ were $x = -1$ and $x = 1$.  
   - $x = -1 \notin [-0.5, 2.5]$ $\implies$ **DISCARDED.**
   - $x = 1 \in (-0.5, 2.5)$ $\implies$ **VALID INTERIOR CANDIDATE.**

2. **Evaluate Function at Valid Candidates & Endpoints:**
   - **Interior Critical Point:**
     $$f(1) = (1)^3 - 3(1) = -2.000$$
   - **Left Endpoint ($x = -0.5$):**
     $$f(-0.5) = (-0.5)^3 - 3(-0.5) = -0.125 + 1.500 = 1.375 = \frac{11}{8}$$
   - **Right Endpoint ($x = 2.5$):**
     $$f(2.5) = (2.5)^3 - 3(2.5) = 15.625 - 7.500 = 8.125 = \frac{65}{8}$$

3. **Comparison & Verdict:**
   - Largest value: $8.125$ at boundary endpoint $x = 2.5$.
   - Smallest value: $-2.000$ at interior critical point $x = 1$.
   $$\mathbf{Absolute\;Maximum = 8.125 \quad (at\;x = 2.5)}$$
   $$\mathbf{Absolute\;Minimum = -2.000 \quad (at\;x = 1.0)}$$

---

## 3. Multi-Disciplinary Engineering Practice Set & Full Solutions

---

### Practice Problem 1: Electrical / Electronics Engineering
#### Maximum Power Transfer Theorem & Efficiency Analysis

**Physical Setup:**  
A DC power source with fixed Thevenin voltage $V_s = 24\,\text{V}$ and internal source resistance $R_s = 6\,\Omega$ supplies power to an adjustable variable load resistor $R_L > 0$. The power dissipated in the load is modeled by:
$$P(R_L) = \frac{V_s^2 R_L}{(R_s + R_L)^2}$$

**Tasks:**
1. Determine the exact value of $R_L$ that maximizes the power delivered to the load.
2. Calculate the maximum power $P_{\max}$.
3. Calculate the electrical efficiency $\eta = \frac{P_{\text{load}}}{P_{\text{total}}}$ at the point of maximum power transfer.

**Complete Mathematical Solution:**

1. **Differentiate $P(R_L)$ with respect to $R_L$:**  
   Treat $V_s$ and $R_s$ as positive constants. Apply the Quotient Rule $\frac{d}{dx}\left[\frac{u}{v}\right] = \frac{u'v - uv'}{v^2}$:
   - Let $u(R_L) = V_s^2 R_L \implies u'(R_L) = V_s^2$
   - Let $v(R_L) = (R_s + R_L)^2 \implies v'(R_L) = 2(R_s + R_L)(1)$
   
   $$\frac{dP}{dR_L} = \frac{V_s^2 (R_s + R_L)^2 - V_s^2 R_L \cdot 2(R_s + R_L)}{(R_s + R_L)^4}$$
   
   Factor out the common term $V_s^2(R_s + R_L)$ from the numerator:
   $$\frac{dP}{dR_L} = \frac{V_s^2 (R_s + R_L) \left[(R_s + R_L) - 2R_L\right]}{(R_s + R_L)^4} = \frac{V_s^2 (R_s - R_L)}{(R_s + R_L)^3}$$

2. **Solve for Critical Numbers:**  
   $$\frac{dP}{dR_L} = 0 \implies V_s^2 (R_s - R_L) = 0 \implies \mathbf{R_L = R_s}$$
   For $R_s = 6\,\Omega$, our critical load resistance is $R_L = 6\,\Omega$.

3. **Verify Extremum via First Derivative Test:**  
   - For $0 < R_L < R_s$: $(R_s - R_L) > 0 \implies \frac{dP}{dR_L} > 0$ (Power is increasing $\nearrow$).
   - For $R_L > R_s$: $(R_s - R_L) < 0 \implies \frac{dP}{dR_L} < 0$ (Power is decreasing $\searrow$).
   - Since $P'$ transitions from $(+)$ to $(-)$ across $R_L = R_s$, $R_L = R_s$ is the **unambiguous global maximum**.

4. **Calculate Maximum Power $P_{\max}$:**  
   $$P_{\max} = P(R_s) = \frac{V_s^2 R_s}{(R_s + R_s)^2} = \frac{V_s^2 R_s}{(2R_s)^2} = \frac{V_s^2 R_s}{4R_s^2} = \frac{V_s^2}{4R_s}$$
   Substituting numerical values $V_s = 24\,\text{V}$, $R_s = 6\,\Omega$:
   $$P_{\max} = \frac{(24)^2}{4(6)} = \frac{576}{24} = \mathbf{24\,\text{Watts}}$$

5. **Calculate Efficiency $\eta$:**  
   $$P_{\text{total}} = I^2(R_s + R_L)$$
   $$P_{\text{load}} = I^2 R_L$$
   $$\eta = \frac{P_{\text{load}}}{P_{\text{total}}} = \frac{I^2 R_L}{I^2(R_s + R_L)} = \frac{R_L}{R_s + R_L}$$
   At maximum power transfer, $R_L = R_s$:
   $$\eta = \frac{R_s}{R_s + R_s} = \frac{R_s}{2R_s} = \frac{1}{2} = \mathbf{50\%}$$
   *(Key Engineering Insight: At maximum power transfer, exactly half the source power is lost as internal heat within the source resistance $R_s$! This is why power distribution grids operate at high impedance $\eta \approx 95\%$, whereas RF transmitters operate at matched impedance $\eta = 50\%$).*

---

### Practice Problem 2: Civil / Structural Engineering
#### Maximum Deflection of a Simply Supported Bridge Girder

**Physical Setup:**  
A simply supported structural beam of span length $L = 6.0\,\text{m}$ carries a uniform distributed load $w_0 = 12\,\text{kN/m}$. The beam has flexural rigidity $EI = 1.8 \times 10^4\,\text{kN}\cdot\text{m}^2$. The elastic downward deflection equation is:
$$y(x) = \frac{w_0}{24EI} \left(x^4 - 2Lx^3 + L^3x\right), \quad x \in [0, L]$$

**Tasks:**
1. Find all critical numbers of deflection in $(0, L)$.
2. Prove that maximum deflection occurs at the exact geometric midpoint $x = L/2$.
3. Compute the peak deflection $y_{\max}$ in millimeters.

**Complete Mathematical Solution:**

1. **Differentiate Deflection $y(x)$:**  
   Let $k = \frac{w_0}{24EI} > 0$.
   $$y'(x) = k \frac{d}{dx}\left[x^4 - 2Lx^3 + L^3x\right] = k \left(4x^3 - 6Lx^2 + L^3\right)$$

2. **Find Roots of the Cubic Derivative:**  
   We solve $4x^3 - 6Lx^2 + L^3 = 0$.
   Notice by physical symmetry that $x = L/2$ is an expected root:
   $$4\left(\frac{L}{2}\right)^3 - 6L\left(\frac{L}{2}\right)^2 + L^3 = 4\left(\frac{L^3}{8}\right) - 6L\left(\frac{L^2}{4}\right) + L^3 = \frac{1}{2}L^3 - \frac{3}{2}L^3 + L^3 = 0$$
   Therefore, $(2x - L)$ is an exact factor of $4x^3 - 6Lx^2 + L^3$.

3. **Polynomial Division & Complete Factorization:**  
   Dividing $(4x^3 - 6Lx^2 + L^3)$ by $(2x - L)$:
   $$\frac{4x^3 - 6Lx^2 + 0x + L^3}{2x - L} = 2x^2 - 2Lx - L^2$$
   Check: $(2x - L)(2x^2 - 2Lx - L^2) = 4x^3 - 4Lx^2 - 2L^2x - 2Lx^2 + 2L^2x + L^3 = 4x^3 - 6Lx^2 + L^3$. Perfect!

4. **Solve Remaining Roots via Quadratic Formula:**  
   $$2x^2 - 2Lx - L^2 = 0 \implies x = \frac{-(-2L) \pm \sqrt{(-2L)^2 - 4(2)(-L^2)}}{2(2)} = \frac{2L \pm \sqrt{4L^2 + 8L^2}}{4} = \frac{2L \pm \sqrt{12L^2}}{4} = \frac{1 \pm \sqrt{3}}{2}L$$
   Evaluating numerical values:
   $$x_a = \frac{1 + 1.732}{2}L \approx 1.366 L > L \quad (\text{Outside Physical Beam!})$$
   $$x_b = \frac{1 - 1.732}{2}L \approx -0.366 L < 0 \quad (\text{Outside Physical Beam!})$$
   Therefore, the **sole critical number in the physical span $[0, L]$ is $x = L/2$**.

5. **Evaluate Maximum Deflection $y_{\max}$:**  
   Evaluate $y(x)$ at $x = L/2$:
   $$y(L/2) = \frac{w_0}{24EI} \left[\left(\frac{L}{2}\right)^4 - 2L\left(\frac{L}{2}\right)^3 + L^3\left(\frac{L}{2}\right)\right]$$
   $$= \frac{w_0}{24EI} \left[\frac{L^4}{16} - \frac{2L^4}{8} + \frac{L^4}{2}\right] = \frac{w_0}{24EI} L^4 \left[\frac{1}{16} - \frac{4}{16} + \frac{8}{16}\right] = \frac{w_0}{24EI} L^4 \left(\frac{5}{16}\right)$$
   $$\mathbf{y_{\max} = \frac{5 w_0 L^4}{384 E I}}$$

6. **Boundary Check & Numerical Evaluation:**  
   - At boundary supports: $y(0) = 0$ and $y(L) = \frac{w_0}{24EI}(L^4 - 2L^4 + L^4) = 0$.
   - Since $y(L/2) > 0$ and $y(0) = y(L) = 0$, $x = L/2$ is the absolute maximum deflection.
   - Substituting given constants ($w_0 = 12\,\text{kN/m}$, $L = 6.0\,\text{m}$, $EI = 1.8 \times 10^4\,\text{kN}\cdot\text{m}^2$):
     $$y_{\max} = \frac{5 \cdot 12 \cdot (6.0)^4}{384 \cdot (18000)} = \frac{60 \cdot 1296}{6912000} = \frac{77760}{6912000} = 0.01125\,\text{m} = \mathbf{11.25\,\text{mm}}$$

---

### Practice Problem 3: Chemical & Biomedical Engineering
#### Optimal Reaction Temperature Under Catalyst Thermal Deactivation

**Physical Setup:**  
In a continuous bioreactor synthesizing an active pharmaceutical ingredient, the reaction rate $R(T)$ depends on temperature $T$ (in $^\circ\text{C}$). Increased temperature accelerates reaction kinetics according to the Arrhenius law, but simultaneously triggers exponential denaturation of the biocatalyst enzyme. The overall rate is modeled by:
$$R(T) = T \cdot e^{-T/50}, \quad T \in [0, 200]\,^\circ\text{C}$$

**Tasks:**
1. Determine the optimal operating temperature $T_{\text{opt}}$ that maximizes the synthesis rate.
2. Verify using both the First and Second Derivative Tests.
3. Compare the peak rate against the boundary limits $T = 0\,^\circ\text{C}$ and $T = 200\,^\circ\text{C}$.

**Complete Mathematical Solution:**

1. **Differentiate $R(T)$ Using Product Rule:**  
   $$R'(T) = \frac{d}{dT}\left[T \cdot e^{-T/50}\right] = (1) \cdot e^{-T/50} + T \cdot \left(-\frac{1}{50}e^{-T/50}\right)$$
   Factoring out $e^{-T/50}$:
   $$R'(T) = e^{-T/50} \left(1 - \frac{T}{50}\right)$$

2. **Solve for Critical Numbers:**  
   Since $e^{-T/50} > 0$ for all real $T$, $R'(T) = 0$ if and only if:
   $$1 - \frac{T}{50} = 0 \implies \mathbf{T = 50\,^\circ\text{C}}$$
   $T = 50\,^\circ\text{C}$ lies well within the operating interval $[0, 200]\,^\circ\text{C}$.

3. **Classification via First Derivative Test:**  
   - For $0 \le T < 50$: $1 - T/50 > 0 \implies R'(T) > 0$ (Reaction accelerating $\nearrow$).
   - For $50 < T \le 200$: $1 - T/50 < 0 \implies R'(T) < 0$ (Thermal denaturation dominating $\searrow$).
   - Transition from $(+)$ to $(-)$ confirms $T = 50\,^\circ\text{C}$ is a **Local Maximum**.

4. **Classification via Second Derivative Test:**  
   $$R''(T) = \frac{d}{dT}\left[e^{-T/50} \left(1 - \frac{T}{50}\right)\right]$$
   $$= -\frac{1}{50}e^{-T/50} \left(1 - \frac{T}{50}\right) + e^{-T/50} \left(-\frac{1}{50}\right) = \frac{e^{-T/50}}{50} \left(\frac{T}{50} - 2\right)$$
   Evaluating at $T = 50$:
   $$R''(50) = \frac{e^{-1}}{50} (1 - 2) = -\frac{1}{50e} < 0 \implies \text{Concave Down } (\cap) \implies \mathbf{Maximum\;Confirmed!}$$

5. **Evaluate Closed Interval Candidates:**  
   - Critical point: $R(50) = 50 e^{-1} = \frac{50}{e} \approx \mathbf{18.394\,\text{units}}$
   - Left boundary ($T = 0$): $R(0) = 0 \cdot e^0 = \mathbf{0.000\,\text{units}}$
   - Right boundary ($T = 200$): $R(200) = 200 e^{-4} = \frac{200}{54.598} \approx \mathbf{3.663\,\text{units}}$
   - **Conclusion:** Absolute Maximum synthesis rate is $\frac{50}{e} \approx 18.39\,\text{units}$ at **$T = 50\,^\circ\text{C}$**.

---

### Practice Problem 4: Mechanical & Fluid Engineering
#### Optimal Rectangular Irrigation / Cooling Channel Cross-Section

**Physical Setup:**  
A coolant channel of rectangular cross-section with width $b$ and fluid depth $y$ must carry an area $A = 8.0\,\text{m}^2$. To minimize viscous boundary-layer wall friction and pumping power loss, the wetted perimeter $P$ must be minimized. The wetted perimeter is:
$$P = b + 2y$$

**Tasks:**
1. Formulate the single-variable objective function $P(y)$ for fluid depth $y > 0$.
2. Find the optimal depth $y$ and channel width $b$ that minimizes friction perimeter.
3. Prove that the optimal hydraulic geometry has a width equal to twice its depth ($b = 2y$).

**Complete Mathematical Solution:**

1. **Formulate Single-Variable Function:**  
   Area constraint: $A = b \cdot y = 8.0 \implies b = \frac{A}{y} = \frac{8}{y}$.  
   Substitute into perimeter:
   $$P(y) = \frac{8}{y} + 2y = 8y^{-1} + 2y, \quad y \in (0, \infty)$$

2. **Differentiate and Find Critical Numbers:**  
   $$P'(y) = -8y^{-2} + 2 = -\frac{8}{y^2} + 2$$
   Setting $P'(y) = 0$:
   $$-\frac{8}{y^2} + 2 = 0 \implies \frac{8}{y^2} = 2 \implies y^2 = 4 \implies \mathbf{y = 2.0\,\text{m}} \quad (y > 0)$$

3. **Classification via Second Derivative Test:**  
   $$P''(y) = \frac{d}{dy}\left[-8y^{-2} + 2\right] = 16y^{-3} = \frac{16}{y^3}$$
   At $y = 2.0\,\text{m}$:
   $$P''(2) = \frac{16}{2^3} = \frac{16}{8} = +2 > 0 \implies \text{Concave Up } (\cup) \implies \mathbf{Absolute\;Minimum!}$$

4. **Calculate Dimensions & Verify Hydraulic Ratio:**  
   - Optimal Depth: $y = 2.0\,\text{m}$
   - Optimal Width: $b = \frac{A}{y} = \frac{8.0}{2.0} = \mathbf{4.0\,\text{m}}$
   - Minimum Wetted Perimeter: $P_{\min} = 4.0 + 2(2.0) = \mathbf{8.0\,\text{m}}$
   - Hydraulic Ratio:
     $$\frac{b}{y} = \frac{4.0}{2.0} = 2 \implies \mathbf{b = 2y} \quad \blacksquare$$
   *(Universal Fluid Mechanics Rule: The most efficient rectangular open channel always has a width exactly equal to twice its water depth).*

---

## 4. Master Verification Summary Table

| Problem | Target Function | Domain | Critical Point | Classification | Peak Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Worked Example** | $f(x) = x^3 - 3x$ | $[-0.5, 2.5]$ | $x = 1, \; 2.5$ (End) | Min at $1$, Max at $2.5$ | Min: $-2$, Max: $8.125$ |
| **Electrical (Power)** | $P(R_L) = \frac{V_s^2 R_L}{(R_s + R_L)^2}$ | $(0, \infty)$ | $R_L = R_s$ | Absolute Maximum | $P_{\max} = \frac{V_s^2}{4R_s}$ |
| **Civil (Beam)** | $y(x) = k(x^4 - 2Lx^3 + L^3x)$ | $[0, L]$ | $x = L/2$ | Absolute Maximum | $y_{\max} = \frac{5 w_0 L^4}{384 E I}$ |
| **Chemical (Reactor)** | $R(T) = T e^{-T/50}$ | $[0, 200]\,^\circ\text{C}$ | $T = 50\,^\circ\text{C}$ | Absolute Maximum | $R_{\max} = \frac{50}{e} \approx 18.39$ |
| **Fluid (Channel)** | $P(y) = A/y + 2y$ | $(0, \infty)$ | $y = \sqrt{A/2}$ | Absolute Minimum | $b = 2y, \; P_{\min} = 2\sqrt{2A}$ |
