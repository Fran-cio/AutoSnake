from __future__ import annotations

import pygame

from autosnake import config
from autosnake.domain.logic import make_initial_state, set_direction, step
from autosnake.domain.types import Direction, GameStatus


def draw_grid(screen: pygame.Surface) -> None:
    for x in range(0, config.WINDOW_WIDTH, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (x, 0), (x, config.WINDOW_HEIGHT), 1)
    for y in range(0, config.WINDOW_HEIGHT, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOR, (0, y), (config.WINDOW_WIDTH, y), 1)


def draw_state(screen: pygame.Surface, font: pygame.font.Font, state) -> None:
    screen.fill(config.BG_COLOR)
    draw_grid(screen)

    food_rect = pygame.Rect(state.food.x * config.CELL_SIZE, state.food.y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
    pygame.draw.rect(screen, config.FOOD_COLOR, food_rect)

    for i, segment in enumerate(state.snake):
        color = config.SNAKE_HEAD_COLOR if i == 0 else config.SNAKE_BODY_COLOR
        rect = pygame.Rect(segment.x * config.CELL_SIZE, segment.y * config.CELL_SIZE, config.CELL_SIZE, config.CELL_SIZE)
        pygame.draw.rect(screen, color, rect)

    score = font.render(f"Score: {state.score}", True, config.TEXT_COLOR)
    screen.blit(score, (12, 8))

    if state.status is GameStatus.GAME_OVER:
        over = font.render("Game Over - Press R to restart", True, config.GAME_OVER_COLOR)
        screen.blit(over, (12, 36))


def run() -> int:
    pygame.init()
    pygame.display.set_caption(config.WINDOW_TITLE)
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 22)

    fixed_dt = 1.0 / config.MOVE_TICKS_PER_SEC
    accumulator = 0.0
    state = make_initial_state(config.GRID_WIDTH, config.GRID_HEIGHT)

    running = True
    while running:
        frame_time = clock.tick(config.FPS) / 1000.0
        accumulator += frame_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key in (pygame.K_w, pygame.K_UP):
                    set_direction(state, Direction.UP)
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    set_direction(state, Direction.DOWN)
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    set_direction(state, Direction.LEFT)
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    set_direction(state, Direction.RIGHT)
                elif event.key == pygame.K_r and state.status is GameStatus.GAME_OVER:
                    state = make_initial_state(config.GRID_WIDTH, config.GRID_HEIGHT)

        while accumulator >= fixed_dt:
            step(state, config.GRID_WIDTH, config.GRID_HEIGHT)
            accumulator -= fixed_dt

        draw_state(screen, font, state)
        pygame.display.flip()

    pygame.quit()
    return 0
