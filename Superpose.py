from manim import *

class Superposition(Scene):
    def construct(self):
        # Create axes with x_range from 0 to 8*pi and centered y-axis
        axis = Axes(
            x_range=[0, 9*PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"color": BLACK},
        )
        X_AXIS="displacement/m"
        Y_AXIS="distant/m"
        labels = axis.get_axis_labels(
        Tex(X_AXIS,color=BLACK).scale(0.5), Tex(Y_AXIS,color=BLACK).scale(0.5))
        
        a = ValueTracker(0) #value of "a"
        lambda1 = lambda x : np.sin( x + a.get_value() ) if PI-a.get_value()>x>0-a.get_value() else 0
        lambda2 = lambda x : np.sin( x - a.get_value() ) if 9*PI+a.get_value()>x>8*PI+a.get_value() else 0
        # Create two sine waves with different phase shifts
        sine_wave_1 = always_redraw(lambda : axis.plot(lambda1).set_color(DARK_BLUE))
        sine_wave_2 = always_redraw(lambda : axis.plot(lambda2).set_color(DARK_BROWN))

        # Group the sine waves 
        sine_waves = VGroup(sine_wave_1, sine_wave_2)

        # Create the superposition (by summing the individual functions)
        superposition_wave = always_redraw(
        lambda: axis.plot(lambda x: lambda1(x) + lambda2(x)).set_color(DARK_BLUE))
        # Display the axes and sine waves
        self.play(Create(VGroup(axis, labels)))
        self.play(Create(superposition_wave))
        # Move the sine waves and display the superposition
        self.play(a.animate.set_value(-10 * PI), run_time=4, rate_func=rate_functions.linear)