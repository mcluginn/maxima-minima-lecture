from manim import *
import numpy as np

# Global Dark Engineering Theme Configuration
config.background_color = "#0B0F19"
CYAN = "#38BDF8"       # Dynamic Curves / Dependent Variables
AMBER = "#F59E0B"      # Target Values / Milestones / Critical Extrema
CORAL = "#F43F5E"      # Alerts / Negative Rates / Heat
GREEN = "#10B981"      # Solved States / Validated Results / Half-Life
TEXT_WHITE = "#F8FAFC"
MUTED_GRAY = "#94A3B8"
AXES_GRAY = "#475569"
CARD_BG = "#0F172A"


# =============================================================================
# SCENE 1: Introduction to Differential Equations in Motion
# =============================================================================
class Scene01_IntroDE(Scene):
    def construct(self):
        # Title Banner
        title = Text("Applications of Differential Equations", font_size=32, color=TEXT_WHITE, weight=BOLD)
        subtitle = Text("Elementary Engineering Applications // First-Order Physical Models", font_size=18, color=CYAN)
        banner = VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.4)
        self.play(FadeIn(banner, shift=DOWN * 0.2), run_time=1.0)

        # Concept Comparison Cards
        card_l = RoundedRectangle(corner_radius=0.18, height=3.6, width=5.6, stroke_color=AXES_GRAY, fill_color=CARD_BG, fill_opacity=0.9).move_to([-3.2, -0.6, 0])
        card_r = RoundedRectangle(corner_radius=0.18, height=3.6, width=5.6, stroke_color=CYAN, fill_color=CARD_BG, fill_opacity=0.9).move_to([3.2, -0.6, 0])

        txt_l_head = Text("Static Algebra", font_size=20, color=MUTED_GRAY, weight=BOLD).next_to(card_l.get_top(), DOWN, buff=0.25)
        txt_l_body = VGroup(
            Text("• Describes static state: y = f(x)", font_size=15, color=TEXT_WHITE),
            Text("• Evaluates fixed snapshots", font_size=15, color=TEXT_WHITE),
            Text("• No intrinsic rate mechanism", font_size=15, color=MUTED_GRAY),
            MathTex(r"y = 3x^2 - 12", font_size=20, color=MUTED_GRAY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).next_to(txt_l_head, DOWN, buff=0.3)

        txt_r_head = Text("Dynamic Differential Model", font_size=20, color=CYAN, weight=BOLD).next_to(card_r.get_top(), DOWN, buff=0.25)
        txt_r_body = VGroup(
            Text("• Describes physical rate of change", font_size=15, color=TEXT_WHITE),
            Text("• Relates rate to current state", font_size=15, color=TEXT_WHITE),
            Text("• Predicts continuous future evolution", font_size=15, color=AMBER),
            MathTex(r"\frac{dy}{dt} = -k\,(y - y_s)", font_size=22, color=CYAN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).next_to(txt_r_head, DOWN, buff=0.3)

        self.play(Create(card_l), Write(txt_l_head), FadeIn(txt_l_body), run_time=1.2)
        self.wait(0.5)
        self.play(Create(card_r), Write(txt_r_head), FadeIn(txt_r_body), run_time=1.2)
        self.wait(2.0)


# =============================================================================
# SCENE 2: The 4-Step Physical Modeling Blueprint
# =============================================================================
class Scene02_ModelingBlueprint(Scene):
    def construct(self):
        title = Text("The 4-Step Mathematical Modeling Blueprint", font_size=30, color=TEXT_WHITE, weight=BOLD).to_edge(UP, buff=0.4)
        subtitle = Text("From Empirical Physics to Predictive Calculus", font_size=16, color=CYAN).next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.8)

        steps = [
            ("Step 1: Physical Law Formulation", "Translate observed physics into a rate relation", r"\frac{dy}{dt} \propto \text{driving potential}"),
            ("Step 2: Differential Equation Setup", "Introduce proportionality constant k and sign", r"\frac{dy}{dt} = -k\,(y - y_s)"),
            ("Step 3: Separation of Variables", "Group variables with their respective differentials", r"\frac{dy}{y - y_s} = -k\,dt \implies \int \frac{dy}{y - y_s} = -k\int dt"),
            ("Step 4: Initial Value Resolution", "Apply initial conditions y(0) = y₀ to determine C", r"y(t) = y_s + (y_0 - y_s)e^{-kt}")
        ]

        step_cards = VGroup()
        for i, (hdr, desc, math_str) in enumerate(steps):
            box = RoundedRectangle(corner_radius=0.15, height=1.05, width=11.2, stroke_color=CYAN if i%2==0 else AMBER, stroke_width=1.8, fill_color=CARD_BG, fill_opacity=0.9)
            h = Text(hdr, font_size=16, color=CYAN if i%2==0 else AMBER, weight=BOLD).align_to(box, UL).shift(RIGHT * 0.3 + DOWN * 0.22)
            d = Text(desc, font_size=13, color=MUTED_GRAY).next_to(h, DOWN, buff=0.1, aligned_edge=LEFT)
            m = MathTex(math_str, font_size=19, color=TEXT_WHITE).align_to(box, UR).shift(LEFT * 0.4 + DOWN * 0.35)
            card = VGroup(box, h, d, m)
            step_cards.add(card)

        step_cards.arrange(DOWN, buff=0.2).next_to(subtitle, DOWN, buff=0.35)

        for card in step_cards:
            self.play(FadeIn(card, shift=UP * 0.15), run_time=0.7)
            self.wait(0.3)

        self.wait(2.0)


# =============================================================================
# SCENE 3: Separation of Variables Mathematical Engine
# =============================================================================
class Scene03_SeparationVariables(Scene):
    def construct(self):
        title = Text("Separation of Variables Engine", font_size=30, color=TEXT_WHITE, weight=BOLD).to_edge(UP, buff=0.4)
        subtitle = Text("Algorithmic Derivation for First-Order Autonomous & Factorable DEs", font_size=16, color=CYAN).next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.8)

        # Container card for continuous morphing
        card = RoundedRectangle(corner_radius=0.2, height=4.2, width=9.6, stroke_color=CYAN, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.95).shift(DOWN * 0.2)
        self.play(Create(card), run_time=0.8)

        eq1 = MathTex(r"\frac{dy}{dt} = g(y)\,h(t)", font_size=32, color=TEXT_WHITE).move_to(card.get_center())
        eq2 = MathTex(r"\frac{1}{g(y)}\,dy = h(t)\,dt", font_size=32, color=AMBER).move_to(card.get_center())
        eq3 = MathTex(r"\int \frac{dy}{g(y)} = \int h(t)\,dt + C", font_size=32, color=CYAN).move_to(card.get_center())
        eq4 = MathTex(r"G(y) = H(t) + C \implies y(t) = G^{-1}(H(t) + C)", font_size=30, color=GREEN).move_to(card.get_center())

        label1 = Text("1. Standard First-Order Factorable Form", font_size=15, color=MUTED_GRAY).next_to(card.get_top(), DOWN, buff=0.3)
        label2 = Text("2. Separate Variables: y on Left, t on Right", font_size=15, color=MUTED_GRAY).next_to(card.get_top(), DOWN, buff=0.3)
        label3 = Text("3. Apply Continuous Indefinite Integration", font_size=15, color=MUTED_GRAY).next_to(card.get_top(), DOWN, buff=0.3)
        label4 = Text("4. Explicit Analytical Solution Family", font_size=15, color=MUTED_GRAY).next_to(card.get_top(), DOWN, buff=0.3)

        self.play(Write(label1), Write(eq1), run_time=1.0)
        self.wait(1.0)

        self.play(ReplacementTransform(label1, label2), ReplacementTransform(eq1, eq2), run_time=1.0)
        self.wait(1.0)

        self.play(ReplacementTransform(label2, label3), ReplacementTransform(eq2, eq3), run_time=1.0)
        self.wait(1.0)

        self.play(ReplacementTransform(label3, label4), ReplacementTransform(eq3, eq4), run_time=1.0)
        self.wait(2.0)


