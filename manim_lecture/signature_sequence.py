from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(__file__))
from common_theme import *


# -------------------------------------------------------------
# SIGNATURE SCENE 1: THE FUNCTION & MOVING POINT
# -------------------------------------------------------------
class SignatureScene1_TheFunction(Scene):
    def construct(self):
        header = create_header("The Cubic Function Landscape", "Tracing vertical displacement and turning behavior along f(x) = x³ - 3x", CYAN)
        self.play(Write(header), run_time=1.0)

        # Coordinate System
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=8.0,
            y_length=5.0,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": True, "font_size": 18},
            tips=True,
        ).shift(DOWN * 0.45)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN, buff=0.2)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT, buff=0.2)
        axes_group = VGroup(axes, x_label, y_label)

        def f(x): return x**3 - 3*x

        curve = axes.plot(f, x_range=[-2.15, 2.15], color=CYAN, stroke_width=4)
        curve_label = MathTex(r"f(x) = x^3 - 3x", color=CYAN, font_size=28).to_corner(UL, buff=1.2)

        self.play(Create(axes_group), run_time=1.2)
        self.play(Create(curve), Write(curve_label), run_time=1.8)

        # ValueTracker & Moving Point
        x_tracker = ValueTracker(-2.05)
        dot = always_redraw(lambda: Dot(
            axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
            color=AMBER, radius=0.09
        ))

        # Vertical tracking line
        v_line = always_redraw(lambda: DashedLine(
            start=axes.c2p(x_tracker.get_value(), 0),
            end=axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
            color=MUTED_GRAY, stroke_width=1.5
        ))

        # Coordinate readout
        coord_readout = always_redraw(lambda: MathTex(
            f"({x_tracker.get_value():.2f}, {f(x_tracker.get_value()):.2f})",
            font_size=22, color=TEXT_WHITE
        ).next_to(dot, UP if f(x_tracker.get_value()) >= 0 else DOWN, buff=0.2))

        self.play(FadeIn(dot), Create(v_line), FadeIn(coord_readout))
        self.wait(0.5)

        # Animate along curve
        # Phase 1: Ascent to peak
        self.play(x_tracker.animate.set_value(-1.0), run_time=2.5, rate_func=smooth)
        self.wait(0.8)

        # Phase 2: Descent into trough
        self.play(x_tracker.animate.set_value(1.0), run_time=3.0, rate_func=smooth)
        self.wait(0.8)

        # Phase 3: Final ascent
        self.play(x_tracker.animate.set_value(2.05), run_time=2.2, rate_func=smooth)
        self.wait(1.5)


