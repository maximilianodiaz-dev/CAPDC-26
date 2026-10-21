# CAPDC-10 — US-003 — ver y auditar los tenants dados de alta en la plataforma

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-10)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | Listo |
| Sprint | Sprint 1 — Fundacional |
| Story points | 5 |
| Etiquetas | iam, should |
| Responsable | GENESIS . CACERES FERNANDEZ |
| Épica | CAPDC-1 IAM |
| Creada | 2026-09-20 |
| Resuelta | 2026-10-09 |

## Descripción

Como Super Admin, quiero ver y auditar los tenants dados de alta en la plataforma, para administrar el sistema.

**Dependencias:** US-001, US-002  
**RF:** RF-005, RF-006  
**Casos de uso:** UC-19  
**Reglas relacionadas:** RN-010, RN-020, RNF-005, RNF-015

**Criterios de aceptación:**

1. Dado un Super Admin, cuando solicita el listado de tenants, entonces ve por cada uno solo nombre, estado, fecha de alta y plan (UC-19; RN-010).
2. Dado un Super Admin, cuando consulta cualquier endpoint de administración, entonces ninguna respuesta incluye datos operativos (reservas, clientes) (RN-010).
3. Dado un tenant, cuando el Super Admin lo activa o lo desactiva, entonces su estado se actualiza y el cambio queda en el log estructurado (RF-006; RN-020).
4. Dado un tenant ya desactivado, cuando el Super Admin lo desactiva otra vez, entonces se informa que la operación no aplica (UC-19, E1).
5. Dado un tenant desactivado, cuando un usuario de ese tenant intenta iniciar sesión, entonces se informa que la cuenta no está disponible (RN-020).
6. Dado un usuario que no es Super Admin, cuando accede a la administración de tenants, entonces se le niega el acceso (RNF-005).

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (hasta que exista el pipeline, https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-39#icft=CAPDC-39, se ejecutan en el entorno Docker local).
* Pull Request revisado y mergeado a `main`, con la clave https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-10#icft=CAPDC-10 en la rama, los commits y el título del PR.
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

## Comentarios

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-02

**Módulo Tenant creado** @GENESIS . CACERES FERNANDEZ. Te lo asigno para que sigas con el QA.

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-07

![](blob:https://media.staging.atl-paas.net/?type=file&localId=83c1d02545bf&id=a979f95f-9a2e-475f-810a-0114b6b5f8e7&&collection=&height=752&occurrenceKey=null&width=1981&__contextId=null&__displayType=null&__external=false&__fileMimeType=null&__fileName=null&__fileSize=null&__mediaTraceId=null&url=null)

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

**Resultado QA – US-003: Ver y auditar los tenants dados de alta en la plataforma**

Se completó la revisión funcional mediante pruebas automatizadas e inspección de las vistas y serializadores administrativos.

**Resultados de las pruebas:**

* Administración de tenants: 9/9 pruebas aprobadas.
* Autenticación: 17/17 pruebas aprobadas.
* Suite completa del backend: 93/93 pruebas aprobadas.
* Cobertura global: 99,62%, superior al mínimo exigido del 80%.

**Criterios de aceptación verificados:**

1. El listado administrativo devuelve únicamente los metadatos permitidos: identificador, nombre, estado, plan y fecha de alta.
2. Las vistas de listado, activación y desactivación utilizan un serializador limitado a metadatos administrativos, sin exponer información operativa del negocio.
3. La activación y desactivación actualizan el estado; la prueba de desactivación comprueba además la persistencia y el registro estructurado del evento.
4. Se rechaza una segunda desactivación de un tenant inactivo con HTTP 400.
5. Se bloquea el inicio de sesión de usuarios asociados a tenants inactivos y se permite para tenants activos.
6. Se deniega el acceso administrativo a usuarios que no sean Super Admin y a solicitudes sin autenticación.

**Conclusión:** QA funcional favorable para US-003. Los resultados automatizados y la inspección de la implementación respaldan el cumplimiento de los criterios de aceptación revisados.

La finalización administrativa de la historia queda sujeta a confirmar los requisitos de la definición de hecho relativos al Pull Request, merge a `main`, CI y documentación, según corresponda.
