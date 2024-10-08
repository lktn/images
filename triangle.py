from manim import *
import random

config.pixel_height = 1920
config.pixel_width = 1080
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
        #self.move_camera(phi=65 * DEGREES, theta=270*DEGREES, run_time=15, rate_func=linear)

class Thoi(Scene):
    def construct(self):
        t = MathTable([
            [r".",     r"Thứ 2",   r"Thứ 3",     r"Thứ 4",    r"Thứ 5",      r"Thứ 6",     r"Thứ 7"],
            [r"1",     r"CC-HDTN", r"Hoá Học",   r"Toán Học", r"Thể Dục",    r"Ngoại ngữ", r"Văn Học"],
            [r"2",     r"Lịch Sử", r"Toán Học",  r"Toán Học", r"Quốc Phòng", r"Thể Dục",   r"Văn Học"],
            [r"3",     r"Văn Học", r"Toán Học",  r"Tin Học",  r".",          r"Hóa Học",   r"Hoá Học"],
            [r"4",     r"GDKT&PL", r"Ngoại Ngữ", r"HDTN",     r".",          r"Tin Học",   r"Ngoại Ngữ"],
            [r"5",     r"Vật Lý",  r"Vật Lý",    r"Vật Lý",   r".",          r"GDKT&PL",   r"HDTN"]
        ], include_outer_lines=True, element_to_mobject=lambda e: Text(e, font="Arial")).scale(0.5)
        for cell in t.get_entries():
            cell.set(font_size=30)
        self.add(t)

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

