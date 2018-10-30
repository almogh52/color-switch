from PIL import Image, ImageTk
import os
from BaseObstacle import BaseObstacle

class Obstacle(BaseObstacle):
    def __init__(self, parent):
        BaseObstacle.__init__(self, parent)

        # Set this obstacle properties
        self.width = 200
        self.height = 200

        # Set rotate as 0
        self.rotateAmount = 0

        # Open the obstacle image
        self.pil_image = Image.open(os.path.dirname(os.path.abspath(__file__)) + r"/Resources/Obstacle.png")
        self.pil_image = self.pil_image.resize((200, 200), Image.BICUBIC)

        # Create a tkinter image from the pil image
        self.tk_image = ImageTk.PhotoImage(self.pil_image)

        self.parent.bind("<Map>", self.rotate, add="+")

    
    def rotate(self, event=None):
        # Set the tkinter image as the original rotated with the current rotate amount
        self.tk_image = ImageTk.PhotoImage(self.pil_image.rotate(self.rotateAmount))

        # Set the tkinter image as the obstacle image
        self.parent.itemconfig(self.image, image=self.tk_image)

        # Increase rotate amount (Need to do modulo 360 in order to remove unnecessary full circle rotations)
        self.rotateAmount += 2
        self.rotateAmount %= 360

        self.parent.after(10, self.rotate)

    def is_obstacle_collide_with_ball(self, ball):
        obstacle_coords = self.parent.coords(self.image)
        ball_coords = self.parent.coords(ball.image)

        #print(obstacle_coords)
        #print(ball_coords)

        collision_point = (ball_coords[0], ball_coords[1] - ball.BALL_DIAMETER // 2)

        if collision_point[1] >= obstacle_coords[1] - self.height / 2 and collision_point[1] <= obstacle_coords[1] + self.height / 2:
            current_image = self.pil_image.rotate(self.rotateAmount)
            
            collision_pixel = (int(collision_point[0] - (obstacle_coords[0] - self.width / 2)), int(collision_point[1] - (obstacle_coords[1] - self.height / 2)))
            #print(collision_pixel)

            if int(collision_pixel[1]) < self.height and current_image.getpixel(collision_pixel) != (0, 0, 0, 0):
                color = current_image.getpixel(collision_pixel)
                if ball.check_ball_color(color):
                    print("DJDJD")

        else:
            return False
    
