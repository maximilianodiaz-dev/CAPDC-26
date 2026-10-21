> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13959178) · versión 6 · última edición 2026-09-24

# Especificación de Casos de Uso

## Plataforma SaaS de Administración de Reservas y Citas

| Campo | Detalle |
| --- | --- |
| **Etapa** | 1 — Discovery & Análisis de Negocio (cierre de análisis funcional detallado) |
| **Versión** | 2.2 — precisiones de UC-02, UC-03 y UC-19 para el Sprint 1 (2026-09-24); v2.1: reglas de alta de cuentas, slug, invitación de staff y vínculo usuario-recurso |
| **Trazabilidad** | Cada caso de uso referencia los RF de `03-especificacion-requerimientos.md` |
| **Última actualización** | 2026-09-24 |
| **Archivo fuente** | `04-casos-de-uso.md` |

## 1. Índice de Casos de Uso

| ID | Nombre | Actor principal | RF relacionados |
| --- | --- | --- | --- |
| UC-01 | Registrar Usuario | Cualquier usuario | RF-001 |
| UC-02 | Iniciar Sesión | Cualquier usuario | RF-002, RF-003 |
| UC-03 | Registrar Negocio (Onboarding) | Dueño de Negocio | RF-007, RF-008 |
| UC-04 | Gestionar Staff | Dueño de Negocio | RF-009, RF-010 |
| UC-05 | Editar Datos del Negocio | Dueño de Negocio | RF-011 |
| UC-06 | Gestionar Catálogo de Servicios | Dueño de Negocio | RF-012 |
| UC-07 | Gestionar Recursos | Dueño de Negocio | RF-013, RF-014 |
| UC-08 | Configurar Disponibilidad de Recurso | Dueño de Negocio / Staff | RF-015, RF-016 |
| UC-09 | Configurar Servicio Grupal | Dueño de Negocio | RF-017 |
| UC-10 | Consultar Disponibilidad de Horarios | Cliente Final | RF-018 |
| UC-11 | Crear Reserva | Cliente Final | RF-019, RF-020, RF-021 |
| UC-12 | Ver Agenda de Citas | Staff / Dueño de Negocio | RF-022 |
| UC-13 | Modificar Reserva | Staff | RF-023 |
| UC-14 | Cancelar Reserva (Staff) | Staff | RF-024 |
| UC-15 | Cancelar Reserva (Cliente) | Cliente Final | RF-025 |
| UC-16 | Notificar Evento de Reserva | Sistema | RF-026, RF-027, RF-028 |
| UC-17 | Ver Dashboard del Negocio | Dueño de Negocio | RF-029 |
| UC-18 | Exportar Reporte de Citas | Dueño de Negocio | RF-030 |
| UC-19 | Administrar Tenants | Super Admin | RF-005, RF-006 |
| UC-20 | Consultar Disponibilidad por Chat | Cliente Final | RF-031 |
| UC-21 | Recibir Recomendación de Profesional | Cliente Final | RF-032, RF-033 |
| UC-22 | Completar Reserva Guiada por Chat | Cliente Final | RF-035 |
| UC-23 | Responder Preguntas Frecuentes del Negocio | Cliente Final | RF-036, RF-037 |

## UC-01 — Registrar Usuario

**Objetivo:**  Permitir que una persona cree una cuenta en la plataforma. **Actor:**  Dueño de Negocio (auto-registro) o Staff invitado. El Cliente Final no tiene cuenta en el MVP (RN-019, SUP-011). **Precondiciones:**  El correo electrónico no debe estar previamente registrado en el sistema.

**Flujo Principal**

1. El usuario accede al formulario de registro.
2. El usuario ingresa nombre, email y contraseña.
3. El sistema valida el formato de los datos.
4. El sistema verifica que el correo no esté registrado.
5. El sistema crea la cuenta con estado "activa" y rol Dueño de Negocio en el auto-registro, o Staff cuando proviene de una invitación (RN-019).
6. El sistema confirma el registro exitoso.

**Flujos Alternativos**

* **A1:**  El usuario se registra a través de una invitación de staff (ver UC-04). El rol se asigna automáticamente como Staff y el negocio queda preasociado.

