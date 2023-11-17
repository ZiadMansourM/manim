from manim import *


def get_two_points_on_line(i):
    """Returns two points on the line represented by the cell at index i
    Args:
        - i (int): index of the cell
    Returns:
        - first_point (tuple[float, float]): (x, y) coordinates of the first point
        - second_point (tuple[float, float]): (x, y) coordinates of the second point
    """
    x_value = lambda val: val // 5
    y_value = lambda val: val % 5
    if x_value(i) != 0:
        m_value = lambda x, y, c: (y - c) / x
        first_point = (-4, m_value(x_value(i), y_value(i), -4))
        second_point = (4, m_value(x_value(i), y_value(i), 4))
    else:
        c_value = lambda x, y, m: y - m * x
        first_point = (c_value(x_value(i), y_value(i), -4), -4)
        second_point = (c_value(x_value(i), y_value(i), 4), 4)
    return first_point, second_point


class HoughTransformSceneOne(Scene):
    def construct(self):
        grid = VGroup(
            *[Square() for _ in range(25)]
        ).arrange_in_grid(5, 5, buff=0.1)
        grid.scale(0.5).to_edge(LEFT, buff=1)

        diagonal = VGroup(*[grid[i] for i in range(0, 25, 6)])
        diagonal.set_color(YELLOW)

        # Create accumulator space representation, higher and to the right
        accumulator = Axes(
            x_range=[-4, 5], y_range=[-4, 5],
            x_length=8, y_length=8,
            axis_config={"color": WHITE}
        ).scale(0.8).to_edge(RIGHT, buff=1)
        
        accumulator_labels = accumulator.get_axis_labels(x_label='c', y_label='m')

        # Animation for traversing the image and filling accumulator
        self.play(Create(grid), Create(accumulator), Write(accumulator_labels))
        self.play(diagonal.animate.set_fill(YELLOW, opacity=0.5))

        # Traverse each cell and update accumulator (simplified representation)
        for i, cell in enumerate(grid):
            self.play(cell.animate.set_fill(RED, opacity=0.5), run_time=0.1)
            if cell in diagonal:
                first_point, second_point = get_two_points_on_line(i)
                line = Line(
                    accumulator.c2p(first_point[0], first_point[1]),
                    accumulator.c2p(second_point[0], second_point[1]),
                    color=DARK_BLUE
                )
                self.play(Create(line), run_time=0.1)
            self.play(cell.animate.set_fill(BLACK, opacity=0), run_time=0.1)
        
        # Draw a blue dot at (0, 1)
        dot = Dot(accumulator.c2p(0, 1), color=RED)
        self.play(Create(dot))

        # Write text to the up right of the dot saying "m=1 & c=0"
        text = MathTex("m=1, \\ c=0", color=WHITE)
        text.next_to(dot, UR)
        red_box = SurroundingRectangle(text, color=RED)
        self.play(Create(red_box), Write(text))

        # wait for a bit
        self.wait(3)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )

        self.wait(1)


class HoughTransformSceneTwo(Scene):
    def construct(self):
        grid = VGroup(
            *[Square() for _ in range(25)]
        ).arrange_in_grid(5, 5, buff=0.1)
        grid.scale(0.5).to_edge(LEFT, buff=1)

        diagonal = VGroup(*[grid[i] for i in range(0, 25, 6)])
        diagonal.set_color(YELLOW)

        # Create accumulator space representation, higher and to the right
        accumulator = Axes(
            x_range=[-np.pi/2, np.pi/2, np.pi/18], 
            y_range=[-4, 5],
            x_length=8, 
            y_length=8,
            tips=False,
            axis_config={"color": WHITE}
        ).scale(0.8).to_edge(RIGHT, buff=1)
        
        accumulator_labels = accumulator.get_axis_labels(
            x_label=MathTex("\\theta"),
            y_label=MathTex("\\rho")
        )

        # Animation for traversing the image and filling accumulator
        self.play(Create(grid), Create(accumulator), Write(accumulator_labels))
        self.play(diagonal.animate.set_fill(YELLOW, opacity=0.5))

        # Traverse each cell and update accumulator (simplified representation)
        x_value = lambda val: val // 5
        y_value = lambda val: val % 5
        for i, cell in enumerate(grid):
            self.play(cell.animate.set_fill(RED, opacity=0.5), run_time=0.1)
            if cell in diagonal:
                y, x = x_value(i), y_value(i)
                curve = accumulator.plot(
                    lambda theta: x * np.cos(theta) + y * np.sin(theta), 
                    x_range=[-np.pi/2, np.pi/2, np.pi/18],
                    color=DARK_BLUE
                )
                self.play(Create(curve), run_time=0.1)
            self.play(cell.animate.set_fill(BLACK, opacity=0), run_time=0.1)

        # Draw a blue dot at (-np.pi/4, 0)
        dot = Dot(accumulator.c2p(-np.pi/4, 0), color=RED)
        self.play(Create(dot))

        text = MathTex("rho=0, \\ theta=-45", color=WHITE)
        text.to_edge(UP)

        red_box = SurroundingRectangle(text, color=RED)
        self.play(Create(red_box), Write(text))

        arrow = Arrow(red_box.get_bottom(), dot.get_top(), buff=0.1, color=RED)
        self.play(GrowArrow(arrow))

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )

        self.wait(1)
