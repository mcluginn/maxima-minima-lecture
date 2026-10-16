"""
manim_lecture/mathalino_problems.py
Authentic mathematical animations for selected optimization problems from MATHALINO:
1. MathalinoProblem1_NumberOptimization (Problem 1, 01-04 Number Problems)
2. MathalinoProblem2_RiverbankLot (Problem 10, 09-11 Rectangular Lot Problems)
3. MathalinoProblem3_OpenTopBox (Problem 16, 15-17 Box Open at the Top)
4. MathalinoProblem4_TourBusRevenue (Problem 03, Tour Bus 80 Seats)
5. MathalinoProblem5_TrapezoidalGutter (Problem 42, 41-42 Trapezoidal Gutter)
"""

from manim import *
import numpy as np
import sys
import os

sys.path.append(os.path.dirname(__file__))
from common_theme import *


# -------------------------------------------------------------
# 1. NUMBER OPTIMIZATION (MATHALINO PROBLEM 1)
# Source: https://mathalino.com/reviewer/differential-calculus/01-04-number-problems-in-maxima-and-minima
# "What number exceeds its square by the maximum amount?"
# -------------------------------------------------------------
class MathalinoProblem1_NumberOptimization(Scene):
    def construct(self):
        header = create_header(
            "Mathalino Prob 1: Number Optimization",
            "What number exceeds its square by the maximum amount? (Source: mathalino.com)",
            AMBER
        )
        self.play(Write(header), run_time=0.8)

        # Left Parabola Graph: y = x - x^2
        axes = Axes(
            x_range=[-0.2, 1.2, 0.2],
            y_range=[-0.1, 0.35, 0.1],
            x_length=5.6,
            y_length=4.4,
            axis_config={"color": AXES_GRAY, "stroke_width": 1.5, "include_numbers": True, "font_size": 16},
            tips=True,
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        x_lbl = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN, buff=0.15)
        y_lbl = axes.get_y_axis_label("f(x)", edge=UP, direction=LEFT, buff=0.15)

        def f(x): return x - x**2
        curve = axes.plot(f, x_range=[0.0, 1.0], color=CYAN, stroke_width=3.5)
        curve_label = MathTex(r"f(x) = x - x^2", color=CYAN, font_size=22).next_to(axes, UP, buff=0.1)

        self.play(Create(axes), Create(x_lbl), Create(y_lbl), Create(curve), Write(curve_label), run_time=1.0)

        # Right Telemetry & Derivation Card
        card = create_telemetry_card(width=6.2, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        title = Text("Mathematical Modeling Workflow", font_size=18, color=AMBER).move_to(card.get_top() + DOWN * 0.35)
        self.play(FadeIn(card), Write(title))

        steps = [
            MathTex(r"\text{1. Define: } x = \text{number}, \,\, x^2 = \text{square}", font_size=20, color=TEXT_WHITE),
            MathTex(r"\text{2. Objective: } f(x) = x - x^2", font_size=22, color=CYAN),
            MathTex(r"\text{3. Differentiate: } f'(x) = 1 - 2x = 0", font_size=22, color=AMBER),
            MathTex(r"\text{4. Critical Number: } 2x = 1 \implies x = \frac{1}{2}", font_size=23, color=AMBER),
            MathTex(r"\text{5. Maximum Excess: } f\left(\frac{1}{2}\right) = \frac{1}{2} - \frac{1}{4} = \frac{1}{4}", font_size=21, color=TEXT_WHITE),
            MathTex(r"\text{6. Concavity: } f''(x) = -2 < 0 \implies \mathbf{Strict\;Maximum}", font_size=20, color=CYAN)
        ]
        group = VGroup(*steps).arrange(DOWN, buff=0.22).next_to(title, DOWN, buff=0.25)

        # Peak Point on Curve
        peak_dot = Dot(axes.c2p(0.5, 0.25), color=AMBER, radius=0.09)
        peak_lbl = MathTex(r"\left(\frac{1}{2}, \frac{1}{4}\right)", font_size=19, color=AMBER).next_to(peak_dot, UP, buff=0.1)
        tan_peak = Line(axes.c2p(0.3, 0.25), axes.c2p(0.7, 0.25), color=AMBER, stroke_width=3)

        for s in steps[:3]:
            self.play(Write(s), run_time=0.6)
        
        self.play(Write(steps[3]), FadeIn(peak_dot), Create(tan_peak), Write(peak_lbl), run_time=0.8)
        
        for s in steps[4:]:
            self.play(Write(s), run_time=0.6)

        self.wait(2.0)


# -------------------------------------------------------------
# 2. RECTANGULAR LOT OPTIMIZATION (MATHALINO PROBLEM 10)
# Source: https://mathalino.com/reviewer/differential-calculus/09-11-rectangular-lot-problems-in-maxima-and-minima
# "A rectangular field of given area is to be fenced off along the bank of a river.
# If no fence is needed along the river, what is the shape of the rectangle requiring the least amount of fencing?"
# -------------------------------------------------------------
class MathalinoProblem2_RiverbankLot(Scene):
    def construct(self):
        header = create_header(
            "Mathalino Prob 10: Riverbank Fencing Optimization",
            "Minimum perimeter fence for fixed area A along a river (Source: mathalino.com)",
            CYAN
        )
        self.play(Write(header), run_time=0.8)

        # Left Geometric Model
        # River at top
        river_bank = Line(LEFT * 5.8, LEFT * 0.6, color=BLUE_D, stroke_width=8).shift(UP * 1.5)
        river_text = Text("RIVER (No Fencing Required)", font_size=15, color=BLUE_B).next_to(river_bank, UP, buff=0.12)
        
        # Rectangular Fence (3 sides)
        # Optimal: x = 2y. For display, x = 3.6, y = 1.8
        p_top_l = LEFT * 4.6 + UP * 1.45
        p_top_r = LEFT * 1.8 + UP * 1.45
        p_bot_l = LEFT * 4.6 + DOWN * 0.35
        p_bot_r = LEFT * 1.8 + DOWN * 0.35

        fence_l = Line(p_top_l, p_bot_l, color=AMBER, stroke_width=3.5)
        fence_b = Line(p_bot_l, p_bot_r, color=AMBER, stroke_width=3.5)
        fence_r = Line(p_top_r, p_bot_r, color=AMBER, stroke_width=3.5)
        fences = VGroup(fence_l, fence_b, fence_r)

        lbl_x = MathTex("x", color=AMBER, font_size=24).next_to(fence_b, DOWN, buff=0.15)
        lbl_y = MathTex("y", color=AMBER, font_size=24).next_to(fence_l, LEFT, buff=0.15)
        area_tag = MathTex(r"\text{Area } A = xy", color=CYAN, font_size=22).move_to((p_top_l + p_bot_r) / 2)

        self.play(Create(river_bank), Write(river_text), run_time=0.8)
        self.play(Create(fences), Write(lbl_x), Write(lbl_y), Write(area_tag), run_time=1.0)

        # Right Card: Formulation & Calculus
        card = create_telemetry_card(width=6.4, height=4.8).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        title = Text("Geometric Constraint Reduction", font_size=18, color=CYAN).move_to(card.get_top() + DOWN * 0.35)
        self.play(FadeIn(card), Write(title))

        steps = [
            MathTex(r"\text{1. Constraint: } A = xy \implies x = \frac{A}{y}", font_size=21, color=TEXT_WHITE),
            MathTex(r"\text{2. Objective (Fence): } P = x + 2y", font_size=22, color=AMBER),
            MathTex(r"\text{3. Single Variable: } P(y) = \frac{A}{y} + 2y", font_size=22, color=CYAN),
            MathTex(r"\text{4. Differentiate: } \frac{dP}{dy} = -\frac{A}{y^2} + 2 = 0", font_size=22, color=AMBER),
            MathTex(r"\text{5. Solve: } 2y^2 = A = xy \implies y = \frac{1}{2}x", font_size=23, color=GREEN),
            MathTex(r"\text{6. Optimum Shape: } \mathbf{\text{Width } y = \frac{1}{2} \times \text{Length } x}", font_size=21, color=AMBER),
            MathTex(r"\text{7. Minimum Check: } \frac{d^2P}{dy^2} = \frac{2A}{y^3} > 0 \implies \mathbf{Minimum}", font_size=19, color=TEXT_WHITE)
        ]
        group = VGroup(*steps).arrange(DOWN, buff=0.20).next_to(title, DOWN, buff=0.22)

        for s in steps:
            self.play(Write(s), run_time=0.6)
            self.wait(0.15)

        self.wait(2.0)


# -------------------------------------------------------------
# 3. OPEN-TOP BOX OPTIMIZATION (MATHALINO PROBLEM 16)
# Source: https://mathalino.com/reviewer/differential-calculus/15-17-box-open-at-the-top
# "Find the volume of the largest box that can be made by cutting equal squares
# out of the corners of a piece of cardboard of dimensions 15 inches by 24 inches,
# and then turning up the sides."
# -------------------------------------------------------------
class MathalinoProblem3_OpenTopBox(Scene):
    def construct(self):
        header = create_header(
            "Mathalino Prob 16: Open-Top Box Optimization",
            "Cardboard 15\" × 24\": Cut corner squares x to maximize Volume (Source: mathalino.com)",
            AMBER
        )
        self.play(Write(header), run_time=0.8)

        # Left: Cardboard Sheet Model (24 x 15 ratio -> 4.8 x 3.0)
        sheet_w = 4.8
        sheet_h = 3.0
        sheet = Rectangle(width=sheet_w, height=sheet_h, color=CARD_BORDER, fill_color=CARD_BG, fill_opacity=0.6).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)
        
        lbl_24 = MathTex(r"24''", font_size=20, color=CYAN).next_to(sheet, UP, buff=0.1)
        lbl_15 = MathTex(r"15''", font_size=20, color=CYAN).next_to(sheet, LEFT, buff=0.1)

        # 4 Corner Cutouts (squares of size cut_s = 0.6)
        cut_s = 0.65
        c_ul = Rectangle(width=cut_s, height=cut_s, color=CORAL, fill_color=CORAL, fill_opacity=0.35).align_to(sheet, UL)
        c_ur = Rectangle(width=cut_s, height=cut_s, color=CORAL, fill_color=CORAL, fill_opacity=0.35).align_to(sheet, UR)
        c_dl = Rectangle(width=cut_s, height=cut_s, color=CORAL, fill_color=CORAL, fill_opacity=0.35).align_to(sheet, DL)
        c_dr = Rectangle(width=cut_s, height=cut_s, color=CORAL, fill_color=CORAL, fill_opacity=0.35).align_to(sheet, DR)
        corners = VGroup(c_ul, c_ur, c_dl, c_dr)
        
        cut_lbl = MathTex(r"x \times x", font_size=16, color=CORAL).move_to(c_ul)

        self.play(Create(sheet), Write(lbl_24), Write(lbl_15), run_time=1.0)
        self.play(FadeIn(corners), Write(cut_lbl), run_time=0.8)

        # Right: Derivation Card with TransformMatchingTex
        card = create_telemetry_card(width=6.5, height=4.8).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.45)
        title = Text("Volume Objective & Critical Points", font_size=18, color=AMBER).move_to(card.get_top() + DOWN * 0.35)
        self.play(FadeIn(card), Write(title))

        eq1 = MathTex(r"V(x) = (24 - 2x)(15 - 2x)x", font_size=22, color=TEXT_WHITE).next_to(title, DOWN, buff=0.3)
        self.play(Write(eq1), run_time=0.8)

        eq2 = MathTex(r"V(x) = 4x^3 - 78x^2 + 360x", font_size=22, color=CYAN).move_to(eq1)
        self.play(TransformMatchingTex(eq1, eq2), run_time=0.9)
        self.wait(0.4)

        eq3 = MathTex(r"V'(x) = 12x^2 - 156x + 360 = 0", font_size=22, color=AMBER).next_to(eq2, DOWN, buff=0.25)
        self.play(Write(eq3), run_time=0.8)

        eq4 = MathTex(r"x^2 - 13x + 30 = 0 \implies (x - 10)(x - 3) = 0", font_size=21, color=TEXT_WHITE).next_to(eq3, DOWN, buff=0.22)
        self.play(Write(eq4), run_time=0.8)

        # Domain & Feasibility check
        feasibility = VGroup(
            MathTex(r"\text{Feasible Domain: } 0 < x < \frac{15}{2} = 7.5''", font_size=19, color=TEXT_MUTED),
            MathTex(r"x = 10'' \implies \mathbf{Impossible} \,\, (15 - 20 < 0)", font_size=20, color=CORAL),
            MathTex(r"\mathbf{Optimal\;Depth: } x = 3'' \in (0, 7.5)", font_size=22, color=GREEN),
            MathTex(r"V_{\max} = (24 - 6)(15 - 6)(3) = \mathbf{486\text{ in}^3}", font_size=24, color=AMBER)
        ).arrange(DOWN, buff=0.18).next_to(eq4, DOWN, buff=0.22)

        for item in feasibility:
            self.play(Write(item), run_time=0.6)
            self.wait(0.2)

        self.wait(2.0)


