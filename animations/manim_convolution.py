from manim import *

from stem import Stem

class Convolution(Scene):
    """TODO: Docstring"""
    def construct(self):

        title = Text("Convolution:").align_on_border(UP).align_on_border(LEFT)
        self.add(title)
        self.add(Tex("$x(n) \circledast h(n) = \sum_k x(k) h(n-k)$").next_to(title, RIGHT).align_on_border(UP))

        plane = NumberPlane(
            x_range=(-5, 9, 1),
            x_length=14,
            y_length=8,
        )
        self.add(plane)

        n = np.arange(-2,3,1)
        func1 = lambda x: 0.75*x if x >= 0 else 0
        func2 = lambda x: 1 if x >= 0 else 0

        stem1 = Stem.from_function(func1, n, color=RED).shift(2*LEFT)
        stem2 = Stem.from_function(func2, n, color=YELLOW).shift(2*DOWN + 2*LEFT)

        eq1 = Tex("$x(n) = 3n/4$").next_to(stem1, DOWN)
        eq1b = Tex("$x(k)$")
        eq2 = Tex("$h(n) = u(n)$").next_to(stem2, DOWN)
        eq3 = Tex("$h(k-5)$")
        eq4 = Tex("$h(5-k)$")

        self.wait()
        self.play(Create(stem1), Create(stem2))
        self.play(Write(eq1), Write(eq2))
        self.wait(3)
        self.play(
            ReplacementTransform(eq1, eq1b.next_to(stem1, UP)),
            ReplacementTransform(eq2, eq3.next_to(stem2, UP))
        )
        self.play(
            stem2.animate.shift(2*UP + 5*RIGHT),
            eq3.animate.shift(2*UP + 5*RIGHT)
        )
        self.wait(3)
        self.play(
            Rotate(stem2, radians=PI, axis=UP),
            ReplacementTransform(eq3, eq4.next_to(stem2, UP)))
        self.wait(3)

        L = Line(5*LEFT+3*DOWN, 5*RIGHT+3*DOWN)
        self.play(Create(L), Create(Stem((0,0)).shift(3*RIGHT+3*DOWN)))
        self.play(Create(Tex("$x(n) \circledast h(n)$").shift(4*LEFT + 2*DOWN)))

        eq = eq4
        h_center = eq.get_center()

        y1 = np.array([func1(x) for x in n])
        y2 = np.array([func2(x) for x in n])
        c = np.convolve(y1, y2)

        for idx in range(1, 6, 1):
            eq_next = Tex(f"$h({5-idx}-k)$").move_to(h_center)
            self.play(
                stem2.animate.shift(LEFT),
                ReplacementTransform(eq, eq_next)
            )
            eq = eq_next
            self.play( # start at -2 due to extra line object at end of VGroup
                *[Indicate(s) for s in stem1[-2:-2-idx:-1]],
                *[Indicate(s) for s in stem2[-2:-2-idx:-1]]
            )
            self.play(Create(Stem((5-idx, c[-idx])).shift(3*DOWN+2*LEFT)))
            self.wait()
        self.wait(3)


