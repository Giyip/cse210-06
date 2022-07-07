

class Line:
    """A line entity representing a piece of the terrain

    The responsibility of Line is to save a representation of a line.

    Attributes:
        _position1 (Point): the position where the line starts
        _position2 (Point): the position where the line ends
    """

    def __init__(self, position1, position2):
        """Constructs a new line object"""
        self._position1 = position1
        self._position2 = position2

    def get_position1(self):
        """Gets the position the line starts.

        Returns:
            Point: the position the line starts
        """
        return self._position1

    def get_position2(self):
        """Gets the position the line ends.

        Returns:
            Point: the position the line ends
        """
        return self._position2

    def calculate_y(self, x):
        """Calculates y according to the given x.

        Returns:
            integer: the y value according the given x 
        """
        x1 = self._position1.get_x()
        y1 = self._position1.get_y()
        x2 = self._position2.get_x()
        y2 = self._position2.get_y()
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        y = int(m*x + b)
        return y