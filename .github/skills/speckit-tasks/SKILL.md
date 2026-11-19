---
name: speckit-tasks
description: Descompone una spec y un plan aprobados en tareas Python pequeñas, ordenadas y verificables.
---

# Speckit Tasks

## Objetivo

Preparar una lista ejecutable de trabajo que conecte los requisitos de la spec con cambios y validaciones concretos.

## Pasos

1. Lee la spec, el plan técnico y sus límites de "Fuera de alcance".
2. Divide el trabajo en tareas pequeñas con resultado observable; agrupa por archivo o componente cuando ayude a mantener cambios coherentes.
3. Ordena las tareas por dependencias reales y señala explícitamente esas dependencias.
4. Incluye tareas de pruebas y validación para los comportamientos nuevos, además de la revisión final de alcance.
5. Evita tareas que añadan dependencias, cambien workflows o alteren funcionalidades no cubiertas por la spec.
6. Si se solicita guardar el desglose, crea un documento nuevo como `specs/<nombre-de-funcionalidad>-tasks.md`; verifica que no exista y no sobrescribas documentos existentes.

## Criterios de salida

- Cada tarea es accionable, acotada y comprobable.
- El orden respeta las dependencias y no contiene dependencias inventadas.
- Todas las tareas trazan a un requisito o a una validación necesaria.
- Las tareas fuera de alcance están excluidas y no se ha modificado código.
