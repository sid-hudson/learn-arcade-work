import arcade

def draw_ground():
    """Draw the Ground and River"""
    arcade.draw_lrtb_rectangle_filled(0,500,250,0, arcade.color.AO)
    arcade.draw_polygon_filled(((150, 250),
                                (350, 250),
                                (325, 0),
                                (175, 0),
                                ),
                               arcade.color.BLUE_SAPPHIRE)

def draw_bunny(x, y):
    arcade.draw_ellipse_filled(140 + x - 140, 100 + y - 100, 50, 20, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(160 + x - 140, 105 + y - 100, 10, arcade.csscolor.BROWN)
    arcade.draw_ellipse_filled(157 + x - 140, 110 + y - 100, 7, 25, arcade.csscolor.BROWN)
    arcade.draw_ellipse_filled(155 + x - 140, 90 + y - 100, 20, 5, arcade.csscolor.BROWN)
    arcade.draw_ellipse_filled(125 + x - 140, 90 + y - 100, 20, 5, arcade.csscolor.BROWN)
    arcade.draw_circle_filled(118 + x - 140, 105 + y - 100, 6, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(162 + x - 140, 107 + y - 100, 2, arcade.csscolor.BLACK)

def draw_rabbit_family():
    """Draw a Rabbit Couple"""
    draw_bunny(140, 100)
    draw_bunny(120, 70)

def draw_tree(x, y):
    arcade.draw_rectangle_filled(100 + x - 100, 275 + y - 275, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(100 + x - 100, 375 + y - 275, 70 + x - 100, 275 + y - 275, 130 + x - 100, 275 + y - 275, arcade.csscolor.DARK_GREEN)

def draw_forest():
    """Draw Multiple Trees"""
    draw_tree(100, 275)
    draw_tree(400, 275)
    draw_tree(25, 275)
    draw_tree(475, 275)


def draw_sun():
    """Draw the Sun"""
    arcade.draw_circle_filled(450, 450, 30, arcade.color.AMBER)
    arcade.draw_circle_filled(450, 450, 25, arcade.color.CHROME_YELLOW)
    arcade.draw_circle_filled(450, 450, 20, arcade.color.SAE)

def main():
    arcade.open_window(500, 500, "Lab 3")
    arcade.set_background_color(arcade.csscolor.SKY_BLUE)
    arcade.start_render()

    draw_ground()
    draw_sun()
    draw_forest()
    draw_rabbit_family()

    arcade.finish_render()
    arcade.run()

main()