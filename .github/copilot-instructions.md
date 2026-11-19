# Instrucciones del proyecto

- Antes de modificar código, lee la especificación correspondiente en `specs/` y respeta tanto sus requisitos como sus límites de "Fuera de alcance".
- Mantén el SDK `google-genai` y el modelo `gemini-3.8-flash`.
- Mantén los reintentos con `tenacity` para errores `ServerError`.
- No modifiques archivos ni comportamiento que la especificación correspondiente deje fuera de alcance.
- Trata los archivos de `specs/` como referencia; no los sobrescribas al implementar sus requisitos.
- Usa las skills de desarrollo para Copilot únicamente desde `.github/skills/`. No las mezcles con las skills de ejecución del agente en `skills/`.
- Trata `specs/` como la fuente de requisitos, especificaciones y planes; no la uses para almacenar skills de Copilot ni del agente.
- Sigue las fases de desarrollo en orden cuando apliquen: `speckit-constitution`, `speckit-specify`, `speckit-clarify`, `speckit-plan`, `speckit-tasks` y `speckit-implement`.
- Antes de crear un documento de especificación o plan, comprueba si ya existe y no lo sobrescribas sin autorización explícita.
