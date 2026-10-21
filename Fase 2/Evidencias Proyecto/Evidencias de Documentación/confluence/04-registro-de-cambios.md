> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/17563659) · versión 8 · última edición 2026-10-14

# 04 Registro de Cambios

Registro cronológico (más reciente primero) de los cambios relevantes hechos a los documentos de `docs/`. Cada documento afectado tiene además su propia sección "Control de cambios". Sirve de soporte de trazabilidad para la memoria de título y como guía para actualizar Confluence.

# 2026-10-14 — Confirmado: no se requiere despliegue en AWS, basta un video de la demo

- **El profesor guía confirmó (RES-009)** que la Etapa 6 (Infraestructura AWS) y el despliegue de la Etapa 7 quedan **descartados**, no "diferidos a confirmar" como decía la documentación desde el 2026-09-24. La entrega final se presenta con un **video de la demo** corriendo en contenedores locales, no con un sistema desplegado.
- **6 documentos actualizados** para reflejar la confirmación (antes todos decían "pendiente de confirmación del profesor" o similar): `00-contexto-general` (Cloud: No aplica), `01-1` (Etapa 6 descartada), `01-4` (RES-009 reformulado), `02-1` (§4 Arquitectura Física pasa de "vista preliminar" a "no se implementa"), `03-1` (nota de AWS diferido reformulada), `03-2` (Etapa 6 de "diferida" a "descartada", sin pendiente sobre dónde vive `LLM_API_KEY` en producción).
- No cambia nada del código ni de la arquitectura ya construida — es una confirmación formal de una decisión que ya se venía aplicando en la práctica desde que Sprint 1 empezó a desarrollarse en Docker local.
- Contrato documentado en `00` (v1.4), `01-1` (v1.3), `01-4` (v2.8), `02-1` (v2.4), `03-1` (v3.12), `03-2` (v2.6).

| Documento | Versión |
| --- | --- |
| `00-contexto-general.md` | 1.4 |
| `01-1-acta-de-constitucion-plataforma-saas-de-reservas-y-citas.md` | 1.3 |
| `01-4-especificacion-de-requerimientos-del-sistema-srs.md` | 2.8 |
| `02-1-arquitectura-de-software-del-sistema.md` | 2.4 |
| `03-1-configuracion-de-jira-y-github.md` | 3.12 |
| `03-2-entorno-de-desarrollo-local.md` | 2.6 |

# 2026-10-14 — Corrección: US-029 pasa de CAPDC-43 a CAPDC-49 (colisión con Jira real)

- **Colisión detectada al sincronizar con Confluence/Jira**: la historia US-029 (landing/demo de 14 días) se había registrado como CAPDC-43, asumiendo que era la siguiente clave libre tras CAPDC-42. Al sincronizar este repositorio con el estado real de Jira se descubrió que CAPDC-43 a 48 ya existían, asignados a un Sprint 0 retroactivo (propuesta del proyecto, documentación grupal, mockup funcional — ver `03-1` §5.5) que no constaba en ningún documento previo.
- **US-029 se reincorpora con la clave corregida: CAPDC-49**, la primera libre después de ese rango. Se mantiene en el Sprint 2, 5 SP, Should, sin épica propia — sin cambios en el resto de su definición.
- **Corregidas todas las referencias cruzadas**: `01-3` §7.1/§12, `03-1` §3/§5.2/§5.3/§5.5, y `01-4` (nota de SUP-010, que también citaba la clave incorrecta).
- Contrato documentado en `01-3` (v2.6), `03-1` (v3.11) y `01-4` (v2.7).

| Documento | Versión |
| --- | --- |
| `01-3-product-backlog-mvp.md` | 2.6 |
| `03-1-configuracion-de-jira-y-github.md` | 3.11 |
| `01-4-especificacion-de-requerimientos-del-sistema-srs.md` | 2.7 |

# 2026-10-14 — Enlace de invitación visible en la UI, y correo real sin depender de AWS

