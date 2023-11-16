from manim import *

from hough import (
    Intro,
    Transition,
    HoughTransformSceneOne
)

class Main(Scene):
    def construct(self):
        self.add_sound("/manim/assets/sounds/3b1b-eulerclock.mp3", time_offset=0.2, gain=-20)
        Intro.construct(self)
        Transition.construct(self, "Example One")
        HoughTransformSceneOne.construct(self)
        Transition.construct(self, "Thank You ^^")