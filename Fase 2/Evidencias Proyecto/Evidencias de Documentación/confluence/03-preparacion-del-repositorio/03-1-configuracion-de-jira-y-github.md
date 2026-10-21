> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/14057510) · versión 12 · última edición 2026-10-14

# Configuración de Jira y GitHub — Reparto de Responsabilidades y Plan de Sprints

| Campo | Detalle |
| --- | --- |
| **Fase** | 2 — Preparación del Repositorio |
| **Versión** | 3.12 — el profesor guía confirma que no se requiere despliegue en AWS, basta un video de la demo (2026-10-14); v3.11: US-029/CAPDC-49 reincorporada al Sprint 2 |
| **Rol aplicado** | DevOps Engineer / Product Owner |
| **Archivo fuente** | `docs/10-setup-github.md` |
| **Estado** | Documento vivo |

**Nota de actualización (v3.0, 2026-09-23):**  la versión 2.0 definía labels, milestones, GitHub Projects e Issues para gestionar el backlog, y un plan de 5 sprints (Sprint 5 dedicado al asistente). Se reemplaza por (a) el reparto Jira / GitHub siguiente, en línea con el objetivo específico "Gestión de Jira y Confluence" (`00-contexto-general.md` §6.1), y (b) el plan aprobado de **4 sprints**, con todo el Epic 7 (asistente IA) dentro del Sprint 3. El nombre del archivo y de la página de Confluence se mantienen para no romper el índice.

## 1. Reparto de Responsabilidades

| Herramienta | Se usa para | No se usa para |
| --- | --- | --- |
| **Jira** | Backlog, épicas, historias de usuario, criterios de aceptación, story points, priorización MoSCoW, sprints, tablero y seguimiento de avance | Código |
| **GitHub** | Código fuente, ramas, commits, Pull Requests, code review, CI (GitHub Actions) y protección de `main` | Backlog, sprints, Issues, Projects y Milestones |
| **Confluence** | Documentación del proyecto | Seguimiento de tareas |

**Regla:**  no se crean Issues, Projects ni Milestones en GitHub. Todo trabajo planificado vive en Jira; GitHub solo recibe el código que lo implementa.

**Trazabilidad entre herramientas:**  la clave de la issue de Jira (el proyecto Jira tiene la clave `CAPDC`; ej. `CAPDC-12`) se incluye en el título de cada Pull Request y en los mensajes de commit relevantes. Así cada PR se rastrea hasta su historia de usuario, y de ahí al RF, caso de uso y módulo. La integración automática "GitHub for Jira" es opcional y no se requiere para el MVP.

## 2. Jira — Configuración del Proyecto

Proyecto Jira de tipo Scrum. Se mantiene la taxonomía de **3 dimensiones ortogonales**: cada issue recibe un valor de cada dimensión.

### 2.1 Tipo (Issue Type)

| Issue Type | Uso |
| --- | --- |
| Epic | Agrupa las historias de un módulo (ver 2.3) |
| Story | Historia de usuario del backlog (`US-XXX`) |
| Task | Configuración, infraestructura, documentación o trabajo técnico sin historia asociada |
| Bug | Defecto |

### 2.2 Prioridad — labels MoSCoW

| Label | Significado |
| --- | --- |
| `must` | Must have |
| `should` | Should have |
| `could` | Could have |

Se usan labels y no el campo nativo "Priority" de Jira, porque este último tiene una escala distinta (Highest–Lowest) que no equivale a MoSCoW.

### 2.3 Épica — mapea a los 7 módulos de `docs/02-1-arquitectura-de-software-del-sistema.md`

IAM · Tenant · Catalog · **Booking** (dominio núcleo) · Notification · Reporting · **Assistant** (Must-have del MVP).

**Story points:**  campo numérico nativo de Jira ("Story point estimate"), valores 1, 2, 3, 5, 8, 13.

## 3. Jira — Plan de 4 Sprints (aprobado)

