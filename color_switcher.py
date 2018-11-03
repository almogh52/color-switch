from base.base_sprite import BaseSprite

class ColorSwitcher(BaseSprite):
    SWITCHER_BORDER = 5
    SWITCHER_DIAMETER = 35

    def __init__(self, screen, y_pos):
        # Call the super constructor with the screen, the image and the size of the switcher
        BaseSprite.__init__(self, 
                            screen, 
                            "resources/switcher.png", 
                            (self.SWITCHER_DIAMETER + self.SWITCHER_BORDER, self.SWITCHER_DIAMETER + self.SWITCHER_BORDER),
                            y_pos)