> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13729795) · versión 7 · última edición 2026-10-14

# EXPERTIA — Contexto General del Proyecto de Título

**Business Management Platform — Plataforma SaaS de Reservas y Citas**

| Campo | Información |
| --- | --- |
| **Versión** | 1.4 — el profesor guía confirma que no se requiere despliegue en AWS, basta un video de la demo (2026-10-14); v1.3: estrategia del asistente con Gemini, riesgos, ADR y SP conciliados |
| **Estado** | Vigente |
| **Última actualización** | 2026-09-24 |

# 1. Identificación del Proyecto

| Campo | Detalle |
| --- | --- |
| **Nombre del producto** | EXPERTIA |
| **Tipo** | Plataforma SaaS multi-tenant de reservas y gestión |
| **Carrera** | Ingeniería en Informática — Duoc UC |
| **Integrantes** | Maximiliano Díaz · Genesis Cáceres · Alberto Rincón |
| **Profesor guía** | Félix Cifuentes |
| **Tamaño del equipo** | 3 personas |

# 2. Visión del Producto

**EXPERTIA**  es una plataforma SaaS multi-tenant de reservas y citas, diseñada para ser **genérica, simple de configurar y adaptable a distintos tipos de negocios de servicios** .

La solución está orientada a negocios como:

* Salones de belleza y peluquerías.
* Clínicas y consultorios.
* Gimnasios y centros deportivos.
* Otros negocios que requieren gestionar servicios, profesionales, recursos y reservas.

El proyecto considera como referentes del mercado soluciones como:

