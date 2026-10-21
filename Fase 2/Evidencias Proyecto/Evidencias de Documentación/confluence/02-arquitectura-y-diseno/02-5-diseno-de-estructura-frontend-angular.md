> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13959211) · versión 5 · última edición 2026-10-07

# Etapa 5 — Diseño Frontend

| Campo | Detalle |
| --- | --- |
| **Etapa** | 5 — Diseño Frontend |
| **Versión** | 2.3 — esqueleto implementado (CAPDC-41) y pantallas de registro e inicio de sesión (CAPDC-8), 2026-09-24; v2.2: reglas del slug y palabras reservadas |
| **Rol aplicado** | Arquitecto Frontend Angular |
| **Entrada** | `08-estructura-backend.md` (contratos de API por módulo) |
| **Estado** | Documento vivo |

## Decisiones resueltas

| Decisión | Resolución |
| --- | --- |
| Arquitectura de componentes | Standalone components (sin NgModules clásicos) |
| Manejo de estado | Signals en servicios inyectables (sin NgRx) |

## 1. Principios Rectores

1. **Alineación 1:1 con los módulos del backend.**  Cada área de `features/` corresponde a un bounded context del backend (Etapa 2), de modo que el mapeo "qué endpoint consume qué pantalla" sea directo.
2. **Separación Smart/Dumb components.**  Todo componente es o bien un contenedor (`pages/`, con estado e inyección de servicios) o bien presentacional (`components/`, recibe datos por `input()` y emite eventos por `output()`, sin conocer servicios ni backend). Esto sostiene la reutilización real de `shared/components`.
3. **Lazy loading por defecto.**  Ninguna feature se carga en el bundle inicial salvo lo estrictamente necesario para el layout activo. Justificación: RNF-010 (usabilidad/responsive) y que un Cliente Final que solo va a reservar no debería descargar el código del panel administrativo completo.
4. **Carpetas que explican responsabilidad, no tecnología.**  `core/`, `shared/` y `layouts/` no son "cajones técnicos"; cada uno resuelve una pregunta de diseño distinta (ver secciones 3 a 5).

## 2. Árbol de Carpetas Completo

```
src/app/
│
├── core/                              → Servicios singleton, guards, interceptors (una sola instancia en toda la app)
│   ├── guards/
│   │   ├── auth.guard.ts
│   │   ├── role.guard.ts
│   │   └── guest-only.guard.ts
│   ├── interceptors/
│   │   ├── auth.interceptor.ts
│   │   ├── error.interceptor.ts
│   │   └── loading.interceptor.ts
│   ├── services/
│   │   ├── auth.service.ts             → sesión, token, signal de usuario actual
│   │   └── notification-toast.service.ts
│   └── models/
│       └── usuario.model.ts            → tipos compartidos por toda la app (Rol, Usuario)
│
├── shared/                             → Componentes/pipes/directivas reutilizables, sin lógica de negocio
│   ├── components/
│   │   ├── button/
│   │   ├── modal/
│   │   ├── loading-spinner/
│   │   └── form-field/
│   ├── pipes/
│   │   └── fecha-local.pipe.ts         → conversión UTC → America/Santiago (SUP-003)
│   └── directives/
│
├── layouts/                            → Shells estructurales, uno por grupo de rutas
│   ├── public-layout/                  → Sin barra de navegación autenticada; usado por Cliente Final
│   ├── auth-layout/                    → Layout minimalista para login/registro
│   ├── admin-layout/                   → Sidebar + topbar; usado por Dueño de Negocio y Staff
│   └── super-admin-layout/             → Layout de plataforma, distinto visualmente del admin de tenant
│
├── features/                           → Áreas de funcionalidad, alineadas a los módulos del backend
│   ├── landing/                        → Página pública de marketing (hero, calculadora, captura de demo) — excepción: no mapea a un bounded context del backend, ver nota abajo
│   ├── auth/                           → mapea a IAM
│   ├── onboarding/                     → mapea a Tenant
│   ├── catalog-admin/                  → mapea a Catalog (vista de administración)
│   ├── booking-public/                 → mapea a Booking (flujo público de reserva)
│   ├── agenda/                         → mapea a Booking (vista interna de staff/dueño)
│   ├── dashboard/                      → mapea a Reporting
│   ├── super-admin/                    → mapea a IAM (gestión de tenants por Super Admin)
│   └── chat-assistant/                 → mapea a Assistant (Epic 7, nuevo — widget conversacional público)
│
└── app.routes.ts                       → Router raíz (ver Sección 7)
```

### Estructura interna repetida en cada carpeta de `features/`

