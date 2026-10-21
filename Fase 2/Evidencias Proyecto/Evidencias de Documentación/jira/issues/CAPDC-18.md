# CAPDC-18 — US-011 — definir servicios grupales con cupo máximo (ej. clases de gimnasio)

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-18)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | En curso |
| Sprint | Sprint 2 — Catálogo |
| Story points | 5 |
| Etiquetas | catalog, should |
| Responsable | ALBERTO SLEITHER RINCON SEGREDO |
| Épica | CAPDC-3 Catalog |
| Creada | 2026-09-20 |
| Resuelta | — |

## Descripción

Como dueño de negocio, quiero definir servicios grupales con cupo máximo (ej. clases de gimnasio), para dar soporte a negocios con reservas grupales.

**Criterios de aceptación:**

1. Dado un Dueño, cuando marca un servicio como grupal con un cupo máximo mayor a cero, entonces queda en modalidad grupal — Escenario 3 (UC-09; RF-017).
2. Dado un cupo igual o menor a cero, cuando se guarda, entonces se rechaza (UC-09, E1).
3. Dado un servicio grupal sin cupo, o un servicio individual con cupo, cuando se guarda, entonces se rechaza (`02-3`, restricción de `servicios`).
4. Dado un servicio grupal, cuando se consulta, entonces informa su cupo máximo; el rechazo de reservas por sobre el cupo (RN-006) se verifica en el Sprint 3.

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (CAPDC-39), sin bajar la cobertura mínima de `03-3`.
* Pull Request de `develop` a `main` revisado y aprobado por un compañero del equipo antes de fusionar (`03-1`).
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

_Fuente: Confluence 01.3 Product Backlog — MVP, §14 (v2.5)._
