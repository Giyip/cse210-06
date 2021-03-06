import constants
import math
from game.casting.actor import Actor
from game.shared.point import Point

class Projectile(Actor):
    """A circular projectile.
    
    The responsibility of Projectile if to move itself.
    
    Attributes:
        _radius (integer): the circle's radius, which represents the projectile 
    """
    
    def __init__(self, position, radius, v0, angle0):
        """Constructs an instance of projectile
        """
        super().__init__()
        self._radius = radius
        self._initial_position = position
        self.set_position(position)
        self._v0 = v0
        angle0_rad = math.radians(angle0)
        self._v0x = v0 * math.cos(angle0_rad)
        self._v0y = v0 * math.sin(angle0_rad)
        self._t = 0

    def get_radius(self):
        """Get the value of the radius of the projectile
        Returns:
            radius (float): the radius of the projectile
        """
        return self._radius

    def move_next(self):
        """Moves the projectile to its new position
        """
        self._t += constants.TIME_RATE
        x = self._calculate_x()
        y = - self._calculate_y()
        velocity = Point(int(x), int(y))
        self.set_velocity(velocity)
        x = (self._initial_position.get_x() + self._velocity.get_x())
        y = (self._initial_position.get_y() + self._velocity.get_y()) 
        self.set_position(Point(x, y))

    def calculate_projection_position(self, t):
        """Calculates a position for a projection
        Returns: 
            Point: calculated position for a projection
        """
        x = self._v0x * t
        y = - (self._v0y * t - (constants.GRAVITY * math.pow(t, 2) / 2))
        x = (self._initial_position.get_x() + int(x))
        y = (self._initial_position.get_y() + int(y)) 
        return Point(x, y)


    def _calculate_x(self):
        """Calculate the movement in the x axis
        Return:
            x (float): the movement in the x axis
        """
        return self._v0x * self._t

    def _calculate_y(self):
        """Calculate the movement in the y axis
        Return:
            y (float): the movement in the y axis
        """
        y = 0
        y = self._v0y * self._t - (constants.GRAVITY * math.pow(self._t, 2) / 2)
        return y