# =============================================================================
# SCENE 4: Newton's Law of Cooling - Analytical Derivation Morph
# =============================================================================
class Scene04_NewtonCoolingLaw(Scene):
    def construct(self):
        title = Text("Newton's Law of Cooling: Analytical Derivation", font_size=28, color=TEXT_WHITE, weight=BOLD).to_edge(UP, buff=0.4)
        subtitle = Text("Rate of change is proportional to the temperature difference", font_size=15, color=CYAN).next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.8)

        # Derivation box
        box = RoundedRectangle(corner_radius=0.2, height=4.4, width=10.4, stroke_color=CYAN, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.95).shift(DOWN * 0.25)
        self.play(Create(box), run_time=0.8)

        steps = [
            MathTex(r"\frac{dT}{dt} = -k\,(T - T_s)", font_size=28, color=WHITE),
            MathTex(r"\frac{dT}{T - T_s} = -k\,dt", font_size=28, color=WHITE),
            MathTex(r"\int \frac{dT}{T - T_s} = -k\int dt", font_size=28, color=CYAN),
            MathTex(r"\ln(T - T_s) = -kt + \ln C_1", font_size=28, color=CYAN),
            MathTex(r"T - T_s = C_1 e^{-kt}", font_size=28, color=AMBER),
            MathTex(r"\text{At } t = 0,\, T = T_0 \implies C_1 = T_0 - T_s", font_size=26, color=AMBER),
            MathTex(r"T(t) = T_s + (T_0 - T_s)\,e^{-kt}", font_size=32, color=GREEN)
        ]

        for s in steps:
            s.move_to(box.get_center())

        curr = steps[0]
        self.play(Write(curr), run_time=0.8)
        self.wait(0.6)

        for nxt in steps[1:]:
            self.play(ReplacementTransform(curr, nxt), run_time=0.8)
            curr = nxt
            self.wait(0.5)

        self.wait(2.0)


