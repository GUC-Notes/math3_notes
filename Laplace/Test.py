from manim import *
class Test(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10.3,
        "y_min": -1.5,
        "y_max": 1.5,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
        "x_labeled_nums": range(-10, 12, 2),
    }
    def construct(self):
        # numberplane = NumberPlane()
        # self.add(numberplane)
        self.setup_axes()
        dot = Circle(radius=0.08,color=GREEN).move_to(self.coords_to_point(3,1))
        dot1 = Circle(radius=0.08,color=GREEN).move_to(self.coords_to_point(5,1))
        graph_1 = self.get_graph(lambda x : 0,
                                    color = RED,
                                    x_min = -4, # Domain 1
                                    x_max = 3
                                    )
        graph_2 =self.get_graph(lambda x : 1,
                                    color = GREEN,
                                    x_min = 3, # Domain 2
                                    x_max = 5
                                    )
        graph_3 = self.get_graph(lambda x : 0,
                                    color = RED,
                                    x_min = 5, # Domain 1
                                    x_max = 10
                                    )
        text = MathTex("H(t-a) H(t-b)")
        text.set_color_by_gradient(GREEN,PURPLE)
        self.play(
            ShowCreation(graph_1),
            run_time = 1
        )
        self.add(dot)
        self.add(dot1)
        self.add(text)
        self.play(
            ShowCreation(graph_2),
            run_time = 1
        )
        self.play(
            ShowCreation(graph_3),
            run_time = 1
        )
        self.wait()
