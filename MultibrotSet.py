from manim import *
config.pixel_height = 2880*2
config.pixel_width = 2880*2
class MultibrotSet(Scene):
    def construct(self):
        d = 7
        n = 500

        a = (d-1)*d**(d/(1-d))
        b = 2**(1/(d-1))
        m = 2*b/n
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
                x = i*m-b
                y = j*m-b
                if f(x, y, d, a, b):
                    g.append([x, y])
                    
        self.add(
            VGroup(*[Dot(point=[x, y, 0], radius=0.002) for x, y in g], Circle(radius=b)).scale(3.5), 
            MathTex(f"Area \\approx {16*len(g)/(n**2):.6f}", color=GREEN),
            )