# =============================================================================
# SCENE 5: Cooling Problem 1 - Thermometer After 6 Minutes (Mathalino 01)
# =============================================================================
class Scene05_CoolingProblem1_Thermometer6Min(Scene):
    def construct(self):
        title = Text("Mathalino Problem 01: Thermometer Reading After 6 Minutes", font_size=27, color=TEXT_WHITE, weight=BOLD)
        subtitle = Text("Given: T₀ = 70°F, Ts = 10°F (Outside), T(3) = 25°F. Find T(6).", font_size=15, color=CYAN)
        banner = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_corner(UL, buff=0.4)
        self.play(FadeIn(banner), run_time=0.8)

        # 1. Vector Thermometer (Left)
        stem = RoundedRectangle(corner_radius=0.16, height=3.8, width=0.34, stroke_color=WHITE, stroke_width=2.5, fill_color="#1E293B", fill_opacity=0.6).move_to([-4.8, -0.4, 0])
        bulb = Circle(radius=0.36, stroke_color=WHITE, stroke_width=2.5, fill_color=CORAL, fill_opacity=0.9).move_to(stem.get_bottom() + DOWN * 0.12)
        ambient_box = RoundedRectangle(corner_radius=0.18, height=4.6, width=2.2, stroke_color=CYAN, stroke_width=1.5, stroke_opacity=0.5, fill_color="#0369A1", fill_opacity=0.12).move_to([-4.8, -0.4, 0])
        ambient_tag = Text("Air: Ts = 10°F", font_size=12, color=CYAN, weight=BOLD).next_to(ambient_box, UP, buff=0.12)

        temp_tracker = ValueTracker(70.0)

        def get_mercury():
            val = max(10.0, min(70.0, temp_tracker.get_value()))
            h = max(0.2, ((val - 10.0) / 60.0) * 3.2)
            m = Rectangle(width=0.22, height=h, fill_color=CORAL, fill_opacity=0.95, stroke_width=0)
            m.align_to(bulb.get_top() + DOWN * 0.08, DOWN).set_x(stem.get_x())
            return m

        mercury = always_redraw(get_mercury)
        badge_bg = RoundedRectangle(corner_radius=0.1, height=0.42, width=1.1, fill_color=CARD_BG, stroke_color=AMBER, stroke_width=1.5)
        badge_txt = always_redraw(lambda: Text(f"{temp_tracker.get_value():.1f}°F", font_size=14, color=AMBER, weight=BOLD).move_to(badge_bg.get_center()))
        badge = VGroup(badge_bg, badge_txt)
        badge.add_updater(lambda b: b.next_to(mercury, RIGHT, buff=0.15).align_to(mercury.get_top(), UP))

        self.play(FadeIn(ambient_box), FadeIn(ambient_tag), FadeIn(stem), FadeIn(bulb), FadeIn(mercury), FadeIn(badge), run_time=0.9)

        # 2. Axes & Curve (Right)
        axes = Axes(
            x_range=[0, 7.5, 1], y_range=[0, 80, 20],
            x_length=6.0, y_length=3.6,
            axis_config={"color": AXES_GRAY, "stroke_width": 2}
        ).to_corner(DR, buff=0.6).shift(UP * 0.1)

        x_lbl = Text("Time t (min)", font_size=13, color=MUTED_GRAY).next_to(axes.x_axis.get_end(), DOWN, buff=0.18).shift(LEFT * 0.5)
        y_lbl = Text("Temp T (°F)", font_size=13, color=MUTED_GRAY).next_to(axes.y_axis.get_top(), UP, buff=0.1)

        x_ticks = VGroup(*[Text(str(i), font_size=11, color=MUTED_GRAY).next_to(axes.c2p(i, 0), DOWN, buff=0.1) for i in [1, 2, 3, 4, 5, 6, 7]])
        y_ticks = VGroup(*[Text(str(j), font_size=11, color=MUTED_GRAY).next_to(axes.c2p(0, j), LEFT, buff=0.1) for j in [20, 40, 60, 80]])

        asym_line = DashedLine(axes.c2p(0, 10), axes.c2p(7.2, 10), color=CYAN, stroke_width=1.8, dash_length=0.1)
        asym_txt = MathTex(r"T_s = 10^\circ\text{F}", font_size=13, color=CYAN).next_to(axes.c2p(1.2, 10), UP, buff=0.06)

        def t_func(t):
            return 10.0 + 60.0 * (0.25 ** (t / 3.0))

        curve = axes.plot(t_func, x_range=[0, 6.0], color=CYAN, stroke_width=3.5)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), FadeIn(x_ticks), FadeIn(y_ticks), Create(asym_line), FadeIn(asym_txt), run_time=1.0)

        # Animate cooling
        t_val = ValueTracker(0.0)
        dot = Dot(color=AMBER, radius=0.08).move_to(axes.c2p(0, 70))
        dot.add_updater(lambda d: d.move_to(axes.c2p(t_val.get_value(), t_func(t_val.get_value()))))
        self.add(dot)

        self.play(Create(curve), t_val.animate.set_value(6.0), temp_tracker.animate.set_value(13.75), run_time=3.0, rate_func=linear)
        dot.clear_updaters()

        p0 = Dot(axes.c2p(0, 70), color=WHITE, radius=0.06)
        l0 = MathTex(r"(0, 70^\circ)", font_size=14, color=WHITE).next_to(p0, UR, buff=0.08)
        p3 = Dot(axes.c2p(3, 25), color=CYAN, radius=0.06)
        l3 = MathTex(r"(3, 25^\circ)", font_size=14, color=CYAN).next_to(p3, UR, buff=0.08)
        p6 = Dot(axes.c2p(6, 13.75), color=AMBER, radius=0.08)
        l6 = MathTex(r"(6, 13.75^\circ\text{F})", font_size=15, color=AMBER).next_to(p6, UR, buff=0.1)

        self.play(FadeIn(p0), Write(l0), FadeIn(p3), Write(l3), FadeIn(p6), Write(l6), run_time=0.8)

        # Formula and Result Card
        res_card = RoundedRectangle(corner_radius=0.15, height=1.1, width=4.8, fill_color=CARD_BG, fill_opacity=0.95, stroke_color=GREEN, stroke_width=2).move_to([1.2, 2.5, 0])
        eq_res = MathTex(r"T(t) = 10 + 60\left(\frac{1}{4}\right)^{t/3} \implies T(6) = \mathbf{13.75^\circ\text{F}}", font_size=20, color=GREEN).move_to(res_card.get_center())

        self.play(Create(res_card), Write(eq_res), run_time=0.9)
        self.wait(2.0)