| Sprint | Fechas | Contenido | SP (Must) | Objetivo del sprint |
| --- | --- | --- | --- | --- |
| Sprint 1 — Fundacional | jue 24 sep–dom 11 oct (18 días, incluye la preparación) | IAM + Tenant (sin US-005) + preparación y CI (AWS diferido) | 39 (31) | Login funcional, registro de negocio, staff y pipeline de CI operativo en contenedores locales |
| Sprint 2 — Catálogo | **mié 14**–dom 25 oct (11 días efectivos; plan original lun 12–dom 25 oct) | Catalog + modelo genérico Servicio ↔ Recurso + US-005 (onboarding por rubro) + US-029 (landing/demo, fuera del árbol de épicas) | 39 (29) | Servicios y recursos configurables, con disponibilidad, mostrando los 3 escenarios (individual, compuesto, grupal) y onboarding con plantillas por rubro |
| Sprint 3 — Reservas + IA | lun 26 oct–dom 8 nov | Booking + motor de reservas + **todo el Epic 7** (asistente IA con Gemini, US-022 a US-028) | 76 (68) | Flujo completo de reserva pública y reserva conversacional |
| Sprint 4 — Cierre | lun 9–sáb 14 nov | Notification + Reporting + QA integral | 19 (3) | Notificaciones, dashboard, reportes y aseguramiento de calidad antes de la entrega |
| **Total** |  |  | **173 (131)** |  |

La **Etapa 10 — Cierre, Pruebas Finales y Documentación**  (15–21 nov) se mantiene como semana propia, fuera de los sprints.

**Cambios de calendario:**  el 2026-09-23 se adelantó el inicio del Sprint 1 (antes 17 oct) manteniendo el cierre; el 2026-09-24 el inicio se movió de mié 23 sep a **jue 24 sep**, porque el sprint no pudo iniciarse el día anterior. Solo cambian las fechas: la metodología (Scrum), las épicas por sprint, las 28 historias y los objetivos de cada sprint no cambian, salvo el traslado de US-005 descrito abajo. Fechas anteriores: Sprint 1 17–24 oct, Sprint 2 25 oct–1 nov, Sprint 3 2–8 nov.

**Sprint 2 inicia el 2026-10-14 en vez del 12 oct (2026-10-14):**  el cierre del Sprint 1 (Pull Request de `develop` a `main` en revisión) se extendió más allá del 11 oct. Mismo criterio que en el Sprint 1: **se mantiene fijo el cierre del 25 oct** en vez de correr todo el calendario hacia adelante, para no afectar el Sprint 3 ni la fecha de entrega de noviembre. El Sprint 2 queda en 11 días efectivos en vez de 14, con el mismo scope (34 SP / 29 Must). **Riesgo a vigilar:** si a mitad de sprint la velocidad real no proyecta completar el scope en los 11 días, aplicar el mismo tipo de Plan B que ya existe para el Sprint 3 (degradar alcance antes que recortar historias Must, y comunicarlo).

**US-005 pasa del Sprint 1 al Sprint 2 (2026-09-24):**  la elección del rubro ya queda cubierta por US-004 (RF-007 registra nombre, rubro y contacto). US-005 solo *aplica* la plantilla de servicios y recursos del rubro, y esos servicios y recursos pertenecen a Catalog, que se construye en el Sprint 2. Sus 8 SP compensan la capacidad que libera el aplazamiento de AWS. Las plantillas iniciales están definidas en `02-2-modelo-de-dominio-ddd.md` §3.5.

**US-029 (CAPDC-49) se agrega al Sprint 2 (2026-10-14):**  el formulario de demo de 14 días en la landing pública (SUP-010) existía como nota de diseño desde el Sprint 1 (dónde viviría el endpoint y la feature de frontend), pero nunca se había convertido en historia con story points ni sprint asignado — quedó detectado como un hueco de planificación al iniciar el Sprint 2. No tiene épica propia (SUP-010 la define explícitamente fuera del árbol de épicas); se agrega aquí 5 SP (Should) sobre el Sprint 2 ya ajustado a 11 días, lo que aumenta el riesgo de capacidad anotado arriba. **Corrección de clave:** se había registrado primero como CAPDC-43, pero esa clave ya pertenecía al Sprint 0 (§5.5, descubierto al sincronizar este documento con el estado real de Jira); se corrige a CAPDC-49.

