> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13729847) · versión 7 · última edición 2026-10-14

# Diseño de Estructura Backend (Django REST Framework)

| Campo | Información |
| --- | --- |
| Documento | Diseño de Estructura Backend (Django REST Framework) |
| Etapa | 4 — Diseño Backend |
| Versión | 2.12 — `POST /api/negocio/staff/invitar/` devuelve el token en `DEBUG` para mostrarlo en la UI (2026-10-14); v2.11: editar datos del negocio (CAPDC-14) |
| Rol aplicado | Arquitecto Backend / Backend Architect Python |
| Entrada | `05-arquitectura-software.md`, `06-modelo-dominio.md`, `07-modelo-base-datos.md` |
| Cambios principales | Incorporación de la app `assistant` (Epic 7) |
| Estado | Vigente |
| Última actualización | 2026-10-07 |

# 0. ADR-004 — Framework Backend: Django REST Framework

| Campo | Detalle |
| --- | --- |
| Contexto | El equipo posee mayor experiencia y velocidad de desarrollo con Python que con Java. |
| Problema | Riesgo de capacidad identificado en Discovery: 92 Story Points Must-Have en 4 semanas. |
| Decisión | Reemplazar Spring Boot por Django + Django REST Framework (DRF). |
| Fecha | Etapa 4 |
| Estado | Aprobado |

## Alternativas Evaluadas

| Alternativa | Evaluación | Decisión |
| --- | --- | --- |
| Spring Boot | Decisión original (RES-001) | Rechazada |
| FastAPI | Mejor encaje teórico con Clean Architecture | Rechazada |
| Django + DRF | Mayor productividad y experiencia del equipo | Aprobada |

## Consecuencias Aceptadas

| Consecuencia | Mitigación |
| --- | --- |
| Django utiliza Active Record (`models.py`) | Prohibición explícita de lógica de negocio en modelos |
| Riesgo de mezclar persistencia y dominio | Uso obligatorio de `domain.py` |
| Riesgo de acoplamiento arquitectónico | Reglas de `import-linter` |

## Enforcement Arquitectónico

| Herramienta | Propósito |
| --- | --- |
| import-linter | Validar dependencias permitidas |
| Regla principal | `domain.py` no puede importar `django.db` |
| Resultado | Falla automática del pipeline CI |

# 1. Componentes que se Mantienen Sin Cambios

| Elemento | Estado |
| --- | --- |
| Bounded Contexts | Sin cambios |
| Shared Kernel | Sin cambios |
| ADR-001 (Monolito Modular) | Sin cambios |
| ADR-002 (Comunicación por interfaces) | Sin cambios |
| Modelo de Dominio (`06-modelo-dominio.md`) | Sin cambios |
| PostgreSQL (`07-modelo-base-datos.md`) | Sin cambios |
| Restricción EXCLUDE | Sin cambios |

# 2. Árbol de Proyecto Completo

## Resumen General

| Campo | Información |
| --- | --- |
| Proyecto | `backend/` dentro del monorepo `expertia` |
| Framework | Django REST Framework |
| Patrón arquitectónico | Monolito Modular |
| Organización | Módulos por bounded context |
| Lenguaje | Python |
| Gestor de dependencias | Poetry |
| Configuración | Centralizada en `config/` |
| Módulos de negocio | 7 |
| Shared Kernel | Sí |
| Epic 7 | Incluido mediante `apps/assistant/` |

## Estructura General del Proyecto

```
backend/
├── manage.py
├── pyproject.toml
├── Dockerfile.dev
├── .importlinter
│
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── docker.py
│   ├── urls.py
│   ├── exception_handler.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── shared/
│   ├── iam/
│   ├── tenant/
│   ├── catalog/
│   ├── booking/
│   ├── notification/
│   ├── reporting/
│   └── assistant/
│
└── tests/
```

## Directorio Raíz

| Elemento | Responsabilidad |
| --- | --- |
| `manage.py` | Punto de entrada para la ejecución de comandos Django. |
| `pyproject.toml` | Gestión de dependencias mediante Poetry (ver `docs/11`). |
| `config/` | Configuración transversal del sistema. |
| `apps/` | Contenedor de los módulos de negocio. |
| `tests/` | Pruebas automatizadas con estructura espejo de `apps/`. |

## Configuración Global (`config/`)

| Elemento | Responsabilidad |
| --- | --- |
| `settings/` | Configuración por entorno. |
| `urls.py` | Routing raíz, incluye los `urls.py` de cada app. |
| `exception_handler.py` | Manejo global de excepciones, equivalente a `GlobalExceptionHandler` de la versión Java. |
| `asgi.py` / `wsgi.py` | Configuración de despliegue y ejecución de Django. |

### Configuración por Entorno (`config/settings/`)

| Archivo | Responsabilidad |
| --- | --- |
| `base.py` | Configuración compartida del sistema (`INSTALLED_APPS`, `REST_FRAMEWORK`, `SIMPLE_JWT`, etc.). |
| `dev.py` | Configuración para desarrollo local utilizando PostgreSQL en `localhost:5432`. |
| `docker.py` | Configuración para entorno Docker utilizando el servicio `postgres` definido en `docker-compose`. |

## Módulos del Sistema (`apps/`)

