import utils
from base.base_sprite import BaseSprite

class Ball(BaseSprite):
    BALL_BORDER = 5
    BALL_DIAMETER = 25

    MAX_SPEED = 7.6
    ACCELERATION = 0.35

    def __init__(self, screen):
        # Call the super constructor with the screen, no image, the size of the ball and the initial y pos
        BaseSprite.__init__(self, 
                            screen, 
                            None, 
                            (self.BALL_DIAMETER + self.BALL_BORDER, self.BALL_DIAMETER + self.BALL_BORDER),
                            screen.get_rect().height * 2 / 3)

        # Start the player's speed as 0
        self.speed = 0

        # Set initial ball's image file as None to be used in the switch ball color
        self.image_file = None

        # Set a random color for the ball
        self.switch_ball_color()

    def switch_ball_color(self):
        image_file_path = utils.random_file_from_folder("Resources/Ball")

        # While the new image file is the same as the previous image, request a new one
        while image_file_path == self.image_file:
            # Get a random ball image from the ball images folder
            image_file_path = utils.random_file_from_folder("Resources/Ball")

        # Set the image file as the new image file path
        self.image_file = image_file_path

        # Load the ball image and resize it to it's size by the diameter + border
        self.image = utils.load_and_resize_image(self.image_file, (self.BALL_DIAMETER + self.BALL_BORDER, self.BALL_DIAMETER + self.BALL_BORDER))

        # Get the most used color in the image and use it as the ball's color
        self.color = utils.get_dominant_color_from_image(self.image_file)

    def clicked(self):
        # Set speed to max speed
        self.speed = self.MAX_SPEED

    def update(self):
        map_delta = 0

        # Change speed according to the acceleration
        self.speed -= self.ACCELERATION

        # If the new y pos is smaller than the middle of the screen (if the ball need to pass the middle), set the obstacle delta as the speed
        if self.rect.y - self.speed <= self.screen.get_rect().height / 2 - self.height / 2:
            # Move the obstacles by the current speed
            map_delta = self.speed
        else:
            # Change the y pos using the speed
            self.rect.y -= self.speed

        # Draw the image on the screen
        self.screen.blit(self.image, self.rect)

        return map_delta