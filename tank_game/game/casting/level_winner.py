from game.casting.actor import Actor


class LevelWinner(Actor):
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
        self._message = ""
        self._player = player

    def update_winner(self, player):
        self._player = player
        self._message = f"{self._player} wins the level!"

    def get_text(self):
        return self._message

    def remove_message(self):
        self._message = ""