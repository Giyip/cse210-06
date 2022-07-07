from game.casting.actor import Actor

class Projectile(Actor):
    """A circular projectile.
    
    The responsibility of Projectile if to move itself.
    
    Attributes:
        _radius (integer): the circle's radius, which represents the projectile 
    """
    
    def __init__(self):
        """Constructs an instance of projectile
        """
        super().__init__()
        self._radius = 0

    def get_radius(self):
        pass

    def move_next(self):
        pass

    def get_rectangle(self):
        pass
