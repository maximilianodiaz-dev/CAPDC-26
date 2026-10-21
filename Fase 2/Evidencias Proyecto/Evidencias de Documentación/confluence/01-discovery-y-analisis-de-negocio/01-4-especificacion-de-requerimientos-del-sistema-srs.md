> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13828119) · versión 8 · última edición 2026-10-14

## Plataforma SaaS de Administración de Reservas y Citas

| Campo | Detalle |
| --- | --- |
| **Etapa** | 1 — Discovery & Análisis de Negocio (cierre formal) |
| **Versión** | 2.8 — RES-009: el profesor guía confirma que no se requiere despliegue en AWS, basta un video de la demo (2026-10-14); v2.7: SUP-010 corrige clave de US-029 |
| **Estado** | Para revisión y aprobación del equipo |
| **Última actualización** | 2026-10-07 |
| **Archivo fuente** | `03-especificacion-requerimientos.md` |

## 1. Introducción

### 1.1 Propósito

Este documento especifica de manera formal los requerimientos funcionales, no funcionales, restricciones, supuestos, reglas de negocio y dependencias del sistema, como base de diseño para las Etapas 2 a 9 del proyecto (Arquitectura, Modelo de Datos, Backend, Frontend, Infraestructura, CI/CD, QA e Implementación).

### 1.2 Alcance

El sistema es una plataforma SaaS multi-tenant de administración de reservas y citas para negocios de servicios con agenda (rubro genérico, validado en dos verticales piloto: salón de belleza/spa y clínica/consultorio profesional), con un **asistente conversacional (chatbot)**  como canal adicional de agendamiento.

Este documento cubre exclusivamente el alcance del **MVP** , tal como fue acotado en el Product Backlog v2.0 (`02-product-backlog.md`), el cual incorpora el Epic 7 — Asistente Conversacional como parte del alcance Must-have a defender.

### 1.3 Documentos de referencia

- `00-project-charter.md` — Alcance general y restricciones del proyecto
- `01-benchmark-competitivo.md` — Análisis competitivo y propuesta de valor
- `02-product-backlog.md` — Épicas, historias de usuario y priorización

### 1.4 Convención de numeración

| Prefijo | Significado |
| --- | --- |
| RF-XXX | Requerimiento Funcional |
| RNF-XXX | Requerimiento No Funcional |
| RES-XXX | Restricción |
| SUP-XXX | Supuesto |
| RN-XXX | Regla de Negocio |
| DEP-XXX | Dependencia |

## 2. Descripción General del Sistema

### 2.1 Actores

| Actor | Descripción |
| --- | --- |
| Super Admin | Administra la plataforma a nivel global (tenants, no datos operativos) |
| Dueño de Negocio | Administrador del tenant; configura servicios, recursos y staff |
| Staff / Profesional | Gestiona su propia agenda de citas |
| Cliente Final | Reserva servicios a través de la página pública del negocio |

### 2.2 Perspectiva del Producto

Monolito modular, multi-tenant, con frontend Angular desacoplado del backend Django REST Framework vía API REST, persistencia en PostgreSQL, contenerizado con Docker y desplegado en AWS mediante GitHub Actions.

## 3. Requerimientos Funcionales (RF)

### 3.1 Módulo — Autenticación y Multi-tenancy

| ID | Requerimiento | Historia relacionada |
| --- | --- | --- |
| RF-001 | El sistema debe permitir el registro de un nuevo usuario con email y contraseña. | US-001 |
| RF-002 | El sistema debe permitir el inicio de sesión mediante email y contraseña, retornando un token de sesión. | US-001 |
| RF-003 | El sistema debe asignar a cada usuario uno de los roles definidos (Super Admin, Dueño de Negocio, Staff, Cliente Final). | US-001 |
| RF-004 | El sistema debe restringir el acceso a los datos de un tenant exclusivamente a los usuarios asociados a ese tenant. | US-002 |
| RF-005 | El sistema debe permitir al Super Admin listar y visualizar el estado de todos los tenants registrados. | US-003 |
| RF-006 | El sistema debe permitir al Super Admin activar/desactivar un tenant. | US-003 |

