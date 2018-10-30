from tkinter import Tk, Frame, Canvas
from Ball import Ball
from Obstacle import Obstacle


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # Save the master window and change the title
        self.master = master
        self.master.title("Color Switch")

        # Set the frame to full the entire window
        self.pack(fill="both", expand=True)

        # Create the main canvas and add it to
        self.canvas = Canvas(self, bg="black")
        self.canvas.pack(fill="both", expand=True)

        # Create the ball and add it to the window
        self.obs = Obstacle(self.canvas)
        #self.canvas.create_window(0, 0, window=self.obs)
        
        # Create the ball and add it to the window
        self.ball = Ball(self.canvas, self)

    def move_obstacles(self, delta):
        self.obs.move_obstacle(delta)

# Create root window and create the main window and start the main loop
root = Tk()
root.geometry("500x500")

app = MainWindow(master=root)
app.mainloop()