- **UX de invitación de staff**: `POST /api/negocio/staff/invitar/` ahora devuelve el token en la respuesta cuando `settings.DEBUG=True`, y la pantalla "Mi equipo" muestra el enlace completo con botón "Copiar" — ya no hace falta revisar los logs del backend para probar el flujo. En producción (con correo real) el cuerpo sigue vacío, el token solo llega por el correo de verdad.
- **Aclaración sobre AWS SES**: SUP-006/DEP-005 (`01-4`) y la tabla de despliegue (`02-1`) ahora dejan explícito que el correo transaccional con AWS SES solo necesita credenciales de API, no el despliegue completo de la app en AWS (RES-009/DEP-006, que sigue diferido) — el adaptador real de `NotificationPort` puede construirse en el Sprint 4 sin esperar a que se retome la infraestructura AWS.
- Contrato documentado en `02-4` (v2.12), `02-1` (v2.3) y `01-4` (v2.6).

| Documento | Versión |
| --- | --- |
| `02-4-diseno-de-estructura-backend.md` | 2.12 |
| `02-1-arquitectura-de-software-del-sistema.md` | 2.3 |
| `01-4-especificacion-de-requerimientos-del-sistema-srs.md` | 2.6 |

# 2026-10-14 — Sprint 0 y frente de documentación grupal

- **Registro retroactivo del Sprint 0** en `03-1` §5.5: la propuesta (CAPDC-43), la documentación grupal Entrega 1 (CAPDC-45) y el mockup funcional (CAPDC-48) se hicieron antes del Sprint 1, pero el Sprint 0 se cerró en Jira recién el 2026-10-14 porque el Sprint 1 se inició sin completarlo antes. No se reescriben las fechas del sprint cerrado.
- **Frente de documentación grupal** (épica CAPDC-44): entregables académicos fuera de los sprints de desarrollo, sin story points. Entregas 2 y 3 (CAPDC-46 y 47) con fechas objetivo internas: 25 oct (cierre del Sprint 2) y 21 nov (cierre de la Etapa 10); se reemplazan si la asignatura fija fechas oficiales.
- **Sprints auxiliares**: "Sprint B" (prueba, cerrado, no se puede eliminar) se conserva; "Sprint 4 — Cierre 2" (vacío) se elimina.
- Con esto, todo lo que existe en Jira queda documentado en Confluence.

| Documento | Versión |
| --- | --- |
| `03-1-configuracion-de-jira-y-github.md` | 3.10 |

# 2026-10-14 — Criterios de aceptación del Sprint 2

- **Nueva §14 en **`01-3`: definición de hecho del Sprint 2 y criterios de aceptación de US-008, US-009, US-010, US-011 y US-005 (CAPDC-15 a 18 y CAPDC-12), redactados solo con lo documentado (RF, casos de uso, RN, modelo de dominio y base de datos).
- **4 decisiones registradas** para poder redactarlos: los criterios que dependen de reservas se verifican en el Sprint 3; eliminar o desactivar servicios y recursos; el Staff solo configura la disponibilidad de su recurso vinculado (RN-017); la plantilla por rubro solo se ofrece con el catálogo vacío.
- **Meta del Sprint 2 en Jira** alineada con `03-1` (incluye el onboarding con plantillas por rubro).
- Criterios cargados en la descripción de las issues de Jira, con `01-3` como fuente.

| Documento | Versión |
| --- | --- |
| `01-3-product-backlog-mvp.md` | 2.5 |

# 2026-10-14 — Sprint 2 inicia el 14 de octubre (no el 12)

- **Ajuste de calendario**: el cierre del Sprint 1 (PR de `develop` a `main` en revisión) se extendió más allá del 11 oct, así que el Sprint 2 inicia el 14 en vez del 12.
- **Mismo criterio que el Sprint 1**: se mantiene fijo el cierre del 25 oct en vez de correr todo el calendario hacia adelante, para no afectar el Sprint 3 ni la fecha de entrega de noviembre. Queda en 11 días efectivos en vez de 14, con el mismo scope (34 SP / 29 Must).
- **Riesgo registrado**: si a mitad de sprint la velocidad real no alcanza a completar el scope en 11 días, aplicar el mismo tipo de Plan B que ya existe para el Sprint 3.
- Contrato documentado en `03-1` (v3.9).

| Documento | Versión |
| --- | --- |
| `03-1-configuracion-de-jira-y-github.md` | 3.9 |

