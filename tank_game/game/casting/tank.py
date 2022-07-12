#import imp
from turtle import width
import pyray
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
        self._can_move = False

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
        if self._can_move:
            self.set_velocity(Point(0, 5))
            super().move_next()
        #print(f"pos: {self.get_position().get_x(), self.get_position().get_y()}")
        #self.set_velocity(Point(0,0))

    def set_can_move(self, can_move):
        self._can_move = can_move

    def get_rectangle(self):
        """Gets the rectangle that will represent the tank, at checking collisions with other actors.

        Returns:
            pyray.Rectangle: the rectangle that will represent the tank
        """
        x1 = self._position.get_x()
        y1 = self._position.get_y()
        width = self._size.get_x()
        height = self._size.get_y()
        return pyray.Rectangle(x1, y1, width, height)

    def set_rotation(self, rotation):
        """sets the  to the given x.

        Returns:
            integer: the y value according the given x 
        """
        self._rotation = rotation