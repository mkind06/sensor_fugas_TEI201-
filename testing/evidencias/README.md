# Evidencias de testeo

## Avance 3

| Evidencia | Qué respalda |
|---|---|
| [Resultados de pruebas P1–P9](../resultados_avance3.md) | Registros del Monitor Serie: LED, lectura de sensores, publicación JSON cada 1 s, caudal ≈ 3,5 L/min con la bomba, reinicios por la bomba y su solución |
| [Fotos del banco y de la placa soldada](../../hardware/fotos/README.md) | Montaje del banco de PVC, sistema integrado y ambas caras de la placa |
| [Esquemático](../../hardware/esquemas/README.md) | Conexiones probadas, incluidas las correcciones del soldado |
| Dashboard y CSV | Se muestran en vivo en la presentación; el CSV se descarga desde el dashboard |

# Evidencias de testeo - Avance 2 (antecedente)

## Evidencia incorporada

| Evidencia disponible | Qué respalda | Límite |
|---|---|---|
| [Dos fotos del montaje final](../../hardware/fotos/README.md) | Banco hidráulico, dos sensores, protoboards y computador; monitor web y CAD visibles en una toma | No registran secuencia de estados ni duración continua |
| [Siete mediciones reales](../datos/lecturas_preajuste.csv) | Diagnóstico previo al ajuste con condición y parámetros identificados | Todas son anteriores al ajuste final; no son un ensayo de cinco minutos |
| [Logs históricos](../datos/diagnostico.md) | Problemas de lectura e iteración del montaje | Bloques separados, sin fecha de ensayo completo |
| Reporte del equipo | La presentación mostró normalidad, advertencia y fuga | Observación cualitativa sin registro final guardado |

El [Testeo sintético de verde](../datos/testeo_verde.md) verifica lógica y se mantiene separado de la evidencia física.

## Evidencia que falta respaldar

La guía, sección 3.1, exige operación integrada continua durante un mínimo de cinco minutos y actuación visible coherente con las lecturas. Falta conservar un registro de esa duración con la configuración final y evidencia legible de los estados. Si la operación fue observada directamente por el evaluador, eso puede ser parte de la evaluación presencial; el repositorio no permite verificarla independientemente.

Un video continuo que muestre banco, indicadores y lecturas, acompañado de CSV real, sería una forma de respaldarlo. La guía no impone nombres como banco_led_verde.jpg ni obliga a entregar un archivo de video específico. Las capturas adicionales y primeros planos son medios sugeridos para hacer la documentación más clara, no nuevos requisitos académicos.

## Fuera de esta entrega

No se presentan sesiones con usuarios externos o instalación en campo como realizadas. Esas actividades y sus reportes corresponden a desarrollos posteriores; no se agregan participantes, encuestas o métricas para completar una plantilla.
