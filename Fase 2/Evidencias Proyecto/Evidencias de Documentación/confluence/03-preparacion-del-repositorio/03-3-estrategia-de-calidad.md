> **Exportado desde Confluence** · Espacio EXPERTIA-CAP26 · [Ver página original](https://maximilianodiazprofesional.atlassian.net/wiki/spaces/EXPERTIACA/pages/23232513) · versión 1 · última edición 2026-10-07

# Fase 2 (continuación) — Etapa 8: Estrategia de Calidad

| Campo | Detalle |
| --- | --- |
| **Fase** | 2 (continuación) — Etapa 8 (Acta de Constitución §6, `01-1`) |
| **Versión** | 1.0 — definición inicial (CAPDC-40, 2026-10-07) |
| **Rol aplicado** | QA Engineer |
| **Estado** | Documento vivo |

**Objetivo:** cumplir RNF-012 ("el proyecto debe mantener una cobertura de pruebas automatizadas mínima, a definir formalmente en la Etapa 8"), definiendo qué tipos de prueba existen, qué cobertura mínima se exige y cómo se aplican esos umbrales en el pipeline de CI (CAPDC-39). La ejecución del QA integral (pruebas manuales exploratorias de punta a punta) se mantiene en el Sprint 4, como ya establece `03-1` §3.1.

## 1. Tipos de prueba

| Tipo | Dónde vive | Qué verifica | Herramienta |
| --- | --- | --- | --- |
| Unitaria de dominio (backend) | `backend/tests/test_*_domain.py` | Funciones y value objects puros de `domain.py` (ej. `normalizar_para_slug`, `Email`), sin Django ni base de datos | `pytest` |
| Integración de API (backend) | `backend/tests/test_*.py` (el resto) | El flujo completo HTTP → vista → servicio → repositorio → base de datos real, incluyendo permisos, aislamiento multi-tenant y reglas de negocio (RN-\*) | `pytest-django` + `rest_framework.test.APIClient` |
| Unitaria de componente/servicio (frontend) | `frontend/src/app/**/*.spec.ts` | Formularios, servicios HTTP (mockeados con `HttpTestingController`), guards, interceptors y layouts | Jasmine + Karma (Chrome headless) |
| Verificación manual contra el servidor real | Parte del flujo de cada historia (no automatizada) | Que el feature funcione de punta a punta en Docker antes de cerrar la tarjeta de Jira — se documenta en el changelog de cada entrega, no sustituye a las pruebas automatizadas | `curl` / navegador |

La mayoría de las pruebas de backend son de integración (no mocks de la base de datos): es una decisión deliberada, ya registrada como feedback del proyecto — un incidente previo con mocks que no detectaron una migración rota hizo preferir pruebas contra una base de datos real.

## 2. Cobertura mínima

| Proyecto | Métrica | Umbral mínimo | Medido en CAPDC-40 (2026-10-07) |
| --- | --- | --- | --- |
| Backend | Líneas (`coverage.py`) | **80%** | 99.6% |
| Frontend | Statements | **80%** | 88.98% |
| Frontend | Lines | **80%** | 88.67% |
| Frontend | Functions | **75%** | 87.5% |
| Frontend | Branches | **60%** | 67.96% |

**Por qué el umbral queda muy por debajo de lo medido hoy:** los módulos `catalog`, `booking`, `notification` (salvo el adaptador de consola), `reporting` y `assistant` todavía son esqueletos vacíos (`startapp` sin implementar) — Django los cuenta como "100% cubiertos" por no tener líneas ejecutables, lo que infla el promedio actual artificialmente. A medida que se implementen en los sprints 2 a 4, el promedio real bajará de forma natural; un umbral del 80% dejado con margen evita que el pipeline se rompa por esa caída esperada, sin dejar de ser una exigencia real de calidad.

**Por qué no se persigue el 100%:** quedan 3 líneas sin cubrir en `apps/iam/models.py` y `apps/iam/repositories.py` (casos borde defensivos de bajo valor). No se agregaron pruebas solo para subir el número — cae dentro de la misma norma que ya rige el resto del proyecto: no se escribe código (ni pruebas) para escenarios que no aportan valor real.

**Frontend — limitación conocida de medición:** Angular (`@angular-devkit/build-angular:karma` con `codeCoverage: true`) solo instrumenta los archivos que algún `.spec.ts` llega a importar — un componente sin ninguna prueba no figura ni siquiera como "0% cubierto", simplemente no aparece en el reporte. Antes de CAPDC-40, 9 componentes nuevos (pantallas de negocio, staff, panel de Super Admin, layouts) no tenían ningún `.spec.ts` y por lo tanto no se medían; el 92.5% que mostraba el reporte en ese momento era real pero correspondía solo a una fracción pequeña de la aplicación. CAPDC-40 agregó pruebas livianas (creación del componente + una validación de comportamiento clave) a los 9 archivos, llevando la base medida de 160 a 354 statements. De aquí en adelante, cualquier componente nuevo sin al menos una prueba básica queda fuera de la medición de cobertura — es responsabilidad de quien lo construye agregarle al menos un `.spec.ts` mínimo.

## 3. Umbrales aplicados en CI

Ambos umbrales se aplican automáticamente, tanto en el pipeline de GitHub Actions (CAPDC-39, `.github/workflows/ci.yml`) como en ejecución local — no son una verificación aparte, son el comportamiento por defecto del mismo comando que ya se usa para correr las pruebas:

- **Backend:** `backend/pyproject.toml` → `[tool.pytest.ini_options]` define `addopts = "--cov=apps --cov-report=term-missing --cov-fail-under=80"`. Cualquier `pytest` (local o en CI) falla si la cobertura total baja de 80%.
- **Frontend:** `frontend/karma.conf.js` → `coverageReporter.check.global` define los 4 umbrales de la tabla anterior. Cualquier `ng test` (local o en CI, vía el servicio `frontend-test`) falla si alguna métrica baja de su umbral. Verificado manualmente subiendo el umbral de `statements` a un valor imposible (99.9%): el comando terminó con código de salida 1 y el mensaje `Coverage for statements (88.98%) does not meet global threshold (99.9%)`, confirmando que el gate realmente bloquea el build y no es cosmético.

## 4. Próximos pasos

- Revisar el umbral mínimo al cierre de cada sprint, cuando los módulos nuevos (Catalog en el Sprint 2, Booking y Assistant en el Sprint 3, Notification y Reporting en el Sprint 4) empiecen a aportar código real — es esperable que la cobertura medida baje antes de estabilizarse, y el umbral del 80% está pensado para absorber esa caída sin bloquear el pipeline innecesariamente.
- Mantener la disciplina de agregar al menos una prueba básica a todo componente de frontend nuevo, dado el límite de medición descrito en la sección 2.

## Control de cambios

| Versión | Fecha | Cambio | Responsable |
| --- | --- | --- | --- |
| 1.0 | 2026-10-07 | Definición inicial: tipos de prueba, cobertura mínima (backend 80%, frontend 80/80/75/60) y umbrales aplicados en CI (CAPDC-40, RNF-012) | Alberto Rincón |
