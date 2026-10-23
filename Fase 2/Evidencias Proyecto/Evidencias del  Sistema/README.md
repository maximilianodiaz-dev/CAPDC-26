# EXPERTIA — Arquitectura Frontend y Backend

Este documento resume cómo está organizado el código de **EXPERTIA** y qué archivos sirven como evidencia de cada capa. Son los archivos más representativos, no todos.

> **Capturas de pantalla:** las imágenes de la estructura de carpetas y de cada archivo de evidencia están en el documento de la carpeta **Documentación de sistema**.

## Índice

- [Stack tecnológico](#stack-tecnológico)
- [Estructura general del repositorio](#estructura-general-del-repositorio)
- [Backend (Django + DRF)](#backend-django--drf)
  - [Estructura](#estructura-del-backend)
  - [Patrón en capas por módulo](#patrón-en-capas-por-módulo)
  - [Archivos de evidencia](#archivos-de-evidencia-del-backend)
- [Integración continua y cobertura](#integración-continua-y-cobertura)
- [Frontend (Angular 18)](#frontend-angular-18)
  - [Estructura](#estructura-del-frontend)
  - [Archivos de evidencia](#archivos-de-evidencia-del-frontend)

---

## Stack tecnológico

| Capa | Tecnología |
| --- | --- |
| Frontend | Angular 18 (SPA) |
| Backend | Django + Django REST Framework |
| Pruebas backend | pytest, pytest-django, pytest-cov |
| Pruebas frontend | Jasmine + Karma |
| Calidad de código | ruff, import-linter |
| Contenedores | Docker / Docker Compose |
| CI | GitHub Actions |

---

## Estructura general del repositorio

```text
expertia/
├── .github/
│   └── workflows/
│       └── ci.yml            # Pipeline de integración continua
├── backend/                  # API REST (Django + DRF)
├── frontend/                 # SPA (Angular 18)
├── docs/                     # Documentación del proyecto
├── infra/                    # Infraestructura
├── .env.example              # Variables de entorno de ejemplo (sin secretos)
├── .gitignore
├── docker-compose.yml        # Orquestación de los contenedores
└── README.md
```

---

## Backend (Django + DRF)

### Estructura del backend

El código está en `backend/apps/`, dividido en un módulo por área de negocio. Las pruebas automatizadas están aparte, en `backend/tests/`.

```text
backend/
├── apps/
│   ├── assistant/      # Asistente IA de agendamiento
│   ├── booking/        # Motor de reservas
│   ├── catalog/        # Servicios, recursos y disponibilidad
│   ├── iam/            # Autenticación, autorización y roles
│   ├── notification/   # Notificaciones
│   ├── reporting/      # Dashboard y reportes
│   ├── shared/         # Código común entre módulos
│   ├── tenant/         # Gestión del negocio (multi-tenant)
│   └── __init__.py
├── config/             # Configuración de Django (settings, urls)
├── tests/              # Pruebas automatizadas
├── .importlinter       # Reglas de arquitectura entre módulos
├── Dockerfile.dev
├── manage.py
├── poetry.lock
└── pyproject.toml      # Dependencias, pytest y umbral de cobertura
```

### Patrón en capas por módulo

Todos los módulos siguen el mismo patrón en capas:

| Archivo | Capa | Responsabilidad |
| --- | --- | --- |
| `domain.py` | Dominio | Reglas de negocio puras, sin depender de Django |
| `models.py` | Persistencia | Definición de las tablas |
| `repositories.py` | Acceso a datos | Consultas y escritura en la base de datos |
| `services.py` | Aplicación | Casos de uso |
| `views.py` / `urls.py` | API | Endpoints REST |

### Archivos de evidencia del backend

#### 1. `backend/apps/catalog/domain.py`

Lógica de negocio pura (el cálculo de disponibilidad), sin depender de Django.

#### 2. `backend/apps/catalog/models.py`

Diseño de las tablas.

#### 3. `backend/apps/catalog/services.py` y `views.py`

Cómo se conecta todo con la API.

#### 4. `backend/tests/test_catalog_domain.py`

Pruebas automatizadas de la lógica de dominio.

---

## Integración continua y cobertura

### `.github/workflows/ci.yml`

El pipeline corre en cada push y Pull Request a `main` y `develop`.

- **Job Backend:** build de la imagen Docker, verificación de migraciones (`makemigrations --check`), `ruff`, `import-linter` y `pytest`.
- **Job Frontend:** build de la imagen y pruebas con Karma (Chrome headless).

### `backend/pyproject.toml`

Define las dependencias y el umbral mínimo de cobertura: `pytest` falla si la cobertura baja de **80%** (`--cov-fail-under=80`).

---

## Frontend (Angular 18)

### Estructura del frontend

El código está en `frontend/src/app/`, separado en tres áreas:

| Carpeta | Contenido |
| --- | --- |
| `core/` | Servicios HTTP, modelos y guards |
| `features/` | Una carpeta por pantalla o flujo |
| `shared/` | Componentes reutilizables |

```text
frontend/
├── public/
├── src/
│   └── app/
│       ├── core/        # Servicios HTTP, modelos, guards
│       ├── features/    # Una carpeta por pantalla/flujo
│       └── shared/      # Componentes reutilizables
├── angular.json
├── Dockerfile.dev
├── Dockerfile.test
├── karma.conf.js        # Pruebas y umbrales de cobertura
├── package.json
├── proxy.conf.json      # Proxy hacia la API en desarrollo
├── tsconfig.json
├── tsconfig.app.json
└── tsconfig.spec.json
```

### Archivos de evidencia del frontend

#### 1. `frontend/src/app/core/services/catalog.service.ts`

Cómo el frontend se comunica con la API.

#### 2. `frontend/src/app/features/inicio/pages/servicios-page/servicios-page.component.ts`

Una pantalla completa: componente, plantilla y estilos en un solo archivo.

#### 3. `frontend/src/app/features/landing/landing-page.component.ts`

La landing pública.

#### 4. `frontend/src/app/features/inicio/pages/catalog-pages.spec.ts`

Pruebas automatizadas del frontend.

