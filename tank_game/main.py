import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.health import Health
from game.casting.tank import Tank
from game.scripting.script import Script
from game.scripting.control_tank1_action import ControlTank1Action
from game.scripting.control_tank2_action import ControlTank2Action
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.projectile_collide_terrain_action import ProjectileCollideTerrainAction
from game.scripting.projectile_collide_tank_action import ProjectileCollideTankAction
from game.scripting.handle_mouse_button_pressed import HandleMouseButtonPressed
from game.director.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.mouse_service import MouseService
from game.shared.point import Point
from game.casting.line import Line
from game.casting.terrain import Terrain
from game.casting.projectile import Projectile

def main():
    # create positions for the terrain
    position1 = Point(0, 550)
    position2 = Point(300, 550)
    position3 = Point(600, 450)
    position4 = Point(900, 450)
    line1 = Line(position1, position2)
    line2 = Line(position2, position3)
    line3 = Line(position3, position4)
    surface = [line1, line2, line3]
    terrain = Terrain(surface)
    terrain.set_text("terrain")

    # create position for the player1
    x1 = constants.X_POSITION_PLAYER1
    results1 = terrain.calculate_new_position(x1)
    y1 = results1["y"] - constants.HEIGHT_PLAYER1
    size1 = Point(constants.WIDTH_PLAYER1, constants.HEIGHT_PLAYER1)
    tank1 = Tank(size1)
    tank1.set_position(Point(x1, y1))
    tank1.set_text(constants.ID_PLAYER1)
    tank1.set_color(constants.YELLOW)

    # create position for the player2
    x2 = constants.X_POSITION_PLAYER2 - constants.WIDTH_PLAYER2
    results2 = terrain.calculate_new_position(x2)
    y2 = results2["y"] - constants.HEIGHT_PLAYER2
    size2 = Point(constants.WIDTH_PLAYER2, constants.HEIGHT_PLAYER2)
    tank2 = Tank(size2)
    tank2.set_position(Point(x2, y2))
    tank2.set_text(constants.ID_PLAYER2)
    tank2.set_color(constants.GREEN)

    # create testing projectile
    #xp = int(x1 + constants.WIDTH_PLAYER1 / 2)
    #yp = int(y1 - constants.HEIGHT_PLAYER1 / 2)
    #position_p = Point(xp, yp)
    #projectile = Projectile(position_p, constants.PROJECTILE_RADIUS, constants.PROJECTILE_EXAMPLE_V0, constants.PROJECTILE_EXAMPLE_ANGLE)
    #projectile.set_position()

    # create the scores
    score1 = Score("Player 1")
    score2 = Score("Player 2")
    score2.set_position(Point(constants.MAX_X-7*constants.CELL_SIZE, 0))

    # create the healths
    health1 = Health(constants.PLAYERS_HEALTH)
    health2 = Health(constants.PLAYERS_HEALTH)
    health1.set_position(Point(2, 20))
    health2.set_position(Point(constants.MAX_X-7*constants.CELL_SIZE, 20))

    # create the cast
    cast = Cast()
    cast.add_actor("terrain", terrain)
    cast.add_actor("tanks", tank1)
    cast.add_actor("tanks", tank2)
    #cast.add_actor("projectiles", projectile)
    cast.add_actor("scores", score1)
    cast.add_actor("scores", score2)
    cast.add_actor("healths", health1)
    cast.add_actor("healths", health2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    mouse_service = MouseService()

    script = Script()
    #script.add_action("input", ControlTank1Action(keyboard_service))
    #script.add_action("input", ControlTank2Action(keyboard_service))
    script.add_action("input", HandleMouseButtonPressed(mouse_service, constants.ID_PLAYER1))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", ProjectileCollideTerrainAction())
    script.add_action("update", ProjectileCollideTankAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()