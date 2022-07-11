import pyray
import constants
import levels
from game.scripting.action import Action

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script, scene_manager):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores = cast.get_actors("scores")
        healths = cast.get_actors("healths")
        projectiles = cast.get_actors("projectiles")
        tanks = cast.get_actors("tanks")
        terrain = cast.get_first_actor("terrain")
        # messages = cast.get_actors("messages")

        # Verifying tank out of the window in the y axis
        for tank in tanks:
            position = tank.get_position()
            if position.get_y() >= constants.MAX_Y:
                if tank.get_text() == constants.ID_PLAYER1:
                    score = scores[1]
                    score.add_points(1)
                    health = healths[0]
                    health.update_value(0)
                else:
                    score = scores[0]
                    score.add_points(1)
                    health = healths[1]
                    health.update_value(0)
                scene_manager.change_scene = True
        self._video_service.clear_buffer()
        self._video_service.draw_actors(scores)
        self._video_service.draw_actors(healths)
        self._video_service.draw_projectiles(projectiles)
        self._video_service.draw_tanks(tanks)
        self._video_service.draw_terrain(terrain)
        # self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()

        if scene_manager.change_scene == True:
            pyray.wait_time(3000)
            scene_manager.scene += 1
            if scene_manager.scene in levels.LEVELS:
                self.reset(cast, script, scene_manager)
            else:
                scene_manager.game_over = True
                scene_manager.manage_game_over(cast, script)

    def reset(self, cast, script, scene_manager):
        """Resets the window for a new scene

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        if scene_manager.change_scene == True:
            scene_manager.prepare_scene(cast, script)
            scores = cast.get_actors("scores")
            healths = cast.get_actors("healths")
            tanks = cast.get_actors("tanks")
            terrain = cast.get_first_actor("terrain")
            # messages = cast.get_actors("messages")

            self._video_service.clear_buffer()
            self._video_service.draw_actors(scores)
            self._video_service.draw_actors(healths)
            self._video_service.draw_tanks(tanks)
            self._video_service.draw_terrain(terrain)
            # self._video_service.draw_actors(messages, True)
            self._video_service.flush_buffer()
            scene_manager.change_scene = False