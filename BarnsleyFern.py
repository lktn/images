from manim import *
import numpy as np
import random
config.pixel_height = 2880
config.pixel_width = 1620
class BarnsleyFern(Scene):
    def construct(self):
        x, y = 0, 0
        v = []
        for _ in range(100000):
            r = random.random()
            if r < 0.01:
                x = +0
                y = +0.16*y
            elif r < 0.86:
                x = +0.85*x + 0.04*y
                y = -0.04*x + 0.85*y + 1.6
            elif r < 0.93:
                x = +0.20*x - 0.26*y
                y = +0.23*x + 0.22*y + 1.6
            else:
                x = -0.15*x + 0.28*y
                y = +0.26*x + 0.24*y + 0.44

            v.append([x, y])

        self.add(VGroup(*[Dot(point=[x, y, 0], radius=0.005, color=GREEN) for x, y in v]).scale(2).move_to(DOWN/2))