### Shared Kernel

| Elemento | Responsabilidad |
| --- | --- |
| `domain.py` | Contiene elementos compartidos como `TenantId`, `RangoHorario` y `DomainException`. |
| `models.py` | Modelo abstracto base con atributos comunes (`created_at`, `updated_at`, `TenantScopedModel`). |

### Módulos de Negocio

| Módulo | Responsabilidad |
| --- | --- |
| `iam` | Identidad y Acceso. |
| `tenant` | Gestión de Negocio. |
| `catalog` | Servicios y Recursos. |
| `booking` | Motor de Reservas (dominio núcleo). |
| `notification` | Notificaciones. |
| `reporting` | Dashboard y Reportes (solo lectura). |
| `assistant` | Asistente Conversacional (Epic 7, incorporado en v2.1). |

**Nota (2026-09-23):**  la landing pública y su formulario de solicitud de demo (captura de leads comerciales, SUP-010) **no**  tienen una app propia — es contenido de marketing, no un bounded context. Se expone como un endpoint liviano dentro de `apps/tenant/` (ej. `POST /api/leads/`) que reutiliza `NotificationPort` para avisar al equipo; no agrega modelos ni servicios de dominio nuevos.

**Puerto de notificación en desarrollo:**  `NotificationPort` se define en el Sprint 1 (la invitación de staff lo necesita, US-006) con un adaptador de consola que imprime el correo; el adaptador real (correo transaccional) se implementa en el Sprint 4 con el módulo Notification.

## Directorio de Pruebas

| Elemento | Responsabilidad |
| --- | --- |
| `tests/` | Contiene pruebas automatizadas del sistema. |
| Estructura espejo | Replica la organización de `apps/` para mantener consistencia entre módulos y pruebas. |

## Justificación Arquitectónica de `apps/`

| Decisión | Justificación |
| --- | --- |
| Utilizar `apps/` como carpeta contenedora | Mantiene la organización por módulo primero definida en la arquitectura. |
| No ubicar las apps en la raíz del proyecto | Evita mezclar visualmente componentes técnicos (`manage.py`, `config/`) con los módulos de negocio. |
| Mantener agrupados los bounded contexts | Refuerza la separación lógica entre dominios funcionales. |
| Seguir una organización orientada al negocio | Facilita la comprensión de la arquitectura y la navegación del repositorio. |

# 3. Estructura Interna de cada App

## Referencia: Booking

### Estructura

```
apps/booking/
├── models.py
├── domain.py
├── services.py
├── repositories.py
├── validators.py
├── serializers.py
├── views.py
├── permissions.py
├── exceptions.py
├── urls.py
├── migrations/
└── tests.py
```

## Responsabilidad de cada archivo

| Archivo | Equivalencia Arquitectónica | Responsabilidad |
| --- | --- | --- |
| `models.py` | infrastructure/persistence | Modelos Django (Active Record) |
| `domain.py` | domain/model | Dataclasses puras de Python |
| `services.py` | application/service | Orquestación de casos de uso |
| `repositories.py` | infrastructure/mapper | Traduce QuerySets ↔ dataclasses |
| `validators.py` | domain/service | Servicios de dominio y validaciones de negocio |
| `serializers.py` | api/dto | DRF Serializers |
| `views.py` | api/controller | DRF ViewSets |
| `permissions.py` | security | Control de acceso específico del módulo |
| `exceptions.py` | application/domain | Excepciones específicas |
| `urls.py` | routing | Rutas del módulo |
| `migrations/` | persistence | Migraciones autogeneradas |
| `tests.py` | testing | Pruebas del módulo |

## models.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Clases `models.Model` de Django |
| Origen | Mapeadas 1:1 desde `07-modelo-base-datos.md` |
| Incluye | Constraints e índices PostgreSQL |
| Restricción | No contiene lógica de negocio |

## domain.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Modelo de dominio puro |
| Tecnología | Dataclasses de Python |
| Dependencias Django | Ninguna |
| Contenido | Entidades y Value Objects definidos en `06-modelo-dominio.md` |
| Objetivo | Permitir pruebas unitarias sin base de datos |

## services.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Implementación de casos de uso |
| Función principal | Orquestar flujo de aplicación |
| Ejemplo | `CrearReservaService` implementa UC-11 |
| Dependencias | validators.py, repositories.py y otros módulos |

## repositories.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Traducir modelos ORM a objetos de dominio |
| Función | Frontera entre dominio y persistencia |
| Equivalencia Java | infrastructure/mapper |

## validators.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Servicios de dominio |
| Ejemplo | `ValidadorDisponibilidadService` |
| Reglas asociadas | RN-001, RN-002 y RN-006 |
| Operan sobre | `domain.py` |

## serializers.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Contratos HTTP |
| Tecnología | DRF Serializers |
| Equivalencia Java | DTO |
| Función | Mapeo API ↔ Application |

## views.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Endpoints REST |
| Tecnología | DRF ViewSet / APIView |
| Función | Traducir HTTP ↔ Services |
| Restricción | Sin lógica de negocio |

## permissions.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Control de acceso |
| Tecnología | BasePermission de DRF |
| Ejemplo | `EsPropietarioDeLaReserva` |

