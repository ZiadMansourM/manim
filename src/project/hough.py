from manim import *

class HoughTransformScene(Scene):
    def construct(self):
        # Create a 5x5 grid
        grid = VGroup(*[Square() for _ in range(25)]).arrange_in_grid(5, 5)
        grid.move_to(LEFT * 3)

        # Highlight the vertical line at column 4
        line = VGroup(*[grid[i] for i in range(3, 25, 5)])
        line.set_color(YELLOW)

        # Create accumulator space representation
        accumulator = Axes(
            x_range=[0, 10], y_range=[0, 10],
            x_length=5, y_length=5
        ).move_to(RIGHT * 3)

        # Animation for traversing the image and filling accumulator
        self.play(Create(grid), Create(accumulator))
        self.play(line.animate.set_fill(YELLOW, opacity=0.5))

        # Traverse each cell and update accumulator (simplified representation)
        for i, cell in enumerate(grid):
            self.play(cell.animate.set_fill(RED, opacity=0.5))
            if cell in line:
                # Update the accumulator space (example update)
                point = Dot(accumulator.c2p(i % 5, i // 5), color=RED)
                self.play(Create(point))
            self.play(cell.animate.set_fill(BLACK, opacity=0))

        self.wait(1)
