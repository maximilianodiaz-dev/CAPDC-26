# CAPDC-49 — US-029 — solicitar una demo gratuita de 14 días desde la landing pública

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-49)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | En curso |
| Sprint | Sprint 2 — Catálogo |
| Story points | 5 |
| Etiquetas | should |
| Responsable | ALBERTO SLEITHER RINCON SEGREDO |
| Épica | — |
| Creada | 2026-10-14 |
| Resuelta | — |

## Descripción

Como visitante de la landing pública, quiero solicitar una demo gratuita de 14 días dejando mis datos de contacto, para evaluar la plataforma antes de registrarme.

**Dependencias:** —  
**Supuesto:** SUP-010 (fuera del árbol de épicas, sin módulo propio)

**Criterios de aceptación:**

1. Dado un visitante sin sesión, cuando completa nombre, nombre del negocio, correo y cantidad de profesionales, entonces la solicitud se registra y se notifica al equipo (reutiliza `NotificationPort`, mismo adaptador de consola que CAPDC-13 hasta que exista el módulo Notification).
2. Dado un campo obligatorio vacío o un correo con formato inválido, cuando se envía el formulario, entonces se rechaza indicando qué corregir.
3. Dada una solicitud enviada con éxito, entonces se confirma visualmente sin redirigir a ningún flujo autenticado (es anónimo, sin cuenta ni tenant).
4. No crea cuenta, usuario ni tenant — es una captura de interés comercial, nunca un alta real en la plataforma.

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (CAPDC-39), sin bajar la cobertura mínima de `03-3`.
* Pull Request de `develop` a `main` revisado y aprobado por un compañero del equipo antes de fusionar (`03-1`).
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

_Fuente: Confluence 01.3 Product Backlog — MVP, §7.1 (v2.6)._
