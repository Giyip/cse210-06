from game.shared.point import Point
from game.casting.actor import Actor

class Health(Actor):
    """A record of Tank health.
    
    The responsibility of Health is to keep track of the health the player has remaining from
    succesful opponent hits. It contains methods for removing health. Client should use
    get_text() to get a string representation of the health remaining.

    Attributes:
        _value (integer): the health's value
    """

    def __init__(self, health):
        """
            Constructor for a Health instance
        """
        super().__init__()
        self._value = health
        self.update_value(0)

    def get_value(self):
        """It returns the health's value
        Returns:
            integer: the health's value
        """
        return f"{self._value}%"
    
    def update_value(self, value):
        """Updates the health's value

        Args:
            value (integer): The given value.
        """
        self._value -= value
        self.set_text(f"{self._value}%")
