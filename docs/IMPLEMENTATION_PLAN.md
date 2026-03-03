# Documentación de Implementación — Snake 2D (Python, PC, WASD)

## Objetivo
Desarrollar Snake 2D para escritorio en Python con pygame, incluyendo:
- WASD (flechas opcionales)
- score, game over, restart
- loop con lógica por ticks y render desacoplado

## Alcance MVP
- Movimiento en grilla
- Anti-reversa inmediata
- Comida y crecimiento
- Colisiones (pared/cuerpo)
- Reinicio con `R`
- Salida con `ESC` o cerrar ventana

## Arquitectura propuesta
Estructura modular:
- `src/autosnake/main.py` → bootstrap + loop
- `src/autosnake/game/config.py` → constantes
- `src/autosnake/game/snake.py` → entidad snake
- `src/autosnake/game/food.py` → spawn comida
- `src/autosnake/game/game.py` → orquestación de estados
- `src/autosnake/game/renderer.py` + `ui.py` → render HUD/mensajes

## Parámetros clave
- `FPS = 60`
- `MOVE_TICKS_PER_SEC = 10..15`
- Movimiento discreto por celda

## Criterios de aceptación
1. Juego inicia y renderiza estable.
2. WASD controla snake sin reversa instantánea.
3. Comer incrementa score y longitud.
4. Colisión de pared/cuerpo produce game over.
5. `R` reinicia sin reiniciar proceso.
6. Cierre limpio con `ESC` o botón de ventana.

## Plan incremental por PR
1. Bootstrap técnico (estructura + loop base)
2. Movimiento + input + anti-reversa
3. Comida + score + colisiones + restart
4. Tests + documentación final
