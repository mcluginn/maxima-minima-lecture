from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(__file__))
from common_theme import *


# -------------------------------------------------------------
# SCENE 01: THE OPENING HOOK (HILL-SHAPED TERRAIN)
# -------------------------------------------------------------
class Scene01_HookHill(Scene):
    def construct(self):
        header = create_header("The Geometry of Nature: Mountain Terrains", "Where does physical motion pause? Where are the peaks?", CYAN)
        self.play(Write(header), run_time=1.0)

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 5, 1],
            x_length=9.0,
            y_length=4.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": False},
            tips=True,
        ).shift(DOWN * 0.45)

        # Smooth double-crested hill curve
        def hill(x):
            return 3.5 * np.exp(-0.4 * (x + 1.2)**2) + 2.2 * np.exp(-0.8 * (x - 1.8)**2)

        curve = axes.plot(hill, x_range=[-3.8, 3.8], color=CYAN, stroke_width=4.5)
        self.play(Create(axes), Create(curve), run_time=1.4)

        # Probe moving across the peaks
        x_val = ValueTracker(-3.5)
        probe = always_redraw(lambda: Dot(
            axes.c2p(x_val.get_value(), hill(x_val.get_value())),
            color=AMBER, radius=0.1
        ))

        # Dynamic tangent vector
        def get_slope_vector():
            x0 = x_val.get_value()
            eps = 0.01
            m = (hill(x0 + eps) - hill(x0 - eps)) / (2 * eps)
            dx = 0.6 / np.sqrt(1 + m**2)
            dy = m * dx
            p1 = axes.c2p(x0 - dx, hill(x0) - dy)
            p2 = axes.c2p(x0 + dx, hill(x0) + dy)
            return Line(p1, p2, color=AMBER if abs(m) < 0.15 else (CYAN if m > 0 else CORAL), stroke_width=3.5)

        tangent = always_redraw(get_slope_vector)

        self.play(FadeIn(probe), Create(tangent))

        # Move to Major Peak
        self.play(x_val.animate.set_value(-1.2), run_time=2.5, rate_func=smooth)
        peak1 = Dot(axes.c2p(-1.2, hill(-1.2)), color=AMBER, radius=0.12)
        tag1 = Text("Summit (f' = 0)", font_size=20, color=AMBER).next_to(peak1, UP, buff=0.2)
        self.play(FadeIn(peak1), Write(tag1), Flash(peak1, color=AMBER))
        self.wait(1.0)

        # Move through valley to Minor Peak
        self.play(x_val.animate.set_value(1.8), run_time=3.0, rate_func=smooth)
        peak2 = Dot(axes.c2p(1.8, hill(1.8)), color=CYAN, radius=0.12)
        tag2 = Text("Secondary Ridge (f' = 0)", font_size=20, color=CYAN).next_to(peak2, UP, buff=0.2)
        self.play(FadeIn(peak2), Write(tag2), Flash(peak2, color=CYAN))
        self.wait(1.0)

        self.play(x_val.animate.set_value(3.5), run_time=1.8, rate_func=smooth)
        self.wait(1.5)