class ImpulseResponse(Scene):
    def construct(self):
        rect = VGroup(Rectangle(height=1, width=2), Tex("$h(n)$"))

        n = [0, 1, 2, 3]
        x = [0.25, 0.5, 0.75, 0.25]
        xa = [0.25, 0, 0, 0]
        xb = [0, 0.5, 0, 0]
        xc = [0, 0, 0.75, 0]
        xd = [0, 0, 0, 0.25]

        s = VGroup(*[Stem(p) for p in zip(n,x)], Line(0*LEFT, 3*RIGHT))
        sa = VGroup(*[Stem(p, color=RED) for p in zip(n,xa)], Line(0*LEFT, 3*RIGHT, color=RED))
        sb = VGroup(*[Stem(p, color=BLUE) for p in zip(n,xb)], Line(0*LEFT, 3*RIGHT, color=BLUE))
        sc = VGroup(*[Stem(p, color=YELLOW) for p in zip(n,xc)], Line(0*LEFT, 3*RIGHT, color=YELLOW))
        sd = VGroup(*[Stem(p, color=GREEN) for p in zip(n,xd)], Line(0*LEFT, 3*RIGHT, color=GREEN))

        eqa = Tex("$x(n) \delta(n-0)$", font_size=28)
        eqb = Tex("$x(n) \delta(n-1)$", font_size=28)
        eqc = Tex("$x(n) \delta(n-2)$", font_size=28)
        eqd = Tex("$x(n) \delta(n-3)$", font_size=28)

        eqa1 = Tex("$x(0) \delta(n-0)$", font_size=28)
        eqb1 = Tex("$x(1) \delta(n-1)$", font_size=28)
        eqc1 = Tex("$x(2) \delta(n-2)$", font_size=28)
        eqd1 = Tex("$x(3) \delta(n-3)$", font_size=28)

        eqa2 = Tex("$x(0) h(n-0)$", font_size=28)
        eqb2 = Tex("$x(1) h(n-1)$", font_size=28)
        eqc2 = Tex("$x(2) h(n-2)$", font_size=28)
        eqd2 = Tex("$x(3) h(n-3)$", font_size=28)

        eqe1 = Tex("$x(k)h(n-k)$", font_size=32)
        eqe2 = Tex("$y(n) = \sum_k x(k) h(n-k)$", font_size=32)

        txt1 = Tex(
            "Let's say we have a system with known \\\\impulse response $h(n)$.",
            font_size=32,
            tex_environment=None
        ).align_on_border(RIGHT).align_on_border(UP)
        txt2 = Tex(
            "And some input signal $x(n)$.",
            font_size=32,
            tex_environment=None
        ).align_on_border(RIGHT).align_on_border(UP)
        txt3 = Tex(
            "$x(n)$ can be decomposed into a set of shifted impulses.",
            font_size=32,
            tex_environment=None
        ).align_on_border(RIGHT).align_on_border(UP)
        txt4 = Tex(
            "Because the unit sample sequence only captures\\\\one value, x(n) is essentially a constant.",
            font_size=32,
            tex_environment=None
        ).align_on_border(RIGHT).align_on_border(UP)
        txt5 = Tex(
            "Each impulse can be sent through the system individually.\\\\The response is just the impulse response scaled by $x(k)$",
            font_size=32,
            tex_environment=None
        ).align_on_border(RIGHT).align_on_border(UP)
        txt6 = Tex(
            "From the superposition principle, we know the final\\\\response is the sum of each impulse response.",
            font_size=32,
            tex_environment=None
        ).align_on_border(RIGHT).align_on_border(UP)
        txt7 = Tex(
            "This is why only the \\textbf{impulse response} is \\\\needed to know the response to any input signal.",
            font_size=32,
            tex_environment=None
        ).align_on_border(RIGHT).align_on_border(UP)


        self.wait()

        self.play(Write(txt1))
        self.wait()
        self.play(Create(rect))
        self.wait(2)
        self.play(ReplacementTransform(txt1, txt2))
        self.wait(2)
        self.play(Create(s.next_to(rect, LEFT)))
        self.wait(4)
        self.play(ReplacementTransform(txt2,txt3))
        self.wait(4)
        self.play(s.animate.align_on_border(LEFT).align_on_border(UP))
        self.wait()
        self.play(Create(sa.align_to(s, DOWN).align_to(s, LEFT)))
        self.play(sa.animate.next_to(s, DOWN))
        self.play(Write(eqa.next_to(sa, RIGHT)))
        self.play(Create(sb.align_to(s, DOWN).align_to(s, LEFT)))
        self.play(sb.animate.next_to(sa, DOWN))
        self.play(Write(eqb.next_to(sb, RIGHT)))
        self.play(Create(sc.align_to(s, DOWN).align_to(s, LEFT)))
        self.play(sc.animate.next_to(sb, DOWN))
        self.play(Write(eqc.next_to(sc, RIGHT)))
        self.play(Create(sd.align_to(s, DOWN).align_to(s, LEFT)))
        self.play(sd.animate.next_to(sc, DOWN))
        self.play(Write(eqd.next_to(sd, RIGHT)))
        self.wait(2)
        self.play(ReplacementTransform(txt3, txt4))
        self.wait(4)
        self.play(
            ReplacementTransform(eqa, eqa1.next_to(sa, RIGHT)),
            ReplacementTransform(eqb, eqb1.next_to(sb, RIGHT)),
            ReplacementTransform(eqc, eqc1.next_to(sc, RIGHT)),
            ReplacementTransform(eqd, eqd1.next_to(sd, RIGHT)),
        )
        self.wait(2)
        self.play(ReplacementTransform(txt4, txt5))
        self.wait(4)
        self.play(eqa1.animate.move_to(rect.get_center()))
        self.play(ReplacementTransform(eqa1, eqa2.next_to(rect, RIGHT).align_to(sa, DOWN)))
        self.wait(2)
        self.play(eqb1.animate.move_to(rect.get_center()))
        self.play(ReplacementTransform(eqb1, eqb2.next_to(eqa2, DOWN)))
        self.wait(2)
        self.play(eqc1.animate.move_to(rect.get_center()))
        self.play(ReplacementTransform(eqc1, eqc2.next_to(eqb2, DOWN)))
        self.wait(2)
        self.play(eqd1.animate.move_to(rect.get_center()))
        self.play(ReplacementTransform(eqd1, eqd2.next_to(eqc2, DOWN)))
        self.wait(2)
        self.play(Write(eqe1.next_to(rect,RIGHT)))
        self.wait(2)
        self.play(ReplacementTransform(txt5,txt6.align_on_border(RIGHT).align_on_border(UP)))
        self.wait(4)
        self.play(
            eqa2.animate.move_to(eqb2.get_center()),
            eqc2.animate.move_to(eqb2.get_center()),
            eqd2.animate.move_to(eqb2.get_center()),
        )
        self.play(
            FadeOut(eqa2),
            FadeOut(eqb2),
            FadeOut(eqc2),
            FadeOut(eqd2),
        )
        self.play(ReplacementTransform(eqe1,eqe2.next_to(rect,RIGHT)))
        self.wait()
        self.play(ReplacementTransform(txt6, txt7.align_on_border(UP).align_on_border(RIGHT)))
        self.wait(4)


