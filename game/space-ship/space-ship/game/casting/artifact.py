import random

from game.casting.actor import Actor
from game.shared.point import Point

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._life = 0
    
    def falling(self):
        """Gets the selected direction based on the currently pressed keys.
         Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0
        
        
        dy += 1

        direction = Point(dx, dy)
        direction = direction.scale(5)
        
        return direction
    
    def move_down(self,max_x, list): 
        for artifact in list:
            artifact.move_next(max_x)
    
    def move_up(self,max_x, list): 
        for artifact in list:
            artifact.move_prev(max_x)