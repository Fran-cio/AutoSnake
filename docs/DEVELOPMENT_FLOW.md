# Development Flow — AutoSnake (SR2)

## Objetivo
Entregar Snake 2D MVP terminado y dejar trazabilidad de coordinación multiagente.

## Cronología resumida
1. **Arquitectura/PM inicial**: definición de estructura, ADR, DoD y plan de PR incremental.
2. **Validación de acceso GitHub**: primer commit, corrección de identidad de autor bot.
3. **PR de documentación**: README base + plan/progreso.
4. **Orquestación multiagente ampliada**: arquitectura, frontend, backend, QA, security, PM, DevOps, Product, UX/UI, Smart-contracts, Fullstack.
5. **Implementación MVP**: módulos de juego, input, colisiones, food, score, game over, restart.
6. **Hardening**: tests de lógica, CI mínima, docs de interacción con agentes.

## Matriz de delegación (resumen)
| Agente | Foco | Resultado operativo |
|---|---|---|
| lead-architect-sr2 | arquitectura/riesgos | diseño modular + fixed tick |
| frontend-dev-sr2 | gameplay e input | reglas de movimiento + anti-reversa |
| backend-dev-sr2 | lógica testeable | separación lógica pura |
| qa-dev-sr2 | pruebas | cobertura de reglas críticas |
| security-dev-sr2 | higiene seguridad | gitignore/deps/secret hygiene |
| project-manager-sr2 | cierre/retrospectiva | documentación de flujo y DoD |
| devops-dev-sr2 | CI | workflow de tests en GitHub Actions |
| product-manager-sr2 | valor/roadmap | prioridades MVP/v0.2 |
| uxui-dev-sr2 | UX visual | HUD y game-over legibles |
| smart-contracts-dev-sr2 | aplicabilidad | no aplicable al MVP local |
| fullstack-dev-sr2 | release structure | checklist de entrega integral |

## Puntos de mejora identificados
1. **Persistencia de outputs de subagentes**: guardar respuestas completas automáticamente en `docs/agents/raw/`.
2. **Plantilla única de delegación**: objetivo, constraints, formato de salida, DoD.
3. **Preflight de credenciales**: verificar git/gh auth antes de abrir primer PR.
4. **Entorno de test reproducible**: usar devcontainer o workflow local sin depender de `venv` del host.
5. **Automatización de changelog** por PR y estado de hitos.

## Estado de cierre
- Código MVP implementado.
- Documentación de flujo e interacciones disponible.
- CI inicial agregado.
