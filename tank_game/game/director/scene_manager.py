import constants
import levels
import pyray

from game.casting.score import Score
from game.casting.health import Health
from game.casting.tank import Tank
from game.scripting.control_tank1_action import ControlTank1Action
from game.scripting.control_tank2_action import ControlTank2Action
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.projectile_collide_terrain_action import ProjectileCollideTerrainAction
from game.scripting.projectile_collide_tank_action import ProjectileCollideTankAction
from game.scripting.handle_mouse_button_pressed import HandleMouseButtonPressed
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.mouse_service import MouseService
from game.shared.point import Point
from game.casting.terrain import Terrain
from game.casting.welcome import Welcome
from game.casting.level_winner import LevelWinner
from game.casting.end import End
from game.scripting.tank_collide_terrain_action import TankCollideTerrainAction
from game.scripting.generate_aim_action import GenerateAimAction

class SceneManager:

    def __init__(self):
        self.KEYBOARD_SERVICE = KeyboardService()
        self.VIDEO_SERVICE = VideoService()
        self.MOUSE_SERVICE = MouseService()
        self.game_over = False
        self.scene = 0
        self.change_scene = False
        self.who_plays = constants.ID_PLAYER1
        self.projectile_projections = []
        self.welcome_message = Welcome("Welcome! Use the mouse to aim and click to lauch projectile.")
        self.level_winner = LevelWinner(constants.ID_PLAYER1)
        self.end_message = End(constants.ID_PLAYER1)

    def _add_welcome_message(self, cast):
        """Prepares welcome message
        Args:
            cast (Cast): the cast of actors
        """
        self.welcome_message.set_position(Point(260, 130))
        cast.add_actor("welcome", self.welcome_message)

    def _remove_welcome_message(self):
        """Removes welcome message
        """
        self.welcome_message.remove_message()

    def _add_level_winner(self, cast):
        """Prepares level message
        Args:
            cast (Cast): the cast of actors
        """
        healths = cast.get_actors("healths")
        if healths[0].get_value() == 0:
            self.level_winner.update_winner(constants.ID_PLAYER2)
        else:
            self.level_winner.update_winner(constants.ID_PLAYER1)
        self.level_winner.set_position(Point(360, 130))
        cast.add_actor("LevelWinner", self.level_winner)

    def _remove_level_message(self):
        """Removes level message
            """
        self.level_winner.remove_message()

    def _add_end_message(self, cast):
        """Prepares end message
            Args:
                cast (Cast): the cast of actors
            """
        self.end_message.set_position(Point(360, 130))
        cast.add_actor("end", self.end_message)

    def prepare_scene(self, cast, script):
        """Prepares a new scene
        Args:
            scene (integer): the id of scene to prepare
            cast (Cast): the cast of actors
            script (Script): the script of actions
        """
        if self.scene == 0:
            self._add_terrain(cast)
            self._add_tanks(cast)
            self._add_stats(cast)
            self._add_welcome_message(cast)
            self._add_actions(script)
        else:
            cast.remove_actors("terrain")
            cast.remove_actors("tanks")
            cast.remove_actors("projectiles")
            self._remove_welcome_message()
            if self.scene < 10:
                self._add_level_winner(cast)
            else:
                self._remove_level_message()
                self._add_end_message(cast)
            self._add_terrain(cast)
            self._add_tanks(cast)
            self._reset_healths(cast)

    def _add_tanks(self, cast):
        """Adds tanks on a new scene
        Args:
            scene (integer): the id of scene to prepare
            cast (Cast): the cast of actors
        """
        terrain = cast.get_first_actor("terrain")
        position_tank1 = terrain.get_tank_position(constants.ID_PLAYER1)    
        size1 = Point(constants.WIDTH_PLAYER1, constants.HEIGHT_PLAYER1)
        tank1 = Tank(size1)
        tank1.set_position(position_tank1)
        tank1.set_text(constants.ID_PLAYER1)
        tank1.set_color(constants.YELLOW)

        position_tank2 = terrain.get_tank_position(constants.ID_PLAYER2)
        size2 = Point(constants.WIDTH_PLAYER2, constants.HEIGHT_PLAYER2)
        tank2 = Tank(size2)
        tank2.set_position(position_tank2)
        tank2.set_text(constants.ID_PLAYER2)
        tank2.set_color(constants.GREEN)

        if self.scene == 10:
            scores = cast.get_actors("scores")
            if scores[0].get_points() < scores[1].get_points():
                cast.add_actor("tanks", tank1)
            else:
                cast.add_actor("tanks", tank2)
        else:
            cast.add_actor("tanks", tank1)
            cast.add_actor("tanks", tank2)

    def _add_stats(self, cast):
        """Adds stats on a new scene
        Args:
            scene (integer): the id of scene to prepare
            cast (Cast): the cast of actors
        """
        # create the scores
        score1 = Score("Tank 1")
        score2 = Score("Tank 2")
        score2.set_position(Point(constants.MAX_X-7*constants.CELL_SIZE, 0))

        # create the healths
        health1 = Health(constants.PLAYERS_HEALTH)
        health2 = Health(constants.PLAYERS_HEALTH)
        health1.set_position(Point(2, 20))
        health2.set_position(Point(constants.MAX_X-7*constants.CELL_SIZE, 20))

        # add scores and healths to the cast
        cast.add_actor("scores", score1)
        cast.add_actor("scores", score2)
        cast.add_actor("healths", health1)
        cast.add_actor("healths", health2)

    def _add_terrain(self, cast):
        """Adds the terrain on a new scene
        Args:
            scene (integer): the id of scene to prepare
            cast (Cast): the cast of actors
        """
        terrain = Terrain(levels.LEVELS[self.scene])
        terrain.set_text("terrain")
        terrain.set_color(constants.SIENNA)
        cast.add_actor("terrain", terrain)

    def _add_actions(self, script):
        """Adds the actions on a new scene
        Args:
            scene (integer): the id of scene to prepare
            script (Script): the script of actions
        """
        #script.add_action("input", ControlTank1Action(self._KEYBOARD_SERVICE))
        #script.add_action("input", ControlTank2Action(self._KEYBOARD_SERVICE))
        script.add_action("input", HandleMouseButtonPressed(self.MOUSE_SERVICE, constants.ID_PLAYER1))
        script.add_action("input", GenerateAimAction(self.MOUSE_SERVICE))
        script.add_action("update", MoveActorsAction())
        script.add_action("update", ProjectileCollideTankAction())
        script.add_action("update", ProjectileCollideTerrainAction())
        script.add_action("update", TankCollideTerrainAction())
        script.add_action("output", DrawActorsAction(self.VIDEO_SERVICE))

    def _reset_healths(self, cast):
        """Resets the healths for a new scene
        Args:
            scene (integer): the id of scene to prepare
            cast (Cast): the cast of actors
        """
        # create the healths
        healths = cast.get_actors("healths")
        health1 = healths[0]
        health2 = healths[1]
        health1.update_value(constants.PLAYERS_HEALTH)
        health2.update_value(constants.PLAYERS_HEALTH)

    def manage_game_over(self, cast, script):
        """Manages game over
        Args:
            scene (integer): the id of scene to manage
            cast (Cast): the cast of actors
            script (Script): the script of actions
        """
        pass
        # end = End(levels.LEVELS[self.scene])
        # cast.add_actor("end", end)