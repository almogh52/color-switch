import pygame

class Window(object):
    BACKGROUND_COLOR = (35, 35, 35)
    MAX_FPS = 60

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        # Create a clock that will be used as a framerate monitor and limiter
        clock = pygame.time.Clock()

        app_running = True

        # While the user didn't exit the game, continue main loop (frames)
        while app_running:
            # Clear the screen by filling it with black color
            self.screen.fill(self.BACKGROUND_COLOR)

            # Handle events
            for event in pygame.event.get():
                # Quit Event
                if event.type == pygame.QUIT:
                    app_running = False

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(self.MAX_FPS)