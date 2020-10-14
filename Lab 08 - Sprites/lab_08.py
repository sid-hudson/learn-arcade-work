import arcade
import random

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):


    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up game and variable"""

# Sprite list
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
# Score
        self.score = 0
# Set up character
# Character image from
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
# Create coins
        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_list.append(coin)

    def on_draw(self):
        """ Draw everything I need"""
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
# Draw text on screen
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Mouse motion"""
# Match player x and y to mouse location
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and logic"""
# Calls update
        self.coin_list.update()
# Generate list of sprites that player can collide with
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.coin_list)
# Remove sprites that are collided with
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()