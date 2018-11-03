import pygame
import utils

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, screen, image, size, y_pos):
        # Call the super constructor
        pygame.sprite.Sprite.__init__(self)

        # Save the screen as a field
        self.screen = screen

        # Set the height and the width by the sprite's size
        self.width = size[0]
        self.height = size[1]

        # Create the sprite's rect and set the sprite in the middle of the screen
        self.rect = pygame.Rect(screen.get_rect().width / 2 - self.width / 2, y_pos, self.width, self.height)

        # If an image was sent, set it
        if image is not None:
            # Load the image and resize it to the correct size
            self.image = utils.load_and_resize_image(image, (self.width, self.height))

    def check_collsion_with_ball(self, ball):
        # Try to get the overlap point, if succeeded (point isn't None), return true 
        return utils.get_overlap_point(self.image, self.rect, ball.image, ball.rect) != None

    def update(self, delta):
        # Apply y pos delta to the image
        self.rect.y = self.rect.y + delta

        # Draw the image onto the screen, the rect being used is the image rect with the center of the sprite
        self.screen.blit(self.image, self.rect)