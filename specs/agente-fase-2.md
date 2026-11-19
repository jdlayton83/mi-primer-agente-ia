# Spec: Agente Fase 2 (Instrucción de sistema y entrada dinámica)

## Objetivo
Evolucionar `main.py` para que acepte prompts dinámicos y aplique una instrucción de sistema clara manteniendo la fiabilidad actual.

## Requisitos
- Mantener el SDK `google-genai`, el modelo `gemini-3.8-flash` y la política de reintentos con `tenacity` ante `ServerError`.
- Configurar `GenerateContentConfig` con una `system_instruction` que defina al agente como un asistente técnico claro, estructurado y práctico.
- Hacer que `generar_respuesta(prompt: str)` reciba el prompt como parámetro.
- Hacer que `ejecutar_agente()` lea `AGENT_PROMPT` desde variables de entorno y use un prompt por defecto si no está definida o está vacía.
- Imprimir la respuesta de forma legible en la salida estándar.

## Fuera de alcance
- No cambiar el workflow de GitHub Actions ni persistir archivos en disco en esta iteración.