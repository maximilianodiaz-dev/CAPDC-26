# CAPDC-8 — US-001 — registrarme e iniciar sesión de forma segura

> [Ver en Jira](https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-8)

| Campo | Valor |
| --- | --- |
| Tipo | Historia |
| Estado | Listo |
| Sprint | Sprint 1 — Fundacional |
| Story points | 8 |
| Etiquetas | iam, must |
| Responsable | GENESIS . CACERES FERNANDEZ |
| Épica | CAPDC-1 IAM |
| Creada | 2026-09-20 |
| Resuelta | 2026-10-09 |

## Descripción

Como usuario, quiero registrarme e iniciar sesión de forma segura, para acceder a la plataforma según mi rol.

**Dependencias:** —  
**RF:** RF-001, RF-002, RF-003  
**Casos de uso:** UC-01, UC-02  
**Reglas relacionadas:** RN-018, RN-019, SUP-011, RNF-003, RNF-005

**Criterios de aceptación:**

1. Dado un correo no registrado y una contraseña válida, cuando el usuario se auto-registra, entonces se crea una cuenta activa con rol Dueño de Negocio (sin poder elegir otro rol), sin tenant asociado todavía (RN-019), y la contraseña se guarda solo como hash.
2. Dado un correo ya registrado, cuando intenta registrarse, entonces se rechaza indicando que ya existe una cuenta con ese correo (UC-01, E1).
3. Dada una contraseña que no cumple la política (menos de 10 caracteres, común o solo numérica), cuando se registra, entonces se rechaza y se pide corrección (UC-01, E2; RN-018).
4. Dadas credenciales válidas de una cuenta activa, cuando inicia sesión, entonces recibe un token de acceso de 30 minutos y uno de refresco de 7 días con rotación, que identifican al usuario, su rol y su tenant (si tiene) (UC-02; RN-018).
5. Dadas credenciales inválidas, cuando inicia sesión, entonces se rechaza sin indicar si el error está en el correo o en la contraseña (UC-02, E1).
6. Dada una cuenta desactivada, cuando inicia sesión, entonces se informa que la cuenta no está disponible (UC-02, E2).
7. Dados 5 intentos fallidos de inicio de sesión en 15 minutos, cuando se hace un intento más, entonces se rechaza durante 15 minutos (RN-018).

**Definición de hecho:**

* Código con pruebas automatizadas que pasan en CI (hasta que exista el pipeline, https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-39#icft=CAPDC-39, se ejecutan en el entorno Docker local).
* Pull Request revisado y mergeado a `main`, con la clave https://maximilianodiazprofesional.atlassian.net/browse/CAPDC-8#icft=CAPDC-8 en la rama, los commits y el título del PR.
* Documentación actualizada si corresponde (con su fila en el Control de cambios).

## Comentarios

**ALBERTO SLEITHER RINCON SEGREDO** · 2026-09-29

Genesis por fa, realiza el QA correspondiente, ya que el desarrollo se hicieron todas las pruebas.

**GENESIS . CACERES FERNANDEZ** · 2026-10-09

### Resultado QA — US-001: Registrarme e iniciar sesión de forma segura

**Resultado: PRUEBAS SATISFACTORIAS**

Se ejecutaron las pruebas automatizadas de autenticación en el entorno Docker local, obteniendo **17 de 17 pruebas aprobadas** (`17 passed in 11.70s`).

Se verificaron los siguientes criterios y comportamientos:

* **Registro de usuario:** creación de una cuenta activa con rol Dueño de Negocio, sin tenant asociado inicialmente y con contraseña almacenada como hash.
* **Correo duplicado:** el sistema rechaza el registro e informa que ya existe una cuenta con ese correo.
* **Política de contraseñas:** se rechazan contraseñas que no cumplen los requisitos establecidos.
* **Inicio de sesión:** se valida la autenticación y la emisión de tokens con la información del usuario, su rol y su tenant cuando corresponde.
* **Duración de tokens:** se comprueba una duración de 30 minutos para el token de acceso y 7 días para el token de refresco.
* **Credenciales inválidas:** el sistema muestra un mensaje genérico («Credenciales inválidas»), sin revelar si el correo o la contraseña son incorrectos.
* **Cuenta desactivada:** comportamiento cubierto satisfactoriamente por la prueba automatizada correspondiente.
* **Protección contra intentos fallidos:** se comprueba el bloqueo tras intentos fallidos, incluyendo la limitación por IP.
* **Rotación de tokens:** se valida la rotación del token de refresco y la invalidación del token anterior.

Adicionalmente, se realizaron pruebas manuales en el frontend, verificando el registro de cuentas, el inicio de sesión correcto, el rechazo de contraseñas incorrectas y de formato inválido, el rechazo de correos ya registrados, el mensaje genérico para credenciales inválidas y el bloqueo temporal después de múltiples intentos fallidos.

**Conclusión:** las 17 pruebas automatizadas y las verificaciones manuales realizadas fueron satisfactorias para los aspectos comprobados. La evidencia de QA es favorable para US-001.

Las pruebas se ejecutaron localmente en Docker. La revisión y aprobación del Pull Request, su fusión a `main` y la comprobación de la ejecución en CI deben verificarse por separado conforme a la definición de terminado de la historia.
