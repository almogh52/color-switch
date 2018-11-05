import pygame
import random
import utils

class BallExplosion(pygame.sprite.Sprite):
    BALL_RADIUS = 3
    VELOCITY = 15
    BALL_COLORS = [
        (26, 188, 156),
        (241, 196, 15),
        (211, 84, 0),
        (231, 76, 60),
        (46, 204, 113),
        (52, 152, 219),
        (142, 68, 173),
        (52, 73, 94),
        (57, 32, 160)
    ]

    def __init__(self, screen):
        self.screen = screen

        # Get the screen's rect to be used in the random position
        screen_rect = screen.get_rect()

        # Set a random y for the ball
        self.y = random.randint(50, screen_rect.height) - 200

        # Get a random bool that indicates if the ball should start from left or right
        if utils.random_bool():
            # Set initial x pos
            self.x = screen_rect.width + 5

            # Set the ball's direction
            self.direction = (-1, -1 if self.y > screen_rect.height / 2 else 1)
        else:
            # Set initial x pos
            self.x = 0

            # Set the ball's direction
            self.direction = (1, -1 if self.y > screen_rect.height / 2 else 1)

        # Get a random color for the ball
        self.color = random.choice(self.BALL_COLORS)

    def update(self):
        # Change the ball's position by the velocity
        self.x += self.VELOCITY * self.direction[0]
        self.y += self.VELOCITY * self.direction[1]

        # Draw the circle onto the screen
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.BALL_RADIUS)
