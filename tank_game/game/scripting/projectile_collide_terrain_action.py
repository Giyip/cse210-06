import constants
import pyray
from game.scripting.action import Action
from game.casting.rectangle import Rectangle
from game.shared.point import Point

class ProjectileCollideTerrainAction(Action):
    """
    An update action that checks the collision between the projectile and the terrain (also the limits of the window)

    The responsibility of ProjectileCollideTerrainAction is to check the collisions between the projectile and the terrain.
    """
    def execute(self, cast, script, scene_manager):
        """Executes the projectile collide terrain action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        projectiles = cast.get_actors("projectiles")
        terrain = cast.get_first_actor("terrain")
        remove_projectile = False
        for projectile in projectiles:
            position_p = projectile.get_position()
            x = position_p.get_x()
            y = position_p.get_y() 
            if x >= constants.MAX_X or x <= 0:
                cast.remove_actor("projectiles", projectile)
                continue
            if y >= constants.MAX_Y:
                cast.remove_actor("projectiles", projectile)
                continue
            center = pyray.Vector2(x, y)
            radius = projectile.get_radius()
            surface = terrain.get_surface()
            for i in range(len(surface)):
                for j in range(len(surface[0])):
                    position = surface[i][j].get_position()
                    size = surface[i][j].get_size()
                    xt = position.get_x()
                    yt = position.get_y()
                    width = size.get_x()
                    height = size.get_y()
                    rect = pyray.Rectangle(xt, yt, width, height)
                    if pyray.check_collision_circle_rec(center, radius, rect):
                        remove_projectile = True
                        surface[i][j] = Rectangle(Point(0,0),Point(0,0))
                        break
                if remove_projectile:
                    break
            if remove_projectile:        
                cast.remove_actor("projectiles", projectile)
                remove_projectile = False