# AutoSnake — Execution Plan (MVP)

This repository will implement a 2D Snake game in Python using pygame.

## MVP Scope
- Grid-based movement
- WASD controls (arrows optional)
- Fixed logic tick + decoupled render FPS
- Food spawn and snake growth
- Score HUD
- Game Over on wall/self collision
- Restart with `R`
- Exit with `ESC` / window close

## Delivery flow (incremental PRs)
1. Bootstrap project structure + pygame entrypoint
2. Core snake movement + anti-reverse rule
3. Food, score, collisions, game over, restart
4. Tests + docs hardening

## Commit attribution convention
Every commit should include agent attribution, e.g.:
`feat(game): add fixed tick loop [by: frontend-dev-sr2]`
