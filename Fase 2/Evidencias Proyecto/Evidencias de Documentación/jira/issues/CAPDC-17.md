# CAPDC-17 — US-010 — configurar la disponibilidad horaria de cada recurso

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-17)

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

Como dueño de negocio, quiero configurar la disponibilidad horaria de cada recurso, para que el sistema sepa cuándo puede reservarse.

**Criterios de aceptación:**

1. Dado un recurso, cuando se define un horario semanal recurrente (día y rango horario), entonces se guarda como su disponibilidad base (UC-08; RF-015).
2. Dado un rango con hora de fin no posterior a la de inicio, cuando se guarda, entonces se rechaza (UC-08, E1).
3. Dado un recurso con disponibilidad base, cuando se agrega una excepción (fecha bloqueada por ausencia o feriado), entonces ese día queda excluido de su disponibilidad (RF-016).
4. Dado un recurso sin disponibilidad configurada, entonces queda marcado como "no reservable" (UC-08, A1).
5. Dado un servicio y un rango de fechas, cuando se calcula la disponibilidad, entonces un bloque es válido solo si cada grupo de recursos del servicio tiene al menos uno disponible a la vez, descontando las excepciones (`02-2` §4.6); las reservas existentes se descuentan en el Sprint 3.
6. Dado un Staff con un recurso vinculado, cuando configura la disponibilidad de ese recurso, entonces se guarda; si intenta configurar la de otro recurso, se le niega el acceso (RN-017).

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (CAPDC-39), sin bajar la cobertura mínima de `03-3`.
* Pull Request de `develop` a `main` revisado y aprobado por un compañero del equipo antes de fusionar (`03-1`).
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

_Fuente: Confluence 01.3 Product Backlog — MVP, §14 (v2.5)._
