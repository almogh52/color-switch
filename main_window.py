import pygame
from ball import Ball
from obstacle import Obstacle

class MainWindow():
    def __init__(self, width, height):
        # Set the window size and pos
        self.rect = pygame.Rect(0, 0, width, height)

        # Initialize the pygame library
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode(self.rect.size)

        # Create the ball
        self.ball = Ball(self.screen)

        self.obs = Obstacle(self.screen)

    def run(self):
        # Create a clock that will be used as a framerate monitor and limiter
        clock = pygame.time.Clock()

        game_running = True

        # While the user didn't exit the game, continue main loop (frames)
        while game_running:
            # Handle events
            for event in pygame.event.get():
                # Quit Event
                if event.type == pygame.QUIT:
                    game_running = False
                
                # Key down event
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.clicked()

            self.ball.update()
            self.obs.update()

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(60)

        # Quit app after the user choose to quit
        pygame.quit()

MainWindow(800, 600).run()