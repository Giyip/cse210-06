import pyray
import constants


class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug=False):
        """Constructs a new VideoService using the specified debug mode.

        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    def draw_tanks(self, tanks):
        """Draws the given tanks

        Args:
            tanks (list<Tank>): the tanks to draw.
        """
        for tank in tanks:
            self._draw_tank(tank)

    def _draw_tank(self, tank):
        """Draws the given tank

        Args:
            tank (Tank): the tank to draw.
        """
        position = tank.get_position()
        size = tank.get_size()
        color = tank.get_color()
        rotation = tank.get_rotation()
        self._draw_rectangle(position, size, rotation, color)

    def draw_healths(self, healths):
        """Draws the given healths

        Args:
            healths (list<Health>): the healths to draw.
        """
        for health in healths:
            self._draw_health(health)

    def _draw_health(self, health):
        """Draws the given player's health

        Args:
            health (Health): the health to draw.
        """
        pass

    def _draw_rectangle(self, position, size, rotation, color):
        """Draws a rectangle according to the given values
        Args:
            position (Point): The position of the rectangle.
            size (Point): The size of the rectangle.
            color (Color): The color for the line.
        """
        x = position.get_x()
        y = position.get_y()
        width = size.get_x()
        height = size.get_y()
        r, g, b, a = color.to_tuple()
        rect = pyray.Rectangle(x, y, width, height)
        new_position = pyray.Vector2(0, 0)
        pyray.draw_rectangle_pro(rect, new_position, int(rotation), pyray.Color(r, g, b, a))
        
    def draw_projectiles(self, projectiles):
        """Draws the given projectiles

        Args:
            projectiles (list<Projectiles>): the projectiles to draw.
        """
        for projectile in projectiles:
            self._draw_projectile(projectile)

    def _draw_projectile(self, projectile):
        """Draws the given projectile

        Args:
            projectile (Projectile): the projectile to draw.
        """
        radius = projectile.get_radius()
        position = projectile.get_position()
        color = projectile.get_color()
        self._draw_circle(position, radius, color)

    def _draw_circle(self, position, radius, color):
        """Draws a cicle according the given values

        Args:
            position (Point): the circle's position
            radius: the circle's radius
            color: the circle's color
        """
        x = position.get_x() # center of the circle
        y = position.get_y() # center of the circle
        r, g, b, a = color.to_tuple()
        pyray.draw_circle(x, y, radius, pyray.Color(r,g,b,a))
    
    def draw_terrain(self, terrain):
        """Draws the terrain for the game

        Args:
            terrain (Terrain): the terrain to draw.
        """
        for line in terrain.get_surface():
            color = terrain.get_color()
            self._draw_line(line, color)

    def _draw_line(self, line, color):
        """Draws the given line on the screen.

        Args:
            line (Line): The line to draw.
            color (Color): The color for the line.
        """
        position1 = line.get_position1()
        position2 = line.get_position2()
        x1 = position1.get_x()
        y1 = position1.get_y()
        x2 = position2.get_x()
        y2 = position2.get_y()
        #extracted_color = color.to_tuple()
        r, g, b, a = color.to_tuple()
        pyray.draw_line(x1, y1, x2, y2, pyray.Color(r, g, b, a))
        #pyray.draw_line(x1, y1, x2, y2, pyray.Color(extracted_color[0], extracted_color[1], extracted_color[2], extracted_color[3]))

    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()

        if centered:
            width = pyray.measure_text(text, font_size)
            offset = int(width / 2)
            x -= offset

        pyray.draw_text(text, x, y, font_size, color)

    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """
        for actor in actors:
            self.draw_actor(actor, centered)

    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(constants.MAX_X, constants.MAX_Y, constants.CAPTION)
        pyray.set_target_fps(constants.FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, constants.MAX_Y, constants.CELL_SIZE):
            pyray.draw_line(0, y, constants.MAX_X, y, pyray.GRAY)

        for x in range(0, constants.MAX_X, constants.CELL_SIZE):
            pyray.draw_line(x, 0, x, constants.MAX_Y, pyray.GRAY)

    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)