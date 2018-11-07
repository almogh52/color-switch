from base.base_window import Window
from base.base_sprite import BaseSprite
from main_window import MainWindow
import pygame

class Menu(Window):
    PLAY_BUTTON_SIZE = (150, 150)
    PLAY_BUTTON_Y = 75

    def __init__(self, width, height):
        # Set the window size and pos
        self.rect = pygame.Rect(0, 0, width, height)

        # Initialize the pygame library
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode(self.rect.size)

        # Create the play button
        self.play_btn = BaseSprite(self.screen,
                              "resources/play.png",
                              self.PLAY_BUTTON_SIZE,
                              self.PLAY_BUTTON_Y)

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

                # Mouse button down event
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # If the play button was clicked, run the game
                    if self.play_btn.rect.collidepoint(event.pos):
                        MainWindow(self.screen).run()

            # Update the play button
            self.play_btn.update()

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(self.MAX_FPS)

Menu(800, 600).run()