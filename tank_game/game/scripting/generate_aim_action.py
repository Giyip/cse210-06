import constants
import math
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.projectile import Projectile

class GenerateAimAction(Action):

    def __init__(self, mouse_service):
        self._mouse_service = mouse_service

    def execute(self, cast, script, scene_manager):
        player = scene_manager.who_plays
        cursor_position = self._mouse_service.get_cursor_position()
        xc = cursor_position.get_x()
        yc = cursor_position.get_y()
        projections = []
        
        if player == constants.ID_PLAYER1:
            # create  projections for the player 1
            tank1 = cast.get_actors("tanks")[0]
            position_t = tank1.get_position()
            xp = int(position_t.get_x() + constants.WIDTH_PLAYER1 / 2)
            yp = int(position_t.get_y() - constants.HEIGHT_PLAYER1 / 2) 
            position_p = Point(xp, yp)
            h = math.sqrt(math.pow(yc - yp, 2) + math.pow(xc - xp, 2))
            theta = int(math.asin((yc - yp) / h) * 180 / math.pi)
            if xc > xp:
                theta = - theta
            else:
                theta = 180 + theta
            color = tank1.get_color()
            projectile = Projectile(position_p, constants.PROJECTION_RADIUS, constants.PROJECTILE_EXAMPLE_V0, theta)
            projectile.set_color(color)
            projections.append(projectile)
            for i in range(1,11):
                pp = projectile.calculate_projection_position(constants.TIME_RATE * i)
                projection = Projectile(pp, constants.PROJECTION_RADIUS, constants.PROJECTILE_EXAMPLE_V0, theta)
                projection.set_color(color)
                projections.append(projection)
        else:
            # create  projections for the player 2
            tank2 = cast.get_actors("tanks")[1]
            position_t = tank2.get_position()
            xp = int(position_t.get_x() + constants.WIDTH_PLAYER2 / 2)
            yp = int(position_t.get_y() - constants.HEIGHT_PLAYER2 / 2) 
            position_p = Point(xp, yp)
            h = math.sqrt(math.pow(yc - yp, 2) + math.pow(xc - xp, 2))
            theta = int(math.asin((yc - yp) / h) * 180 / math.pi)
            if xc > xp:
                theta = - theta
            else:
                theta = 180 + theta
            color = tank2.get_color()
            projectile = Projectile(position_p, constants.PROJECTION_RADIUS, constants.PROJECTILE_EXAMPLE_V0, theta)
            projectile.set_color(color)
            projections.append(projectile)
            for i in range(1,11):
                pp = projectile.calculate_projection_position(constants.TIME_RATE * i)
                projection = Projectile(pp, constants.PROJECTION_RADIUS, constants.PROJECTILE_EXAMPLE_V0, theta)
                projection.set_color(color)
                projections.append(projection)
        scene_manager.projectile_projections = projections