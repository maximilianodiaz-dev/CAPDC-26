# CAPDC-16 — US-009 — definir recursos (profesionales, salas, equipos) y asociarlos a uno o más servicios

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-16)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | En curso |
| Sprint | Sprint 2 — Catálogo |
| Story points | 8 |
| Etiquetas | catalog, must |
| Responsable | ALBERTO SLEITHER RINCON SEGREDO |
| Épica | CAPDC-3 Catalog |
| Creada | 2026-09-20 |
| Resuelta | — |

## Descripción

Como dueño de negocio, quiero definir recursos (profesionales, salas, equipos) y asociarlos a uno o más servicios, para reflejar cómo opera realmente mi negocio.

**Criterios de aceptación:**

1. Dado un Dueño, cuando crea un recurso con nombre y tipo (profesional, sala o equipo), entonces queda activo en su tenant (UC-07; RF-013).
2. Dado un servicio, cuando el Dueño le asocia varios recursos en un mismo grupo, entonces son alternativas entre sí — Escenario 1, individual con alternativas (RF-014; `02-2` §4.2).
3. Dado un servicio, cuando el Dueño le asocia recursos en grupos distintos, entonces todos se requieren a la vez — Escenario 2, recurso compuesto (UC-07, A1).
4. Dado un recurso de otro tenant, cuando se intenta asociar a un servicio, entonces se rechaza (UC-07, E1; RN-004).
5. Dado un recurso asociado a un servicio, cuando se intenta eliminar, entonces se rechaza y se sugiere desactivarlo (`02-3` §4.6).
6. Dado un recurso de tipo profesional, cuando el Dueño lo vincula a una cuenta de su tenant (Staff o él mismo), entonces queda vinculado; una cuenta se vincula a lo más a un recurso, y las salas y equipos no se vinculan (RN-017).
7. Dado un Staff o un Dueño de otro tenant, cuando intenta gestionar recursos de este tenant, entonces se le niega el acceso (RN-005).

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (CAPDC-39), sin bajar la cobertura mínima de `03-3`.
* Pull Request de `develop` a `main` revisado y aprobado por un compañero del equipo antes de fusionar (`03-1`).
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

_Fuente: Confluence 01.3 Product Backlog — MVP, §14 (v2.5)._
