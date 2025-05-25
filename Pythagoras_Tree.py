from manim import *
config.pixel_height = 2700*2
config.pixel_width = 4800*2
class PythagorasTree(Scene):
    def construct(self):
        text = Tex("Pythagoras Tree", font_size=50).move_to(-3.4*UP).set_color_by_gradient(PINK, BLUE)

        def pythagoras_tree(s, n, i):
            if n == 0: return VGroup()
            p1, p2, p3, p4 = s.get_vertices()
            z = [p1, p2, p3, p4]

            s1 = s.copy().scale(2**(-1/2), about_point=z[i % 4])
            s1.rotate(-3*PI/4, about_point=z[i % 4])

            s2 = s.copy().scale(2**(-1/2), about_point=z[(i+1) % 4])
            s2.rotate(3*PI/4, about_point=z[(i+1) % 4])
            return VGroup(s1, s2, pythagoras_tree(s1, n-1, i+1), pythagoras_tree(s2, n-1, i-1))

        s = Square(fill_color=GREEN, side_length=1.5, fill_opacity=1, stroke_width=0).move_to(-2*UP)

        self.add(text, VGroup(s, pythagoras_tree(s, 10, 0)).set_color_by_gradient(PINK, BLUE))