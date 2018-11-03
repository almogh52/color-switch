import pygame
import utils

class Ball(pygame.sprite.Sprite):
    BALL_BORDER = 5
    BALL_DIAMETER = 25

    MAX_SPEED = 7.6
    ACCELERATION = 0.35

    def __init__(self, screen):
        # Call the super constructor
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        # The width and height is the diameter of the ball + it's border
        self.width = self.height = self.BALL_DIAMETER + self.BALL_BORDER

        # Set the ball's rect, x pos in the middle of the screen, y pos in the lower part of the screen
        self.rect = pygame.Rect(screen.get_rect().width / 2 - self.width / 2, screen.get_rect().height * 2 / 3, self.width, self.width)

        # Start the player's speed as 0
        self.speed = 0

        # Set a random color for the ball
        self.switch_ball_color()

    def switch_ball_color(self):
        # Get a random ball image from the ball images folder
        self.image_file = utils.random_file_from_folder("Resources/Ball")

        # Load the ball image and resize it to it's size by the diameter + border
        self.image = utils.load_and_resize_image(self.image_file, (self.BALL_DIAMETER + self.BALL_BORDER, self.BALL_DIAMETER + self.BALL_BORDER))

        # Get the most used color in the image and use it as the ball's color
        self.color = utils.get_dominant_color_from_image(self.image_file)

    def clicked(self):
        # Set speed to max speed
        self.speed = self.MAX_SPEED

    def update(self):
        obstacle_delta = 0

        # Change speed according to the acceleration
        self.speed -= self.ACCELERATION

        # If the new y pos is smaller than the middle of the screen (if the ball need to pass the middle), set the obstacle delta as the speed
        if self.rect.y - self.speed <= self.screen.get_rect().height / 2 - self.height / 2:
            # Move the obstacles by the current speed
            obstacle_delta = self.speed
        else:
            # Change the y pos using the speed
            self.rect.y -= self.speed

        # Draw the image on the screen
        self.screen.blit(self.image, self.rect)

        return obstacle_delta