**AWS descartado (confirmado 2026-10-14):**  la infraestructura en AWS y el despliegue continuo quedan fuera de lo que se trabaja en estos sprints y de la entrega — el profesor guía confirmó que no se requiere desplegar; la demo final se presenta con un video. El proyecto se desarrolla y demuestra en contenedores locales (RNF-013). El pipeline de CI ejecuta build, pruebas, lint y reglas de arquitectura; sin etapa de despliegue.

**Estrategia de calidad (Etapa 8):**  se define como una Task del Sprint 1 (cobertura mínima de RNF-012, tipos de prueba y umbrales en CI), porque las pruebas se ejecutan en CI desde el primer sprint. La ejecución del QA integral se mantiene en el Sprint 4.

### 3.1 Plan detallado del Sprint 1 (jue 24 sep – dom 11 oct)

**Historias (39 SP):**

| Historia | Épica | SP | Prioridad |
| --- | --- | --- | --- |
| US-001 Registro e inicio de sesión (incluye modelo de usuario propio y activación de JWT) | IAM | 8 | must |
| US-002 Aislamiento de datos entre tenants | IAM | 13 | must |
| US-003 Super Admin: ver y auditar tenants | IAM | 5 | should |
| US-004 Registrar negocio (incluye rubro y slug) | Tenant | 5 | must |
| US-006 Invitar y gestionar staff | Tenant | 5 | must |
| US-007 Editar datos del negocio | Tenant | 3 | should |

**Tasks (sin story points, label **`preparacion`**):**

| Clave | Task | Estado |
| --- | --- | --- |
| CAPDC-36 | Repositorio Git y remoto en GitHub | Listo |
| CAPDC-37 | Entorno local en contenedores (PostgreSQL, Django, Angular) | Listo |
| CAPDC-38 | Crear el proyecto Jira, tablero Scrum y cargar el backlog | Listo |
| CAPDC-39 | Pipeline de CI en GitHub Actions (build, pruebas, `ruff`, `import-linter`) | Por hacer |
| CAPDC-40 | Estrategia de calidad: cobertura mínima, tipos de prueba y umbrales en CI (RNF-012) | Por hacer |
| CAPDC-41 | Esqueleto Angular: `core/`, `shared/`, `layouts/`, `features/`, rutas, guards e interceptors | Por hacer |
| CAPDC-42 | Comando para crear el Super Admin y datos semilla iniciales | Por hacer |

**Registro del 2026-09-24:**  al iniciar el Sprint 1, las tasks CAPDC-36, CAPDC-37 y CAPDC-38 quedaron en "Listo". El objetivo del Sprint 1 en Jira es: "Login funcional, registro de negocio, staff y pipeline de CI operativo en contenedores locales". Los criterios de aceptación de las historias están en `01-3-product-backlog-mvp.md` §13.

**Meta extra (si hay holgura):**  adelantar US-008 (crear y editar servicios, 5 SP), que solo depende de US-004. Si se adelanta, se mueve en Jira al Sprint 1 y se registra en el control de cambios.

**Dependencia entre sprints a vigilar:**  US-016 (cancelar por enlace, Sprint 3) depende de US-017 (correo de confirmación, Sprint 4). En el Sprint 3 el enlace de cancelación se genera y el correo se emite por consola; el envío real llega en el Sprint 4.

### Orden interno del Sprint 3

El asistente depende de que Catalog y Booking estén construidos (RN-013: solo invoca sus Application Services). Por eso, dentro del Sprint 3, Booking se construye primero y el asistente después; las historias del Epic 7 no pueden empezar antes de que el flujo de reserva (US-012) esté funcionando. US-024 (calificación) y US-026 (FAQ) no dependen de Booking y pueden adelantarse a los sprints 1 o 2 si hay holgura.

### Alerta de capacidad y conciliación de story points

| Aspecto | Detalle |
| --- | --- |
| Scope Must-have original | 92 story points contra 4 semanas |
| Scope vigente | **131 SP Must-have, 168 en total** (Backlog `01-3`, historia por historia) |
| Cifra de 104 SP | Corresponde a una estimación previa a incorporar el Epic 7 (`00-contexto-general.md` v1.0 y la presentación). Se reemplaza por las cifras del backlog; la diferencia debe comunicarse al profesor guía |
| Carga del Sprint 3 | Booking (34 SP) + Epic 7 (42 SP) = 76 SP en dos semanas (26 oct–8 nov), el sprint más cargado del plan |
| **Plan B** | Si a mitad del Sprint 3 o al cierre del Sprint 2 la velocidad real no proyecta completar Booking + Epic 7: recortar el Epic 6 completo y degradar US-011 (servicios grupales) a "documentado, no implementado"; usar la Etapa 10 como contingencia |
| Regla | **Nunca recortar el Epic 7 en su lugar** |