## exceptions.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Excepciones específicas del módulo |
| Ejemplos | `SolapamientoReservaException`, `CupoAgotadoException` |

## urls.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Definir rutas del módulo |
| Integración | Incluidas desde `config/urls.py` |

## migrations

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Versionado de esquema |
| Generación | `manage.py makemigrations` |

## tests.py

| Campo | Descripción |
| --- | --- |
| Responsabilidad | Pruebas del módulo |
| Alcance | Unitarias e integración |

# 3.1 App `assistant` (Epic 7, nuevo en v2.1)

## Estructura

```
apps/assistant/
├── models.py
├── domain.py
├── services.py
├── ports.py
├── adapters.py
├── tools.py
├── repositories.py
├── serializers.py
├── views.py
├── permissions.py
├── exceptions.py
├── urls.py
├── migrations/
└── tests.py
```

## Responsabilidad de cada archivo

| Archivo | Responsabilidad |
| --- | --- |
| `models.py` | Modelos Django: `Conversacion`, `Mensaje` (`07-modelo-base-datos.md` §4.11). |
| `domain.py` | Dataclasses: `Conversacion`, `Mensaje` (`06-modelo-dominio.md` §8). |
| `services.py` | `OrquestadorAsistenteService`. No contiene reglas de negocio de reserva ni catálogo. |
| `ports.py` | `LlmProviderPort` (`typing.Protocol`) definido en ADR-005. |
| `adapters.py` | Implementación concreta de `LlmProviderPort` para el proveedor LLM seleccionado (DEP-009). |
| `tools.py` | Catálogo cerrado de herramientas invocables por el LLM. Cada herramienta es un wrapper sobre servicios de `catalog` o `booking`. |
| `repositories.py` | Traducción entre QuerySets de Django y dataclasses de `domain.py`. |
| `serializers.py` | DRF Serializers para el endpoint de chat. |
| `views.py` | DRF ViewSet que expone el endpoint conversacional (ej. `POST /api/assistant/mensajes/`). |
| `permissions.py` | Acceso público (Cliente Final sin cuenta, mismo comportamiento que UC-10 y UC-11). |
| `exceptions.py` | `LlmNoDisponibleException` (RNF-018). |
| `urls.py` | Configuración de rutas del módulo. |
| `migrations/` | Migraciones de base de datos. |
| `tests.py` | Pruebas del módulo. |

## Diferencia clave respecto a las demás apps

| Aspecto | Descripción |
| --- | --- |
| Reglas de negocio | `apps/assistant/services.py` no implementa reglas de negocio de reserva ni catálogo. |
| Reutilización de servicios | Las reglas ya existen en `apps/booking/services.py` y `apps/catalog/services.py`. |
| Servicio principal | `OrquestadorAsistenteService` importa e invoca directamente servicios de Booking y Catalog. |
| Dependencias permitidas | Assistant → Booking, Assistant → Catalog. |
| Restricción RN-013 | `tools.py` materializa el límite funcional del asistente. |
| Alcance del LLM | Si una función no está definida en `tools.py`, el LLM no puede invocarla. |

## Ubicación de `ports.py` y `adapters.py`

| Decisión | Justificación |
| --- | --- |
| Ubicación | Ambos archivos se encuentran dentro de `assistant`. |
| Motivo | `assistant` es el único módulo que depende del proveedor de LLM. |
| Comparación | A diferencia de `NotificationPort`, que vive conceptualmente cerca de `booking`, el puerto del LLM no necesita ser conocido por otros módulos. |
| Consistencia arquitectónica | Decisión alineada con ADR-005. |

# 4. Mapeo con la Versión Java Original

## Equivalencia entre Clean Architecture y Django/DRF

| Concepto Clean Architecture (`05`, `06`) | Django / DRF |
| --- | --- |
| `api/controller` | `views.py` |
| `api/dto` | `serializers.py` |
| `application/service` | `services.py` |
| `domain/model` | `domain.py` (dataclasses, no `models.Model`) |
| `domain/service` | `validators.py` |
| `domain/repository` (interfaz) | Función o protocolo definido en `repositories.py` |
| `infrastructure/persistence` | `models.py` |
| `infrastructure/mapper` | Funciones de traducción dentro de `repositories.py` |
| `application/port` (ej. `NotificationPort`) | Protocolo de Python (`typing.Protocol`) definido en `apps/booking/ports.py`, implementado en `apps/notification/adapters.py` |

# 5. Security

## Componentes de Seguridad

| Componente | Equivalente Django/DRF |
| --- | --- |
| Autenticación JWT | `djangorestframework-simplejwt` — emite y valida tokens de acceso/refresco |
| Modelo de usuario | `AUTH_USER_MODEL` custom en `apps/iam/models.py` (extiende `AbstractBaseUser`), con mapeo a `domain.py::Usuario` vía `repositories.py` |
| Hashing de contraseñas | Hasher por defecto de Django (PBKDF2 o Argon2 si se instala `argon2-cffi`) |
| Control de acceso por rol | Clases `permissions.py` por app (ej. `EsDuenoDeNegocio`, `EsSuperAdmin`) aplicadas en `views.py` mediante `permission_classes` |
| CORS | `django-cors-headers`, configurado en `config/settings/base.py` |

