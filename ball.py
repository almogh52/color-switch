import pygame

class Ball(pygame.sprite.Sprite):
    BALL_BORDER = 5
    BALL_DIAMETER = 25

    MAX_SPEED = 8.5
    ACCELERATION = 0.35

    def __init__(self, screen):
        # Call the super constructor
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen

        # The width and height is the diameter of the ball + it's border
        self.width = self.height = self.BALL_DIAMETER + self.BALL_BORDER

        # Set the ball's rect, x pos in the middle of the screen, y pos in the lower part of the screen
        self.rect = pygame.Rect(screen.get_rect().width / 2 - self.width / 2, screen.get_rect().height * 2 / 3, self.width, self.width)

        # Load the ball image and resize it to it's size by the diameter + border
        self.image = pygame.image.load("Ball.png")
        self.image = pygame.transform.scale(self.image, (self.BALL_DIAMETER + self.BALL_BORDER, self.BALL_DIAMETER + self.BALL_BORDER))

        # Start the player's speed as 0
        self.speed = 0

    def clicked(self):
        # Set speed to max speed
        self.speed = self.MAX_SPEED

    def update(self):
        # Change speed according to the acceleration
        self.speed -= self.ACCELERATION

        # Change the y pos using the speed
        self.rect.y -= self.speed

        # Draw the image on the screen
        self.screen.blit(self.image, self.rect)