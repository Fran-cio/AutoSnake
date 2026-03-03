from __future__ import annotations

import pygame

from .types import Direction

KEY_TO_DIRECTION = {
    pygame.K_w: Direction.UP,
    pygame.K_UP: Direction.UP,
    pygame.K_s: Direction.DOWN,
    pygame.K_DOWN: Direction.DOWN,
    pygame.K_a: Direction.LEFT,
    pygame.K_LEFT: Direction.LEFT,
    pygame.K_d: Direction.RIGHT,
    pygame.K_RIGHT: Direction.RIGHT,
}
