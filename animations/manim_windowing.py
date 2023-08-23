from manim import *

from stem import Stem


class RectangularWindow(Scene):
    def construct(self):

        n = np.arange(1024)
        x = np.cos(2*np.pi*0.02*n)
        w = np.zeros(n.size)
        w[n < 32] = 1
        y = x*w

        X = np.abs(np.fft.fftshift(np.fft.fft(x/x.size)))
        W = np.abs(np.fft.fftshift(np.fft.fft(w/w.size)))*n.size/32
        Y = np.abs(np.fft.fftshift(np.fft.fft(y/y.size)))*n.size/32

        ax_x = Axes(
            x_range=(0, n.size-1, 1),
            y_range=(-1, 1, 0.1),
            x_length=12,
            y_length=6,
        )
        ax_x.set_stroke(width=4)

        ax_X = Axes(
            x_range=(-n.size/2, n.size/2 - 1, 1),
            y_range=(0, 1, 0.1),
            x_length=12,
            y_length=6,
        )

        curve_x = ax_x.plot(lambda m: x[int(m)])
        curve_X = ax_X.plot(lambda m: X[int(m)+n.size//2])
        curve_w = ax_x.plot(lambda m: w[int(m)])
        curve_W = ax_X.plot(lambda m: W[int(m)+n.size//2])
        curve_y = ax_x.plot(lambda m: y[int(m)])
        curve_Y = ax_X.plot(lambda m: Y[int(m)+n.size//2])

        self.wait()
        self.play(Create(curve_x), run_time=2)
        self.wait(2)
        self.play(curve_x.animate.scale(0.25).shift(3*UP))
        self.play(Create(curve_X.center()), run_time=2)
        self.wait(2)
        self.play(curve_X.animate.scale(0.25).shift(4*RIGHT+UP), curve_x.animate.shift(4*RIGHT))
        self.play(Create(curve_w.scale(0.5).shift(LEFT)))
        self.wait(3)
        self.play(Create(curve_W.scale(0.5).shift(LEFT+DOWN)))
        self.wait(3)
        self.play(curve_x.animate.align_on_border(LEFT))
        self.wait()
        txt_mult = Text("x").next_to(curve_x,RIGHT)
        txt_eq = Text("=")
        self.play(Write(txt_mult), curve_w.animate.next_to(txt_mult))
        self.play(Write(txt_eq.next_to(curve_w,RIGHT)))
        self.play(Create(curve_y.scale(0.25).next_to(txt_eq,RIGHT)))
        self.wait(2)
        self.play(curve_X.animate.center().scale(2))
        self.play(curve_W.animate.scale(0.5).next_to(curve_X,LEFT).shift(0.25*UP))
        self.wait()
        self.play(curve_W.animate.next_to(curve_X,RIGHT).shift(0.25*UP), Create(curve_Y.scale(0.5).next_to(curve_X,DOWN)), run_time=8)
        self.wait(2)
        txt_expl = Tex("Using a finite number of samples\\\\decreases frequency resolution due\\\\to the energy spreading caused by\\\\the inherent rectangular window.")
        txt_expl.set(font_size=28, aligned_edge=LEFT)
        self.play(Write(txt_expl.next_to(curve_X,LEFT).shift(UP+RIGHT)))
        self.wait(5)

