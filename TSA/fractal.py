from manim import *

class FractalZoom(ZoomedScene):
    def construct(self):
        self.camera.background_color = BLACK
        zoom_target = Dot(point=ORIGIN)
        zoomed_display = self.zoomed_display

        self.add(zoom_target)
        self.activate_zooming()

        # Fake zooming in effect
        for _ in range(20):
            self.play(
                zoomed_display.scale, 1.5,
                run_time=0.5,
                rate_func=linear
            )

