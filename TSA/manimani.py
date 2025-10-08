from manim import *

class SpiralTrance(Scene):
    def construct(self):
        squares = VGroup()
        colors = color_gradient([BLUE, PURPLE, RED, ORANGE, YELLOW], 50)

        for i in range(50):
            s = Square(side_length=0.5 + i * 0.05)
            s.set_stroke(color=colors[i], width=2)
            s.rotate(i * 0.1)
            s.move_to(ORIGIN)
            squares.add(s)

        self.play(Create(squares), run_time=2)
        self.wait(0.5)

        self.play(
            squares.animate.arrange_in_grid(rows=1).scale(0.5),
            run_time=2
        )

        squares.generate_target()
        for i, sq in enumerate(squares.target):
            sq.scale(2)
            sq.rotate(PI / 4 * i)
            sq.set_color(colors[-(i % len(colors))])

        self.play(MoveToTarget(squares), run_time=3)
        self.wait(1)

        self.play(Rotate(squares, angle=4*PI), run_time=5)
        self.wait()
