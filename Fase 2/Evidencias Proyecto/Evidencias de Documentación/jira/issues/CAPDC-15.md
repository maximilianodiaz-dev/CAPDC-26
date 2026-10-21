# CAPDC-15 — US-008 — crear y editar servicios (nombre, duración, precio)

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-15)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | En curso |
| Sprint | Sprint 2 — Catálogo |
| Story points | 5 |
| Etiquetas | catalog, must |
| Responsable | ALBERTO SLEITHER RINCON SEGREDO |
| Épica | CAPDC-3 Catalog |
| Creada | 2026-09-20 |
| Resuelta | — |

## Descripción

Como dueño de negocio, quiero crear y editar servicios (nombre, duración, precio), para ofrecerlos a mis clientes.

**Criterios de aceptación:**

1. Dado un Dueño, cuando crea un servicio con nombre, duración y precio válidos, entonces queda activo en el catálogo de su tenant (UC-06; RF-012).
2. Dada una duración igual o menor a cero, o un precio negativo, cuando se guarda, entonces se rechaza (UC-06, E1).
3. Dado un servicio existente, cuando el Dueño edita sus datos con valores válidos, entonces una nueva consulta devuelve los valores actualizados (RF-012).
4. Dado un servicio, cuando el Dueño lo desactiva, entonces queda inactivo y se conserva su registro; cuando lo elimina y no tiene reservas, se elimina. El bloqueo por reservas futuras se verifica en el Sprint 3 (UC-06, A1 y E2).
5. Dado un Staff o un Dueño de otro tenant, cuando intenta crear, editar o eliminar servicios de este tenant, entonces se le niega el acceso (RN-005).

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (CAPDC-39), sin bajar la cobertura mínima de `03-3`.
* Pull Request de `develop` a `main` revisado y aprobado por un compañero del equipo antes de fusionar (`03-1`).
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

_Fuente: Confluence 01.3 Product Backlog — MVP, §14 (v2.5)._
