import arcade
import random
import math

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_ASTEROID = 0.2
COIN_COUNT = 25
ASTEROID_COUNT = 25

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Bounces the coins
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Asteroid(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set point of orbit
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """Update position of ball"""
        # Calculate new x and y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y

        # Increase angle
        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8")

        self.player_list = None
        self.coin_list = None
        self.asteroid_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        """ Set up game and variable"""

        # Sprite list
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.asteroid_list = arcade.SpriteList()
        # Score
        self.score = 0
        # Set up character
        # Character image from kenny.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
        # Create coins and asteroids
        # Coin image from https://opengameart.org/content/my-game-sprites
        # Asteroid image from http://pixelartmaker.com/art/a50cf250e426f40
        for i in range(COIN_COUNT):
            coin = Coin("coin.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            coin.change_x = random.randrange(-3, 4)
            coin.change_y = random.randrange(-3, 4)
            self.coin_list.append(coin)

        for i in range(ASTEROID_COUNT):
            asteroid = Asteroid("asteroid.png", SPRITE_SCALING_ASTEROID)
            asteroid.circle_center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.circle_center_x = random.randrange(SCREEN_WIDTH)
            asteroid.circle_radius = random.randrange(10, 200)
            asteroid.circle_angle = random.random() * 2 * math.pi
            self.asteroid_list.append(asteroid)

    def on_draw(self):
        """ Draw everything I need"""
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.asteroid_list.draw()
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
        self.asteroid_list.update()
        # Generate list of sprites that player can collide with
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)
        asteroid_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                 self.asteroid_list)
        # Remove sprites that are collided with
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        for asteroid in asteroid_hit_list:
            asteroid.remove_from_sprite_lists()
            self.score -= 1


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()