# 2026-10-07 — Corrección: repositorio privado, y revisión en equipo

- **Corregida una nota desactualizada**: desde la v3.0, este documento decía "el repositorio será público". En realidad ya es privado — la nota nunca se actualizó para reflejarlo. Quedó corregida, sin implicar ningún cambio de configuración real en GitHub.
- **El flujo de Pull Request se actualiza**: ya no lo revisa y fusiona solo el autor — se asigna como revisor a un compañero del equipo (agregado como Collaborator en GitHub), que prueba el código y aprueba antes de fusionar.
- Contrato documentado en `03-1` (v3.8).

| Documento | Versión |
| --- | --- |
| `03-1-configuracion-de-jira-y-github.md` | 3.8 |

# 2026-10-07 — CAPDC-40: estrategia de calidad (RNF-012)

- **Nuevo documento** `03-3-estrategia-de-calidad.md`: define los tipos de prueba del proyecto (unitaria de dominio, integración de API, unitaria de frontend, verificación manual) y la cobertura mínima — 80% de líneas en el backend, 80%/80%/75%/60% (statements/lines/functions/branches) en el frontend.
- **Umbrales aplicados en CI y en local** (no solo en el pipeline): `backend/pyproject.toml` (`--cov-fail-under=80`) y `frontend/karma.conf.js` (`coverageReporter.check.global`). Verificado que el gate del frontend realmente bloquea el build subiendo temporalmente el umbral a un valor imposible.
- **Corregido un hueco de medición en el frontend**: Angular solo instrumenta los archivos que algún `.spec.ts` importa; 9 componentes nuevos (pantallas de negocio, staff, panel de Super Admin, layouts) no tenían ninguna prueba y no se medían, aunque el reporte mostraba "92.5%" — un número real pero calculado sobre una fracción pequeña de la app. Se agregaron pruebas livianas a los 9 archivos, llevando la base medida de 160 a 354 statements.
- **RNF-012 actualizado** en `01-4` (v2.4): ya no dice "a definir formalmente en la Etapa 8", cita los umbrales concretos.
- Contrato documentado en `03-3` (v1.0).

| Documento | Versión |
| --- | --- |
| `03-3-estrategia-de-calidad.md` | 1.0 |
| `01-4-especificacion-de-requerimientos-del-sistema-srs.md` | 2.4 |

# 2026-10-07 — CAPDC-39: pipeline de CI en GitHub Actions

- **Implementado** `.github/workflows/ci.yml` con dos jobs, corriendo en cada push y Pull Request a `main`/`develop`:
- `backend`: construye la imagen Docker, `makemigrations --check` (sin migraciones pendientes), `ruff`, `import-linter` (reglas de arquitectura) y `pytest`.
- `frontend`: `ng build` y `ng test` con Chrome headless, reutilizando el servicio `frontend-test` que ya existía en `docker-compose.yml` (con Chromium) pero nunca se había usado.
- **Corregido** un test inestable (`test_login_entrega_tokens_con_usuario_rol_y_tenant`): la resta `exp - iat` podía dar 1 segundo menos por cómo `simplejwt` calcula el `iat` del access token derivado del refresh token; se ajustó la aserción con una tolerancia de ±1s para no arriesgar la confiabilidad del pipeline.
- **Verificado** ejecutando localmente, paso por paso, la misma secuencia de comandos que usa el workflow (incluida la suite completa de 93 pruebas de backend y las 28 de frontend).
- Reglas de protección de `main` concretadas en `03-1` (antes "pendiente de definir al cerrar el pipeline"): requieren los jobs `backend` y `frontend` en verde.

| Documento | Versión |
| --- | --- |
| `03-1-configuracion-de-jira-y-github.md` | 3.7 |

# 2026-10-07 — CAPDC-14 (US-007): editar datos del negocio

