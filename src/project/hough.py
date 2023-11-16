from manim import *

class HoughTransformScene(Scene):
    def construct(self):
        # Create a 5x5 grid, smaller and more to the left
        grid = VGroup(*[Square() for _ in range(25)]).arrange_in_grid(5, 5, buff=0.1)
        grid.scale(0.5).to_edge(LEFT, buff=1)

        # Highlight the other diagonal line
        diagonal = VGroup(*[grid[i] for i in range(4, 25, 4) if i != 24])
        diagonal.set_color(YELLOW)

        # Create accumulator space representation, higher and to the right
        accumulator = Axes(
            x_range=[0, 5], y_range=[0, 5],
            x_length=4, y_length=4,
            axis_config={"color": WHITE}
        ).to_edge(RIGHT, buff=1)
        accumulator_labels = accumulator.get_axis_labels(x_label='c', y_label='m')

        # Animation for traversing the image and filling accumulator
        self.play(Create(grid), Create(accumulator), Write(accumulator_labels))
        self.play(diagonal.animate.set_fill(YELLOW, opacity=0.5))

        # Traverse each cell and update accumulator (simplified representation)
        for i, cell in enumerate(grid):
            self.play(cell.animate.set_fill(RED, opacity=0.5), run_time=0.1)
            if cell in diagonal:
                # Update the accumulator space (example update)
                point = Dot(accumulator.c2p(0, 1), color=RED)
                self.play(Create(point), run_time=0.1)
            self.play(cell.animate.set_fill(BLACK, opacity=0), run_time=0.1)

        self.wait(1)