```
features/booking-public/
├── pages/            → Componentes contenedor, uno por ruta (ej. SeleccionarServicioPage, ConfirmarReservaPage)
├── components/       → Presentacionales específicos de esta feature (ej. CalendarioDisponibilidadComponent)
├── services/         → Llamadas HTTP a los endpoints del módulo Booking del backend
├── models/           → Interfaces que replican los DTO de api/dto del backend (ej. CrearReservaRequest)
└── booking-public.routes.ts   → Definición de rutas lazy de esta feature
```

## 3. `core/` — ¿Qué responsabilidad resuelve?

**Pregunta que responde:**  "¿qué necesita existir una sola vez, en toda la aplicación, sin importar qué feature esté activa?"

| Subcarpeta | Responsabilidad |
| --- | --- |
| `guards/` | Lógica de autorización que se ejecuta antes de activar una ruta (Sección 8). |
| `interceptors/` | Lógica transversal sobre cada petición HTTP saliente/entrante (Sección 9). |
| `services/` | Servicios verdaderamente singleton. `AuthService` mantiene el signal del usuario autenticado y del token; existe una sola instancia para toda la app (se provee en `root`). |
| `models/` | Solo los tipos que múltiples features necesitan (ej. `Rol`). Un modelo usado por una sola feature vive en esa feature, no aquí; evitar que `core/models` se convierta en un cajón de sastre es una decisión deliberada. |

**Por qué no está aquí la lógica de negocio de reservas, catálogo, etc.:**  `core` es para lo genuinamente transversal a toda la aplicación. Si un servicio solo lo usa `booking-public`, vive en `features/booking-public/services`, no en `core`. Mantener esta disciplina evita que `core` termine absorbiendo toda la aplicación con el tiempo.

## 4. `shared/` — ¿Qué responsabilidad resuelve?

**Pregunta que responde:**  "¿qué componente visual se repite en más de una feature, sin conocer nada del dominio de negocio?"

| Subcarpeta | Responsabilidad |
| --- | --- |
| `components/` | Presentacionales puros: un `ButtonComponent` no sabe qué es una "reserva"; recibe `label`, `variant` y emite `click`. Si un componente necesita inyectar un servicio de negocio, no pertenece a `shared`. |
| `pipes/` | Transformaciones de presentación reutilizables, como `fecha-local.pipe.ts`, que resuelve la conversión de zona horaria (RNF y SUP-003) en un solo lugar en vez de repetirla en cada componente que muestra una fecha. |
| `directives/` | Comportamiento reutilizable de UI sin estado de negocio. |

**Regla de oro:**  si el componente necesitara cambiar porque cambia una regla de negocio (ej. "ahora los servicios grupales se muestran distinto"), no pertenece a `shared`; pertenece a la feature correspondiente.

## 5. `layouts/` — ¿Qué responsabilidad resuelve?

**Pregunta que responde:**  "¿qué estructura visual (navegación, cabecera, contenedor) envuelve a un grupo de rutas?"

Cada layout es un componente con un `<router-outlet>` propio, seleccionado por el router raíz según el grupo de rutas (ver diagrama `routing_layouts_angular`).

| Layout | Usado por | Elementos propios |
| --- | --- | --- |
| `public-layout` | Cliente Final (sin cuenta) | Header simple con nombre/logo del negocio, sin navegación administrativa |
| `auth-layout` | Cualquier usuario antes de autenticarse | Diseño centrado, sin sidebar |
| `admin-layout` | Dueño de Negocio, Staff | Sidebar con navegación a agenda/catálogo/dashboard, topbar con datos del tenant activo |
| `super-admin-layout` | Super Admin | Navegación distinta, sin referencias a un tenant específico (coherente con RN-010: el Super Admin no opera datos de un tenant) |

**Por qué** `layouts`**es una carpeta separada de** `features`**:**  un layout no tiene lógica de negocio ni pertenece a un solo módulo del backend; es una decisión puramente de estructura visual y navegación. Tratarlo como una "feature más" mezclaría dos preocupaciones distintas (organización de rutas vs. presentación de shell).

## 6. `features/` — Detalle por Área

### 6.1 Referencia detallada: `booking-public` (la feature más visitada del sistema)

