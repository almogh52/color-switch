from base.base_sprite import BaseSprite
from star import Star
import utils

class BaseObstacle(BaseSprite):
    OBSTACLE_SIZE = 0

    def get_collision_point(self, ball):
        return (0, 0)

    def position_for_star(self):
        return self.rect.y + (self.height / 2 - Star.STAR_SIZE / 2)

    def check_collsion_with_ball(self, ball):
        # Get the collision point of the obstacle and the ball
        collision_point = self.get_collision_point(ball)

        # If the obstacle and the ball don't collide, return false
        if collision_point is None:
            return False

        # Try to get the color of the collision point from the screen
        try:
            color = self.screen.get_at(collision_point)
        except:
            # Default color - black color
            color = (0, 0, 0, 255)

        # If the color isn't black and isn't the ball's color, return true
        if not utils.color_is_black(color) and not utils.compare_colors(color, ball.color):
            return True

        return False