## Políticas de Autenticación y Alta de Cuentas (RN-018, RN-019)

| Aspecto | Decisión |
| --- | --- |
| Modelo de usuario | `AUTH_USER_MODEL` propio en `apps/iam` (UUID, email, rol, `tenant_id` nulable, estado). Se define en US-001 antes de la primera migración; hasta entonces `simplejwt` está desactivado y todo endpoint niega el acceso por defecto |
| Contraseñas | Mínimo 10 caracteres, no común, no solo numérica (validadores de Django) |
| Tokens | Acceso 30 minutos; refresco 7 días con rotación |
| Intentos de inicio de sesión | 5 intentos fallidos en 15 minutos → bloqueo de 15 minutos, por IP y por cuenta (throttling de DRF, RN-018) |
| Auto-registro | Solo crea `DUENO_NEGOCIO` |
| Staff | Solo por invitación: token firmado (`django.core.signing`), de un solo uso, vence a los 7 días |
| Super Admin | Se crea con `manage.py crear_super_admin` (implementado, CAPDC-42). Idempotente: si ya existe, no hace nada; si el correo pertenece a otra cuenta, falla sin pisarla. Credenciales por `--email`/`--password` o por las variables `SUPERADMIN_EMAIL`/`SUPERADMIN_PASSWORD` (`.env.example`) |
| Cliente Final | Sin cuenta en el MVP (SUP-011); reserva con nombre y correo |
| Recuperación de contraseña | Fuera del MVP (SUP-011) |

## Módulo Tenant — creado antes de lo previsto (CAPDC-10, 2026-10-02)

CAPDC-10 (US-003, "Super Admin ve y audita tenants") necesita el modelo `Tenant`, formalmente
trabajo de CAPDC-11 (US-004). Para no migrar dos veces, `apps/tenant/models.py` ya tiene el
esquema completo de `docs/07-modelo-base-datos.md` §4.1 (nombre, slug, rubro, dirección, horario,
estado, plan, teléfono, correo de contacto, contexto del asistente); CAPDC-10 solo implementa el
listado de metadatos y activar/desactivar. CAPDC-11 reutiliza este mismo modelo para el registro
real del negocio, sin migración nueva.

`usuarios.tenant_id`** pasa a ser una FK real**  a `tenants.id` (`ON DELETE RESTRICT`), tal como ya
decía `docs/07-modelo-base-datos.md` §4.2 pero que hasta ahora era solo un `UUIDField` suelto (no
existía `Tenant` para referenciar). Se implementó con `models.ForeignKey("tenant.Tenant", ...)` —
una referencia perezosa por nombre de app, que no requiere `import apps.tenant` en el código de
IAM y por lo tanto no viola la dirección de dependencia (`Tenant -> IAM`, nunca al revés, `docs/05-arquitectura-software.md` §3). `usuario.tenant_id` se sigue usando igual que antes.

## Endpoints de Administración de Tenants (UC-19, RF-005, RF-006, implementados)

| Endpoint | Función | Respuestas |
| --- | --- | --- |
| `GET /api/admin/tenants/` | Lista todos los tenants, solo con metadatos administrativos (RN-010): `id`, `nombre`, `estado`, `plan`, `fecha_alta` — nunca rubro, slug, dirección, teléfono, correo de contacto ni contexto del asistente | 200; 403 (no es Super Admin) |
| `POST /api/admin/tenants/{id}/activar/` | Activa un tenant | 200; 400 (ya estaba activo); 404 |
| `POST /api/admin/tenants/{id}/desactivar/` | Desactiva un tenant | 200; 400 (ya estaba inactivo); 404 |

Todos requieren el permiso `EsSuperAdmin` (`apps/tenant/permissions.py`). Cada cambio de estado
queda en el log estructurado (`apps.tenant`, RNF-015) con el tenant, el estado anterior/nuevo y
el Super Admin que lo hizo.

**Puerto **`VerificadorTenantPort`** (RN-020):**  el login (`apps.iam.services.autenticar`) necesita
saber si el tenant del usuario está activo, pero IAM no puede importar Tenant. Se resuelve con el
mismo patrón que `NotificationPort`/`LlmProviderPort` (ADR-002): `apps/iam/ports.py` define el
puerto (un `Protocol`), y `apps/tenant/adapters.py::VerificadorTenantDjango` lo implementa; se
registra en `TenantConfig.ready()`. Si el tenant de un usuario está inactivo (o no existe), el
login responde igual que una cuenta desactivada (403, "La cuenta no está disponible").

## Endpoints de Mi Negocio (`MiNegocioView`, UC-03/UC-05, RF-007/RF-011)

`apps/tenant/views.py::MiNegocioView` concentra las tres operaciones sobre el negocio del Dueño
autenticado, por verbo HTTP sobre el mismo recurso `GET/POST/PATCH /api/negocio/`:

| Endpoint | Función | Respuestas |
| --- | --- | --- |
| `POST /api/negocio/` | Registra el negocio (`nombre`, `rubro`, `telefono`, `email_contacto` opcional) — CAPDC-11 | 201 (tenant creado + tokens renovados); 400; 401; 403; 409 (ya tiene un negocio, RN-019) |
| `GET /api/negocio/` | Devuelve los datos completos del negocio propio (incluye dirección y horario) — CAPDC-14 | 200; 401; 403; 404 (el Dueño no tiene negocio aún) |
| `PATCH /api/negocio/` | Edita nombre, dirección, horario y (opcional) el slug — UC-05, CAPDC-14 | 200; 400 (datos inválidos, horario incoherente, o slug no disponible); 401; 403; 404 |

**Registro (**`POST`**, CAPDC-11):** requiere `EsDuenoDeNegocio`. Si no se envía `email_contacto`, se
usa el correo del propio Dueño. El `slug` no se solicita: se genera desde el `nombre` con
`apps.tenant.domain.normalizar_para_slug` (minúsculas, sin tildes, separado por guiones, 3 a 50
caracteres, RN-016); si el resultado ya existe o coincide con una palabra reservada (`auth`,
`app`, `admin`, `api`, `docs`, `login`), `apps.tenant.services.generar_slug_unico` agrega un
sufijo numérico hasta encontrar uno disponible. El tenant queda `ACTIVO`, con plan `BASICO` y sin
servicios ni recursos — la plantilla por rubro se aplica en US-005 (Sprint 2).

Como el `tenant_id` del Dueño cambia en el momento del registro, la respuesta incluye un par
`access`/`refresh` nuevo (`apps.iam.services.emitir_tokens`, extraído de `autenticar` para
reutilizarlo aquí) para que no tenga que volver a iniciar sesión; el token emitido en el login
original sigue siendo válido hasta su expiración natural (30 min) pero con `tenant_id: null`.

La verificación de unicidad del slug es una consulta más una escritura secuenciales (sin bloqueo
a nivel de base de datos); se considera aceptable para el volumen de un proyecto académico (bajo
concurrencia), igual que el resto de las decisiones de alcance de `SUP-005`.

**Editar (**`PATCH`**, UC-05, CAPDC-14):** a diferencia del registro, aquí `nombre`, `calle`, `comuna`,
`ciudad`, `horario_apertura` y `horario_cierre` son todos obligatorios (decisión documentada en
`01-3` §13: "la dirección es opcional al registrar y obligatoria al editar"). El `slug` es
opcional; si se envía y es distinto del actual, se valida formato (RN-016: minúsculas, números y
guiones, 3 a 50 caracteres), palabra reservada y unicidad (excluyendo el propio tenant) — a
diferencia del registro, aquí **no** se autogenera un sufijo: un slug no disponible se rechaza
directamente (`SlugNoDisponible`, 400), porque es una elección explícita de quien ya tiene el
negocio. Un `horario_cierre` no posterior al `horario_apertura` se rechaza (`HorarioInvalido`,
400) antes de tocar la base de datos, además del `CheckConstraint` ya existente como defensa en
profundidad. La advertencia de que los enlaces compartidos dejan de funcionar al cambiar el slug
es responsabilidad del frontend (texto de ayuda junto al campo), no del backend.

## Endpoints de Invitar y Gestionar Staff (UC-04, RF-009, RF-010, implementados CAPDC-13)

| Endpoint | Función | Respuestas |
| --- | --- | --- |
| `GET /api/negocio/staff/` | Lista el staff del negocio del Dueño autenticado | 200; 401; 403 (no es Dueño) |
| `POST /api/negocio/staff/invitar/` | Invita un correo; genera un token de invitación firmado y lo "envía" (consola en desarrollo). Con `settings.DEBUG=True`, la respuesta incluye `{"token": "..."}` para que el frontend muestre el enlace completo en la UI (CAPDC-13, 2026-10-14); en producción, con correo real, el cuerpo va vacío — el token solo llega por el correo de verdad | 202; 400 (correo inválido); 401; 403; 409 (el correo ya tiene una cuenta) |
| `POST /api/negocio/staff/aceptar-invitacion/` | Pública: la persona invitada completa su registro (`token`, `nombre`, `password`) | 201 (cuenta Staff creada); 400 (token inválido/vencido, o contraseña fuera de política) |
| `POST /api/negocio/staff/{id}/activar/` | Reactiva una cuenta de staff desactivada | 200; 404 (no existe o es de otro tenant) |
| `POST /api/negocio/staff/{id}/desactivar/` | Desactiva una cuenta de staff sin eliminarla | 200; 404 |

Las cuatro primeras requieren `EsDuenoDeNegocio`; el listado y las acciones de activar/desactivar
filtran siempre por `request.user.tenant_id`, así que un Dueño nunca ve ni modifica staff de otro
tenant (RN-005) — ni siquiera adivinando un `id` ajeno (404, no 403, para no confirmar su
existencia).

**Modelo **`MiembroStaff` (`apps/tenant/models.py`, entidad interna del agregado Tenant, docs/02-2
§3.2): no hereda `TenantScopedModel` (que usa un `tenant_id` plano sin FK) porque el esquema
documentado exige una FK real con `ON DELETE CASCADE` (docs/02-3 §4.3); sigue el mismo patrón que
`Usuario.tenant` — un campo FK llamado `tenant`/`usuario` que genera automáticamente las columnas
`tenant_id`/`usuario_id`.