### 3.2 Módulo — Onboarding y Gestión de Tenant

| ID | Requerimiento | Historia relacionada |
| --- | --- | --- |
| RF-007 | El sistema debe permitir registrar un negocio (tenant) con nombre, rubro, datos de contacto (correo y teléfono) y un identificador público (slug) para su página de reservas. | US-004 |
| RF-008 | El sistema debe preconfigurar servicios y recursos sugeridos según el rubro seleccionado, mediante un asistente de configuración inicial. | US-005 |
| RF-009 | El sistema debe permitir invitar cuentas de staff mediante correo electrónico. | US-006 |
| RF-010 | El sistema debe permitir activar/desactivar cuentas de staff dentro de un tenant. | US-006 |
| RF-011 | El sistema debe permitir editar los datos generales del negocio (nombre, dirección, horario general). | US-007 |

### 3.3 Módulo — Catálogo de Servicios y Recursos

| ID | Requerimiento | Historia relacionada |
| --- | --- | --- |
| RF-012 | El sistema debe permitir crear, editar y eliminar servicios (nombre, duración, precio, descripción). | US-008 |
| RF-013 | El sistema debe permitir crear, editar y eliminar recursos, tipificados como profesional, sala o equipo. | US-009 |
| RF-014 | El sistema debe permitir asociar uno o más recursos a un servicio. | US-009 |
| RF-015 | El sistema debe permitir configurar disponibilidad horaria semanal recurrente por recurso. | US-010 |
| RF-016 | El sistema debe permitir configurar excepciones de disponibilidad (bloqueos puntuales, ausencias, feriados). | US-010 |
| RF-017 | El sistema debe permitir definir servicios grupales con un cupo máximo de participantes. | US-011 |

### 3.4 Módulo — Motor de Reservas

| ID | Requerimiento | Historia relacionada |
| --- | --- | --- |
| RF-018 | El sistema debe permitir consultar los horarios disponibles de un servicio dentro de un rango de fechas. | US-012 |
| RF-019 | El sistema debe permitir crear una reserva seleccionando servicio, recurso y horario disponible. | US-012 |
| RF-020 | El sistema debe impedir la creación de una reserva que se solape en el tiempo con otra reserva del mismo recurso. | US-012 |
| RF-021 | El sistema debe generar un identificador único de confirmación al crear una reserva. | US-013 |
| RF-022 | El sistema debe permitir listar las reservas de un staff o negocio, filtradas por día o semana. | US-014 |
| RF-023 | El sistema debe permitir modificar una reserva existente (cambio de horario o recurso). | US-015 |
| RF-024 | El sistema debe permitir cancelar una reserva, tanto por el staff/negocio como por el cliente final. | US-015 |
| RF-025 | El sistema debe permitir al cliente final cancelar su propia reserva mediante un enlace único enviado por correo. | US-016 |

### 3.5 Módulo — Notificaciones

| ID | Requerimiento | Historia relacionada |
| --- | --- | --- |
| RF-026 | El sistema debe enviar un correo de confirmación al cliente final al crear una reserva. | US-017 |
| RF-027 | El sistema debe enviar un correo recordatorio al cliente final 24 horas antes de la cita. | US-018 |
| RF-028 | El sistema debe notificar por correo al negocio cuando se crea una nueva reserva. | US-019 |

### 3.6 Módulo — Panel de Administración

| ID | Requerimiento | Historia relacionada |
| --- | --- | --- |
| RF-029 | El sistema debe mostrar un dashboard con el número de citas del día/semana y la tasa de ocupación de recursos. | US-020 |
| RF-030 | El sistema debe permitir exportar un reporte de citas del mes en formato CSV o PDF. | US-021 |

### 3.7 Módulo — Asistente Conversacional (nuevo)

