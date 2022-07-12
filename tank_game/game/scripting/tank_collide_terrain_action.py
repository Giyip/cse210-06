import constants
import pyray
from game.scripting.action import Action
from game.casting.rectangle import Rectangle
from game.shared.point import Point

class TankCollideTerrainAction(Action):
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
        tanks = cast.get_actors("tanks")
        terrain = cast.get_first_actor("terrain")
        
        for tank in tanks:
            can_move = True
            #for line in terrain.get_surface():
            position_t = tank.get_position()
            size_t = tank.get_size()
            xt = position_t.get_x()
            yt = position_t.get_y() 
            width_t = size_t.get_x()
            height_t = size_t.get_y()
            rect_t = pyray.Rectangle(xt, yt, width_t, height_t)
            surface = terrain.get_surface()
            for i in range(len(surface)):
                for j in range(len(surface[0])):
                    #if surface[i][j] != 0 and surface[i][j] != 2 and surface[i][j] != 3:
                    position_r = surface[i][j].get_position()
                    size_r = surface[i][j].get_size()
                    xr = position_r.get_x()
                    yr = position_r.get_y()
                    width_r = size_r.get_x()
                    height_r = size_r.get_y()
                    rect_r = pyray.Rectangle(xr, yr, width_r, height_r)
                    if pyray.check_collision_recs(rect_t, rect_r):
                        can_move = False
                        break
                if not can_move:
                    break
            if can_move:
                tank.set_can_move(True)
            else:
                tank.set_can_move(False)
                tank.set_velocity(Point(0,0))