## 4. Jira — Tablero

Jira está configurado **en español**. Tablero Scrum del proyecto, con las columnas **Por hacer (To Do) → En curso (In Progress) → En revisión (In Review) → Listo (Done)**. El Backlog es una vista aparte, no una columna del tablero. La columna "En revisión" corresponde a una historia cuyo Pull Request está abierto en GitHub esperando revisión.

| Vista | Propósito |
| --- | --- |
| Tablero del sprint | Seguimiento diario del flujo de trabajo |
| Backlog agrupado por épica, con story points | Verificar el avance de cada módulo |
| Roadmap / línea de tiempo | Épicas sobre los 4 sprints y efecto del Plan B |

## 5. Carga del Backlog en Jira (proyecto CAPDC)

**El backlog no se importó desde el CSV.** El 2026-09-24 se actualizaron directamente las issues que ya existían en el proyecto Jira `CAPDC`, para no duplicarlas. El archivo `docs/jira/backlog-jira.csv` se conserva solo como respaldo de referencia; no se usó para importar.

### 5.1 Épicas (CAPDC-1 a CAPDC-7)

| Clave | Épica | Inicio | Fin | Sprint |
| --- | --- | --- | --- | --- |
| CAPDC-1 | IAM | 2026-09-24 | 2026-10-11 | Sprint 1 |
| CAPDC-2 | Tenant | 2026-09-24 | 2026-10-11 | Sprint 1 (US-005 en Sprint 2) |
| CAPDC-3 | Catalog | 2026-10-14 | 2026-10-25 | Sprint 2 (inicio real 14 oct, no 12; ver §3) |
| CAPDC-4 | Booking | 2026-10-26 | 2026-11-08 | Sprint 3 |
| CAPDC-5 | Notification | 2026-11-09 | 2026-11-14 | Sprint 4 |
| CAPDC-6 | Reporting | 2026-11-09 | 2026-11-14 | Sprint 4 |
| CAPDC-7 | Assistant | 2026-10-26 | 2026-11-08 | Sprint 3 |

### 5.2 Historias (CAPDC-8 a CAPDC-35, y US-029 fuera de esa serie)

Las 28 historias de usuario de `docs/01-3-product-backlog-mvp.md` corresponden a CAPDC-8 a CAPDC-35, en el mismo orden: **US-001 = CAPDC-8, US-002 = CAPDC-9, …, US-028 = CAPDC-35** (clave = número de historia + 7). Cada una tiene el título "US-0XX — …", la descripción del backlog (Como/Quiero/Para, dependencias, RF y casos de uso relacionados), labels MoSCoW + módulo y story points. La tabla completa de correspondencia está en `01-3` §12.

| Historia | Épica | Prioridad | Sprint |
| --- | --- | --- | --- |
| US-001 a US-003 (CAPDC-8 a 10) | IAM | must / should | Sprint 1 |
| US-004, US-006, US-007 (CAPDC-11, 13, 14) | Tenant | must / should | Sprint 1 |
| US-005 (CAPDC-12) | Tenant | must | Sprint 2 (después de Catalog) |
| US-008 a US-011 (CAPDC-15 a 18) | Catalog | must / should | Sprint 2 |
| US-012 a US-016 (CAPDC-19 a 23) | Booking | must / should | Sprint 3 |
| US-017 a US-019 (CAPDC-24 a 26) | Notification | must / should / could | Sprint 4 |
| US-020, US-021 (CAPDC-27, 28) | Reporting | should / could | Sprint 4 |
| US-022 a US-028 (CAPDC-29 a 35) | Assistant | must / should | Sprint 3 (después de Booking) |
| US-029 (CAPDC-49) | — (fuera del árbol de épicas, SUP-010) | should | Sprint 2 |