* AgendaPro.
* Calendly.
* [http://SimplyBook.me](http://SimplyBook.me) .
* Booksy.
* Fresha.

El objetivo no es replicar estas plataformas, sino identificar necesidades comunes y diseñar una solución académica que priorice **simplicidad de configuración, transparencia y capacidad de adaptación a diferentes modelos de negocio** .

# 3. El Problema

La gestión manual o poco integrada de reservas puede generar diferentes dificultades operativas para los negocios de servicios.

Entre los principales problemas identificados se encuentran:

* **Pérdida de clientes:**  dificultades para gestionar solicitudes y reservas oportunamente.
* **Errores en la agenda:**  conflictos de horarios, disponibilidad y asignación de recursos.
* **Ausencia de visibilidad operativa:**  dificultad para conocer el estado de las reservas y el funcionamiento general del negocio.

Estos problemas afectan especialmente a negocios pequeños y medianos que necesitan administrar sus agendas sin incorporar soluciones excesivamente complejas.

# 4. Objetivo del Proyecto

Desarrollar una **plataforma SaaS de reservas y citas** , simple de configurar y adaptable a distintos tipos de negocios de servicios.

La solución deberá permitir que un negocio pueda configurar sus servicios, recursos, disponibilidad y reglas de reserva sin requerir conocimientos técnicos especializados.

El proyecto busca demostrar que un núcleo común puede utilizarse para diferentes modelos de negocio mediante una arquitectura suficientemente flexible, pero manteniendo un alcance controlado para el contexto del proyecto de título.

# 5. Análisis Competitivo

Como parte del análisis inicial se identificaron distintas características y oportunidades asociadas a soluciones existentes en el mercado.

| Competidor | Aspecto identificado |
| --- | --- |
| **AgendaPro** | Se identifican percepciones de aumento de costos y experiencias variables respecto a la estabilidad de la aplicación. |
| **Calendly** | Está principalmente orientado a coordinación de reuniones y no cubre de forma general la gestión de recursos físicos. |
| [http://SimplyBook.me](http://SimplyBook.me) | Presenta un amplio conjunto de configuraciones y funcionalidades, lo que puede aumentar la complejidad inicial para determinados usuarios. |
| **Booksy** | Su orientación principal está relacionada con determinados negocios de servicios y presenta limitaciones para otros contextos, como escenarios de salud regulada. |
| **Fresha** | Su modelo comercial incorpora mecanismos asociados a transacciones y servicios adicionales que deben ser considerados por los negocios. |

### Oportunidad identificada

A partir de la revisión inicial se identifica una oportunidad conceptual en la combinación de tres características:

**Genericidad + Simplicidad + Transparencia de costos**

EXPERTIA busca utilizar estos tres conceptos como principios de diseño del producto.

**Nota:**  Las afirmaciones competitivas deberán ser validadas y respaldadas mediante fuentes durante la etapa de Discovery, antes de utilizarlas como conclusiones definitivas en la documentación académica.

# 6. Propuesta de Valor — Objetivos Específicos

Los diferenciadores de EXPERTIA se expresan en tres objetivos específicos:

## 6.1 Gestión de Jira y Confluence

Administración, organización y optimización de herramientas para la gestión del proyecto.

## 6.2 Diseñar un modelo de negocio genérico

Resolver distintos escenarios: **profesional individual, recursos compuestos y servicios grupales** , mediante el modelo genérico Servicio ↔ Recurso (ver Sección 8).

## 6.3 Incorporar IA al agendamiento

Reserva mediante lenguaje natural, permitiendo consultar disponibilidad, recomendar y completar una reserva por la plataforma (ver Sección 9).

**Nota de actualización (v1.1, 2026-09-23):**  esta sección reemplaza los "Tres Pilares" anteriores (Simplicidad, Transparencia y Arquitectura Evolutiva) por los tres objetivos específicos definidos en la presentación del proyecto (diapositiva "Objetivos Específicos"). La arquitectura de Monolito Modular + Bounded Contexts sigue vigente y se documenta en la Sección 10.1; simplicidad y transparencia se mantienen como principios de diseño en las Secciones 2 y 5.

# 7. Alcance del MVP

## 7.1 Módulos — Bounded Contexts

El MVP contempla inicialmente **7 módulos principales** .

| Módulo | Responsabilidad |
| --- | --- |
| **IAM** | Autenticación, autorización y gestión de roles. |
| **Tenant** | Gestión del negocio y configuración del tenant. |
| **Catalog** | Gestión de servicios, recursos y modelo genérico de operación. |
| **Booking** | Motor de reservas y núcleo transaccional del sistema. |
| **Notification** | Comunicación y notificaciones dirigidas a clientes y usuarios. |
| **Reporting** | Dashboard y reportes operativos del negocio. |
| **Asistente IA** | Asistente de agendamiento en lenguaje natural. Módulo transversal que interactúa principalmente con Booking, Catalog y Reporting. |

## 7.2 Verticales Piloto

La solución será validada inicialmente mediante dos verticales:

1. **Salón de belleza / peluquería**
2. **Clínica / consultorio médico**

Estas verticales permitirán comprobar si el modelo genérico puede representar diferentes escenarios de negocio sin requerir modificaciones estructurales significativas.

## 7.3 Funcionalidades Fuera de Alcance

Las siguientes funcionalidades no forman parte del MVP:

* Pagos en línea.
* Marketplace público.
* Aplicación móvil nativa.
* Integraciones externas complejas no necesarias para validar el MVP.
* Chatbot como reemplazo de soporte humano.

El asistente virtual tendrá como objetivo apoyar el proceso de reserva y consulta, pero **no reemplazará la atención humana ni los canales de soporte del negocio** .

# 8. Diferenciador Técnico — Modelo Genérico Servicio ↔ Recurso

Uno de los principales desafíos técnicos de EXPERTIA consiste en representar diferentes modelos de negocio mediante un **modelo de datos común** .

La relación:

**Servicio ↔ Recurso**

permitirá representar distintos escenarios sin construir una solución independiente para cada rubro.

## 8.1 Escenario 1 — Profesional Individual

**Ejemplo:**  peluquería / barbería / spa.

Un servicio puede requerir un único profesional como recurso.

```
Servicio
   │
   └── Profesional
```

Ejemplo:

Corte de cabello → Profesional Juan

## 8.2 Escenario 2 — Recurso Compuesto

**Ejemplo:**  clínica / consultorio.

Un servicio puede requerir la combinación de diferentes recursos.

```
Servicio
   │
   ├── Sala
   ├── Equipo
   └── Profesional
```

Ejemplo:

Consulta médica → Box 02 + Equipo médico + Profesional

## 8.3 Escenario 3 — Servicio Grupal

**Ejemplo:**  gimnasio / clases.

Un servicio puede admitir múltiples reservas hasta alcanzar una capacidad máxima.

```
Servicio
   │
   └── Cupo máximo
          │
          ├── Reserva 1
          ├── Reserva 2
          ├── Reserva 3
          └── ...
```

Ejemplo:

Clase de spinning → máximo 15 participantes.

### Objetivo del modelo

El modelo busca permitir que estos tres escenarios sean representados mediante una estructura común, evitando crear reglas rígidas específicas para cada vertical.

# 9. Innovación — Asistente Virtual de Agendamiento

EXPERTIA contempla un asistente virtual orientado a facilitar el proceso de reserva.

El objetivo es permitir que el cliente pueda interactuar mediante **lenguaje natural** , reduciendo la necesidad de navegar manualmente por múltiples pantallas.

## 9.1 Flujo Conceptual

```
Consulta del cliente
        ↓
Interpretación de intención
        ↓
Consulta de módulos
        ↓
Validación de disponibilidad
        ↓
Respuesta
        ↓
Reserva
```

El asistente deberá interactuar principalmente con los módulos:

* Booking.
* Catalog.
* Reporting.

## 9.2 Capacidades Esperadas

El asistente deberá contemplar inicialmente:

* Consultas de disponibilidad mediante lenguaje natural.
* Identificación de servicios.
* Consulta de profesionales disponibles.
* Recomendación de profesionales según criterios definidos.
* Orientación durante el proceso de reserva.
* Confirmación de una reserva.
* Respuestas a preguntas frecuentes del negocio.

## 9.3 Estrategia de Implementación

El asistente del MVP se implementa con un **modelo de lenguaje (LLM) de Google Gemini** (variante Flash), usando invocación de herramientas (tool/function calling):

* El LLM solo puede invocar un catálogo cerrado de herramientas, que son envoltorios delgados sobre los Application Services existentes de Catalog y Booking (RN-013, ADR-005). Nunca accede directo a la base de datos ni a los repositorios.
* La integración se aísla tras un puerto/adaptador (`LlmProviderPort`), de modo que cambiar de proveedor no afecta a los demás módulos.
* Si el proveedor no está disponible, el asistente degrada de forma controlada y el flujo web de reserva sigue operando (RNF-018).
* El acceso al asistente está condicionado al plan PRO del tenant (RN-015), lo que acota el consumo del presupuesto.
* Presupuesto de referencia: \~10 USD/mes, financiado personalmente por Alberto Rincón (RES-006).

**Nota de actualización (v1.3, 2026-09-24):**  esta sección reemplaza la estrategia anterior (chatbot basado en reglas en el MVP y LLM como Fase 2 posterior a la defensa). La decisión de incorporar el LLM en el MVP se tomó el 2026-09-23 y está reflejada en el Backlog (Epic 7), el SRS (RES-006, DEP-009, SUP-008/009, RN-015) y la arquitectura (ADR-005).

# 10. Arquitectura de Software

## 10.1 Patrón Arquitectónico

La solución utilizará inicialmente un:

**Monolito Modular con Bounded Contexts y comunicación controlada.**

El diseño estará preparado para permitir una eventual evolución hacia una arquitectura de microservicios.

```
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│     IAM      │  │    Tenant    │  │   Catalog    │
└──────────────┘  └──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   Booking    │  │ Notification │  │  Reporting   │
└──────────────┘  └──────────────┘  └──────────────┘

┌────────────────────────────────────────────────────┐
│              Asistente IA                         │
│              Módulo transversal                    │
└────────────────────────────────────────────────────┘
```

## 10.2 Stack Tecnológico

| Capa | Tecnología |
| --- | --- |
| **Frontend** | Angular — SPA responsiva |
| **Backend** | Django REST Framework |
| **Base de datos** | PostgreSQL — AWS RDS |
| **Contenedores** | Docker |
| **Cloud** | No aplica — el profesor guía confirmó que no se requiere despliegue (2026-10-14); la entrega se demuestra con un video del sistema corriendo en contenedores locales (ver RES-009) |
| **Control de versiones** | GitHub |
| **CI/CD** | GitHub Actions |

**Nota de consistencia:**  El Project Charter inicial contemplaba Spring Boot como tecnología backend. La decisión de usar **Django REST Framework**  quedó formalizada en el ADR-004 (`02-4-diseno-de-estructura-backend.md` §0), y los documentos vigentes ya la reflejan.

# 11. Plan de Trabajo — 4 Sprints

La implementación se organizará en cuatro sprints principales.

| Sprint | Contenido |
| --- | --- |
| **Sprint 1 — Fundacional** (24 sep–11 oct) | IAM + Tenant + preparación y CI (AWS diferido) |
| **Sprint 2 — Catálogo** (12–25 oct) | Catalog + modelo genérico Servicio ↔ Recurso + onboarding por rubro (US-005) |
| **Sprint 3 — Reservas + IA** (26 oct–8 nov) | Booking + motor de reservas + Asistente IA completo (Epic 7, LLM Google Gemini) |
| **Sprint 4 — Cierre** (9–14 nov) | Notification + Reporting + QA integral |

**Nota de actualización (v1.1, 2026-09-23):**  el plan de 4 sprints es el plan aprobado y vigente; sustituye al plan de 5 sprints propuesto en el Backlog v2.0 / `03-1` v2.0 (Sprint 5 dedicado al asistente). Todo el Epic 7 (US-022 a US-028) se ejecuta dentro del Sprint 3, junto con Booking. Dentro del sprint, Booking va primero y el asistente después, porque el asistente depende de Booking y Catalog ya construidos (RN-013). Se recupera además la Etapa 10 (Cierre, Pruebas Finales y Documentación, 15–21 nov) como semana propia, sin consumirla como Sprint 5.

**Nota de actualización (v1.3, 2026-09-24):**  el Sprint 1 inicia el jue 24 sep (no pudo iniciarse el 23). AWS y el despliegue quedan diferidos hasta que el profesor guía confirme (RES-009). US-005 (onboarding por rubro) pasa al Sprint 2, porque depende de Catalog. Detalle en `03-1-configuracion-de-jira-y-github.md` §3.

## 11.1 Métricas de Planificación

| Métrica | Valor |
| --- | --- |
| **Story Points** | 131 SP Must-have (168 en total) |
| **Plazo de implementación** | \~7,5 semanas (24 sep–14 nov; plan original: 4 semanas) |
| **Equipo** | 3 integrantes |
| **Alcance obligatorio** | Incluye el asistente IA completo (Epic 7, LLM Gemini) en el Sprint 3 |

# 12. Gestión de Riesgos

## 12.1 Riesgo Principal

Se identifica como riesgo principal la carga de **131 Story Points Must-have (168 en total)**  en 4 sprints (24 sep–14 nov) con un equipo de 3 integrantes. El Sprint 3 concentra Booking y todo el Epic 7 (76 SP en dos semanas), por lo que es el punto más exigente del plan. Requiere mantener un control estricto del alcance.

## 12.2 Estrategias de Mitigación

### Plan B — Recorte controlado de alcance

Si a mitad del Sprint 3 o al cierre del Sprint 2 la velocidad real no proyecta completar Booking y el Epic 7: recortar el Epic 6 completo (Panel de Administración) y degradar US-011 (servicios grupales) a "documentado, no implementado". Regla: **nunca recortar el Epic 7** ; el asistente es parte del MVP a defender.

### Adelantar trabajo sin dependencias

Con la capacidad que libera el aplazamiento de AWS, se puede adelantar trabajo que no depende de otros módulos (por ejemplo US-008, o US-024 y US-026 del Epic 7), registrando el cambio en Jira.

### Riesgos del proveedor de LLM

Costo acotado por el plan PRO y por un tope de mensajes por tenant/día; degradación controlada ante caída del proveedor (RNF-018).

## 12.3 Mitigación Primaria

Mantener el orden de dependencias (Booking antes del asistente dentro del Sprint 3) y usar la Etapa 10 (15–21 nov) como contingencia antes de recurrir al Plan B.

## 12.4 Mitigación Secundaria

En caso de requerirse una reducción de alcance, los primeros candidatos a revisión serán:

1. **Servicios grupales (US-011).**
2. **Dashboard avanzado / funcionalidades avanzadas de Reporting (Epic 6).**

Estas funcionalidades deberán evaluarse según su impacto en los objetivos principales del MVP antes de ser eliminadas o simplificadas.

# 13. Próximos Pasos

Los siguientes puntos permanecen abiertos y deberán ser abordados durante las siguientes etapas del proyecto:

* Definir criterios de éxito y KPIs para validar el MVP.
* Definir criterios de aceptación de las historias, al planificar cada sprint.
* Definir el diseño de las reservas grupales (restricción `EXCLUDE`) antes del Sprint 3 (`02-3` §4.9).
* Definir los montos concretos de los planes Básico y Pro.
* \~\~Confirmar con el profesor guía si el despliegue en AWS se realiza tras la entrega de noviembre\~\~ **Confirmado (2026-10-14): no se requiere despliegue; la entrega se presenta con un video de la demo.** Sigue pendiente comunicarle la conciliación de story points (131 Must / 168 en total).
* Validar y documentar los supuestos del análisis competitivo.
* Validar el alcance final de cada sprint.

# 14. Decisiones Técnicas (ADR)

Todas las decisiones de arquitectura están formalizadas:

| ID | Decisión | Estado |
| --- | --- | --- |
| **ADR-001** | Monolito Modular vs. microservicios | Formalizada (`02-1` §1.3) |
| **ADR-002** | Comunicación entre módulos por interfaces síncronas | Formalizada (`02-1` §2.1) |
| **ADR-003** | ECS Fargate vs. EC2 para el cómputo en AWS | Formalizada; el despliegue en AWS está diferido (`02-1` §4.1) |
| **ADR-004** | Framework backend: Django REST Framework | Formalizada (`02-4` §0) |
| **ADR-005** | Integración del asistente vía puerto/adaptador LLM (Google Gemini) | Formalizada (`02-1` §4.2) |

La decisión de alcance multi-rubro con 2 verticales piloto está en el Acta (`01-1` §2), y el modelo genérico Servicio ↔ Recurso en `02-2` §0 y `02-3`; son decisiones de alcance y de modelado, no ADR numerados.

# 15. Estado Actual del Proyecto

**Estado general:**  🟢 **VIGENTE**

EXPERTIA cuenta con una definición inicial de producto, alcance, arquitectura objetivo, módulos principales, estrategia de implementación y planificación de sprints.

La siguiente etapa deberá transformar este contexto en artefactos técnicos y funcionales verificables, especialmente:

* Requisitos.
* Épicas.
* Historias de usuario.
* Modelo de dominio.
* Arquitectura.
* Modelo de datos.
* Contratos entre módulos.
* Backlog priorizado.
* Criterios de aceptación.
* Estrategia de pruebas.
* Plan de implementación.

**Documento vivo:**  Este documento constituye el contexto general vigente de EXPERTIA. Deberá actualizarse cuando una decisión formal de proyecto modifique el alcance, arquitectura, stack tecnológico, funcionalidades del MVP, estrategia de implementación o planificación.

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 1.0 | 2026-09-06 | Versión inicial vigente | Equipo del proyecto |
| 1.1 | 2026-09-23 | Sección 6 reemplazada por los 3 objetivos específicos; Sprint 3 incluye todo el Epic 7 (plan de 4 sprints) | Alberto Rincón |
| 1.2 | 2026-09-23 | Calendario reprogramado: fechas por sprint en §11 y plazo de implementación de \~7,5 semanas | Alberto Rincón |
| 1.3 | 2026-09-24 | Sprint 1 inicia el 2026-09-24; AWS diferido; §9.3 y §12 alineados a Gemini en el MVP y al Plan B; story points conciliados (131 Must / 168); §14 con los ADR ya formalizados; nota de consistencia de Django resuelta | Alberto Rincón |
| 1.4 | 2026-10-14 | El profesor guía confirma que el despliegue en AWS **no se requiere**  para la entrega — la demo final se presenta con un video, no con un sistema desplegado | Alberto Rincón |
