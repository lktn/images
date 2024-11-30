from manim import *
import numpy as np
import random
config.pixel_height = 2880
config.pixel_width = 1620
class BarnsleyFern(Scene):
    def construct(self):
        x, y = 0, 0
        v = []
        for _ in range(500000):
            r = random.random()
            if r < 0.01:
                a = +0
                b = +0.16*y
            elif r < 0.86:
                a = +0.85*x + 0.04*y
                b = -0.04*x + 0.85*y + 1.6
            elif r < 0.93:
                a = +0.20*x - 0.26*y
                b = +0.23*x + 0.22*y + 1.6
            else:
                a = -0.15*x + 0.28*y
                b = +0.26*x + 0.24*y + 0.44

            x, y = a, b
            v.append([a, b])

        self.add(VGroup(*[Dot(point=[x, y, 0], radius=0.004, color=GREEN) for x, y in v]).scale(2).move_to(DOWN/2))
