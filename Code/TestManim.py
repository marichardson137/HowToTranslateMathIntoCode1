from manim import *


class Test(Scene):

    def format_point(self, point) -> str:
        """Format the given point to look presentable."""
        return f"[{point[0]:.2f}, {point[1]:.2f}]"

    def construct(self):

        title_1 = Tex("How To")
        title_2 = Tex("TRANSLATE").center().scale(2)
        title_3 = Tex("Math into Code")

        title_1.next_to(title_2, UP).shift(LEFT*2.2)
        title_3.next_to(title_2, DOWN).shift(RIGHT*1.3)

        self.play(LaggedStart(
            Write(title_2),
            Write(title_1),
            Write(title_3),
            lag_ratio=0.20,
            run_time=3
        ))
        self.wait(1.5)

        self.play(
            FadeOut(title_1),
            FadeOut(title_2),
            FadeOut(title_3),
            run_time=1.5
        )

        math = Text("Mathematics").scale(2).set_color(RED_D)
        cs = Text("Computer Science").scale(2).set_color(BLUE_D)

        sigma = MathTex(r"\sum_{i=1}^{n}").shift(
            LEFT*2 + UP*1.3).set_color(DARK_GRAY)
        integral = MathTex(r"\iint f(x,y)dxdy").shift(
            RIGHT*2 + DOWN*1.2).set_color(DARK_GRAY)
        self.play(LaggedStart(
            Write(math),
            FadeIn(sigma, shift=UP*0.3),
            FadeIn(integral, shift=DOWN*0.3),
            lag_ratio=0.20,
            run_time=2
        ))
        self.wait(2)

        codeExample1 = Code(
            "Code/Summation.py",
            tab_width=4,
            insert_line_no=True,
            font="Monospace",
            background="rectangle",
            background_stroke_width=0,
            background_stroke_color=BLACK,
            language="Python",
        ).shift(LEFT*2 + DOWN*2).scale(0.75)

        codeExample2 = Code(
            "Code/Summation.java",
            tab_width=4,
            insert_line_no=True,
            font="Monospace",
            background="rectangle",
            background_stroke_width=0,
            background_stroke_color=BLACK,
            language="Java",
        ).shift(RIGHT*2 + UP*2).scale(0.5)

        self.play(
            FadeOut(integral, shift=UP*0.3),
            ReplacementTransform(math, cs),
            FadeOut(sigma, shift=DOWN*0.3),
            Write(codeExample1),
            Write(codeExample2),
            lag_ratio=0.1,
            run_time=1.5
        )

        self.wait(1.5)
        self.play(LaggedStart(
            FadeOut(codeExample1),
            FadeOut(cs),
            FadeOut(codeExample2),
            lag_ratio=0.2,
            run_time=2
        ))

        ax = Axes(x_range=[-1, 10, 1]).add_coordinates()

        dot_axes = Dot(ax.c2p(1, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(1, 2))

        self.play(Create(ax), GrowFromCenter(dot_axes), Create(lines))

        p1 = dot_axes.get_center()
        p1b = p1 + [1, 0, 0]
        p2 = np.array(ax.coords_to_point(8, -3))
        p2b = p2 - [1, 0, 0]
        bezier = CubicBezier(p1, p1b + 3 * RIGHT, p2b -
                             3 * RIGHT, p2).set_color(DARK_GRAY)
        # self.play(Create(bezier))

        def lines_updater(obj):
            """An updater that moves the coordinate lines to match the dot."""
            obj = ax.get_lines_to_point(dot_axes.get_center())
            lines.become(obj)

        def format_point(self, point) -> str:
            """Format the given point to look presentable."""
            return f"[{point[0]:.2f}, {point[1]:.2f}]"

        dotLabel = Tex()

        def label_updater(obj):
            """An updater that displays the circle's position above it."""
            obj.become(
                Tex(f"{self.format_point(ax.p2c(dot_axes.get_center()))}")).scale(0.75)
            obj.next_to(dot_axes, UP, buff=0.35)

        label_updater(dotLabel)
        self.play(Write(dotLabel), run_time=0.6)

        lines.add_updater(lines_updater)
        dotLabel.add_updater(label_updater)

        dot_axes.save_state()
        self.play(MoveAlongPath(dot_axes, bezier), run_time=3,
                  run_func=rate_functions.ease_in_out_cubic)
        self.wait()
        self.play(Restore(dot_axes), run_time=2)

        self.wait()
