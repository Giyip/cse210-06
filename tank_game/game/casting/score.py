from game.casting.actor import Actor

class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by succesfully
    hitting the opponent. It contains methods for adding and getting points. Client should use
    get_text() to get a string representation of the points earned.

    Attributes:
    """