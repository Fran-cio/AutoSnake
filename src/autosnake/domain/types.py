from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class GameStatus(Enum):
    RUNNING = "running"
    GAME_OVER = "game_over"


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class GameState:
    snake: list[Point]
    direction: Direction
    food: Point
    score: int = 0
    status: GameStatus = GameStatus.RUNNING