class zeta(ThreeDScene):
    def construct(self):
        a = 1.3#0105
        a1 = MathTex(r"\zeta(s)=\sum_{n=1}^\infty\frac{1}{n^s}").move_to(2*a*UP)
        a2 = MathTex(r"\Re(s)> 1").move_to(3*a*UP)
        a3 = MathTex(r"\zeta(s)=1+\frac{1}{2^s}+\frac{1}{3^s}+\frac{1}{4^s}+\cdots").move_to(a*UP)
        a4 = MathTex(r"\Re(s)\le 0")
        a5 = MathTex(r"\Gamma(s)=\int_0^\infty e^{-t}t^{s-1}dt")
        a6 = MathTex(r"t=nx")
        a7 = MathTex(r"\Gamma(s)=\int_0^\infty e^{-nx}(nx)^{s-1}ndx")
        a8 = MathTex(r"\Gamma(s)=\int_0^\infty e^{-nx}x^{s-1}n^{s-1}ndx")
        a9 = MathTex(r"\Gamma(s)=\int_0^\infty e^{-nx}x^{s-1}n^sdx")
        a10 = MathTex(r"\Gamma(s)=n^s\int_0^\infty e^{-nx}x^{s-1}dx")
        a11 = MathTex(r"\Gamma(s)n^{-s}=\int_0^\infty e^{-nx}x^{s-1}dx")
        a12 = MathTex(r"\Gamma(s)\sum_{n=1}^\infty n^{-s}=\int_0^\infty\sum_{n=1}^\infty e^{-nx}x^{s-1}dx")
        a13 = MathTex(r"\Gamma(s)\sum_{n=1}^\infty n^{-s}=\int_0^\infty x^{s-1}\sum_{n=1}^\infty e^{-nx}dx")
        a14 = MathTex(r"\sum_{n=1}^\infty e^{-nx}=e^{-x}+e^{-2x}+e^{-3x}+\cdots")
        a15 = MathTex(r"\Gamma(s)\sum_{n=1}^\infty n^{-s}=\int_0^\infty x^{s-1}Sdx")
        a16 = MathTex(r"S=e^{-x}+e^{-2x}+e^{-3x}+\cdots")
        a17 = MathTex(r"e^xS=1+e^{-x}+e^{-2x}+\cdots")
        a18 = MathTex(r"e^xS=1+S")
        a19 = MathTex(r"e^x=\frac{1}{S}+1")
        a20 = MathTex(r"e^x-1=\frac{1}{S}")
        a21 = MathTex(r"\frac{1}{e^x-1}=S")
        a22 = MathTex(r"\Gamma(s)\sum_{n=1}^\infty n^{-s}=\int_0^\infty\frac{x^{s-1}}{e^x-1}dx")
        a23 = MathTex(r"\Gamma(s)\zeta(s)=\int_0^\infty\frac{x^{s-1}}{e^x-1}dx")
        a24 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=\int_\infty^0\frac{(-x)^{s-1}}{e^x-1}dx+\int_0^\infty\frac{(-x)^{s-1}}{e^x-1}dx").scale(0.8)
        a25 = MathTex(r"\int_0^\infty\frac{(-x)^{s-1}}{e^x-1}dx=\int_0^\infty\frac{(-xe^{2\pi i})^s}{e^x-1}\frac{dx}{-x}")
        a26 = MathTex(r"\int_0^\infty\frac{(-x)^{s-1}}{e^x-1}=\int_0^\infty\frac{e^{\pi si}(-xe^{\pi i})^s}{e^x-1}\frac{dx}{-x}")
        a27 = MathTex(r"\int_0^\infty\frac{(-x)^{s-1}}{e^x-1}=\int_0^\infty\frac{e^{\pi si}x^s}{e^x-1}\frac{dx}{-x}")
        a28 = MathTex(r"\int_0^\infty\frac{(-x)^s}{e^x-1}=-e^{\pi i(s)}\int_0^\infty\frac{x^s}{e^x-1}\frac{dx}x")
        a29 = MathTex(r"\int_0^\infty\frac{(-x)^s}{e^x-1}=-e^{\pi si}\int_0^\infty\frac{x^{s-1}}{e^x-1}dx")
        a30 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=\int_\infty^0\frac{(-x)^{s-1}}{e^x-1}dx-e^{\pi si}\int_0^\infty\frac{x^{s-1}}{e^x-1}dx")
        a31 = MathTex(r"\int_\infty^0\frac{(-x)^{s-1}}{e^x-1}dx=\int_\infty^0\frac{(-xe^{-2\pi i})^s}{e^x-1}\frac{dx}{-x}")
        a32 = MathTex(r"\int_\infty^0\frac{(-x)^{s-1}}{e^x-1}=\int_\infty^0\frac{e^{-\pi si}(-xe^{-\pi i})^s}{e^x-1}\frac{dx}{-x}")
        a33 = MathTex(r"\int_\infty^0\frac{(-x)^{s-1}}{e^x-1}=\int_\infty^0\frac{e^{-\pi si}x^s}{e^x-1}\frac{dx}{-x}")
        a34 = MathTex(r"\int_\infty^0\frac{(-x)^s}{e^x-1}=-e^{-\pi si}\int_\infty^0\frac{x^s}{e^x-1}\frac{dx}x")
        a35 = MathTex(r"\int_\infty^0\frac{(-x)^s}{e^x-1}=-e^{-\pi si}\int_\infty^0\frac{x^{s-1}}{e^x-1}dx")
        a36 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=-e^{-\pi si}\int_\infty^0\frac{x^{s-1}}{e^x-1}dx-e^{\pi si}\int_0^\infty\frac{x^{s-1}}{e^x-1}dx").scale(0.8)
        a37 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=(e^{-\pi si}-e^{\pi si})\int_0^\infty\frac{x^{s-1}}{e^x-1}dx")
        a38 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=-2i\sin\pi s\int_0^\infty\frac{x^{s-1}}{e^x-1}dx")
        a39 = MathTex(r"\Gamma(s)\zeta(s)=-\frac{1}{2i\sin\pi s}\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx")
        a40 = MathTex(r"2\sin\pi s\Gamma(s)\zeta(s)=i\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx")
        a41 = MathTex(r"\int_Cf(z)dz=-2\pi i\sum\text{Res}(f(z))")
        a42 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=-2\pi i\sum\text{Res}\left(\frac{(-x)^{s-1}}{e^x-1}\right)")
        a43 = MathTex(r"\text{Res}\left(\frac{(-x)^{s-1}}{e^x-1}\right)=\lim_{z\to 2n\pi i}(z-2n\pi i)\frac{(-z)^{s-1}}{e^z-1}")
        a44 = MathTex(r"\text{Res}\left(\frac{(-x)^{s-1}}{e^x-1}\right)=(-2n\pi i)^{s-1}\lim_{z\to 2n\pi i}\frac{(z-2n\pi i)}{e^z-1}")
        a45 = MathTex(r"\text{Res}\left(\frac{(-x)^{s-1}}{e^x-1}\right)=(-2n\pi i)^{s-1}")
        a46 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=-2\pi i\sum(-2n\pi i)^{s-1}")
        a47 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=-2\pi i\left(\sum_{n=1}^\infty(-2n\pi i)^{s-1}+\sum_{n=1}^\infty(2n\pi i)^{s-1}\right)")
        a48 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=(-2\pi i)(2\pi)^{s-1}\left(\sum_{n=1}^\infty(-ni)^{s-1}+\sum_{n=1}^\infty(ni)^{s-1}\right)")
        a49 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=(-2\pi i)(2\pi)^{s-1}\left((-i)^{s-1}\sum_{n=1}^\infty n^{s-1}+i^{s-1}\sum_{n=1}^\infty n^{s-1}\right)").scale(0.8)
        a50 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=(-2\pi i)(2\pi)^{s-1}\left((-i)^{s-1}+i^{s-1}\right)\sum_{n=1}^\infty n^{s-1}")
        a51 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=(-2\pi i)(2\pi)^{s-1}\left((-i)^{s-1}+i^{s-1}\right)\zeta(1-s)")
        a52 = MathTex(r"\int_\infty^\infty\frac{(-x)^{s-1}}{e^x-1}dx=(-i)(2\pi)^s2\sin\frac{\pi s}2\zeta(1-s)")
        a53 = MathTex(r"2\sin\pi s\Gamma(s)\zeta(s)=i(-i)(2\pi)^s2\sin\frac{\pi s}2\zeta(1-s)")
        a54 = MathTex(r"\sin\pi s\Gamma(s)\zeta(s)=(2\pi)^s\sin\frac{\pi s}2\zeta(1-s)")
        a55 = MathTex(r"\Gamma(s)\Gamma(1-s)=\frac\pi{\sin\pi s}")
        a56 = MathTex(r"\sin\pi s\Gamma(s)\Gamma(1-s)\zeta(s)=(2\pi)^s\sin\frac{\pi s}2\Gamma(1-s)\zeta(1-s)")
        a57 = MathTex(r"\pi\zeta(s)=(2\pi)^s\sin\frac{\pi s}2\Gamma(1-s)\zeta(1-s)")
        a58 = MathTex(r"\zeta(s)=2^s\pi^{s-1}\sin\frac{\pi s}2\Gamma(1-s)\zeta(1-s)")
        f1 = VGroup(a5, a7, a8, a9, a10, a11, a12, a13, a15, a22, a23, a39, a40, a53, a54, a56, a57, a58).move_to(-a*UP)
        f2 = VGroup(a6, a14, a16, a17, a18, a19, a20, a21, a24, a30, a36, a37, a38, a41, a42, a46, a47, a48, a49, a50, a51, a52, a55).move_to(-2*a*UP)
        f3 = VGroup(a25, a26, a27, a28, a29, a31, a32, a33, a34, a35, a43, a44, a45).move_to(-3*a*UP)
        self.play(Write(a1))
        self.play(Write(a2))
        self.play(Write(a3))
        self.play(Write(a4))
        self.play(Write(a5))
        self.play(Write(a6))
        for t in [a7, a8, a9, a10, a11, a12, a13]:
            self.play(Transform(VGroup(a5, a6), t))
        self.play(Write(a14))
        self.play(ReplacementTransform(a14, a16), ReplacementTransform(VGroup(a5, a6), a15))
        for t in [a17, a18, a19, a20, a21]:
            self.play(Transform(a16, t))
        self.play(ReplacementTransform(VGroup(a16, a15), a22))
        self.play(ReplacementTransform(a22, a23))
        self.play(Write(a24))
        self.play(Write(a25))
        for t in [a26, a27, a28, a29]:
            self.play(Transform(a25, t))
        self.play(ReplacementTransform(VGroup(a25, a24), a30))
        self.play(Write(a31))
        for t in [a32, a33, a34, a35]:
            self.play(Transform(a31, t))
        self.play(ReplacementTransform(VGroup(a31, a30), a36))
        for t in [a37, a38]:
            self.play(Transform(a36, t))
        self.play(ReplacementTransform(VGroup(a36, a23), a39))
        self.play(ReplacementTransform(a39, a40))
        self.play(Write(a41))
        self.play(ReplacementTransform(a41, a42))
        self.play(Write(a43))
        for t in [a44, a45]:
            self.play(Transform(a43, t))
        self.play(ReplacementTransform(VGroup(a42, a43), a46))
        for t in [a47, a48, a49, a50, a51, a52]:
            self.play(Transform(a46, t))
        self.play(ReplacementTransform(VGroup(a40, a46), a53))
        self.play(ReplacementTransform(a53, a54))
        self.play(Write(a55))
        self.play(ReplacementTransform(VGroup(a54, a55), a56))
        for t in [a57, a58]:
            self.play(Transform(a56, t))

