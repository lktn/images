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
            if abs(c) > b:
                return False
            elif abs(c) < a:
                return True
            z = c
            for _ in range(100):
                z = z**d + c
                if abs(z) > 2:
                    return False
            return True

        g = []
        for i in range(n+1):
            for j in range(n+1):
                x = i*m-b
                y = j*m-b
                if f(x, y, d, a, b):
                    g.append([x, y])
                    
        self.add(VGroup(*[Dot(point=[x, y, 0], radius=0.002) for x, y in g], 
                Circle(radius=b, stroke_width=0.5, color=WHITE)).scale(3.5),
                MathTex(f"Area\\approx{4*b**2*len(g)/n**2:.10f}").move_to(-6*UP))