| ID | Requerimiento | Historia relacionada |
| --- | --- | --- |
| RF-031 | El sistema debe permitir al cliente final consultar disponibilidad de un servicio mediante una conversación en lenguaje natural. | US-022 |
| RF-032 | El asistente debe identificar, entre los recursos disponibles para un servicio y horario solicitados, cuáles tienen calificación asignada. | US-023 |
| RF-033 | El asistente debe recomendar como primera opción el recurso disponible con mayor calificación, cuando exista más de uno disponible. | US-023 |
| RF-034 | El sistema debe permitir al Dueño de Negocio asignar manualmente una calificación numérica (escala 1.0–5.0) a cada recurso de tipo profesional. | US-024 |
| RF-035 | El asistente debe permitir completar el flujo completo de creación de una reserva (selección de servicio, recurso/horario, datos del cliente y confirmación) dentro de la misma conversación. | US-025 |
| RF-036 | El sistema debe permitir al Dueño de Negocio configurar contenido de preguntas frecuentes (horario, ubicación, políticas) que el asistente usará como fuente de respuesta. | US-026 |
| RF-037 | El asistente debe responder consultas del cliente final sobre información configurada del negocio, y debe indicar explícitamente cuando no dispone de la información solicitada. | US-027 |

## 4. Requerimientos No Funcionales (RNF)

| ID | Categoría | Requerimiento |
| --- | --- | --- |
| RNF-001 | Rendimiento | La consulta de disponibilidad de horarios debe responder en menos de 2 segundos (percentil 95) bajo carga normal. |
| RNF-002 | Rendimiento | La creación de una reserva debe completarse de extremo a extremo en menos de 3 segundos. |
| RNF-003 | Seguridad | Las contraseñas deben almacenarse mediante hashing (bcrypt o equivalente), nunca en texto plano. |
| RNF-004 | Seguridad | Toda comunicación cliente-servidor debe realizarse sobre HTTPS/TLS. |
| RNF-005 | Seguridad | El sistema debe implementar control de acceso basado en roles (RBAC) a nivel de API. |
| RNF-006 | Seguridad | Los datos de cada tenant deben estar lógicamente aislados (aislamiento a nivel de fila mediante identificador de tenant) para prevenir fuga de datos entre negocios. |
| RNF-007 | Disponibilidad | El sistema debe apuntar a una disponibilidad objetivo de 99% durante el período de evaluación académica. |
| RNF-008 | Escalabilidad | La arquitectura debe organizarse en módulos con límites de dominio claros (bounded contexts), que permitan una futura extracción a microservicios sin reescritura completa. |
| RNF-009 | Usabilidad | El flujo de reserva del cliente final debe poder completarse en un máximo de 4 pantallas o pasos. |
| RNF-010 | Usabilidad | La interfaz debe ser responsive (escritorio, tablet, móvil), dado que no se construirá una app nativa. |
| RNF-011 | Mantenibilidad | El backend debe estructurarse en módulos por dominio de negocio, no por capa técnica transversal. |
| RNF-012 | Mantenibilidad | El proyecto debe mantener una cobertura de pruebas automatizadas mínima. Definido formalmente en la Etapa 8 — Estrategia de Calidad (`03-3`, CAPDC-40): 80% de líneas en el backend, 80%/80%/75%/60% (statements/lines/functions/branches) en el frontend, aplicado como umbral obligatorio en el pipeline de CI. |
| RNF-013 | Portabilidad | El sistema completo (backend, frontend, base de datos) debe poder desplegarse mediante contenedores Docker. |
| RNF-014 | Despliegue | El pipeline de CI/CD debe ejecutar automáticamente build, pruebas y despliegue ante cada integración a la rama principal. Mientras el despliegue en AWS esté diferido (RES-009), el pipeline ejecuta build, pruebas, lint y reglas de arquitectura, sin etapa de despliegue. |
| RNF-015 | Observabilidad | El sistema debe registrar logs estructurados de operaciones críticas (creación/cancelación de reservas, fallos de autenticación). |
| RNF-016 | Cumplimiento | El sistema debe manejar datos personales de clientes conforme a principios básicos de protección de datos (minimización, acceso restringido), en línea con la Ley N.º 19.628 de Chile sobre protección de la vida privada. |
| RNF-017 | Rendimiento | El asistente conversacional debe responder en menos de 5 segundos (percentil 95) por turno de conversación. |
| RNF-018 | Disponibilidad | Si el proveedor de LLM externo no está disponible, el sistema debe degradar de forma controlada (mensaje de error claro al usuario) sin afectar el flujo de reserva tradicional vía web. |
| RNF-019 | Cumplimiento | El historial de conversaciones del asistente se considera dato personal del cliente y debe recibir las mismas protecciones descritas en RNF-016. |

