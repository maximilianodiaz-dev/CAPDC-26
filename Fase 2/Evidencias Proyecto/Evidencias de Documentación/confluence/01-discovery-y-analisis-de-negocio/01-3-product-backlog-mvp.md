> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13991945) · versión 8 · última edición 2026-10-14

# Product Backlog — MVP

| Campo | Detalle |
| --- | --- |
| **Etapa** | 1 — Discovery & Análisis de Negocio |
| **Rol aplicado** | Product Owner |
| **Versión** | 2.6 — US-029 (landing/demo) corregida a CAPDC-49, la clave CAPDC-43 ya estaba asignada en Jira a trabajo del Sprint 0 (2026-10-14); v2.5: criterios de aceptación del Sprint 2 en §14 |
| **Archivo fuente** | `02-product-backlog.md` |
| **Estado** | Documento vivo |

## Convenciones

| Aspecto | Detalle |
| --- | --- |
| Escala de estimación | Fibonacci (1, 2, 3, 5, 8, 13) |
| Historia de referencia (3 pts) | "Como cliente final, quiero ver los servicios disponibles de un negocio." |
| Prioridad | MoSCoW: **M** ust have / **S** hould have / **C** ould have / **W** on't have (fuera de alcance MVP) |

### Supuestos base (a confirmar con el equipo)

* Verticales piloto: Salón de belleza/spa + Clínica/consultorio profesional.
* Actores: Super Admin (plataforma), Dueño de Negocio (tenant admin), Staff/Profesional, Cliente Final.

## 1. EPIC 1 — Autenticación y Multi-tenancy (fundacional, cross-cutting)

Debe resolverse primero: todo lo demás depende de tener usuarios, roles y aislamiento de datos por tenant.

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-001 | Como usuario, quiero registrarme e iniciar sesión de forma segura, para acceder a la plataforma según mi rol. | M | 8 | — |
| US-002 | Como sistema, se debe garantizar aislamiento de datos entre tenants a nivel de base de datos y backend, para operar como SaaS multi-cliente de forma segura. | M | 13 | US-001 |
| US-003 | Como Super Admin, quiero ver y auditar los tenants dados de alta en la plataforma, para administrar el sistema. | S | 5 | US-001, US-002 |

**Subtotal Must (Epic 1):**  21 pts

## 2. EPIC 2 — Onboarding y Gestión de Tenant

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-004 | Como dueño de negocio, quiero registrar mi negocio (tenant) en la plataforma, para empezar a operar. | M | 5 | US-001 |
| US-005 | Como dueño de negocio, quiero seleccionar el rubro de mi negocio durante el registro, para que el sistema preconfigure servicios y recursos típicos de esa vertical. | M | 8 | US-004, US-009 |
| US-006 | Como dueño de negocio, quiero invitar y gestionar cuentas de mi staff, para asignarles servicios y horarios. | M | 5 | US-004 |
| US-007 | Como dueño de negocio, quiero editar los datos generales de mi negocio (nombre, dirección, horario general), para mantener mi información actualizada. | S | 3 | US-004 |

**Subtotal Must (Epic 2):**  18 pts

**Nota de planificación (2026-09-24):**  US-005 se ejecuta en el Sprint 2, después de Catalog: aplica la plantilla de servicios y recursos del rubro, que se crean en Catalog. La selección del rubro al registrar el negocio queda cubierta por US-004. Las plantillas iniciales (Salón de belleza y Clínica) están en `02-2-modelo-de-dominio-ddd.md` §3.5.

## 3. EPIC 3 — Catálogo de Servicios y Recursos

Corazón del diferenciador técnico: el modelo de recursos debe soportar profesional individual y recurso compuesto sin complejidad excesiva para el usuario final.

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-008 | Como dueño de negocio, quiero crear y editar servicios (nombre, duración, precio), para ofrecerlos a mis clientes. | M | 5 | US-004 |
| US-009 | Como dueño de negocio, quiero definir recursos (profesionales, salas, equipos) y asociarlos a uno o más servicios, para reflejar cómo opera realmente mi negocio. | M | 8 | US-008 |
| US-010 | Como dueño de negocio, quiero configurar la disponibilidad horaria de cada recurso, para que el sistema sepa cuándo puede reservarse. | M | 8 | US-009 |
| US-011 | Como dueño de negocio, quiero definir servicios grupales con cupo máximo (ej. clases de gimnasio), para dar soporte a negocios con reservas grupales. | S | 5 | US-009 |

**Subtotal Must (Epic 3):**  21 pts

## 4. EPIC 4 — Motor de Reservas (Booking Engine)

