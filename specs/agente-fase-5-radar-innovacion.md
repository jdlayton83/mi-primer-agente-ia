# Spec: Agente Fase 5 (Radar semanal de innovación)

## Objetivo

Crear un resumen semanal de proyectos innovadores SaaS relacionados con datos, business intelligence, analítica, automatización e inteligencia artificial empresarial que puedan inspirar oportunidades para databi.cloud.

El agente debe descubrir información publicada públicamente, contrastarla y generar recomendaciones que indiquen qué explorar, por qué puede ser relevante y qué fuente verificar. No debe copiar ni reproducir software ajeno.

## Requisitos

### Programación

- Añadir una ejecución automática semanal los martes a las 09:00 Europe/Madrid.
- Permitir una ejecución manual adicional para probar el radar sin esperar al horario semanal.
- La primera ejecución automática prevista es el martes 24 de noviembre de 2026 a las 09:00 Europe/Madrid.
- Usar el campo `timezone` de `schedule` en GitHub Actions para conservar la hora local durante los cambios entre horario de invierno y verano.

### Fuentes

- Consultar exclusivamente fuentes públicas.
- Combinar RSS y fuentes web públicas curadas.
- Mantener una lista de fuentes configurada en el repositorio, separada del código de ejecución si es posible.
- Admitir fuentes relacionadas con SaaS, productos digitales, startups, datos, BI, analítica, automatización e IA empresarial.
- Registrar para cada hallazgo al menos: título, fuente, fecha o periodo conocido, enlace original y motivo de relevancia.
- No navegar por páginas privadas, autenticadas o protegidas que requieran credenciales.
- No realizar scraping evasivo, eludir controles de acceso ni descargar código ajeno.

### Generación del resumen

- Mantener el SDK `google-genai`, el modelo `gemini-3.8-flash` y los reintentos con `tenacity` ante `ServerError`.
- Usar una skill de ejecución específica, por ejemplo `radar_innovacion`.
- El contenido generado debe usar datos confirmados y distinguir hechos de hipótesis o inferencias.
- El resumen debe incluir:
  1. una introducción breve;
  2. los proyectos o tendencias más relevantes;
  3. para cada elemento: propuesta de valor, señales de innovación, posible aplicación para databi.cloud y nivel de interés;
  4. fuentes verificables;
  5. riesgos, dudas o datos no confirmados;
  6. próximos pasos recomendados.
- No presentar como hecho una información no verificable.
- No recomendar copiar, clonar o reproducir productos ajenos.
- Limitar la respuesta a un formato útil por correo y legible.

### Entrega por correo

- Enviar el resumen mediante SMTP.
- Exigir que los valores de conexión se proporcionen mediante GitHub Secrets:
  - `RADAR_SMTP_HOST`;
  - `RADAR_SMTP_PORT`;
  - `RADAR_SMTP_USER`;
  - `RADAR_SMTP_PASSWORD`;
  - `RADAR_SMTP_FROM`;
  - `RADAR_SMTP_TO`.
- Usar TLS o una variante segura de la conexión SMTP compatible con el proveedor configurado.
- No registrar contraseñas, cuentas completas ni credenciales en logs.
- Si falta una configuración obligatoria, mostrar un aviso claro y terminar sin intentar enviar correo.
- El asunto puede incluir fecha y una etiqueta, por ejemplo `Radar semanal de innovación - <fecha>`.

### Seguridad y privacidad

- Todos los secretos deben residir en GitHub Secrets o variables de entorno locales privadas.
- No persistir el contenido recibido o generado por el agente en el repositorio.
- No incluir datos personales, contratos, precios internos, credenciales o información privada de databi.cloud que no haya sido proporcionada expresamente.
- Validar entradas y URLs antes de solicitarlas o incluirlas en el correo.

## Criterios de aceptación

- Existe una ejecución programada semanal a la hora acordada y una ejecución manual disponible.
- El radar recopila y resume proyectos de fuentes públicas definidas.
- Cada hallazgo incluye fuente y enlace verificable.
- El correo se entrega a la dirección configurada mediante secretos, o el fallo queda informado sin exponer secretos.
- El modelo mantiene `gemini-3.8-flash`, `google-genai` y los reintentos con `tenacity`.
- La salida distingue hechos, inferencias y próximos pasos.
- No se escribe ni persiste contenido adicional en el repositorio durante la ejecución.

## Fuera de alcance

- No modificar `main.py` hasta que exista un plan de implementación aprobado y el alcance concreto esté aprobado.
- No añadir integraciones con CRM, Teams, Slack, correo de Microsoft Graph o APIs comerciales en esta fase.
- No introducir nuevas dependencias hasta que el plan las justifique y se actualice `requirements.txt` en una fase posterior.
- No cambiar el modelo `gemini-3.8-flash`, el SDK `google-genai` ni la política actual de reintentos.
- No crear matrices de jobs ni triggers adicionales innecesarios.
- No descargar, copiar, clonar ni reutilizar el código de los proyectos encontrados.
- No enviar a listas abiertas ni recurrir a recopilaciones masivas de direcciones.
- No incluir datos personales o información privada sin autorización expresa.