## 5. Restricciones (RES)

| ID | Restricción |
| --- | --- |
| RES-001 | El stack tecnológico es fijo: Angular, Django REST Framework, PostgreSQL, Docker, GitHub, AWS y GitHub Actions. No se evaluarán alternativas tecnológicas. Redacción original: Spring Boot, reemplazado por Django REST Framework mediante ADR-004 (`08-estructura-backend.md` §0). |
| RES-002 | La arquitectura debe implementarse como Monolito Modular, no como microservicios desde el inicio. |
| RES-003 | El proyecto debe completarse entre el 10 de agosto y el 21 de noviembre de 2026 (~15 semanas). |
| RES-004 | El equipo de desarrollo está compuesto por 3 integrantes. |
| RES-005 | El presupuesto de infraestructura AWS está limitado a la capa gratuita (Free Tier) o a un presupuesto académico mínimo. |
| RES-006 | Excepción explícita a la restricción de "sin presupuesto para servicios de pago de terceros", exclusivamente para el proveedor de LLM del asistente conversacional (Epic 7), dado su rol central en el valor diferenciador del MVP. El proveedor seleccionado es **Google Gemini**  (API con soporte de tool/function calling, cumple SUP-008), con un presupuesto de referencia de ~10 USD/mes **financiado personalmente por Alberto Rincón**  (integrante del equipo, Backend), no por una partida institucional o de equipo — se deja explícito por transparencia en la memoria. La restricción original se mantiene vigente para pasarelas de pago, WhatsApp Business API y SMS. |
| RES-007 | El idioma de la interfaz para el MVP es exclusivamente español. |
| RES-008 | El sistema no contempla el desarrollo de una aplicación móvil nativa. |
| RES-009 | La infraestructura y el despliegue en AWS quedan **fuera del alcance del proyecto**  (ya no "diferidos a confirmar", sino descartados): el sistema se desarrolla y demuestra en contenedores locales (RNF-013), y la entrega final se acompaña de un **video de la demo**  en vez de un despliegue real. **Confirmado por el profesor guía (2026-10-14)**, reemplazando la nota anterior de "pendiente de confirmación" (decisión original 2026-09-24). |

**Redacción original de RES-006 (histórica, ya no vigente para el proveedor de LLM):**  "No se dispone de presupuesto para servicios de pago de terceros (pasarelas de pago, WhatsApp Business API, SMS)."

## 6. Supuestos (SUP)

| ID | Supuesto |
| --- | --- |
| SUP-001 | Los negocios que usarán la plataforma ya tienen definido su catálogo de servicios y precios al momento de registrarse. |
| SUP-002 | Todos los usuarios acceden mediante un navegador web moderno (Chrome, Firefox, Edge, Safari actualizados). |
| SUP-003 | La zona horaria de operación del MVP es única: America/Santiago. |
| SUP-004 | Los pagos de los servicios reservados se gestionan fuera de la plataforma (efectivo, transferencia, POS físico del negocio) durante el MVP. |
| SUP-005 | El volumen de datos y usuarios concurrentes durante la evaluación del proyecto de título corresponde a un entorno académico, no productivo real. |
| SUP-006 | Existirá disponible y verificado un servicio de correo transaccional (AWS SES) para el envío de notificaciones. **Aclaración (2026-10-14):** solo requiere credenciales de API de SES, no el despliegue completo de la aplicación en AWS (RES-009/DEP-006, que sigue diferido) — el backend puede llamar a SES desde cualquier entorno, incluido Docker local, así que no depende de que se retome la infraestructura AWS. |
| SUP-007 | Los dos verticales piloto (salón de belleza/spa y clínica/consultorio) son representativos suficientes para validar la genericidad del modelo de datos. |
| SUP-008 | El proveedor de LLM seleccionado debe soportar invocación estructurada de herramientas/funciones (tool/function calling), condición necesaria para que el asistente solo pueda invocar Application Services existentes (ver RN-013). Cumplido por Google Gemini (RES-006). |
| SUP-009 | El presupuesto de LLM aprobado (RES-006, ~10 USD/mes) es suficiente para el volumen de conversaciones esperado durante la evaluación académica del proyecto, consistente con el supuesto de entorno no productivo (SUP-005), usando el modelo Gemini Flash. Se recomienda un tope simple de mensajes por tenant/día como salvaguarda de presupuesto, a definir en Etapa 4. |
| SUP-010 | La landing pública y el formulario de solicitud de demo (captura de leads comerciales) son una funcionalidad de marketing fuera del árbol de Épicas del Product Backlog; no generan una entidad de dominio nueva ni un módulo propio — se documentan directamente en `08-estructura-backend.md`/`09-estructura-frontend.md` y reutilizan `NotificationPort` para notificar la solicitud. Historia asignada: US-029 / CAPDC-49 (`01-3` §7.1), Sprint 2, 5 SP. |
| SUP-011 | La recuperación de contraseña y las cuentas de Cliente Final quedan fuera del MVP: el cliente reserva sin cuenta y el rol `CLIENTE_FINAL` existe en el modelo sin flujo de registro (decisión 2026-09-24). |

