from manim import *

class MobiusTransformation(Scene):
    def construct(self):
        grid = ComplexPlane().add_coordinates()
        self.play(Create(grid))

        func = lambda z: (z - 1) / (z + 1)

        dot = Dot(grid.n2p(0.5 + 0.5j), color=RED)
        self.add(dot)

        def update_dot(mob, dt):
            t = self.time / 4
            z = np.exp(2 * PI * 1j * t)
            fz = func(z)
            mob.move_to(grid.n2p(fz))

        dot.add_updater(update_dot)
        self.wait(8)

