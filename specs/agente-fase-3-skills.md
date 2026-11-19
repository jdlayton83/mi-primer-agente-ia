# Spec: Agente Fase 3 (Carga modular de Skills)

## Objetivo
Permitir que `main.py` cargue dinámicamente un archivo de skill en Markdown desde la carpeta `skills/` para especializar el comportamiento del agente según la tarea.

## Requisitos
- Mantener intactos el cliente `google-genai`, el modelo `gemini-3.8-flash` y la política de reintentos con `tenacity` ante `ServerError`.
- Leer la variable de entorno `AGENT_SKILL` (por ejemplo, `"resumen_ejecutivo"`).
- Si `AGENT_SKILL` está definida, buscar el archivo `skills/{AGENT_SKILL}.md` y leer su contenido en UTF-8.
- Si el archivo existe, combinar la identidad base del agente con el contenido de la skill dentro de `system_instruction` en `GenerateContentConfig`.
- Si `AGENT_SKILL` no está definida o el archivo no existe, mostrar un aviso claro por consola y ejecutar el agente con su `system_instruction` base por defecto sin lanzar una excepción fatal.
- Mantener la lectura dinámica de `AGENT_PROMPT`.

## Fuera de alcance
- No modificar `.github/workflows/run_agent.yml` en esta iteración.
- No añadir nuevas dependencias externas a `requirements.txt`.