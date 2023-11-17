from manim import *


class IntroScene(Scene):
    def construct(self):
        course_code = Text("CMPS446", font_size=64)
        course_code.set_color_by_gradient(BLUE, PURPLE)
        course_title = Text("Image Processing and Computer Vision")
        prof_line = Text("Prof. Youssef Ghatas", color=BLUE)
        prof_line.set_color_by_gradient(BLUE, PURPLE)
        
        final_line = Text("Hope you like it too!")
        final_line.set_color_by_gradient(BLUE, PURPLE)
        
        course_code.next_to(ORIGIN, UP)
        course_title.next_to(course_code, DOWN)
        prof_line.next_to(course_title, DOWN)
        
        self.wait(1)
        self.play(Write(course_code), run_time=2)
        self.play(Write(course_title), run_time=2)
        self.play(Write(prof_line), run_time=2)
        self.wait(1.2)
        self.play(
            FadeOut(course_title), 
            FadeOut(prof_line), 
            ReplacementTransform(course_code, final_line)
        )
        self.wait(2)
        self.play(FadeOut(final_line))
        self.wait(1)
