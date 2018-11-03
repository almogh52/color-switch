import pygame
from obstacle import Obstacle

class MapSprites(pygame.sprite.Group):
    def check_collsion_with_ball(self, ball):
        sprites = self.sprites()
        collides = False

        # Call the collision function in all obstacles and do an or bitwise with the collides boolean
        for sprite in sprites:
            # If the sprite is an obstacle, check if it collides with the ball
            if type(sprite) is Obstacle:
                collides |= sprite.check_collsion_with_ball(ball)

        return collides