**Manejo de Errores**

* **E1:**  El correo ya existe → el sistema rechaza el registro e indica que ya existe una cuenta con ese correo.
* **E2:**  La contraseña no cumple la política mínima de seguridad (RN-018: al menos 10 caracteres, no común ni solo numérica) → el sistema solicita corrección.

**Postcondiciones:**  Existe una cuenta de usuario activa, con rol asignado, lista para iniciar sesión.

## UC-02 — Iniciar Sesión

**Objetivo:**  Autenticar a un usuario y otorgarle acceso según su rol. **Actor:**  Cualquier usuario registrado. **Precondiciones:**  El usuario debe tener una cuenta activa (UC-01 completado).

**Flujo Principal**

1. El usuario ingresa email y contraseña.
2. El sistema valida las credenciales.
3. El sistema genera un token de sesión asociado al usuario, su rol y su tenant (si aplica).
4. El sistema redirige al panel correspondiente según el rol del usuario.

**Flujos Alternativos**

* **A1:**  El usuario es Super Admin → se redirige al panel de administración de tenants (no a un panel de negocio).

**Manejo de Errores**

* **E1:**  Credenciales inválidas → el sistema rechaza el acceso sin especificar si el error es el email o la contraseña (buena práctica de seguridad).
* **E2:**  Cuenta desactivada por el Dueño de Negocio, o cuenta de un tenant desactivado por el Super Admin (RN-020) → el sistema informa que la cuenta no está disponible.

**Postcondiciones:**  El usuario cuenta con una sesión activa y acceso a las funcionalidades permitidas por su rol.

## UC-03 — Registrar Negocio (Onboarding)

**Objetivo:**  Dar de alta un nuevo tenant en la plataforma y preconfigurarlo según su rubro. **Actor:**  Dueño de Negocio. **Precondiciones:**  El usuario debe tener una cuenta creada (UC-01) y sesión iniciada (UC-02). Un Dueño puede existir sin negocio hasta completar este caso de uso, y cada Dueño registra un solo negocio (RN-019).

**Flujo Principal**

1. El usuario inicia el asistente de registro de negocio.
2. El usuario ingresa nombre del negocio, rubro (vertical) y datos de contacto (correo y teléfono; la dirección es opcional en el registro y se completa en UC-05).
3. El sistema crea el tenant y lo asocia al usuario como Dueño de Negocio.
4. El sistema preconfigura servicios y recursos por defecto según el rubro seleccionado (ver RN-007). Las plantillas iniciales están en `06-modelo-dominio.md` §3.5; la aplicación de la plantilla se completa en el Sprint 2, cuando existe el módulo Catalog (US-005).
5. El sistema presenta el panel del negocio con los datos preconfigurados, listos para editar.

**Flujos Alternativos**

* **A1:**  El usuario decide omitir la preconfiguración sugerida y partir con el negocio vacío.

**Manejo de Errores**

* **E1:**  El rubro seleccionado no tiene plantilla definida → el sistema crea el tenant sin preconfiguración y lo notifica.

**Postcondiciones:**  Existe un tenant activo, asociado a un Dueño de Negocio, con o sin datos preconfigurados según el rubro.

## UC-04 — Gestionar Staff

**Objetivo:**  Permitir al Dueño de Negocio incorporar y administrar cuentas de su personal. **Actor:**  Dueño de Negocio. **Precondiciones:**  El tenant debe existir (UC-03 completado).

**Flujo Principal**

1. El Dueño de Negocio ingresa el correo de la persona a invitar.
2. El sistema envía una invitación por correo con un enlace de registro (ver UC-01, flujo A1). El enlace lleva un token firmado, de un solo uso, que vence a los 7 días (RN-019). En desarrollo el correo se emite por consola hasta contar con el adaptador real de Notification.
3. La persona invitada completa su registro y queda asociada como Staff del tenant.
4. El Dueño de Negocio visualiza la lista de staff y puede activar/desactivar cuentas.

**Flujos Alternativos**

* **A1:**  El Dueño de Negocio desactiva a un miembro del staff sin eliminarlo, preservando el historial de reservas atendidas por esa persona.

**Manejo de Errores**