## 7. Reglas de Negocio (RN)

| ID | Regla |
| --- | --- |
| RN-001 | Una reserva no puede crearse si el recurso solicitado no tiene disponibilidad configurada en el horario solicitado. |
| RN-002 | Dos reservas no pueden solaparse en el tiempo para un mismo recurso (exclusión mutua). |
| RN-003 | La duración de una reserva queda determinada por la duración configurada del servicio asociado. |
| RN-004 | Un recurso pertenece exclusivamente a un tenant; no puede compartirse entre negocios distintos. |
| RN-005 | Un usuario Staff solo puede gestionar reservas, servicios y recursos del tenant al que pertenece. |
| RN-006 | Un servicio grupal no puede aceptar más reservas que su cupo máximo configurado. |
| RN-007 | Al registrarse, un tenant debe seleccionar un rubro (vertical), lo que determina la plantilla de servicios/recursos sugerida por el asistente de configuración. |
| RN-008 | Una reserva cancelada libera automáticamente el bloque de tiempo del recurso asociado. |
| RN-009 | Un cliente final solo puede cancelar su propia reserva mediante el enlace único enviado en su correo de confirmación. |
| RN-010 | El Super Admin no puede acceder a los datos operativos (reservas, clientes) de un tenant, solo a metadatos administrativos (estado, fecha de alta, plan). |
| RN-011 | La calificación de un recurso (profesional) es asignada manualmente por el Dueño de Negocio, en escala 1.0–5.0, y es opcional; un recurso sin calificación no se pondera en las recomendaciones del asistente. |
| RN-012 | Al existir más de un recurso disponible para un servicio y horario, el asistente debe recomendar primero el de mayor calificación. |
| RN-013 | El asistente conversacional solo puede invocar Application Services ya existentes de los módulos Catalog y Booking; no puede acceder directamente a repositorios ni a la base de datos. |
| RN-014 | Antes de confirmar una reserva, el asistente debe recolectar exactamente los mismos datos mínimos requeridos que el flujo web (RF-019), sin excepciones por canal. |
| RN-015 | El acceso al asistente conversacional (widget de chat y su endpoint) solo está disponible para tenants en plan **PRO** ; un tenant en plan **BÁSICO**  no expone el canal conversacional (ver `tenants.plan` en `07-modelo-base-datos.md`). Regla motivada por el control de costo del proveedor de LLM (RES-006), no por una restricción de producto arbitraria. |
| RN-016 | El identificador público (slug) de un tenant es único en toda la plataforma, se genera a partir del nombre del negocio (minúsculas, sin tildes, separado por guiones; si ya existe o es una palabra reservada se agrega un sufijo numérico, ej. `admin-2`), tiene entre 3 y 50 caracteres `a-z 0-9 -` y no puede ser una palabra reservada de las rutas del sistema (`auth`, `app`, `admin`, `api`, `docs`, `login`); al editarlo manualmente, un slug reservado se rechaza. El Dueño de Negocio puede editarlo, con una advertencia de que los enlaces ya compartidos dejarán de funcionar. |
| RN-017 | Un recurso de tipo profesional puede estar vinculado a una cuenta de usuario (`recursos.usuario_id`), y una cuenta se vincula a lo más a un recurso. El vínculo aplica tanto a Staff como a un Dueño de Negocio que también atiende. Los recursos de tipo sala o equipo no tienen cuenta. La agenda de un Staff muestra las reservas que incluyen el recurso vinculado a su cuenta. |
| RN-018 | Política de acceso: contraseña de al menos 10 caracteres, no común ni solo numérica; token de acceso de 30 minutos y token de refresco de 7 días con rotación; límite de intentos de inicio de sesión para frenar fuerza bruta: tras 5 intentos fallidos en 15 minutos, se rechazan nuevos intentos durante 15 minutos. |
| RN-019 | Alta de cuentas por rol: el auto-registro crea únicamente Dueños de Negocio; el Staff ingresa solo por invitación (enlace con token firmado, de un solo uso, que vence a los 7 días); el Super Admin se crea mediante un comando de administración; el Cliente Final no tiene cuenta en el MVP (SUP-011). Un Dueño puede existir sin negocio (sin tenant) hasta completar el registro del negocio (UC-03), y cada Dueño registra un solo negocio. |
| RN-020 | Desactivar un tenant bloquea el inicio de sesión de todos sus usuarios ("cuenta no disponible") y su página pública deja de estar disponible; activar el tenant revierte el efecto. Los cambios de estado de un tenant se registran en el log estructurado (RNF-015). El Super Admin solo lista y gestiona el estado de los tenants (RF-005, RF-006); no existe un historial de auditoría adicional en el MVP. |