### 5.3 Tasks de preparación del Sprint 1 (CAPDC-36 a CAPDC-42)

Las siete tasks de la tabla de la sección 3.1, con label `preparacion`, en el mismo orden de esa tabla (CAPDC-36 a CAPDC-42).

**CAPDC-49 (US-029, agregada 2026-10-14):**  Historia tipo `Story`, sin label de épica/módulo (no tiene bounded context propio, ver `01-3` §7.1), label MoSCoW `should`, 5 SP, Sprint 2. Se registró primero por error como CAPDC-43 — rompe la fórmula "clave = número de historia + 7" porque el rango CAPDC-36–42 ya estaba tomado por tasks, y además CAPDC-43 ya pertenecía al Sprint 0 (§5.5), algo que no constaba en este documento al momento de redactarla. Corregida a CAPDC-49, la primera clave libre después del rango del Sprint 0.

### 5.4 Sprints creados en Jira

| Sprint | Fechas | SP | Objetivo |
| --- | --- | --- | --- |
| Sprint 0 inicio/planificación | trabajo previo al 24 sep (cerrado en Jira el 14 oct; ver §5.5) | — | Definir y preparar los elementos iniciales del proyecto antes del desarrollo, incluyendo la propuesta, documentación grupal y mockup funcional |
| Sprint 1 — Fundacional | 24 sep – 11 oct | 39 | Login funcional, registro de negocio, staff y pipeline de CI operativo en contenedores locales |
| Sprint 2 — Catálogo | 14 – 25 oct (inicio real; plan original 12 oct) | 39 (34 Catalog + 5 US-029) | Servicios y recursos configurables, con disponibilidad, mostrando los 3 escenarios (individual, compuesto, grupal) y onboarding con plantillas por rubro |
| Sprint 3 — Reservas + IA | 26 oct – 8 nov | 76 | Flujo completo de reserva pública y reserva conversacional |
| Sprint 4 — Cierre | 9 – 14 nov | 19 | Notificaciones, dashboard, reportes y aseguramiento de calidad antes de la entrega |

### 5.5 Sprint 0 y frente de documentación grupal (CAPDC-43 a CAPDC-48)

**Registro retroactivo (2026-10-14).** El trabajo inicial del proyecto (propuesta, primera entrega de la documentación grupal y mockup funcional) se hizo antes del Sprint 1, pero el Sprint 1 se inició en Jira sin haber iniciado ni completado antes el Sprint 0. Para dejar Jira ordenado, el Sprint 0 se creó y se cerró después, el 2026-10-14, con esas tareas en "Listo". Por eso Jira muestra fechas del 14 al 15 oct, que no corresponden al período real del trabajo; no se corrigen en Jira para no reescribir el historial de un sprint cerrado. El mockup es el mismo que se cita en `02-2` §4.2 (`expertia-mockup_1.3.html`).

| Clave | Tipo | Trabajo | Estado | Ubicación en Jira |
| --- | --- | --- | --- | --- |
| CAPDC-43 | Task | Creación de propuesta del proyecto | Listo | Sprint 0 |
| CAPDC-44 | Épica | Documentación grupal del proyecto | — | Fuera de los sprints de desarrollo |
| CAPDC-45 | Task | Documentación grupal — Entrega 1 | Listo | Sprint 0 (épica CAPDC-44) |
| CAPDC-46 | Task | Documentación grupal — Entrega 2 | Por hacer | Backlog (épica CAPDC-44), fecha objetivo 2026-10-25 |
| CAPDC-47 | Task | Documentación grupal — Entrega 3 | Por hacer | Backlog (épica CAPDC-44), fecha objetivo 2026-11-21 |
| CAPDC-48 | Task | Diseño y creación del mockup funcional | Listo | Sprint 0 |

**Frente de documentación grupal:** las entregas de documentación grupal son entregables académicos, no historias del producto. Se gestionan con la épica CAPDC-44, sin story points y fuera de los sprints de desarrollo, por lo que no cuentan en la velocidad. Sus fechas son **fechas objetivo internas**, alineadas con el calendario: la Entrega 2 con el cierre del Sprint 2 (25 oct) y la Entrega 3 con el cierre de la Etapa 10 — Cierre, Pruebas Finales y Documentación (21 nov). Si la asignatura fija fechas oficiales distintas, estas se reemplazan por las oficiales.

