import arcade

def main():
    arcade.open_window(500, 500, "Lab 3")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)
    arcade.start_render()


def draw_ground():
    """Draw the Ground"""
    arcade.draw_lrtb_rectangle_filled(0,500,250,0, arcade.color.AO)
    arcade.draw_lrtb_rectangle_filled(0,500,220,0, arcade.color.BROWN_NOSE)


def draw_waterfall():
    """Draw a Waterfall"""
    arcade.draw_rectangle_filled(250, 0, 200, 500, arcade.color.BLUE_SAPPHIRE)


def draw_forest():
    """Draw Multiple Trees"""
    arcade.draw_rectangle_filled(100, 275, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(100, 375, 70, 275, 130, 275, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(400, 275, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(400, 375, 370, 275, 435, 275, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(25, 275, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(25, 375, -5, 275, 60, 275, arcade.csscolor.DARK_GREEN)
    arcade.draw_rectangle_filled(475, 275, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(475, 375, 445, 275, 505, 275, arcade.csscolor.DARK_GREEN)


def draw_sun():
    """Draw the Sun"""
    arcade.draw_circle_filled(450, 450, 30, arcade.color.AMBER)


main()
draw_ground()
draw_waterfall()
draw_forest()
draw_forest()
draw_sun()

arcade.finish_render()
arcade.run()