- **Implementado** `PATCH /api/negocio/` (y `GET /api/negocio/` para consultarlo): el Dueño edita nombre, dirección (calle, comuna, ciudad) y horario general; a diferencia del registro, estos campos son obligatorios al editar.
- `RegistrarNegocioView`** pasa a **`MiNegocioView`: concentra GET (ver), POST (registrar, CAPDC-11) y PATCH (editar) sobre el mismo recurso `/api/negocio/`.
- **Slug editable**: si se envía uno distinto, se valida formato, palabra reservada y unicidad (RN-016); a diferencia del registro (que agrega un sufijo automático), aquí un slug no disponible se rechaza directamente — es una elección explícita del Dueño.
- **Horario coherente**: un horario de cierre no posterior al de apertura se rechaza antes de tocar la base de datos.
- **Frontend**: pantalla "Mi negocio" (`/app/negocio`) con el formulario de edición, que avisa cuando el slug cambia (los enlaces ya compartidos dejarán de funcionar).
- **Verificado** con 12 pruebas nuevas (93 en total) y probado contra el servidor real (editar datos, cambiar slug, rechazo de slug duplicado/reservado/inválido, rechazo de horario incoherente).
- Contrato documentado en `02-4` (v2.11).

| Documento | Versión |
| --- | --- |
| `02-4-diseno-de-estructura-backend.md` | 2.11 |

# 2026-10-03 — CAPDC-13 (US-006): invitar y gestionar staff

- **Implementado** `POST /api/negocio/staff/invitar/`: el Dueño invita un correo; se genera un token de invitación firmado (`django.core.signing`, vigencia 7 días) sin necesidad de una tabla de invitaciones — el "uso único" se logra porque, una vez aceptada, el correo ya queda registrado y un segundo intento se rechaza por duplicado.
- **Implementado** `POST /api/negocio/staff/aceptar-invitacion/` (público): la persona invitada completa su registro y queda asociada como Staff del tenant, visible de inmediato en `GET /api/negocio/staff/`.
- **Implementado** activar/desactivar staff (`POST .../{id}/activar|desactivar/`): desactivar bloquea el inicio de sesión sin eliminar el registro, preservando su historial (UC-04, A1) — mismo mecanismo que ya bloqueaba el login de un tenant desactivado (RN-020).
- **Nuevo modelo** `MiembroStaff` (entidad interna del agregado Tenant, docs/02-2 §3.2), con FK reales a `tenants` y `usuarios` (`ON DELETE CASCADE`).
- **Nuevo puerto** `NotificationPort` (mismo patrón que `VerificadorTenantPort`): el Sprint 1 solo implementa un adaptador de consola que imprime el "correo" en el log del servidor; el envío real llega en el Sprint 4 con el módulo Notification.
- **Frontend**: pantalla "Mi equipo" (`/app/staff`) para invitar y activar/desactivar staff, y pantalla pública (`/invitacion/aceptar`) para que la persona invitada complete su registro.
- **Verificado** con 12 pruebas nuevas (81 en total) y probado contra el servidor real (invitar, aceptar invitación, listar, desactivar con bloqueo de login, reactivar).
- Contrato documentado en `02-4` (v2.10); `miembros_staff` gana `created_at`/`updated_at` en `02-3` (v2.6), porque todo modelo hereda `BaseModel`.

| Documento | Versión |
| --- | --- |
| `02-4-diseno-de-estructura-backend.md` | 2.10 |
| `02-3-diseno-de-base-de-datos.md` | 2.6 |

# 2026-10-02 — CAPDC-11 (US-004): registrar negocio

- **Implementado** `POST /api/negocio/`: un Dueño autenticado sin negocio registra nombre, rubro, teléfono y (opcionalmente) un correo de contacto distinto al suyo.
- **Slug generado automáticamente** (RN-016) desde el nombre: minúsculas, sin tildes, separado por guiones, 3 a 50 caracteres; si choca con uno existente o con una palabra reservada (`auth`, `app`, `admin`, `api`, `docs`, `login`), se agrega un sufijo numérico hasta encontrar uno disponible.
- **RN-019 implementada**: un Dueño que ya tiene un negocio no puede registrar otro (409).
- Tras el alta, se emiten `access`/`refresh` nuevos para el Dueño (reutilizando `apps.iam.services.emitir_tokens`, extraído de `autenticar`) porque su `tenant_id` acaba de cambiar.
- **Verificado** con 16 pruebas nuevas (69 en total, incluye pruebas puras de la función de normalización del slug) y probado contra el servidor real (registro exitoso, slug con sufijo, rechazo por negocio duplicado).
- Contrato documentado en `02-4` (v2.9).

