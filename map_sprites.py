import pygame

class MapSprites(pygame.sprite.Group):
    def remove_hidden_sprites(self, screen):
        # Get the list of sprites
        sprites = self.sprites()

        # For each sprite check if it's hidden (y value bigger than screen width)
        for sprite in sprites:
            if sprite.rect.y >= screen.get_rect().height:
                self.remove(sprite)

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