from tkinter import Canvas
from abc import ABC, abstractmethod

class BaseObstacle(ABC, Canvas):
    def __init__(self, parent=None):
        # Save the parent
        self.parent = parent

        # Set default properties
        self.height = 0
        self.width = 0
        self.y = 0

        # Bind to the onload event, to init the pos of the obstacle
        self.parent.bind("<Map>", self.init_pos, add="+")

        # Create an abstract class
        ABC.__init__(self)

    def init_pos(self, event):       
        # Place the obstacle in the new pos
        self.place(x=self.parent.winfo_width() / 2 - self.width / 2, y=self.y)

    def move_obstacle(self, delta):
        # Add the delta to y pos
        self.y += delta

        # Place the obstacle in the new pos
        self.place(x=self.parent.winfo_width() / 2 - self.width / 2, y=self.y)