# =============================================================================
# SCENE 6: Cooling Problem 2 - Time to Within Half Degree (Mathalino 02)
# =============================================================================
class Scene06_CoolingProblem2_HalfDegree(Scene):
    def construct(self):
        title = Text("Mathalino Problem 02: Time to Within Half Degree of Air", font_size=26, color=TEXT_WHITE, weight=BOLD)
        subtitle = Text("T₀ = 75°F, Ts = 20°F, T(4) = 30°F. Target: T = 20.5°F. Find elapsed time t.", font_size=15, color=CYAN)
        banner = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_corner(UL, buff=0.4)
        self.play(FadeIn(banner), run_time=0.8)

        # Coordinates & Axes
        axes = Axes(
            x_range=[0, 14, 2], y_range=[15, 80, 15],
            x_length=7.4, y_length=3.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2}
        ).to_corner(DR, buff=0.6).shift(UP * 0.1)

        x_lbl = Text("Time t (minutes)", font_size=13, color=MUTED_GRAY).next_to(axes.x_axis.get_end(), DOWN, buff=0.18).shift(LEFT * 0.6)
        y_lbl = Text("Temp T (°F)", font_size=13, color=MUTED_GRAY).next_to(axes.y_axis.get_top(), UP, buff=0.1)

        x_ticks = VGroup(*[Text(str(i), font_size=11, color=MUTED_GRAY).next_to(axes.c2p(i, 15), DOWN, buff=0.1) for i in [2, 4, 6, 8, 10, 12]])
        y_ticks = VGroup(*[Text(str(j), font_size=11, color=MUTED_GRAY).next_to(axes.c2p(0, j), LEFT, buff=0.1) for j in [30, 45, 60, 75]])

        # Ambient Asymptote (T = 20) & Half Degree Band (T = 20.5)
        asym = DashedLine(axes.c2p(0, 20), axes.c2p(13.5, 20), color=CYAN, stroke_width=1.8, dash_length=0.1)
        asym_l = MathTex(r"T_s = 20^\circ\text{F}", font_size=13, color=CYAN).next_to(axes.c2p(1.5, 20), DOWN, buff=0.08)

        target_line = DashedLine(axes.c2p(0, 20.5), axes.c2p(13.5, 20.5), color=AMBER, stroke_width=1.8, dash_length=0.08)
        target_tag = MathTex(r"T = 20.5^\circ\text{F}\text{ (Target)}", font_size=13, color=AMBER).next_to(axes.c2p(6.5, 20.5), UP, buff=0.08)

        def t_func2(t):
            return 20.0 + 55.0 * ((2.0 / 11.0) ** (t / 4.0))

        curve = axes.plot(t_func2, x_range=[0, 11.03], color=CYAN, stroke_width=3.5)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), FadeIn(x_ticks), FadeIn(y_ticks), Create(asym), FadeIn(asym_l), Create(target_line), FadeIn(target_tag), run_time=1.0)

        # Plot curve to target
        self.play(Create(curve), run_time=2.5, rate_func=linear)

        p0 = Dot(axes.c2p(0, 75), color=WHITE, radius=0.06)
        l0 = MathTex(r"(0, 75^\circ)", font_size=14, color=WHITE).next_to(p0, UR, buff=0.08)
        p4 = Dot(axes.c2p(4, 30), color=CYAN, radius=0.06)
        l4 = MathTex(r"(4, 30^\circ)", font_size=14, color=CYAN).next_to(p4, UR, buff=0.08)
        pt = Dot(axes.c2p(11.029, 20.5), color=AMBER, radius=0.09)
        lt = MathTex(r"(11.029\text{ min},\, 20.5^\circ\text{F})", font_size=15, color=AMBER).next_to(pt, UR, buff=0.1)

        self.play(FadeIn(p0), Write(l0), FadeIn(p4), Write(l4), FadeIn(pt), Write(lt), run_time=0.9)

        # Derivation Summary Box (Left)
        d_box = RoundedRectangle(corner_radius=0.18, height=3.6, width=4.6, stroke_color=AMBER, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.95).move_to([-4.0, -0.6, 0])
        d_text = VGroup(
            MathTex(r"T(t) = 20 + 55\left(\frac{2}{11}\right)^{t/4}", font_size=18, color=TEXT_WHITE),
            MathTex(r"20.5 = 20 + 55\left(\frac{2}{11}\right)^{t/4}", font_size=18, color=TEXT_WHITE),
            MathTex(r"\frac{0.5}{55} = \frac{1}{110} = \left(\frac{2}{11}\right)^{t/4}", font_size=18, color=CYAN),
            MathTex(r"t = \frac{4\ln(1/110)}{\ln(2/11)}", font_size=20, color=AMBER),
            MathTex(r"\mathbf{t \approx 11.029\text{ minutes}}", font_size=21, color=GREEN)
        ).arrange(DOWN, buff=0.18).move_to(d_box.get_center())

        self.play(Create(d_box), Write(d_text), run_time=1.2)
        self.wait(2.0)


