---
name: speckit-plan
description: Diseña un plan técnico mínimo, validable y alineado con la spec para implementar una funcionalidad en este repositorio Python.
---

# Speckit Plan

## Objetivo

Traducir requisitos aprobados a una estrategia de implementación y validación, sin modificar código durante la planificación.

## Pasos

1. Lee la spec completa, sus aclaraciones y "Fuera de alcance", además de `.github/copilot-instructions.md`.
2. Inspecciona los archivos Python, configuración y pruebas relacionados; comprueba el estado de Git y conserva cambios preexistentes.
3. Relaciona cada requisito con los archivos y componentes que probablemente deban cambiar.
4. Describe el enfoque más pequeño que satisface la spec, sus interfaces, manejo de errores, compatibilidad Python y riesgos.
5. Define verificaciones focalizadas: pruebas existentes o nuevas necesarias, lint/type-check y comprobaciones manuales justificadas.
6. Identifica explícitamente los archivos que no deben tocarse por estar fuera de alcance.
7. Si se solicita guardar el plan, usa un archivo nuevo como `specs/<nombre-de-funcionalidad>-plan.md`; comprueba que no exista y no reemplaces un plan o spec existente sin autorización.

## Criterios de salida

- Cada requisito tiene una estrategia de implementación y una forma de validación.
- El plan preserva los límites de alcance y evita dependencias o abstracciones innecesarias.
- El plan refleja el estado real del repositorio y no asume que los cambios locales están limpios.
- No se ha editado código durante esta fase.
