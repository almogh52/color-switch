from tkinter import Frame
from PIL import ImageTk, Image
import random
import os

class Ball():
    # Consts
    BALL_BORDER = 5
    BALL_DIAMETER = 25

    BALL_ACCELERATION = -0.10
    MAX_SPEED = 4.5

    BALL_TIMER_TICK = 7

    def __init__(self, parent=None, main=None):
        # Save the parent and the main window
        self.parent = parent
        self.main = main

        # Open the image of the ball and resize to it's small size
        image = Image.open(os.path.dirname(os.path.abspath(__file__)) + r"/Resources/Ball/Pink.png")
        image = image.resize((self.BALL_DIAMETER + self.BALL_BORDER, self.BALL_DIAMETER + self.BALL_BORDER), Image.ANTIALIAS)

        # Create a tkinter image from the PIL image
        self.image_pil = ImageTk.PhotoImage(image=image)

        # Set the initial image as None since it is created on the onload event
        self.image = None

        self.color = (255, 0, 130)

        # Initial speed is 0
        self.speed = 0

        # Bind to the onload event, to init the pos of the obstacle
        self.parent.bind("<Map>", self.init_pos, add="+")

        # Start the player's update when the window is loaded
        self.parent.bind("<Map>", self.update, add="+")

        # Bind to the event 
        self.parent.bind("<Button-1>", self.mouse_click)

    def init_pos(self, event):
        # Create the ball as an image in the parent canvas in the middle of the screen
        self.image = self.parent.create_image(self.parent.winfo_width() / 2, self.parent.winfo_height() * 2 / 3, image=self.image_pil)

    def mouse_click(self, event):
        # When the mouse is clicked, reset the ball's speed to MAX_SPEED
        self.speed = self.MAX_SPEED

    def check_ball_color(self, color):
        for i in range(3):
            if not (self.color[i] - 10 <= color[i] <= self.color[i] + 10):
                return False

        return True

    def update(self, event):
        # Change speed using acceleration
        self.speed = self.speed + self.BALL_ACCELERATION

        # If the new y pos is smaller than the middle of the screen (if the ball need to pass the middle), move the obstacles
        if self.parent.coords(self.image)[1] - self.speed <= self.parent.winfo_height() / 2 - self.BALL_DIAMETER / 2:
            # Move all obstacles
            self.main.move_obstacles(self.speed)
        else:
            # Move the ball in the y axis by it's speed
            self.parent.move(self.image, 0, -self.speed)

        # Schedule this to happen again after 10ms
        self.parent.after(self.BALL_TIMER_TICK, self.update, event)

