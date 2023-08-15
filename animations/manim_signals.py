from manim import *

from stem import Stem


class ContinuousSignalExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        ax = Axes(
            x_range=[-10, 9, 1],
            y_range=[-1, 1, 0.1],
        )
        ax.set_color(BLACK)
        curve = ax.plot(lambda t: np.sin(2*np.pi*0.05*t), color=BLACK)
        self.add(ax, curve)


class DiscreteSignalExample(Scene):
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