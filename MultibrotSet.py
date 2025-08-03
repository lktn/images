from manim import *
import numpy as np
config.pixel_height = 5760
config.pixel_width = 5760
class MultibrotSet(Scene):
    def construct(self):
        d = 7
        n = 500

        a = (d-1)*d**(d/(1-d))
        b = 2**(1/(d-1))
        m = 2*b/n
        def f(c, d, a, b):
            if abs(c) < a: return True
            z = c
            for _ in range(100):
                if abs(z) > b: return False
                z = z**d + c
            return True

        g = [
            Dot(point=[x, y, 0], radius=0.002) 
            for x in np.linspace(-b, b, n)
            for y in np.linspace(-b, b, n)
            if f(complex(x, y), d, a, b)
        ]

        self.add(
            VGroup(*g, Circle(radius=b, stroke_width=0.5, color=WHITE)).scale(3.5),
            MathTex(f"Area\\approx{4*b**2*len(g)/n**2:.10f}").move_to(-6*UP)
        )
