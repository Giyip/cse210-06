#import imp
from game.casting.actor import Actor
from game.shared.point import Point

class Tank(Actor):
    """A tank entity represeting the player.

    The responsibility of Tank is to move itself.

    Attributes:
        _size (Point): the tank's size 
        _rotation (float): the tank's rotation
    """
    
    def __init__(self, size):
        """Constructs an instance of tank
        """
        super().__init__()
        self._size = size
        self._rotation = 0

    def get_size(self):
        """Gets the tank's size.

        Returns:
            Point: The tank's size.
        """
        return self._size

    def get_rotation(self):
        """Gets the tank's rotation.

        Returns:
            float: The tank's rotation.
        """
        return self._rotation

    def move_next(self):
        """Moves the tank to its next position."""
        super().move_next()
        #print(f"pos: {self.get_position().get_x(), self.get_position().get_y()}")
        self.set_velocity(Point(0,0))

    def get_rectangle(self):
        pass

    def set_rotation(self, rotation):
        """sets the  to the given x.

        Returns:
            integer: the y value according the given x 
        """
        self._rotation = rotation