import pyray
import constants
from game.scripting.action import Action


class ProjectileCollideTankAction(Action):
    """
    An update action that handles the collision of the projectiles with the tanks

    The responsibility of ProjectileCollideTankAction is to handle the collision of the projectiles with the tanks
    """

    def __init__(self):
        self._is_game_over = False
        self._winner = ""
        #self._destroy_projectile = False


    def execute(self, cast, script):
        """Executes the projectile collide tank action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_projectile_collide_tank(cast)
        
    def _handle_projectile_collide_tank(self, cast):
        """Handles the projectile collide tank action.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        healths = cast.get_actors("healths")
        scores = cast.get_actors("scores")
        tanks = cast.get_actors("tanks")
        projectiles = cast.get_actors("projectiles")
        for projectile in projectiles:
            radius = projectile.get_radius()
            position = projectile.get_position()
            center = pyray.Vector2(position.get_x(), position.get_y())
            destroy_projectile = False
            
            for tank in tanks:
                rect = tank.get_rectangle()
                if pyray.check_collision_circle_rec(center, radius, rect):
                    if tank.get_text() == constants.ID_PLAYER1:
                        value = healths[0].get_value()
                        value -= constants.PROJECTILE_POWER
                        healths[0].update_value(value)
                        if value <= 0:
                            self._winner = constants.ID_PLAYER2
                            scores[1].add_points(1)
                            healths[0].update_value(constants.PLAYERS_HEALTH)
                    elif tank.get_text() == constants.ID_PLAYER2:
                        value = healths[1].get_value()
                        value -= constants.PROJECTILE_POWER
                        healths[1].update_value(value)
                        if value <= 0:
                            self._winner = constants.ID_PLAYER1
                            scores[0].add_points(1)
                            healths[1].update_value(constants.PLAYERS_HEALTH)
                    destroy_projectile = True
                    break
            if destroy_projectile:
                cast.remove_actor("projectiles", projectile)