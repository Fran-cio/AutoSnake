from autosnake.game.food import respawn_food
from autosnake.game.game import Game
from autosnake.game.state import GameState
from autosnake.game.types import Direction, Point


def test_reverse_direction_is_ignored() -> None:
    game = Game.create()
    game.snake.set_direction(Direction.LEFT)
    assert game.snake.pending_direction == Direction.RIGHT


def test_snake_grows_and_score_increases_on_food() -> None:
    game = Game.create()
    head = game.snake.head
    game.food = Point(head.x + 1, head.y)
    start_len = len(game.snake.segments)

    game.tick()

    assert len(game.snake.segments) == start_len + 1
    assert game.score == 1


def test_wall_collision_triggers_game_over() -> None:
    game = Game.create()
    game.snake.segments.clear()
    game.snake.segments.appendleft(Point(0, 0))
    game.snake.direction = Direction.LEFT
    game.snake.pending_direction = Direction.LEFT

    game.tick()

    assert game.state == GameState.GAME_OVER


def test_reset_restores_running_state() -> None:
    game = Game.create()
    game.state = GameState.GAME_OVER
    game.score = 99

    game.reset()

    assert game.state == GameState.RUNNING
    assert game.score == 0


def test_food_respawn_avoids_occupied_cells() -> None:
    occupied = {Point(0, 0), Point(0, 1), Point(1, 0)}
    food = respawn_food(3, 3, occupied)
    assert food not in occupied
