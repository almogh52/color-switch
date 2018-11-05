import pygame
from ball import Ball
from map_sprites import MapSprites
from obstacles import *
from color_switcher import ColorSwitcher
from base.base_obstacle import BaseObstacle
import random

class MainWindow():
    BACKGROUND_COLOR = (35, 35, 35)
    MAX_FPS = 60
    DISTANCE_BETWEEN_SPRITES = 60

    def __init__(self, width, height):
        # Set the window size and pos
        self.rect = pygame.Rect(0, 0, width, height)

        # Initialize the pygame library
        pygame.init()

        # Create the window
        self.screen = pygame.display.set_mode(self.rect.size)

        # Create the ball
        self.ball = Ball(self.screen)

        # Create a group of sprites that will represent the map sprites
        self.map_sprites = MapSprites()
        
        # Add the first obstacle
        self.map_sprites.add(circle_obstacle.CircleObstacle(self.screen, self.screen.get_rect().height * 0.5 / 8))

        # Save the last sprite on the map
        self.last_sprite = ColorSwitcher(self.screen, self.screen.get_rect().height * 0.5 / 8 - self.DISTANCE_BETWEEN_SPRITES - ColorSwitcher.SWITCHER_BORDER - ColorSwitcher.SWITCHER_DIAMETER)

        # Add the first color switcher
        self.map_sprites.add(self.last_sprite)

        # Set the ball as not destroyed
        self.destroyed = False

    def draw_fps(self, clock):
        # Get the current fps from the clock
        fps = int(clock.get_fps())

        # If the fps is 0, set it as calculating
        if fps == 0:
            fps = "Calculating"

        # Get default font renderer
        my_font = pygame.font.Font(None, 30)

        # Render the fps label and print it in the top left of the screen
        fps_label = my_font.render(f"FPS: {fps}", True, (255,255,255))
        self.screen.blit(fps_label, (2, 2))

    def add_new_sprite(self, y_pos):
        LIST_OF_OBSTACLE_TYPES = [
            circle_obstacle.CircleObstacle,
            plus_obstacle.PlusObstacle
        ]

        # If the last sprite is an obstacle
        if issubclass(type(self.last_sprite), BaseObstacle):
            # Randomize whatever should be another obstacle or a color switcher (1 to 3 chance)
            if random.randint(0, 2) == 0:
                # Choose a random obstacle
                obstacle_type = random.choice(LIST_OF_OBSTACLE_TYPES)

                self.last_sprite = obstacle_type(self.screen, y_pos - obstacle_type.OBSTACLE_SIZE)
            else:
                # Add a color switcher
                self.last_sprite = ColorSwitcher(self.screen, y_pos - ColorSwitcher.SWITCHER_BORDER - ColorSwitcher.SWITCHER_DIAMETER)
        else:
            # Choose a random obstacle
            obstacle_type = random.choice(LIST_OF_OBSTACLE_TYPES)

            self.last_sprite = obstacle_type(self.screen, y_pos - obstacle_type.OBSTACLE_SIZE)

    def ball_destroyed(self):
        # Set the ball as destroyed
        self.destroyed = True

    def run(self):
        # Create a clock that will be used as a framerate monitor and limiter
        clock = pygame.time.Clock()

        game_running = True

        # While the user didn't exit the game, continue main loop (frames)
        while game_running:
            # Clear the screen by filling it with black color
            self.screen.fill(self.BACKGROUND_COLOR)

            # Handle events
            for event in pygame.event.get():
                # Quit Event
                if event.type == pygame.QUIT:
                    game_running = False
                
                # Key down event
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.destroyed:
                        self.ball.clicked()

            if not self.destroyed:
                # If the last sprite is almost entring screen, add a new sprite
                if -100 <= self.last_sprite.rect.y <= 0:
                    self.add_new_sprite(self.last_sprite.rect.y - self.DISTANCE_BETWEEN_SPRITES)
                    self.map_sprites.add(self.last_sprite)

                # Update the ball and get the map pos delta from it
                map_delta : float = self.ball.update()

                # Update the obstacle using the given obstacle delta
                self.map_sprites.update(map_delta)

                # Remove the hidden sprites from the screen
                self.map_sprites.remove_hidden_sprites(self.screen)

                # Check for all sprites on the map if they collide with the ball
                collided_sprites = self.map_sprites.check_collsion_with_ball(self.ball)

                # Handle each collided sprite
                for sprite in collided_sprites:
                    # Obstacle Handler
                    # If the sprite is a subclass of the base obstacle, it means the ball should explode
                    if issubclass(type(sprite), BaseObstacle):
                        self.ball_destroyed()

                    # Color Switcher Handler
                    elif type(sprite) == ColorSwitcher:
                        # Remove the color switcher from the screen
                        self.map_sprites.remove(sprite)

                        # Switch the ball's color
                        self.ball.switch_ball_color()
            else:
                pass

            # Draw current fps
            self.draw_fps(clock)

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(self.MAX_FPS)

        # Quit app after the user choose to quit
        pygame.quit()

MainWindow(800, 600).run()