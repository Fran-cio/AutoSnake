"""Rendering helpers."""

from __future__ import annotations

import pygame

from . import config


def draw_grid(screen: pygame.Surface) -> None:
    for x in range(0, config.WINDOW_WIDTH, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (x, 0), (x, config.WINDOW_HEIGHT), 1)
    for y in range(0, config.WINDOW_HEIGHT, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (0, y), (config.WINDOW_WIDTH, y), 1)


def draw_bootstrap_marker(screen: pygame.Surface) -> None:
    rect = pygame.Rect(
        (config.GRID_WIDTH // 2) * config.CELL_SIZE,
        (config.GRID_HEIGHT // 2) * config.CELL_SIZE,
        config.CELL_SIZE,
        config.CELL_SIZE,
    )
    pygame.draw.rect(screen, config.SNAKE_HEAD_COLOR, rect)


def draw_hud(screen: pygame.Surface, font: pygame.font.Font) -> None:
    hud = font.render(
        f"Bootstrap ready | FPS: {config.FPS} | Ticks: {config.MOVE_TICKS_PER_SEC}",
        True,
        config.TEXT_COLOR,
    )
    screen.blit(hud, (12, 10))
