# CAPDC-11 — US-004 — registrar mi negocio (tenant) en la plataforma

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-11)

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

Como dueño de negocio, quiero registrar mi negocio (tenant) en la plataforma, para empezar a operar.

**Dependencias:** US-001  
**RF:** RF-007  
**Casos de uso:** UC-03  
**Reglas relacionadas:** RN-007, RN-016, RN-019

**Criterios de aceptación:**

1. Dado un Dueño autenticado sin negocio, cuando registra nombre, rubro y datos de contacto (correo y teléfono) válidos, entonces se crea un tenant activo asociado a él como Dueño (UC-03; RF-007).
2. Dado un nombre de negocio, cuando se crea el tenant, entonces el slug se genera desde el nombre (minúsculas, sin tildes, con guiones, 3 a 50 caracteres) y es único (RN-016).
3. Dado un slug ya existente o reservado (`auth`, `app`, `admin`, `api`, `docs`, `login`), cuando se registra el negocio, entonces el slug lleva un sufijo numérico y sigue siendo único (RN-016).
4. Dado un nombre vacío, un rubro no válido o un contacto inválido, cuando se intenta registrar, entonces se rechaza (RN-007).
5. Dado el registro completado, entonces el tenant queda con su rubro y sin servicios ni recursos; la plantilla se aplica en US-005 (Sprint 2).
6. Dado un Dueño que ya tiene un negocio, cuando intenta registrar otro, entonces se rechaza (RN-019).
7. Dado un usuario no autenticado o sin rol Dueño, cuando intenta registrar un negocio, entonces se rechaza (UC-03).

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (hasta que exista el pipeline, https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-39#icft=CAPDC-39, se ejecutan en el entorno Docker local).
* Pull Request revisado y mergeado a `main`, con la clave https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-11#icft=CAPDC-11 en la rama, los commits y el título del PR.
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

## Comentarios

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-02

@GENESIS . CACERES FERNANDEZ CAPDC-11 (US-004, registrar negocio) completado y subido a develop.

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

**Comentario QA – CAPDC-11: Registrar mi negocio (US-004)**

Se realiza validación de la funcionalidad de registro de negocio, verificándose mediante pruebas automatizadas locales el cumplimiento de los principales criterios de aceptación.

**Evidencia de validación:**

* Pruebas específicas de registro de negocio: 12 aprobadas.
* Suite completa del backend: 93 pruebas aprobadas.
* Cobertura global del backend: 99,62 %, superando el mínimo establecido del 80 %.
* Se verifica el registro exitoso del negocio, la asociación al dueño, la generación de slug normalizado y único, el rechazo de registros duplicados por dueño y las restricciones de acceso según autenticación y rol.
* Se verifica la actualización de la documentación técnica y del changelog.
* El commit asociado a CAPDC-11 se encuentra integrado en la rama `main`.

**Observaciones:**  
La ejecución de GitHub Actions reporta un fallo en el trabajo de frontend (`exit code 1`), cuya causa debe revisarse en los registros del pipeline. Asimismo, se identifica como mejora pendiente reforzar las pruebas de validación del formato del teléfono y del correo de contacto, así como la comprobación de ausencia de servicios y recursos.

Considerando los resultados satisfactorios de las pruebas locales y la implementación verificada, se deja constancia del avance de la validación QA, manteniendo registradas las observaciones señaladas para su seguimiento.
