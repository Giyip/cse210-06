from game.casting.line import Line
from game.scripting.action import Action
from game.shared.point import Point


class PlayerTurret(Action):

    def __init__(self, mouse_service, video_service):
        self._mouse_service = mouse_service
        self._video_service = video_service

    def execute(self, cast, script, scene_manager):
        tanks = cast.get_actors("tanks")
        if tanks[0].get_text() == scene_manager.who_plays:
            start = tanks[0].get_position()
            color = tanks[0].get_color()
        else:
            start = tanks[1].get_position()
            color = tanks[1].get_color()
        end = self._mouse_service.get_click_position()
        line = Line(start, end)
        x = 0
        if end.get_x() < 0:
            x = start.get_x() - 50
        elif end.get_x() > 0:
            x = start.get_x() + 50
        y = line.calculate_y(x)
        end = Point(x, y)
        line = Line(start, end)
        # self._video_service.draw_line(line, color)
        script_reset = script.get_actions("output")[0]
        script_reset.draw_line(cast, line, color)