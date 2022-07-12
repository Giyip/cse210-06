import pyray
from game.shared.point import Point

class MouseService:
    """Gets the inputs from the mouse. 
    The responsibility of the class is to keep track of the inputs from the mouse.
    """
    def is_mouse_button_left_pressed(self):
        """Checks if the mouse's left button was pressed
        
        Return:
            boolean: if the mouse's left button was pressed
        """
        return pyray.is_mouse_button_pressed(pyray.MOUSE_BUTTON_LEFT)

    def get_click_position(self):
        """Gets the click's position
        
        Return:
            Point: the click's position
        """
        click_position = pyray.get_mouse_position()
        x = click_position.x
        y = click_position.y
        return Point(int(x), int(y))
