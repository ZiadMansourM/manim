from manim import *

from hough_transform_utils import (
    HoughTransformSceneOne,
    HoughTransformSceneTwo
)
from intro import IntroScene
from transition import TransitionScene


class Main(Scene):
    def construct(self):
        # self.add_sound(
        #     "/manim/assets/sounds/3b1b-eulerclock-cut.mp3", 
        #     time_offset=0.2, 
        #     gain=-20
        # )
        IntroScene.construct(self)
        TransitionScene.construct(self, "Example One")
        HoughTransformSceneOne.construct(self)
        TransitionScene.construct(self, "Example Two")
        HoughTransformSceneTwo.construct(self)
        TransitionScene.construct(self, "Thank You ^^")


class Dev(Scene):
    def construct(self):
        IntroScene.construct(self)
        TransitionScene.construct(self, "Example Two")
        HoughTransformSceneTwo.construct(self)
        TransitionScene.construct(self, "Thank You ^^")