* **E1:**  El correo invitado ya pertenece a otro tenant como Dueño de Negocio → el sistema rechaza la invitación e informa el conflicto.

**Postcondiciones:**  La cuenta de staff queda activa y asociada al tenant, o desactivada según la acción realizada.

## UC-05 — Editar Datos del Negocio

**Objetivo:**  Mantener actualizada la información general del tenant. **Actor:**  Dueño de Negocio. **Precondiciones:**  El tenant debe existir.

**Flujo Principal**

1. El Dueño de Negocio accede a la configuración general del negocio.
2. Edita nombre, dirección, horario general de atención y/o el identificador público (slug) de la página de reservas; al cambiar el slug el sistema advierte que los enlaces ya compartidos dejarán de funcionar (RN-016).
3. El sistema guarda los cambios y los refleja de inmediato en la página pública de reservas.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  Datos incompletos o con formato inválido (ej. dirección vacía) → el sistema rechaza el guardado hasta corregir.

**Postcondiciones:**  Los datos generales del negocio quedan actualizados y visibles en la página pública.

## UC-06 — Gestionar Catálogo de Servicios

**Objetivo:**  Permitir al Dueño de Negocio definir los servicios que ofrece. **Actor:**  Dueño de Negocio. **Precondiciones:**  El tenant debe existir.

**Flujo Principal**

1. El Dueño de Negocio crea un servicio indicando nombre, duración y precio.
2. El sistema valida los datos y guarda el servicio como parte del catálogo del tenant.
3. El Dueño de Negocio puede editar o eliminar servicios existentes.

**Flujos Alternativos**

* **A1:**  El servicio se marca como "inactivo" en lugar de eliminarse, si ya tiene reservas históricas asociadas.

**Manejo de Errores**

* **E1:**  Duración del servicio igual o menor a cero → el sistema rechaza el valor.
* **E2:**  Se intenta eliminar un servicio con reservas futuras activas → el sistema bloquea la eliminación y sugiere desactivarlo.

**Postcondiciones:**  El catálogo de servicios del tenant queda actualizado.

## UC-07 — Gestionar Recursos

**Objetivo:**  Permitir al Dueño de Negocio definir los recursos con los que presta sus servicios (profesionales, salas, equipos) y asociarlos a servicios. **Actor:**  Dueño de Negocio. **Precondiciones:**  Debe existir al menos un servicio creado (UC-06).

**Flujo Principal**

1. El Dueño de Negocio crea un recurso, indicando su tipo (profesional, sala o equipo) y nombre.
2. El sistema guarda el recurso asociado al tenant.
3. El Dueño de Negocio asocia el recurso a uno o más servicios del catálogo.

**Flujos Alternativos**

* **A1:**  Un servicio requiere más de un recurso simultáneo (ej. sala + equipo + profesional). El sistema permite asociar múltiples recursos a un mismo servicio (recurso compuesto).

**Manejo de Errores**

* **E1:**  Se intenta asociar un recurso de otro tenant → el sistema rechaza la operación (ver RN-004).

**Postcondiciones:**  Los recursos quedan creados y asociados a los servicios correspondientes.

## UC-08 — Configurar Disponibilidad de Recurso

**Objetivo:**  Definir cuándo un recurso puede ser reservado. **Actor:**  Dueño de Negocio o Staff (según permisos configurados). **Precondiciones:**  El recurso debe existir (UC-07).

**Flujo Principal**

1. El usuario define un horario semanal recurrente para el recurso (ej. lunes a viernes 9:00–18:00).
2. El sistema guarda la configuración de disponibilidad base.
3. El usuario puede agregar excepciones puntuales (bloqueos, ausencias, feriados).
4. El sistema excluye esos bloques puntuales del cálculo de disponibilidad.

**Flujos Alternativos**

* **A1:**  El recurso no tiene disponibilidad configurada aún → el sistema lo marca como "no reservable" hasta que se configure.

**Manejo de Errores**

* **E1:**  El rango horario ingresado es inválido (hora de fin anterior a hora de inicio) → el sistema rechaza el guardado.

**Postcondiciones:**  El recurso cuenta con una disponibilidad calculable, usada por el motor de reservas (UC-10, UC-11).

