from manim import *
config.pixel_height = 2700
config.pixel_width = 4800
class DragonCurve(Scene):
    def construct(self):
        def dragon_curve(l, n):
            if n == 0: return l
            p1 = l.get_start()
            p2 = l.get_end()
            l1 = l.copy().scale(2**(-0.5), about_point=p1).rotate(+PI/4, about_point=p1)
            l2 = l.copy().scale(2**(-0.5), about_point=p2).rotate(-PI/4, about_point=p2).rotate(PI)
            return VGroup(dragon_curve(l1, n-1), dragon_curve(l2, n-1))

        n = 16
        self.add(dragon_curve(Line([-3, 0, 0], [3, 0, 0], stroke_width=0.5), n).move_to(ORIGIN))