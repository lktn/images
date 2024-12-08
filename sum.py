from manim import *
import random
config.pixel_height = 2880*2
config.pixel_width = 2880*2
class Pi(Scene):
    def construct(self):
        a = Square().scale(3)
        b = Circle().scale(3)
        vg = []
        vr = []
        n = 500
        #for i in range(1, n):
            #x = random.uniform(-3, 3)
            #y = random.uniform(-3, 3)
            #if np.sqrt(x**2+y**2) <= 3:
            #    vg.add(Dot([x, y, 0], color=BLUE).scale(0.1))
            #else:
            #    vr.add(Dot([x, y, 0], color=RED).scale(0.1))
        for i in range(0, n+1):
            for j in range(0, n+1):
                x = -3 + 6*i/n
                y = -3 + 6*j/n
                if np.sqrt(x**2+y**2) <= 3:
                    vg.append([x, y])
                else:
                    vr.append([x, y])

        self.add(
            VGroup(*[Dot(point=[x, y, 0], radius=0.01, color=BLUE) for x, y in vg]),
            VGroup(*[Dot(point=[x, y, 0], radius=0.01, color=RED) for x, y in vr]),
            MathTex(f"\\pi \\approx {4*len(vg)/n**2:.10f}")
            )

class MultibrotSet(Scene):
    def construct(self):
        d = 5
        n = 1000

        m = 4/n
        a = (d-1)*d**(d/(1-d))
        b = 2**(1/(d-1))
        def f(x, y, d, a, b):
            c = complex(x, y)
            z = c
            s = abs(z)
            if s > b:
                return False
            elif s < a:
                return True
            for i in range(1, 100):
                z = z**d + c
                if abs(z) > 2:
                    return False
            return True

        g = []
        for i in range(0, n+1):
            for j in range(0, n+1):
                x = i*m-2
                y = j*m-2
                if f(x, y, d, a, b):
                    g.append([x, y])
                    
        self.add(
            VGroup(*[Dot(point=[x, y, 0], radius=0.002) for x, y in g], Circle(radius=b)).scale(4), 
            MathTex(f"Area \\approx {16*len(g)/(n**2):.6f}", color=GREEN),
            )

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