## UC-09 — Configurar Servicio Grupal

**Objetivo:**  Permitir servicios donde varios clientes reservan el mismo bloque horario (ej. clases grupales). **Actor:**  Dueño de Negocio. **Precondiciones:**  El servicio debe existir (UC-06) y estar marcado como grupal.

**Flujo Principal**

1. El Dueño de Negocio marca un servicio como "grupal" y define su cupo máximo.
2. El sistema aplica la validación de cupo (RN-006) en lugar de la exclusividad 1:1 estándar (RN-002).

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  Cupo máximo igual o menor a cero → el sistema rechaza el valor.

**Postcondiciones:**  El servicio queda habilitado para aceptar múltiples reservas simultáneas hasta su cupo máximo.

## UC-10 — Consultar Disponibilidad de Horarios

**Objetivo:**  Permitir al cliente final ver los horarios disponibles de un servicio antes de reservar. **Actor:**  Cliente Final. **Precondiciones:**  El servicio y sus recursos deben tener disponibilidad configurada (UC-08).

**Flujo Principal**

1. El cliente accede a la página pública del negocio.
2. Selecciona un servicio.
3. El sistema calcula y muestra los horarios disponibles según la disponibilidad de los recursos asociados y las reservas ya existentes.

**Flujos Alternativos**

* **A1:**  El servicio es grupal → el sistema muestra los bloques con cupos aún disponibles, indicando cuántos lugares quedan.

**Manejo de Errores**

* **E1:**  El servicio no tiene ningún recurso con disponibilidad → el sistema informa que no hay horarios disponibles en el rango consultado.

**Postcondiciones:**  El cliente visualiza un listado de horarios reservables, sin efectos sobre el estado del sistema.

## UC-11 — Crear Reserva

**Caso de uso crítico del sistema.**

**Objetivo:**  Permitir que un cliente final agende una cita. **Actor:**  Cliente Final. **Precondiciones:**  El cliente debe haber consultado disponibilidad (UC-10) y seleccionado un horario válido.

**Flujo Principal**

1. El cliente selecciona un horario disponible y confirma la reserva.
2. El sistema valida nuevamente que el horario siga disponible (control de concurrencia).
3. El sistema crea la reserva y le asigna un identificador único de confirmación.
4. El sistema bloquea el horario correspondiente en el recurso asociado.
5. El sistema dispara el evento de notificación de confirmación (UC-16).
6. El sistema muestra al cliente la confirmación con el identificador de reserva.

**Flujos Alternativos**

* **A1:**  El servicio requiere más de un recurso (compuesto) → el sistema valida y bloquea la disponibilidad de todos los recursos involucrados de forma atómica.

**Manejo de Errores**

* **E1:**  El horario fue tomado por otra persona entre la consulta (UC-10) y la confirmación → el sistema rechaza la reserva e informa que el horario ya no está disponible, sugiriendo refrescar los horarios.
* **E2:**  El servicio es grupal y el cupo ya se completó → el sistema rechaza la reserva indicando cupo lleno.

**Postcondiciones:**  Existe una reserva confirmada, el horario queda bloqueado para nuevas reservas, y se ha disparado la notificación de confirmación.

## UC-12 — Ver Agenda de Citas

**Objetivo:**  Permitir al staff o dueño de negocio visualizar sus citas programadas. **Actor:**  Staff / Dueño de Negocio. **Precondiciones:**  Debe existir sesión iniciada con rol Staff o Dueño de Negocio.

**Flujo Principal**

1. El usuario accede a la vista de agenda.
2. Selecciona el rango a visualizar (día o semana).
3. El sistema muestra las reservas correspondientes a los recursos que el usuario puede ver.

**Flujos Alternativos**

* **A1:**  El Dueño de Negocio visualiza la agenda de todos los recursos del tenant; el Staff visualiza únicamente la de los recursos que tiene asignados, es decir, el recurso vinculado a su cuenta (RN-017).

**Manejo de Errores:**  No aplica (operación de solo lectura).

**Postcondiciones:**  El usuario visualiza correctamente su agenda, sin efectos sobre el estado del sistema.

