> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13861079) · versión 7 · última edición 2026-10-14

# Project Charter — Plataforma SaaS de Reservas y Citas

**Proyecto de Título — Ingeniería en Informática**

| Campo | Información |
| --- | --- |
| **Versión** | 1.3 — Etapa 6 (AWS) descartada: el profesor guía confirma que no se requiere despliegue, basta un video de la demo (2026-10-14); v1.2: Sprint 1 inicia el 2026-09-24, stack Django |
| **Etapa** | 0 — Kickoff y Alcance |
| **Estado** | Cerrada |
| **Última actualización** | 2026-09-24 |

## 1. Visión del Producto

La solución corresponde a una **plataforma SaaS multi-tenant para la administración de reservas y citas** , orientada a negocios de servicios que requieren gestionar agendas, profesionales, recursos y atención de clientes.

La plataforma estará dirigida inicialmente a distintos tipos de negocios que trabajan con sistemas de agenda, tales como:

* Salones de belleza.
* Clínicas y consultorios.
* Gimnasios.
* Centros de atención y servicios profesionales.
* Otros negocios basados en reservas.

La solución toma como referencia conceptual plataformas existentes de gestión de reservas, como **AgendaPro** , pero busca desarrollar una arquitectura propia orientada al contexto académico y técnico del proyecto de título.

Cada negocio operará como un **tenant independiente** , permitiendo configurar:

* Servicios ofrecidos.
* Profesionales o colaboradores.
* Salas y otros recursos.
* Equipamiento disponible.
* Horarios de atención.
* Disponibilidad de recursos.
* Reglas de reserva.
* Clientes finales.
* Reservas y citas.

Los clientes finales podrán acceder a la plataforma para **consultar disponibilidad y realizar reservas en línea** , mientras que cada negocio contará con herramientas para administrar su operación y agenda.

## 2. Justificación de la Decisión de Alcance: Multi-rubro Genérico

### 2.1 Decisión adoptada

Se establece como decisión de alcance desarrollar un **MVP genérico multi-rubro** , cuya aplicabilidad será validada mediante **dos verticales piloto** , las cuales serán definidas durante la Etapa 1 — Discovery & Análisis de Negocio.

Esta decisión busca equilibrar la **generalización arquitectónica** , el valor académico del proyecto y las restricciones reales de tiempo y recursos disponibles.

### 2.2 Alternativas evaluadas

| Alternativa | Nivel de riesgo | Justificación |
| --- | --- | --- |
| **Un solo rubro específico** | Bajo | Permite controlar fácilmente el alcance, pero presenta menor valor desde el punto de vista de diseño arquitectónico generalizable. |
| **Multi-rubro sin acotar** | Alto | Puede generar un alcance excesivamente amplio y difícil de controlar dentro de las 15 semanas disponibles. |
| **Núcleo genérico + 2 verticales piloto** | Controlado | Permite demostrar capacidad de generalización mediante un núcleo común y validar la solución con casos de uso concretos. |

### 2.3 Decisión final

Se selecciona la alternativa:

**Núcleo genérico + 2 verticales piloto.**

Esta estrategia permite construir una solución reutilizable sin convertir el proyecto en una plataforma excesivamente amplia.

La decisión será formalizada posteriormente mediante el documento **ADR-001 — Decisión de Alcance Multi-rubro** , durante la **Etapa 2 — Arquitectura de Software** .

## 3. Restricciones del Proyecto

| Restricción | Detalle |
| --- | --- |
| **Fecha de inicio** | 10 de agosto de 2026 |
| **Fecha de término** | 21 de noviembre de 2026 |
| **Duración total** | Aproximadamente 15 semanas |
| **Equipo** | 3 integrantes |
| **Stack tecnológico** | Angular, Django REST Framework (ADR-004; la v1.0 de este documento indicaba Spring Boot), PostgreSQL, Docker, GitHub, AWS (despliegue diferido), GitHub Actions |
| **Arquitectura objetivo** | Monolito Modular, preparado para una futura evolución hacia microservicios |

