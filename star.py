from base.base_sprite import BaseSprite

class Star(BaseSprite):
    STAR_SIZE = 44

    def __init__(self, screen, y_pos):
        # Call the super constructor with the screen, no image, the size of the ball and the initial y pos
        BaseSprite.__init__(self, 
                            screen, 
                            "resources/star.png", 
                            (self.STAR_SIZE, self.STAR_SIZE),
                            y_pos)
