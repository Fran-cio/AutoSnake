# AutoSnake — Plan de Implementación (MVP)

## Objetivo
Desarrollar Snake 2D en Python/pygame para PC.

## Arquitectura
- `main.py`: loop principal
- `game/game.py`: estado y reglas
- `game/snake.py`: movimiento y anti-reversa
- `game/food.py`: spawn seguro
- `game/renderer.py`: render + HUD
- `tests/test_logic.py`: reglas críticas

## Criterios de aceptación
1. Render estable.
2. WASD funciona y no permite reversa inmediata.
3. Comer comida aumenta score y longitud.
4. Colisión con pared/cuerpo produce game over.
5. `R` reinicia partida.
6. `ESC`/cerrar ventana termina limpio.
