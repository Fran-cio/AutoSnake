"""AutoSnake entrypoint.

PR scope: pygame bootstrap with fixed logic timestep + decoupled render loop.
"""

from __future__ import annotations

import sys
import pygame

from autosnake.game import config
from autosnake.game import renderer


def run() -> int:
    pygame.init()
    pygame.display.set_caption(config.WINDOW_TITLE)

    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 20)

    fixed_dt = 1.0 / config.MOVE_TICKS_PER_SEC
    accumulator = 0.0
    running = True

    while running:
        frame_time = clock.tick(config.FPS) / 1000.0
        accumulator += frame_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        while accumulator >= fixed_dt:
            # Reserved for logic updates in next PRs.
            accumulator -= fixed_dt

        screen.fill(config.BG_COLOR)
        renderer.draw_grid(screen)
        renderer.draw_bootstrap_marker(screen)
        renderer.draw_hud(screen, font)
        pygame.display.flip()

    pygame.quit()
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
