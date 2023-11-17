from manim import *


class TransitionScene(Scene):
    def construct(self, text: str):
        transition_screen = Text(text, font_size=56, color=BLUE)
        self.play(Write(transition_screen), run_time=2)
        self.wait(2)
        self.play(FadeOut(transition_screen))
