from manim import *
import numpy as np

# Set global presentation colors
BG_COLOR = "#0B0F19"
CYAN_ACCENT = "#38BDF8"
AMBER_ACCENT = "#F59E0B"
CORAL_ACCENT = "#F43F5E"
GREEN_ACCENT = "#10B981"
MUTED_TEXT = "#94A3B8"

class NewtonCoolingPrototype(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # -------------------------------------------------------------
        # 1. Title Banner & Physical Setup
        # -------------------------------------------------------------
        title = Text("Newton's Law of Cooling", font_size=32, color=WHITE, weight=BOLD)
        subtitle = Text("Physical Modeling & Asymptotic Decay // Mathalino Problem 01", font_size=16, color=MUTED_TEXT)
        title_group = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        title_group.to_corner(UL, buff=0.5)
        self.play(FadeIn(title_group, shift=DOWN * 0.2), run_time=0.8)

        # -------------------------------------------------------------
        # 2. Vector Thermometer Construction (Left Side)
        # -------------------------------------------------------------
        thermo_group = VGroup()
        glass_stem = RoundedRectangle(corner_radius=0.18, height=3.8, width=0.36, stroke_color=WHITE, stroke_width=2.5, fill_color="#1E293B", fill_opacity=0.6)
        glass_stem.move_to([-4.8, -0.2, 0])
        
        bulb = Circle(radius=0.38, stroke_color=WHITE, stroke_width=2.5, fill_color=CORAL_ACCENT, fill_opacity=0.9)
        bulb.move_to(glass_stem.get_bottom() + DOWN * 0.15)

        # Ambient Air Environment Indicator
        ambient_box = RoundedRectangle(corner_radius=0.2, height=4.6, width=2.4, stroke_color=CYAN_ACCENT, stroke_width=1.5, stroke_opacity=0.5, fill_color="#0369A1", fill_opacity=0.12)
        ambient_box.move_to([-4.8, -0.3, 0])
        ambient_label = Text("Outside Air: Ts = 10°F", font_size=13, color=CYAN_ACCENT, weight=BOLD)
        ambient_label.next_to(ambient_box, UP, buff=0.15)

        # Mercury column driven by ValueTracker
        temp_tracker = ValueTracker(70.0) # Initial 70 deg F

        def get_mercury_level():
            # Maps 10F - 70F to height in stem
            val = temp_tracker.get_value()
            clamped = max(10.0, min(70.0, val))
            frac = (clamped - 10.0) / 60.0
            max_h = 3.2
            h = max(0.2, frac * max_h)
            m = Rectangle(width=0.22, height=h, fill_color=CORAL_ACCENT, fill_opacity=0.95, stroke_width=0)
            m.align_to(bulb.get_top() + DOWN * 0.1, DOWN)
            m.set_x(glass_stem.get_x())
            return m

        mercury_col = always_redraw(get_mercury_level)
        
        # Realtime temperature readout badge
        temp_badge = VGroup()
        temp_bg = RoundedRectangle(corner_radius=0.12, height=0.45, width=1.1, fill_color="#0F172A", fill_opacity=0.9, stroke_color=AMBER_ACCENT, stroke_width=1.5)
        temp_val_label = always_redraw(lambda: Text(f"{temp_tracker.get_value():.1f}°F", font_size=15, color=AMBER_ACCENT, weight=BOLD).move_to(temp_bg.get_center()))
        temp_badge = VGroup(temp_bg, temp_val_label)
        temp_badge.add_updater(lambda b: b.next_to(mercury_col, RIGHT, buff=0.2).align_to(mercury_col.get_top(), UP))

        thermo_group.add(glass_stem, bulb)

        self.play(
            FadeIn(ambient_box),
            FadeIn(ambient_label),
            FadeIn(thermo_group),
            FadeIn(mercury_col),
            FadeIn(temp_badge),
            run_time=1.0
        )

        # -------------------------------------------------------------
        # 3. Cooling Coordinate Plane & Asymptote (Right Side)
        # -------------------------------------------------------------
        axes = Axes(
            x_range=[0, 7.5, 1],
            y_range=[0, 80, 20],
            x_length=6.2,
            y_length=3.8,
            axis_config={"color": "#64748B", "stroke_width": 2, "include_numbers": False},
        ).to_corner(DR, buff=0.6).shift(UP * 0.2)

        # Axis tick labels
        x_label = Text("Time t (min)", font_size=14, color=MUTED_TEXT).next_to(axes.x_axis.get_end(), DOWN, buff=0.2).shift(LEFT * 0.6)
        y_label = Text("Temp T (°F)", font_size=14, color=MUTED_TEXT).next_to(axes.y_axis.get_end(), LEFT, buff=0.15).shift(UP * 0.1)

        # Explicit numeric tick markings
        x_ticks = VGroup(*[
            Text(str(i), font_size=12, color=MUTED_TEXT).next_to(axes.c2p(i, 0), DOWN, buff=0.12)
            for i in [1, 2, 3, 4, 5, 6, 7]
        ])
        y_ticks = VGroup(*[
            Text(str(j), font_size=12, color=MUTED_TEXT).next_to(axes.c2p(0, j), LEFT, buff=0.12)
            for j in [20, 40, 60, 80]
        ])

        # Ambient Asymptote Line (T = 10)
        asymptote_line = DashedLine(
            start=axes.c2p(0, 10),
            end=axes.c2p(7.2, 10),
            color=CYAN_ACCENT,
            stroke_width=2,
            dash_length=0.12
        )
        asymptote_text = MathTex(r"T_s = 10^\circ\text{F}\text{ (Ambient Asymptote)}", font_size=14, color=CYAN_ACCENT)
        asymptote_text.next_to(asymptote_line, UP, buff=0.08).shift(RIGHT * 1.5)

        self.play(
            Create(axes),
            Write(x_label), Write(y_label),
            FadeIn(x_ticks), FadeIn(y_ticks),
            Create(asymptote_line),
            FadeIn(asymptote_text),
            run_time=1.2
        )

        # -------------------------------------------------------------
        # 4. Animated Cooling Curve & Tracking Dot
        # Function: T(t) = 10 + 60*(0.25)**(t/3)
        # -------------------------------------------------------------
        def temp_func(t):
            return 10.0 + 60.0 * (0.25 ** (t / 3.0))

        curve = axes.plot(temp_func, x_range=[0, 6.0], color=CYAN_ACCENT, stroke_width=3.5)

        tracker_dot = Dot(color=AMBER_ACCENT, radius=0.08)
        tracker_dot.move_to(axes.c2p(0, 70))

        # Time marker
        time_tracker = ValueTracker(0.0)
        tracker_dot.add_updater(lambda d: d.move_to(axes.c2p(time_tracker.get_value(), temp_func(time_tracker.get_value()))))

        self.add(tracker_dot)

        # Animate cooling in tandem with thermometer and curve
        self.play(
            Create(curve),
            time_tracker.animate.set_value(6.0),
            temp_tracker.animate.set_value(13.75),
            run_time=3.5,
            rate_func=linear
        )
        tracker_dot.clear_updaters()

        # Key Observation Points
        dot_0 = Dot(axes.c2p(0, 70), color=WHITE, radius=0.07)
        label_0 = MathTex(r"(0,\,70^\circ)", font_size=15, color=WHITE).next_to(dot_0, UR, buff=0.1)

        dot_3 = Dot(axes.c2p(3, 25), color=CYAN_ACCENT, radius=0.07)
        label_3 = MathTex(r"(3,\,25^\circ)", font_size=15, color=CYAN_ACCENT).next_to(dot_3, UR, buff=0.1)

        dot_6 = Dot(axes.c2p(6, 13.75), color=AMBER_ACCENT, radius=0.09)
        label_6 = MathTex(r"(6,\,13.75^\circ\text{F})", font_size=16, color=AMBER_ACCENT).next_to(dot_6, UR, buff=0.12)

        self.play(
            FadeIn(dot_0), Write(label_0),
            FadeIn(dot_3), Write(label_3),
            FadeIn(dot_6), Write(label_6),
            run_time=1.0
        )

        # -------------------------------------------------------------
        # 5. Continuous Equation Morphing (Top Right / Center)
        # -------------------------------------------------------------
        eq1 = MathTex(r"\frac{dT}{dt} = -k(T - T_s)", font_size=24, color=WHITE)
        eq1.move_to([1.2, 2.8, 0])

        eq2 = MathTex(r"\frac{dT}{T - T_s} = -k\,dt", font_size=24, color=WHITE)
        eq2.move_to([1.2, 2.8, 0])

        eq3 = MathTex(r"\int \frac{dT}{T - T_s} = -k \int dt", font_size=24, color=CYAN_ACCENT)
        eq3.move_to([1.2, 2.8, 0])

        eq4 = MathTex(r"\ln(T - T_s) = -kt + \ln C", font_size=24, color=CYAN_ACCENT)
        eq4.move_to([1.2, 2.8, 0])

        eq5 = MathTex(r"T(t) = T_s + (T_0 - T_s)e^{-kt}", font_size=24, color=GREEN_ACCENT)
        eq5.move_to([1.2, 2.8, 0])

        eq6 = MathTex(r"T(t) = 10 + 60\left(\frac{1}{4}\right)^{t/3}", font_size=26, color=AMBER_ACCENT)
        eq6.move_to([1.2, 2.8, 0])

        # Step through equation transformations
        self.play(Write(eq1), run_time=0.8)
        self.wait(0.5)
        self.play(ReplacementTransform(eq1, eq2), run_time=0.8)
        self.wait(0.4)
        self.play(ReplacementTransform(eq2, eq3), run_time=0.8)
        self.wait(0.4)
        self.play(ReplacementTransform(eq3, eq4), run_time=0.8)
        self.wait(0.4)
        self.play(ReplacementTransform(eq4, eq5), run_time=0.9)
        self.wait(0.6)
        self.play(ReplacementTransform(eq5, eq6), run_time=1.0)
        self.wait(0.5)

        # -------------------------------------------------------------
        # 6. Final Result Callout Card (Teaching Pause Ready)
        # -------------------------------------------------------------
        result_card = RoundedRectangle(corner_radius=0.15, height=1.0, width=4.4, fill_color="#0F172A", fill_opacity=0.95, stroke_color=GREEN_ACCENT, stroke_width=2)
        result_card.move_to([1.2, 1.8, 0])
        result_text = MathTex(r"T(6) = 10 + 60\left(\frac{1}{4}\right)^2 = \mathbf{13.75^\circ\text{F}}", font_size=22, color=GREEN_ACCENT)
        result_text.move_to(result_card.get_center())

        self.play(FadeIn(result_card), Write(result_text), run_time=0.8)
        self.wait(2.0)