# =============================================================================
# SCENE 7: Simple Chemical Conversion & Radioactive Decay Foundations
# =============================================================================
class Scene07_ChemicalConversion_Decay(Scene):
    def construct(self):
        title = Text("Simple Chemical Conversion & Radioactive Decay", font_size=28, color=TEXT_WHITE, weight=BOLD).to_edge(UP, buff=0.4)
        subtitle = Text("Rate of decrease is proportional to the remaining amount present", font_size=15, color=CYAN).next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.8)

        # Derivation box
        box = RoundedRectangle(corner_radius=0.2, height=4.2, width=10.4, stroke_color=CYAN, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.95).shift(DOWN * 0.25)
        self.play(Create(box), run_time=0.8)

        steps = [
            MathTex(r"\frac{dx}{dt} = -kx\quad (k > 0)", font_size=30, color=WHITE),
            MathTex(r"\frac{dx}{x} = -k\,dt", font_size=30, color=WHITE),
            MathTex(r"\int \frac{dx}{x} = -k\int dt \implies \ln x = -kt + C_1", font_size=28, color=CYAN),
            MathTex(r"x(t) = C\,e^{-kt}", font_size=30, color=AMBER),
            MathTex(r"\text{Initial condition: } x(0) = x_0 \implies C = x_0", font_size=27, color=AMBER),
            MathTex(r"x(t) = x_0\,e^{-kt}", font_size=34, color=GREEN)
        ]

        for s in steps:
            s.move_to(box.get_center())

        curr = steps[0]
        self.play(Write(curr), run_time=0.8)
        self.wait(0.6)

        for nxt in steps[1:]:
            self.play(ReplacementTransform(curr, nxt), run_time=0.8)
            curr = nxt
            self.wait(0.5)

        self.wait(2.0)


