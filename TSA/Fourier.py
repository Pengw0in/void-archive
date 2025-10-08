from manim import *
import numpy as np

class FourierEpicycles(Scene):
    def construct(self):
        path = [complex(np.cos(t) + 0.5*np.cos(3*t), np.sin(t) - 0.5*np.sin(3*t)) for t in np.linspace(0, TAU, 100)]
        n_vectors = 50
        dft = np.fft.fft(path)
        freqs = np.fft.fftfreq(len(path))
        components = sorted(zip(dft, freqs), key=lambda x: abs(x[0]), reverse=True)

        def epi(t):
            result = 0j
            for k in range(n_vectors):
                coeff, freq = components[k]
                result += coeff * np.exp(2j * PI * freq * t)
            return result / len(path)

        dots = [Dot() for _ in range(n_vectors)]
        circles = [Circle(radius=0.01, stroke_color=WHITE, stroke_width=1) for _ in range(n_vectors)]
        traces = TracedPath(dots[0].get_center, stroke_color=YELLOW, stroke_opacity=0.6)

        self.add(traces)

        def update_all(mob, dt):
            t = self.time / 4 % 1
            z = 0j
            for i, (coeff, freq) in enumerate(components[:n_vectors]):
                prev_z = z
                z += coeff * np.exp(2j * PI * freq * t) / len(path)
                dots[i].move_to([prev_z.real, prev_z.imag, 0])
                circles[i].move_to([prev_z.real, prev_z.imag, 0])
                circles[i].scale_to_fit_width(abs(coeff)/len(path))

        full_group = VGroup(*dots, *circles)
        full_group.add_updater(update_all)
        self.add(full_group)
        self.wait(10)

