from manim import *

from stem import Stem


class ContinuousTimeSignalExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        ax = Axes(
            x_range=[-10, 9, 1],
            y_range=[-1, 1, 0.1],
        )
        ax.set_color(BLACK)
        curve = ax.plot(lambda t: np.sin(2*np.pi*0.05*t), color=BLACK)
        self.add(ax, curve)


class DiscreteTimeSignalExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        ax = Axes(
            x_range=[-10, 9, 1],
            y_range=[-1, 1, 0.1],
        )
        ax.set_color(BLACK)
        curve = ax.plot(lambda t: np.sin(2*np.pi*0.05*t), color=BLACK)
        points = curve.get_point_from_function(np.arange(-10,9,1))
        stem = VGroup(*[Stem(p, ax=ax, color=BLACK) for p in zip(points[0], points[1])])
        self.add(ax, stem)


class DiscreteValueSignalExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        ax = Axes(
            x_range=[-12, 12, 2],
            y_range=[-3, 3, 1],
        )
        ax.set_color(BLACK)
        numplane = NumberPlane()
        self.add(numplane, ax)

        cont_val = ax.plot(lambda t: 3*np.sin(2*np.pi*0.05*t), color=BLACK)
        points = cont_val.get_point_from_function(np.arange(-9,10,1))
        cont_stem = VGroup(*[Stem(p, ax=ax, color=BLACK) for p in zip(points[0], points[1])])

        disc_val = ax.plot(lambda t: np.round(3*np.sin(2*np.pi*0.05*t)), color=BLACK)
        points = disc_val.get_point_from_function(np.arange(-9,10,1))
        disc_stem = VGroup(*[Stem(p, ax=ax, color=BLUE, line_func=DashedLine) for p in zip(points[0], points[1])])
        self.play(Create(cont_stem), run_time=1)
        self.wait(2)

        txt1 = Text("Let's force the values to the grid.", color=BLACK, width=5)
        txt2 = Text("to get a discrete-valued signal", color=BLUE, width=5)
        txt1.align_on_border(LEFT).align_on_border(UP)
        txt2.next_to(txt1, direction=DOWN)
        self.play(Write(txt1), Write(txt2), run_time=2)
        self.wait(2)

        self.play(Create(disc_stem), run_time=1)
        self.wait(2)

        rect1 = Rectangle(height=1, width=3, color=RED)
        rect2 = rect1.copy()
        rect1.move_to(3*DOWN + 2.5*LEFT)
        rect2.move_to(3*UP + 2.5*RIGHT)
        self.play(FadeIn(rect1), FadeIn(rect2), run_time=2)
        self.wait(10)