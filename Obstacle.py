from PIL import Image, ImageTk
import os
from BaseObstacle import BaseObstacle

class Obstacle(BaseObstacle):
    def __init__(self, parent):
        BaseObstacle.__init__(self, parent)

        # Set this obstacle properties
        self.width = 200
        self.height = 200

        # Open the obstacle image
        self.pil_image = Image.open(os.path.dirname(os.path.abspath(__file__)) + r"/Resources/Obstacle.png")
        self.pil_image = self.pil_image.resize((200, 200), Image.BICUBIC)

        self.tk_image = ImageTk.PhotoImage(self.pil_image)
    
