> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/13828110) · versión 7 · última edición 2026-10-14

# Fase 2 (continuación) — Antes de la Etapa 9

| Campo | Detalle |
| --- | --- |
| **Fase** | 2 (continuación) — Antes de la Etapa 9 |
| **Versión** | 2.6 — Etapa 6 (AWS) descartada, confirmado por el profesor guía (2026-10-14); v2.5: pruebas del frontend y proxy de desarrollo |
| **Rol aplicado** | DevOps Engineer |
| **Archivo fuente** | `docs/11-entorno-desarrollo.md` |
| **Estado** | Documento vivo |

**Objetivo:** dejar el entorno local 100% listo para que el equipo empiece a escribir código en la Etapa 9. Este documento no contiene lógica de negocio, solo configuración.

**Estado del entorno (2026-09-24):** el entorno está implementado y verificado en el repositorio (`docker-compose.yml`, `backend/`, `frontend/`, `infra/`, `.env.example`, `README.md`). Todo corre en Docker: Python 3.12, Poetry y Node 20 viven dentro de las imágenes, por lo que **no es obligatorio instalarlos en el equipo**; las secciones 1 a 5 describen la instalación local solo como alternativa.

| Servicio | Puerto en el equipo | Verificación |
| --- | --- | --- |
| Frontend (Angular 18) | 4200 (`FRONTEND_HOST_PORT`) | http://localhost:4200 |
| Backend (Django REST) | 8000 (`BACKEND_HOST_PORT`; en equipos con el puerto ocupado, ej. 8001) | `/api/health/` responde `{"status":"ok","database":"ok"}`; Swagger en `/api/docs/` |
| PostgreSQL 16 | 5433 (`POSTGRES_HOST_PORT`); 5432 dentro de Docker | Extensiones `pgcrypto` y `btree_gist` instaladas por `infra/docker/init-postgres.sql` |

Comandos: `docker compose up -d --build` (levantar), `docker compose exec backend pytest` (pruebas), `docker compose exec backend lint-imports` (reglas de arquitectura), `docker compose exec backend ruff check .` (lint), `docker compose --profile test run --rm frontend-test` (pruebas del frontend con Chromium headless). El servidor de Angular reenvía `/api` al backend (`frontend/proxy.conf.json`), así que en el navegador se usa siempre http://localhost:4200, sin depender del puerto del backend.

**Notas de implementación:** (1) el frontend usa `npm install` en el Dockerfile, porque `npm ci` falla con npm 10.8 sobre este árbol de dependencias; el `package-lock.json` se versiona igualmente. (2) La autenticación JWT se activa en US-001, cuando se define el modelo de usuario propio; hasta entonces todo endpoint niega el acceso por defecto. (3) Los puertos del equipo son configurables porque 5432 y 8000 suelen estar ocupados por otros proyectos.

## 1. Requisitos y versiones

| Herramienta | Versión requerida | Por qué esta versión |
| --- | --- | --- |
| Python | 3.12 | Última versión estable compatible con Django 5.x y todas las librerías del stack (ver `docs/08-estructura-backend.md`) |
| Poetry | 1.8+ | Gestión de dependencias con lockfile reproducible (equivalente a lo que Maven daba en la versión Java) |
| Node.js | 20 (LTS) | Requerido por Angular 18+ (sin cambios respecto a la versión anterior) |
| Angular CLI | 18+ | Sin cambios: el frontend no se ve afectado por ADR-004 |
| Docker Desktop | Última estable | Requisito de RNF-013 |
| PostgreSQL | 16 (vía Docker únicamente) | Sin cambios (ver Sección 5) |
| Git | Última estable | — |
| VS Code | Última estable | — |

### Instalación recomendada

