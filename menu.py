from base.base_window import Window
from base.base_sprite import BaseSprite
from obstacles.circle_obstacle import CircleObstacle
from main_window import MainWindow
from help import Help
import pygame
import os

# Set the screen to be centered
os.environ['SDL_VIDEO_CENTERED'] = '1'

class Menu(Window):
    TITLE_SIZE = (900, 225)
    TITLE_Y = 0

    PLAY_BUTTON_SIZE = (150, 150)
    PLAY_BUTTON_Y = 281

    CIRCLE_1_Y = 224
    CIRCLE_2_Y = 255
    CIRCLE_2_SIZE = 200

    def __init__(self, width, height):
        # Set the window size and pos
        self.rect = pygame.Rect(0, 0, width, height)

        # Initialize the pygame library
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode(self.rect.size)

        # Set the game's name
        pygame.display.set_caption("Color Switch")

        # Create the title
        self.title_sprite = BaseSprite(self.screen,
                                       "resources/title.png",
                                       self.TITLE_SIZE,
                                       self.TITLE_Y)

        # Create the play button
        self.play_btn = BaseSprite(self.screen,
                                   "resources/play.png",
                                   self.PLAY_BUTTON_SIZE,
                                   self.PLAY_BUTTON_Y)

        self.help_btn = BaseSprite(self.screen,
                                   "resources/help.png",
                                   (187, 75),
                                   520)

        # Create a group of sprites with the sprites
        self.sprites = pygame.sprite.Group(self.play_btn, self.title_sprite, self.help_btn)

        # Add the circles for the outside of the play button
        self.sprites.add(CircleObstacle(self.screen, self.CIRCLE_1_Y, angle_delta=1))
        self.sprites.add(CircleObstacle(self.screen, self.CIRCLE_2_Y, size=self.CIRCLE_2_SIZE, angle_delta=-1))

    def draw_credit(self):
        # Get default font renderer
        my_font = pygame.font.Font("resources/Bonk.ttf", 24)

        # Render the credit label
        credit_label = my_font.render("© 2018 Almog Hamdani", True, (255,255,255))

        # Get the rect of the label and calculate it's position
        credit_rect = credit_label.get_rect()
        credit_pos = (self.screen.get_rect().width / 2 - credit_rect.width / 2, self.screen.get_rect().height - credit_rect.height - 10)

        self.screen.blit(credit_label, credit_pos)

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

            self.draw_credit()

            # Update all the sprites
            self.sprites.update()

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(self.MAX_FPS)

Menu(1150, 680).run()