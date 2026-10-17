# Elementary Applications of First-Order Differential Equations
## Master Worked Solutions & Lecturer Answer Key

**Curriculum Subject:** Differential Equations for Engineering  
**Primary Reference:** MATHalino Engineering Math Review ([mathalino.com/reviewer/applications](https://mathalino.com/reviewer/applications))  
**Pedagogical Style:** 3Blue1Brown Kinematic Modeling & Continuous Vector Animations  
**Author / Lecturer:** Engineering Mathematics Faculty  

---

### Executive Summary & Mathematical Architecture

This lecture focuses on the physical intuition, mathematical derivation, and engineering interpretation of first-order ordinary differential equations (ODEs). Every problem is grounded in authentic, verified data from MATHalino, solved from first principles via separation of variables, and validated through physical asymptotic behavior.

---

## 1. Newton's Law of Cooling: Governing Theory

### Physical Law
Newton's empirical law of cooling states that the time rate of change of the temperature of an object is directly proportional to the difference between its instantaneous temperature $T(t)$ and the ambient temperature of its surrounding medium $T_s$:

$$\frac{dT}{dt} \propto (T - T_s)$$

Since an object hotter than its environment cools ($\frac{dT}{dt} < 0$ when $T > T_s$) and an object colder warms ($\frac{dT}{dt} > 0$ when $T < T_s$), we introduce a strictly positive constant of proportionality $k > 0$ and a negative sign:

$$\frac{dT}{dt} = -k(T - T_s)$$

### Separation of Variables & General Solution
1. **Separate Variables:**
   $$\frac{dT}{T - T_s} = -k\,dt$$

2. **Integrate Both Sides:**
   $$\int \frac{dT}{T - T_s} = -k \int dt$$
   $$\ln|T - T_s| = -kt + C_1$$

3. **Exponentiate:**
   $$|T - T_s| = e^{-kt + C_1} = e^{C_1} e^{-kt}$$
   $$T - T_s = C e^{-kt} \quad \text{where } C = \pm e^{C_1}$$

4. **Apply Initial Condition $T(0) = T_0$:**
   $$T_0 - T_s = C e^{0} = C \implies C = T_0 - T_s$$

5. **Explicit Temperature Function:**
   $$T(t) = T_s + (T_0 - T_s)e^{-kt}$$

### Asymptotic Verification
As $t \to \infty$, $e^{-kt} \to 0$, hence $\lim_{t \to \infty} T(t) = T_s$. The ambient temperature $T_s$ serves as a horizontal asymptote. The physical system can never cross $T_s$ under pure conduction/convection cooling.

---

## 2. Mathalino Cooling Problem 01: Thermometer After 6 Minutes

**Direct Source Citation:**  
[MATHalino Reviewer: Thermometer reading after 6 minutes of being outside](https://mathalino.com/reviewer/elementary-differential-equations/theremometer-reading-after-6-minutes-being-outside)

### Problem Statement
A thermometer which has been at the reading of $70^\circ\text{F}$ inside a house is placed outside where the air temperature is $10^\circ\text{F}$. Three minutes later it is found that the thermometer reading is $25^\circ\text{F}$. Find the thermometer reading after $6$ minutes.

### Given Data
- Initial thermometer temperature: $T_0 = 70^\circ\text{F}$ at $t = 0$
- Ambient air temperature: $T_s = 10^\circ\text{F}$
- Intermediate reading: $T(3) = 25^\circ\text{F}$ at $t = 3\text{ minutes}$
- Target: $T(6)$ at $t = 6\text{ minutes}$

### Step-by-Step Derivation
1. **Formulate the Particular Temperature Model:**
   $$T(t) = T_s + (T_0 - T_s)e^{-kt} = 10 + (70 - 10)e^{-kt} = 10 + 60e^{-kt}$$

2. **Determine the Cooling Parameter from the 3-Minute Observation:**
   $$25 = 10 + 60e^{-3k}$$
   $$15 = 60e^{-3k} \implies \frac{15}{60} = \frac{1}{4} = e^{-3k}$$
   Taking the cube root of both sides:
   $$e^{-k} = \left(\frac{1}{4}\right)^{1/3}$$

3. **Substitute $e^{-k}$ Back into the Model:**
   $$T(t) = 10 + 60\left[\left(\frac{1}{4}\right)^{1/3}\right]^t = 10 + 60\left(\frac{1}{4}\right)^{t/3}$$

4. **Calculate Temperature at $t = 6\text{ minutes}$:**
   $$T(6) = 10 + 60\left(\frac{1}{4}\right)^{6/3} = 10 + 60\left(\frac{1}{4}\right)^2 = 10 + 60\left(\frac{1}{16}\right)$$
   $$T(6) = 10 + \frac{60}{16} = 10 + 3.75 = \mathbf{13.75^\circ\text{F}}$$

### Independent Verification & Interpretation
- After the first 3 minutes, the temperature excess $(T - T_s)$ dropped from $60^\circ\text{F}$ to $15^\circ\text{F}$ (a factor of $1/4$).
- Over the next 3 minutes (from $t = 3$ to $t = 6$), the excess must again shrink by the same constant ratio:
  $$\Delta T(6) = \frac{1}{4} \times 15^\circ\text{F} = 3.75^\circ\text{F}$$
  $$T(6) = T_s + 3.75^\circ\text{F} = 10 + 3.75 = 13.75^\circ\text{F}$$
- **Final Result:** $\mathbf{13.75^\circ\text{F}}$ (Matches MATHalino exactly).

---

## 3. Mathalino Cooling Problem 02: Time to Within Half Degree

**Direct Source Citation:**  
[MATHalino Reviewer: Time for the thermometer reading to drop to within half degree of the air temperature](https://mathalino.com/reviewer/elementary-differential-equations/02-time-thermometer-reading-drop-within-half-degree-air)

### Problem Statement
A thermometer reading $75^\circ\text{F}$ is taken out where the temperature is $20^\circ\text{F}$. The thermometer reading is $30^\circ\text{F}$ four minutes later. Find the time (in minutes) taken for the reading to drop from $75^\circ\text{F}$ to within half degree of the air temperature.

### Given Data
- Initial reading: $T_0 = 75^\circ\text{F}$ at $t = 0$
- Ambient air temperature: $T_s = 20^\circ\text{F}$
- 4-minute reading: $T(4) = 30^\circ\text{F}$ at $t = 4\text{ minutes}$
- Target condition: Temperature is within $0.5^\circ\text{F}$ of air temperature:
  $$T(t) - T_s = 0.5^\circ\text{F} \implies T(t) = 20 + 0.5 = 20.5^\circ\text{F}$$

### Step-by-Step Derivation
1. **Formulate the Particular Temperature Model:**
   $$T(t) = 20 + (75 - 20)e^{-kt} = 20 + 55e^{-kt}$$

2. **Evaluate at $t = 4\text{ minutes}$:**
   $$30 = 20 + 55e^{-4k}$$
   $$10 = 55e^{-4k} \implies \frac{10}{55} = \frac{2}{11} = e^{-4k}$$
   $$e^{-k} = \left(\frac{2}{11}\right)^{1/4}$$
   Therefore:
   $$T(t) = 20 + 55\left(\frac{2}{11}\right)^{t/4}$$

3. **Set $T(t) = 20.5^\circ\text{F}$ and Solve for Elapsed Time $t$:**
   $$20.5 = 20 + 55\left(\frac{2}{11}\right)^{t/4}$$
   $$0.5 = 55\left(\frac{2}{11}\right)^{t/4}$$
   $$\frac{0.5}{55} = \frac{1}{110} = \left(\frac{2}{11}\right)^{t/4}$$

4. **Logarithmic Resolution:**
   $$\ln\left(\frac{1}{110}\right) = \frac{t}{4} \ln\left(\frac{2}{11}\right)$$
   $$t = \frac{4\ln(1/110)}{\ln(2/11)} = \frac{4(-\ln 110)}{\ln 2 - \ln 11} = \frac{-4(4.70048)}{-1.70475} \approx \mathbf{11.029\text{ minutes}}$$

### Independent Verification
- At $t = 4\text{ min}$: $T = 30^\circ\text{F}$ ($\Delta T = 10^\circ\text{F}$).
- At $t = 8\text{ min}$: $\Delta T = 10 \times (2/11) \approx 1.818^\circ\text{F}$ ($T \approx 21.82^\circ\text{F}$).
- At $t = 11.029\text{ min}$: $\Delta T = 0.50^\circ\text{F}$ ($T = 20.50^\circ\text{F}$).
- **Final Result:** $\mathbf{11.029\text{ minutes}}$ (Matches MATHalino exactly).

---

## 4. Simple Chemical Conversion & Radioactive Decay: Governing Theory

### Physical Law
In elementary chemical conversions and spontaneous radioactive decay, the rate of transformation of an unconverted/undecayed substance is directly proportional to the instantaneous amount of substance remaining:

$$\frac{dx}{dt} = -kx \quad (k > 0)$$

where $x(t)$ represents the quantity of unconverted reactant or undecayed radioactive nuclei remaining at time $t$.

### Separation & Integration
$$\frac{dx}{x} = -k\,dt \implies \int \frac{dx}{x} = -k \int dt \implies \ln x = -kt + \ln C$$
$$x(t) = C e^{-kt}$$
With initial condition $x(0) = x_0$:
$$x(t) = x_0 e^{-kt}$$

---

## 5. Mathalino Radioactive Decay Problem 01: Radium Half-Life

**Direct Source Citation:**  
[MATHalino Reviewer: Find how long would it take for half amount of radium to decompose](https://mathalino.com/reviewer/elementary-differential-equations/01-half-life-decomposing-radium)

### Problem Statement
Radium decomposes at a rate proportional to the quantity of radium present. Suppose it is found that in $25\text{ years}$ approximately $1.1\%$ of a certain quantity of radium has decomposed. Determine how long (in years) it will take for one-half of the original amount of radium to decompose.

### Given Data
- Percentage decomposed at $t = 25\text{ years}$: $1.1\%$
- Remaining amount: $x(25) = (100\% - 1.1\%)x_0 = 98.9\% x_0 = 0.989 x_0$
- Target: Find half-life $t_{1/2}$ such that $x(t) = 0.5 x_0$

### Step-by-Step Derivation
1. **Formulate the Decay Model:**
   $$x(t) = x_0 e^{-kt}$$

2. **Substitute the 25-Year Observation:**
   $$0.989 x_0 = x_0 e^{-25k} \implies 0.989 = e^{-25k} \implies e^{-k} = (0.989)^{1/25}$$
   Thus:
   $$x(t) = x_0 (0.989)^{t/25}$$

3. **Set $x(t) = 0.5 x_0$ for One-Half Remaining:**
   $$0.5 x_0 = x_0 (0.989)^{t/25}$$
   $$0.5 = (0.989)^{t/25} \implies 0.5^{25} = 0.989^t$$

4. **Solve via Natural Logarithms:**
   $$25 \ln(0.5) = t \ln(0.989)$$
   $$t = \frac{25 \ln(0.5)}{\ln(0.989)} = \frac{25(-0.693147)}{-0.011061} \approx \mathbf{1566.65\text{ years}}$$

### Independent Verification
- Decay rate per year: $\approx \frac{1.1\%}{25} = 0.044\%$ per year.
- Using continuous approximation: $t_{1/2} \approx \frac{\ln 2}{k} = \frac{0.69315}{0.0004424} \approx 1566.65\text{ years}$.
- **Final Result:** $\mathbf{1,566.65\text{ years}}$ (Matches MATHalino exactly).

---

## 6. Mathalino Radioactive Decay Problem 02: 90% Dissipated

**Direct Source Citation:**  
[MATHalino Reviewer: Time to dissipate 90% of certain radioactive substance](https://mathalino.com/reviewer/elementary-differential-equations/02-time-dissipite-90-certain-radioactive-substance)

### Problem Statement
A certain radioactive substance has a half-life of $38\text{ hours}$. Find how long it takes for $90\%$ of the radioactivity to be dissipated.

### Given Data
- Half-life: $t_{1/2} = 38\text{ hours}$ ($x(38) = 0.5 x_0$)
- Dissipation condition: $90\%$ dissipated implies $10\%$ remains:
  $$x(t) = (100\% - 90\%)x_0 = 0.10 x_0$$

### Step-by-Step Derivation
1. **Formulate the Decay Function Using Half-Life Base:**
   $$x(t) = x_0 e^{-kt}$$
   At $t = 38\text{ hr}$, $x = 0.5 x_0$:
   $$0.5 = e^{-38k} \implies e^{-k} = (0.5)^{1/38}$$
   $$x(t) = x_0 (0.5)^{t/38}$$

2. **Set $x(t) = 0.10 x_0$:**
   $$0.10 x_0 = x_0 (0.5)^{t/38} \implies 0.10 = (0.5)^{t/38}$$

3. **Solve Logarithmically:**
   $$\ln(0.10) = \frac{t}{38} \ln(0.5)$$
   $$t = \frac{38 \ln(0.10)}{\ln(0.5)} = \frac{38(-2.302585)}{-0.693147} \approx \mathbf{126.23\text{ hours}}$$

### Independent Verification
- After $1$ half-life ($38\text{ hr}$): $50\%$ remains.
- After $2$ half-lives ($76\text{ hr}$): $25\%$ remains.
- After $3$ half-lives ($114\text{ hr}$): $12.5\%$ remains.
- After $3.322$ half-lives: $0.5^{3.322} = 0.10$ ($10\%$ remains).
- $3.3219 \times 38\text{ hr} \approx 126.23\text{ hours}$.
- **Final Result:** $\mathbf{126.23\text{ hours}}$ (Matches MATHalino exactly).

---

## 7. Engineering Physics Extension: Velocity of Escape from Earth

**Direct Source Citation:**  
[MATHalino Reviewer: Elementary Applications — Velocity of Escape from the Earth](https://mathalino.com/reviewer/applications)

### Physical Law
According to Newton's Law of Universal Gravitation, the gravitational attractive force on a projectile of mass $m$ at distance $r$ from the Earth's center is:

$$F = -G\frac{M m}{r^2} = -m\frac{g R^2}{r^2}$$

where $R$ is the radius of the Earth, and $g = \frac{GM}{R^2}$ is the acceleration due to gravity at Earth's surface ($9.81\text{ m/s}^2$).

By Newton's second law, acceleration in vertical radial motion is $a = \frac{dv}{dt} = v\frac{dv}{dr}$:

$$v\frac{dv}{dr} = -\frac{g R^2}{r^2}$$

### Separation & Integration
$$\int v\,dv = -g R^2 \int r^{-2}dr$$
$$\frac{1}{2}v^2 = \frac{g R^2}{r} + C$$

### Boundary Condition & Minimum Escape Speed
For the projectile to break free and escape Earth's gravitational potential without returning, its velocity must remain non-negative as $r \to \infty$:
$$\lim_{r \to \infty} \frac{1}{2}v^2 = 0 + C \ge 0 \implies C \ge 0$$

For the minimum escape velocity $v_{esc}$ launched from Earth's surface ($r = R$):
$$\frac{1}{2}v_{esc}^2 = \frac{g R^2}{R} = g R$$
$$v_{esc} = \sqrt{2gR}$$

### Numerical Evaluation
With standard physical constants:
- $g \approx 9.80665\text{ m/s}^2$
- $R \approx 6,371\text{ km} = 6.371 \times 10^6\text{ m}$

$$v_{esc} = \sqrt{2 \times 9.80665 \times 6.371 \times 10^6} \approx \sqrt{1.2495 \times 10^8} \approx 11,178\text{ m/s} \approx \mathbf{11.18\text{ km/s}}$$
In Imperial units ($g \approx 32.174\text{ ft/s}^2, R \approx 3,959\text{ miles}$):
$$v_{esc} \approx \mathbf{6.95\text{ mi/s}} \approx \mathbf{25,020\text{ mph}}$$
