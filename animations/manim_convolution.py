from manim import *

class Convolution(Scene):
    """TODO: Docstring"""
    def construct(self):

        plane = NumberPlane()
        self.add(plane)

        n = np.arange(-2,3,1)
        x1 = n
        x2 = np.array([1 if m >= 0 else 0 for m in n])

        vg1 = VGroup()
        vg2 = VGroup()

        for m, w1, w2 in zip(n, x1, x2):
            edge1 = DOWN if w1 >= 0 else UP
            edge2 = DOWN if w2 >= 0 else UP

            vg1.add(Vector(w1*UP).move_to(m*RIGHT, aligned_edge=edge1))
            vg2.add(Vector(w2*UP).move_to(m*RIGHT, aligned_edge=edge2))

        self.play(Create(vg1))
        self.wait()
        self.play(vg1.animate.scale(0.25).move_to(3*LEFT + 2*UP))
        self.wait()
        self.play(Create(vg2))

        self.wait(2)

