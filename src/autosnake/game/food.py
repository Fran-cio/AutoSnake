from __future__ import annotations

import random
from typing import Iterable

from .types import Point


def respawn_food(grid_width: int, grid_height: int, occupied: Iterable[Point]) -> Point:
    occupied_set = set(occupied)
    cells = [
        Point(x, y)
        for x in range(grid_width)
        for y in range(grid_height)
        if Point(x, y) not in occupied_set
    ]
    if not cells:
        raise RuntimeError("No free cells to spawn food")
    return random.choice(cells)
