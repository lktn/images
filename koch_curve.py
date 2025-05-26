from manim import *
config.pixel_height = 2700
config.pixel_width = 4800
class KochCurve(Scene):
    def construct(self):
        text = Tex("Koch Curve", font_size=50).move_to(-2.5*UP).set_color_by_gradient(PINK, BLUE)

        def Koch_Curve(l, n):
            if n == 0: return l
            
            p1 = l.get_start()
            p2 = l.copy().scale(1/3).get_start()
            p3 = l.copy().scale(1/3).get_end()
            p4 = l.get_end()

            l1 = l.copy().scale(1/3, about_point=p1)
            l2 = l.copy().scale(1/3).rotate(PI/3, about_point=p2)
            l3 = l.copy().scale(1/3).rotate(-PI/3, about_point=p3)
            l4 = l.copy().scale(1/3, about_point=p4)
            return VGroup(Koch_Curve(l1, n-1), Koch_Curve(l2, n-1), Koch_Curve(l3, n-1), Koch_Curve(l4, n-1))

        l = Line([-6, -1, 0], [6, -1, 0], stroke_width=0.8)
        n = 6
        self.add(text, Koch_Curve(l, n).set_color_by_gradient(PINK, BLUE))