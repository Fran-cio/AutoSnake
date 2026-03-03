from __future__ import annotations

import pygame

from . import config
from .game import Game
from .state import GameState


def draw_grid(screen: pygame.Surface) -> None:
    for x in range(0, config.WINDOW_WIDTH, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (x, 0), (x, config.WINDOW_HEIGHT), 1)
    for y in range(0, config.WINDOW_HEIGHT, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (0, y), (config.WINDOW_WIDTH, y), 1)


def draw_game(screen: pygame.Surface, game: Game, font: pygame.font.Font) -> None:
    screen.fill(config.BG_COLOR)
    draw_grid(screen)

    for index, segment in enumerate(game.snake.segments):
        color = config.SNAKE_HEAD_COLOR if index == 0 else config.SNAKE_BODY_COLOR
        pygame.draw.rect(
            screen,
            color,
            pygame.Rect(
                segment.x * config.CELL_SIZE,
                segment.y * config.CELL_SIZE,
                config.CELL_SIZE,
                config.CELL_SIZE,
            ),
        )

    pygame.draw.rect(
        screen,
        config.FOOD_COLOR,
        pygame.Rect(
            game.food.x * config.CELL_SIZE,
            game.food.y * config.CELL_SIZE,
            config.CELL_SIZE,
            config.CELL_SIZE,
        ),
    )

    score_text = font.render(f"Score: {game.score}", True, config.TEXT_COLOR)
    screen.blit(score_text, (10, 10))

    if game.state == GameState.GAME_OVER:
        overlay = pygame.Surface((config.WINDOW_WIDTH, config.WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill(config.OVERLAY_COLOR)
        screen.blit(overlay, (0, 0))

        lines = [
            "GAME OVER",
            f"Score: {game.score}",
            "Press R to restart",
            "ESC to quit",
        ]
        for idx, line in enumerate(lines):
            rendered = font.render(line, True, config.TEXT_COLOR)
            x = (config.WINDOW_WIDTH - rendered.get_width()) // 2
            y = (config.WINDOW_HEIGHT - rendered.get_height()) // 2 + idx * 30
            screen.blit(rendered, (x, y))
