from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Direction(str, Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


OPPOSITE = {
    Direction.UP: Direction.DOWN,
    Direction.DOWN: Direction.UP,
    Direction.LEFT: Direction.RIGHT,
    Direction.RIGHT: Direction.LEFT,
}


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def move_point(point: Point, direction: Direction) -> Point:
    if direction == Direction.UP:
        return Point(point.x, point.y - 1)
    if direction == Direction.DOWN:
        return Point(point.x, point.y + 1)
    if direction == Direction.LEFT:
        return Point(point.x - 1, point.y)
    return Point(point.x + 1, point.y)