### 3.1 Consideración arquitectónica

La arquitectura inicial será implementada como un **Monolito Modular** , buscando mantener una separación clara entre dominios, responsabilidades y componentes internos.

La solución deberá quedar preparada para una eventual evolución hacia una arquitectura distribuida, sin que dicha evolución sea considerada parte obligatoria del MVP.

El objetivo es evitar una complejidad arquitectónica innecesaria durante el desarrollo, manteniendo al mismo tiempo una base técnica que permita demostrar criterios de diseño y escalabilidad.

## 4. Planificación Temporal por Etapas — Roadmap

| # | Etapa | Duración | Fechas aproximadas | Rol dominante |
| --- | --- | --- | --- | --- |
| **0** | Kickoff y Alcance | 1 semana | 10–14 ago | Product Owner / Technical Lead |
| **1** | Discovery & Análisis de Negocio | 2 semanas | 15–28 ago | Business Analyst / Product Owner |
| **2** | Arquitectura de Software | 1 semana | 29 ago–4 sep | Arquitecto de Software |
| **3** | Modelo de Datos | 1 semana | 5–11 sep | Arquitecto de Base de Datos |
| **4** | Diseño Backend — Django REST Framework | 1 semana | 12–18 sep | Arquitecto Backend |
| **5** | Diseño Frontend — Angular | 1 semana | 19–25 sep | Arquitecto Frontend |
| **6** | Infraestructura AWS | **Descartada** — el profesor guía confirmó que no se requiere despliegue (2026-10-14); la entrega se demuestra con un video | No aplica | Arquitecto AWS |
| **7** | CI/CD | CI dentro del Sprint 1; despliegue diferido junto con AWS | 24 sep–11 oct | DevOps Engineer |
| **8** | Estrategia de Calidad — QA | Definición en Sprint 1; QA integral en Sprint 4 | 24 sep–11 oct y 9–14 nov | QA Engineer |
| **9** | Implementación — Sprints | 4 sprints (\~7,5 semanas) | 24 sep–14 nov | Equipo completo |
| **10** | Cierre, Pruebas Finales y Documentación | 1 semana | 15–21 nov | Equipo completo |

**Calendario reprogramado (2026-09-23 y 2026-09-24):**  el Sprint 1 se adelantó de 17 oct a mié 23 sep y, el 2026-09-24, se movió a **jue 24 sep** porque no pudo iniciarse el día anterior. Se mantiene la fecha de cierre (Sprint 4, sáb 14 nov) y la Etapa 10. La Etapa 6 (AWS) queda descartada y el despliegue de la Etapa 7 no se realiza — el profesor guía confirmó (2026-10-14) que la entrega se demuestra con un video, sin necesidad de desplegar; el CI (Etapa 7) y la definición de la estrategia de calidad (Etapa 8) se ejecutan como Tasks dentro del Sprint 1, y el QA integral en el Sprint 4. La Etapa 5 (Diseño Frontend) se solapa con los primeros días del Sprint 1, pero su documentación ya estaba completa el 19 sep. Fechas originales: Etapa 6 26 sep–2 oct, Etapa 7 3–9 oct, Etapa 8 10–16 oct, Etapa 9 17 oct–14 nov. Detalle de sprints en `03-1-configuracion-de-jira-y-github.md` §3.

### 4.1 Nota de gestión de riesgo

Las **Etapas 0–8** , correspondientes principalmente a definición, análisis y diseño de la solución, se encuentran comprimidas en aproximadamente nueve semanas.

Esta planificación es intencional. En el contexto de un proyecto de título, se considera necesario invertir tiempo suficiente en la definición del problema, arquitectura, modelo de datos, infraestructura, calidad y estrategia de implementación antes de iniciar el desarrollo intensivo.

