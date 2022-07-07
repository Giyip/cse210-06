import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlTank1Action(Action):
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

    def execute(self, cast, script):
        """Executes the control tank 1 action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        x = 0
        # left
        if self._keyboard_service.is_key_down('a'):
            #x = -constants.CELL_SIZE
            tank1 = cast.get_actors("tanks")[0]
            position = tank1.get_position()
            x1 = position.get_x()
            y1 = position.get_y()
            terrain = cast.get_first_actor("terrain")
            x2 = x1 - constants.CELL_SIZE
            new_position = terrain.calculate_new_position(x2)
            y2 = new_position.get_y() - constants.HEIGHT_PLAYER1
            velocity = Point(x2-x1, y2-y1)
            tank1.set_velocity(velocity)

        # right
        if self._keyboard_service.is_key_down('d'):
            #x = constants.CELL_SIZE
            tank1 = cast.get_actors("tanks")[0]
            position = tank1.get_position()
            x1 = position.get_x()
            y1 = position.get_y()
            terrain = cast.get_first_actor("terrain")
            x2 = x1 + constants.CELL_SIZE
            new_position = terrain.calculate_new_position(x2)
            y2 = new_position.get_y() - constants.HEIGHT_PLAYER1
            velocity = Point(x2-x1, y2-y1)
            tank1.set_velocity(velocity)

        # up
        #if self._keyboard_service.is_key_down('w'):
        #    self._direction = Point(0, -constants.CELL_SIZE)

        # down
        #if self._keyboard_service.is_key_down('s'):
        #    self._direction = Point(0, constants.CELL_SIZE)

        #if x != 0:
        #    tank1 = cast.get_actors("tanks")[0]
        #    position = tank1.get_position()
        #    terrain = cast.get_first_actor("terrain")
        #    velocity = terrain.calculate_new_position(position.get_x() + x)
        #    tank1.set_velocity(velocity)