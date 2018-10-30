import pygame

class MainWindow():
    def __init__(self, width, height):
        # Set the window size and pos
        self.rect = pygame.Rect(0, 0, width, height)

        # Initialize the pygame library
        pygame.init()

        # Create the window
        self.display = pygame.display.set_mode(self.rect.size)

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

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(60)

        # Quit app after the user choose to quit
        pygame.quit()

MainWindow(800, 600).run()