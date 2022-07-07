from game.shared.point import Point
from game.casting.actor import Actor

class Health(Actor):
    """A record of Tank health.
    
    The responsibility of Health is to keep track of the health the player has remaining from
    succesful opponent hits. It contains methods for removing health. Client should use
    get_text() to get a string representation of the health remaining.

    Attributes:
        _value (integer): the health's value
        _size (Point): the rectangle's size, the visible representation of the health's value
    """

    def __init__(self):
        """
            Constructor for a Health instance
        """
        super().__init__()
        self._value = 100
        self._size = Point(0, 0)

    def get_value(self):
        """It returns the health's value
        Returns:
            integer: the health's value
        """
        return self._value

    def get_size(self):
        """It returns the rectangle's size, the visible representation of the health's value
        Returns:
            Point: the rectangle's size
        """
        return self._size
    
    def update_value(self, value):
        """Updates the health's value

        Args:
            value (integer): The given value.
        """
        self._value = value