class TimeDomainAliasing(Scene):
    def construct(self):

        N1 = 6
        N2 = 2

        L1 = Line(0.5*N1*LEFT, 0.5*N1*RIGHT, color=RED)
        L2 = Line(0.5*N2*LEFT, 0.5*N2*RIGHT, color=BLUE)

        r1 = N1/(2*PI)
        r2 = (N1+N2)/(2*PI)

        C1 = Circle(radius=r1, color=WHITE)
        C2 = Circle(radius=r2, color=WHITE)

        A11 = Arc(radius=r1, angle=N1/r1, color=RED)
        A12 = Arc(radius=r1, angle=N2/r1, color=BLUE).set_stroke(opacity=0.9)
        A12.rotate(angle=-A12.angle)

        A21 = Arc(radius=r2, angle=N1/r2, color=RED)
        A22 = Arc(radius=r2, angle=N2/r2, color=BLUE)
        A22.rotate(angle=-A22.angle)

        txt = Text("With LINEAR convolution we pull one signal through another.")
        txt.set(font_size=28)
        txt.align_on_border(LEFT).align_on_border(UP)

        self.wait()
        self.play(
            Create(L1.shift(UP)),
            Create(L2.shift(DOWN)),
            Write(txt),
        )
        self.wait(2)
        self.play(L1.animate.center())
        self.play(L2.animate.next_to(L1, LEFT))
        self.wait(2)
        self.play(L2.animate.next_to(L1, RIGHT), run_time=5)
        self.wait(2)
        self.play(Unwrite(txt))
        txt = Text("With CIRCULAR convolution, the x-axis changes from a line to a circle.")
        txt.align_on_border(UP)
        txt.set(font_size=28)
        self.play(Write(txt))
        self.wait()
        self.play(Create(C1.shift(3*LEFT)), Create(Dot(C1.get_right())))
        self.play(Write(Text("Start", font_size=20).next_to(C1, RIGHT)))
        self.wait()
        self.play(Unwrite(txt))
        txt = Text("If we make the output buffer the same size as the larger signal")
        txt.set(font_size=28).align_on_border(UP)
        txt2 = Text("(i.e. zero pad the smaller signal to the size of the larger one before the DFT.)")
        txt2.set(font_size=28).next_to(txt, DOWN)
        self.play(Write(txt), Write(txt2))
        self.wait()
        A11.move_to(L1.get_center())
        A12.move_to(L2.get_center())
        self.play(
            ReplacementTransform(L1, A11),
            ReplacementTransform(L2, A12),
            run_time=2
        )
        self.wait()
        A11.set_z_index(C1.z_index+1)
        A12.set_z_index(C1.z_index+2)
        self.play(
            A11.animate.move_arc_center_to(C1.get_center()),
            A12.animate.move_arc_center_to(C1.get_center()),
        )
        self.wait(2)
        self.play(Unwrite(txt), Unwrite(txt2))
        txt = Text("The equivalent convolution in the time domain has the smaller signal overlap")
        txt.set(font_size=28).align_on_border(UP)
        txt2 = Text("the larger one, corrupting the output of the convolution.")
        txt2.set(font_size=28).next_to(txt, DOWN)
        self.play(Write(txt), Write(txt2))
        self.wait(2)
        self.play(
            Rotate(A12, angle=(2*PI + A12.angle), about_point=C1.get_center()),
            run_time=5
        )
        self.wait(3)
        self.play(Unwrite(txt), Unwrite(txt2))
        txt = Text("If we make the output buffer large enough to fit both signals")
        txt.set(font_size=28).align_on_border(UP)
        txt2 = Text("(i.e. zero pad both signals to N+M-1 before the DFT)")
        txt2.set(font_size=28).next_to(txt, DOWN)
        self.play(Write(txt), Write(txt2))
        self.wait(2)
        self.play(Create(C2.shift(3*RIGHT)))
        self.wait()
        self.play(
            Create(A21.move_arc_center_to(C2.get_center())),
            Create(A22.move_arc_center_to(C2.get_center())),
            Create(Dot(C2.get_right())),
            Write(Text("Start", font_size=20).next_to(C2, RIGHT))
        )
        self.wait()
        self.play(
            Rotate(A22, angle=2*PI, about_point=C2.get_center()),
            run_time=5
        )
        self.wait()
        self.play(Unwrite(txt), Unwrite(txt2))
        txt = Text("There is no overalap, and no corruption of the output.")
        txt.set(font_size=28).align_on_border(UP)
        self.play(Write(txt))
        self.wait(5)
