import constants
import pyray
from game.scripting.action import Action

class ProjectileCollideTerrainAction(Action):
    """
    An update action that checks the collision between the projectile and the terrain (also the limits of the window)

    The responsibility of ProjectileCollideTerrainAction is to check the collisions between the projectile and the terrain.
    """
    def execute(self, cast, script):
        """Executes the projectile collide terrain action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        projectiles = cast.get_actors("projectiles")
        terrain = cast.get_first_actor("terrain")

        for projectile in projectiles:
            #for line in terrain.get_surface():
            position_p = projectile.get_position()
            x = position_p.get_x()
            y = position_p.get_y()
            results = terrain.calculate_new_position(x)
            x_terrain = x
            y_terrain = results["y"]
            #point = pyray.Vector2(x_terrain, y_terrain)
            aux_rect = pyray.Rectangle(x_terrain - 5, y_terrain, 10, constants.MAX_Y - y_terrain)
            center = pyray.Vector2(x, y)
            radius = projectile.get_radius()
            #if pyray.check_collision_point_circle(point, center, radius):
            if pyray.check_collision_circle_rec(center, radius, aux_rect):
                cast.remove_actor("projectiles", projectile)
            elif x >= constants.MAX_X or x <= 0:
                cast.remove_actor("projectiles", projectile)