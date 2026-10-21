# Evidencias de documentación: Expertia

**Expertia** es una plataforma SaaS de reservas y citas para negocios de servicios, como peluquerías, clínicas y gimnasios. Es el proyecto APT de la asignatura Capstone, carrera de Ingeniería en Informática, Duoc UC.

**Equipo:** Maximiliano Díaz · Genesis Cáceres · Alberto Rincón
**Profesor guía:** Félix Cifuentes

En esta carpeta están las evidencias de cómo documentamos y gestionamos el proyecto. Usamos dos herramientas de Atlassian:

| Herramienta | Para qué la usamos | Sitio original |
| --- | --- | --- |
| **Confluence** | Documentación técnica y funcional: acta, benchmark, requerimientos, casos de uso, arquitectura, modelo de datos, diseño de backend y frontend, entorno, calidad y registro de cambios | [Espacio EXPERTIA-CAP26](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA) |
| **Jira** | Gestión ágil (Scrum): backlog, épicas, historias de usuario con criterios de aceptación, story points, prioridad MoSCoW y sprints | [Proyecto CAPDC](https://maximilianodiazprofesional.atlassian.net/jira/software/projects/CAPDC/boards) |
| **GitHub** | Solo código fuente, Pull Requests e integración continua. Cada commit y PR lleva la clave de Jira (ej. `CAPDC-8`) | Repositorio del proyecto |

> Los sitios de Atlassian requieren acceso. Por eso el contenido completo también está exportado aquí en Markdown, para revisarlo directamente en GitHub.

## Contenido

```
01-evidencias-documentacion/
├── README.md                ← este archivo
├── confluence/              ← las 15 páginas del espacio, exportadas a Markdown
│   ├── README.md            ← índice con versión, fecha y enlace a cada página original
│   ├── 00-contexto-general.md
│   ├── 01-discovery-y-analisis-de-negocio/
│   ├── 02-arquitectura-y-diseno/
│   ├── 03-preparacion-del-repositorio/
│   └── 04-registro-de-cambios.md
├── jira/                    ← exportación del proyecto CAPDC (49 incidencias)
│   ├── README.md            ← resumen por sprint y por épica
│   ├── backlog.md / .csv    ← backlog completo
│   └── issues/              ← una ficha por incidencia, con criterios de aceptación y comentarios
└── capturas/                ← pantallazos de Jira y Confluence
```

## Por dónde empezar

1. **[Contexto general](confluence/00-contexto-general.md):** el problema, la propuesta de valor y el alcance del MVP.
2. **[Índice de Confluence](confluence/README.md):** toda la documentación, ordenada por etapa.
3. **[Resumen de Jira](jira/README.md):** cómo se planificó y cómo avanza cada sprint.
4. **[Registro de cambios](confluence/04-registro-de-cambios.md):** las decisiones y ajustes del proyecto, en orden cronológico.

## Trazabilidad

```
Historia de usuario (Jira, US-XXX = CAPDC-N)
  → Requerimiento funcional (SRS, RF-XXX)
    → Caso de uso (UC-XX)
      → Módulo de la arquitectura (bounded context)
        → Commit / Pull Request en GitHub (con la clave CAPDC-N)
```

---
*Exportado el 20 de octubre de 2026. La versión vigente de cada documento es la de Confluence y Jira.*