# -------------------------------------------------------------
# SIGNATURE SCENE 2: THE DYNAMIC TANGENT LINE
# -------------------------------------------------------------
class SignatureScene2_TheTangent(Scene):
    def construct(self):
        header = create_header("Dynamic Tangent & Instantaneous Slope", "Vanishing rate of change at turning points: f'(x) = 0", AMBER)
        self.play(Write(header), run_time=1.0)

        # Coordinate System
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=7.2,
            y_length=4.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": True, "font_size": 18},
            tips=True,
        ).shift(DOWN * 0.45 + LEFT * 1.6)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN, buff=0.2)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT, buff=0.2)

        def f(x): return x**3 - 3*x
        def f_prime(x): return 3*x**2 - 3

        curve = axes.plot(f, x_range=[-2.15, 2.15], color=CYAN, stroke_width=4)
        curve_label = MathTex(r"f(x) = x^3 - 3x", color=CYAN, font_size=24).next_to(axes, UP, buff=0.15).shift(LEFT * 1.5)

        self.play(Create(axes), Create(x_label), Create(y_label), Create(curve), Write(curve_label), run_time=1.2)

        # ValueTracker & Tangent
        x_tracker = ValueTracker(-2.05)
        dot = always_redraw(lambda: Dot(
            axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
            color=AMBER, radius=0.08
        ))

        def get_tangent_line():
            x0 = x_tracker.get_value()
            y0 = f(x0)
            m = f_prime(x0)
            length = 0.85
            dx = length / np.sqrt(1 + m**2)
            dy = m * dx
            p1 = axes.c2p(x0 - dx, y0 - dy)
            p2 = axes.c2p(x0 + dx, y0 + dy)
            color = AMBER if abs(m) < 0.2 else (CYAN if m > 0 else CORAL)
            return Line(p1, p2, color=color, stroke_width=3.5)

        tangent_line = always_redraw(get_tangent_line)

        # Right Telemetry Card
        panel = create_telemetry_card(width=4.0, height=4.8).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.45)
        panel_title = Text("Real-Time Telemetry", font_size=20, color=CYAN).move_to(panel.get_top() + DOWN * 0.4)

        pos_readout = always_redraw(lambda: MathTex(
            r"x = " + f"{x_tracker.get_value():.2f}", font_size=24, color=TEXT_WHITE
        ).next_to(panel_title, DOWN, buff=0.4))

        slope_readout = always_redraw(lambda: MathTex(
            r"f'(x) = " + f"{f_prime(x_tracker.get_value()):+.2f}", font_size=26,
            color=AMBER if abs(f_prime(x_tracker.get_value())) < 0.2 else (CYAN if f_prime(x_tracker.get_value()) > 0 else CORAL)
        ).next_to(pos_readout, DOWN, buff=0.3))

        status_readout = always_redraw(lambda: Text(
            "TURNING POINT (Peak)" if abs(x_tracker.get_value() + 1.0) < 0.08 else
            ("TURNING POINT (Trough)" if abs(x_tracker.get_value() - 1.0) < 0.08 else
             ("Ascending (f' > 0)" if f_prime(x_tracker.get_value()) > 0 else "Descending (f' < 0)")),
            font_size=16,
            color=AMBER if abs(f_prime(x_tracker.get_value())) < 0.2 else (CYAN if f_prime(x_tracker.get_value()) > 0 else CORAL)
        ).next_to(slope_readout, DOWN, buff=0.3))

        self.play(FadeIn(panel), Write(panel_title), FadeIn(dot), Create(tangent_line),
                  FadeIn(pos_readout), FadeIn(slope_readout), FadeIn(status_readout))
        self.wait(0.5)

        # Move to Local Max
        self.play(x_tracker.animate.set_value(-1.0), run_time=2.8, rate_func=smooth)
        dot_max = Dot(axes.c2p(-1.0, 2.0), color=AMBER, radius=0.11)
        max_box = VGroup(
            MathTex(r"\text{Local Max } (-1, 2)", font_size=21, color=AMBER),
            MathTex(r"f'(-1) = 0", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.08).next_to(axes.c2p(-1.0, 2.0), UP + LEFT * 0.8, buff=0.15)
        self.play(FadeIn(dot_max), FadeIn(max_box), run_time=0.8)
        self.wait(1.2)

        # Move to Local Min
        self.play(x_tracker.animate.set_value(1.0), run_time=3.0, rate_func=smooth)
        dot_min = Dot(axes.c2p(1.0, -2.0), color=CYAN, radius=0.11)
        min_box = VGroup(
            MathTex(r"\text{Local Min } (1, -2)", font_size=21, color=CYAN),
            MathTex(r"f'(1) = 0", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.08).next_to(axes.c2p(1.0, -2.0), DOWN + RIGHT * 0.8, buff=0.15)
        self.play(FadeIn(dot_min), FadeIn(min_box), run_time=0.8)
        self.wait(1.2)

        # Outro
        self.play(x_tracker.animate.set_value(2.05), run_time=2.2, rate_func=smooth)
        self.wait(1.5)


# -------------------------------------------------------------
# SIGNATURE SCENE 3: EQUATION MORPHING (TransformMatchingTex)
# -------------------------------------------------------------
class SignatureScene3_EquationMorph(Scene):
    def construct(self):
        header = create_header("Algebraic Factoring & Critical Roots", "Factoring f'(x) to isolate critical numbers x = -1 and x = +1", AMBER)
        self.play(Write(header), run_time=1.0)

        # Left Graph
        axes = Axes(
            x_range=[-2.4, 2.4, 1],
            y_range=[-3.2, 3.2, 1],
            x_length=5.6,
            y_length=4.4,
            axis_config={"color": AXES_GRAY, "stroke_width": 1.5, "include_numbers": True, "font_size": 17},
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        def f(x): return x**3 - 3*x
        curve = axes.plot(f, x_range=[-2.15, 2.15], color=CYAN, stroke_width=3.5)
        curve_label = MathTex(r"f(x) = x^3 - 3x", color=CYAN, font_size=24).next_to(axes, UP, buff=0.15)

        pt_max = Dot(axes.c2p(-1, 2), color=AMBER, radius=0.09)
        pt_min = Dot(axes.c2p(1, -2), color=CYAN, radius=0.09)

        self.play(Create(axes), Create(curve), Write(curve_label), FadeIn(pt_max), FadeIn(pt_min), run_time=1.2)

        # Right Card: TransformMatchingTex stages
        box = create_telemetry_card(width=6.6, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        step_title = Text("Algebraic Factorization", font_size=20, color=AMBER).move_to(box.get_top() + DOWN * 0.45)
        self.play(FadeIn(box), Write(step_title))

        eq1 = MathTex(r"f'(x)", r"=", r"3x^2", r"-", r"3", font_size=32, color=TEXT_WHITE).next_to(step_title, DOWN, buff=0.45)
        self.play(Write(eq1), run_time=0.9)
        self.wait(0.8)

        eq2 = MathTex(r"f'(x)", r"=", r"3", r"(x^2 - 1)", font_size=32, color=TEXT_WHITE).move_to(eq1)
        self.play(TransformMatchingTex(eq1, eq2), run_time=1.0)
        self.wait(0.8)

        eq3 = MathTex(r"f'(x)", r"=", r"3", r"(x - 1)", r"(x + 1)", font_size=32, color=CYAN).move_to(eq2)
        self.play(TransformMatchingTex(eq2, eq3), run_time=1.0)
        self.wait(0.8)

        eq4 = MathTex(
            r"f'(x) = 0", r"\implies", r"x = -1", r"\text{ or }", r"x = +1",
            font_size=29, color=AMBER
        ).next_to(eq3, DOWN, buff=0.5)
        self.play(Write(eq4), run_time=1.0)
        self.wait(0.8)

        # Drop lines to x-axis
        drop_neg1 = DashedLine(axes.c2p(-1, 2), axes.c2p(-1, 0), color=AMBER, stroke_width=2.5, dash_length=0.08)
        drop_pos1 = DashedLine(axes.c2p(1, -2), axes.c2p(1, 0), color=CYAN, stroke_width=2.5, dash_length=0.08)

        self.play(Create(drop_neg1), Flash(pt_max, color=AMBER), run_time=0.9)
        self.play(Create(drop_pos1), Flash(pt_min, color=CYAN), run_time=0.9)

        verdict_card = VGroup(
            Text("Zeros of f'(x) align with horizontal tangents:", font_size=15, color=MUTED_GRAY),
            MathTex(r"x_1 = -1 \quad (\text{Peak}), \quad x_2 = +1 \quad (\text{Trough})", font_size=20, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.15).next_to(eq4, DOWN, buff=0.45)

        self.play(FadeIn(verdict_card))
        self.wait(2.0)


# -------------------------------------------------------------
# SIGNATURE SCENE 4: FIRST DERIVATIVE TEST SIGN CHART
# -------------------------------------------------------------
class SignatureScene4_DerivativeTest(Scene):
    def construct(self):
        header = create_header("The First Derivative Test", "Evaluating sign changes across critical partitions", CYAN)
        self.play(Write(header), run_time=1.0)

        num_line = NumberLine(
            x_range=[-3, 3, 1], length=10.0, color=AXES_GRAY, include_numbers=False, stroke_width=3
        ).shift(UP * 0.9)

        tick_neg1 = num_line.n2p(-1)
        tick_pos1 = num_line.n2p(1)

        dot_neg1 = Dot(tick_neg1, color=AMBER, radius=0.1)
        dot_pos1 = Dot(tick_pos1, color=CYAN, radius=0.1)

        label_neg1 = MathTex(r"x = -1", font_size=24, color=AMBER).next_to(dot_neg1, DOWN, buff=0.2)
        label_pos1 = MathTex(r"x = +1", font_size=24, color=CYAN).next_to(dot_pos1, DOWN, buff=0.2)
        fprime_zero1 = MathTex(r"f'=0", font_size=18, color=MUTED_GRAY).next_to(label_neg1, DOWN, buff=0.1)
        fprime_zero2 = MathTex(r"f'=0", font_size=18, color=MUTED_GRAY).next_to(label_pos1, DOWN, buff=0.1)

        self.play(Create(num_line), FadeIn(dot_neg1), FadeIn(dot_pos1),
                  Write(label_neg1), Write(label_pos1), Write(fprime_zero1), Write(fprime_zero2), run_time=1.2)

        # Interval 1: x < -1
        region1 = Line(num_line.n2p(-3), num_line.n2p(-1), color=CYAN, stroke_width=6)
        center1 = num_line.n2p(-2.0)
        sign1 = MathTex(r"+", font_size=48, color=CYAN).move_to(center1 + UP * 0.45)
        arrow1 = MathTex(r"\nearrow", font_size=32, color=CYAN).next_to(sign1, UP, buff=0.12)
        test1 = Text("x = -2: f' = +9 > 0", font_size=15, color=MUTED_GRAY).move_to(center1 + DOWN * 0.8)
        self.play(Create(region1), FadeIn(sign1), FadeIn(arrow1), Write(test1), run_time=1.0)

        # Interval 2: -1 < x < 1
        region2 = Line(num_line.n2p(-1), num_line.n2p(1), color=CORAL, stroke_width=6)
        center2 = num_line.n2p(0.0)
        sign2 = MathTex(r"-", font_size=48, color=CORAL).move_to(center2 + UP * 0.45)
        arrow2 = MathTex(r"\searrow", font_size=32, color=CORAL).next_to(sign2, UP, buff=0.12)
        test2 = Text("x = 0: f' = -3 < 0", font_size=15, color=MUTED_GRAY).move_to(center2 + DOWN * 0.8)
        self.play(Create(region2), FadeIn(sign2), FadeIn(arrow2), Write(test2), run_time=1.0)

        # Interval 3: x > 1
        region3 = Line(num_line.n2p(1), num_line.n2p(3), color=CYAN, stroke_width=6)
        center3 = num_line.n2p(2.0)
        sign3 = MathTex(r"+", font_size=48, color=CYAN).move_to(center3 + UP * 0.45)
        arrow3 = MathTex(r"\nearrow", font_size=32, color=CYAN).next_to(sign3, UP, buff=0.12)
        test3 = Text("x = +2: f' = +9 > 0", font_size=15, color=MUTED_GRAY).move_to(center3 + DOWN * 0.8)
        self.play(Create(region3), FadeIn(sign3), FadeIn(arrow3), Write(test3), run_time=1.0)
        self.wait(0.8)

        # Verdict Cards
        card_max = RoundedRectangle(corner_radius=0.15, width=5.2, height=1.7, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=AMBER, stroke_width=2).shift(DOWN * 2.3 + LEFT * 3.1)
        card_max_text = VGroup(
            Text("Sign shifts: (+) to (-)", font_size=16, color=MUTED_GRAY),
            Text("LOCAL MAXIMUM", font_size=20, color=AMBER, weight=BOLD),
            MathTex(r"f(-1) = 2 \implies \mathbf{(-1, 2)}", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.12).move_to(card_max)

        card_min = RoundedRectangle(corner_radius=0.15, width=5.2, height=1.7, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=CYAN, stroke_width=2).shift(DOWN * 2.3 + RIGHT * 3.1)
        card_min_text = VGroup(
            Text("Sign shifts: (-) to (+)", font_size=16, color=MUTED_GRAY),
            Text("LOCAL MINIMUM", font_size=20, color=CYAN, weight=BOLD),
            MathTex(r"f(1) = -2 \implies \mathbf{(1, -2)}", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.12).move_to(card_min)

        self.play(FadeIn(card_max), Write(card_max_text), FadeIn(card_min), Write(card_min_text), run_time=1.2)
        self.wait(2.0)


# -------------------------------------------------------------
# SIGNATURE SCENE 5: THE EXTREMA REVEAL & COORDINATES
# -------------------------------------------------------------
class SignatureScene5_ExtremaReveal(Scene):
    def construct(self):
        header = create_header("Extrema Coordinates & Verification", "Evaluating original function f(x) to anchor extrema heights", CYAN)
        self.play(Write(header), run_time=1.0)

        # Full Dual-Graph Display
        axes = Axes(
            x_range=[-2.4, 2.4, 1],
            y_range=[-3.2, 3.2, 1],
            x_length=7.0,
            y_length=4.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": True, "font_size": 18},
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        def f(x): return x**3 - 3*x
        curve = axes.plot(f, x_range=[-2.15, 2.15], color=CYAN, stroke_width=4)

        # Horizontal Tangent lines at peaks
        tan_max = Line(axes.c2p(-1.6, 2.0), axes.c2p(-0.4, 2.0), color=AMBER, stroke_width=3)
        tan_min = Line(axes.c2p(0.4, -2.0), axes.c2p(1.6, -2.0), color=CYAN, stroke_width=3)

        dot_max = Dot(axes.c2p(-1, 2), color=AMBER, radius=0.11)
        dot_min = Dot(axes.c2p(1, -2), color=CYAN, radius=0.11)

        self.play(Create(axes), Create(curve), FadeIn(dot_max), FadeIn(dot_min),
                  Create(tan_max), Create(tan_min), run_time=1.5)

        # Right Card: Full Evaluation
        panel = create_telemetry_card(width=5.2, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        panel_title = Text("Exact Altitude Evaluation", font_size=20, color=CYAN).move_to(panel.get_top() + DOWN * 0.45)
        self.play(FadeIn(panel), Write(panel_title))

        calc_max = VGroup(
            Text("1. Local Maximum Coordinate:", font_size=16, color=AMBER, weight=BOLD),
            MathTex(r"f(-1) = (-1)^3 - 3(-1)", font_size=20, color=TEXT_WHITE),
            MathTex(r"= -1 + 3 = \mathbf{+2}", font_size=20, color=AMBER),
            MathTex(r"\implies \text{Point } \mathbf{(-1, 2)}", font_size=22, color=AMBER)
        ).arrange(DOWN, buff=0.15).next_to(panel_title, DOWN, buff=0.35)

        calc_min = VGroup(
            Text("2. Local Minimum Coordinate:", font_size=16, color=CYAN, weight=BOLD),
            MathTex(r"f(1) = (1)^3 - 3(1)", font_size=20, color=TEXT_WHITE),
            MathTex(r"= 1 - 3 = \mathbf{-2}", font_size=20, color=CYAN),
            MathTex(r"\implies \text{Point } \mathbf{(1, -2)}", font_size=22, color=CYAN)
        ).arrange(DOWN, buff=0.15).next_to(calc_max, DOWN, buff=0.35)

        self.play(Write(calc_max), Flash(dot_max, color=AMBER), run_time=1.5)
        self.wait(0.8)
        self.play(Write(calc_min), Flash(dot_min, color=CYAN), run_time=1.5)
        self.wait(2.0)


# -------------------------------------------------------------
# SIGNATURE SCENE 6: SECOND DERIVATIVE TEST & CONCAVITY
# -------------------------------------------------------------
class SignatureScene6_SecondDerivative(Scene):
    def construct(self):
        header = create_header("Second Derivative & Concavity Bending", "Bending rate of change f''(x) = 6x verifies extrema", AMBER)
        self.play(Write(header), run_time=1.0)

        # Transformation of Equation: f'(x) -> f''(x)
        eq_deriv1 = MathTex(r"f'(x)", r"=", r"3x^2 - 3", font_size=32, color=TEXT_WHITE).to_edge(UP, buff=1.4)
        eq_deriv2 = MathTex(r"f''(x)", r"=", r"\frac{d}{dx}[3x^2 - 3]", font_size=32, color=AMBER).move_to(eq_deriv1)
        eq_deriv3 = MathTex(r"f''(x)", r"=", r"6x", font_size=34, color=AMBER).move_to(eq_deriv2)

        self.play(Write(eq_deriv1), run_time=0.9)
        self.wait(0.6)
        self.play(TransformMatchingTex(eq_deriv1, eq_deriv2), run_time=1.0)
        self.wait(0.6)
        self.play(TransformMatchingTex(eq_deriv2, eq_deriv3), run_time=1.0)
        self.wait(1.0)

        # Dual Concavity Containers
        card_down = RoundedRectangle(corner_radius=0.2, width=5.8, height=3.8, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=AMBER, stroke_width=2).shift(DOWN * 1.5 + LEFT * 3.3)
        card_up = RoundedRectangle(corner_radius=0.2, width=5.8, height=3.8, fill_color=CARD_BG, fill_opacity=0.9, stroke_color=CYAN, stroke_width=2).shift(DOWN * 1.5 + RIGHT * 3.3)

        # Concave Down content
        bowl_down = Arc(radius=0.75, start_angle=0, angle=PI, color=AMBER, stroke_width=3.5).move_to(card_down.get_top() + DOWN * 0.85)
        dot_d = Dot(bowl_down.get_top(), color=AMBER, radius=0.09)
        content_down = VGroup(
            Text("CONCAVE DOWN (∩)", font_size=19, color=AMBER, weight=BOLD),
            MathTex(r"f''(-1) = 6(-1) = -6 < 0", font_size=19, color=TEXT_WHITE),
            Text("Slopes decreasing: Traps a", font_size=14, color=MUTED_GRAY),
            Text("LOCAL MAXIMUM", font_size=21, color=AMBER, weight=BOLD)
        ).arrange(DOWN, buff=0.10).next_to(bowl_down, DOWN, buff=0.3)

        # Concave Up content
        bowl_up = Arc(radius=0.75, start_angle=PI, angle=PI, color=CYAN, stroke_width=3.5).move_to(card_up.get_top() + DOWN * 0.85)
        dot_u = Dot(bowl_up.get_bottom(), color=CYAN, radius=0.09)
        content_up = VGroup(
            Text("CONCAVE UP (∪)", font_size=19, color=CYAN, weight=BOLD),
            MathTex(r"f''(1) = 6(1) = +6 > 0", font_size=19, color=TEXT_WHITE),
            Text("Slopes increasing: Holds a", font_size=14, color=MUTED_GRAY),
            Text("LOCAL MINIMUM", font_size=21, color=CYAN, weight=BOLD)
        ).arrange(DOWN, buff=0.10).next_to(bowl_up, DOWN, buff=0.3)

        self.play(FadeIn(card_down), Create(bowl_down), FadeIn(dot_d), Write(content_down), run_time=1.2)
        self.play(FadeIn(card_up), Create(bowl_up), FadeIn(dot_u), Write(content_up), run_time=1.2)
        self.wait(2.0)


# -------------------------------------------------------------
# SIGNATURE SCENE 7: THE COUNTEREXAMPLE (g(x) = x³)
# -------------------------------------------------------------
class SignatureScene7_Counterexample(Scene):
    def construct(self):
        header = create_header("Inflection Terrace Counterexample", "g'(0) = 0 without an extremum: The stationary inflection trap", CORAL)
        self.play(Write(header), run_time=1.0)

        # Coordinate axes
        axes = Axes(
            x_range=[-2.2, 2.2, 1],
            y_range=[-3.0, 3.0, 1],
            x_length=6.4,
            y_length=4.6,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": True, "font_size": 18},
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        def g(x): return x**3
        curve = axes.plot(g, x_range=[-1.42, 1.42], color=CYAN, stroke_width=4)
        curve_label = MathTex(r"g(x) = x^3", color=CYAN, font_size=28).next_to(axes.c2p(1.2, g(1.2)), RIGHT, buff=0.2)

        # Horizontal tangent at origin
        tan_zero = Line(axes.c2p(-1.0, 0), axes.c2p(1.0, 0), color=AMBER, stroke_width=3.5)
        dot_origin = Dot(axes.c2p(0, 0), color=AMBER, radius=0.11)

        self.play(Create(axes), Create(curve), Write(curve_label), FadeIn(dot_origin), Create(tan_zero), run_time=1.4)

        # Right Analysis Card
        panel = create_telemetry_card(width=5.4, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        panel_title = Text("Critical Analysis of g(x) = x³", font_size=20, color=CORAL).move_to(panel.get_top() + DOWN * 0.4)
        self.play(FadeIn(panel), Write(panel_title))

        steps = VGroup(
            MathTex(r"g'(x) = 3x^2", font_size=24, color=TEXT_WHITE),
            MathTex(r"g'(0) = 3(0)^2 = 0 \quad (\text{Horizontal})", font_size=22, color=AMBER),
            Text("Examine neighborhood slopes:", font_size=16, color=MUTED_GRAY),
            MathTex(r"x < 0 \implies g'(x) = 3x^2 > 0 \quad (\nearrow)", font_size=20, color=CYAN),
            MathTex(r"x > 0 \implies g'(x) = 3x^2 > 0 \quad (\nearrow)", font_size=20, color=CYAN),
            Text("NO SIGN CHANGE across x = 0!", font_size=18, color=CORAL, weight=BOLD),
            Text("Origin is a STATIONARY INFLECTION point.", font_size=16, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.15).next_to(panel_title, DOWN, buff=0.25)

        for step in steps:
            self.play(Write(step), run_time=0.6)
            self.wait(0.2)

        self.play(Flash(dot_origin, color=CORAL, flash_radius=0.4), run_time=0.8)
        self.wait(2.0)


# -------------------------------------------------------------
# UNIFIED MASTER SEQUENCE: SEAMLESS 3BLUE1BROWN TRANSFORMATION
# -------------------------------------------------------------
class SignatureSequenceMaster(Scene):
    def construct(self):
        # 1. Coordinate plane & Curve f(x) = x³ - 3x
        header = create_header("The Cubic Function: Complete Calculus Flow", "f(x) = x³ - 3x: Continuous Kinematic Derivation", CYAN)
        self.play(Write(header), run_time=0.8)

        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=6.0,
            y_length=4.4,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": True, "font_size": 17},
            tips=True,
        ).to_edge(LEFT, buff=0.7).shift(DOWN * 0.45)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN, buff=0.2)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT, buff=0.2)
        axes_group = VGroup(axes, x_label, y_label)

        def f(x): return x**3 - 3*x
        curve = axes.plot(f, x_range=[-2.15, 2.15], color=CYAN, stroke_width=3.5)
        curve_label = MathTex(r"f(x) = x^3 - 3x", color=CYAN, font_size=24).next_to(axes, UP, buff=0.15)

        self.play(Create(axes_group), Create(curve), Write(curve_label), run_time=1.2)

        # 2. Moving Point & Tangent Line
        x_tracker = ValueTracker(-2.0)
        dot = always_redraw(lambda: Dot(
            axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
            color=AMBER, radius=0.09
        ))

        def get_slope():
            x = x_tracker.get_value()
            return 3 * x**2 - 3

        def get_tangent_line():
            x = x_tracker.get_value()
            m = 3 * x**2 - 3
            p = axes.c2p(x, f(x))
            angle = np.arctan(m * (axes.y_length / 7.0) / (axes.x_length / 5.0))
            color = AMBER if abs(m) < 0.2 else (CYAN if m > 0 else CORAL)
            return Line(p - 1.2 * np.array([np.cos(angle), np.sin(angle), 0]),
                        p + 1.2 * np.array([np.cos(angle), np.sin(angle), 0]),
                        color=color, stroke_width=3.5)

        tangent_line = always_redraw(get_tangent_line)

        # Telemetry Card on Right
        side_panel = create_telemetry_card(width=6.0, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        panel_title = Text("Instantaneous Derivative Telemetry", font_size=19, color=CYAN).move_to(side_panel.get_top() + DOWN * 0.4)
        
        telemetry_display = always_redraw(lambda: VGroup(
            Text(f"x = {x_tracker.get_value():.2f}", font_size=20, color=TEXT_WHITE),
            Text(f"y = f(x) = {f(x_tracker.get_value()):.2f}", font_size=20, color=TEXT_WHITE),
            Text(f"m = f'(x) = {get_slope():.2f}", font_size=24, 
                 color=AMBER if abs(get_slope()) < 0.2 else (CYAN if get_slope() > 0 else CORAL)),
            Text("Stationary Peak f'(-1) = 0" if abs(x_tracker.get_value() - (-1)) < 0.15 else 
                 ("Stationary Valley f'(1) = 0" if abs(x_tracker.get_value() - 1) < 0.15 else
                  ("Steepest Descent f'(0) = -3" if abs(x_tracker.get_value()) < 0.15 else 
                   ("Climbing f'(x) > 0" if get_slope() > 0 else "Falling f'(x) < 0"))),
                 font_size=16, color=AMBER if abs(get_slope()) < 0.2 else TEXT_WHITE)
        ).arrange(DOWN, buff=0.25).next_to(panel_title, DOWN, buff=0.4))

        self.play(FadeIn(dot), FadeIn(tangent_line), FadeIn(side_panel), Write(panel_title), FadeIn(telemetry_display), run_time=1.0)

        # Animate probe across turning points
        self.play(x_tracker.animate.set_value(-1.0), run_time=1.8, rate_func=smooth)
        self.wait(0.5)
        self.play(x_tracker.animate.set_value(0.0), run_time=1.2, rate_func=smooth)
        self.wait(0.3)
        self.play(x_tracker.animate.set_value(1.0), run_time=1.2, rate_func=smooth)
        self.wait(0.5)
        self.play(x_tracker.animate.set_value(2.0), run_time=1.4, rate_func=smooth)
        self.wait(0.5)

        # 3. Transition to Algebraic Morphing
        self.play(FadeOut(telemetry_display), FadeOut(dot), FadeOut(tangent_line), run_time=0.6)

        morph_title = Text("Algebraic Factorization Morph", font_size=19, color=AMBER).move_to(side_panel.get_top() + DOWN * 0.4)
        self.play(Transform(panel_title, morph_title), run_time=0.6)

        eq1 = MathTex(r"f'(x)", r"=", r"3x^2", r"-", r"3", font_size=32, color=TEXT_WHITE).next_to(morph_title, DOWN, buff=0.45)
        self.play(Write(eq1), run_time=0.8)
        self.wait(0.6)

        eq2 = MathTex(r"f'(x)", r"=", r"3", r"(x^2 - 1)", font_size=32, color=TEXT_WHITE).move_to(eq1)
        self.play(TransformMatchingTex(eq1, eq2), run_time=0.9)
        self.wait(0.6)

        eq3 = MathTex(r"f'(x)", r"=", r"3", r"(x - 1)", r"(x + 1)", font_size=32, color=CYAN).move_to(eq2)
        self.play(TransformMatchingTex(eq2, eq3), run_time=0.9)
        self.wait(0.6)

        eq4 = MathTex(
            r"f'(x) = 0 \implies x = -1 \text{ or } x = +1",
            font_size=24, color=AMBER
        ).next_to(eq3, DOWN, buff=0.4)
        self.play(Write(eq4), run_time=0.8)

        # Drop lines from extrema to x-axis
        drop_neg1 = DashedLine(axes.c2p(-1, 2), axes.c2p(-1, 0), color=AMBER, stroke_width=2.5, dash_length=0.08)
        drop_pos1 = DashedLine(axes.c2p(1, -2), axes.c2p(1, 0), color=CYAN, stroke_width=2.5, dash_length=0.08)
        pt_max = Dot(axes.c2p(-1, 2), color=AMBER, radius=0.1)
        pt_min = Dot(axes.c2p(1, -2), color=CYAN, radius=0.1)
        label_max = MathTex(r"(-1, 2)", font_size=20, color=AMBER).next_to(pt_max, UP, buff=0.12)
        label_min = MathTex(r"(1, -2)", font_size=20, color=CYAN).next_to(pt_min, DOWN, buff=0.12)

        self.play(Create(drop_neg1), Create(drop_pos1), FadeIn(pt_max), FadeIn(pt_min), Write(label_max), Write(label_min), run_time=1.0)
        self.wait(1.0)

        # 4. Concavity Verification
        concav_title = Text("Second Derivative & Concavity Verification", font_size=17, color=CYAN).move_to(side_panel.get_top() + DOWN * 0.4)
        self.play(Transform(panel_title, concav_title), FadeOut(eq3), FadeOut(eq4), run_time=0.6)

        f_double = MathTex(r"f''(x) = 6x", font_size=28, color=AMBER).next_to(concav_title, DOWN, buff=0.35)
        concav_info = VGroup(
            MathTex(r"f''(-1) = -6 < 0 \implies \text{Concave Down } (\cap)", font_size=20, color=AMBER),
            Text("Traps LOCAL MAXIMUM at (-1, 2)", font_size=15, color=TEXT_WHITE),
            MathTex(r"f''(1) = +6 > 0 \implies \text{Concave Up } (\cup)", font_size=20, color=CYAN),
            Text("Holds LOCAL MINIMUM at (1, -2)", font_size=15, color=TEXT_WHITE),
        ).arrange(DOWN, buff=0.2).next_to(f_double, DOWN, buff=0.3)

        self.play(Write(f_double), Write(concav_info), run_time=1.4)
        self.wait(2.5)