| Documento | Versión |
| --- | --- |
| `02-4-diseno-de-estructura-backend.md` | 2.9 |

# 2026-10-02 — CAPDC-10 (US-003): Super Admin ve y audita tenants

- **Módulo Tenant creado**, adelantado desde CAPDC-11: el modelo ya tiene el esquema completo documentado (nombre, slug, rubro, dirección, horario, estado, plan, contacto, contexto del asistente), para no migrar dos veces.
- `usuarios.tenant_id`** pasa a ser una FK real**  a `tenants.id`, tal como ya decía el esquema pero que hasta ahora no se podía implementar (no existía `Tenant`). Se usó una referencia perezosa por nombre de app para no romper la regla de dependencia (IAM no importa Tenant).
- **Implementados** los endpoints de administración (`GET /api/admin/tenants/`, activar/desactivar), con permiso exclusivo de Super Admin y log estructurado de cada cambio de estado.
- **RN-020 implementada** vía un puerto (`VerificadorTenantPort`, mismo patrón que `NotificationPort`): el login ahora rechaza a los usuarios de un tenant desactivado.
- **Verificado** con 9 pruebas nuevas (53 en total) y probado contra el servidor real (listado, activar, desactivar, idempotencia, login bloqueado y restablecido).
- Contrato documentado en `02-4` (v2.8).

| Documento | Versión |
| --- | --- |
| `02-4-diseno-de-estructura-backend.md` | 2.8 |

# 2026-09-25 — CAPDC-42: comando para crear el Super Admin

- **Implementado** `manage.py crear_super_admin` (RN-019: es el único camino para crear esta cuenta, no hay auto-registro). Idempotente: ejecutarlo dos veces no duplica ni pisa la cuenta. Credenciales por argumentos o por `SUPERADMIN_EMAIL`/`SUPERADMIN_PASSWORD` en `.env`.
- **Alcance real de la task:** la parte de "datos semilla" queda diferida — Tenant y Catalog todavía no existen en código, así que no hay negocios de demostración que cargar todavía. Se retoma cuando exista Catalog (Sprint 2).
- **Verificado** con 6 pruebas nuevas (44 en total) y probado contra el servidor real (creación, re-ejecución idempotente, login con el rol correcto).

| Documento | Versión |
| --- | --- |
| `02-4-diseno-de-estructura-backend.md` | 2.7 |

# 2026-09-25 — CAPDC-9 (US-002): aislamiento multi-tenant

- **Implementado** el mecanismo genérico de aislamiento: el tenant activo se toma del JWT en un middleware (`TenantMiddleware`), vive en una `ContextVar` durante la petición, y `TenantScopedModel`/`TenantScopedManager` lo aplican automáticamente a cualquier modelo de negocio futuro (Catalog, Booking, ...).
- `apps.iam.Usuario` se mantiene fuera de este mecanismo a propósito (login busca por correo antes de conocer el tenant).
- **Verificado** con 9 pruebas nuevas (38 en total): filtrado por tenant, consulta vacía sin tenant en contexto, lectura/edición/borrado cruzado sin efecto, `tenant_id` obligatorio, y una prueba de integración con login real.
- Contrato documentado en `02-4` §Aislamiento Multi-tenant (v2.6).

| Documento | Versión |
| --- | --- |
| `02-4-diseno-de-estructura-backend.md` | 2.6 |

# 2026-09-25 — Flujo de Git simplificado a 2 ramas

- **Se descartó la rama por historia** (`feature/CAPDC-N-...`); con un solo desarrollador no aportaba aislamiento real. Ahora el flujo es `main`** + **`develop`: todo el trabajo se hace en `develop`, y se integra a `main` por Pull Request cuando el autor lo da por probado.
- **Reorganización aplicada:** el trabajo del Sprint 1 hecho hasta ahora (backend de IAM y esqueleto Angular, antes repartido en 2 ramas de historia) se consolidó en `develop` y se fusionó a `main`. `main` y `develop` quedaron sincronizadas con GitHub (`origin/main`, `origin/develop`).
- **Documentos actualizados:** `03-1` §6 y `CLAUDE.md`.

