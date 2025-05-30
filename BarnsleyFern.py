from manim import *
import random
config.pixel_height = 2880
config.pixel_width = 1620
class BarnsleyFern(Scene):
    def construct(self):
        x, y = 0, 0
        v = []
        for _ in range(100000):
            r = random.random()
            a, b = x, y
            if r < 0.01:
                x = +0
                y = +0.16 * b
            elif r < 0.86:
                x = +0.85 * a + 0.04 * b
                y = -0.04 * a + 0.85 * b + 1.6
            elif r < 0.93:
                x = +0.20 * a - 0.26 * b
                y = +0.23 * a + 0.22 * b + 1.6
            else:
                x = -0.15 * a + 0.28 * b
                y = +0.26 * a + 0.24 * b + 0.44

            v.append([x, y, 0])

        self.add(VGroup(*[Dot(point=i, radius=0.005, color=GREEN) for i in v]).scale(2).move_to(ORIGIN))