**Invitación sin tabla propia (RN-019):** el enlace de invitación es un token firmado con
`django.core.signing` (`salt` dedicado, vigencia 7 días vía `max_age`), sin persistirlo en base de
datos. El "uso único" se logra sin una tabla de invitaciones: una vez aceptada, el correo ya queda
registrado como cuenta, así que un segundo intento con el mismo token se rechaza por correo
duplicado (409) — el mismo mecanismo que ya existía para el registro de un Dueño.

**Puerto **`NotificationPort`** (**`apps/tenant/ports.py`**):** igual patrón que `VerificadorTenantPort`
(ADR-002). El Sprint 1 solo registra un adaptador de consola
(`apps/notification/adapters.py::AdaptadorConsola`, registrado en `TenantConfig.ready()`) que
imprime el "correo" en el log del servidor; el adaptador real (correo transaccional) llega en el
Sprint 4 con el módulo Notification. `apps.iam.services.registrar_staff` (variante de
`_crear_cuenta` con `rol=STAFF`) es el único camino para crear una cuenta Staff, usado por Tenant al
aceptar la invitación — nunca hay auto-registro para este rol (RN-019).

Al desactivar un miembro, se desactiva también su `Usuario.estado` (no solo `MiembroStaff.estado`),
reutilizando el mismo bloqueo de login que ya aplica RN-020 a un tenant desactivado — su historial
de reservas se conserva, nunca se elimina el registro (UC-04, A1).

## Endpoints de Autenticación (CAPDC-8, implementados)

| Endpoint | Función | Respuestas |
| --- | --- | --- |
| `POST /api/auth/registro/` | Auto-registro de un Dueño (`email`, `nombre`, `password`); ignora cualquier `rol` o `tenant_id` enviado | 201; 400 (formato o política de contraseña); 409 (correo ya registrado) |
| `POST /api/auth/login/` | Inicio de sesión; devuelve `access`, `refresh` y el usuario | 200; 401 (credenciales inválidas, mensaje genérico); 403 (cuenta no disponible); 429 (límite de intentos) |
| `POST /api/auth/refresh/` | Renueva el token de acceso; rota el refresco y anula el anterior (lista negra) | 200; 401 (refresco vencido o ya usado) |

Los tokens llevan los claims `user_id`, `rol` y `tenant_id` (nulo para un Dueño sin negocio). El `AUTH_USER_MODEL` es `iam.Usuario` y la contraseña se guarda con el hasher por defecto de Django. El código de estado de cada error lo define el atributo `http_status` de la excepción de dominio, que traduce `config/exception_handler.py`.

**Datos semilla iniciales (CAPDC-42):**  la task original incluye "Super Admin y datos semilla". Hoy solo el Super Admin es construible por comando: Tenant ya existe en código (CAPDC-10/CAPDC-11) pero Catalog todavía no (llega en el Sprint 2), así que no hay servicios/recursos que sembrar todavía. La carga de tenants de demostración (ej. un Salón de belleza y una Clínica, como en el mockup) queda pendiente para cuando exista el módulo Catalog, y se documentará en ese momento.

## Aislamiento Multi-tenant (RNF-006, US-002, implementado CAPDC-9)

| Aspecto | Decisión |
| --- | --- |
| Tenant activo | `apps/shared/tenant_context.py`: una `ContextVar` (`tenant_actual()`), fijada una sola vez por petición |
| Cómo se fija | `apps/shared/middleware.py::TenantMiddleware`, registrado en `MIDDLEWARE` (`config/settings/base.py`). Decodifica el JWT del encabezado `Authorization` y toma el claim `tenant_id` que el propio servidor emitió al hacer login (`apps.iam.services.autenticar`); nunca un valor enviado por el cliente en el cuerpo o la URL. Si el token falta o no es válido, deja el tenant vacío — el rechazo (401) lo sigue dando `JWTAuthentication` en la vista, no el middleware |
| Modelo base | `TenantScopedModel` (abstracto, en `apps/shared/models.py`) con `tenant_id` obligatorio (`UUIDField` sin `null=True`) y `objects = TenantScopedManager()` |
| Manager | `TenantScopedManager.get_queryset()` filtra siempre por `tenant_actual()`; sin tenant en el contexto, devuelve `.none()` — nunca "todos los tenants" por omisión. `.sin_filtro_de_tenant()` existe solo para comandos de administración (ej. CAPDC-42), no para servir peticiones de la API |
| `apps.iam.Usuario` | **No**  hereda de `TenantScopedModel`, a propósito: el login busca una cuenta por correo antes de saber a qué tenant pertenece (y un Dueño puede no tener tenant aún, RN-019); su manager (`UsuarioManager`) se mantiene global |
| Verificación | `backend/tests/test_shared_tenant_scope.py`: filtrado por tenant, consulta vacía sin tenant en el contexto, lectura/edición/borrado de un registro de otro tenant no tiene efecto, `tenant_id` es obligatorio a nivel de base de datos, y una prueba de integración que hace login real y confirma que el tenant visto por el middleware coincide con el del token |
| Row-Level Security de PostgreSQL | Mejora posterior; no se usa en el MVP para no agregar complejidad |

## Niveles de Acceso

