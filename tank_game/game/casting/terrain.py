from turtle import position
import constants
from game.casting.actor import Actor
from game.casting.rectangle import Rectangle
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
        self._surface = []
        self._position_tank1 = Point(0, 0)
        self._position_tank2 = Point(0, 0)
        self._initialize_surface(surface)

    def _initialize_surface(self, surface):
        rows = len(surface)
        cols = len(surface[0])
        row_size = int(constants.MAX_Y / rows)
        col_size = int(constants.MAX_X / cols)
        for i in range(rows):
            self._surface.append([])
            for j in range(cols):
                position = Point(0, 0)
                size = Point(0, 0)
                self._surface[i].append(Rectangle(position, size))
        x = 0
        for i in range(rows):
            y = 0
            for j in range(cols):
                if surface[i][j] == 1:
                    position = Point(y, x)
                    size = Point(col_size, row_size)
                    self._surface[i][j] = Rectangle(position, size)
                elif surface[i][j] == 2:
                    self._position_tank1 = Point(y, x)
                elif surface[i][j] == 3:
                    self._position_tank2 = Point(y, x)
                y += row_size
            x += col_size

    def get_surface(self):
        """Gets the list of rectangles

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

    def get_tank_position(self, tank):
        """Calculate a position according to the given x

        Args:
            x (integer): The given x.
        Returns:
            Dict(string, float): the calculated position and the rotation
        """
        if tank == constants.ID_PLAYER1:
            return self._position_tank1
        else:
            return self._position_tank2

    def calculate_tank_position(self, tank):
        """Calculate a position according to the given x

        Args:
            x (integer): The given x.
        Returns:
            Dict(string, float): the calculated position and the rotation
        """
        pass