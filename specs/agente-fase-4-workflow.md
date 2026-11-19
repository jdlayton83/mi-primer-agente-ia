# Spec: Agente Fase 4 (Parámetros del workflow)

## Objetivo

Permitir configurar la skill y el prompt del agente al ejecutar manualmente GitHub Actions, preservando los fallbacks que ya ofrece `main.py`.

## Requisitos

- Mantener `workflow_dispatch` como mecanismo de ejecución manual.
- Añadir a `workflow_dispatch` dos inputs opcionales de tipo texto:
  - `agent_skill`, con valor predeterminado vacío. La persona que ejecuta el workflow puede indicar el nombre de una skill, por ejemplo `resumen_ejecutivo`, sin la extensión `.md`.
  - `agent_prompt`, con valor predeterminado vacío. La persona que ejecuta el workflow puede indicar el mensaje que recibirá el agente.
- Pasar ambos inputs como variables de entorno al paso que ejecuta `python main.py`:
  - `AGENT_SKILL` recibe el valor de `agent_skill`.
  - `AGENT_PROMPT` recibe el valor de `agent_prompt`.
- Conservar la variable `GEMINI_API_KEY` desde `secrets.GEMINI_API_KEY`; no imprimir ni exponer su valor en logs.
- Mantener la compatibilidad con el comportamiento actual de `main.py`:
  - Si `AGENT_SKILL` está vacía o no existe, el agente usa la `system_instruction` base.
  - Si `AGENT_PROMPT` está vacío o no existe, el agente usa su prompt predeterminado.
  - Cuando se proporciona `AGENT_SKILL`, el nombre identifica el archivo Markdown correspondiente en `skills/`.
- Los valores predeterminados vacíos deben conservar el comportamiento actual del workflow cuando no se personalizan los inputs.

## Criterios de aceptación

- La ejecución manual ofrece los dos campos opcionales y permite dejarlos vacíos.
- El paso que ejecuta `main.py` recibe `AGENT_SKILL` y `AGENT_PROMPT` mediante su entorno.
- Ejecutar sin valores conserva los fallbacks de `main.py`; proporcionar valores permite parametrizar la ejecución.
- La configuración existente de Python, instalación de dependencias y acceso a `GEMINI_API_KEY` se conserva.

## Fuera de alcance

- No modificar `main.py`.
- No cambiar el modelo `gemini-3.8-flash` ni la lógica de reintentos con `tenacity` ante `ServerError`.
- No añadir triggers distintos de `workflow_dispatch` ni matrices de jobs innecesarias.
- No añadir dependencias ni modificar `requirements.txt`.
- No cambiar la estructura ni el contenido de `skills/`, ni las especificaciones existentes en `specs/`.
- No alterar el manejo del secreto `GEMINI_API_KEY` más allá de conservar su uso actual.
