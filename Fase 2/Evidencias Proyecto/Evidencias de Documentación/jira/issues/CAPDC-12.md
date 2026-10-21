# CAPDC-12 — US-005 — seleccionar el rubro de mi negocio durante el registro

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-12)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | En curso |
| Sprint | Sprint 2 — Catálogo |
| Story points | 8 |
| Etiquetas | must, tenant |
| Responsable | ALBERTO SLEITHER RINCON SEGREDO |
| Épica | CAPDC-2 Tenant |
| Creada | 2026-09-20 |
| Resuelta | — |

## Descripción

Como dueño de negocio, quiero seleccionar el rubro de mi negocio durante el registro, para que el sistema preconfigure servicios y recursos típicos de esa vertical.

**Criterios de aceptación:**

1. Dado un negocio de rubro Salón de belleza o Clínica sin servicios ni recursos, cuando el Dueño acepta la plantilla, entonces se crean los servicios, recursos y grupos definidos en `02-2` §3.5 (UC-03; RF-008; RN-007).
2. Dada la plantilla de Clínica aplicada, entonces "Consulta especialista" requiere a la vez Box 1, Equipo médico y Profesional 2 (Escenario 2); con la de Salón, "Taller de peinados" queda grupal con cupo 4 (Escenario 3).
3. Dados los servicios y recursos creados por la plantilla, entonces son editables y eliminables como cualquier otro, y los recursos quedan "no reservables" hasta configurar su disponibilidad (`02-2` §3.5).
4. Dado un Dueño que omite la plantilla, entonces su negocio queda sin servicios ni recursos (UC-03, A1).
5. Dado un rubro sin plantilla (Gimnasio u Otro), cuando se ofrece la preconfiguración, entonces se informa que no hay plantilla y el negocio queda vacío (UC-03, E1).
6. Dado un negocio que ya tiene servicios o recursos, entonces no se ofrece la plantilla.

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (CAPDC-39), sin bajar la cobertura mínima de `03-3`.
* Pull Request de `develop` a `main` revisado y aprobado por un compañero del equipo antes de fusionar (`03-1`).
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

_Fuente: Confluence 01.3 Product Backlog — MVP, §14 (v2.5)._
