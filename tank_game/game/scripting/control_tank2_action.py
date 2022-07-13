import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlTank2Action(Action):
    """
    An input action that controls the Tank 1.

    The responsibility of ControlTank1Action is to get the direction and move the tank 1.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new class ControlTank1Action(Action): using the specified KeyboardService.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, scene_manager):
        """Executes the control tank 2 action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        x = 0
        # left
        if self._keyboard_service.is_key_down('j'):
            tank2 = cast.get_actors("tanks")[1]
            position = tank2.get_position()
            x1 = position.get_x()
            y1 = position.get_y()
            x2 = x1 - constants.CELL_SIZE
            if x2 >= 0:
                terrain = cast.get_first_actor("terrain")
                results = terrain.calculate_new_position(x2)
                y = results["y"]
                rotation = results["rotation"]
                y2 = y - constants.HEIGHT_PLAYER2
                velocity = Point(x2-x1, y2-y1)
                tank2.set_velocity(velocity)
                tank2.set_rotation(rotation)

        # right
        if self._keyboard_service.is_key_down('l'):
            tank2 = cast.get_actors("tanks")[1]
            position = tank2.get_position()
            x1 = position.get_x()
            y1 = position.get_y()
            x2 = x1 + constants.CELL_SIZE
            if (x2 + constants.WIDTH_PLAYER2) <= constants.MAX_X:
                terrain = cast.get_first_actor("terrain")
                results = terrain.calculate_new_position(x2)
                y = results["y"]
                rotation = results["rotation"]
                y2 = y - constants.HEIGHT_PLAYER2
                velocity = Point(x2-x1, y2-y1)
                tank2.set_velocity(velocity)
                tank2.set_rotation(rotation)