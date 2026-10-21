# CAPDC-13 — US-006 — invitar y gestionar cuentas de mi staff

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-13)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | Listo |
| Sprint | Sprint 1 — Fundacional |
| Story points | 5 |
| Etiquetas | must, tenant |
| Responsable | GENESIS . CACERES FERNANDEZ |
| Épica | CAPDC-2 Tenant |
| Creada | 2026-09-20 |
| Resuelta | 2026-10-09 |

## Descripción

Como dueño de negocio, quiero invitar y gestionar cuentas de mi staff, para asignarles servicios y horarios.

**Dependencias:** US-004  
**RF:** RF-009, RF-010  
**Casos de uso:** UC-04  
**Reglas relacionadas:** RN-005, RN-018, RN-019

**Criterios de aceptación:**

1. Dado un Dueño, cuando invita un correo válido, entonces se genera un enlace con token firmado y se envía el correo (por consola en desarrollo) (UC-04; RN-019).
2. Dado un enlace vencido (más de 7 días) o ya usado, cuando se intenta registrar, entonces se rechaza (RN-019).
3. Dado un enlace válido, cuando la persona completa su registro con contraseña conforme a RN-018, entonces se crea una cuenta con rol Staff asociada al tenant y aparece en su lista de staff (UC-01, A1).
4. Dado un correo que pertenece a un Dueño de otro tenant, cuando se invita, entonces se rechaza informando el conflicto (UC-04, E1).
5. Dado un Dueño, cuando desactiva a un miembro del staff, entonces su cuenta queda inactiva, no puede iniciar sesión y su registro se conserva (RF-010; UC-04, A1).
6. Dado un Dueño, cuando activa una cuenta de staff desactivada, entonces vuelve a estar activa (RF-010).
7. Dado un Staff o un Dueño de otro tenant, cuando intenta invitar o gestionar staff de este tenant, entonces se le niega el acceso (RN-005).

_Nota de alcance: asignar servicios y horarios al staff no entra en el Sprint 1; depende de Catalog y del vínculo usuario-recurso (RN-017, Sprint 2)._

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (hasta que exista el pipeline, https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-39#icft=CAPDC-39, se ejecutan en el entorno Docker local).
* Pull Request revisado y mergeado a `main`, con la clave https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-13#icft=CAPDC-13 en la rama, los commits y el título del PR.
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

## Comentarios

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-07

**CAPDC-40 (estrategia de calidad, RNF-012) completado y subido a** `develop`**.**

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-07

@Maximiliano Díaz @GENESIS . CACERES FERNANDEZ US-006 — invitar y gestionar cuentas de mi staff Listo.

![](blob:https://media.staging.atl-paas.net/?type=file&localId=79716d1bdcf9&id=97644f57-6584-4160-a907-cf2396aea778&&collection=&height=534&occurrenceKey=null&width=1457&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

**Revisión QA — US-006: Invitar y gestionar cuentas de staff**

Se revisaron las pruebas automatizadas del módulo `tests/test_tenant_staff.py`. Se identificaron 12 pruebas que cubren el flujo de invitaciones, validación de tokens, registro de staff, políticas de contraseña, activación y desactivación de cuentas, autenticación y restricciones de acceso entre tenants.

Las pruebas de los archivos revisados fueron ejecutadas en Docker y aprobaron. Se destaca especialmente la prueba que verifica que un dueño no puede ver ni gestionar el personal de otro tenant.

**Observación:** queda por confirmar que el rechazo de correos existentes cubra específicamente el caso de un dueño perteneciente a otro tenant.

La revisión QA queda documentada con esta observación. La confirmación del Pull Request revisado y fusionado a `main` forma parte de la definición de hecho de la historia.
