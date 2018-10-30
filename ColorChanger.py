from tkinter import Canvas

class ColorSwitcher(Canvas):
    def __init__(self, parent=None):
        
        Canvas.__init__(self, parent, height=50, width=50)
