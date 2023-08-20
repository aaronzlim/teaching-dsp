from manim import *

from stem import Stem

class UnitSampleSequence(Scene):
    """TODO: Docstring"""
    def construct(self):

        self.camera.background_color = WHITE

        ax = Axes(
            x_range=(-5,5,1),
        )
        ax.set_color(BLACK)

        def unit_sample(n):
            if np.isscalar(n):
                return 1 if n == 0 else 0
            else:
                return np.array([1 if m == 0 else 0 for m in n])

        plot = ax.plot(unit_sample)
        points = plot.get_point_from_function(np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5]))

        seq = VGroup(*[Stem(p, ax=ax, stroke_width=10, color=BLACK) for p in zip(points[0],points[1])])

        self.add(ax, seq)

        self.add(Text("1", color=BLACK).move_to(0.8*UP+0.5*RIGHT))

        self.add(Tex("$x(n) = \delta(n)$", color=BLACK).next_to(ax,DOWN))


class UnitStepSequence(Scene):
    """TODO: Docstring"""
    def construct(self):

        self.camera.background_color = WHITE

        ax = Axes(
            x_range=(-5,5,1),
        )
        ax.set_color(BLACK)

        def unit_sample(n):
            if np.isscalar(n):
                return 1 if n >= 0 else 0
            else:
                return np.array([1 if m >= 0 else 0 for m in n])

        plot = ax.plot(unit_sample)
        points = plot.get_point_from_function(np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5]))

        seq = VGroup(*[Stem(p, ax=ax, stroke_width=10, color=BLACK) for p in zip(points[0],points[1])])

        self.add(ax, seq)

        self.add(Text("1", color=BLACK).move_to(0.8*UP+0.5*RIGHT))

        self.add(Tex("$x(n) = u(n)$", color=BLACK).next_to(ax,DOWN))


class RealExponentialSequence(Scene):
    """TODO: Docstring"""
    def construct(self):

        self.camera.background_color = WHITE

        ax = Axes(
            x_range=(-5,5,1),
            y_range=(0,33,1)
        )
        ax.set_color(BLACK)

        plot = ax.plot(lambda x: 2.0**x)
        points = plot.get_point_from_function(np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5]))

        seq = VGroup(*[Stem(p, ax=ax, stroke_width=10, color=BLACK) for p in zip(points[0],points[1])])

        self.add(ax, seq)

        self.add(Tex("$x(n) = a^n$", color=BLACK).next_to(ax,DOWN))


class ComplexExponentialSequence(Scene):
    """TODO: Docstring"""
    def construct(self):

        self.camera.background_color = WHITE

        ax = Axes(
            x_range=(-5,5,1),
            y_range=(-1,2,0.1)
        )
        ax.set_color(BLACK)

        rplot = ax.plot(lambda x: np.real(np.exp(2j*np.pi*0.3*x)))
        cplot = ax.plot(lambda x: np.imag(np.exp(2j*np.pi*0.3*x)))
        rpoints = rplot.get_point_from_function(np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5]))
        cpoints = cplot.get_point_from_function(np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5]))

        rseq = VGroup(*[Stem(p, ax=ax, stroke_width=10, color=RED) for p in zip(rpoints[0],rpoints[1])])
        cseq = VGroup(*[Stem(p, ax=ax, stroke_width=10, color=BLUE) for p in zip(cpoints[0],cpoints[1])])

        rplot.set_color(RED)
        cplot.set_color(BLUE)

        self.add(ax, rplot, cplot, rseq, cseq)

        self.add(Tex("$x(n) = re^{j \omega n}$", color=BLACK).next_to(ax,DOWN))