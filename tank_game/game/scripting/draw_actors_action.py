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

    def execute(self, cast, script):
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

        self._video_service.clear_buffer()
        self._video_service.draw_actors(scores)
        self._video_service.draw_actors(healths)
        self._video_service.draw_projectiles(projectiles)
        self._video_service.draw_tanks(tanks)
        self._video_service.draw_terrain(terrain)
        # self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()