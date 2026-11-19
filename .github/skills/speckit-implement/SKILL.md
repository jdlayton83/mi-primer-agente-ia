---
name: speckit-implement
description: Implementa tareas aprobadas siguiendo la spec y el plan, con cambios Python mínimos y validación específica.
---

# Speckit Implement

## Objetivo

Ejecutar el trabajo aprobado sin desviarse de los requisitos ni de los límites establecidos.

## Pasos

1. Antes de editar, lee la spec, el plan, las tareas y `.github/copilot-instructions.md`; inspecciona el código pertinente y el estado de Git.
2. Conserva cambios locales existentes. No reviertas ni reformatees cambios ajenos a la tarea.
3. Implementa únicamente los requisitos aprobados con los patrones y tipos ya usados por el proyecto.
4. Mantén `google-genai`, `gemini-3.8-flash` y la política de reintentos de `tenacity` ante `ServerError`; no cambies workflow ni dependencias si la spec los deja fuera de alcance.
5. Mantén separadas las skills de Copilot en `.github/skills/`, las skills de ejecución del agente en `skills/` y las specs/planes en `specs/`.
6. Añade o ajusta solo pruebas focalizadas que cubran comportamiento nuevo o corregido. Ejecuta las pruebas, el análisis de tipos y la comprobación de sintaxis pertinentes al cambio.
7. Revisa el diff final contra los criterios de aceptación y confirma que no se modificaron archivos fuera de alcance.

## Criterios de salida

- Cada requisito implementado tiene validación adecuada o se informa claramente qué no pudo verificarse.
- No hay errores nuevos de sintaxis o tipos en los archivos afectados.
- El diff es mínimo, conserva cambios preexistentes y excluye todos los archivos fuera de alcance.
- El resumen final indica qué archivos cambiaron y los resultados de validación.
