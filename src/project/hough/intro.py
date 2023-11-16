from manim import *

class Intro(Scene):
    def construct(self):
        course_code = Text("CMPS446", font_size=64)
        course_code.set_color_by_gradient(BLUE, PURPLE)

        course_title = Text("Image Processing and Computer Vision")
        final_line = Text("By Prof. Youssef Ghatas", color=BLUE)
        color_final_line = Text("Hope you like it too!")

        color_final_line.set_color_by_gradient(BLUE, PURPLE)

        course_title.next_to(course_code, DOWN)

        self.wait(1)
        self.play(Write(course_code), run_time=2)
        self.play(Write(course_title), run_time=2)
        self.wait(1.2)
        self.play(FadeOut(course_title), ReplacementTransform(course_code, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)
        self.play(FadeOut(final_line))
        self.wait(1)
