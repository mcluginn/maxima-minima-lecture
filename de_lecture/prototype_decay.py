from manim import *
import numpy as np

# Global lecture palette
BG_COLOR = "#0B0F19"
CYAN_ACCENT = "#38BDF8"
AMBER_ACCENT = "#F59E0B"
CORAL_ACCENT = "#F43F5E"
GREEN_ACCENT = "#10B981"
MUTED_TEXT = "#94A3B8"

class RadioactiveDecayPrototype(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # -------------------------------------------------------------
        # 1. Title Banner
        # -------------------------------------------------------------
        title = Text("Simple Chemical Conversion & Radioactive Decay", font_size=30, color=WHITE, weight=BOLD)
        subtitle = Text("First-Order Kinetics & Half-Life Thresholds // Mathalino Problem 02", font_size=16, color=MUTED_TEXT)
        title_group = VGroup(title, subtitle).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        title_group.to_corner(UL, buff=0.5)
        self.play(FadeIn(title_group, shift=DOWN * 0.2), run_time=0.8)

        # -------------------------------------------------------------
        # 2. Physical Particle Chamber (Left Stage)
        # -------------------------------------------------------------
        chamber = RoundedRectangle(
            corner_radius=0.2, height=4.2, width=3.4,
            stroke_color=CYAN_ACCENT, stroke_width=2,
            fill_color="#0F172A", fill_opacity=0.85
        ).move_to([-4.4, -0.4, 0])

        chamber_label = Text("Radioactive Chamber: x(t)", font_size=13, color=CYAN_ACCENT, weight=BOLD)
        chamber_label.next_to(chamber, UP, buff=0.15)

        # Generate a lattice of radioactive nuclei dots
        np.random.seed(42)
        n_particles = 48
        particles = VGroup()
        for r in range(6):
            for c in range(8):
                cx = -5.7 + c * 0.38 + np.random.uniform(-0.06, 0.06)
                cy = -2.0 + r * 0.6 + np.random.uniform(-0.06, 0.06)
                p = Dot(point=[cx, cy, 0], radius=0.065, color=CYAN_ACCENT)
                particles.add(p)

        particle_counter = Text("Remaining: 100%", font_size=13, color=WHITE, weight=BOLD)
        particle_counter.next_to(chamber, DOWN, buff=0.18)

        self.play(
            FadeIn(chamber),
            FadeIn(chamber_label),
            FadeIn(particles),
            FadeIn(particle_counter),
            run_time=1.0
        )

        # -------------------------------------------------------------
        # 3. Decay Coordinate Axes (Right Stage)
        # -------------------------------------------------------------
        axes = Axes(
            x_range=[0, 150, 25],
            y_range=[0, 1.1, 0.2],
            x_length=6.2,
            y_length=3.8,
            axis_config={"color": "#64748B", "stroke_width": 2, "include_numbers": False},
        ).to_corner(DR, buff=0.6).shift(UP * 0.2)

        x_label = Text("Time t (hours)", font_size=14, color=MUTED_TEXT).next_to(axes.x_axis.get_end(), DOWN, buff=0.2).shift(LEFT * 0.6)
        y_label = Text("Fraction x / x₀", font_size=14, color=MUTED_TEXT).next_to(axes.y_axis.get_end(), LEFT, buff=0.15).shift(UP * 0.1)

        x_ticks = VGroup(*[
            Text(str(i), font_size=11, color=MUTED_TEXT).next_to(axes.c2p(i, 0), DOWN, buff=0.12)
            for i in [25, 50, 75, 100, 125, 150]
        ])
        y_ticks = VGroup(*[
            Text(f"{j:.1f}", font_size=11, color=MUTED_TEXT).next_to(axes.c2p(0, j), LEFT, buff=0.12)
            for j in [0.2, 0.4, 0.6, 0.8, 1.0]
        ])

        # 50% Half-Life Threshold Line (x = 0.5)
        half_line = DashedLine(
            start=axes.c2p(0, 0.5), end=axes.c2p(140, 0.5),
            color=GREEN_ACCENT, stroke_width=1.8, dash_length=0.1
        )
        half_text = MathTex(r"0.50\,x_0\text{ (50\% Half-Life)}", font_size=13, color=GREEN_ACCENT)
        half_text.next_to(half_line, UP, buff=0.06).shift(RIGHT * 1.0)

        # 10% Remaining Threshold Line (x = 0.1, 90% dissipated)
        dissip_line = DashedLine(
            start=axes.c2p(0, 0.1), end=axes.c2p(140, 0.1),
            color=AMBER_ACCENT, stroke_width=1.8, dash_length=0.1
        )
        dissip_text = MathTex(r"0.10\,x_0\text{ (90\% Dissipated Target)}", font_size=13, color=AMBER_ACCENT)
        dissip_text.next_to(dissip_line, UP, buff=0.06).shift(RIGHT * 1.5)

        self.play(
            Create(axes),
            Write(x_label), Write(y_label),
            FadeIn(x_ticks), FadeIn(y_ticks),
            Create(half_line), FadeIn(half_text),
            Create(dissip_line), FadeIn(dissip_text),
            run_time=1.2
        )

        # -------------------------------------------------------------
        # 4. Animated Exponential Curve & Particle Decay
        # Function: x(t) = x0 * (0.5)**(t/38)
        # -------------------------------------------------------------
        def decay_func(t):
            return 0.5 ** (t / 38.0)

        curve = axes.plot(decay_func, x_range=[0, 135], color=CYAN_ACCENT, stroke_width=3.5)
        tracker_dot = Dot(color=AMBER_ACCENT, radius=0.08)
        tracker_dot.move_to(axes.c2p(0, 1.0))

        time_tracker = ValueTracker(0.0)
        tracker_dot.add_updater(lambda d: d.move_to(axes.c2p(time_tracker.get_value(), decay_func(time_tracker.get_value()))))
        self.add(tracker_dot)

        # Particle fading animation in sync
        # As time approaches 126 hr, ~90% of particles fade to dark muted grey
        indices_to_decay = np.random.permutation(n_particles)
        halfway_idx = int(n_particles * 0.5)
        target_idx = int(n_particles * 0.9)

        decay_anims_1 = [particles[i].animate.set_color("#334155").set_opacity(0.3) for i in indices_to_decay[:halfway_idx]]
        decay_anims_2 = [particles[i].animate.set_color("#334155").set_opacity(0.3) for i in indices_to_decay[halfway_idx:target_idx]]

        # Phase 1: From t = 0 to t = 38 (Half-life)
        self.play(
            Create(axes.plot(decay_func, x_range=[0, 38], color=CYAN_ACCENT, stroke_width=3.5)),
            time_tracker.animate.set_value(38.0),
            *decay_anims_1,
            particle_counter.animate.become(Text("Remaining: 50%", font_size=13, color=GREEN_ACCENT, weight=BOLD).next_to(chamber, DOWN, buff=0.18)),
            run_time=2.5,
            rate_func=linear
        )

        # Half-life Milestone Dot & Label
        dot_half = Dot(axes.c2p(38, 0.5), color=GREEN_ACCENT, radius=0.08)
        label_half = MathTex(r"(38\,\text{hr},\,0.5x_0)", font_size=15, color=GREEN_ACCENT).next_to(dot_half, UR, buff=0.1)
        self.play(FadeIn(dot_half), Write(label_half), run_time=0.6)

        # Phase 2: From t = 38 to t = 126.23 (90% dissipated)
        self.play(
            Create(axes.plot(decay_func, x_range=[38, 126.23], color=CYAN_ACCENT, stroke_width=3.5)),
            time_tracker.animate.set_value(126.23),
            *decay_anims_2,
            particle_counter.animate.become(Text("Remaining: 10%", font_size=13, color=AMBER_ACCENT, weight=BOLD).next_to(chamber, DOWN, buff=0.18)),
            run_time=3.0,
            rate_func=linear
        )
        tracker_dot.clear_updaters()

        # 90% Target Dot & Label
        dot_target = Dot(axes.c2p(126.23, 0.1), color=AMBER_ACCENT, radius=0.09)
        label_target = MathTex(r"(126.23\,\text{hr},\,0.1x_0)", font_size=16, color=AMBER_ACCENT).next_to(dot_target, UR, buff=0.12)
        self.play(FadeIn(dot_target), Write(label_target), run_time=0.8)

        # -------------------------------------------------------------
        # 5. Continuous Equation Morphing
        # -------------------------------------------------------------
        eq1 = MathTex(r"\frac{dx}{dt} = -kx", font_size=24, color=WHITE)
        eq1.move_to([1.2, 2.8, 0])

        eq2 = MathTex(r"\frac{dx}{x} = -k\,dt", font_size=24, color=WHITE)
        eq2.move_to([1.2, 2.8, 0])

        eq3 = MathTex(r"\int \frac{dx}{x} = -k \int dt \implies x(t) = x_0 e^{-kt}", font_size=23, color=CYAN_ACCENT)
        eq3.move_to([1.2, 2.8, 0])

        eq4 = MathTex(r"x(t) = x_0 (0.5)^{t/38}", font_size=25, color=GREEN_ACCENT)
        eq4.move_to([1.2, 2.8, 0])

        eq5 = MathTex(r"0.1 x_0 = x_0 (0.5)^{t/38} \implies 0.1 = 0.5^{t/38}", font_size=23, color=AMBER_ACCENT)
        eq5.move_to([1.2, 2.8, 0])

        self.play(Write(eq1), run_time=0.7)
        self.wait(0.4)
        self.play(ReplacementTransform(eq1, eq2), run_time=0.7)
        self.wait(0.4)
        self.play(ReplacementTransform(eq2, eq3), run_time=0.8)
        self.wait(0.5)
        self.play(ReplacementTransform(eq3, eq4), run_time=0.8)
        self.wait(0.5)
        self.play(ReplacementTransform(eq4, eq5), run_time=0.9)
        self.wait(0.5)

        # -------------------------------------------------------------
        # 6. Final Result Callout Card
        # -------------------------------------------------------------
        result_card = RoundedRectangle(corner_radius=0.15, height=1.0, width=4.6, fill_color="#0F172A", fill_opacity=0.95, stroke_color=AMBER_ACCENT, stroke_width=2)
        result_card.move_to([1.2, 1.8, 0])
        result_text = MathTex(r"t = \frac{38 \ln 0.1}{\ln 0.5} \approx \mathbf{126.23~\text{hours}}", font_size=22, color=AMBER_ACCENT)
        result_text.move_to(result_card.get_center())

        self.play(FadeIn(result_card), Write(result_text), run_time=0.8)
        self.wait(2.0)
