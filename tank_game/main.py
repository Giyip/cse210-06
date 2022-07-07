import constants

from game.shared.point import Point
from game.casting.line import Line
from game.casting.terrain import Terrain
from game.casting.cast import Cast
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.scripting.script import Script
from game.scripting.draw_actors_action import DrawActorsAction
from game.director.director import Director
from game.casting.tank import Tank
from game.scripting.control_tank1_action import ControlTank1Action
from game.scripting.move_actors_action import MoveActorsAction

def main():
    # create positions for the terrain
    position1 = Point(0, 300)
    position2 = Point(300, 300)
    position3 = Point(600, 500)
    position4 = Point(900, 500)
    line1 = Line(position1, position2)
    line2 = Line(position2, position3)
    line3 = Line(position3, position4)
    surface = [line1, line2, line3]
    terrain = Terrain(surface)
    terrain.set_text("terrain")

    # create position for the player1
    position_t1 = terrain.calculate_new_position(constants.X_POSITION_PLAYER1)
    x1 = position_t1.get_x()
    y1 = position_t1.get_y() - constants.HEIGHT_PLAYER1
    size1 = Point(constants.WIDTH_PLAYER1, constants.HEIGHT_PLAYER1)
    tank1 = Tank(size1)
    tank1.set_position(Point(x1, y1))
    tank1.set_text("tank1")

    # create position for the player2
    x2 = constants.X_POSITION_PLAYER2
    y2 = terrain.calculate_new_position(x2)
    size2 = Point(constants.WIDTH_PLAYER2, constants.HEIGHT_PLAYER2)
    tank2 = Tank(size2)
    tank2.set_position(Point(x2, y2))

    # create the cast
    cast = Cast()
    cast.add_actor("terrain", terrain)
    cast.add_actor("tanks", tank1)
    #cast.add_actor("tanks", tank2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlTank1Action(keyboard_service))
    #script.add_action("input", ControlCycle2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    #script.add_action("update", HandleCollisionsAction(video_service))
    #script.add_action("update", TrailGrowthAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()