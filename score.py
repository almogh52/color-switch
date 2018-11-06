from star import Star
import pygame
import utils

class Score(pygame.sprite.Sprite):
    BASE_POS = 5
    DISTANCE = 10
    COLOR = (255, 211, 0)

    def __init__(self, screen):
        # Call the super constructor
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        
        # Load and resize the star image
        self.image = utils.load_and_resize_image("resources/star.png", (Star.STAR_SIZE, Star.STAR_SIZE))
        self.image.fill(self.COLOR, None, pygame.BLEND_MIN) # Fill the star image with the score color

        # Set initial score at 0
        self.score = 0

        # Open the font for the score
        self.font = pygame.font.Font("resources/Bonk.ttf", 50)

    def update(self):
        # Create the star's rect in the base pos and blit it onto the screen
        image_rect = self.image.get_rect(x = self.BASE_POS, y = self.BASE_POS)
        self.screen.blit(self.image, image_rect)

        # Render the score label and blit it to the screen
        score_label = self.font.render(str(self.score), True, self.COLOR)
        score_rect = score_label.get_rect(x = self.BASE_POS + image_rect.width + self.DISTANCE, 
                                        y = self.BASE_POS + image_rect.height / 2 - score_label.get_rect().width)
        self.screen.blit(score_label, score_rect)

    def increase(self):
        self.score += 1
