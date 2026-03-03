from enum import Enum


class GameState(str, Enum):
    RUNNING = "RUNNING"
    GAME_OVER = "GAME_OVER"
