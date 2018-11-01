import pygame
import utils
from PIL import Image

class Obstacle(pygame.sprite.Sprite):
    OBSTACLE_SIZE = 200
    ROTATE_DELTA = 1.5

    def __init__(self, screen):
        # Call the super constructor
        pygame.sprite.Sprite.__init__(self)

        # Save the screen as a field
        self.screen = screen

        # Set the height and the width by the obstacle size
        self.width = self.height = self.OBSTACLE_SIZE

        # Create the sprite's rect and set the obstacle in the middle of the screen
        self.rect = pygame.Rect(screen.get_rect().width / 2 - self.width / 2, -self.height, self.width, self.height)

        # Load the image and resize it to the correct size
        self.image = utils.load_and_resize_image("Obstacle.png", (self.width, self.height))

        # Set the rotation amount as 0
        self.rotateAmount = 0

    def update(self):
        # Rotate the original image by the rotate amount
        image = pygame.transform.rotate(self.image, self.rotateAmount)

        # Increase the rotate amount for the next rotation
        self.rotateAmount = (self.rotateAmount + self.ROTATE_DELTA) % 360

        # Draw the image onto the screen, the rect being used is the image rect with the center of the sprite
        self.screen.blit(image, image.get_rect(center=self.rect.center))