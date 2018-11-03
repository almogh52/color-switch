import pygame
from ball import Ball
from map_sprites import MapSprites
from obstacles.circle_obstacle import CircleObstacle
from color_switcher import ColorSwitcher

class MainWindow():
    BACKGROUND_COLOR = (35, 35, 35)

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
        self.map_sprites.add(CircleObstacle(self.screen))

        # Add the first color switcher
        self.map_sprites.add(ColorSwitcher(self.screen))

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
                    if event.key == pygame.K_SPACE:
                        self.ball.clicked()

            # Update the ball and get the map pos delta from it
            map_delta : float = self.ball.update()

            # Update the obstacle using the given obstacle delta
            self.map_sprites.update(map_delta)

            # Check for all sprites on the map if they collide with the ball
            collided_sprites = self.map_sprites.check_collsion_with_ball(self.ball)

            # Handle each collided sprite
            for sprite in collided_sprites:
                # Obstacle Handler
                if type(sprite) == CircleObstacle:
                    print("Dead")

                # Color Switcher Handler
                elif type(sprite) == ColorSwitcher:
                    # Remove the color switcher from the screen
                    self.map_sprites.remove(sprite)

                    # Switch the ball's color
                    self.ball.switch_ball_color()

            # Draw current fps
            self.draw_fps(clock)

            # Update the display each frame
            pygame.display.update()

            # Limit to 60 fps
            clock.tick(60)

        # Quit app after the user choose to quit
        pygame.quit()

MainWindow(800, 600).run()