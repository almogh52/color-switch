import pygame

class MapSprites(pygame.sprite.Group):
    def check_collsion_with_ball(self, ball):
        # Get the list of sprites
        sprites = self.sprites()

        collided_sprites = []

        # Call the collision function in all sprites and add them to the collided sprites list if they collide with the ball
        for sprite in sprites:
            # If the sprite collides with the ball, add it to the collided sprites list
            if sprite.check_collsion_with_ball(ball):
                collided_sprites.append(sprite)

        return collided_sprites