| Carpeta | Contenido |
| --- | --- |
| `pages/` | `SeleccionarServicioPage` (UC-10), `ConfirmarReservaPage` (UC-11), `ReservaConfirmadaPage` (muestra código de confirmación), `CancelarReservaPage` (UC-15, resuelve por token de URL) |
| `components/` | `CalendarioDisponibilidadComponent` (presentacional, recibe los horarios ya calculados y emite la selección), `TarjetaServicioComponent` |
| `services/` | `DisponibilidadService`, `ReservaPublicaService`; consumen directamente los endpoints públicos definidos en `booking/api` del backend (Sección 5 de `08-estructura-backend.md`) |
| `models/` | Interfaces que replican `CrearReservaRequest` / `ReservaResponse` del backend. Se mantienen como una traducción 1:1 explícita (sin reutilizar tipos "genéricos") para detectar fácilmente cuando el contrato de API cambia |

### 6.2 Resumen de las demás features

| Feature | Páginas principales | Particularidad |
| --- | --- | --- |
| `landing` *(nuevo)* | Home comercial (hero, propuesta de valor, calculadora de pérdidas, formulario de solicitud de demo) | No usa ninguno de los 4 layouts existentes (`public-layout`, `auth-layout`, `admin-layout`, `super-admin-layout`) — layout propio, sin sidebar ni contexto de tenant; es la única feature sin bounded context 1:1 en el backend (consume un endpoint liviano de `apps/tenant/`, ver `08-estructura-backend.md`) |
| `auth` | Login, Registro | Usa `auth-layout`; sus formularios son los únicos que no requieren `authGuard` (usan `guestOnlyGuard`) |
| `onboarding` | Asistente de registro de negocio (wizard multi-paso) | Único flujo con navegación de wizard propia (stepper), no un router-outlet estándar |
| `catalog-admin` | Gestión de servicios, gestión de recursos, configuración de disponibilidad | Usa `admin-layout`; requiere rol `DUENO_NEGOCIO` |
| `agenda` | Vista diaria/semanal de citas, modificar/cancelar reserva (staff) | Usa `admin-layout`; requiere rol `DUENO_NEGOCIO` o `STAFF` |
| `dashboard` | Métricas del negocio, exportar reporte | Usa `admin-layout`; consulta el módulo `reporting` del backend (solo lectura) |
| `super-admin` | Listado de tenants, activar/desactivar | Usa `super-admin-layout`; requiere rol `SUPER_ADMIN` exclusivamente |
| `chat-assistant` *(nuevo)* | Widget de chat flotante (`ChatWidgetComponent`) + `ConversacionPage` si se abre a pantalla completa | Usa `public-layout` (embebido dentro de `booking-public`, no es una ruta independiente); consume el endpoint público de `apps/assistant` (Etapa 4, Sección 3.1); no requiere autenticación, igual que `booking-public`; el widget solo se renderiza si el tenant activo tiene `plan = PRO` (RN-015) — `booking-public` ya tiene ese dato cargado en el contexto del tenant público |

### 6.3 Detalle — `chat-assistant` (Epic 7, nuevo en v2.0)

```
features/chat-assistant/
├── components/
│   ├── chat-widget/            → Botón flotante + panel de conversación (presentacional + contenedor liviano)
│   ├── chat-mensaje/           → Presentacional: una burbuja de mensaje (cliente o asistente)
│   └── chat-typing-indicator/  → Presentacional: indicador de "escribiendo..."
├── services/
│   └── chat.service.ts         → Envía mensajes al endpoint de `apps/assistant`, mantiene el signal de historial de la conversación activa
├── models/
│   └── mensaje.model.ts        → Interfaz que replica el DTO de mensaje del backend
└── (sin archivo de rutas propio — se embebe como componente dentro de booking-public.routes.ts, no es una ruta lazy independiente)
```

**Por qué** `chat-assistant`**no es una ruta propia:**  a diferencia de las demás features, el widget de chat no es una pantalla que se navega; es un componente persistente superpuesto sobre `booking-public` (visible mientras el cliente navega el catálogo o consulta disponibilidad de forma tradicional). Es consistente con RF-031/RF-034: "sin salir del chat" tampoco implica salir de la página pública del negocio. Se importa como componente standalone directamente en el layout de `booking-public` y no se declara en `app.routes.ts`.

## 7. Routing y Lazy Loading

Vista general: ver diagrama `routing_layouts_angular`.

### Estructura de `app.routes.ts` (conceptual)

| Ruta | Layout | Protección | Carga |
| --- | --- | --- | --- |
| `/` *(nuevo, 2026-09-23)* | layout propio de `landing` | Ninguna (pública) | Lazy `landing.routes.ts` — home comercial, primer punto de contacto |
| `/:tenantSlug` | `public-layout` | Ninguna (pública) | Lazy `booking-public.routes.ts` (ruta de mayor tráfico esperado: el enlace que un negocio comparte con sus clientes) |
| `/auth` | `auth-layout` | `guestOnlyGuard` | Lazy `auth.routes.ts` |
| `/app` | `admin-layout` | `authGuard` + `roleGuard(['DUENO_NEGOCIO','STAFF'])` | Hijas lazy: `agenda`, `catalog-admin`, `dashboard`, `onboarding` (esta última solo accesible una vez, inmediatamente después del registro) |
| `/admin` | `super-admin-layout` | `roleGuard(['SUPER_ADMIN'])` | Lazy `super-admin.routes.ts` |

