from manim import *

class Progressivewave(Scene):
    def construct(self):
        Y_AXIS="displacement/m"
        X_AXIS="distant/m"
        self.camera.background_color = WHITE
        a = ValueTracker(0) #value of "a"
        axis = Axes(x_range=[0,10*PI,PI],y_range=[-2,2],axis_config={"color": BLACK})
        sin = always_redraw(lambda : axis.plot(lambda x : np.sin( x + a.get_value())).set_color(DARK_BLUE)) #f(x) = sin(x + a)
        labels = axis.get_axis_labels(
        Tex(X_AXIS,color=BLACK).scale(0.75), Tex(Y_AXIS,color=BLACK).scale(0.75))

        ##Scene
        self.play(
            Create(VGroup(axis, labels)),Create(sin)
            )
        self.play(a.animate.set_value(-5 * PI), run_time=3, rate_func=rate_functions.linear)