**Sprints auxiliares de Jira:** "Sprint B" (14–20 sep, cerrado y sin actividades) fue un sprint de prueba creado al configurar el tablero; Jira no permite eliminar sprints cerrados, así que se conserva. "Sprint 4 — Cierre 2" (vacío y sin fechas) no forma parte del plan y se elimina.

**Nota sobre CAPDC-49 (2026-10-14):**  este rango (CAPDC-43 a 48) es la razón por la que US-029 (landing/demo de 14 días, `01-3` §7.1) se corrigió de CAPDC-43 a **CAPDC-49**. Al redactar US-029 no se conocía este Sprint 0 retroactivo, así que se le asignó por error la siguiente clave "aparentemente libre" (CAPDC-43), que en realidad ya pertenecía a la propuesta del proyecto. Ver `01-3` §12 y §7.1 para el detalle de la corrección.

**Recomendación operativa:**  el Product Owner interno revisa las issues cargadas antes de avanzar de sprint, para evitar inconsistencias de formato.

## 6. GitHub — Solo Código y Pull Requests

| Elemento | Convención |
| --- | --- |
| Rama principal | `main`, protegida — requiere que los jobs `Backend` y `Frontend` del workflow `CI` estén en verde antes de fusionar un Pull Request (configurar en Settings → Branches → Branch protection rules); refleja el código validado |
| Rama de desarrollo | `develop`: todo el trabajo del sprint se hace directamente aquí, sin una rama por historia (proyecto de una sola persona, decisión 2026-09-25). Cada commit referencia la clave Jira de la historia que avanza (ej. `CAPDC-8 feat: login con JWT`) |
| Integración a `main` | Pull Request de `develop` a `main` en GitHub, con el título con la clave Jira principal del avance. Se asigna como revisor a un compañero del equipo (Collaborator con permiso `Read` o `Write`, agregado en Settings → Collaborators), que prueba el código y deja su revisión (Approve / Request changes); se fusiona cuando el CI está en verde y la revisión está aprobada |
| CI | GitHub Actions (`.github/workflows/ci.yml`, CAPDC-39): job `backend` (build de la imagen Docker, `makemigrations --check`, `ruff`, `import-linter`, `pytest`) y job `frontend` (`ng build`, `ng test` con Chrome headless vía el servicio `frontend-test` ya definido en `docker-compose.yml`). Corre en cada push a `main`/`develop` y en cada Pull Request hacia esas ramas. El despliegue continuo queda diferido junto con AWS |

**Repositorio:**  `https://github.com/AlbertoRSS/expertia.git`. **Privado mientras dura el desarrollo** — corrección del 2026-10-07: la versión anterior de este documento decía "será público", pero esa nota quedó desactualizada frente a la configuración real del repositorio, que ya era privado. El acceso de cada integrante del equipo se da explícitamente como Collaborator. Aun siendo privado, sigue sin deber contener secretos (ver `.gitignore` y `docs/03-2` §6) ni contenido interno de Jira; los PRs referencian solo la clave. Queda abierto evaluar si se vuelve público más adelante (ej. al entregar la tesis), a decidir con el profesor guía.

**Historial de esta decisión (2026-09-25):**  se evaluaron y descartaron las ramas por historia (`feature/CAPDC-N-...`) tras el Sprint 1: con un solo desarrollador no aportaban aislamiento real y sí más pasos para fusionar. `main` y `develop` ya están sincronizadas con GitHub (`origin/main`, `origin/develop`) desde el commit que trae el backend de IAM y el esqueleto Angular.

## 7. Cierre de esta actividad

### Objetivos cumplidos

- Reparto Jira / GitHub / Confluence definido, sin solapamientos.
- Taxonomía de 3 dimensiones trasladada a Jira.
- Plan aprobado de 4 sprints con calendario vigente, plan detallado del Sprint 1 y story points conciliados.
- Mapeo de las 28 historias a épicas, prioridades y sprints, con archivo de importación a Jira.

### Próximos pasos

