from manim import *

class TestText(Scene):
    def construct(self):
        title = Text("Differential Calculus: Maxima & Minima", font_size=36, color=BLUE)
        eq = Text("f'(x) = 3x² − 3", font_size=40, color=YELLOW)
        eq.next_to(title, DOWN, buff=0.5)
        self.play(Write(title))
        self.play(FadeIn(eq))
        self.wait(1)
