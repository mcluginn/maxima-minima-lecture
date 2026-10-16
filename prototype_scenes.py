from manim import *
import numpy as np

# Global Dark Engineering Theme Configuration
config.background_color = "#0B0F19"  # Midnight Navy
CYAN = "#38BDF8"       # Increasing / Function Curve
AMBER = "#F59E0B"      # Critical Points / Turning Points
CORAL = "#F43F5E"      # Decreasing / Alerts
TEXT_WHITE = "#F8FAFC"
MUTED_GRAY = "#94A3B8"
AXES_GRAY = "#475569"
GRID_GRAY = "#1E293B"


class Scene1_MovingTangent(Scene):
    def construct(self):
        # 1. Title Banner
        title = Text("1. The Function & Dynamic Tangent", font_size=32, color=TEXT_WHITE)
        subtitle = Text("Slope vanishes at turning points: f'(x) = 0", font_size=20, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.35)
        self.play(Write(title_group), run_time=1.0)

        # 2. Coordinate Axes
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-3.5, 3.5, 1],
            x_length=7.2,
            y_length=4.8,
            axis_config={
                "color": AXES_GRAY,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 18,
            },
            tips=True,
        ).shift(DOWN * 0.45 + LEFT * 1.6)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN, buff=0.2)
        y_label = axes.get_y_axis_label("y", edge=UP, direction=LEFT, buff=0.2)
        axes_group = VGroup(axes, x_label, y_label)

        # 3. Curve f(x) = x^3 - 3x (clamped domain to prevent banner collision)
        def f(x):
            return x**3 - 3*x

        def f_prime(x):
            return 3*x**2 - 3

        curve = axes.plot(f, x_range=[-2.15, 2.15], color=CYAN, stroke_width=4)
        curve_label = MathTex(r"f(x) = x^3 - 3x", color=CYAN, font_size=26)
        curve_label.next_to(axes.c2p(1.5, f(1.5)), RIGHT, buff=0.3).shift(UP * 0.4)

        self.play(Create(axes_group), run_time=1.0)
        self.play(Create(curve), Write(curve_label), run_time=1.5)

        # 4. Moving Point with ValueTracker
        x_tracker = ValueTracker(-2.05)

        # Dot on curve
        dot = always_redraw(lambda: Dot(
            axes.c2p(x_tracker.get_value(), f(x_tracker.get_value())),
            color=AMBER,
            radius=0.08
        ))

        # Dynamic Tangent Line
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

        # Readout panel on right
        panel = RoundedRectangle(
            corner_radius=0.2,
            width=4.0,
            height=4.8,
            fill_color="#111827",
            fill_opacity=0.9,
            stroke_color=GRID_GRAY,
            stroke_width=1.5
        ).to_edge(RIGHT, buff=0.5).shift(DOWN * 0.45)

        panel_title = Text("Real-Time Telemetry", font_size=20, color=CYAN).move_to(panel.get_top() + DOWN * 0.4)
        
        # Dynamic Readouts
        pos_readout = always_redraw(lambda: MathTex(
            r"x = " + f"{x_tracker.get_value():.2f}",
            font_size=24, color=TEXT_WHITE
        ).next_to(panel_title, DOWN, buff=0.4))

        slope_readout = always_redraw(lambda: MathTex(
            r"f'(x) = " + f"{f_prime(x_tracker.get_value()):+.2f}",
            font_size=26,
            color=AMBER if abs(f_prime(x_tracker.get_value())) < 0.2 else (CYAN if f_prime(x_tracker.get_value()) > 0 else CORAL)
        ).next_to(pos_readout, DOWN, buff=0.3))

        status_readout = always_redraw(lambda: Text(
            "TURNING POINT (Peak)" if abs(x_tracker.get_value() + 1.0) < 0.08 else
            ("TURNING POINT (Trough)" if abs(x_tracker.get_value() - 1.0) < 0.08 else
             ("Ascending (f' > 0)" if f_prime(x_tracker.get_value()) > 0 else "Descending (f' < 0)")),
            font_size=16,
            color=AMBER if abs(f_prime(x_tracker.get_value())) < 0.2 else (CYAN if f_prime(x_tracker.get_value()) > 0 else CORAL)
        ).next_to(slope_readout, DOWN, buff=0.3))

        self.play(FadeIn(panel), Write(panel_title))
        self.play(FadeIn(dot), Create(tangent_line), FadeIn(pos_readout), FadeIn(slope_readout), FadeIn(status_readout))
        self.wait(0.5)

        # 5. Motion along curve: Ascent to Local Max (-1, 2)
        self.play(x_tracker.animate.set_value(-1.0), run_time=2.8, rate_func=smooth)
        
        # Max Callout (Cleanly offset to avoid tick overlap)
        dot_max = Dot(axes.c2p(-1.0, 2.0), color=AMBER, radius=0.11)
        max_box = VGroup(
            MathTex(r"\text{Local Max } (-1, 2)", font_size=21, color=AMBER),
            MathTex(r"f'(-1) = 0", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.08).next_to(axes.c2p(-1.0, 2.0), UP + LEFT * 0.8, buff=0.15)
        
        self.play(FadeIn(dot_max), FadeIn(max_box), run_time=0.8)
        self.wait(1.2)

        # 6. Descent to Local Min (1, -2)
        self.play(x_tracker.animate.set_value(1.0), run_time=3.0, rate_func=smooth)
        
        # Min Callout (Cleanly offset)
        dot_min = Dot(axes.c2p(1.0, -2.0), color=CYAN, radius=0.11)
        min_box = VGroup(
            MathTex(r"\text{Local Min } (1, -2)", font_size=21, color=CYAN),
            MathTex(r"f'(1) = 0", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.08).next_to(axes.c2p(1.0, -2.0), DOWN + RIGHT * 0.8, buff=0.15)
        
        self.play(FadeIn(dot_min), FadeIn(min_box), run_time=0.8)
        self.wait(1.2)

        # 7. Complete to right boundary
        self.play(x_tracker.animate.set_value(2.05), run_time=2.2, rate_func=smooth)
        self.wait(1.5)


class Scene2_EquationMorph(Scene):
    def construct(self):
        # 1. Title Banner
        title = Text("2. Equation Morphing & Root Identification", font_size=32, color=TEXT_WHITE)
        subtitle = Text("Transforming derivative to find critical numbers", font_size=20, color=AMBER)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.35)
        self.play(Write(title_group), run_time=1.0)

        # 2. Left Side: Graph thumbnail with critical points and drop-lines
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

        # 3. Right Side: Algebraic Morphing Sequence
        box = RoundedRectangle(
            corner_radius=0.2,
            width=6.6,
            height=4.8,
            fill_color="#111827",
            fill_opacity=0.9,
            stroke_color=GRID_GRAY,
            stroke_width=1.5
        ).to_edge(RIGHT, buff=0.6).shift(DOWN * 0.45)
        self.play(FadeIn(box))

        step_title = Text("Algebraic Factorization", font_size=20, color=AMBER).move_to(box.get_top() + DOWN * 0.45)
        self.play(Write(step_title))

        # Equation Stages using TransformMatchingTex
        eq1 = MathTex(r"f'(x)", r"=", r"3x^2", r"-", r"3", font_size=32, color=TEXT_WHITE).next_to(step_title, DOWN, buff=0.45)
        self.play(Write(eq1), run_time=0.9)
        self.wait(0.8)

        # Stage 2: Factor out 3
        eq2 = MathTex(r"f'(x)", r"=", r"3", r"(x^2 - 1)", font_size=32, color=TEXT_WHITE).move_to(eq1)
        self.play(TransformMatchingTex(eq1, eq2), run_time=1.0)
        self.wait(0.8)

        # Stage 3: Difference of squares
        eq3 = MathTex(r"f'(x)", r"=", r"3", r"(x - 1)", r"(x + 1)", font_size=32, color=CYAN).move_to(eq2)
        self.play(TransformMatchingTex(eq2, eq3), run_time=1.0)
        self.wait(0.8)

        # Stage 4: Solve f'(x) = 0
        eq4 = MathTex(
            r"f'(x) = 0", r"\implies", r"x = -1", r"\text{ or }", r"x = +1",
            font_size=29, color=AMBER
        ).next_to(eq3, DOWN, buff=0.5)
        self.play(Write(eq4), run_time=1.0)
        self.wait(0.8)

        # 4. Vertical Drop-Lines on Graph (clean, elegant, no crossing text!)
        drop_neg1 = DashedLine(
            start=axes.c2p(-1, 2),
            end=axes.c2p(-1, 0),
            color=AMBER,
            stroke_width=2.5,
            dash_length=0.08
        )
        drop_pos1 = DashedLine(
            start=axes.c2p(1, -2),
            end=axes.c2p(1, 0),
            color=CYAN,
            stroke_width=2.5,
            dash_length=0.08
        )

        coord_tag1 = MathTex(r"x = -1", font_size=20, color=AMBER).next_to(axes.c2p(-1, 0), DOWN, buff=0.25)
        coord_tag2 = MathTex(r"x = +1", font_size=20, color=CYAN).next_to(axes.c2p(1, 0), UP, buff=0.25)

        self.play(Create(drop_neg1), Flash(pt_max, color=AMBER), FadeIn(coord_tag1), run_time=1.0)
        self.play(Create(drop_pos1), Flash(pt_min, color=CYAN), FadeIn(coord_tag2), run_time=1.0)

        verdict_card = VGroup(
            Text("Roots of f'(x) = 0 coincide with horizontal tangents:", font_size=15, color=MUTED_GRAY),
            MathTex(r"x_1 = -1 \quad (\text{Peak}), \quad x_2 = +1 \quad (\text{Trough})", font_size=20, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.15).next_to(eq4, DOWN, buff=0.45)

        self.play(FadeIn(verdict_card))
        self.wait(2.0)


class Scene3_SignChart(Scene):
    def construct(self):
        # 1. Title Banner
        title = Text("3. The First Derivative Test & Sign Chart", font_size=32, color=TEXT_WHITE)
        subtitle = Text("Translating derivative signs into local extrema", font_size=20, color=CYAN)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.15).to_edge(UP, buff=0.35)
        self.play(Write(title_group), run_time=1.0)

        # 2. Number Line
        num_line = NumberLine(
            x_range=[-3, 3, 1],
            length=10.0,
            color=AXES_GRAY,
            include_numbers=False,
            stroke_width=3
        ).shift(UP * 0.9)

        # Critical points on number line
        tick_neg1 = num_line.n2p(-1)
        tick_pos1 = num_line.n2p(1)

        dot_neg1 = Dot(tick_neg1, color=AMBER, radius=0.1)
        dot_pos1 = Dot(tick_pos1, color=CYAN, radius=0.1)

        label_neg1 = MathTex(r"x = -1", font_size=24, color=AMBER).next_to(dot_neg1, DOWN, buff=0.2)
        label_pos1 = MathTex(r"x = +1", font_size=24, color=CYAN).next_to(dot_pos1, DOWN, buff=0.2)
        fprime_zero1 = MathTex(r"f'=0", font_size=18, color=MUTED_GRAY).next_to(label_neg1, DOWN, buff=0.1)
        fprime_zero2 = MathTex(r"f'=0", font_size=18, color=MUTED_GRAY).next_to(label_pos1, DOWN, buff=0.1)

        self.play(Create(num_line), run_time=1.0)
        self.play(FadeIn(dot_neg1), FadeIn(dot_pos1), Write(label_neg1), Write(label_pos1), Write(fprime_zero1), Write(fprime_zero2))
        self.wait(0.5)

        # 3. Interval 1: x < -1 (centered at n2p(-2.0))
        region1 = Line(num_line.n2p(-3), num_line.n2p(-1), color=CYAN, stroke_width=6)
        center1 = num_line.n2p(-2.0)
        sign1 = MathTex(r"+", font_size=48, color=CYAN).move_to(center1 + UP * 0.45)
        arrow1 = MathTex(r"\nearrow", font_size=32, color=CYAN).next_to(sign1, UP, buff=0.12)
        test1 = Text("x = -2: f' = +9 > 0", font_size=15, color=MUTED_GRAY).move_to(center1 + DOWN * 0.8)

        self.play(Create(region1), FadeIn(sign1), FadeIn(arrow1), Write(test1), run_time=1.0)
        self.wait(0.6)

        # 4. Interval 2: -1 < x < 1 (centered at n2p(0.0))
        region2 = Line(num_line.n2p(-1), num_line.n2p(1), color=CORAL, stroke_width=6)
        center2 = num_line.n2p(0.0)
        sign2 = MathTex(r"-", font_size=48, color=CORAL).move_to(center2 + UP * 0.45)
        arrow2 = MathTex(r"\searrow", font_size=32, color=CORAL).next_to(sign2, UP, buff=0.12)
        test2 = Text("x = 0: f' = -3 < 0", font_size=15, color=MUTED_GRAY).move_to(center2 + DOWN * 0.8)

        self.play(Create(region2), FadeIn(sign2), FadeIn(arrow2), Write(test2), run_time=1.0)
        self.wait(0.6)

        # 5. Interval 3: x > 1 (centered at n2p(2.0))
        region3 = Line(num_line.n2p(1), num_line.n2p(3), color=CYAN, stroke_width=6)
        center3 = num_line.n2p(2.0)
        sign3 = MathTex(r"+", font_size=48, color=CYAN).move_to(center3 + UP * 0.45)
        arrow3 = MathTex(r"\nearrow", font_size=32, color=CYAN).next_to(sign3, UP, buff=0.12)
        test3 = Text("x = +2: f' = +9 > 0", font_size=15, color=MUTED_GRAY).move_to(center3 + DOWN * 0.8)

        self.play(Create(region3), FadeIn(sign3), FadeIn(arrow3), Write(test3), run_time=1.0)
        self.wait(0.8)

        # 6. Conclusion Cards at Bottom (cleanly separated)
        card_max = RoundedRectangle(
            corner_radius=0.15, width=5.2, height=1.7,
            fill_color="#111827", fill_opacity=0.9, stroke_color=AMBER, stroke_width=2
        ).shift(DOWN * 2.3 + LEFT * 3.1)
        
        card_max_text = VGroup(
            Text("Sign shifts: (+) to (-)", font_size=16, color=MUTED_GRAY),
            Text("LOCAL MAXIMUM", font_size=20, color=AMBER, weight=BOLD),
            MathTex(r"f(-1) = 2 \implies \mathbf{(-1, 2)}", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.12).move_to(card_max)

        card_min = RoundedRectangle(
            corner_radius=0.15, width=5.2, height=1.7,
            fill_color="#111827", fill_opacity=0.9, stroke_color=CYAN, stroke_width=2
        ).shift(DOWN * 2.3 + RIGHT * 3.1)
        
        card_min_text = VGroup(
            Text("Sign shifts: (-) to (+)", font_size=16, color=MUTED_GRAY),
            Text("LOCAL MINIMUM", font_size=20, color=CYAN, weight=BOLD),
            MathTex(r"f(1) = -2 \implies \mathbf{(1, -2)}", font_size=19, color=TEXT_WHITE)
        ).arrange(DOWN, buff=0.12).move_to(card_min)

        self.play(FadeIn(card_max), Write(card_max_text), run_time=1.0)
        self.play(FadeIn(card_min), Write(card_min_text), run_time=1.0)
        self.wait(2.0)
