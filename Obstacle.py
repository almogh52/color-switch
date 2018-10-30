from tkinter import Canvas
from BaseObstacle import BaseObstacle

class Obstacle(BaseObstacle):
    def __init__(self, parent):
        BaseObstacle.__init__(self, parent)

        # Set this obstacle properties
        self.width = 100
        self.height = 100
        self.y = -self.height

        # Init the canvas super class
        Canvas.__init__(self, parent, height=self.height, width=self.width, bg="white", bd=0, highlightthickness=0)

        # Set the obstacle's initial pos
        self.place(x=self.parent.winfo_width() / 2 - self.width / 2, y=self.y)
    