# -------------------------------------------------------------
# 4. MAXIMUM REVENUE TOUR BUS (MATHALINO PROBLEM 03)
# Source: https://mathalino.com/reviewer/differential-calculus/03-maximum-revenue-tour-bus-80-seats
# "A tour bus has 80 seats. When tour costs P28,000, all seats sell.
# For each additional P1,000 charged, 2 fewer seats sell. Find the largest possible revenue."
# -------------------------------------------------------------
class MathalinoProblem4_TourBusRevenue(Scene):
    def construct(self):
        header = create_header(
            "Mathalino Prob 03: Applied Maximum Revenue",
            "80-Seat Tour Bus: Balancing ticket price vs. demand (Source: mathalino.com)",
            GREEN
        )
        self.play(Write(header), run_time=0.8)

        # Left: Revenue Parabola R(x) = 28000 + 300x - 25x^2
        axes = Axes(
            x_range=[-1, 14, 2],
            y_range=[27500, 29200, 500],
            x_length=5.6,
            y_length=4.4,
            axis_config={"color": AXES_GRAY, "stroke_width": 1.5, "include_numbers": False},
            tips=True,
        ).to_edge(LEFT, buff=0.8).shift(DOWN * 0.45)

        x_lbl = Text("x (P1,000 increments)", font_size=13, color=MUTED_GRAY).next_to(axes.x_axis, DOWN, buff=0.15)
        y_lbl = Text("Revenue (PHP)", font_size=13, color=MUTED_GRAY).next_to(axes.y_axis, UP, buff=0.15)

        def R(x): return 28000 + 300*x - 25*x**2
        curve = axes.plot(R, x_range=[0, 12], color=GREEN, stroke_width=3.5)
        
        # Max Point: x = 6, R = 28900
        pt_max = Dot(axes.c2p(6, 28900), color=AMBER, radius=0.1)
        lbl_max = MathTex(r"\mathbf{(6, \text{P}28{,}900)}", font_size=20, color=AMBER).next_to(pt_max, UP, buff=0.12)
        tan_max = Line(axes.c2p(4.5, 28900), axes.c2p(7.5, 28900), color=AMBER, stroke_width=2.5)

        self.play(Create(axes), Write(x_lbl), Write(y_lbl), Create(curve), run_time=1.0)
        self.play(FadeIn(pt_max), Create(tan_max), Write(lbl_max), run_time=0.8)

        # Right: Derivation Card
        card = create_telemetry_card(width=6.4, height=4.8).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.45)
        title = Text("Revenue Model Formulation", font_size=18, color=GREEN).move_to(card.get_top() + DOWN * 0.35)
        self.play(FadeIn(card), Write(title))

        steps = [
            MathTex(r"\text{Base: } \frac{\text{P}28{,}000}{80} = \text{P}350/\text{seat}; \,\, \Delta p = \frac{\text{P}1{,}000}{80} = \text{P}12.50", font_size=18, color=TEXT_WHITE),
            MathTex(r"\text{Price: } p(x) = 350 + 12.5x", font_size=20, color=CYAN),
            MathTex(r"\text{Quantity: } q(x) = 80 - 2x", font_size=20, color=AMBER),
            MathTex(r"R(x) = (350 + 12.5x)(80 - 2x) = 28{,}000 + 300x - 25x^2", font_size=19, color=TEXT_WHITE),
            MathTex(r"\frac{dR}{dx} = 300 - 50x = 0 \implies \mathbf{x = 6}", font_size=22, color=GREEN),
            MathTex(r"\text{Optimal Fare: } p = 350 + 12.5(6) = \mathbf{\text{P}425/\text{seat}}", font_size=19, color=CYAN),
            MathTex(r"\text{Passengers: } q = 80 - 2(6) = \mathbf{68\text{ seats}}", font_size=19, color=AMBER),
            MathTex(r"\mathbf{\text{Maximum Revenue} = 425 \times 68 = \text{P}28{,}900} \,\, \text{[Option C]}", font_size=21, color=AMBER)
        ]
        group = VGroup(*steps).arrange(DOWN, buff=0.16).next_to(title, DOWN, buff=0.20)

        for s in steps:
            self.play(Write(s), run_time=0.5)
            self.wait(0.12)

        self.wait(2.0)


