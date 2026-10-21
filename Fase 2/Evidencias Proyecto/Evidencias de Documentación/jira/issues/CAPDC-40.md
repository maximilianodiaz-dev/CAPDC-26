# CAPDC-40 — Estrategia de calidad: cobertura mínima, tipos de prueba y umbrales en CI (RNF-012)

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-40)

| Campo | Valor |
| --- | --- |
| Tipo | Tarea |
| Estado | Listo |
| Sprint | Sprint 1 — Fundacional |
| Story points | — |
| Etiquetas | preparacion |
| Responsable | GENESIS . CACERES FERNANDEZ |
| Épica | — |
| Creada | 2026-09-24 |
| Resuelta | 2026-10-09 |

## Descripción

Task de preparación del Sprint 1 (sin story points). Ver docs/03-1-configuracion-de-github.md §3.1.

## Comentarios

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

**Resultado de validación QA — CAPDC-40: Estrategia de calidad (RNF-012)**

Se verificó la documentación de la estrategia de calidad y la configuración de los umbrales de cobertura en el backend, frontend y pipeline de integración continua.

1. **Tipos de pruebas definidos**

* Pruebas unitarias de dominio en backend.
* Pruebas de integración de API con base de datos real.
* Pruebas unitarias de componentes y servicios de frontend.
* Verificación manual del funcionamiento contra el servidor real.

2. **Umbrales de cobertura configurados**

* Backend: mínimo de 80% de cobertura de líneas.
* Frontend: mínimo de 80% en statements, 80% en lines, 75% en functions y 60% en branches.

3. **Resultados de ejecución local mediante Docker**

* Backend: 93 pruebas aprobadas; cobertura de 99,62%, superior al mínimo del 80%.
* Frontend: 61 pruebas aprobadas en Chrome Headless.
* Cobertura frontend: statements 88,98%; lines 88,67%; functions 87,50%; branches 67,96%. Todas las métricas cumplen sus respectivos umbrales.

4. **Configuración de CI**

  
Se verificó que `.github/workflows/ci.yml` contempla la construcción del backend y frontend, comprobación de migraciones, Ruff, import-linter, pruebas de backend, compilación Angular y pruebas de frontend.

**Conclusión:** la estrategia de calidad está documentada, los umbrales están configurados y las ejecuciones locales verificadas cumplen los mínimos establecidos por RNF-012.

La ejecución local no sustituye la confirmación de una ejecución exitosa del workflow en GitHub Actions, si esta se exige como parte del cierre definitivo.
