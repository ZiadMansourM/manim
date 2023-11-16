from manim import *

class HoughTransformScene(Scene):
    def construct(self):
        # Create a 5x5 grid, smaller and more to the left
        grid = VGroup(*[Square() for _ in range(25)]).arrange_in_grid(5, 5, buff=0.1)
        grid.scale(0.5).to_edge(LEFT, buff=1)

        # Highlight the vertical line at column 4
        line = VGroup(*[grid[i] for i in range(3, 25, 5)])
        line.set_color(YELLOW)

        # Create accumulator space representation, higher and to the right
        accumulator = Axes(
            x_range=[0, 10], y_range=[0, 10],
            x_length=4, y_length=4
        ).to_edge(RIGHT, buff=1).shift(UP * 1.5)

        # Animation for traversing the image and filling accumulator
        self.play(Create(grid), Create(accumulator))
        self.play(line.animate.set_fill(YELLOW, opacity=0.5))

        # Traverse each cell and update accumulator (simplified representation)
        for i, cell in enumerate(grid):
            self.play(cell.animate.set_fill(RED, opacity=0.5), run_time=0.1)
            if cell in line:
                # Update the accumulator space (example update)
                point = Dot(accumulator.c2p(i % 5, i // 5), color=RED)
                self.play(Create(point), run_time=0.1)
            self.play(cell.animate.set_fill(BLACK, opacity=0), run_time=0.1)

        self.wait(1)
