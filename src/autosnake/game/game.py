from __future__ import annotations

from dataclasses import dataclass

from . import config
from .food import respawn_food
from .snake import Snake
from .state import GameState
from .types import Direction, Point


@dataclass
class Game:
    snake: Snake
    food: Point
    score: int
    state: GameState

    @classmethod
    def create(cls) -> "Game":
        mid_x = config.GRID_WIDTH // 2
        mid_y = config.GRID_HEIGHT // 2
        start_segments = [
            Point(mid_x - i, mid_y) for i in range(config.START_LENGTH)
        ]
        snake = Snake(start_segments, Direction[config.START_DIRECTION])
        food = respawn_food(config.GRID_WIDTH, config.GRID_HEIGHT, snake.segments)
        return cls(snake=snake, food=food, score=0, state=GameState.RUNNING)

    def reset(self) -> None:
        fresh = self.create()
        self.snake = fresh.snake
        self.food = fresh.food
        self.score = fresh.score
        self.state = fresh.state

    def is_outside(self, point: Point) -> bool:
        return (
            point.x < 0
            or point.x >= config.GRID_WIDTH
            or point.y < 0
            or point.y >= config.GRID_HEIGHT
        )

    def tick(self) -> None:
        if self.state != GameState.RUNNING:
            return

        predicted_head = self.snake.next_head()
        grow = predicted_head == self.food

        # Simulate next segments for robust self-collision check.
        segments = list(self.snake.segments)
        simulated = [predicted_head] + segments[:-1]
        if grow:
            simulated = [predicted_head] + segments

        if self.is_outside(predicted_head) or predicted_head in simulated[1:]:
            self.state = GameState.GAME_OVER
            return

        self.snake.step(grow=grow)

        if grow:
            self.score += 1
            self.food = respawn_food(config.GRID_WIDTH, config.GRID_HEIGHT, self.snake.segments)
