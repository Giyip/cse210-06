import constants
import math
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.projectile import Projectile

class HandleMouseButtonPressed(Action):

    def __init__(self, mouse_service):
        self._mouse_service = mouse_service

    def execute(self, cast, script):
        if self._mouse_service.is_mouse_button_left_pressed():
            click_position = self._mouse_service.get_click_position()
            xc = click_position.get_x()
            yc = click_position.get_y()
            #print(f"x: {xc}, y: {yc}")
            # create  projectile
            tank2 = cast.get_actors("tanks")[1]
            position_t = tank2.get_position()
            xp = int(position_t.get_x() + constants.WIDTH_PLAYER1 / 2)
            yp = int(position_t.get_y() - constants.HEIGHT_PLAYER1 / 2) 
            position_p = Point(xp, yp)
            h = math.sqrt(math.pow(yc - yp, 2) + math.pow(xc - xp, 2))
            theta = int(math.asin((yc - yp) / h) * 180 / math.pi)
            if xc > xp:
                theta = - theta
            else:
                theta = 180 + theta
            #elif xc < xp and yc < yp:
            #    theta = 180 + theta
            #elif xc < xp and yc > yp:
            #    theta = 180 - theta
            projectile = Projectile(position_p, constants.PROJECTILE_RADIUS, constants.PROJECTILE_EXAMPLE_V0, theta)
            cast.add_actor("projectiles", projectile)
    