class hinhthang(Scene):
    def construct(self):
        a = [-1-1.25,  +1.5,0]
        b = [+1-1.25,  +1.5,0]
        c = [+2.5-1.25,-1.5,0]
        d = [-2-1.25,  -1.5,0]
        e = [1.75-1.25, 0,  0]
        a1 = Polygon(a, e, c, d, color=BLUE, fill_opacity=1, stroke_width=0)
        a2 = Polygon(a, b, e, color=BLUE, fill_opacity=1, stroke_width=0)
        self.play(GrowFromCenter(VGroup(a1, a2)))

        a3 = BraceBetweenPoints(a, b, UP)
        a4 = MathTex("a").next_to(a3, UP, buff=0.15).scale(1.2)
        a5 = Brace(a1, -UP)
        a6 = MathTex("b").next_to(a5, -UP, buff=0.15).scale(1.2)
        self.play(FadeIn(VGroup(a3, a4), shift=-UP))
        self.play(FadeIn(VGroup(a5, a6), shift=UP))
        self.play(Rotate(a2, angle=-PI, about_point=e, run_time=2), FadeOut(VGroup(a3, a4)))
        self.wait()

        a7 = Brace(VGroup(a1, a2), -UP)
        a8 = MathTex("a+b").next_to(a7, -UP, buff=0.15).scale(1.2)
        self.play(Transform(VGroup(a5, a6), VGroup(a7, a8)))

        a9 = Brace(VGroup(a1, a2), LEFT)
        a10 = MathTex("h").next_to(a9, LEFT, buff=0.15).scale(1.2)
        a11 = dashed_line = DashedLine(a, [-2-1.25, 1.5, 0], dash_length=0.07, dashed_ratio=0.3)
        self.play(FadeIn(VGroup(a9, a10), shift=-LEFT), Write(a11))

        a12 = MathTex(r"Area=\frac{1}{2}", "h", "(a+b)").move_to(-4*UP).scale(1.2)
        self.play(Write(a12[0]))
        self.play(TransformFromCopy(a10, a12[1]))
        self.play(Transform(a8, a12[2]))
        self.play(Circumscribe(a12))
        self.wait()