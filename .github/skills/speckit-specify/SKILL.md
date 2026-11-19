---
name: speckit-specify
description: Convierte una necesidad del usuario en una especificación funcional clara y comprobable para este proyecto Python.
---

# Speckit Specify

## Objetivo

Definir qué debe hacer una funcionalidad y cuáles son sus límites antes de planificar o implementar código.

## Pasos

1. Lee las instrucciones de `.github/copilot-instructions.md` y la documentación pertinente en `specs/`.
2. Resume el problema, los usuarios o flujos afectados y el resultado esperado, sin asumir detalles no proporcionados.
3. Especifica escenarios, requisitos funcionales, criterios de aceptación y una sección explícita "Fuera de alcance".
4. Incluye restricciones Python relevantes —por ejemplo, interfaz de configuración, errores esperados y comportamiento observable— sin imponer una implementación prematura.
5. Si un requisito material es ambiguo, solicita aclaración antes de cerrar la spec.
6. Guarda una nueva especificación en `specs/<nombre-de-funcionalidad>.md` solo cuando se solicite crear el documento. Comprueba primero que la ruta no exista; no reemplaces ni edites specs existentes sin autorización explícita.
7. Redacta el documento manualmente; no ejecutes `specify.exe`.

## Criterios de salida

- La necesidad y los criterios de aceptación se pueden comprobar sin depender de una solución concreta.
- Los supuestos, requisitos y límites de alcance están diferenciados.
- Las dudas bloqueantes están resueltas o señaladas como pendientes.
- Ninguna especificación preexistente ha sido sobrescrita.
