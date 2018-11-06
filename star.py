from base.base_sprite import BaseSprite
import math
import pygame

class Star(BaseSprite):
    SCORE_BASE_POS = 5
    STAR_SIZE = 44
    ANIMATION_FRAMES = 110

    def __init__(self, screen, y_pos, taken_event):
        # Call the super constructor with the screen, no image, the size of the ball and the initial y pos
        BaseSprite.__init__(self, 
                            screen, 
                            "resources/star.png", 
                            (self.STAR_SIZE, self.STAR_SIZE),
                            y_pos)

        # Initial values
        self.picked = False
        self.speed = (0, 0)
        self.accleration = (0, 0)
        self.time = self.ANIMATION_FRAMES

        # Save handler for the taken event
        self.taken_event = taken_event

    def calc_accleration(self):
        # Calc the accleration for the y axis
        y_distance = self.rect.y - self.SCORE_BASE_POS
        y_acc = (2 * y_distance) / (self.time ** 2)

        # Calc the accleration for the x axis
        x_distance = self.rect.x - self.SCORE_BASE_POS
        x_acc = (2 * x_distance) / (self.time ** 2)

        self.accleration = (x_acc, y_acc)

    def pick(self):
        # Set the star as picked up and calculate the initial accleration
        self.picked = True
        self.calc_accleration()

    def update(self, map_delta):
        # If the star isn't picked up yet, update it normally
        if not self.picked:
            BaseSprite.update(self, map_delta)
        else:
            # Change speed by the accelration for each axis
            self.speed = (self.speed[0] + self.accleration[0], self.speed[1] + self.accleration[1])

            # Get the animation precentage (currect frame / total frame)
            precentage = self.time / self.ANIMATION_FRAMES

            # Fill the image with yellow by the animation frame
            self.image.fill((255, 211 + precentage * (255 - 211), precentage * 255), None, pygame.BLEND_MIN)

            # Change location by the speeds
            self.rect.x -= self.speed[0]
            self.rect.y -= self.speed[1]

            # If the star reached it's animation dest(at the score), kill it and call taken handler
            if self.rect.x <= self.SCORE_BASE_POS and self.rect.y <= self.SCORE_BASE_POS:
                self.taken_event()
                self.kill()
                return

            # Decrease the frame counter and re-calculate the accleration for both axis
            self.time -= 1
            self.calc_accleration()

            # Prefrom normal update
            BaseSprite.update(self, 0)