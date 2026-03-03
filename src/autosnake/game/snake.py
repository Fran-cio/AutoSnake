from __future__ import annotations

from collections import deque
from typing import Iterable

from .types import Direction, OPPOSITE, Point, move_point


class Snake:
    def __init__(self, start_segments: Iterable[Point], start_direction: Direction) -> None:
        self.segments = deque(start_segments)
        self.direction = start_direction
        self.pending_direction = start_direction

    @property
    def head(self) -> Point:
        return self.segments[0]

    def set_direction(self, new_direction: Direction) -> None:
        if new_direction == OPPOSITE[self.direction]:
            return
        self.pending_direction = new_direction

    def next_head(self) -> Point:
        return move_point(self.head, self.pending_direction)

    def step(self, grow: bool) -> None:
        self.direction = self.pending_direction
        new_head = move_point(self.head, self.direction)
        self.segments.appendleft(new_head)
        if not grow:
            self.segments.pop()

    def occupies(self, point: Point) -> bool:
        return point in self.segments

    def collides_with_self(self) -> bool:
        return self.head in list(self.segments)[1:]
