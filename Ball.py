from tkinter import Canvas


class Ball(Canvas):
    BALL_DIAMETER = 25

    BALL_ACCELERATION = -0.10
    MAX_SPEED = 4.5

    BALL_TIMER_TICK = 7

    def __init__(self, parent=None, main=None):
        Canvas.__init__(self, parent, height=self.BALL_DIAMETER, width=self.BALL_DIAMETER, bg="black", bd=0, highlightthickness=0)

        # Save the parent and the main window
        self.parent = parent
        self.main = main

        # Create the ball
        self.oval = self.create_oval(0, 0, self.BALL_DIAMETER, self.BALL_DIAMETER, fill="white")

        # Initial y pos
        self.y = 250

        # Initial speed is 0
        self.speed = 0

        # Start the player's update when the window is loaded
        self.parent.bind("<Map>", self.update, add="+")

        # Bind to the event 
        self.parent.bind("<Button-1>", self.mouse_click)

    def mouse_click(self, event):
        # When the mouse is clicked, reset the ball's speed to MAX_SPEED
        self.speed = self.MAX_SPEED

    def update(self, event):
        # Change speed using acceleration
        self.speed = self.speed + self.BALL_ACCELERATION

        print(self.speed)

        # If the new y pos is smaller than the middle of the screen (if the ball need to pass the middle), move the obstacles
        if self.y - self.speed <= self.parent.winfo_height() / 2 - self.BALL_DIAMETER / 2:
            # Move all obstacles
            self.main.move_obstacles(self.speed)
        else:
            # Set ball's y pos using the speed
            self.y -= self.speed

        # Place the ball in it's x and y
        self.place(x=self.parent.winfo_width() / 2 - self.BALL_DIAMETER / 2, y=self.y)

        # Schedule this to happen again after 10ms
        self.after(self.BALL_TIMER_TICK, self.update, event)

