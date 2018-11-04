import pygame
import utils
from base.base_obstacle import BaseObstacle
from base.base_sprite import BaseSprite
import utils

class PlusObstacle(BaseObstacle):
    OBSTACLE_SIZE = 260
    ROTATE_DELTA = 1.5
    OFFSET_FROM_MIDDLE = 95

    def __init__(self, screen, y_pos):
        # Call the super constructor with the screen, the obstacle's image, the size and the initial y pos
        BaseSprite.__init__(self, 
                            screen, 
                            "resources/obstacles/plus.png", 
                            (self.OBSTACLE_SIZE, self.OBSTACLE_SIZE),
                            y_pos)
                            
        # Get random bool to pick the obstacle's side of the screen
        if utils.random_bool():
            self.rect.x += self.OFFSET_FROM_MIDDLE
        else:
            self.rect.x -= self.OFFSET_FROM_MIDDLE

        # Get random bool to pick the rotation direction
        if utils.random_bool():
            self.angle_delta = self.ROTATE_DELTA
        else:
            self.angle_delta = -self.ROTATE_DELTA

        # Set the rotation amount as 0
        self.rotateAmount = 0

    def get_collision_point(self, ball):
        # Rotate the original image by the rotate amount
        image = pygame.transform.rotozoom(self.image, self.rotateAmount, 1)

        # Get the collision point of the obstacle and the ball
        return utils.get_overlap_point(image, image.get_rect(center=self.rect.center), ball.image, ball.rect)

    def update(self, delta):
        # Rotate the original image by the rotate amount
        image = pygame.transform.rotozoom(self.image, self.rotateAmount, 1)

        # Increase the rotate amount for the next rotation
        self.rotateAmount = (self.rotateAmount + self.angle_delta) % 360

        # Apply y pos delta to the image
        self.rect.y += delta

        # Draw the image onto the screen, the rect being used is the image rect with the center of the sprite
        self.screen.blit(image, image.get_rect(center=self.rect.center))