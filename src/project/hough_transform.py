from manim import *

from hough import (
    Intro,
    Transition,
    HoughTransformSceneOne,
    HoughTransformSceneTwo
)

class Main(Scene):
    def construct(self):
        # self.add_sound("/manim/assets/sounds/3b1b-eulerclock-cut.mp3", time_offset=0.2, gain=-20)
        Intro.construct(self)
        Transition.construct(self, "Example One")
        HoughTransformSceneOne.construct(self)
        Transition.construct(self, "Example Two")
        HoughTransformSceneTwo.construct(self)
        Transition.construct(self, "Thank You ^^")

class Dev(Scene):
    def construct(self):
        Intro.construct(self)
        Transition.construct(self, "Example Two")
        HoughTransformSceneTwo.construct(self)
        Transition.construct(self, "Thank You ^^")