Es el flujo crítico de negocio: si esto no funciona impecablemente, el producto no tiene valor.

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-012 | Como cliente final, quiero ver los horarios disponibles de un servicio y reservar una cita, para agendar sin llamar al negocio. | M | 13 | US-010 |
| US-013 | Como cliente final, quiero recibir confirmación de que mi reserva fue registrada, para tener certeza de que quedó agendada. | M | 3 | US-012 |
| US-014 | Como staff/dueño de negocio, quiero ver mi agenda diaria y semanal de citas, para organizar mi jornada. | M | 8 | US-012 |
| US-015 | Como staff, quiero modificar o cancelar una cita existente, para gestionar cambios de último minuto. | M | 5 | US-012 |
| US-016 | Como cliente final, quiero cancelar mi propia cita desde un link enviado por email, para no depender de llamar al negocio. | S | 5 | US-012, US-017 |

**Subtotal Must (Epic 4):**  29 pts

## 5. EPIC 5 — Notificaciones

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-017 | Como cliente final, quiero recibir un email de confirmación al reservar, para tener respaldo de mi cita. | M | 3 | US-012 |
| US-018 | Como cliente final, quiero recibir un recordatorio por email 24h antes de mi cita, para no olvidarla. | S | 5 | US-017 |
| US-019 | Como dueño de negocio, quiero recibir una notificación cuando se agenda una nueva cita, para estar al tanto sin revisar el sistema constantemente. | C | 3 | US-012 |

