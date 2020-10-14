import arcade
arcade.open_window(600, 600, "Lab 2")
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()
# draw the ocean
arcade.draw_lrtb_rectangle_outline(0, 599, 300, 0, arcade.csscolor.BLACK)

# draw the bridge
arcade.draw_circle_outline(300, 300, 100, arcade.csscolor.BLACK)

# draw the sun

arcade.draw_circle_filled(500, 500, 30, arcade.csscolor.YELLOW)
arcade.draw_circle_outline(500, 500, 25, arcade.csscolor.BLACK)
arcade.draw_line(500, 550, 400, 550, arcade.csscolor.BLACK)


arcade.finish_render()
arcade.run()
