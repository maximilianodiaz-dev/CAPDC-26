# CAPDC-14 — US-007 — editar los datos generales de mi negocio (nombre, dirección, horario general)

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-14)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | Listo |
| Sprint | Sprint 1 — Fundacional |
| Story points | 3 |
| Etiquetas | should, tenant |
| Responsable | GENESIS . CACERES FERNANDEZ |
| Épica | CAPDC-2 Tenant |
| Creada | 2026-09-20 |
| Resuelta | 2026-10-09 |

## Descripción

Como dueño de negocio, quiero editar los datos generales de mi negocio (nombre, dirección, horario general), para mantener mi información actualizada.

**Dependencias:** US-004  
**RF:** RF-011  
**Casos de uso:** UC-05  
**Reglas relacionadas:** RN-005, RN-016

**Criterios de aceptación:**

1. Dado un Dueño, cuando edita nombre, dirección u horario general con datos válidos, entonces se guardan y una nueva consulta del negocio devuelve los valores actualizados; su visualización en la página pública se verifica cuando exista (Sprint 3) (UC-05).
2. Dado un Dueño, cuando cambia el slug a uno válido y libre, entonces se actualiza y el sistema muestra la advertencia de que los enlaces ya compartidos dejarán de funcionar (RN-016).
3. Dado un slug ya usado, reservado o con formato inválido, cuando se intenta guardar, entonces se rechaza (RN-016).
4. Dados datos incompletos o inválidos (ej. dirección vacía), cuando se intenta guardar, entonces se rechaza hasta corregirlos (UC-05, E1).
5. Dado un horario de cierre no posterior al de apertura, cuando se guarda, entonces se rechaza.
6. Dado un Staff o un Dueño de otro tenant, cuando intenta editar el negocio, entonces se le niega el acceso (RN-005).

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (hasta que exista el pipeline, https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-39#icft=CAPDC-39, se ejecutan en el entorno Docker local).
* Pull Request revisado y mergeado a `main`, con la clave https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-14#icft=CAPDC-14 en la rama, los commits y el título del PR.
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

## Comentarios

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-07

**CAPDC-14 (US-007, editar datos del negocio) completado, backend + frontend, y subido a** `develop`  
  
@GENESIS . CACERES FERNANDEZ @Maximiliano Díaz

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-07

![](blob:https://media.staging.atl-paas.net/?type=file&localId=b58cd5ed08d9&id=60f63074-57b9-438f-babb-3fd0bf2fd9c2&&collection=&height=1041&occurrenceKey=null&width=1460&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

### Resultado QA — US-007: Editar los datos generales del negocio

**Resultado: PRUEBAS SATISFACTORIAS**

Se ejecutaron las pruebas automatizadas del backend en el entorno Docker, obteniendo **12 de 12 pruebas aprobadas** (`12 passed in 6.82s`).

Se validaron los siguientes criterios:

* Actualización del nombre, dirección y horario general del negocio.
* Cambio de identificador público (_slug_) a uno válido y disponible.
* Rechazo de identificadores ocupados, reservados o con formato inválido.
* Rechazo de nombre y dirección vacíos.
* Validación del horario de cierre respecto del horario de apertura.
* Restricción de edición para usuarios staff, dueños de otros negocios y solicitudes sin autenticación.

Adicionalmente, se realizaron pruebas manuales en el frontend, comprobando la modificación de los datos generales, la persistencia de los cambios después de recargar la página y la visualización del aviso sobre los enlaces anteriores al modificar el _slug_.

**Conclusión:** las pruebas automatizadas y las verificaciones funcionales realizadas fueron satisfactorias para los aspectos comprobados. La tarea cuenta con evidencia de QA favorable. La revisión, aprobación y fusión del Pull Request deberán verificarse conforme a la definición de terminado de la historia.