| Funcionalidad | Nivel de acceso |
| --- | --- |
| Reservas | Público |
| Disponibilidad | Público |
| Gestión de catálogo | `DUENO_NEGOCIO` / `STAFF` |
| Gestión de agenda | `DUENO_NEGOCIO` / `STAFF` |
| Administración de tenants | `SUPER_ADMIN` |
| Endpoint conversacional (`assistant`) | Público, condicionado a `tenant.plan = PRO` (RN-015) |

## Consideraciones del Módulo Assistant

| Funcionalidad | Acceso |
| --- | --- |
| Conversación con asistente | Público, solo si `tenant.plan = PRO` (RN-015) |
| Configuración FAQ (`contexto_asistente`, RF-036) | `DUENO_NEGOCIO` |
| Asignación de calificación (`RF-034`) | `DUENO_NEGOCIO` |

### Nota de Diseño

El endpoint conversacional del módulo `assistant` mantiene el mismo nivel de acceso que los casos de uso UC-10 y UC-11. Conforme a RN-014, el asistente no requiere autenticación adicional y solicita únicamente los mismos datos mínimos necesarios para realizar una reserva. La configuración de FAQ y la asignación de calificaciones permanecen en los módulos `tenant` y `catalog` respectivamente; `assistant` consume dicha información únicamente en modo lectura. La verificación de `tenant.plan = PRO` (RN-015) se implementa como una clase de `permissions.py` en `apps/assistant/` (ej. `TenantTienePlanPro`), evaluada antes de procesar cualquier mensaje; no requiere tocar `apps/tenant/`.

# 6. Exceptions

## Jerarquía de Excepciones

| Elemento | Descripción |
| --- | --- |
| `DomainException` | Clase base definida en `apps/shared/domain.py` |
| Excepciones por módulo | Cada aplicación extiende `DomainException` con excepciones específicas (ej. `SolapamientoReservaException`) |

## Manejo Centralizado

| Componente | Responsabilidad |
| --- | --- |
| `config/settings/base.py` | Registro del `EXCEPTION_HANDLER` global |
| `config/exception_handler.py` | Traducción de excepciones de dominio a respuestas HTTP estandarizadas |
| Equivalente Java | `@RestControllerAdvice` |

## Caso Particular: `LlmNoDisponibleException`

| Aspecto | Descripción |
| --- | --- |
| Excepción | `LlmNoDisponibleException` |
| Requerimiento asociado | RNF-018 |
| Mensaje esperado | "El asistente no está disponible en este momento, intenta reservar desde la página del negocio" |
| Comportamiento | Nunca retorna un error 500 genérico |
| Alcance | Exclusivo de `apps/assistant/` |
| Impacto sobre Booking y Catalog | Ninguno |

### Nota de Diseño

`LlmNoDisponibleException` se gestiona exclusivamente dentro del módulo `assistant`. No puede propagarse hacia `booking` ni `catalog`, ya que estos módulos no dependen de `assistant`, respetando la regla de dependencia definida en `05-arquitectura-software.md`.

# 7. Validation — Dos Niveles

## Estrategia de Validación

| Nivel | Dónde vive | Mecanismo Django/DRF |
| --- | --- | --- |
| Validación de forma | `serializers.py` | Validadores de campo de DRF (`validators=[...]`, métodos `validate_<campo>`) |
| Validación de negocio | `domain.py` / `validators.py` | Servicios de dominio e invariantes de las dataclasses |

## Justificación

| Tipo de Validación | Motivo |
| --- | --- |
| Validación de forma | Es más económica y se ejecuta antes de interactuar con la base de datos |
| Validación de negocio | Requiere consultar el estado actual del sistema y aplicar reglas de dominio |

# 8. Configuración (`config/settings/`)

## Configuración Principal

| Archivo / Sección | Propósito |
| --- | --- |
| `INSTALLED_APPS` | Los 7 módulos (incluye `assistant`) más `rest_framework`, `rest_framework_simplejwt`, `corsheaders` y `django.contrib.postgres` |
| Credenciales del proveedor LLM | Variables de entorno (`LLM_API_KEY`, `LLM_PROVIDER`) leídas desde `apps/assistant/adapters.py` |
| `REST_FRAMEWORK` | Autenticación, permisos por defecto y manejo global de excepciones |
| `SIMPLE_JWT` | Configuración de tokens JWT |
| `DATABASES` | Configuración PostgreSQL según entorno (`dev.py` o `docker.py`) |
| `CORS_ALLOWED_ORIGINS` | Orígenes permitidos para el frontend Angular |
| `TIME_ZONE` | `UTC` |
| Configuración `django-import-linter` | Archivo `.importlinter` ubicado en la raíz del proyecto |

## REST Framework

| Configuración | Propósito |
| --- | --- |
| `DEFAULT_AUTHENTICATION_CLASSES` | JWT |
| `DEFAULT_PERMISSION_CLASSES` | Usuario autenticado por defecto, excepto endpoints públicos |
| `EXCEPTION_HANDLER` | Manejo centralizado de excepciones |

## Configuración de Base de Datos

| Entorno | Configuración |
| --- | --- |
| Desarrollo | `dev.py` |
| Docker | `docker.py` |
| Motor soportado | PostgreSQL |
| Motor no utilizado | SQLite |

