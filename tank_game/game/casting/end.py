from game.casting.actor import Actor


class End(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by succesfully
    hitting the opponent. It contains methods for adding and getting points. Client should use
    get_text() to get a string representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """

    def __init__(self, player):
        super().__init__()
        self._player = player

    def get_text(self):
        return f"{self._player} is the winner!!!"