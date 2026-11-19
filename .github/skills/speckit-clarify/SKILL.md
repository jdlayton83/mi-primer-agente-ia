---
name: speckit-clarify
description: Detecta ambigüedades y contradicciones en una spec y obtiene decisiones antes de planificar la implementación.
---

# Speckit Clarify

## Objetivo

Reducir la incertidumbre de una especificación sin ampliar su alcance ni decidir por el usuario cuestiones de comportamiento importantes.

## Pasos

1. Lee la spec objetivo completa y las instrucciones del proyecto en `.github/copilot-instructions.md`.
2. Contrasta requisitos, criterios de aceptación y "Fuera de alcance"; localiza solo ambigüedades, contradicciones o casos límite que cambien la solución.
3. Agrupa preguntas breves y concretas, priorizando decisiones que bloqueen el plan o tengan impacto funcional.
4. Pregunta al usuario antes de resolver por su cuenta una decisión material.
5. Incorpora las respuestas a la spec únicamente cuando se solicite editarla. Preserva el texto existente que no esté afectado y no sobrescribas archivos.
6. Si no quedan preguntas bloqueantes, deja constancia de que la spec está lista para planificación; no inicies la implementación en esta fase.

## Criterios de salida

- Las ambigüedades relevantes están resueltas o explícitamente registradas como pendientes.
- Los requisitos no se contradicen y los casos límite importantes tienen resultado esperado.
- Las decisiones añadidas reflejan las respuestas del usuario, no supuestos de Copilot.
- No se han modificado código ni documentos no autorizados.