# -------------------------------------------------------------
# 5. TRAPEZOIDAL GUTTER OPTIMIZATION (MATHALINO PROBLEM 42)
# Source: https://mathalino.com/reviewer/differential-calculus/41-42-maxima-and-minima-problem-involving-a-trapezoidal-gutter
# "From a strip of tin 14 inches a trapezoidal gutter is to be made by bending up the sides
# at an angle of 45°. Find the width of the base for greatest carrying capacity."
# -------------------------------------------------------------
class MathalinoProblem5_TrapezoidalGutter(Scene):
    def construct(self):
        header = create_header(
            "Mathalino Prob 42: Trapezoidal Gutter Capacity",
            "14-inch metal strip bent at 45°: Maximize hydraulic carrying capacity (Source: mathalino.com)",
            CORAL
        )
        self.play(Write(header), run_time=0.8)

        # Left: Trapezoidal Cross-Section Model
        # Base a, slant s = (14-a)/2, angle 45 deg
        # Base from (-1.0, -1.0) to (1.0, -1.0) in local coords -> scale for canvas
        orig_x = -3.8
        orig_y = -0.5
        b_left = np.array([orig_x - 0.9, orig_y, 0])
        b_right = np.array([orig_x + 0.9, orig_y, 0])
        t_left = np.array([orig_x - 1.9, orig_y + 1.0, 0])
        t_right = np.array([orig_x + 1.9, orig_y + 1.0, 0])

        poly = Polygon(b_left, b_right, t_right, t_left, color=CORAL, stroke_width=3.5, fill_color=CORAL, fill_opacity=0.15)
        base_line = Line(b_left, b_right, color=AMBER, stroke_width=4.5)
        
        lbl_base = MathTex(r"\text{Base } a", font_size=20, color=AMBER).next_to(base_line, DOWN, buff=0.12)
        lbl_side = MathTex(r"s = \frac{14 - a}{2}", font_size=18, color=CYAN).next_to(Line(b_left, t_left), LEFT, buff=0.1)
        lbl_angle = MathTex(r"45^\circ", font_size=17, color=TEXT_WHITE).move_to(b_left + np.array([0.3, 0.25, 0]))

        # Dashed height line
        h_line = DashedLine(t_left, np.array([t_left[0], orig_y, 0]), color=MUTED_GRAY, stroke_width=2)
        lbl_h = MathTex(r"h = s\sin 45^\circ", font_size=17, color=MUTED_GRAY).next_to(h_line, LEFT, buff=0.08)

        self.play(Create(poly), Create(base_line), Write(lbl_base), Write(lbl_side), Write(lbl_angle), run_time=1.2)
        self.play(Create(h_line), Write(lbl_h), run_time=0.8)

        # Right: Derivation Card
        card = create_telemetry_card(width=6.4, height=4.8).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.45)
        title = Text("Trapezoidal Cross-Section Calculus", font_size=18, color=CORAL).move_to(card.get_top() + DOWN * 0.35)
        self.play(FadeIn(card), Write(title))

        steps = [
            MathTex(r"\text{Height: } h = \frac{14 - a}{2\sqrt{2}}", font_size=21, color=TEXT_WHITE),
            MathTex(r"\text{Area: } A(a) = ah + h^2 = \frac{14a - a^2}{2\sqrt{2}} + \frac{(14 - a)^2}{8}", font_size=20, color=CYAN),
            MathTex(r"\frac{dA}{da} = \frac{7 - a}{\sqrt{2}} + \frac{a - 14}{4} = 0", font_size=21, color=AMBER),
            MathTex(r"a(2\sqrt{2} - 1) = 14(\sqrt{2} - 1)", font_size=21, color=TEXT_WHITE),
            MathTex(r"a = \frac{14(\sqrt{2} - 1)}{2\sqrt{2} - 1} \approx \mathbf{3.17\text{ inches}}", font_size=24, color=GREEN),
            MathTex(r"\text{Slant Sides: } s = \frac{14 - 3.17}{2} \approx \mathbf{5.41\text{ inches}}", font_size=19, color=TEXT_MUTED),
            MathTex(r"\text{Concavity: } \frac{d^2A}{da^2} = \frac{1}{4} - \frac{1}{\sqrt{2}} < 0 \implies \mathbf{Maximum}", font_size=19, color=AMBER)
        ]
        group = VGroup(*steps).arrange(DOWN, buff=0.20).next_to(title, DOWN, buff=0.22)

        for s in steps:
            self.play(Write(s), run_time=0.5)
            self.wait(0.15)

        self.wait(2.0)
