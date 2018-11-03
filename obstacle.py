import pygame
import utils
from PIL import Image
from base_sprite import BaseSprite

class Obstacle(BaseSprite):
    OBSTACLE_SIZE = 260
    ROTATE_DELTA = 1.5

    def __init__(self, screen):
        # Call the super constructor with the screen, the obstacle's image, the size and the initial y pos
        BaseSprite.__init__(self, 
                            screen, 
                            "Resources/Obstacle.png", 
                            (self.OBSTACLE_SIZE, self.OBSTACLE_SIZE),
                            -self.OBSTACLE_SIZE)

        # Set the rotation amount as 0
        self.rotateAmount = 0

    def check_collsion_with_ball(self, ball):
        # Get the collision point of the obstacle and the ball
        collision_point = utils.get_overlap_point(self.image, self.rect, ball.image, ball.rect)

        # If the obstacle and the ball don't collide, return false
        if collision_point is None:
            return False

        # Try to get the color of the collision point from the screen
        try:
            color = self.screen.get_at(collision_point)
        except:
            # Default color - black color
            color = (0, 0, 0, 255)

        # If the color isn't black and isn't the ball's color, return true
        if not utils.color_is_black(color) and not utils.compare_colors(color, ball.color):
            return True

        return False

    def update(self, delta):
        # Rotate the original image by the rotate amount
        image = pygame.transform.rotate(self.image, self.rotateAmount)

        # Increase the rotate amount for the next rotation
        self.rotateAmount = (self.rotateAmount + self.ROTATE_DELTA) % 360

        # Apply y pos delta to the image
        self.rect.y = self.rect.y + delta

        # Draw the image onto the screen, the rect being used is the image rect with the center of the sprite
        self.screen.blit(image, image.get_rect(center=self.rect.center))