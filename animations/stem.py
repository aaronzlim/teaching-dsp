from manim import *


class Stem(VMobject):
    """TODO: Docstring"""
    def __init__(self, coord=(0,0), ax=None, line_func=Line, color=WHITE, **kwargs):
        super().__init__(**kwargs)

        x, y = coord[0:2]

        edge = UP if y >= 0 else DOWN

        if ax is None:
            L = Line([x,0,0], [x,y,0], color=color, **kwargs)
        else:
            L = ax.get_vertical_line((x,y,0), line_func=line_func, color=color, **kwargs)

        D = Dot(color=color).next_to(L, direction=edge).align_to(L, direction=edge)
        D.shift(D.radius*edge)

        self.add(L, D)

    def from_function(func, x, ax=None, line_func=Line, color=WHITE, **kwargs):
        """TODO: Docstring"""
        y = np.array([func(elem) for elem in x])
        points = zip(x,y)
        L = Line(min(x)*RIGHT, max(x)*RIGHT)
        vg = VGroup(L,*[Stem(p, ax=ax, line_func=line_func, color=color, **kwargs) for p in points])
        vg += L
        return vg