| Documento | Versión |
| --- | --- |
| `03-1-configuracion-de-jira-y-github.md` | 3.6 |

# 2026-09-24 — CAPDC-8 (US-001) y CAPDC-41: registro, inicio de sesión y esqueleto Angular

- **Implementado** el registro de Dueños, el inicio de sesión con tokens JWT (acceso 30 min, refresco 7 días con rotación) y el límite de 5 intentos fallidos por cuenta y por IP (RN-018, RN-019), con el usuario propio `iam.Usuario`.
- **Contrato de la API** de autenticación documentado en `02-4` §Endpoints de Autenticación (v2.5).
- **Frontend (CAPDC-41 y CAPDC-8):** esqueleto Angular (`core`, `shared`, `layouts`, guards e interceptores) y pantallas de registro e inicio de sesión conectadas a la API mediante un proxy de desarrollo (`02-5` v2.3, `03-2` v2.5).
- **Ajuste de diseño:** se agrega `usuarios.nombre` (UC-01 pide el nombre y el esquema no lo tenía): `02-3` v2.5 y `02-2` v2.5.

| Documento | Versión |
| --- | --- |
| `02-2-modelo-de-dominio-ddd.md` | 2.5 |
| `02-3-diseno-de-base-de-datos.md` | 2.5 |
| `02-4-diseno-de-estructura-backend.md` | 2.5 |
| `02-5-diseno-de-estructura-frontend-angular.md` | 2.3 |
| `03-2-entorno-de-desarrollo-local.md` | 2.5 |

# 2026-09-24 — Criterios de aceptación del Sprint 1 y tablero en español

- **Criterios de aceptación** de las 6 historias del Sprint 1 (US-001, 002, 003, 004, 006 y 007 = CAPDC-8, 9, 10, 11, 13 y 14) con su definición de hecho: `01-3` §13 (v2.4).
- **Decisiones que los sustentan:** un Dueño puede existir sin negocio hasta registrarlo y registra uno solo (RN-019); 5 intentos fallidos de inicio de sesión en 15 minutos bloquean 15 minutos (RN-018); desactivar un tenant bloquea el inicio de sesión de sus usuarios y su página pública (RN-020); el correo y el teléfono son los datos de contacto del negocio; un slug reservado se trata como colisión al generarlo y se rechaza al editarlo (RN-016).
- **Base de datos y dominio:** `usuarios` admite un Dueño sin `tenant_id`; `tenants.telefono` y `tenants.email_contacto` (`02-3` v2.4, `02-2` v2.4).
- **Tablero de Jira en español:** Por hacer, En curso, En revisión, Listo; el Backlog es una vista aparte. Tasks CAPDC-36, 37 y 38 en "Listo"; objetivo del Sprint 1 registrado (`03-1` v3.5).

| Documento | Versión |
| --- | --- |
| `01-3-product-backlog-mvp.md` | 2.4 |
| `01-4-especificacion-de-requerimientos-del-sistema-srs.md` | 2.3 |
| `01-5-especificacion-de-casos-de-uso.md` | 2.2 |
| `02-2-modelo-de-dominio-ddd.md` | 2.4 |
| `02-3-diseno-de-base-de-datos.md` | 2.4 |
| `02-4-diseno-de-estructura-backend.md` | 2.4 |
| `03-1-configuracion-de-jira-y-github.md` | 3.5 |

# 2026-09-24 — Alineación con Confluence y Jira

**Motivo:** se hicieron cambios directamente en Confluence y Jira; los documentos locales se alinean con ellos.