### Estrategia de precarga (preloading)

No se aplica `PreloadAllModules` de forma global: cargaría el panel administrativo completo incluso para un Cliente Final que solo va a reservar, contradiciendo RNF-010. En su lugar se aplica una **precarga selectiva**  únicamente sobre `booking-public` cuando el usuario navega desde `auth`/`onboarding`, ya que es la ruta con mayor probabilidad de ser la siguiente visitada por un Dueño de Negocio recién registrado que quiere previsualizar su página pública.

### Por qué slug de tenant (`/:tenantSlug`) y no un ID

Una URL pública memorable y compartible (ej. `expertia.cl/salon-maria`) es parte de la propuesta de valor frente a competidores. Un UUID en la URL pública sería una regresión de experiencia frente a lo que el benchmark mostró que valoran los negocios pequeños.

Como `/:tenantSlug` comparte el primer segmento de la URL con las rutas del sistema (`/auth`, `/app`, `/admin`), el backend rechaza como slug las palabras reservadas (`auth`, `app`, `admin`, `api`, `docs`, `login`) — ver RN-016. El slug se genera desde el nombre del negocio y el Dueño puede editarlo desde "Mi negocio", con una advertencia de que los enlaces ya compartidos dejarán de funcionar.

## 8. Guards

| Guard | Tipo | Responsabilidad |
| --- | --- | --- |
| `authGuard` | `CanActivateFn` | Verifica que exista un token JWT válido en `AuthService`; si no, redirige a `/auth/login` |
| `roleGuard(roles[])` | `CanActivateFn` (factory) | Verifica que el rol del usuario autenticado esté en la lista permitida para esa rama de rutas; si no, redirige a una página de "sin permiso" |
| `guestOnlyGuard` | `CanActivateFn` | Impide que un usuario ya autenticado vuelva a ver login/registro; lo redirige directamente a `/app` |

**Por qué funciones (** `CanActivateFn`**) y no clases:**  es el estilo idiomático de Angular standalone (sin NgModules), consistente con la decisión de standalone components: menos boilerplate y más fácil de testear de forma aislada.

## 9. Interceptors

El orden de ejecución importa y se declara explícitamente en la configuración de la app.

| Orden | Interceptor | Responsabilidad |
| --- | --- | --- |
| 1 | `authInterceptor` | Adjunta el header `Authorization: Bearer <token>` a cada petición saliente (excepto a los endpoints públicos de `booking-public`) |
| 2 | `loadingInterceptor` | Activa/desactiva un signal global de "cargando" mientras la petición está en curso, consumido por `shared/components/loading-spinner` |
| 3 | `errorInterceptor` | Captura errores HTTP, traduce los códigos que devuelve `GlobalExceptionHandler` del backend (Etapa 4, Sección 7) a mensajes legibles vía `notification-toast.service`, y redirige a `/auth/login` si el error es 401 |

**Por qué este orden y no otro:**  `authInterceptor` debe ejecutarse primero para que la petición ya salga autenticada; `errorInterceptor` debe ejecutarse último porque necesita ver el resultado final (incluyendo si `authInterceptor` causó un 401 por token expirado).

## 10. Manejo de Estado

Cada feature con estado compartido entre sus componentes internos expone un servicio con signals (ej. `AgendaStateService` en `features/agenda/services`, con un signal de "citas del día seleccionado").

- No existe un store global único.
- El estado vive en el servicio del feature que lo necesita.
- Se inyecta en `root` solo cuando debe sobrevivir a la navegación (ej. `AuthService` en `core`); en los demás casos tiene vida limitada al feature.

**Justificación:**  un store global (NgRx) centraliza estado que, en este MVP, no necesita coordinarse entre features distintas (la agenda no necesita saber del estado del dashboard). Introducir NgRx sería infraestructura sin beneficio inmediato, el mismo argumento que ADR-002 aplicó al backend.

## 11. Cierre de esta actividad

### Objetivos cumplidos

