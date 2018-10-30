from PIL import Image, ImageTk
import os

class BaseObstacle():
    def __init__(self, parent=None):
        # Save the parent
        self.parent = parent

        # Set default properties
        self.height = 0
        self.width = 0
        self.tk_image = None
        self.image = None

        # Bind to the onload event, to init the pos of the obstacle
        self.parent.bind("<Map>", self.init_pos, add="+")

    def init_pos(self, event):       
        # Place the obstacle(image) in the middle of the screen in the initial y pos
        self.image = self.parent.create_image(self.parent.winfo_width() / 2, -self.height, image=self.tk_image)

    def move_obstacle(self, delta):
        # Place the obstacle in the new pos
        self.parent.move(self.image, 0, delta)