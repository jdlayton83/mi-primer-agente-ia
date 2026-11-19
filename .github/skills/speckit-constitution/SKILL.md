---
name: speckit-constitution
description: Define los principios y límites duraderos de desarrollo de este repositorio Python antes de iniciar una funcionalidad.
---

# Speckit Constitution

## Objetivo

Establecer principios de trabajo estables para este repositorio antes de especificar una funcionalidad. Esta skill guía el proceso de desarrollo de Copilot; no es una skill de ejecución del agente.

## Pasos

1. Revisa `.github/copilot-instructions.md`, `README.md` y los documentos existentes en `specs/` que sean pertinentes.
2. Identifica principios verificables sobre compatibilidad, seguridad, dependencias, pruebas, alcance y mantenimiento.
3. Conserva las restricciones ya establecidas: `google-genai`, el modelo `gemini-3.8-flash`, reintentos con `tenacity` ante `ServerError` y respeto al apartado "Fuera de alcance" de cada spec.
4. Si el usuario solicita una constitución y no existe, prepara `.github/constitution.md`. Si ya existe, léela y propone cambios incrementales; no la reemplaces.
5. No ejecutes `specify.exe` ni otros generadores con efectos de escritura para crear o actualizar la constitución.

## Criterios de salida

- Los principios son concretos, comprobables y compatibles con las instrucciones existentes.
- Las restricciones actuales y sus excepciones están expresadas sin contradicciones.
- La constitución solo se crea o actualiza cuando se ha solicitado; ningún archivo existente se sobrescribe sin autorización.
- No se modifican código, workflow, dependencias, specs ni skills de ejecución como parte de esta fase.
