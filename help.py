from base.base_window import Window
from base.base_sprite import BaseSprite

class Help(Window):
    def __init__(self, screen):
        Window.__init__(self, screen)

        self.screen = screen

        self.sprites.add(BaseSprite(screen,
                                    "resources/help.png",
                                    (1150, 650),
                                    0))