from PIL import Image, ImageTk
import os

class BaseObstacle():
    def __init__(self, parent=None):
        # Save the parent
        self.parent = parent

        # Set default properties
        self.height = 0
        self.width = 0
        self.rotateAmount = 0
        self.image = None
        self.tk_image = None
        self.pil_image = None

        # Bind to the onload event, to init the pos of the obstacle
        self.parent.bind("<Map>", self.init_pos, add="+")

        self.parent.bind("<Map>", self.rotate, add="+")

    def init_pos(self, event):       
        # Place the obstacle(image) in the middle of the screen in the initial y pos
        self.image = self.parent.create_image(self.parent.winfo_width() / 2, -self.height, image=self.tk_image)

    def rotate(self, event=None):
        # Set the tkinter image as the original rotated with the current rotate amount
        self.tk_image = ImageTk.PhotoImage(self.pil_image.rotate(self.rotateAmount))

        # Set the tkinter image as the obstacle image
        self.parent.itemconfig(self.image, image=self.tk_image)

        # Increase rotate amount (Need to do modulo 360 in order to remove unnecessary full circle rotations)
        self.rotateAmount += 2
        self.rotateAmount %= 360

        self.parent.after(10, self.rotate)

    def move_obstacle(self, delta):
        # Place the obstacle in the new pos
        self.parent.move(self.image, 0, delta)