# =============================================================================
# SCENE 8: Radioactive Decay Problem 1 - Radium Half-Life (Mathalino 01)
# =============================================================================
class Scene08_RadiumProblem1_HalfLife(Scene):
    def construct(self):
        title = Text("Mathalino Decay 01: Radium Half-Life Determination", font_size=27, color=TEXT_WHITE, weight=BOLD)
        subtitle = Text("Given: In 25 yrs, 1.1% decomposes (x(25) = 0.989 x₀). Find half-life (x = 0.5 x₀).", font_size=15, color=CYAN)
        banner = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_corner(UL, buff=0.4)
        self.play(FadeIn(banner), run_time=0.8)

        # Coordinate axes across century scale
        axes = Axes(
            x_range=[0, 2000, 400], y_range=[0, 1.1, 0.2],
            x_length=7.4, y_length=3.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2}
        ).to_corner(DR, buff=0.6).shift(UP * 0.1)

        x_lbl = Text("Time t (years)", font_size=13, color=MUTED_GRAY).next_to(axes.x_axis.get_end(), DOWN, buff=0.18).shift(LEFT * 0.5)
        y_lbl = Text("Remaining Fraction x / x₀", font_size=13, color=MUTED_GRAY).next_to(axes.y_axis.get_top(), UP, buff=0.1)

        x_ticks = VGroup(*[Text(str(i), font_size=11, color=MUTED_GRAY).next_to(axes.c2p(i, 0), DOWN, buff=0.1) for i in [400, 800, 1200, 1600, 2000]])
        y_ticks = VGroup(*[Text(f"{j:.1f}", font_size=11, color=MUTED_GRAY).next_to(axes.c2p(0, j), LEFT, buff=0.1) for j in [0.2, 0.4, 0.6, 0.8, 1.0]])

        # 50% line
        h_line = DashedLine(axes.c2p(0, 0.5), axes.c2p(1900, 0.5), color=GREEN, stroke_width=1.8, dash_length=0.1)
        h_tag = MathTex(r"0.50\,x_0\text{ (Half-Life)}", font_size=13, color=GREEN).next_to(axes.c2p(300, 0.5), UP, buff=0.06)

        def rad_func(t):
            return 0.989 ** (t / 25.0)

        curve = axes.plot(rad_func, x_range=[0, 1566.65], color=CYAN, stroke_width=3.5)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), FadeIn(x_ticks), FadeIn(y_ticks), Create(h_line), FadeIn(h_tag), run_time=1.0)
        self.play(Create(curve), run_time=2.5, rate_func=linear)

        p0 = Dot(axes.c2p(0, 1.0), color=WHITE, radius=0.06)
        l0 = MathTex(r"(0, 1.0x_0)", font_size=14, color=WHITE).next_to(p0, UR, buff=0.08)
        p25 = Dot(axes.c2p(25, 0.989), color=CYAN, radius=0.06)
        l25 = MathTex(r"(25\text{ yr},\, 0.989x_0)", font_size=14, color=CYAN).next_to(p25, UR, buff=0.1)
        ph = Dot(axes.c2p(1566.65, 0.5), color=GREEN, radius=0.09)
        lh = MathTex(r"(1566.65\text{ yr},\, 0.5x_0)", font_size=15, color=GREEN).next_to(ph, UR, buff=0.1)

        self.play(FadeIn(p0), Write(l0), FadeIn(p25), Write(l25), FadeIn(ph), Write(lh), run_time=0.9)

        # Derivation Box (Left)
        d_box = RoundedRectangle(corner_radius=0.18, height=3.6, width=4.6, stroke_color=GREEN, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.95).move_to([-4.0, -0.6, 0])
        d_text = VGroup(
            MathTex(r"x(t) = x_0 (0.989)^{t/25}", font_size=18, color=TEXT_WHITE),
            MathTex(r"0.5 x_0 = x_0 (0.989)^{t/25}", font_size=18, color=TEXT_WHITE),
            MathTex(r"0.5^{25} = 0.989^t", font_size=18, color=CYAN),
            MathTex(r"t = \frac{25\ln 0.5}{\ln 0.989}", font_size=20, color=AMBER),
            MathTex(r"\mathbf{t \approx 1566.65\text{ years}}", font_size=21, color=GREEN)
        ).arrange(DOWN, buff=0.18).move_to(d_box.get_center())

        self.play(Create(d_box), Write(d_text), run_time=1.2)
        self.wait(2.0)


