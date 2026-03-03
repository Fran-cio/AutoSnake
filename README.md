<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<div align="center">
  <a href="https://github.com/Fran-cio/AutoSnake">
    <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" alt="Logo" width="90" height="90">
  </a>

  <h3 align="center">AutoSnake</h3>

  <p align="center">
    Snake 2D para PC en Python + pygame, construido con PRs incrementales y trazabilidad SR2.
    <br />
    <a href="docs/IMPLEMENTATION_PLAN.md"><strong>Ver plan de implementación »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Fran-cio/AutoSnake/pulls">Ver PRs</a>
    ·
    <a href="https://github.com/Fran-cio/AutoSnake/issues">Reportar bug</a>
    ·
    <a href="https://github.com/Fran-cio/AutoSnake/issues">Pedir feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tabla de Contenidos</summary>
  <ol>
    <li><a href="#about-the-project">Sobre el proyecto</a></li>
    <li><a href="#current-status">Estado actual</a></li>
    <li><a href="#built-with">Stack</a></li>
    <li><a href="#getting-started">Cómo empezar</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contribuir</a></li>
    <li><a href="#license">Licencia</a></li>
    <li><a href="#contact">Contacto</a></li>
  </ol>
</details>

## Sobre el proyecto

AutoSnake implementa el clásico Snake en una vista 2D de escritorio usando **Python + pygame**.

Objetivos del MVP:
- Controles con **W/A/S/D** (flechas opcionales)
- Movimiento por **grilla** con **tick lógico fijo**
- Score, Game Over y reinicio con `R`
- Código modular, mantenible y fácil de extender

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Estado actual

Ver detalle en [`docs/PROGRESS.md`](docs/PROGRESS.md).

Resumen:
- ✅ PR #1: Documentación inicial y convención de commits con atribución
- ✅ PR #2: Bootstrap técnico con estructura Python + loop base pygame
- 🔄 Próximo: movimiento Snake + input WASD + regla anti-reversa

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Stack

- [![Python][Python.org]][Python-url]
- [![Pygame][Pygame.org]][Pygame-url]

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Cómo empezar

### Requisitos

- Python 3.10+
- pip

### Instalación

1. Clonar repo
   ```sh
   git clone https://github.com/Fran-cio/AutoSnake.git
   cd AutoSnake
   ```
2. Instalar dependencias
   ```sh
   pip install -r requirements.txt
   ```
3. Ejecutar
   ```sh
   PYTHONPATH=src python -m autosnake.main
   ```

> Nota: el entrypoint definitivo del juego completo se mantendrá en `src/autosnake/main.py`.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Roadmap

- [x] Definir arquitectura MVP y plan de PRs incrementales
- [x] Bootstrap de proyecto + loop base desacoplado
- [ ] Movimiento Snake en grilla
- [ ] Input WASD + anti-reversa inmediata
- [ ] Food spawn + crecimiento + score
- [ ] Colisiones (pared/cuerpo) + Game Over
- [ ] Reinicio con `R`
- [ ] Tests de reglas críticas
- [ ] Hardening de docs y QA final

Ver avances en [`docs/PROGRESS.md`](docs/PROGRESS.md).

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Contribuir

Las contribuciones son bienvenidas. Para mantener trazabilidad:

1. Crear branch por objetivo acotado.
2. Usar **Conventional Commits**.
3. Incluir atribución en el mensaje de commit, por ejemplo:
   - `feat(game): add food spawn [by: frontend-dev-sr2]`
4. Abrir PR con alcance, validación y riesgos.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Licencia

Distribuido bajo licencia MIT. Ver `LICENSE` cuando esté agregado.

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

## Contacto

Proyecto: [https://github.com/Fran-cio/AutoSnake](https://github.com/Fran-cio/AutoSnake)

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/Fran-cio/AutoSnake.svg?style=for-the-badge
[contributors-url]: https://github.com/Fran-cio/AutoSnake/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Fran-cio/AutoSnake.svg?style=for-the-badge
[forks-url]: https://github.com/Fran-cio/AutoSnake/network/members
[stars-shield]: https://img.shields.io/github/stars/Fran-cio/AutoSnake.svg?style=for-the-badge
[stars-url]: https://github.com/Fran-cio/AutoSnake/stargazers
[issues-shield]: https://img.shields.io/github/issues/Fran-cio/AutoSnake.svg?style=for-the-badge
[issues-url]: https://github.com/Fran-cio/AutoSnake/issues
[license-shield]: https://img.shields.io/github/license/Fran-cio/AutoSnake.svg?style=for-the-badge
[license-url]: https://github.com/Fran-cio/AutoSnake/blob/main/LICENSE
[Python.org]: https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Pygame.org]: https://img.shields.io/badge/Pygame-2.x-1e1e1e?style=for-the-badge
[Pygame-url]: https://www.pygame.org/news
