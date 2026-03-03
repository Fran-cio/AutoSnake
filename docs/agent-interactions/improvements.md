# Improvement Opportunities

1. **Auditoría de subagentes**
   - Problema: no acceso a historial cruzado.
   - Mejora: habilitar visibilidad controlada para sesiones hijas en proyectos auditables.

2. **GitHub auth preflight**
   - Problema: credenciales root/node desalineadas y helper global conflictivo.
   - Mejora: checklist de preflight con `gh auth status`, `git credential.helper`, push dry-run.

3. **PR templates obligatorias**
   - Problema: body inicial mal formateado.
   - Mejora: plantilla versionada en repo + validación automática.

4. **CI temprana**
   - Problema: tests no ejecutables por falta de pytest en entorno.
   - Mejora: GitHub Actions para ejecutar `pip install -r requirements.txt` + `pytest` en cada PR.

5. **Métricas de handoff**
   - Recomendar tracking de:
     - tiempo por subagente,
     - retrabajo por etapa,
     - defect leakage (dev->qa->prod),
     - tamaño medio de PR.
