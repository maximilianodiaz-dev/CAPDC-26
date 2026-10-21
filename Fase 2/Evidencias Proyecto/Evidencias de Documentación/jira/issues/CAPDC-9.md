# CAPDC-9 — US-002 — garantizar aislamiento de datos entre tenants a nivel de base de datos y backend

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-9)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | Listo |
| Sprint | Sprint 1 — Fundacional |
| Story points | 13 |
| Etiquetas | iam, must |
| Responsable | GENESIS . CACERES FERNANDEZ |
| Épica | CAPDC-1 IAM |
| Creada | 2026-09-20 |
| Resuelta | 2026-10-09 |

## Descripción

Como sistema, se debe garantizar aislamiento de datos entre tenants a nivel de base de datos y backend, para operar como SaaS multi-cliente de forma segura.

**Dependencias:** US-001  
**RF:** RF-004  
**Casos de uso:** —  
**Reglas relacionadas:** RN-004, RN-005, RNF-006

**Criterios de aceptación:**

1. Dado un usuario del tenant A, cuando consulta datos de negocio, entonces solo obtiene registros de su tenant (RF-004).
2. Dado un usuario del tenant A, cuando intenta leer, modificar o eliminar un registro del tenant B por su identificador, entonces no accede al registro ni lo altera.
3. Dada una consulta sin tenant activo en el contexto, cuando se usa un modelo con alcance de tenant, entonces no devuelve datos.
4. Dada una petición autenticada, cuando se determina el tenant activo, entonces se toma del token y no de valores enviados por el cliente.
5. Dado un modelo con alcance de tenant, cuando se define, entonces `tenant_id` es obligatorio.
6. Dados los módulos IAM y Tenant, entonces cada uno tiene al menos una prueba automatizada que demuestra que un tenant no accede a los datos de otro.

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (hasta que exista el pipeline, https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-39#icft=CAPDC-39, se ejecutan en el entorno Docker local).
* Pull Request revisado y mergeado a `main`, con la clave https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-9#icft=CAPDC-9 en la rama, los commits y el título del PR.
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

## Comentarios

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-10-02

Genesis por fa realiza el QA de esta tarea.  
  
**Decisión importante:** `Usuario` (IAM) **no** usa este mecanismo — el login necesita buscar por correo antes de saber a qué tenant pertenece. Quedó documentado en `02-4` para que no parezca una inconsistencia.

@GENESIS . CACERES FERNANDEZ

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

| Criterio | Evidencia encontrada | Estado |
| --- | --- | --- |
| CRITERIO ACEPTACION 1: consultar únicamente datos del tenant propio | `test_cada_tenant_solo_ve_sus_propios_registros` |  Aprobado preliminar  |
| CRITERIO ACEPTACION 2: impedir lectura, modificación y eliminación cruzadas | `test_no_se_puede_leer_modificar_ni_eliminar_un_registro_de_otro_tenant` |  Aprobado preliminar  |
| CRITERIO ACEPTACION 3: sin tenant activo, no devolver datos | `test_sin_tenant_en_el_contexto_no_devuelve_nada` |  Aprobado preliminar  |
| CRITERIO ACEPTACION 4: obtener el tenant desde el token | `test_middleware_toma_el_tenant_del_token` |  Aprobado preliminar  |
| CRITERIO ACEPTACION 5: `tenant_id` obligatorio | `test_tenant_id_es_obligatorio` |  Aprobado preliminar  |
| CRITERIO ACEPTACION 6: pruebas de aislamiento en IAM y Tenant | Pruebas de contexto y dominio IAM ejecutadas |  Pendiente  |

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

**Tipo de prueba:** Pruebas automatizadas de backend  
**Entorno:** Docker local  
**Resultado:** 18 pruebas aprobadas de 18 ejecutadas.

**Evidencia:** Ejecución de `pytest` sobre `tests/test_shared_tenant_scope.py` y `tests/test_iam_domain.py`, con resultado `18 passed in 4.91s`.

**Observación:** Las pruebas ejecutadas incluyen verificaciones de aislamiento de consultas, bloqueo de operaciones sobre registros de otro tenant, ausencia de datos sin contexto activo, obligatoriedad de `tenant_id` y determinación del tenant mediante el token.

**Conclusión :** Resultado satisfactorio para las pruebas ejecutadas. La aprobación definitiva de la US-002 queda pendiente de completar la revisión de todos los criterios de aceptación, en particular CA-006, y de confirmar el alcance de las aserciones de cada prueba.

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

Se finaliza la revisión QA de US-002 para el Sprint 1. Se ejecutaron 56 pruebas automatizadas seleccionadas del backend mediante Docker, todas aprobadas. Se obtuvo evidencia favorable del aislamiento general por tenant, la autenticación y las restricciones de gestión del personal entre tenants.

Se deja constancia de que el criterio CA-006, relativo a una prueba específica de aislamiento para IAM, no fue verificado de forma independiente en esta revisión. Este alcance queda documentado para su seguimiento.
