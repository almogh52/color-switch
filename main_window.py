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

    def draw_fps(self, clock):
        # Get the current fps from the clock
        fps = int(clock.get_fps())

        # If the fps isn't 0, draw it onto the screen
        if fps != 0:
            # Get default font renderer
            my_font = pygame.font.Font(None, 50)

            # Render the fps label and print it in the top left of the screen
            fps_label = my_font.render(str(fps), True, (255,255,255))
            self.screen.blit(fps_label, (0, 0))

    def run(self):
        # Create a clock that will be used as a framerate monitor and limiter
        clock = pygame.time.Clock()

        game_running = True

        # While the user didn't exit the game, continue main loop (frames)
        while game_running:
            # Clear the screen by filling it with black color
            self.screen.fill((0, 0, 0))

            # Handle events
            for event in pygame.event.get():
                # Quit Event
                if event.type == pygame.QUIT:
                    game_running = False
                
                # Key down event
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.clicked()

            # Update the ball and get the obstacle y pos delta from it
            obstacle_delta : float = self.ball.update()

            # Update the obstacle using the given obstacle delta
            self.obs.update(obstacle_delta)

            # Draw current fps
            self.draw_fps(clock)

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(60)

        # Quit app after the user choose to quit
        pygame.quit()

MainWindow(800, 600).run()