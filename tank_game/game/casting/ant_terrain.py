import math

from game.casting.actor import Actor
from game.shared.point import Point

class AntTerrain(Actor):
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
            Dict(string, float): the calculated position and the rotation
        """
        y = 0
        rotation = 0
        for line in self._surface:
            position1 = line.get_position1()
            x1 = position1.get_x()
            y1 = position1.get_y()
            position2 = line.get_position2()
            x2 = position2.get_x()
            y2 = position2.get_y()
            
            if x >= x1 and x <= x2:
                y = line.calculate_y(x)
                rotation = self._calculate_angle(line)
                break
        return {"y": y, "rotation": rotation}

    def _calculate_angle(self, line):
        """Calculate the line's angle.

        Args:
            line (Line): The given line.
        Returns:
            float: the calculated angle
        """
        position1 = line.get_position1()
        position2 = line.get_position2()
        m = line.get_m()
        x1 = position1.get_x()
        y1 = position1.get_y()
        x2 = position2.get_x()
        y2 = position2.get_y()
        h = math.sqrt(math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2))
        aux_angle = math.asin((y2 - y1) / h)
        return aux_angle * 180 / math.pi
        #if m >= 0:
        #    return aux_angle * 180 / math.pi
        #else:
        #    return - aux_angle * 180 / math.pi