- Árbol completo de carpetas: `core`, `shared`, `layouts`, `features` (8 áreas alineadas al backend, incluyendo `chat-assistant`).
- Responsabilidad de cada carpeta explicada con criterio de decisión, no solo descripción.
- Routing raíz y estrategia de lazy loading definidos, con justificación de la precarga selectiva.
- 3 guards y 3 interceptors definidos, con orden de ejecución justificado.
- Decisión de manejo de estado resuelta (signals por feature, sin NgRx).
- **Nuevo en v2.0:**  feature `chat-assistant` estructurada como componente embebido (no ruta independiente), consistente con RF-031/RF-034 y con el endpoint público de `apps/assistant`.
- 2 diagramas visuales (regla de dependencia Clean Architecture del backend + estructura de routing/layouts del frontend).

### Entregables

- `09-estructura-frontend.md` (v2.0)
- Diagrama `routing_layouts_angular`

### Próximos pasos

1. Propagar el chatbot hacia `10-setup-github.md` (label/sprint).
2. Propagar el chatbot hacia `11-entorno-desarrollo.md` (variable de entorno del proveedor de LLM).
3. Abrir formalmente la Etapa 6 — Infraestructura AWS.

*Documento vivo — Etapa 5 (Diseño Frontend). Documentación lista para el capítulo "Diseño del Frontend" de la memoria.*

## 12. Implementación inicial (CAPDC-41 y CAPDC-8, 2026-09-24)

**Implementado y verificado** (28 pruebas unitarias con Chrome headless, build de producción sin errores):

| Carpeta | Contenido |
| --- | --- |
| `core/models` | `Usuario`, `Rol`, `Sesion`, `RegistroRequest` |
| `core/services` | `AuthService` (sesión con signals: `usuario`, `token`, `estaAutenticado`), `NotificationToastService`, `LoadingService` |
| `core/guards` | `authGuard`, `guestOnlyGuard`, `roleGuard(roles)` |
| `core/interceptors` | `authInterceptor`, `loadingInterceptor`, `errorInterceptor` (en ese orden) |
| `core/utils` | `mensajeDeError`: traduce los errores de la API a mensajes para el usuario |
| `shared/components` | `form-field`, `loading-spinner` (barra de progreso), `toast-container` |
| `layouts` | `auth-layout`, `admin-layout` |
| `features/auth` | `LoginPage` y `RegistroPage` (rutas lazy `/auth/login` y `/auth/registro`) |
| `features/inicio` | Pantalla de bienvenida de `/app`; avisa al Dueño que aún no registró su negocio |
| `features/sin-permiso` | Destino de `roleGuard` cuando el rol no tiene acceso |

**Pendiente:** `public-layout` y `super-admin-layout` (llegan con sus historias), la feature `landing` y el resto de las features de la sección 2, y el componente `modal`.

**Decisiones de implementación:**

- **Proxy de desarrollo:** el servidor de Angular reenvía `/api` al backend (`frontend/proxy.conf.json`, destino `http://backend:8000` dentro de Docker). El navegador llama siempre a rutas relativas (`/api/...`): no depende del puerto del backend en cada equipo ni necesita CORS.
- **Botones y estilos base:** se resuelven con clases globales (`.btn`, `.btn-primary`) en `styles.scss`, en lugar de un componente `button`; el componente se agregará si aparece lógica propia.
- **Sesión:** los tokens se guardan en `localStorage` (riesgo de XSS aceptado en el MVP; el token de acceso dura 30 minutos, RN-018). Todavía no se renueva automáticamente con el token de refresco: ante un 401 en una ruta protegida se cierra la sesión y se envía al login. La renovación se agrega cuando existan endpoints protegidos que la necesiten.
- **Flujo de registro:** tras registrarse, la app inicia sesión automáticamente con las mismas credenciales y navega a `/app`.
- **Rutas:** `/` redirige a `/auth/login` hasta que exista la landing; `roleGuard` envía a `/sin-permiso` (el Super Admin también llega ahí hasta que exista `/admin`, US-003).
- **Pruebas:** `docker compose --profile test run --rm frontend-test` (servicio con Chromium headless, sin instalar nada en el equipo).

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 2.0 | 2026-08-02 | Agrega la feature `chat-assistant` (Epic 7) | Equipo del proyecto |
| 2.1 | 2026-09-23 | Feature `landing` y ruta pública `/` | Alberto Rincón |
| 2.2 | 2026-09-24 | Reglas del slug y palabras reservadas (RN-016); ejemplo de URL con el dominio `expertia.cl` | Alberto Rincón |
| 2.3 | 2026-09-24 | Nueva §12: esqueleto Angular implementado (`core`, `shared`, `layouts`), pantallas de registro e inicio de sesión, proxy de desarrollo, decisiones de sesión y pruebas | Alberto Rincón |