## Variables de Entorno LLM

| Variable | Propósito |
| --- | --- |
| `LLM_API_KEY` | Credencial del proveedor LLM |
| `LLM_PROVIDER` | Proveedor configurado |

## Configuración Arquitectónica

| Elemento | Descripción |
| --- | --- |
| Archivo | `.importlinter` |
| Restricción 1 | `domain.py` no puede importar `django.db` |
| Restricción 2 | `domain.py` no puede importar `rest_framework` |
| Referencia | ADR-004 |

### Nota de Diseño

La configuración de base de datos apunta siempre a PostgreSQL, incluso en desarrollo. Esta decisión evita divergencias con el modelo físico definido en la Etapa 3, el cual depende de extensiones específicas como `pgcrypto` y `btree_gist`. La conversión horaria hacia `America/Santiago` (SUP-003) continúa realizándose en el frontend.

# 9. Cierre de la Actividad

## Objetivos Cumplidos

| Objetivo | Estado |
| --- | --- |
| ADR-004 formalizado | ✅ |
| Migración Spring → Django | ✅ |
| Árbol de proyecto definido | ✅ |
| Mapeo Clean Architecture | ✅ |
| Seguridad adaptada | ✅ |
| Excepciones adaptadas | ✅ |
| Configuración adaptada | ✅ |
| import-linter configurado | ✅ |
| App Assistant diseñada | ✅ |

## Entregables

| Entregable | Estado |
| --- | --- |
| `08-estructura-backend.md` | Completo |
| ADR-004 | Completo |
| Arquitectura Django/DRF | Completa |
| Diseño Assistant | Completo |

## Próximos Pasos

| Etapa | Actividad |
| --- | --- |
| Etapa 4 | Implementación Backend |
| Documento siguiente | `11-entorno-desarrollo.md` |
| Acción pendiente | Configurar variables del proveedor LLM |
| Acción pendiente | Crear `apps/assistant/` |

## Estado Final

| Campo | Valor |
| --- | --- |
| Etapa | 4 — Diseño Backend |
| Framework | Django REST Framework |
| Arquitectura | Monolito Modular |
| Base de Datos | PostgreSQL |
| Epic 7 | Incorporado |
| Estado | Documentación Completa |

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 2.1 | 2026-08-02 | Incorpora la app `assistant` (Epic 7) | Equipo del proyecto |
| 2.2 | 2026-09-23 | RN-015 (acceso al asistente por plan) y captura de leads de la landing (SUP-010) | Alberto Rincón |
| 2.3 | 2026-09-24 | Raíz del proyecto `backend/` (monorepo); políticas de autenticación y alta de cuentas; aislamiento multi-tenant; adaptador de consola de `NotificationPort` | Alberto Rincón |
| 2.4 | 2026-09-24 | Límite de intentos de inicio de sesión: 5 en 15 minutos, bloqueo de 15 minutos | Alberto Rincón |
| 2.5 | 2026-09-24 | Endpoints de autenticación implementados (registro, login, refresh), con sus códigos de respuesta y claims del token | Alberto Rincón |
| 2.6 | 2026-09-25 | Aislamiento multi-tenant implementado: `TenantMiddleware`, `tenant_context`, `TenantScopedModel`/`TenantScopedManager`, con pruebas unitarias e integración (CAPDC-9) | Alberto Rincón |
| 2.7 | 2026-09-25 | Comando `manage.py crear_super_admin` implementado e idempotente (CAPDC-42); datos semilla de negocios demo quedan explícitamente diferidos a cuando exista Catalog | Alberto Rincón |
| 2.8 | 2026-10-02 | Módulo Tenant creado (CAPDC-10 adelanta el modelo de CAPDC-11); `usuarios.tenant_id` pasa a FK real; endpoints de administración de tenants (UC-19); `VerificadorTenantPort` para RN-020 | Alberto Rincón |
| 2.9 | 2026-10-02 | Endpoint `POST /api/negocio/` para que el Dueño registre su negocio (UC-03, RF-007, CAPDC-11): generación de slug único (RN-016), rechazo si ya tiene negocio (RN-019), renovación de tokens tras el alta | Alberto Rincón |
| 2.10 | 2026-10-03 | Invitar y gestionar staff (UC-04, RF-009, RF-010, CAPDC-13): modelo `MiembroStaff`, token de invitación firmado sin tabla propia (RN-019), puerto `NotificationPort` con adaptador de consola, activar/desactivar bloquea el login del staff (UC-04, A1) | Alberto Rincón |
| 2.11 | 2026-10-07 | Editar datos del negocio (UC-05, RF-011, CAPDC-14): `RegistrarNegocioView` pasa a `MiNegocioView` (GET/POST/PATCH sobre `/api/negocio/`); dirección y horario obligatorios al editar; slug rechazado si no está disponible (sin sufijo automático, a diferencia del registro) | Alberto Rincón |
| 2.12 | 2026-10-14 | `POST /api/negocio/staff/invitar/` devuelve `{"token": "..."}` solo con `settings.DEBUG=True`, para que el frontend muestre el enlace de invitación en la UI en vez de leer los logs del servidor; en producción (correo real) el cuerpo va vacío | Alberto Rincón |