| Herramienta | Método |
| --- | --- |
| Python | `pyenv` (`pyenv install 3.12 && pyenv local 3.12`) en macOS/Linux; instalador oficial de [python.org](http://python.org) en Windows |
| Poetry | Instalador oficial, no vía `pip install poetry` global (ver comando abajo) |
| Node | Sin cambios: `nvm install 20 && nvm use 20` |

```
curl -sSL https://install.python-poetry.org | python3 -
```

## 2. VS Code

### 2.1 Extensiones recomendadas

Se definen en `.vscode/extensions.json` en la raíz del repo.

| Área | Extensiones |
| --- | --- |
| Python | `ms-python.python`, `ms-python.vscode-pylance`, `charliermarsh.ruff` (lint + formato en una extensión) |
| Django | `batisteo.vscode-django` (resaltado de sintaxis de templates/ORM) |
| Angular | Sin cambios: `angular.ng-template`, ESLint, Prettier |
| Docker | Sin cambios: `ms-azuretools.vscode-docker` |
| PostgreSQL | Sin cambios: `ms-ossdata.vscode-pgsql` |
| Git/GitHub | Sin cambios: GitLens, Pull Requests |

### 2.2 `.vscode/settings.json` actualizado

Se retiran las claves específicas de Java (`java.*`) y se agregan:

```
"[python]": {
  "editor.tabSize": 4,
  "editor.defaultFormatter": "charliermarsh.ruff",
  "editor.codeActionsOnSave": { "source.organizeImports": "explicit" }
},
"python.testing.pytestEnabled": true
```

## 3. Inicialización del Backend (Django REST Framework)

No se escribe `pyproject.toml` a mano: se inicializa con Poetry y se agregan las dependencias del stack definido en `docs/08-estructura-backend.md`.

```
mkdir backend && cd backend
poetry init --name reservaspro-backend --python "^3.12" --no-interaction
poetry add django djangorestframework djangorestframework-simplejwt \
  psycopg[binary] django-cors-headers python-dotenv drf-spectacular
poetry add --group dev pytest pytest-django pytest-asyncio ruff mypy \
  import-linter testcontainers[postgres]
poetry run django-admin startproject config .
```

### Dependencias y justificación

| Dependencia | Justificación |
| --- | --- |
| `django` + `djangorestframework` | Framework elegido en ADR-004 |
| `djangorestframework-simplejwt` | Autenticación JWT (Etapa 4, Sección 5) |
| `psycopg[binary]` | Driver PostgreSQL moderno (v3) |
| `django-cors-headers` | Habilitar origen del frontend Angular |
| `drf-spectacular` | Documentación OpenAPI/Swagger automática (equivalente a `springdoc`) |
| `python-dotenv` | Carga de variables desde `.env` |
| `import-linter` | Enforcement de la regla de dependencia de Clean Architecture (ADR-004) |
| `pytest` + `pytest-django` | Testing (se detalla en Etapa 8) |
| `testcontainers[postgres]` | Pruebas de integración contra PostgreSQL real, igual que se haría con el binding Java |

### Creación de las apps

Después de generar el proyecto, crear las 7 apps + shared kernel siguiendo el árbol diseñado en `docs/08-estructura-backend.md`:

```
mkdir apps && cd apps
for app in shared iam tenant catalog booking notification reporting assistant; do
  poetry run python ../manage.py startapp $app
done
```

Requiere ajustar `INSTALLED_APPS` en `config/settings/base.py` apuntando a `apps.<nombre>`. Es un detalle de implementación, no de este documento de entorno.

## 4. Inicialización del Frontend (Angular)

Sin cambios respecto a la versión anterior: ADR-004 no afecta al frontend.

- Se mantienen los mismos comandos de Angular CLI: `ng new frontend --standalone --routing --style=scss --skip-git`
- Se mantiene la misma estructura de `core/`, `shared/`, `layouts/`, `features/` de `docs/09-estructura-frontend.md`.

## 5. PostgreSQL — solo vía Docker

Sin cambios: sigue siendo exclusivamente vía el contenedor de `docker-compose.yml`, con `pgcrypto` y `btree_gist` preinstaladas por `infra/docker/init-postgres.sql`.

## 6. Variables de Entorno

`.env.example` actualizado: se retiran las variables específicas de Spring (`JWT_SECRET` se mantiene, ahora consumida por `djangorestframework-simplejwt` en vez de `jjwt`) y se agrega:

```
DJANGO_SETTINGS_MODULE=config.settings.docker
DJANGO_SECRET_KEY=cambiar-por-un-secreto-real-de-desarrollo
```

Generar `DJANGO_SECRET_KEY` con:

```
poetry run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 6.1 Variables del Asistente Conversacional (nuevo en v2.1 — Epic 7)

```
LLM_PROVIDER=gemini
LLM_API_KEY=por_definir
LLM_REQUEST_TIMEOUT_SECONDS=5
```

| Variable | Valor | Observación |
| --- | --- | --- |
| `LLM_PROVIDER` | `gemini` | Resuelto el 2026-09-23 (RES-006/DEP-009); modelo recomendado: Gemini Flash |
| `LLM_API_KEY` | `por_definir` | Nunca commitear con un valor real |
| `LLM_REQUEST_TIMEOUT_SECONDS` | `5` | Consistente con RNF-017 (respuesta del asistente en menos de 5 s p95) |

**`LLM_PROVIDER` se resolvió el 2026-09-23: Google Gemini.** El presupuesto (RES-006, ~10 USD/mes) lo financia personalmente Alberto Rincón, no una partida institucional. Se recomienda el modelo **Gemini Flash** por costo, dado que el catálogo de herramientas del asistente es deliberadamente pequeño (RN-013) y no requiere la capacidad de un modelo más grande. La clave (`LLM_API_KEY`) se obtiene desde Google AI Studio y nunca debe commitearse con un valor real.

`LLM_API_KEY` nunca debe commitearse con un valor real. Solo existe en `.env` local (ya excluido en `.gitignore`) y, en producción, como secreto gestionado en AWS (a definir en Etapa 6).

**`LLM_REQUEST_TIMEOUT_SECONDS=5`:** un timeout mayor a ese umbral no tendría sentido, porque para cuando expirara ya se habría incumplido el requerimiento no funcional RNF-017.

## 7. Docker Compose — Levantar el entorno completo

El servicio `backend` de `docker-compose.yml` se actualiza:

- Cambia el `Dockerfile.dev` (Python en vez de JDK/Maven).
- Cambia el puerto expuesto (Django corre en 8000, no 8080).
- Cambia la variable de perfil (`DJANGO_SETTINGS_MODULE` en vez de `SPRING_PROFILES_ACTIVE`).

```
docker compose up -d postgres backend frontend
```

| Servicio | Puerto local | Descripción |
| --- | --- | --- |
| `postgres` | 5433 (5432 dentro de Docker) | Configurable con `POSTGRES_HOST_PORT` |
| `backend` | 8000 (configurable con `BACKEND_HOST_PORT`) | Django con `runserver`, recarga automática, código montado como volumen |
| `frontend` | 4200 | Sin cambios |
| `pgadmin` (opcional) | 5050 | Sin cambios |

## 8. Git / GitHub

Sin cambios respecto a la versión anterior.

## 9. Checklist de Verificación del Entorno (actualizado)

- [ ] `python --version` → muestra 3.12.x
- [ ] `poetry --version` → responde sin error
- [ ] `node -v` → muestra 20.x
- [ ] `docker -v` y `docker compose version` → responden sin error
- [ ] `git --version` → responde sin error
- [ ] `docker compose up -d postgres` → contenedor `reservaspro-postgres` queda `healthy`
- [ ] Conexión de prueba: `docker exec -it reservaspro-postgres psql -U reservaspro -d reservaspro -c "SELECT 1;"` → responde `1`
- [ ] `docker compose up -d backend` → responde en `http://localhost:8000`
- [ ] VS Code, al abrir la carpeta del repo, ofrece instalar las extensiones recomendadas (ahora con Python en vez de Java)

## 10. Cierre de esta actividad

### Objetivos cumplidos

- Entorno local rediseñado íntegramente para Python/Django: Poetry, apps de Django, PostgreSQL sin cambios, Docker Compose actualizado y VS Code con extensiones Python.
- Se preservan exactamente los mismos principios de reproducibilidad que la versión Java.
- **Nuevo en v2.1:** variables de entorno del proveedor de LLM agregadas a `.env.example`, con el nombre del proveedor marcado explícitamente como decisión pendiente (no oculta como si ya estuviera resuelta).

### Entregables

- Este documento (`docs/11-entorno-desarrollo.md`, v2.1).
- Scaffold físico del repositorio actualizado (fuera de este documento).

### Próximos pasos

Con `docs/08` y `docs/11` actualizados para el Epic 7, sigue pendiente:

Con el calendario vigente (2026-09-24), el CI y la estrategia de calidad se ejecutan como Tasks dentro del Sprint 1 (24 sep–11 oct); AWS y el despliegue quedan fuera de alcance (RES-009):

1. Etapa 6 (Infraestructura AWS): **descartada** — el profesor guía confirmó (2026-10-14) que no se requiere desplegar; `LLM_API_KEY` se mantiene solo en `.env` local (`.gitignore`), sin necesidad de resolver su gestión en un entorno de producción que no existirá.
2. Etapa 7 (CI/CD): el CI (build, pruebas, lint, `import-linter`) es Task del Sprint 1, ya implementado (CAPDC-39); no hay etapa de despliegue.
3. Etapa 8 (Estrategia de Calidad): Task del Sprint 1, ya implementada (CAPDC-40, ver `03-3`).

*Documento vivo — Fase 2 (Preparación del Entorno de Desarrollo), v2.1.*

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 2.1 | — | Variables de entorno del proveedor LLM (Epic 7) | Equipo del proyecto |
| 2.2 | 2026-09-23 | `LLM_PROVIDER=gemini` | Alberto Rincón |
| 2.3 | 2026-09-23 | Próximos pasos: Etapas 6, 7 y 8 se ejecutan como Tasks dentro del Sprint 1 (calendario reprogramado) | Alberto Rincón |
| 2.4 | 2026-09-24 | Entorno implementado en Docker (PostgreSQL, Django, Angular); puertos configurables; 7 apps incluyendo `assistant`; AWS y despliegue diferidos; CI y calidad como Tasks del Sprint 1 | Alberto Rincón |
| 2.5 | 2026-09-24 | Comando de pruebas del frontend (servicio `frontend-test`) y proxy de desarrollo `/api` | Alberto Rincón |
| 2.6 | 2026-10-14 | Etapa 6 (Infraestructura AWS) descartada: el profesor guía confirmó que no se requiere desplegar; `LLM_API_KEY` se mantiene solo en `.env` local | Alberto Rincón |