# =============================================================================
# SCENE 9: Radioactive Decay Problem 2 - 90% Dissipation (Mathalino 02)
# =============================================================================
class Scene09_DecayProblem2_90Percent(Scene):
    def construct(self):
        title = Text("Mathalino Decay 02: 90% Radioactivity Dissipation", font_size=27, color=TEXT_WHITE, weight=BOLD)
        subtitle = Text("Given: Half-life t₁/₂ = 38 hours. Find time for 90% to dissipate (10% remaining).", font_size=15, color=CYAN)
        banner = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_corner(UL, buff=0.4)
        self.play(FadeIn(banner), run_time=0.8)

        # Coordinate axes
        axes = Axes(
            x_range=[0, 150, 25], y_range=[0, 1.1, 0.2],
            x_length=7.4, y_length=3.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2}
        ).to_corner(DR, buff=0.6).shift(UP * 0.1)

        x_lbl = Text("Time t (hours)", font_size=13, color=MUTED_GRAY).next_to(axes.x_axis.get_end(), DOWN, buff=0.18).shift(LEFT * 0.5)
        y_lbl = Text("Remaining Fraction x / x₀", font_size=13, color=MUTED_GRAY).next_to(axes.y_axis.get_top(), UP, buff=0.1)

        x_ticks = VGroup(*[Text(str(i), font_size=11, color=MUTED_GRAY).next_to(axes.c2p(i, 0), DOWN, buff=0.1) for i in [25, 50, 75, 100, 125, 150]])
        y_ticks = VGroup(*[Text(f"{j:.1f}", font_size=11, color=MUTED_GRAY).next_to(axes.c2p(0, j), LEFT, buff=0.1) for j in [0.2, 0.4, 0.6, 0.8, 1.0]])

        # 50% line & 10% line
        h_line = DashedLine(axes.c2p(0, 0.5), axes.c2p(140, 0.5), color=GREEN, stroke_width=1.8, dash_length=0.1)
        h_tag = MathTex(r"0.50\,x_0\text{ (50\% Half-Life)}", font_size=13, color=GREEN).next_to(axes.c2p(38, 0.5), UP, buff=0.06)

        d_line = DashedLine(axes.c2p(0, 0.1), axes.c2p(140, 0.1), color=AMBER, stroke_width=1.8, dash_length=0.08)
        d_tag = MathTex(r"0.10\,x_0\text{ (90\% Dissipated Target)}", font_size=13, color=AMBER).next_to(axes.c2p(80, 0.1), UP, buff=0.06)

        def dec_func(t):
            return 0.5 ** (t / 38.0)

        curve = axes.plot(dec_func, x_range=[0, 126.23], color=CYAN, stroke_width=3.5)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), FadeIn(x_ticks), FadeIn(y_ticks), Create(h_line), FadeIn(h_tag), Create(d_line), FadeIn(d_tag), run_time=1.0)
        self.play(Create(curve), run_time=2.5, rate_func=linear)

        p0 = Dot(axes.c2p(0, 1.0), color=WHITE, radius=0.06)
        l0 = MathTex(r"(0, 1.0x_0)", font_size=14, color=WHITE).next_to(p0, UR, buff=0.08)
        ph = Dot(axes.c2p(38, 0.5), color=GREEN, radius=0.07)
        lh = MathTex(r"(38\text{ hr},\, 0.5x_0)", font_size=14, color=GREEN).next_to(ph, UR, buff=0.08)
        pt = Dot(axes.c2p(126.23, 0.1), color=AMBER, radius=0.09)
        lt = MathTex(r"(126.23\text{ hr},\, 0.1x_0)", font_size=15, color=AMBER).next_to(pt, UR, buff=0.1)

        self.play(FadeIn(p0), Write(l0), FadeIn(ph), Write(lh), FadeIn(pt), Write(lt), run_time=0.9)

        # Derivation Box (Left)
        d_box = RoundedRectangle(corner_radius=0.18, height=3.6, width=4.6, stroke_color=AMBER, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.95).move_to([-4.0, -0.6, 0])
        d_text = VGroup(
            MathTex(r"x(t) = x_0 (0.5)^{t/38}", font_size=18, color=TEXT_WHITE),
            MathTex(r"0.10 x_0 = x_0 (0.5)^{t/38}", font_size=18, color=TEXT_WHITE),
            MathTex(r"0.10 = 0.5^{t/38} \implies 0.1^{38} = 0.5^t", font_size=17, color=CYAN),
            MathTex(r"t = \frac{38\ln 0.10}{\ln 0.50}", font_size=20, color=AMBER),
            MathTex(r"\mathbf{t \approx 126.23\text{ hours}}", font_size=21, color=GREEN)
        ).arrange(DOWN, buff=0.18).move_to(d_box.get_center())

        self.play(Create(d_box), Write(d_text), run_time=1.2)
        self.wait(2.0)