## UC-13 — Modificar Reserva

**Objetivo:**  Permitir a un staff reprogramar una cita existente. **Actor:**  Staff. **Precondiciones:**  La reserva debe existir y estar en estado "confirmada".

**Flujo Principal**

1. El staff selecciona la reserva a modificar.
2. Ingresa un nuevo horario y/o recurso.
3. El sistema valida disponibilidad del nuevo horario (igual que en UC-11).
4. El sistema libera el bloque anterior y bloquea el nuevo.
5. El sistema notifica el cambio al cliente final.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  El nuevo horario no está disponible → el sistema rechaza el cambio y mantiene la reserva original.

**Postcondiciones:**  La reserva queda actualizada con el nuevo horario/recurso, y el cliente ha sido notificado.

## UC-14 — Cancelar Reserva (Staff)

**Objetivo:**  Permitir al staff o dueño de negocio cancelar una cita. **Actor:**  Staff / Dueño de Negocio. **Precondiciones:**  La reserva debe existir y estar en estado "confirmada".

**Flujo Principal**

1. El usuario selecciona la reserva y confirma la cancelación.
2. El sistema cambia el estado de la reserva a "cancelada".
3. El sistema libera automáticamente el bloque de tiempo del recurso (RN-008).
4. El sistema notifica la cancelación al cliente final.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  La reserva ya estaba cancelada o completada → el sistema informa que la operación no es válida en el estado actual.

**Postcondiciones:**  La reserva queda cancelada y el horario liberado para nuevas reservas.

## UC-15 — Cancelar Reserva (Cliente Final)

**Objetivo:**  Permitir al cliente final cancelar su propia reserva sin intervención del negocio. **Actor:**  Cliente Final. **Precondiciones:**  El cliente debe contar con el enlace único enviado en el correo de confirmación (RF-026).

**Flujo Principal**

1. El cliente accede al enlace único de su reserva.
2. El sistema valida que el enlace corresponda a una reserva vigente y no cancelada.
3. El cliente confirma la cancelación.
4. El sistema cambia el estado de la reserva a "cancelada" y libera el bloque de tiempo.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  El enlace ya fue usado o la reserva ya fue cancelada previamente → el sistema informa que la operación ya no es válida.
* **E2:**  El enlace no corresponde a ninguna reserva existente → el sistema informa error genérico sin revelar información sensible (RN-009).

**Postcondiciones:**  La reserva queda cancelada y el horario liberado.

## UC-16 — Notificar Evento de Reserva

**Objetivo:**  Enviar comunicaciones automáticas asociadas al ciclo de vida de una reserva. **Actor:**  Sistema (disparado por UC-11, UC-13, UC-14, UC-15, y por un job programado). **Precondiciones:**  Debe existir un evento de reserva válido (creación, modificación, cancelación, o recordatorio próximo a vencer).

**Flujo Principal**

1. El sistema detecta un evento relevante (reserva creada, modificada, cancelada, o recordatorio 24h antes).
2. El sistema construye el mensaje de correo correspondiente.
3. El sistema envía el correo al destinatario (cliente final y/o negocio, según el evento).

**Flujos Alternativos**

* **A1:**  Evento de recordatorio (RF-027): se dispara mediante un proceso programado (job) que revisa reservas próximas a las 24 horas, no por una acción directa de usuario.

**Manejo de Errores**

* **E1:**  El proveedor de correo (AWS SES) no está disponible → el sistema registra el fallo en el log y reintenta según política de reintentos definida en Etapa 4.

**Postcondiciones:**  El destinatario recibe la notificación correspondiente, o el fallo queda registrado para su revisión.

## UC-17 — Ver Dashboard del Negocio

**Objetivo:**  Dar visibilidad rápida al Dueño de Negocio sobre el estado operativo de su negocio. **Actor:**  Dueño de Negocio. **Precondiciones:**  Debe existir al menos una reserva registrada para mostrar métricas relevantes.

**Flujo Principal**

1. El Dueño de Negocio accede al dashboard.
2. El sistema calcula y muestra: citas del día, citas de la semana y tasa de ocupación de recursos.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores:**  No aplica (operación de solo lectura).

