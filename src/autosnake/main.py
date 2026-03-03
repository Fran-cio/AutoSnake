from __future__ import annotations

import pygame

from autosnake.game import config
from autosnake.game.game import Game
from autosnake.game.input import KEY_TO_DIRECTION
from autosnake.game.renderer import draw_game
from autosnake.game.state import GameState


def run() -> int:
    pygame.init()
    pygame.display.set_caption(config.WINDOW_TITLE)

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 28)

    game = Game.create()

    fixed_dt = 1.0 / config.MOVE_TICKS_PER_SEC
    accumulator = 0.0
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
                elif event.key == pygame.K_r and game.state == GameState.GAME_OVER:
                    game.reset()
                elif event.key in KEY_TO_DIRECTION and game.state == GameState.RUNNING:
                    game.snake.set_direction(KEY_TO_DIRECTION[event.key])

        while accumulator >= fixed_dt:
            game.tick()
            accumulator -= fixed_dt

        draw_game(screen, game, font)
        pygame.display.flip()

    pygame.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
