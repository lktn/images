from manim import *
import numpy as np
import random
config.pixel_height = 2880
config.pixel_width = 1620
class trinagle_fractal(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        frame=self.camera.frame
        tri = Triangle(color=WHITE)
        for i in range(6):
            t = VGroup(*[tri.copy() for _ in range(3)])
            t[1].next_to(t[0], RIGHT, buff=0)
            new_t = VGroup(t[0], t[1])
            t[2].next_to(new_t, UP, buff=0)
            self.play(frame.animate.move_to(t.get_center()).set_height(t.get_height()*1.5), rate_func=linear)
            self.add(t)
            tri = t

class BarnsleyFern(Scene):
    def construct(self):
        x, y = 0, 0
        v = VGroup()
        for _ in range(200000):
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

            v.add(Dot(point=[a, b, 0], radius=0.005, color=PINK))
            x, y = a, b

        self.add(v.move_to(DOWN/2).scale(2))