**Postcondiciones:**  El usuario visualiza el estado operativo actualizado del negocio.

## UC-18 — Exportar Reporte de Citas

**Objetivo:**  Permitir al Dueño de Negocio obtener un respaldo de sus citas del mes. **Actor:**  Dueño de Negocio. **Precondiciones:**  Debe existir al menos una reserva en el mes consultado.

**Flujo Principal**

1. El Dueño de Negocio selecciona el mes a exportar.
2. El sistema genera el archivo (CSV o PDF) con el detalle de citas del período.
3. El sistema entrega el archivo para descarga.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  No existen citas en el período seleccionado → el sistema informa que no hay datos para exportar.

**Postcondiciones:**  El usuario obtiene un archivo descargable con el reporte solicitado.

## UC-19 — Administrar Tenants

**Objetivo:**  Permitir al Super Admin supervisar y controlar el estado de los negocios registrados en la plataforma. **Actor:**  Super Admin. **Precondiciones:**  Sesión iniciada con rol Super Admin.

**Flujo Principal**

1. El Super Admin accede al listado de tenants.
2. Visualiza metadatos administrativos de cada tenant (estado, fecha de alta, plan).
3. Puede activar o desactivar un tenant.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  Se intenta desactivar un tenant ya desactivado → el sistema informa que la operación no aplica.

**Postcondiciones:**  El estado del tenant queda actualizado y el cambio se registra en el log estructurado. Si el tenant queda desactivado, sus usuarios no pueden iniciar sesión y su página pública deja de estar disponible (RN-020). El Super Admin no accede en ningún momento a datos operativos del tenant (RN-010).

## UC-20 — Consultar Disponibilidad por Chat _(nuevo)_

**Objetivo:**  Permitir al cliente final consultar disponibilidad de un servicio conversando en lenguaje natural con el asistente. **Actor:**  Cliente Final. **Precondiciones:**  El servicio y sus recursos deben tener disponibilidad configurada (UC-08). El asistente está disponible (RNF-018).

**Flujo Principal**

1. El cliente escribe una consulta en lenguaje natural (ej. "¿tienen hora para corte mañana en la tarde?").
2. El asistente interpreta la intención y los parámetros relevantes (servicio, fecha/rango).
3. El asistente invoca el mismo servicio de aplicación que usa UC-10 (`CalculadorDisponibilidadService`, vía el puerto correspondiente); no reimplementa el cálculo de disponibilidad.
4. El asistente presenta los horarios disponibles en formato conversacional.

**Flujos Alternativos**

* **A1:**  El cliente no especifica un servicio → el asistente pregunta cuál servicio le interesa antes de continuar.
* **A2:**  El servicio es grupal → el asistente indica también cupos disponibles por bloque (igual que UC-10, A1).

**Manejo de Errores**

* **E1:**  El proveedor de LLM no está disponible → el asistente informa que no puede procesar la consulta por el chat en este momento y sugiere usar el flujo web tradicional (RNF-018).
* **E2:**  No hay horarios disponibles en el rango consultado → el asistente lo informa y sugiere ampliar el rango de búsqueda.

**Postcondiciones:**  El cliente recibe un listado de horarios disponibles en la conversación, sin efectos sobre el estado del sistema.

## UC-21 — Recibir Recomendación de Profesional _(nuevo)_

**Objetivo:**  Permitir que el asistente recomiende el profesional mejor calificado disponible, para que el cliente elija más rápido cuando hay varias opciones. **Actor:**  Cliente Final. **Precondiciones:**  Debe haberse ejecutado UC-20 con más de un recurso disponible para el servicio y horario solicitados.

**Flujo Principal**

1. El asistente identifica, entre los recursos disponibles, cuáles tienen calificación asignada (RF-032).
2. El asistente ordena las opciones de mayor a menor calificación (RN-012).
3. El asistente presenta como primera opción el recurso mejor calificado disponible.

**Flujos Alternativos**

* **A1:**  Ninguno de los recursos disponibles tiene calificación asignada → el asistente presenta las opciones disponibles sin orden de recomendación explícito, indicando que no hay diferenciación por calificación.

**Manejo de Errores**

