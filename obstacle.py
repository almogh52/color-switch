import pygame
import utils
from PIL import Image

class Obstacle(pygame.sprite.Sprite):
    OBSTACLE_SIZE = 200

    def __init__(self, screen):
        # Call the super constructor
        pygame.sprite.Sprite.__init__(self)

        # Save the screen as a field
        self.screen = screen

        # Set the height and the width by the obstacle size
        self.width = self.height = self.OBSTACLE_SIZE

        # Create the sprite's rect and set the obstacle in the middle of the screen
        self.rect = pygame.Rect(screen.get_rect().width / 2 - self.width / 2, screen.get_rect().height * 2 / 3, self.width, self.height)

        # Load the image and resize it to the correct size
        self.image = utils.load_and_resize_image("Obstacle.png", (200, 200))

    def update(self):
        # Draw the image onto the screen
        self.screen.blit(self.image, self.rect)