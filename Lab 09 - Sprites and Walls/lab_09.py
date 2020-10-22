"""
Artwork from http://kenney.nl

Brain artwork from https://webstockreview.net/explore/brain-clipart-human-brain/
"""

import arcade
import os

SPRITE_SCALING = 0.5
SPRITE_SCALING_BRAIN = 0.01

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Lab 09"

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.brain_list = None
        self.wall_list = None
        self.player_list = None

        # Set up player
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.brain_list = arcade.SpriteList()

        # Set up player
        self.player_sprite = arcade.Sprite("character.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 150
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        # Set up the walls
        # Set up outer walls
        for x in range(0, 1200):
            wall = arcade.Sprite("wall.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 25
            self.wall_list.append(wall)

        for x in range(0, 1200):
            wall = arcade.Sprite("wall.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 675
            self.wall_list.append(wall)

        for y in range(0, 700):
            wall = arcade.Sprite("wall.png", SPRITE_SCALING)
            wall.center_x = 25
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 700):
            wall = arcade.Sprite("wall.png", SPRITE_SCALING)
            wall.center_x = 1175
            wall.center_y = y
            self.wall_list.append(wall)

        # Set up maze
        for y in range(200, 500):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = 205
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(285, 500):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        for y in range(350, 500):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = 350
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(275, 500):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = 500
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(425, 427):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 500
            self.wall_list.append(wall)

        for y in range(100, 200):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = 675
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(350, 600):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = 675
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(750, 1050):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)

        for x in range(800, 1100):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 350
            self.wall_list.append(wall)

        for y in range(425, 550):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = 900
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(1025, 1100):
            wall = arcade.Sprite("wood.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 550
            self.wall_list.append(wall)

        # Place brains

        brain = arcade.Sprite("brain.png", SPRITE_SCALING_BRAIN)
        brain.center_x = 425
        brain.center_y = 300
        self.brain_list.append(brain)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list)
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()

        # Draw all the sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.brain_list.draw()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.physics_engine.update()


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()