## 8. Dependencias (DEP)

### 8.1 Dependencias internas (entre requerimientos)

| ID | Dependencia |
| --- | --- |
| DEP-001 | RF-019 (crear reserva) depende de RF-015 (disponibilidad configurada) y RF-014 (recurso asociado a servicio). |
| DEP-002 | RF-025 (cancelación por cliente) depende de RF-026 (email de confirmación con enlace único). |
| DEP-003 | RF-008 (asistente de onboarding) depende de RF-007 (registro de negocio). |
| DEP-004 | RNF-006 (aislamiento multi-tenant) es prerrequisito de todos los RF que acceden a datos de negocio (RF-007 en adelante). |

### 8.2 Dependencias externas (servicios de terceros/infraestructura)

| ID | Dependencia |
| --- | --- |
| DEP-005 | El envío de correos (RF-026, RF-027, RF-028) depende de un proveedor externo de correo transaccional (AWS SES). Independiente de DEP-006: no requiere que la app esté desplegada en AWS, solo credenciales de API. |
| DEP-006 | El despliegue en producción depende de la disponibilidad de servicios AWS (a definir en detalle en Etapa 6 — Infraestructura). Diferida según RES-009. |
| DEP-007 | El pipeline de CI/CD depende de GitHub Actions y de GitHub como repositorio remoto. |
| DEP-008 | La autenticación segura depende de un estándar/librería de tokens (JWT u equivalente), a definir en Etapa 4 — Diseño Backend. |
| DEP-009 | El módulo Asistente Conversacional depende de un proveedor externo de LLM con soporte de invocación de herramientas (tool calling). Proveedor definido el 2026-09-23: **Google Gemini**  (modelo recomendado: variante Flash, por costo), ver RES-006. |

## 9. Trazabilidad Backlog → Requerimientos

Cada historia de usuario del Product Backlog (`02-product-backlog.md`) queda cubierta por uno o más requerimientos funcionales de este documento (ver columna "Historia relacionada" en la sección 3). No existen historias del backlog sin requerimiento asociado, ni requerimientos sin historia de origen. Esta doble verificación es intencional para sostener la trazabilidad exigida en un documento de ingeniería de memoria de título.

