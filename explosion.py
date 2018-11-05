import pygame
import random
import utils

class BallExplosion(pygame.sprite.Sprite):
    BALL_RADIUS = 3
    BALL_COLORS = [
        (0, 255, 204),
        (255, 101, 0),
        (211, 84, 0),
        (255, 23, 0),
        (0, 255, 108),
        (0, 152, 255),
        (179, 0, 255)
    ]

    def __init__(self, screen):
        # Call the super constructor
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        # Get the screen's rect to be used in the random position
        screen_rect = screen.get_rect()

        # Set a random y for the ball
        self.y = random.randint(0, screen_rect.height)

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

        # Generate a random velocity for the x and y axis
        self.velocity = (random.randint(2, 8), random.randint(2, 8))

    def update(self):
        # Change the ball's position by the velocity
        self.x += self.velocity[0] * self.direction[0]
        self.y += self.velocity[1] * self.direction[1]

        # Draw the circle onto the screen
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.BALL_RADIUS)