- **Renombre de 03.1:** la página pasa a "03.1 Configuración de Jira y GitHub"; el archivo pasa de `03-1-configuracion-de-github.md` a `03-1-configuracion-de-jira-y-github.md` (v3.4) y se actualizan sus referencias.
- **Backlog cargado en Jira (proyecto CAPDC):** no se importó el CSV; se actualizaron las issues existentes para no duplicarlas: épicas CAPDC-1 a 7, historias CAPDC-8 a 35 (US-001 a US-028, mismo orden) y tasks de preparación CAPDC-36 a 42. Sprints creados con sus fechas y objetivos. `docs/jira/backlog-jira.csv` se conserva como respaldo de referencia.
- **Correspondencia US → CAPDC** en `01-3` §12 (v2.3).
- **Fechas de las épicas** en Jira: IAM y Tenant 24 sep–11 oct; Catalog 12–25 oct; Booking y Assistant 26 oct–8 nov; Notification y Reporting 9–14 nov.

| Documento | Versión |
| --- | --- |
| `01-3-product-backlog-mvp.md` | 2.3 |
| `03-1-configuracion-de-jira-y-github.md` | 3.4 |

# 2026-09-24 — Preparación para iniciar el Sprint 1 (Jira y Confluence)

**Motivo:** el Sprint 1 no pudo iniciarse el 23 sep y se inicia el **jue 24 sep**; además se cierran las decisiones abiertas para poder cargar el backlog en Jira y actualizar Confluence. El calendario de los sprints 2 a 4 no cambia.

| Sprint | Fechas (vigentes) | SP (Must) |
| --- | --- | --- |
| 1 — Fundacional | jue 24 sep–dom 11 oct (18 días) | 39 (31) |
| 2 — Catálogo | lun 12–dom 25 oct | 34 (29) |
| 3 — Reservas + IA | lun 26 oct–dom 8 nov | 76 (68) |
| 4 — Cierre | lun 9–sáb 14 nov | 19 (3) |

**Decisiones aplicadas:**

- **AWS y despliegue diferidos** hasta que el profesor guía confirme (RES-009); el proyecto se desarrolla y demuestra en contenedores locales.
- **US-005 pasa al Sprint 2** (depende de Catalog); US-016 depende de US-017 (se corrige la cita a US-018).
- `tenants.slug` (RN-016): generado desde el nombre, único, con palabras reservadas.
- `recursos.usuario_id` (RN-017): vínculo opcional y único entre un recurso profesional y una cuenta (Staff o Dueño-profesional).
- **Reglas de IAM** (RN-018, RN-019, SUP-011): contraseña de 10 caracteres, tokens de 30 min y 7 días, alta de cuentas por rol, Cliente Final sin cuenta, recuperación de contraseña fuera del MVP.
- **Plantillas iniciales por rubro** (Salón y Clínica, con los tres escenarios del modelo genérico): `02-2` §3.5.
- **Aislamiento multi-tenant**: `TenantScopedModel` + manager; Row-Level Security como mejora posterior (`02-4`).
- **Story points conciliados**: se adoptan las cifras del backlog (131 Must / 168 en total) en lugar de los 104 SP previos al Epic 7.
- **Stack backend**: se eliminan las referencias vigentes a Spring Boot/JPA/ArchUnit (Acta, SRS, `02-1`); se mantienen solo las notas históricas de migración de `02-4` y `03-2`.
- **Asistente**: `00-contexto-general` §9.3 y §12 alineados a Gemini en el MVP y al Plan B; §14 con los ADR ya formalizados.
- **Entorno local implementado en Docker** (PostgreSQL 16, Django, Angular 18), con puertos configurables (`03-2` v2.4).
- **Clave del proyecto Jira **`CAPDC`: reemplaza la clave de ejemplo `EXP` (`03-1` v3.3).
- **Archivo de importación a Jira**: `docs/jira/backlog-jira.csv` (7 épicas, 28 historias, 7 tasks del Sprint 1).

| Documento | Versión |
| --- | --- |
| `00-contexto-general.md` | 1.3 |
| `01-1-acta-de-constitucion-...md` | 1.2 |
| `01-3-product-backlog-mvp.md` | 2.2 |
| `01-4-especificacion-de-requerimientos-del-sistema-srs.md` | 2.2 |
| `01-5-especificacion-de-casos-de-uso.md` | 2.1 |
| `02-1-arquitectura-de-software-del-sistema.md` | 2.2 |
| `02-2-modelo-de-dominio-ddd.md` | 2.3 |
| `02-3-diseno-de-base-de-datos.md` | 2.3 |
| `02-4-diseno-de-estructura-backend.md` | 2.3 |
| `02-5-diseno-de-estructura-frontend-angular.md` | 2.2 |
| `03-1-configuracion-de-jira-y-github.md` | 3.3 |
| `03-2-entorno-de-desarrollo-local.md` | 2.4 |

