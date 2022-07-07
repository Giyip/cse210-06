from game.casting.actor import Actor
from game.shared.point import Point

class Terrain(Actor):
    """The playing area the tanks will have available to play against each other.
    
    The responsibility of Terrain is to place the Tanks correctly and show the play field.
    
    Attributes:
        _surface (list<Line>): the list of lines which conforms the terrain
    """

    def __init__(self, surface):
        """Constructs a new instance of Terrain"""
        super().__init__()
        self._surface = surface

    def get_surface(self):
        """Gets the list of lines

        Returns:
            list<Line>: the list of lines
        """
        return self._surface
    
    def set_surface(self, surface):
        """Updates the surface to the given one.

        Args:
            surface (list<Line>): The given surface.
        """
        self._surface = surface

    def calculate_new_position(self, x):
        """Calculate a position according to the given x

        Args:
            x (integer): The given x.
        Returns:
            Point: the calculated position
        """
        y = 0
        for line in self._surface:
            position1 = line.get_position1()
            x1 = position1.get_x()
            y1 = position1.get_y()
            position2 = line.get_position2()
            x2 = position2.get_x()
            y2 = position2.get_y()
            
            if x >= x1 and x <= x2:
                y = line.calculate_y(x)
                break
        return Point(x, y)