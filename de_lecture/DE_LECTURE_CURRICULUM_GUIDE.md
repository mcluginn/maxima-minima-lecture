# Elementary Applications of First-Order Differential Equations
## Master Curriculum Guide, Slide Architecture & Teleprompter Notes

**Lecture Title:** Elementary Applications of First-Order Differential Equations  
**Primary Reference:** MATHalino Engineering Math Review ([mathalino.com/reviewer/applications](https://mathalino.com/reviewer/applications))  
**Target Duration:** 45–60 Minutes (21 Presentation Segments)  
**Teaching Platform:** iPad Pro / Apple Pencil Inking Deck with Embedded Manim Animations  

---

### Pedagogical Strategy: The 9-Step Learning Progression
1. **Physical Intuition:** Observe a physical rate of change before writing equations.
2. **Mathematical Formulation:** State the physical proportionality law ($\frac{dy}{dt} \propto \Delta$).
3. **Parameter Definition:** Clarify independent ($t$), dependent ($y$), and rate constant ($k > 0$).
4. **Governing ODE:** Formulate the first-order autonomous differential equation.
5. **Separation & Integration:** Rigorously separate variables and integrate analytically.
6. **Initial Condition (IVP):** Apply $y(0) = y_0$ to determine the constant of integration $C$.
7. **Model Interpretation:** Analyze the resulting exponential function and its physical bounds.
8. **Application & Prediction:** Solve practical engineering questions using logarithms and algebra.
9. **Physical Verification:** Cross-check results against boundary conditions and empirical milestones.

---

### Slide-by-Slide Teaching Sequence & Apple Pencil Prompts

#### Slide 01: Title Slide — Mathematical Modeling in Motion
- **Visual Asset:** `Scene01_IntroDE.mp4` / Still Frame `Scene01_IntroDE.png`
- **Learning Objective:** Set up the lecture scope and contrast static algebra with dynamic differential equations.
- **Lecturer Speaking Notes:** "Welcome, class. Today we bridge empirical physics and calculus. Most engineering phenomena aren't static snapshots—they are systems in continuous motion governed by rates of change. First-order differential equations are the mathematical language that describes this change."
- **Apple Pencil Annotation Prompt:** Circle the rate term $\frac{dy}{dt}$ on the board and draw a continuous tangent vector arrow pointing forward.

#### Slide 02: Physical Rates & The 4-Step Blueprint
- **Visual Asset:** `Scene02_ModelingBlueprint.mp4` / `Scene02_ModelingBlueprint.png`
- **Learning Objective:** Internalize the 4 universal steps to model any rate-governed engineering system.
- **Lecturer Speaking Notes:** "Regardless of whether we study thermal cooling, radioactive decay, chemical reactions, or spaceflight kinematics, the mathematical workflow remains identical. Step 1: Formulate the physical rate law. Step 2: Write the differential equation with proportionality constant $k$. Step 3: Separate variables and integrate. Step 4: Apply boundary conditions."
- **Interactive Check Question:** "Why must the proportionality constant $k$ be accompanied by an explicit negative sign when physical quantities decay?"

#### Slide 03: Separation of Variables Mathematical Engine
- **Visual Asset:** `Scene03_SeparationVariables.mp4` / `Scene03_SeparationVariables.png`
- **Learning Objective:** Master the algebraic mechanism of separating differentials $\frac{dy}{g(y)} = h(t)dt$.
- **Lecturer Speaking Notes:** "Separation of variables is our primary analytical engine for first-order ODEs. Notice how Leibniz notation $\frac{dy}{dt}$ behaves operationally: we group all dependent terms on the left with $dy$, and all independent terms on the right with $dt$. Integration transforms a differential statement into a function family."
- **Apple Pencil Annotation Prompt:** Highlight the differential pairing $(dy \leftrightarrow g(y))$ and $(dt \leftrightarrow h(t))$.

#### Slide 04: Newton's Law of Cooling — Physical Intuition
- **Visual Asset:** `NewtonCoolingPrototype.mp4` / `cooling_final_frame.png`
- **Learning Objective:** Connect the rate of temperature loss to the thermal driving force $(T - T_s)$.
- **Lecturer Speaking Notes:** "Observe the thermometer. When placed in freezing outside air ($10^\circ\text{F}$), the mercury drops rapidly at first because the temperature difference $(T - T_s)$ is large ($60^\circ\text{F}$). As the thermometer cools, the driving force shrinks, and the rate of cooling $\frac{dT}{dt}$ slows down asymptotically."
- **Interactive Check Question:** "Can a cooling object ever drop below the ambient temperature under purely convective cooling?"

#### Slide 05: Continuous Derivation Morph — Newton's Law
- **Visual Asset:** `Scene04_NewtonCoolingLaw.mp4` / `Scene04_NewtonCoolingLaw.png`
- **Learning Objective:** Derive $T(t) = T_s + (T_0 - T_s)e^{-kt}$ from first principles.
- **Lecturer Speaking Notes:** "Watch each line morph into the next: $\frac{dT}{dt} = -k(T - T_s)$ separates to $\frac{dT}{T - T_s} = -k\,dt$. Integrating gives $\ln(T - T_s) = -kt + \ln C_1$. Exponentiating yields $T - T_s = C_1 e^{-kt}$. When $t = 0$, $T = T_0$, proving that $C_1 = T_0 - T_s$."
- **Apple Pencil Annotation Prompt:** Derive the constant $C_1$ step-by-step in the annotation margin.

#### Slide 06: Mathalino Problem 01 — Thermometer Reading After 6 Minutes
- **Visual Asset:** `Scene05_CoolingProblem1_Thermometer6Min.mp4` / `Scene05_CoolingProblem1_Thermometer6Min.png`
- **Learning Objective:** Solve for the unknown cooling constant $k$ using intermediate observation $T(3) = 25^\circ\text{F}$.
- **Lecturer Speaking Notes:** "MATHalino Problem 01 provides authentic data: inside house at $70^\circ\text{F}$, taken outside to $10^\circ\text{F}$. Three minutes later, the reading is $25^\circ\text{F}$. What will the thermometer read after 6 minutes?"
- **Guided Exercise:** Have students set up $25 = 10 + 60e^{-3k}$ and deduce $e^{-3k} = 1/4$ before revealing the next slide.

#### Slide 07: Problem 01 Exact Resolution & Ratio Insight
- **Visual Asset:** `Scene05_CoolingProblem1_Thermometer6Min.png`
- **Learning Objective:** Calculate $T(6) = 13.75^\circ\text{F}$ and observe the constant ratio decay principle.
- **Lecturer Speaking Notes:** "Notice the elegant shortcut: in equal time intervals of 3 minutes, the excess temperature drops by a constant factor of $1/4$. From $t=0$ to $t=3$, $\Delta T$ drops from $60^\circ$ to $15^\circ$. From $t=3$ to $t=6$, $\Delta T$ drops from $15^\circ$ to $3.75^\circ$. Thus $T(6) = 10 + 3.75 = 13.75^\circ\text{F}$."
- **Apple Pencil Annotation Prompt:** Sketch the ratio arrows on the temperature axis: $60 \to 15 \to 3.75$.

#### Slide 08: Mathalino Problem 02 — Time to Within Half Degree of Air
- **Visual Asset:** `Scene06_CoolingProblem2_HalfDegree.mp4` / `Scene06_CoolingProblem2_HalfDegree.png`
- **Learning Objective:** Formulate a transcendental equation for time $t$ using natural logarithms.
- **Lecturer Speaking Notes:** "In MATHalino Problem 02, $T_0 = 75^\circ\text{F}$, $T_s = 20^\circ\text{F}$, and $T(4) = 30^\circ\text{F}$. We want to find when the reading drops to within half a degree of the air temperature. That means $T - T_s = 0.5^\circ\text{F}$, so $T = 20.5^\circ\text{F}$."
- **Interactive Check Question:** "Why can't we simply ask when $T = 20^\circ\text{F}$ exactly?" (Answer: Exponential decay approaches $T_s$ asymptotically as $t \to \infty$; exact equality requires infinite time).

#### Slide 09: Problem 02 Logarithmic Derivation
- **Visual Asset:** `Scene06_CoolingProblem2_HalfDegree.png`
- **Learning Objective:** Solve $20.5 = 20 + 55(2/11)^{t/4}$ for $t \approx 11.029\text{ minutes}$.
- **Lecturer Speaking Notes:** "Isolating the exponential term gives $\frac{0.5}{55} = \frac{1}{110} = (2/11)^{t/4}$. Taking natural logarithms of both sides yields $t = \frac{4\ln(1/110)}{\ln(2/11)} \approx 11.029\text{ minutes}$."
- **Apple Pencil Annotation Prompt:** Write out $\ln(1/110) = -\ln 110$ and demonstrate how both negative signs cancel to produce a positive elapsed time.

#### Slide 10: Live Teaching & Annotation Pause: Thermal Modeling
- **Visual Asset:** Dual-axis annotation frame
- **Learning Objective:** Student self-check on Newton's cooling model and parameter sensitivity.
- **Apple Pencil Workspace:** Ample blank grid area for instructor to solve variations (e.g. warming problem where $T_0 < T_s$).

#### Slide 11: Simple Chemical Conversion & Radioactive Decay
- **Visual Asset:** `Scene07_ChemicalConversion_Decay.mp4` / `Scene07_ChemicalConversion_Decay.png`
- **Learning Objective:** Understand first-order reaction kinetics $\frac{dx}{dt} = -kx$ and derive $x(t) = x_0 e^{-kt}$.
- **Lecturer Speaking Notes:** "In first-order chemical reactions and radioactive decay, the rate at which unconverted substance disappears is proportional to the amount remaining. The negative sign represents continuous dissipation."

#### Slide 12: Stochastic Particle Kinetics vs Continuum Model
- **Visual Asset:** `RadioactiveDecayPrototype.mp4` / `decay_final_frame.png`
- **Learning Objective:** Reconcile individual random quantum decay events with continuous deterministic macroscopic ODEs.
- **Lecturer Speaking Notes:** "Individual atomic decay events are probabilistic. However, with Avogadro-scale quantities of atoms ($10^{23}$ particles), the law of large numbers converts stochastic events into an extraordinarily precise continuous ODE."

#### Slide 13: Mathalino Decay Problem 01 — Radium Half-Life
- **Visual Asset:** `Scene08_RadiumProblem1_HalfLife.mp4` / `Scene08_RadiumProblem1_HalfLife.png`
- **Learning Objective:** Determine the half-life of Radium from a century-scale baseline ($1.1\%$ in 25 years).
- **Lecturer Speaking Notes:** "MATHalino Radium Problem 01 states that in 25 years, approximately $1.1\%$ of radium decomposes. How long does it take for half the original amount to decompose?"
- **Guided Exercise:** Ensure students recognize that $1.1\%$ decomposed means $98.9\%$ ($0.989 x_0$) remains unconverted!

#### Slide 14: Radium Half-Life Analytical Resolution
- **Visual Asset:** `Scene08_RadiumProblem1_HalfLife.png`
- **Learning Objective:** Calculate $t_{1/2} = \frac{25\ln 0.5}{\ln 0.989} \approx 1,566.65\text{ years}$.
- **Lecturer Speaking Notes:** "Setting $0.5 = (0.989)^{t/25}$ gives $t = \frac{25\ln(0.5)}{\ln(0.989)} \approx 1,566.65\text{ years}$. Notice how a tiny 25-year sample accurately calibrates a multi-millennium geological clock."

#### Slide 15: Mathalino Decay Problem 02 — 90% Dissipation
- **Visual Asset:** `Scene09_DecayProblem2_90Percent.mp4` / `Scene09_DecayProblem2_90Percent.png`
- **Learning Objective:** Solve for target dissipation when half-life $t_{1/2} = 38\text{ hours}$ is given.
- **Lecturer Speaking Notes:** "A radioactive isotope has a 38-hour half-life. Find when 90% has dissipated. Be vigilant with terminology: $90\%$ dissipated means exactly $10\%$ ($0.10 x_0$) remains!"

#### Slide 16: Problem 02 Threshold Resolution
- **Visual Asset:** `Scene09_DecayProblem2_90Percent.png`
- **Learning Objective:** Solve $0.10 = (0.5)^{t/38}$ to obtain $t \approx 126.23\text{ hours}$.
- **Lecturer Speaking Notes:** "Taking logarithms yields $t = \frac{38\ln 0.1}{\ln 0.5} \approx 126.23\text{ hours}$. Notice that 3 half-lives ($114\text{ hr}$) leaves $12.5\%$, so reaching $10\%$ requires slightly more than 3 half-lives."

#### Slide 17: Engineering Physics Extension — Velocity of Escape from Earth
- **Visual Asset:** `Scene10_EscapeVelocity.mp4` / `Scene10_EscapeVelocity.png`
- **Learning Objective:** Model vertical projectile motion under inverse-square variable gravity using $a = v\frac{dv}{dr}$.
- **Lecturer Speaking Notes:** "On the MATHalino index, velocity of escape is a premier engineering application. Gravity is not constant over spaceflight distances: $F = -m\frac{g R^2}{r^2}$. Using the kinematic chain rule $a = v\frac{dv}{dr}$, we obtain the separable ODE $v\,dv = -g R^2 r^{-2} dr$."

#### Slide 18: Escape Velocity Analytical Derivation
- **Visual Asset:** `Scene10_EscapeVelocity.png`
- **Learning Objective:** Integrate $\int v\,dv = -g R^2 \int r^{-2}dr$ and derive $v_{esc} = \sqrt{2gR} \approx 11.18\text{ km/s}$.
- **Lecturer Speaking Notes:** "Integrating gives $\frac{1}{2}v^2 = \frac{g R^2}{r} + C$. Requiring $v \ge 0$ as $r \to \infty$ forces $C \ge 0$. At Earth's surface ($r = R$), minimum escape velocity is $v_{esc} = \sqrt{2gR} \approx 11.18\text{ km/s}$ ($6.95\text{ mi/s}$ or $25,000\text{ mph}$)."

#### Slide 19: Master Comparative Modeling Matrix
- **Visual Asset:** `Scene11_SynthesisComparison.mp4` / `Scene11_SynthesisComparison.png`
- **Learning Objective:** Synthesize the 3 core applications side-by-side in a comparative engineering matrix.
- **Lecturer Speaking Notes:** "Compare all three: Newton's cooling seeks thermal equilibrium ($T \to T_s$), radioactive decay seeks nuclear equilibrium ($x \to 0$), and escape velocity overcomes gravitational attraction ($r \to \infty$). All three yield to separation of variables."

#### Slide 20: Comprehensive Summary & Live Teaching Board
- **Visual Asset:** Full-screen summary board with Apple Pencil annotation zones.
- **Learning Objective:** Review core formulas, logarithmic techniques, and engineering takeaways.

#### Slide 21: Academic References & MATHalino Citations
- **Visual Asset:** Citations card linking all source problems on MATHalino, Stewart Calculus, and Boyce & DiPrima ODEs.