* **E1:**  Solo existe un recurso disponible → el asistente lo presenta directamente, sin necesidad de recomendación comparativa.

**Postcondiciones:**  El cliente recibe una recomendación priorizada, sin efectos sobre el estado del sistema.

## UC-22 — Completar Reserva Guiada por Chat _(nuevo)_

**Caso de uso crítico del Epic 7:**  equivalente conversacional de UC-11.

**Objetivo:**  Permitir que el cliente final complete toda su reserva conversando con el asistente, sin salir del chat. **Actor:**  Cliente Final. **Precondiciones:**  El cliente ha consultado disponibilidad (UC-20) y, opcionalmente, recibido una recomendación (UC-21).

**Flujo Principal**

1. El cliente confirma, dentro de la conversación, el servicio, recurso y horario deseados.
2. El asistente recolecta los datos mínimos requeridos del cliente (RN-014), los mismos que exige el flujo web (RF-019).
3. El asistente invoca el mismo `CrearReservaService` que usa UC-11; no tiene ninguna vía alterna para saltarse las validaciones (RN-013).
4. El sistema aplica las mismas validaciones de UC-11 (RN-001, RN-002, RN-006).
5. El sistema crea la reserva, genera el identificador único de confirmación y dispara la notificación (UC-16).
6. El asistente confirma la reserva al cliente dentro de la misma conversación.

**Flujos Alternativos**

* **A1:**  El servicio requiere más de un recurso (compuesto) → igual que UC-11, A1: el asistente recolecta y confirma todos los recursos involucrados antes de invocar la creación.

**Manejo de Errores**

* **E1:**  El horario fue tomado por otra persona entre la consulta y la confirmación → el asistente informa que el horario ya no está disponible y ofrece volver a consultar disponibilidad (igual que UC-11, E1).
* **E2:**  El servicio es grupal y el cupo ya se completó → el asistente lo informa, igual que UC-11, E2.
* **E3:**  El proveedor de LLM falla a mitad de la conversación → el asistente informa que no puede continuar por chat y dirige al cliente al flujo web tradicional, sin dejar la reserva en estado parcial (RNF-018).

**Postcondiciones:**  Existe una reserva confirmada bajo las mismas garantías que UC-11, y la interacción queda registrada en el historial de conversación (US-028).

## UC-23 — Responder Preguntas Frecuentes del Negocio _(nuevo)_

**Objetivo:**  Permitir que el asistente responda preguntas frecuentes del cliente sobre el negocio (horario, ubicación, políticas), para resolver dudas sin llamar. **Actor:**  Cliente Final. **Precondiciones:**  El Dueño de Negocio debe haber configurado previamente el contenido de preguntas frecuentes (RF-036), almacenado como parte del contexto del asistente asociado al Tenant (ver `contextoAsistente` en `06-modelo-dominio.md`).

**Flujo Principal**

1. El cliente realiza una pregunta sobre el negocio dentro de la conversación.
2. El asistente busca la respuesta dentro del contenido configurado por el negocio.
3. El asistente responde con la información configurada.

**Flujos Alternativos:**  No aplica.

**Manejo de Errores**

* **E1:**  El negocio no configuró información relevante a la pregunta → el asistente admite explícitamente que no dispone de esa información, en lugar de inventar una respuesta (RF-037).

**Postcondiciones:**  El cliente recibe una respuesta basada exclusivamente en información configurada por el negocio, sin efectos sobre el estado del sistema.

## 2. Listado de Diagramas UML a Construir

Se construirán formalmente en las etapas indicadas; este es el plan de documentación gráfica del proyecto.