Por esta razón:

**No se reducirá deliberadamente la fase de diseño para comenzar anticipadamente la programación.**

La intención es disminuir el riesgo de retrabajo, decisiones arquitectónicas improvisadas y cambios estructurales durante la fase de implementación.

## 5. Equipo de Trabajo

El proyecto será desarrollado por un equipo compuesto por **tres integrantes** .

La distribución formal de responsabilidades y roles técnicos será definida durante la **Etapa 1 — Discovery & Análisis de Negocio** .

La asignación deberá considerar tanto las competencias individuales como la necesidad de mantener responsabilidades claramente delimitadas dentro del proyecto.

### Roles técnicos previstos

La estructura de roles podrá considerar responsabilidades como:

* Product Owner.
* Technical Lead.
* Business Analyst.
* Arquitecto de Software.
* Arquitecto Backend.
* Arquitecto Frontend.
* Arquitecto de Base de Datos.
* Arquitecto Cloud / AWS.
* DevOps Engineer.
* QA Engineer.

**Nota:**  La asignación definitiva de estos roles entre los tres integrantes será formalizada durante la Etapa 1.

## 6. Objetivos de la Etapa 0

Los objetivos definidos para la etapa de **Kickoff y Alcance**  fueron completados.

* Definir el alcance general del negocio.
* Establecer el enfoque **multi-rubro genérico** .
* Definir la estrategia de validación mediante **dos verticales piloto** .
* Definir las restricciones temporales y de equipo.
* Establecer el roadmap general del proyecto.
* Definir las principales etapas y sus entregables.
* Justificar la decisión de alcance.
* Establecer la base para el futuro **ADR-001 — Decisión de Alcance Multi-rubro** .

## 7. Entregables de la Etapa

El principal entregable de esta etapa corresponde a:

### Project Charter v1.0

Este documento establece la visión inicial del producto, el alcance general, las restricciones, la estrategia de desarrollo y el roadmap del proyecto.

El Project Charter constituye la línea base inicial para las siguientes etapas del proyecto y será actualizado cuando se produzcan decisiones que modifiquen aspectos relevantes del alcance, planificación o arquitectura.

## 8. Próximos Pasos — Etapa 1: Discovery & Análisis de Negocio

Durante la siguiente etapa se profundizará en la definición funcional y estratégica de la solución.

### 8.1 Definición de verticales piloto

Se deberán seleccionar las dos verticales que serán utilizadas para validar el funcionamiento del núcleo genérico.

Como ejemplos iniciales se consideran:

* Salón de belleza.
* Clínica / consultorio.

La selección definitiva se realizará utilizando criterios de factibilidad, representatividad y capacidad de demostrar la reutilización del modelo de negocio.

### 8.2 Modelo de negocio SaaS

Se deberá definir el modelo comercial conceptual de la plataforma, considerando:

* Planes de servicio.
* Pricing.
* Límites por tenant.
* Cantidad de usuarios.
* Cantidad de profesionales.
* Cantidad de servicios.
* Funcionalidades disponibles por plan.

### 8.3 Definición funcional

Se deberán identificar y priorizar:

* Épicas.
* Historias de usuario.
* Criterios de aceptación.
* Funcionalidades del MVP.
* Funcionalidades fuera de alcance.

La priorización permitirá establecer una línea base funcional para la etapa de implementación.

### 8.4 Actores del sistema

Se deberán formalizar los principales actores de la plataforma:

| Actor | Responsabilidad general |
| --- | --- |
| **Dueño / Administrador del negocio** | Configurar y administrar el tenant. |
| **Staff / Profesional** | Gestionar disponibilidad, agenda y atención de clientes. |
| **Cliente final** | Consultar disponibilidad y realizar reservas. |
| **Super-Administrador de plataforma** | Administrar la plataforma SaaS y sus tenants. |

### 8.5 Distribución de roles técnicos