# =============================================================================
# SCENE 10: Engineering Physics Extension - Velocity of Escape from Earth
# =============================================================================
class Scene10_EscapeVelocity(Scene):
    def construct(self):
        title = Text("Engineering Physics: Velocity of Escape from Earth", font_size=27, color=TEXT_WHITE, weight=BOLD)
        subtitle = Text("Primary Mathalino Index Topic // Inverse-Square Gravity Differential Equation", font_size=15, color=CYAN)
        banner = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_corner(UL, buff=0.4)
        self.play(FadeIn(banner), run_time=0.8)

        # Left: Planet Earth Graphic & Escape Rocket
        earth = Circle(radius=1.2, stroke_color=CYAN, stroke_width=2.5, fill_color="#0369A1", fill_opacity=0.5).move_to([-4.2, -0.8, 0])
        earth_tag = Text("Earth (Radius R)", font_size=13, color=CYAN, weight=BOLD).move_to(earth.get_center())
        
        trajectory = DashedLine(earth.get_top(), earth.get_top() + UP * 2.8, color=AMBER, stroke_width=2.5, dash_length=0.12)
        rocket = Triangle(fill_color=AMBER, fill_opacity=1.0, stroke_width=0).scale(0.18).move_to(earth.get_top() + UP * 0.1)

        self.play(FadeIn(earth), Write(earth_tag), Create(trajectory), FadeIn(rocket), run_time=1.0)
        self.play(rocket.animate.shift(UP * 2.2), run_time=2.0, rate_func=smooth)

        # Right: Separation of Variables & Derivation
        r_box = RoundedRectangle(corner_radius=0.18, height=4.2, width=6.8, stroke_color=CYAN, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.95).move_to([2.6, -0.6, 0])
        r_text = VGroup(
            MathTex(r"a = v\frac{dv}{dr} = -\frac{g R^2}{r^2}", font_size=21, color=TEXT_WHITE),
            MathTex(r"v\,dv = -g R^2 r^{-2}dr", font_size=21, color=CYAN),
            MathTex(r"\int v\,dv = -g R^2 \int r^{-2}dr \implies \frac{1}{2}v^2 = \frac{g R^2}{r} + C", font_size=19, color=TEXT_WHITE),
            MathTex(r"\text{At } r = \infty,\, v \ge 0 \implies C \ge 0", font_size=19, color=AMBER),
            MathTex(r"\text{Minimum escape speed at surface } (r = R):", font_size=18, color=MUTED_GRAY),
            MathTex(r"v_{esc} = \sqrt{2gR} \approx \mathbf{11.18~\text{km/s}}~(6.95~\text{mi/s})", font_size=21, color=GREEN)
        ).arrange(DOWN, buff=0.18).move_to(r_box.get_center())

        self.play(Create(r_box), Write(r_text), run_time=1.8)
        self.wait(2.0)


# =============================================================================
# SCENE 11: Master Synthesis & Comparative Modeling Chart
# =============================================================================
class Scene11_SynthesisComparison(Scene):
    def construct(self):
        title = Text("Comparative Modeling Matrix: 3 Core Applications", font_size=28, color=TEXT_WHITE, weight=BOLD).to_edge(UP, buff=0.4)
        subtitle = Text("Common Differential Architecture Across Engineering & Physical Sciences", font_size=16, color=CYAN).next_to(title, DOWN, buff=0.1)
        self.play(FadeIn(title), FadeIn(subtitle), run_time=0.8)

        # 3 Side-by-Side Application Columns
        cols_data = [
            ("Newton's Cooling", r"\frac{dT}{dt} = -k(T - T_s)", r"T(t) = T_s + (T_0 - T_s)e^{-kt}", "Thermal Equilibrium", CYAN),
            ("Radioactive Decay", r"\frac{dx}{dt} = -kx", r"x(t) = x_0\,e^{-kt}", "Half-Life Threshold", GREEN),
            ("Escape Velocity", r"v\frac{dv}{dr} = -\frac{g R^2}{r^2}", r"v = \sqrt{2gR^2 / r}", "Gravitational Escape", AMBER)
        ]

        col_group = VGroup()
        for name, de_str, sol_str, key_phys, col in cols_data:
            box = RoundedRectangle(corner_radius=0.18, height=4.2, width=3.8, stroke_color=col, stroke_width=2, fill_color=CARD_BG, fill_opacity=0.9)
            h = Text(name, font_size=17, color=col, weight=BOLD).next_to(box.get_top(), DOWN, buff=0.25)
            de_l = Text("Governing DE:", font_size=12, color=MUTED_GRAY).next_to(h, DOWN, buff=0.25, aligned_edge=LEFT)
            de_m = MathTex(de_str, font_size=18, color=TEXT_WHITE).next_to(de_l, DOWN, buff=0.12)
            sol_l = Text("General Solution:", font_size=12, color=MUTED_GRAY).next_to(de_m, DOWN, buff=0.25, aligned_edge=LEFT)
            sol_m = MathTex(sol_str, font_size=17, color=col).next_to(sol_l, DOWN, buff=0.12)
            phys_l = Text("Key Physics:", font_size=12, color=MUTED_GRAY).next_to(sol_m, DOWN, buff=0.25, aligned_edge=LEFT)
            phys_m = Text(key_phys, font_size=13, color=TEXT_WHITE, weight=BOLD).next_to(phys_l, DOWN, buff=0.1)

            card = VGroup(box, h, de_l, de_m, sol_l, sol_m, phys_l, phys_m)
            col_group.add(card)

        col_group.arrange(RIGHT, buff=0.4).shift(DOWN * 0.25)

        for c in col_group:
            self.play(FadeIn(c, shift=UP * 0.2), run_time=0.8)
            self.wait(0.3)

        self.wait(2.0)
