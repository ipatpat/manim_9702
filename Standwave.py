from manim import *

class Standwave(Scene):
    def construct(self):
        # Create axes with x_range from 0 to 8*pi and centered y-axis
        axis1 = Axes(
            x_range=[0, 9*PI, PI],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": BLACK},
        )
        axis2 = Axes(
            x_range=[0, 9*PI, PI],
            y_range=[-1.5, 1.5, 1],
            axis_config={"color": BLACK},
        )
        a = ValueTracker(0) #value of "a"
        lambda1 = lambda x : np.sin( x - a.get_value() ) if 0+a.get_value()>x else 0
        lambda2 = lambda x : -np.sin( x + 9*PI + a.get_value()) if x>18*PI-a.get_value() else 0
        # Create two sine waves with different phase shifts
        sine_wave_1 = always_redraw(lambda : axis1.plot(lambda1).set_color(DARK_BLUE))
        sine_wave_2 = always_redraw(lambda : axis1.plot(lambda2).set_color(DARK_BROWN))

        # Create the superposition (by summing the individual functions)
        superposition_wave = always_redraw(
        lambda: axis2.plot(lambda x: lambda1(x) + lambda2(x)).set_color(DARKER_GRAY))
   
        # Group the waves        
        superpose = VGroup(axis2, superposition_wave).scale([1, 0.5, 1]).shift(2*DOWN)
        sine_waves = VGroup(axis1, sine_wave_1, sine_wave_2).scale([1, 0.5, 1]).shift(2*UP)
        waves = VGroup(sine_waves, superpose)
        # Display the axes and sine waves
        self.play(Create(waves))
        self.play(a.animate.set_value(36 * PI), run_time=10, rate_func=rate_functions.linear)
        # Move the sine waves and display the superposition