| # | Diagrama | Tipo | Propósito | Etapa de construcción |
| --- | --- | --- | --- | --- |
| 1 | Diagrama de Casos de Uso (general) | UML — Casos de Uso | Vista consolidada de los 23 UC y sus actores | Etapa 2 (Arquitectura) |
| 2 | Diagrama de Casos de Uso por Actor | UML — Casos de Uso | Vistas segmentadas: Cliente Final, Staff, Dueño de Negocio, Super Admin | Etapa 2 |
| 3 | Diagrama de Clases (Modelo de Dominio) | UML — Clases | Entidades del dominio y sus relaciones (Tenant, Recurso, Servicio, Reserva, Usuario) | Etapa 3 (Modelo de Datos) |
| 4 | Diagrama de Secuencia — Crear Reserva (UC-11) | UML — Secuencia | Detallar el control de concurrencia y bloqueo de recursos | Etapa 4 (Diseño Backend) |
| 5 | Diagrama de Secuencia — Autenticación (UC-02) | UML — Secuencia | Flujo de login, generación y validación de token | Etapa 4 |
| 6 | Diagrama de Secuencia — Cancelación por Cliente (UC-15) | UML — Secuencia | Validación de enlace único y liberación de recurso | Etapa 4 |
| 7 | Diagrama de Estados — Ciclo de vida de una Reserva | UML — Estados | Estados: Pendiente → Confirmada → Cancelada / Completada / No-show | Etapa 3 |
| 8 | Diagrama de Actividades — Onboarding de Negocio (UC-03) | UML — Actividades | Flujo completo del asistente de configuración por rubro | Etapa 2 |
| 9 | Diagrama de Actividades — Flujo de Reserva end-to-end (UC-10 a UC-11) | UML — Actividades | Desde consulta de disponibilidad hasta confirmación | Etapa 2 |
| 10 | Diagrama de Componentes — Monolito Modular | UML — Componentes | Módulos internos del backend y sus dependencias (bounded contexts) | Etapa 2 |
| 11 | Diagrama de Despliegue (Deployment) | UML — Despliegue | Distribución de contenedores Docker sobre infraestructura AWS | Etapa 6 (Infraestructura) |
| 12 | Diagrama Entidad-Relación (complementario, no-UML) | ER | Modelo físico de base de datos PostgreSQL | Etapa 3 |
| 13 | Diagrama C4 — Contexto | C4 (complementario, no-UML puro) | Vista de más alto nivel: sistema y sus usuarios/sistemas externos | Etapa 2 |
| 14 | Diagrama C4 — Contenedores | C4 (complementario) | Frontend, Backend, Base de Datos y sus interacciones | Etapa 2 |
| 15 | Diagrama de Secuencia — Reserva Guiada por Chat (UC-22) | UML — Secuencia | Interacción Cliente ↔ Asistente ↔ Application Services de Booking/Catalog, mostrando que el LLM nunca accede directo a datos | Etapa 4 |

## 3. Cierre de esta actividad

### Objetivos cumplidos

* 23 casos de uso completamente especificados (objetivo, actor, precondiciones, flujo principal, flujos alternativos, errores, postcondiciones), incorporando UC-20 a UC-23 del Asistente Conversacional.
* Trazabilidad completa hacia los 37 RF del documento de requerimientos.
* Plan de 15 diagramas UML/complementarios, con etapa de construcción asignada a cada uno.

### Entregables

* `04-casos-de-uso.md` (v2.0)

### Documentación generada

Lista para el capítulo de "Análisis y Diseño — Casos de Uso" de la memoria.

### Próximos pasos

El análisis funcional detallado queda cerrado, incluyendo el Epic 7. Toca actualizar formalmente la **Etapa 2 — Arquitectura de Software**  (`05-arquitectura-software.md`) para incorporar un séptimo módulo (Assistant) al monolito modular, y redactar el ADR correspondiente a la integración del proveedor de LLM (puerto/adaptador, consistente con RN-013).

_Documento vivo — Etapa 1 (Discovery & Análisis de Negocio), cierre de análisis funcional._

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 2.0 | 2026-08-02 | Agrega UC-20 a UC-23 (Asistente Conversacional) | Equipo del proyecto |
| 2.1 | 2026-09-24 | UC-01 (actor y política de contraseña), UC-03 (plantillas), UC-04 (token de invitación), UC-05 (slug) y UC-12 (vínculo usuario-recurso) alineados a RN-016 a RN-019 | Alberto Rincón |
| 2.2 | 2026-09-24 | UC-02 (E2 por tenant desactivado), UC-03 (Dueño sin negocio, un negocio por Dueño, contacto) y UC-19 (efecto de desactivar un tenant) alineados a RN-019 y RN-020 | Alberto Rincón |
