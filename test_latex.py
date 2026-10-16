from manim import *

class TestLatex(Scene):
    def construct(self):
        eq = MathTex(r"f'(x) = 3x^2 - 3")
        self.add(eq)
        self.wait(0.5)
