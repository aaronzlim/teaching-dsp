from manim import *

from stem import Stem


class SamplingExample(Scene):
    """TODO: Docstring"""
    def construct(self):

        n = np.arange(-12, 13, 1)

        nl = NumberLine(
            x_range=[min(n), max(n), 1]
        )

        fx = lambda m: 3*np.cos(2*np.pi*(2/len(n))*m)

        ax = Axes(
            x_range=[min(n), max(n), 1],
            y_range=[-3, 3, 1],
        )
        xc = ax.plot(fx)
        points = xc.get_point_from_function(n)

        xd = VGroup(*[Stem(p, ax=ax) for p in zip(points[0], points[1])])

        self.play(Create(nl))
        self.wait()
        self.play(Create(xc))
        self.wait()
        self.play(Create(xd))
        self.wait()
        self.play(FadeOut(xc))
        self.wait(5)


class AliasExample(Scene):
    """TODO: Docstring"""
    def construct(self):

        n = np.arange(-4,5,1)

        nl1 = NumberLine(
            x_range=[min(n), max(n), 1],
            length=14
        )
        nl2 = nl1.copy()

        fx1 = lambda m: np.cos(2*np.pi*0.2*m)
        eq1 = Tex("$cos(2 \pi 0.2 n)$")
        fx2 = lambda m: np.cos(2*np.pi*1.2*m)
        eq2 = Tex("$cos(2\pi 1.2 n)$")

        ax = Axes(
            x_range=[min(n), max(n), 1],
            y_range=[-2, 2, 0.1],
            x_length=10,
            y_length=8
        )
        ax.center()

        x1 = ax.plot(fx1)
        points = x1.get_point_from_function(n)
        s1 = VGroup(*[Stem(p, ax=ax, color=BLUE) for p in zip(points[0], points[1])])
        x2 = ax.plot(fx2)
        points = x2.get_point_from_function(n)
        s2 = VGroup(*[Stem(p, ax=ax, color=BLUE) for p in zip(points[0], points[1])])

        eq1.next_to(s1, DOWN)
        eq2.next_to(s2, DOWN)

        self.play(Create(nl1), Create(x1), Write(eq1))
        self.wait()
        self.play(Create(s1))
        self.wait(2)
        self.play(FadeOut(x1))
        self.wait()

        self.play(nl1.animate.scale(0.5), s1.animate.scale(0.5))
        self.play(nl1.animate.move_to(2.5*UP), s1.animate.move_to(2.6*UP))
        self.play(eq1.animate.next_to(nl1, RIGHT))
        self.wait(2)

        self.play(Create(nl2), Create(x2), Write(eq2))
        self.wait()
        self.play(Create(s2))
        self.wait(2)
        self.play(FadeOut(x2))
        self.wait()

        self.play(nl2.animate.scale(0.5), s2.animate.scale(0.5))
        self.play(nl2.animate.move_to(2*DOWN), s2.animate.move_to(1.9*DOWN))
        self.play(eq2.animate.next_to(nl2, RIGHT))
        self.wait()

        self.play(FadeIn(Tex("$=$")), run_time=2)

        self.wait(5)


class QuantizationExample(Scene):
    """TODO: Docstring"""
    def construct(self):

        n = np.arange(-6, 6, 1)

        nl = NumberLine(
            x_range=[min(n), max(n), 1],
            length=13
        )

        x = 2*np.cos(2*np.pi*0.2*n)
        q = np.round(2*np.cos(2*np.pi*0.2*n))
        e = q - x

        sx = VGroup(*[Stem((x,y), color=WHITE) for x,y in zip(n,x)])
        sq = VGroup(*[Stem((x,y), color=BLUE) for x,y in zip(n,q)])
        se = VGroup(*[Stem((x,y), color=RED) for x,y in zip(n,e)])

        txt1 = Text("Quantize").next_to(nl, DOWN)

        self.play(Create(nl))
        self.wait()
        self.play(Create(sx))
        self.wait()
        self.play(Write(txt1))
        self.play(Create(sq))
        self.wait()
        self.play(FadeOut(txt1))
        self.wait()
        self.play(
            sx.animate.scale(0.3).move_to(4*RIGHT + 2*UP),
            sq.animate.scale(0.3).move_to(4*LEFT + 2*UP)
        )
        self.play(Write(Text("-").move_to(2*UP)))
        self.wait()
        self.play(Create(se))
        self.play(Write(Text("Error").next_to(nl, DOWN)))
        self.play(Write(Text("(Noise)").move_to(1.5*DOWN)))
        self.wait(10)

