from __future__ import annotations

import random
from typing import Iterable

from autosnake.domain.types import Direction, GameState, GameStatus, Point


def is_opposite(current: Direction, new: Direction) -> bool:
    cx, cy = current.value
    nx, ny = new.value
    return cx == -nx and cy == -ny


def next_head(head: Point, direction: Direction) -> Point:
    dx, dy = direction.value
    return Point(head.x + dx, head.y + dy)


def random_food(width: int, height: int, occupied: Iterable[Point]) -> Point:
    occ = set(occupied)
    free = [Point(x, y) for x in range(width) for y in range(height) if Point(x, y) not in occ]
    if not free:
        return Point(-1, -1)
    return random.choice(free)


def make_initial_state(width: int, height: int, start_len: int = 3) -> GameState:
    center = Point(width // 2, height // 2)
    snake = [Point(center.x - i, center.y) for i in range(start_len)]
    food = random_food(width, height, snake)
    return GameState(snake=snake, direction=Direction.RIGHT, food=food)


def set_direction(state: GameState, new_direction: Direction) -> None:
    if state.status is GameStatus.GAME_OVER:
        return
    if is_opposite(state.direction, new_direction):
        return
    state.direction = new_direction


def step(state: GameState, width: int, height: int) -> None:
    if state.status is GameStatus.GAME_OVER:
        return

    head = state.snake[0]
    new_head = next_head(head, state.direction)

    if new_head.x < 0 or new_head.x >= width or new_head.y < 0 or new_head.y >= height:
        state.status = GameStatus.GAME_OVER
        return

    grow = new_head == state.food

    future_body = [new_head, *state.snake]
    if not grow:
        future_body = future_body[:-1]

    if new_head in future_body[1:]:
        state.status = GameStatus.GAME_OVER
        return

    state.snake = future_body

    if grow:
        state.score += 1
        state.food = random_food(width, height, state.snake)
