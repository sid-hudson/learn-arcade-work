import arcade
arcade.open_window(500, 500, "Lab 2")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

# Draw the Ground
arcade.draw_lrtb_rectangle_filled(0,500,250,0, arcade.color.AO)
arcade.draw_lrtb_rectangle_filled(0,500,220,0, arcade.color.BROWN_NOSE)

# Draw Waterfall
arcade.draw_rectangle_filled(250, 0, 200, 500, arcade.color.BLUE_SAPPHIRE)

# draw trees
arcade.draw_rectangle_filled(100, 275, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(100, 375, 70, 275, 130, 275, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(400, 275, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 375, 370, 275, 435, 275, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(25, 275, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(25, 375, -5, 275, 60, 275, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(475, 275, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(475, 375, 445, 275, 505, 275, arcade.csscolor.DARK_GREEN)

# Draw Sun
arcade.draw_circle_filled(450, 450, 30, arcade.color.AMBER)

arcade.finish_render()
arcade.run()