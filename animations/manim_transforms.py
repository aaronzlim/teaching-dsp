from manim import *

from stem import Stem


class SimpleTransforms(Scene):
    def construct(self):
        ax = Axes(
            x_range=(-6, 6, 1),
            y_range=(-3, 3, 1),
            x_length=12,
            y_length=6,
        )
        self.add(ax)
        self.add(Text("Simple Transforms").shift(4*LEFT + 3*UP))

        n = np.arange(*ax.x_range)
        func1 = lambda n: 2*np.sin(np.pi*0.8*n)/(np.pi*0.8*n) if n != 0 else 2
        func4 = lambda n: np.sin(np.pi*0.8*n)/(np.pi*0.8*n) if n != 0 else 1
        func5 = lambda n: 2.5*np.sin(np.pi*0.8*n)/(np.pi*0.8*n) if n != 0 else 2.5

        stem1 = Stem.from_function(func1, x=n, ax=ax)
        stem4 = Stem.from_function(func4, x=n, ax=ax)
        stem5 = Stem.from_function(func5, x=n, ax=ax)

        txt1 = Text("Function").move_to(2*UP + 3*RIGHT)
        txt2 = Text("Delay").move_to(2*UP + 3*RIGHT)
        txt3 = Text("Advance").move_to(2*UP + 3*RIGHT)
        txt4 = Text("Scale").move_to(2*UP + 3*RIGHT)

        eq1 = Tex("x(n)").next_to(txt1, DOWN)
        eq2 = Tex("x(n-k)").next_to(txt2, DOWN)
        eq3 = Tex("x(n+k)").next_to(txt3, DOWN)
        eq4 = Tex("$a \cdot x(n), a < 1$").next_to(txt4, DOWN)
        eq5 = Tex("$a \cdot x(n), a > 1$").next_to(txt4, DOWN)

        self.play(Create(stem1), Create(eq1), Create(txt1))
        self.wait(5)
        self.play(
            stem1.animate.shift(2*RIGHT),
            Transform(eq1, eq2),
            Transform(txt1, txt2)
        )
        self.wait(5)
        self.play(
            stem1.animate.shift(4*LEFT),
            Transform(eq1, eq3),
            Transform(txt1, txt3)
        )
        self.wait(5)
        self.play(
            Transform(stem1, stem4.shift(2*LEFT)),
            Transform(eq1, eq4),
            Transform(txt1, txt4)
        )
        self.wait(2)
        self.play(
            Transform(stem1, stem5.shift(2*LEFT)),
            Transform(eq1, eq5),
            Transform(txt1, txt4)
        )
        self.wait(3)