Se deberá definir la distribución de responsabilidades entre los tres integrantes del equipo, considerando:

* Fortalezas individuales.
* Responsabilidades técnicas.
* Responsabilidades de gestión.
* Cobertura de arquitectura.
* Desarrollo backend.
* Desarrollo frontend.
* Base de datos.
* Cloud / infraestructura.
* DevOps.
* QA.
* Documentación.

## 9. Criterios de Control del Alcance

Para evitar una expansión no controlada del proyecto, las funcionalidades deberán clasificarse según su prioridad y relación con el MVP.

Se utilizarán tres categorías principales:

| Categoría | Descripción |
| --- | --- |
| **MVP** | Funcionalidades necesarias para demostrar el objetivo principal del proyecto. |
| **Post-MVP** | Funcionalidades relevantes que podrán ser consideradas como evolución futura. |
| **Fuera de alcance** | Funcionalidades que no serán desarrolladas durante el proyecto de título. |

Cualquier incorporación significativa que afecte el alcance, arquitectura, tiempo o esfuerzo deberá ser evaluada antes de incorporarse al backlog.

## 10. Principios Iniciales del Proyecto

El desarrollo del proyecto se regirá inicialmente por los siguientes principios:

1. **Alcance controlado:**  evitar funcionalidades que no aporten directamente al objetivo del MVP.
2. **Diseño antes de implementación:**  las decisiones estructurales deberán ser analizadas antes de su implementación.
3. **Arquitectura modular:**  mantener separación clara entre dominios y responsabilidades.
4. **Generalización controlada:**  diseñar un núcleo reutilizable sin intentar cubrir todos los posibles tipos de negocio.
5. **Evidencia técnica:**  las decisiones relevantes deberán quedar respaldadas mediante documentación y artefactos.
6. **Trazabilidad:**  las funcionalidades deberán relacionarse con requisitos, historias de usuario, implementación y pruebas.
7. **Evolución progresiva:**  las funcionalidades y componentes fuera del MVP podrán quedar documentados como evolución futura.
8. **Cloud como objetivo de despliegue:**  AWS será considerado dentro de la estrategia de infraestructura, manteniendo control sobre costos y complejidad.

## 11. Estado de la Etapa 0

**Estado:**  🟢 **CERRADA**

La Etapa 0 establece la línea base inicial del proyecto y proporciona el contexto necesario para iniciar la fase de **Discovery & Análisis de Negocio** .

La siguiente etapa deberá transformar esta visión inicial en una definición más precisa del problema, usuarios, actores, modelo de negocio, requisitos y funcionalidades que conformarán el MVP.

## 12. Historial de Versiones

| Versión | Fecha | Descripción | Responsable |
| --- | --- | --- | --- |
| **1.0** | 2026-08-02 | Creación del Project Charter y cierre de la Etapa 0. | Equipo del proyecto |
| **1.1** | 2026-09-23 | Roadmap reprogramado: inicio adelantado del Sprint 1 (2026-09-23); Etapas 6, 7 y 8 absorbidas en el Sprint 1; Etapa 9 pasa a 23 sep–14 nov; se mantienen el cierre y la Etapa 10. | Alberto Rincón |

**Documento vivo:**  Este documento será actualizado al cierre de cada etapa del proyecto cuando existan cambios relevantes en el alcance, planificación, arquitectura, riesgos o decisiones estratégicas.

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| **1.2** | 2026-09-24 | Sprint 1 inicia el 2026-09-24; stack backend actualizado a Django REST Framework (ADR-004); AWS y despliegue diferidos; CI y estrategia de calidad dentro del Sprint 1. | Alberto Rincón |
| **1.3** | 2026-10-14 | Etapa 6 (Infraestructura AWS) descartada: el profesor guía confirmó que el despliegue no se requiere para la entrega — la demo final se presenta con un video. | Alberto Rincón |