Las Etapas 6 (Infraestructura AWS) y 7 (CI/CD con despliegue) quedan diferidas; la Etapa 8 (Estrategia de Calidad) y el CI se ejecutan como Tasks dentro del Sprint 1 (24 sep–11 oct).

*Documento vivo — Fase 2 (Preparación del Repositorio).*

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 2.0 | — | Labels, milestones y GitHub Projects; 5 sprints con Sprint 5 (asistente) | Equipo del proyecto |
| 3.0 | 2026-09-23 | Backlog y sprints pasan a Jira; GitHub solo para código y PRs; plan aprobado de 4 sprints con el Epic 7 en el Sprint 3 | Alberto Rincón |
| 3.1 | 2026-09-23 | Calendario reprogramado: Sprint 1 inicia 2026-09-23 (Sprints 1–3 con nuevas fechas); Sprint 4 y Etapa 10 se mantienen; estrategia de calidad como Task del Sprint 1 | Alberto Rincón |
| 3.2 | 2026-09-24 | Sprint 1 inicia el 2026-09-24 (18 días); US-005 pasa al Sprint 2; AWS y despliegue diferidos; plan detallado del Sprint 1; SP conciliados (131 Must / 168); archivo de importación a Jira | Alberto Rincón |
| 3.3 | 2026-09-24 | La clave de ejemplo `EXP` se reemplaza por la clave real del proyecto Jira, `CAPDC` | Alberto Rincón |
| 3.4 | 2026-09-24 | Documento renombrado a "03.1 Configuración de Jira y GitHub" (archivo `03-1-configuracion-de-jira-y-github.md`); backlog cargado en Jira actualizando las issues existentes (épicas CAPDC-1 a 7, historias CAPDC-8 a 35, tasks CAPDC-36 a 42) sin usar el CSV; sprints creados; task del proyecto Jira marcada como hecha | Alberto Rincón |
| 3.5 | 2026-09-24 | Tablero de Jira en español (Por hacer, En curso, En revisión, Listo; el Backlog es una vista aparte); tasks CAPDC-36, 37 y 38 en "Listo"; objetivo del Sprint 1 registrado | Alberto Rincón |
| 3.6 | 2026-09-25 | Flujo de 2 ramas (`main` + `develop`) en vez de una rama por historia; integración por Pull Request de `develop` a `main` | Alberto Rincón |
| 3.7 | 2026-10-07 | Pipeline de CI operativo (`.github/workflows/ci.yml`, CAPDC-39): jobs `backend` y `frontend` sobre la infraestructura Docker ya existente; reglas de protección de `main` concretadas (antes "pendiente de definir") | Alberto Rincón |
| 3.8 | 2026-10-07 | Corrige la nota de v3.0-3.7 ("será público"): el repositorio ya era privado, esa nota estaba desactualizada; el PR de integración a `main` ahora lo revisa y aprueba un compañero del equipo (Collaborator), no solo el autor | Alberto Rincón |
| 3.9 | 2026-10-14 | Sprint 2 inicia el 14 oct en vez del 12 (cierre del Sprint 1 se extendió); se mantiene fijo el cierre del 25 oct (mismo criterio que el Sprint 1), quedando en 11 días efectivos con el mismo scope (34 SP) | Alberto Rincón |
| 3.10 | 2026-10-14 | Nueva §5.5: Sprint 0 documentado como registro retroactivo (CAPDC-43, 45, 48), frente de documentación grupal (épica CAPDC-44, entregas 2 y 3 con fechas objetivo 25 oct y 21 nov) y sprints auxiliares de Jira (Sprint B, Sprint 4 — Cierre 2); Sprint 0 agregado a §5.4 | Alberto Rincón |
| 3.11 | 2026-10-14 | US-029 (landing/demo) reincorporada al Sprint 2 con la clave corregida **CAPDC-49**  (no CAPDC-43, que ya pertenecía al Sprint 0 recién documentado en §5.5); Sprint 2 vuelve a figurar con 39 SP en §3 y §5.4; nota cruzada agregada en §5.5 | Alberto Rincón |
| 3.12 | 2026-10-14 | El profesor guía confirma que el despliegue en AWS **no se requiere**  para la entrega — la demo final se presenta con un video | Alberto Rincón |
