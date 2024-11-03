from manim import *
import random
config.pixel_height = 1920
config.pixel_width = 1080
class Mandelbrot(Scene):
    def construct(self):
        def mandelbrot(c, max_iter):
            z = 0
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z**2 + c
                n += 1
            return n

        def check_point(x, y, max_iter=100):
            c = complex(x, y)
            return mandelbrot(c, max_iter)

        v = VGroup()
        for _ in range(1, 1000000):
            x = random.uniform(-2, 1)
            y = random.uniform(-1.5, 1.5)
            if check_point(x, y) == 100:
                v.add(Dot([x, y, 0]).scale(0.02))
                
        self.add(v.scale(3))

class Tetrahedral(ThreeDScene):
    def construct(self):
        a = [0, 0, 9]
        b = [0, 6, 0]
        c = [+3*np.sqrt(3), -3, 0]
        d = [-3*np.sqrt(3), -3, 0]
        a1 = Line(a, b)
        a2 = Line(a, c)
        a3 = Line(a, d)
        a4 = Line(b, c)
        a5 = Line(b, d)
        a6 = Line(c, d)
        self.set_camera_orientation(phi=65 * DEGREES, theta=-90 * DEGREES)
        self.add(a1, a2, a3, a4, a5, a6)

        v = [a, b, c, d]

        dot = Dot(point=ORIGIN, color=WHITE).scale(0.2)
        nhom = VGroup()
        for i in range(50000):
            n = random.choice(v)
            n1 = Dot(point=(dot.get_center()+n)/2, color=WHITE).scale(0.2)
            dot.become(n1)
            nhom.add(n1)

        self.add(nhom)

class Cube(Scene):
    def construct(self):
        r = RegularPolygon(n=9, color=WHITE).scale(6)
        p1, p2, p3, p4, p5, p6, p7, p8, p9 = r.get_vertices()

        a1 = [p1, p2]
        a2 = [p2, p3]
        a3 = [p3, p4]
        a4 = [p4, p5]
        a5 = [p5, p6]
        a6 = [p6, p7]
        a7 = [p7, p8]
        a8 = [p8, p9]
        a9 = [p9, p1]
        v  = [a1, a2, a3, a4, a5, a6, a7, a8, a9]

        dot = Dot(point=r.get_center(), color=WHITE).scale(0.05)
        nhom = VGroup()
        k = 3
        for i in range(200000):
            n = random.choice(v)
            n1 = Dot(point=(n[0] + n[1] + dot.get_center())/k, color=WHITE).scale(0.1)
            dot.become(n1)
            nhom.add(n1)

        self.add(nhom, r)

class Hexagon(Scene):
    def construct(self):
        r = RegularPolygon(n=6, color=WHITE).scale(6)
        self.add(r)

        p1, p2, p3, p4, p5, p6 = r.get_vertices()

        a1 = [p1, p2]
        a2 = [p2, p3]
        a3 = [p3, p4]
        a4 = [p4, p5]
        a5 = [p5, p6]
        a6 = [p1, p6]
        v = [a1, a2, a3, a4, a5, a6]

        dot = Dot(point=r.get_center(), color=WHITE).scale(0.05)
        nhom = VGroup()
        for i in range(10000):
            n = random.choice(v)
            n1 = Dot(point=(n[0] + n[1] + dot.get_center())/3, color=WHITE).scale(0.1)
            dot.become(n1)
            nhom.add(n1)

        self.play(Create(nhom), run_time=10)

class Square(Scene):
    def construct(self):
        square = Square(color=WHITE).scale(5)
        p1, p2, p3, p4 = square.get_vertices()
        self.add(square)
        p5 = Dot(point=[+0, +5, 0]).get_center()
        p6 = Dot(point=[+5, +0, 0]).get_center()
        p7 = Dot(point=[+0, -5, 0]).get_center()
        p8 = Dot(point=[-5, +0, 0]).get_center()
        vertices = [p1, p2, p3, p4, p5, p6, p7, p8]

        dot = Dot(point=square.get_center(), color=WHITE).scale(0.2)
        nhom = VGroup()
        for i in range(200000):
            n = random.choice(vertices)
            n1 = Dot(point=(dot.get_center()+2*n)/3, color=WHITE).scale(0.2)
            dot.become(n1)
            nhom.add(n1)

        self.add(nhom)

class Pentagon(Scene):
    def construct(self):
        pentagon = RegularPolygon(n=5, color=WHITE).scale(5)
        p1, p2, p3, p4, p5 = pentagon.get_vertices()
        self.add(pentagon)
        vertices = [p1, p2, p3, p4, p5]

        dot = Dot(point=pentagon.get_center(), color=WHITE).scale(0.05)
        nhom = VGroup()
        k = (5**0.5-1)/2
        for i in range(200000):
            n = random.choice(vertices)
            n1 = Dot(point=(dot.get_center() + k*(n-dot.get_center())), color=WHITE).scale(0.05)
            dot.become(n1)
            nhom.add(n1)

        self.add(nhom)