**Nota de alcance:**  WhatsApp/SMS quedan explícitamente **fuera del MVP**  (Won't have). Son canales de valor probado (así lo confirma el benchmark de AgendaPro), pero agregan dependencia de proveedores externos de pago (Twilio, WhatsApp Business API) que no aportan al objetivo académico central del proyecto y consumen tiempo de integración desproporcionado frente al plazo disponible. Se documentan como **Fase 2**  en el backlog de producto.

**Subtotal Must (Epic 5):**  3 pts

## 6. EPIC 6 — Panel de Administración

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-020 | Como dueño de negocio, quiero ver un dashboard con métricas básicas (citas del día, citas de la semana, tasa de ocupación), para tener visibilidad de mi negocio. | S | 5 | US-014 |
| US-021 | Como dueño de negocio, quiero exportar un reporte simple de citas del mes, para llevar mi propio control administrativo. | C | 3 | US-020 |

**Subtotal Must (Epic 6):**  0 pts (todo Should/Could)

## 7. EPIC 7 — Asistente Conversacional (Chatbot)

Nuevo canal sobre el motor de reservas ya existente: el asistente no reimplementa reglas de negocio, orquesta los mismos Application Services de Catalog y Booking a través de una interfaz conversacional. Depende de que Catalog y Booking ya estén construidos; es el último módulo funcional en el orden de dependencias.

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-022 | Como cliente final, quiero consultar disponibilidad de un servicio conversando en lenguaje natural con el asistente, para no tener que navegar el calendario manualmente. | M | 8 | US-012 |
| US-023 | Como cliente final, quiero que el asistente me recomiende el profesional mejor calificado disponible, para elegir más rápido cuando hay varias opciones. | M | 5 | US-022, US-024 |
| US-024 | Como dueño de negocio, quiero asignar manualmente una calificación (1.0–5.0) a cada profesional, para que el asistente pueda recomendar mejor. | M | 3 | US-009 |
| US-025 | Como cliente final, quiero completar toda mi reserva conversando con el asistente sin salir del chat, para agendar de la forma más simple posible. | M | 13 | US-022, US-012 |
| US-026 | Como dueño de negocio, quiero configurar la información que el asistente usará para responder preguntas frecuentes, para que resuelva dudas comunes sin mi intervención. | M | 5 | US-004 |
| US-027 | Como cliente final, quiero que el asistente responda mis preguntas frecuentes sobre el negocio (horario, ubicación, políticas), para resolver dudas sin llamar. | M | 5 | US-026 |
| US-028 | Como sistema, se debe registrar el historial de conversación por trazabilidad, para auditoría y mejora continua. | S | 3 | US-022 |

**Subtotal Must (Epic 7):**  39 pts

## 7.1 Landing Pública y Captura de Leads (fuera del árbol de Épicas, SUP-010)

No es un Epic ni un módulo propio — SUP-010 (`01-4`) ya la define así: "funcionalidad de marketing... no genera una entidad de dominio nueva ni un módulo propio". Se agrega aquí como historia real porque hasta el 2026-10-14 solo existía como nota de diseño (dónde viviría, en `02-4`/`02-5`), sin story points ni sprint asignado — un hueco de planificación detectado al revisar el Sprint 2.

**Corrección de clave (2026-10-14):**  esta historia se intentó registrar primero como CAPDC-43, pero esa clave ya estaba asignada en Jira a trabajo del Sprint 0 (propuesta del proyecto), parte de un rango (CAPDC-43 a 48) que no constaba en este documento al redactar la historia por primera vez — ver `03-1` §5.5 para el detalle de ese rango. Se corrige a **CAPDC-49**, la primera clave libre después de ese rango.

| ID | Historia | Prioridad | SP | Dependencias |
| --- | --- | --- | --- | --- |
| US-029 | Como visitante de la landing pública, quiero solicitar una demo gratuita de 14 días dejando mis datos de contacto, para evaluar la plataforma antes de registrarme. | S | 5 | — |

**Criterios de aceptación:**
1\. Dado un visitante sin sesión, cuando completa nombre, nombre del negocio, correo y cantidad de profesionales, entonces la solicitud se registra y se notifica al equipo (reutiliza `NotificationPort`, mismo adaptador de consola que CAPDC-13 hasta que exista el módulo Notification).  
2\. Dado un campo obligatorio vacío o un correo con formato inválido, cuando se envía el formulario, entonces se rechaza indicando qué corregir.  
3\. Dada una solicitud enviada con éxito, entonces se confirma visualmente sin redirigir a ningún flujo autenticado (es anónimo, sin cuenta ni tenant).  
4\. No crea cuenta, usuario ni tenant — es una captura de interés comercial, nunca un alta real en la plataforma.

**Subtotal Must (Landing):**  0 pts (Should)

## 8. Resumen de Priorización y Esfuerzo

| Epic | Pts Must | Pts Should | Pts Could | Total |
| --- | --- | --- | --- | --- |
| 1. Auth y Multi-tenancy | 21 | 5 | 0 | 26 |
| 1. Onboarding y Tenant | 18 | 3 | 0 | 21 |
| 1. Catálogo Servicios/Recursos | 21 | 5 | 0 | 26 |
| 1. Motor de Reservas | 29 | 5 | 0 | 34 |
| 1. Notificaciones | 3 | 5 | 3 | 11 |
| 1. Panel de Administración | 0 | 5 | 3 | 8 |
| 1. Asistente Conversacional | 39 | 3 | 0 | 42 |
| Landing y Captura de Leads (SUP-010) | 0 | 5 | 0 | 5 |
| **Total** | **131** | **36** | **6** | **173** |

## 9. Alerta de Riesgo — Nota del Technical Lead (actualizada)

Cuando se cerró esta actividad por primera vez, el scope Must-have era 92 pts y ya se había marcado como ajustado. Con la incorporación del Epic 7 (Asistente Conversacional), **el Must-have sube a 131 pts, un salto de +42%**  sobre la cifra original, en el plazo de implementación con el mismo equipo de 3 personas (originalmente \~4 semanas; \~7,5 semanas, del 23 sep al 14 nov, tras la reprogramación del 2026-09-23).

Esto **no es realista**  tal como está. Además, el Epic 7 no puede paralelizarse con los epics anteriores: depende funcionalmente de que Catalog (Epic 3) y Booking (Epic 4) ya estén construidos, así que se suma al final de la ruta crítica, no en paralelo.

### Recomendaciones (en orden de preferencia)

1. \~\~**Extender el roadmap a un Sprint 5** , tomando el buffer reservado en Etapa 10 para contingencias.\~\~ **Descartada (2026-09-23):**  el plan aprobado se mantiene en **4 sprints**, con todo el Epic 7 ejecutado dentro del Sprint 3 (después de Booking) y la Etapa 10 intacta como semana de cierre. Ver `03-1` v3.0 §3.
2. **Si la carga del Sprint 3 no es viable** , recortar el Epic 6 completo (Panel de Administración, ya era 0 pts Must) y además degradar US-011 (servicios grupales, Epic 3) a "documentado pero no implementado", para liberar capacidad real de implementación sin tocar el Epic 7.
3. **No recomendado:**  recortar el Epic 7 para compensar. El equipo ya decidió explícitamente que el chatbot es Must-have y forma parte del MVP que se va a defender; recortarlo contradice esa decisión y el valor diferenciador que aporta al benchmark.

Esto no se resuelve en esta actividad (corresponde formalmente a Etapa 8/9), pero queda registrado con la cifra actualizada.

## 10. Fuera de Alcance del MVP (Won't have)

Para evitar "funcionalidades innecesarias", estas quedan fuera y documentadas como trabajo futuro:

* Pagos en línea / integración con pasarela de pago
* Marketplace público de descubrimiento de negocios (tipo Booksy/Fresha)
* Notificaciones por WhatsApp/SMS
* Gestión de inventario de productos
* Gift cards, cupones y programas de fidelización
* Cálculo automático de comisiones para profesionales
* Multi-sede por tenant
* Aplicación móvil nativa (solo se construye web responsive)
* Recuperación de contraseña ("olvidé mi contraseña"): Post-MVP (decisión 2026-09-24, para proteger la capacidad del Sprint 3)
* Cuentas para el rol Cliente Final: en el MVP el cliente reserva sin cuenta; el rol existe en el modelo pero no tiene flujo de registro
* Vertical Gimnasio/clases grupales como tercera vertical piloto oficial (decisión 2026-09-23: el rubro queda soportado estructuralmente en la base de datos para demostrar genericidad, pero no se construyen plantilla de onboarding ni datos de demostración dedicados para el MVP; el servicio grupal ya se valida con la vertical Salón de belleza)

## 11. Cierre de esta actividad

### Objetivos cumplidos

* Backlog completo estructurado en 7 épicas (se agregó Epic 7 — Asistente Conversacional).
* 28 historias de usuario con formato estándar (Como/Quiero/Para).
* Priorización MoSCoW aplicada de forma consistente.
* Estimación en story points con historia de referencia.
* Dependencias explícitas entre historias.
* Alcance "Won't have" documentado explícitamente.
* Riesgo de capacidad recalculado tras el Epic 7 (131 pts Must) con recomendación concreta de mitigación.

### Entregables

* `02-product-backlog.md` (v2.0)

### Documentación generada

Lista para el capítulo de "Especificación de Requisitos" o "Backlog del Producto" de la memoria.

### Próximos pasos

Con el backlog cerrado, corresponde pasar a **Etapa 2 — Arquitectura de Software** , donde estas épicas se traducirán en módulos del monolito modular (bounded contexts) y se redactará el ADR-001 formalizando la decisión de alcance multi-rubro que se arrastra desde la Etapa 0.

## 12. Correspondencia con Jira (proyecto CAPDC)

Trazabilidad entre las historias de este backlog y las issues del proyecto Jira `CAPDC` (cargadas el 2026-09-24 actualizando las issues existentes; ver `03-1-configuracion-de-jira-y-github.md` §5).

**Épicas:**  CAPDC-1 IAM · CAPDC-2 Tenant · CAPDC-3 Catalog · CAPDC-4 Booking · CAPDC-5 Notification · CAPDC-6 Reporting · CAPDC-7 Assistant.

| Historia | Clave Jira | Épica | Sprint | SP |
| --- | --- | --- | --- | --- |
| US-001 | CAPDC-8 | IAM | Sprint 1 | 8 |
| US-002 | CAPDC-9 | IAM | Sprint 1 | 13 |
| US-003 | CAPDC-10 | IAM | Sprint 1 | 5 |
| US-004 | CAPDC-11 | Tenant | Sprint 1 | 5 |
| US-005 | CAPDC-12 | Tenant | Sprint 2 | 8 |
| US-006 | CAPDC-13 | Tenant | Sprint 1 | 5 |
| US-007 | CAPDC-14 | Tenant | Sprint 1 | 3 |
| US-008 | CAPDC-15 | Catalog | Sprint 2 | 5 |
| US-009 | CAPDC-16 | Catalog | Sprint 2 | 8 |
| US-010 | CAPDC-17 | Catalog | Sprint 2 | 8 |
| US-011 | CAPDC-18 | Catalog | Sprint 2 | 5 |
| US-012 | CAPDC-19 | Booking | Sprint 3 | 13 |
| US-013 | CAPDC-20 | Booking | Sprint 3 | 3 |
| US-014 | CAPDC-21 | Booking | Sprint 3 | 8 |
| US-015 | CAPDC-22 | Booking | Sprint 3 | 5 |
| US-016 | CAPDC-23 | Booking | Sprint 3 | 5 |
| US-017 | CAPDC-24 | Notification | Sprint 4 | 3 |
| US-018 | CAPDC-25 | Notification | Sprint 4 | 5 |
| US-019 | CAPDC-26 | Notification | Sprint 4 | 3 |
| US-020 | CAPDC-27 | Reporting | Sprint 4 | 5 |
| US-021 | CAPDC-28 | Reporting | Sprint 4 | 3 |
| US-022 | CAPDC-29 | Assistant | Sprint 3 | 8 |
| US-023 | CAPDC-30 | Assistant | Sprint 3 | 5 |
| US-024 | CAPDC-31 | Assistant | Sprint 3 | 3 |
| US-025 | CAPDC-32 | Assistant | Sprint 3 | 13 |
| US-026 | CAPDC-33 | Assistant | Sprint 3 | 5 |
| US-027 | CAPDC-34 | Assistant | Sprint 3 | 5 |
| US-028 | CAPDC-35 | Assistant | Sprint 3 | 3 |
| US-029 | CAPDC-49 | Landing (fuera del árbol de épicas, SUP-010) | Sprint 2 | 5 |

Tasks de preparación del Sprint 1: CAPDC-36 a CAPDC-42. Tasks del Sprint 0 y del frente de documentación grupal: CAPDC-43 a CAPDC-48 (ver `03-1` §5.5). US-029 usa **CAPDC-49**  — rompe la fórmula "clave = número de historia + 7" porque esos rangos ya estaban tomados cuando se agregó la historia (2026-10-14, después del Sprint 1); una versión anterior de este documento le había asignado por error CAPDC-43, que ya pertenecía al Sprint 0.

## 13. Criterios de aceptación — Sprint 1

Criterios de aceptación de las 6 historias del Sprint 1, redactados solo con lo documentado (RF, casos de uso, reglas RN, modelo de dominio y base de datos). Cada criterio es verificable con una prueba automatizada. Se cargan en la descripción de las issues CAPDC-8 a CAPDC-14 (ver `03-1-configuracion-de-jira-y-github.md` §5).

**Definición de hecho (común a todas las historias):**

* Código con pruebas automatizadas que pasan en CI (hasta que exista el pipeline, CAPDC-39, se ejecutan en el entorno Docker local).
* Pull Request revisado y mergeado a `main`, con la clave CAPDC-N en la rama, los commits y el título del PR.
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

**Decisiones tomadas el 2026-09-24 para poder redactar los criterios:**

| Tema | Decisión | Documentada en |
| --- | --- | --- |
| Dueño sin negocio | Un Dueño puede existir sin tenant hasta registrar su negocio; cada Dueño registra uno solo | RN-019, UC-03, `02-3` §4.2 |
| Límite de intentos de inicio de sesión | 5 intentos fallidos en 15 minutos → bloqueo de 15 minutos | RN-018, `02-4` |
| Desactivar un tenant | Bloquea el inicio de sesión de sus usuarios y su página pública; se registra en el log estructurado | RN-020, UC-19 |
| "Auditar" tenants (US-003) | Listar y ver estado (RF-005) más el registro en el log estructurado de los cambios de estado; sin historial adicional en el MVP | RN-020 |
| Datos de contacto (RF-007) | Correo y teléfono de contacto; la dirección es opcional al registrar y obligatoria al editar | `02-3` §4.1, UC-03 |
| Slug reservado | Al generarlo se trata como colisión (sufijo numérico); al editarlo manualmente se rechaza | RN-016 |
| Asignar servicios y horarios al staff (US-006) | Fuera del Sprint 1: depende de Catalog y del vínculo usuario-recurso (RN-017, Sprint 2). El Sprint 1 cubre invitar y activar/desactivar cuentas | RN-017 |

### US-001 — CAPDC-8 (8 SP)

1. Dado un correo no registrado y una contraseña válida, cuando el usuario se auto-registra, entonces se crea una cuenta activa con rol Dueño de Negocio (sin poder elegir otro rol), sin tenant asociado todavía (RN-019), y la contraseña se guarda solo como hash.
2. Dado un correo ya registrado, cuando intenta registrarse, entonces se rechaza indicando que ya existe una cuenta con ese correo (UC-01, E1).
3. Dada una contraseña que no cumple la política (menos de 10 caracteres, común o solo numérica), cuando se registra, entonces se rechaza y se pide corrección (UC-01, E2; RN-018).
4. Dadas credenciales válidas de una cuenta activa, cuando inicia sesión, entonces recibe un token de acceso de 30 minutos y uno de refresco de 7 días con rotación, que identifican al usuario, su rol y su tenant (si tiene) (UC-02; RN-018).
5. Dadas credenciales inválidas, cuando inicia sesión, entonces se rechaza sin indicar si el error está en el correo o en la contraseña (UC-02, E1).
6. Dada una cuenta desactivada, cuando inicia sesión, entonces se informa que la cuenta no está disponible (UC-02, E2).
7. Dados 5 intentos fallidos de inicio de sesión en 15 minutos, cuando se hace un intento más, entonces se rechaza durante 15 minutos (RN-018).

### US-002 — CAPDC-9 (13 SP)

1. Dado un usuario del tenant A, cuando consulta datos de negocio, entonces solo obtiene registros de su tenant (RF-004).
2. Dado un usuario del tenant A, cuando intenta leer, modificar o eliminar un registro del tenant B por su identificador, entonces no accede al registro ni lo altera.
3. Dada una consulta sin tenant activo en el contexto, cuando se usa un modelo con alcance de tenant, entonces no devuelve datos.
4. Dada una petición autenticada, cuando se determina el tenant activo, entonces se toma del token y no de valores enviados por el cliente.
5. Dado un modelo con alcance de tenant, cuando se define, entonces `tenant_id` es obligatorio.
6. Dados los módulos IAM y Tenant, entonces cada uno tiene al menos una prueba automatizada que demuestra que un tenant no accede a los datos de otro.

### US-003 — CAPDC-10 (5 SP)

1. Dado un Super Admin, cuando solicita el listado de tenants, entonces ve por cada uno solo nombre, estado, fecha de alta y plan (UC-19; RN-010).
2. Dado un Super Admin, cuando consulta cualquier endpoint de administración, entonces ninguna respuesta incluye datos operativos (reservas, clientes) (RN-010).
3. Dado un tenant, cuando el Super Admin lo activa o lo desactiva, entonces su estado se actualiza y el cambio queda en el log estructurado (RF-006; RN-020).
4. Dado un tenant ya desactivado, cuando el Super Admin lo desactiva otra vez, entonces se informa que la operación no aplica (UC-19, E1).
5. Dado un tenant desactivado, cuando un usuario de ese tenant intenta iniciar sesión, entonces se informa que la cuenta no está disponible (RN-020).
6. Dado un usuario que no es Super Admin, cuando accede a la administración de tenants, entonces se le niega el acceso (RNF-005).

### US-004 — CAPDC-11 (5 SP)

1. Dado un Dueño autenticado sin negocio, cuando registra nombre, rubro y datos de contacto (correo y teléfono) válidos, entonces se crea un tenant activo asociado a él como Dueño (UC-03; RF-007).
2. Dado un nombre de negocio, cuando se crea el tenant, entonces el slug se genera desde el nombre (minúsculas, sin tildes, con guiones, 3 a 50 caracteres) y es único (RN-016).
3. Dado un slug ya existente o reservado (`auth`, `app`, `admin`, `api`, `docs`, `login`), cuando se registra el negocio, entonces el slug lleva un sufijo numérico y sigue siendo único (RN-016).
4. Dado un nombre vacío, un rubro no válido o un contacto inválido, cuando se intenta registrar, entonces se rechaza (RN-007).
5. Dado el registro completado, entonces el tenant queda con su rubro y sin servicios ni recursos; la plantilla se aplica en US-005 (Sprint 2).
6. Dado un Dueño que ya tiene un negocio, cuando intenta registrar otro, entonces se rechaza (RN-019).
7. Dado un usuario no autenticado o sin rol Dueño, cuando intenta registrar un negocio, entonces se rechaza (UC-03).

### US-006 — CAPDC-13 (5 SP)

1. Dado un Dueño, cuando invita un correo válido, entonces se genera un enlace con token firmado y se envía el correo (por consola en desarrollo) (UC-04; RN-019).
2. Dado un enlace vencido (más de 7 días) o ya usado, cuando se intenta registrar, entonces se rechaza (RN-019).
3. Dado un enlace válido, cuando la persona completa su registro con contraseña conforme a RN-018, entonces se crea una cuenta con rol Staff asociada al tenant y aparece en su lista de staff (UC-01, A1).
4. Dado un correo que pertenece a un Dueño de otro tenant, cuando se invita, entonces se rechaza informando el conflicto (UC-04, E1).
5. Dado un Dueño, cuando desactiva a un miembro del staff, entonces su cuenta queda inactiva, no puede iniciar sesión y su registro se conserva (RF-010; UC-04, A1).
6. Dado un Dueño, cuando activa una cuenta de staff desactivada, entonces vuelve a estar activa (RF-010).
7. Dado un Staff o un Dueño de otro tenant, cuando intenta invitar o gestionar staff de este tenant, entonces se le niega el acceso (RN-005).

### US-007 — CAPDC-14 (3 SP)

1. Dado un Dueño, cuando edita nombre, dirección u horario general con datos válidos, entonces se guardan y una nueva consulta del negocio devuelve los valores actualizados; su visualización en la página pública se verifica cuando exista (Sprint 3) (UC-05).
2. Dado un Dueño, cuando cambia el slug a uno válido y libre, entonces se actualiza y el sistema muestra la advertencia de que los enlaces ya compartidos dejarán de funcionar (RN-016).
3. Dado un slug ya usado, reservado o con formato inválido, cuando se intenta guardar, entonces se rechaza (RN-016).
4. Dados datos incompletos o inválidos (ej. dirección vacía), cuando se intenta guardar, entonces se rechaza hasta corregirlos (UC-05, E1).
5. Dado un horario de cierre no posterior al de apertura, cuando se guarda, entonces se rechaza.
6. Dado un Staff o un Dueño de otro tenant, cuando intenta editar el negocio, entonces se le niega el acceso (RN-005).

Si un criterio no se puede cumplir tal como está escrito, se ajusta el criterio y el documento antes de cerrar la historia, registrando el cambio en el Control de cambios.

## 14. Criterios de aceptación — Sprint 2

Criterios de aceptación de las 5 historias del Sprint 2, redactados con el mismo método que la §13: solo con lo documentado (RF, casos de uso, reglas RN, modelo de dominio y base de datos). Se cargan en la descripción de las issues CAPDC-12 y CAPDC-15 a CAPDC-18. Orden de trabajo: US-008 → US-009 → US-010 / US-011 → US-005 (US-005 depende de US-009).

**Definición de hecho (común a todas las historias del Sprint 2):**

* Código con pruebas automatizadas que pasan en CI (CAPDC-39), sin bajar la cobertura mínima de `03-3`.
* Pull Request de `develop` a `main` revisado y aprobado por un compañero del equipo antes de fusionar (`03-1`).
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

**Decisiones tomadas el 2026-10-14 para poder redactar los criterios:**

| Tema | Decisión | Documentada en |
| --- | --- | --- |
| Criterios que dependen de reservas | Se verifican cuando exista Booking (Sprint 3); en el Sprint 2 se deja la regla preparada y se prueba lo que no requiere reservas | UC-06 E2, RN-006 |
| Eliminar o desactivar | Mientras no existan reservas, un servicio o recurso se puede eliminar o desactivar; un recurso asociado a un servicio no se elimina, se sugiere desactivarlo | UC-06 A1, `02-3` §4.6 (`ON DELETE RESTRICT`) |
| Quién configura la disponibilidad | El Dueño configura la de cualquier recurso de su tenant; el Staff, solo la del recurso vinculado a su cuenta | UC-08, RN-005, RN-017 |
| Plantilla por rubro | Solo se ofrece mientras el negocio no tenga servicios ni recursos, para evitar duplicados | UC-03, RN-007, `02-2` §3.5 |

### US-008 — CAPDC-15 (5 SP)

1. Dado un Dueño, cuando crea un servicio con nombre, duración y precio válidos, entonces queda activo en el catálogo de su tenant (UC-06; RF-012).
2. Dada una duración igual o menor a cero, o un precio negativo, cuando se guarda, entonces se rechaza (UC-06, E1).
3. Dado un servicio existente, cuando el Dueño edita sus datos con valores válidos, entonces una nueva consulta devuelve los valores actualizados (RF-012).
4. Dado un servicio, cuando el Dueño lo desactiva, entonces queda inactivo y se conserva su registro; cuando lo elimina y no tiene reservas, se elimina. El bloqueo por reservas futuras se verifica en el Sprint 3 (UC-06, A1 y E2).
5. Dado un Staff o un Dueño de otro tenant, cuando intenta crear, editar o eliminar servicios de este tenant, entonces se le niega el acceso (RN-005).

### US-009 — CAPDC-16 (8 SP)

1. Dado un Dueño, cuando crea un recurso con nombre y tipo (profesional, sala o equipo), entonces queda activo en su tenant (UC-07; RF-013).
2. Dado un servicio, cuando el Dueño le asocia varios recursos en un mismo grupo, entonces son alternativas entre sí — Escenario 1, individual con alternativas (RF-014; `02-2` §4.2).
3. Dado un servicio, cuando el Dueño le asocia recursos en grupos distintos, entonces todos se requieren a la vez — Escenario 2, recurso compuesto (UC-07, A1).
4. Dado un recurso de otro tenant, cuando se intenta asociar a un servicio, entonces se rechaza (UC-07, E1; RN-004).
5. Dado un recurso asociado a un servicio, cuando se intenta eliminar, entonces se rechaza y se sugiere desactivarlo (`02-3` §4.6).
6. Dado un recurso de tipo profesional, cuando el Dueño lo vincula a una cuenta de su tenant (Staff o él mismo), entonces queda vinculado; una cuenta se vincula a lo más a un recurso, y las salas y equipos no se vinculan (RN-017).
7. Dado un Staff o un Dueño de otro tenant, cuando intenta gestionar recursos de este tenant, entonces se le niega el acceso (RN-005).

### US-010 — CAPDC-17 (8 SP)

1. Dado un recurso, cuando se define un horario semanal recurrente (día y rango horario), entonces se guarda como su disponibilidad base (UC-08; RF-015).
2. Dado un rango con hora de fin no posterior a la de inicio, cuando se guarda, entonces se rechaza (UC-08, E1).
3. Dado un recurso con disponibilidad base, cuando se agrega una excepción (fecha bloqueada por ausencia o feriado), entonces ese día queda excluido de su disponibilidad (RF-016).
4. Dado un recurso sin disponibilidad configurada, entonces queda marcado como "no reservable" (UC-08, A1).
5. Dado un servicio y un rango de fechas, cuando se calcula la disponibilidad, entonces un bloque es válido solo si cada grupo de recursos del servicio tiene al menos uno disponible a la vez, descontando las excepciones (`02-2` §4.6); las reservas existentes se descuentan en el Sprint 3.
6. Dado un Staff con un recurso vinculado, cuando configura la disponibilidad de ese recurso, entonces se guarda; si intenta configurar la de otro recurso, se le niega el acceso (RN-017).

### US-011 — CAPDC-18 (5 SP)

1. Dado un Dueño, cuando marca un servicio como grupal con un cupo máximo mayor a cero, entonces queda en modalidad grupal — Escenario 3 (UC-09; RF-017).
2. Dado un cupo igual o menor a cero, cuando se guarda, entonces se rechaza (UC-09, E1).
3. Dado un servicio grupal sin cupo, o un servicio individual con cupo, cuando se guarda, entonces se rechaza (`02-3`, restricción de `servicios`).
4. Dado un servicio grupal, cuando se consulta, entonces informa su cupo máximo; el rechazo de reservas por sobre el cupo (RN-006) se verifica en el Sprint 3.

### US-005 — CAPDC-12 (8 SP)

1. Dado un negocio de rubro Salón de belleza o Clínica sin servicios ni recursos, cuando el Dueño acepta la plantilla, entonces se crean los servicios, recursos y grupos definidos en `02-2` §3.5 (UC-03; RF-008; RN-007).
2. Dada la plantilla de Clínica aplicada, entonces "Consulta especialista" requiere a la vez Box 1, Equipo médico y Profesional 2 (Escenario 2); con la de Salón, "Taller de peinados" queda grupal con cupo 4 (Escenario 3).
3. Dados los servicios y recursos creados por la plantilla, entonces son editables y eliminables como cualquier otro, y los recursos quedan "no reservables" hasta configurar su disponibilidad (`02-2` §3.5).
4. Dado un Dueño que omite la plantilla, entonces su negocio queda sin servicios ni recursos (UC-03, A1).
5. Dado un rubro sin plantilla (Gimnasio u Otro), cuando se ofrece la preconfiguración, entonces se informa que no hay plantilla y el negocio queda vacío (UC-03, E1).
6. Dado un negocio que ya tiene servicios o recursos, entonces no se ofrece la plantilla.

_Documento vivo — Etapa 1 (Discovery & Análisis de Negocio)._

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 2.0 | — | Agrega Epic 7 (Asistente Conversacional) | Equipo del proyecto |
| 2.1 | 2026-09-23 | Nota: Gimnasio fuera del alcance oficial; se descarta la recomendación del Sprint 5 (plan de 4 sprints); plazo de implementación actualizado | Alberto Rincón |
| 2.2 | 2026-09-24 | US-005 se ejecuta en el Sprint 2 (dependencia de US-009); US-016 depende de US-017 (corrige la cita a US-018); recuperación de contraseña y cuentas de Cliente Final fuera del MVP | Alberto Rincón |
| 2.3 | 2026-09-24 | Nueva §12 con la correspondencia US-0XX → CAPDC-N (historias CAPDC-8 a 35, épicas CAPDC-1 a 7, tasks CAPDC-36 a 42) | Alberto Rincón |
| 2.4 | 2026-09-24 | Nueva §13 con la definición de hecho y los criterios de aceptación de US-001, US-002, US-003, US-004, US-006 y US-007 (CAPDC-8 a 11, 13 y 14) y las decisiones que los sustentan | Alberto Rincón |
| 2.5 | 2026-10-14 | Nueva §14 con la definición de hecho del Sprint 2 y los criterios de aceptación de US-005, US-008, US-009, US-010 y US-011 (CAPDC-12 y CAPDC-15 a 18), y las 4 decisiones que los sustentan | Alberto Rincón |
| 2.6 | 2026-10-14 | Nueva §7.1 y historia US-029, reincorporada con la clave corregida (**CAPDC-49**  en vez de CAPDC-43 — esa clave ya estaba asignada a trabajo del Sprint 0 en Jira, ver `03-1` §5.5); totales de §8 actualizados a 173 pts | Alberto Rincón |
