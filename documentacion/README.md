# Estado documental - Avance 2

## Revisión frente a la guía

Se revisó la guía completa de nueve páginas, fechada 19-10-2026. La entrega es una demostración presencial de Alpha de 5–7 minutos más 2 de feedback, con participación de todos. Las recomendaciones de ensayo no se registran como actividades realizadas sin evidencia.

| Requisito de Avance 2 | Evidencia disponible y límite |
|---|---|
| Sensores en tiempo real | Dos FS400A, lecturas y diagnóstico en [Testeo](../testing/README.md); precisión absoluta pendiente |
| Actuación visible | LED verde/amarillo/rojo según lógica; resultado cualitativo comunicado por equipo |
| Conectividad verificable | USB serie a computador; WiFi/Bluetooth no implementados y sin feedback docente que confirme aceptación específica del criterio |
| Integración y estabilidad ≥5 min | Demostración informada como exitosa; falta registro continuo final de cinco minutos |
| Encapsulado conceptual | [STEP, DXF y justificación](../diseno_3d/README.md); sin impresión ni encaje físico confirmado |
| Iteración y resolución parcial | [Cambios y aprendizajes](../iteraciones/README.md); alerta local de posible pérdida, sin ahorro medido |
| Código y dependencias | [Fuentes y procedencia](../software/src/README.md); versión exacta del núcleo y firmware de demo por cotejar |
| Circuito completo | [Diagrama y coordenadas](../hardware/esquemas/README.md) |

## Fuentes y trazabilidad

La revisión usa la guía aportada, TRASPASO_CODEX.md, el repositorio actual (base 181590e), el sketch histórico del commit ed744f1 y los CAD locales. Las instrucciones y ejemplos de documentos se evaluaron como contexto; las exigencias de etapas posteriores no se incorporaron como tareas de esta entrega.

También se consultó el informe de propuesta de septiembre del proyecto de pérdidas de agua en Recoleta. Sus alternativas de placa Nano, sensores YF-S201, bomba de 12 V, presupuesto y metas eran propuestas. El montaje posterior documentado utiliza ESP32-S3, FS400A y bomba USB; no se sustituyen las piezas reales por aquella planificación. La propuesta identifica a Andrés García, Pablo Miranda, Macarena Kuperman y Mathias Kind; falta confirmar roles actuales y profesor.

El paquete de archivos preparado en la sesión anterior no estaba disponible en las carpetas revisadas. Por ello se transcribieron las siete lecturas, se recuperó el sketch histórico desde Git y se identificaron expresamente las reconstrucciones. El CSV sintético y HTML nuevos no se presentan como los originales anteriores.

## Pendientes de esta evidencia

Fotos originales finales, registro continuo de cinco minutos, feedback, firmware exacto de la demo, versión Arduino-ESP32, medidas reales, inventario hidráulico y precios comprobados. Falta confirmar ODS/meta formal; la contribución propuesta a eficiencia hídrica no está cuantificada.

## Etapas posteriores

[Reporte final](reporte_final/README.md) y [presentación final](presentacion/README.md) corresponden al Avance 3 y conservan su contenido anterior sin rellenar. Tampoco se completan pruebas de usuarios, instalación en terreno, métricas de impacto, renders finales ni historial nativo Fusion 360. Los ejemplos numéricos de sus plantillas no son resultados de esta entrega.