# -------------------------------------------------------------
# SCENE 02: LOCAL VS ABSOLUTE EXTREMA
# -------------------------------------------------------------
class Scene02_LocalVsAbsolute(Scene):
    def construct(self):
        header = create_header("Local vs. Absolute (Global) Extrema", "Neighborhood champions vs. the entire physical domain [a, b]", CORAL)
        self.play(Write(header), run_time=1.0)

        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 6, 1],
            x_length=7.5,
            y_length=4.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": False},
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        # Curve on [1, 6]
        # Left end at (1, 2.5), Peak at (2.5, 4.5), Valley at (4.2, 1.5), Right end at (6.0, 5.5) [ABS MAX]
        def f_bound(x):
            return 0.15 * (x - 1)*(x - 3.5)*(x - 5) + 0.5*x + 1.8

        curve = axes.plot(f_bound, x_range=[1.0, 6.0], color=CYAN, stroke_width=4)
        
        # Domain boundary lines
        line_a = DashedLine(axes.c2p(1, 0), axes.c2p(1, f_bound(1)), color=MUTED_GRAY, stroke_width=2)
        line_b = DashedLine(axes.c2p(6, 0), axes.c2p(6, f_bound(6)), color=CORAL, stroke_width=2)

        lbl_a = MathTex(r"a", font_size=22, color=TEXT_WHITE).next_to(axes.c2p(1, 0), DOWN, buff=0.2)
        lbl_b = MathTex(r"b", font_size=22, color=TEXT_WHITE).next_to(axes.c2p(6, 0), DOWN, buff=0.2)

        self.play(Create(axes), Create(line_a), Create(line_b), Write(lbl_a), Write(lbl_b), Create(curve), run_time=1.5)

        # Points
        pt_loc_max = Dot(axes.c2p(2.2, f_bound(2.2)), color=AMBER, radius=0.1)
        pt_loc_min = Dot(axes.c2p(4.4, f_bound(4.4)), color=CYAN, radius=0.1)
        pt_abs_max = Dot(axes.c2p(6.0, f_bound(6.0)), color=CORAL, radius=0.13)

        self.play(FadeIn(pt_loc_max), FadeIn(pt_loc_min), FadeIn(pt_abs_max))

        # Comparison Card
        panel = create_telemetry_card(width=5.0, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        panel_title = Text("Extrema Taxonomy", font_size=20, color=CORAL).move_to(panel.get_top() + DOWN * 0.4)
        self.play(FadeIn(panel), Write(panel_title))

        items = VGroup(
            VGroup(
                Text("LOCAL MAXIMUM (Interior)", font_size=16, color=AMBER, weight=BOLD),
                Text("Tallest in immediate open neighborhood (c-δ, c+δ)", font_size=13, color=MUTED_GRAY)
            ).arrange(DOWN, buff=0.08),
            VGroup(
                Text("LOCAL MINIMUM (Interior)", font_size=16, color=CYAN, weight=BOLD),
                Text("Lowest in immediate open neighborhood", font_size=13, color=MUTED_GRAY)
            ).arrange(DOWN, buff=0.08),
            VGroup(
                Text("ABSOLUTE MAXIMUM (at boundary b)", font_size=16, color=CORAL, weight=BOLD),
                Text("Highest point over ENTIRE domain [a, b]!", font_size=13, color=TEXT_WHITE),
                Text("Notice: Occurs where f'(x) ≠ 0!", font_size=14, color=AMBER, weight=BOLD)
            ).arrange(DOWN, buff=0.08)
        ).arrange(DOWN, buff=0.35).next_to(panel_title, DOWN, buff=0.35)

        for item in items:
            self.play(Write(item), run_time=0.8)
            self.wait(0.3)

        self.play(Flash(pt_abs_max, color=CORAL, flash_radius=0.4), run_time=0.8)
        self.wait(2.0)


# -------------------------------------------------------------
# SCENE 03: SINGULARITIES (CORNERS & CUSPS DNE)
# -------------------------------------------------------------
class Scene03_SingularitiesDNE(Scene):
    def construct(self):
        header = create_header("Singular Points: When f'(x) Fails to Exist", "Corners and cusps harbor crucial physical extrema", CORAL)
        self.play(Write(header), run_time=1.0)

        # Panel A: Corner f(x) = |x|
        axes_left = Axes(
            x_range=[-2.2, 2.2, 1], y_range=[-0.5, 2.5, 1],
            x_length=5.0, y_length=4.2,
            axis_config={"color": AXES_GRAY, "stroke_width": 1.5, "include_numbers": False}
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        curve_corner = axes_left.plot(lambda x: abs(x), x_range=[-1.8, 1.8], color=CYAN, stroke_width=4)
        dot_corner = Dot(axes_left.c2p(0, 0), color=CORAL, radius=0.1)

        title_corner = Text("Case A: Corner f(x) = |x|", font_size=18, color=TEXT_WHITE).next_to(axes_left, UP, buff=0.2)
        slope_left = Text("Left slope: -1", font_size=14, color=CORAL).next_to(axes_left.c2p(-1.0, 1.0), LEFT, buff=0.2)
        slope_right = Text("Right slope: +1", font_size=14, color=CYAN).next_to(axes_left.c2p(1.0, 1.0), RIGHT, buff=0.2)
        tag_corner = VGroup(
            Text("f'(0) DOES NOT EXIST", font_size=16, color=CORAL, weight=BOLD),
            Text("Yet x = 0 is an Absolute Minimum!", font_size=14, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.08).next_to(dot_corner, DOWN, buff=0.3)

        self.play(Create(axes_left), Create(curve_corner), FadeIn(dot_corner), Write(title_corner))
        self.play(Write(slope_left), Write(slope_right), Write(tag_corner), run_time=1.2)

        # Panel B: Cusp f(x) = x^(2/3)
        axes_right = Axes(
            x_range=[-2.2, 2.2, 1], y_range=[-0.5, 2.5, 1],
            x_length=5.0, y_length=4.2,
            axis_config={"color": AXES_GRAY, "stroke_width": 1.5, "include_numbers": False}
        ).to_edge(RIGHT, buff=0.8).shift(DOWN * 0.45)

        curve_cusp = axes_right.plot(lambda x: (abs(x)**(2/3)), x_range=[-1.8, 1.8], color=CYAN, stroke_width=4)
        dot_cusp = Dot(axes_right.c2p(0, 0), color=CORAL, radius=0.1)

        title_cusp = Text("Case B: Cusp f(x) = x^(2/3)", font_size=18, color=TEXT_WHITE).next_to(axes_right, UP, buff=0.2)
        vert_tan = DashedLine(axes_right.c2p(0, -0.4), axes_right.c2p(0, 1.8), color=AMBER, stroke_width=2.5, dash_length=0.1)
        tag_cusp = VGroup(
            Text("Vertical Tangent (Slope → ±∞)", font_size=16, color=AMBER, weight=BOLD),
            Text("x = 0 is a True Local Minimum!", font_size=14, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.08).next_to(dot_cusp, DOWN, buff=0.3)

        self.play(Create(axes_right), Create(curve_cusp), FadeIn(dot_cusp), Write(title_cusp))
        self.play(Create(vert_tan), Write(tag_cusp), run_time=1.2)
        self.wait(2.0)


# -------------------------------------------------------------
# SCENE 04: CLOSED INTERVAL METHOD (ENDPOINT SURPRISE)
# -------------------------------------------------------------
class Scene04_ClosedIntervalMethod(Scene):
    def construct(self):
        header = create_header("The Closed Interval Method: f(x) = x³ - 3x on [-0.5, 2.5]", "Testing interior critical candidates against domain boundary endpoints", AMBER)
        self.play(Write(header), run_time=1.0)

        axes = Axes(
            x_range=[-1.5, 3.0, 1], y_range=[-3.0, 9.0, 3],
            x_length=6.4, y_length=4.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": True, "font_size": 17}
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        def f(x): return x**3 - 3*x
        curve = axes.plot(f, x_range=[-0.5, 2.5], color=CYAN, stroke_width=4.5)

        # Ghost curve outside domain
        ghost = DashedVMobject(axes.plot(f, x_range=[-1.4, -0.5], color=MUTED_GRAY, stroke_width=2), num_dashes=15)

        # Shaded Domain Region
        shading = axes.get_area(curve, x_range=[-0.5, 2.5], color=CYAN, opacity=0.12)

        self.play(Create(axes), Create(ghost), Create(curve), FadeIn(shading), run_time=1.4)

        # Points
        pt_left = Dot(axes.c2p(-0.5, f(-0.5)), color=MUTED_GRAY, radius=0.09)
        pt_int = Dot(axes.c2p(1.0, f(1.0)), color=CYAN, radius=0.12)
        pt_right = Dot(axes.c2p(2.5, f(2.5)), color=CORAL, radius=0.14)
        pt_excluded = Dot(axes.c2p(-1.0, f(-1.0)), color=RED, radius=0.09)

        cross = Cross(pt_excluded, stroke_color=RED, stroke_width=3, scale_factor=0.2)

        self.play(FadeIn(pt_left), FadeIn(pt_int), FadeIn(pt_right), FadeIn(pt_excluded), Create(cross))

        # Right Candidate Comparison Table
        panel = create_telemetry_card(width=5.6, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        panel_title = Text("Candidate Evaluation Matrix", font_size=20, color=AMBER).move_to(panel.get_top() + DOWN * 0.4)
        self.play(FadeIn(panel), Write(panel_title))

        rows = VGroup(
            Text("1. Filter Critical Points:", font_size=15, color=MUTED_GRAY),
            MathTex(r"x = -1 \notin [-0.5, 2.5] \implies \mathbf{DISCARDED}", font_size=18, color=RED),
            MathTex(r"x = +1 \in (-0.5, 2.5) \implies \text{VALID INTERIOR}", font_size=18, color=CYAN),
            Text("2. Evaluate All Candidates:", font_size=15, color=MUTED_GRAY),
            MathTex(r"f(1) = -2.000 \implies \mathbf{ABSOLUTE\;MINIMUM}", font_size=20, color=CYAN),
            MathTex(r"f(-0.5) = 1.375 \quad (\text{Left Endpoint})", font_size=18, color=TEXT_WHITE),
            MathTex(r"f(2.5) = \mathbf{8.125} \implies \mathbf{ABSOLUTE\;MAXIMUM}", font_size=20, color=CORAL),
            Text("Takeaway: True peak occurs at boundary!", font_size=15, color=AMBER, weight=BOLD)
        ).arrange(DOWN, buff=0.16).next_to(panel_title, DOWN, buff=0.25)

        for row in rows:
            self.play(Write(row), run_time=0.6)
            self.wait(0.2)

        self.play(Flash(pt_right, color=CORAL, flash_radius=0.4), run_time=0.8)
        self.wait(2.0)


# -------------------------------------------------------------
# SCENE 05: PRACTICAL ENGINEERING OPTIMIZATION (MAX POWER)
# -------------------------------------------------------------
class Scene05_MaxPowerTransfer(Scene):
    def construct(self):
        header = create_header("Engineering Optimization: Maximum Power Transfer", "Impedance matching in electrical, RF, and renewable energy circuits", CYAN)
        self.play(Write(header), run_time=1.0)

        # Power characteristic curve
        # P(RL) = Vs^2 * RL / (Rs + RL)^2
        # Let Vs = 10V, Rs = 2 Ohms -> Pmax = 100/(8) = 12.5 W at RL = 2
        axes = Axes(
            x_range=[0, 8, 2], y_range=[0, 14, 4],
            x_length=6.4, y_length=4.8,
            axis_config={"color": AXES_GRAY, "stroke_width": 2, "include_numbers": True, "font_size": 17}
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        x_lbl = axes.get_x_axis_label("R_L \\; (\\Omega)", edge=RIGHT, direction=DOWN, buff=0.2)
        y_lbl = axes.get_y_axis_label("P(R_L) \\; (\\text{W})", edge=UP, direction=LEFT, buff=0.2)

        def P(r): return (100 * r) / ((2 + r)**2)
        curve = axes.plot(P, x_range=[0.05, 8.0], color=CYAN, stroke_width=4.5)

        # Peak Point at RL = Rs = 2
        pt_peak = Dot(axes.c2p(2.0, 12.5), color=AMBER, radius=0.13)
        peak_drop = DashedLine(axes.c2p(2.0, 12.5), axes.c2p(2.0, 0), color=AMBER, stroke_width=2.5)
        peak_tag = MathTex(r"R_L = R_s = 2\,\Omega", font_size=20, color=AMBER).next_to(axes.c2p(2.0, 0), DOWN, buff=0.25)

        self.play(Create(axes), Create(x_lbl), Create(y_lbl), Create(curve), run_time=1.4)
        self.play(FadeIn(pt_peak), Create(peak_drop), Write(peak_tag), Flash(pt_peak, color=AMBER))

        # Right Derivation Card
        panel = create_telemetry_card(width=5.6, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        panel_title = Text("Calculus of Impedance Matching", font_size=20, color=CYAN).move_to(panel.get_top() + DOWN * 0.4)
        self.play(FadeIn(panel), Write(panel_title))

        eqs = VGroup(
            MathTex(r"P(R_L) = \frac{V_s^2 R_L}{(R_s + R_L)^2}", font_size=22, color=TEXT_WHITE),
            Text("Apply Quotient Rule:", font_size=15, color=MUTED_GRAY),
            MathTex(r"\frac{dP}{dR_L} = V_s^2 \frac{R_s - R_L}{(R_s + R_L)^3}", font_size=22, color=AMBER),
            Text("Stationary Condition dP/dRL = 0:", font_size=15, color=MUTED_GRAY),
            MathTex(r"R_s - R_L = 0 \implies \mathbf{R_L = R_s}", font_size=24, color=AMBER),
            MathTex(r"P_{\max} = \frac{V_s^2}{4R_s} = \mathbf{12.5\,\text{W}}", font_size=20, color=CYAN),
            Text("Governs audio, RF, & solar MPPT tracking!", font_size=14, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.16).next_to(panel_title, DOWN, buff=0.25)

        for eq in eqs:
            self.play(Write(eq), run_time=0.6)
            self.wait(0.2)

        self.wait(2.0)