# 2026-09-23 — Calendario de sprints reprogramado (reemplazado en parte el 2026-09-24)

**Motivo:** el Sprint 1 inicia el mismo día (mié 23 sep) en lugar del 17 oct. Se mantiene la fecha de cierre. No cambian la metodología (Scrum), las épicas por sprint, las 28 historias ni los objetivos de cada sprint.

| Sprint | Fechas anteriores | Fechas nuevas |
| --- | --- | --- |
| 1 — Fundacional | 17–24 oct | mié 23 sep–dom 11 oct (19 días, incluye la preparación) |
| 2 — Catálogo | 25 oct–1 nov | lun 12–dom 25 oct |
| 3 — Reservas + IA | 2–8 nov | lun 26 oct–dom 8 nov |
| 4 — Cierre | 9–14 nov | sin cambio (lun 9–sáb 14 nov) |
| Etapa 10 (cierre) | 15–21 nov | sin cambio |

| Documento | Versión | Cambio |
| --- | --- | --- |
| `03-1-configuracion-de-jira-y-github.md` | 3.1 | Fechas de los 4 sprints, nota de reprogramación, preparación como Tasks del Sprint 1, estrategia de calidad (Etapa 8) como Task del Sprint 1 |
| `01-1-acta-de-constitucion-...md` | 1.1 | Roadmap: Etapas 6, 7 y 8 absorbidas en el Sprint 1; Etapa 9 pasa a 23 sep–14 nov |
| `01-3-product-backlog-mvp.md` | 2.1 | Plazo de implementación actualizado |
| `00-contexto-general.md` | 1.2 | Fechas por sprint en §11; plazo de ~7,5 semanas |
| `02-1-arquitectura-de-software-del-sistema.md` | 2.1 | Plazo de implementación actualizado |
| `03-2-entorno-de-desarrollo-local.md` | 2.3 | Etapas 6, 7 y 8 pasan a ser Tasks del Sprint 1 |

# 2026-09-23 — Plan de 4 sprints y reparto Jira / GitHub

- `03-1` v3.0: backlog y sprints pasan a Jira; GitHub queda solo para código y PRs. Plan aprobado de 4 sprints con todo el Epic 7 (asistente IA) en el Sprint 3; se descarta el Sprint 5.
- `00-contexto-general.md` v1.1: §11 alineado a los 4 sprints con el Epic 7 en el Sprint 3.
- `01-3` v2.1: se descarta la recomendación del Sprint 5.
- **Pendiente:** conciliar 104 SP (plan aprobado) con 131 SP Must-have (Backlog v2.0).

# 2026-09-23 — Objetivos específicos

- `00-contexto-general.md` v1.1: la Sección 6 "Tres Pilares" se reemplaza por los 3 objetivos específicos de la presentación (Jira y Confluence; modelo de negocio genérico; IA en el agendamiento).

# 2026-09-23 — Decisiones de producto

- Modelo genérico: campo `grupo` en `RequisitoRecurso` / `servicio_recurso` para distinguir recursos alternativos de recurso compuesto (`02-2` y `02-3`).
- Proveedor LLM: Google Gemini (modelo Flash), ~10 USD/mes financiado por Alberto Rincón (`01-4` RES-006, DEP-009, SUP-008/009; `02-1` ADR-005; `03-2` `LLM_PROVIDER=gemini`).
- Planes Básico / Pro: `tenants.plan` (`02-2`, `02-3`); regla RN-015: el asistente solo está disponible en plan PRO (`01-4`, `02-4`, `02-5`).
- Landing pública con calculadora y solicitud de demo: feature `landing/` y ruta `/` (`02-5`), captura de leads sin entidad nueva (`02-4`, SUP-010 en `01-4`).
- Alcance: solo 2 verticales piloto (Salón, Clínica); Gimnasio soportado en el esquema pero fuera del alcance demostrado (`01-3` §10, `02-3`).
