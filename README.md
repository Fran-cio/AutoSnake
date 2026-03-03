<a id="readme-top"></a>

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Python][python-shield]][python-url]
[![Pygame][pygame-shield]][pygame-url]

<div align="center">
  <h3 align="center">AutoSnake</h3>
  <p align="center">
    Snake 2D para PC en Python + pygame, con WASD, score, game over y reinicio.
    <br />
    <a href="./docs/DEVELOPMENT_FLOW.md"><strong>Ver flujo completo de desarrollo »</strong></a>
  </p>
</div>

## Sobre el proyecto
Proyecto MVP de Snake con arquitectura modular y trazabilidad por PR/commit.

### Features MVP
- Movimiento por grilla
- Controles WASD (flechas opcionales)
- Anti-reversa inmediata
- Food spawn y crecimiento
- Score en HUD
- Game Over por pared/cuerpo
- Reinicio con `R`
- Salida con `ESC` o cerrar ventana

## Stack
- Python 3.10+
- pygame 2.5+
- pytest (tests de lógica)

## Cómo ejecutar
```bash
pip install -r requirements.txt
PYTHONPATH=src python -m autosnake.main
```

## Cómo testear
```bash
PYTHONPATH=src pytest -q
```

## Documentación
- `docs/IMPLEMENTATION_PLAN.md` — plan técnico y criterios de aceptación
- `docs/PROGRESS.md` — avances/PRs
- `docs/DEVELOPMENT_FLOW.md` — flujo completo y retrospectiva
- `docs/agents/` — interacciones con agentes SR2

## Estado
Proyecto MVP terminado en rama `feat/snake-mvp-complete` y documentado para revisión.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

[issues-shield]: https://img.shields.io/github/issues/Fran-cio/AutoSnake.svg?style=for-the-badge
[issues-url]: https://github.com/Fran-cio/AutoSnake/issues
[license-shield]: https://img.shields.io/github/license/Fran-cio/AutoSnake.svg?style=for-the-badge
[license-url]: https://github.com/Fran-cio/AutoSnake/blob/main/LICENSE
[python-shield]: https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org/
[pygame-shield]: https://img.shields.io/badge/Pygame-2.x-1e1e1e?style=for-the-badge
[pygame-url]: https://www.pygame.org/