## 10. Cierre de esta actividad

### Objetivos cumplidos

- 37 Requerimientos Funcionales numerados y trazados a historias de usuario (incorpora RF-031 a RF-037 del Asistente Conversacional).
- 19 Requerimientos No Funcionales categorizados.
- 9 Restricciones del proyecto formalizadas (RES-006 actualizada con excepción aprobada para LLM; RES-009: AWS diferido).
- 11 Supuestos explícitos documentados (incorpora SUP-010, landing/captura de demo, y SUP-011, recuperación de contraseña y Cliente Final sin cuenta).
- 20 Reglas de Negocio numeradas (incorpora RN-015, acceso al asistente condicionado al plan PRO, y RN-016 a RN-020: slug, vínculo usuario-recurso, política de acceso, alta de cuentas por rol y efecto de desactivar un tenant).
- 9 Dependencias (internas y externas) identificadas.
- Matriz de trazabilidad Backlog ↔ Requerimientos.

### Entregables

- `03-especificacion-requerimientos.md` (v2.0)

### Documentación generada

Lista para el capítulo de "Especificación de Requerimientos" (SRS) de la memoria de título.

### Próximos pasos

Con Requerimientos y Reglas de Negocio formalizados, la Etapa 1 queda completamente cerrada. Corresponde abrir la **Etapa 2 — Arquitectura de Software** , donde:

1. Se definirán los *bounded contexts*  del monolito modular a partir de los módulos de este documento.
2. Se redactará el **ADR-001**  (decisión de alcance multi-rubro + genérico).
3. Se generará el diagrama de arquitectura en notación C4 (Contexto y Contenedores).

*Documento vivo — Etapa 1 (Discovery & Análisis de Negocio), cierre formal.*

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 2.0 | 2026-08-02 | Agrega módulo Asistente Conversacional (Epic 7) | Equipo del proyecto |
| 2.1 | 2026-09-23 | Proveedor Google Gemini (RES-006, DEP-009, SUP-008/009); SUP-010 (landing) y RN-015 (plan PRO) | Alberto Rincón |
| 2.2 | 2026-09-24 | RES-001 con Django REST Framework (ADR-004); RES-009 (AWS diferido) y ajuste de RNF-014/DEP-006; SUP-011; RN-016 a RN-019; RF-007 incluye slug | Alberto Rincón |
| 2.3 | 2026-09-24 | RN-020 (efecto de desactivar un tenant); precisiones de RN-016 (slug reservado y sufijo), RN-018 (límite de 5 intentos en 15 minutos) y RN-019 (Dueño sin negocio hasta UC-03, un negocio por Dueño); RF-007 con correo y teléfono de contacto | Alberto Rincón |
| 2.4 | 2026-10-07 | RNF-012 definido formalmente: cobertura mínima de 80% (backend) y 80/80/75/60% statements/lines/functions/branches (frontend), aplicada como umbral obligatorio en CI (`03-3`, CAPDC-40) | Alberto Rincón |
| 2.5 | 2026-10-14 | SUP-010 referencia su historia ya asignada (US-029/CAPDC-43, Sprint 2, 5 SP) — hasta ahora solo existía como nota de diseño, sin historia real en el backlog | Alberto Rincón |
| 2.6 | 2026-10-14 | SUP-006/DEP-005: aclara que el correo transaccional con AWS SES solo necesita credenciales de API, no el despliegue completo de la app en AWS (RES-009/DEP-006 siguen diferidos sin bloquear esto) | Alberto Rincón |
| 2.7 | 2026-10-14 | SUP-010 corrige la clave de la historia de US-029/CAPDC-43 a **US-029/CAPDC-49**  — CAPDC-43 ya pertenecía a trabajo del Sprint 0 en Jira (`03-1` §5.5), no se conocía ese rango al asignar la clave por primera vez | Alberto Rincón |
| 2.8 | 2026-10-14 | RES-009: el profesor guía confirma que el despliegue en AWS **no se requiere**  para la entrega — la demo final se presenta con un video, no con un sistema desplegado. Reemplaza la nota de "pendiente de confirmación" | Alberto Rincón |
