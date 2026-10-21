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
| Código y dependencias | [Fuentes y procedencia](../software/src/README.md); código aportado por el equipo como el utilizado; versión exacta del núcleo pendiente |
| Circuito completo | [Diagrama y coordenadas](../hardware/esquemas/README.md) |

## Fuentes y trazabilidad

La revisión usa la guía aportada, TRASPASO_CODEX.md, el repositorio actual (base 181590e), el sketch histórico del commit ed744f1 y los CAD locales. Las instrucciones y ejemplos de documentos se evaluaron como contexto; las exigencias de etapas posteriores no se incorporaron como tareas de esta entrega.

El enfoque actual, confirmado por el equipo, es la detección de pérdidas en conducciones de riego agrícola, con aplicación prevista para agricultores y profesionales de agronomía. Se acota a un tramo con recorrido conocido para reducir variables y facilitar el ensayo. La propuesta urbana anterior es un antecedente histórico, no el contexto actual. La selección de ODS es 6/meta 6.4 como vínculo principal y 2/meta 2.4 como complemento; su justificación y fuentes están en el [resumen del proyecto](../README.md). El montaje utiliza ESP32-S3, FS400A y bomba USB. Los integrantes identificados en antecedentes son Andrés García, Pablo Miranda, Macarena Kuperman y Mathias Kind; falta confirmar roles actuales y profesor.

El código fuente utilizado por el equipo fue compartido directamente por el usuario después de la primera revisión. Sus instrucciones ejecutables coinciden con la reconstrucción anterior: K1=288, K2=229 y ventana de 10000 ms. Se actualizó su procedencia y se corrigió el comentario que decía 3 s a 10 s, sin modificar la lógica. El archivo no se extrajo de la placa y no se ejecutó una prueba física durante esta revisión. El CSV sintético y HTML reconstruidos mantienen su procedencia anterior; no se presentan como originales de la demo.

## Pendientes de esta evidencia

Fotos originales finales, registro continuo de cinco minutos, feedback, versión Arduino-ESP32, medidas reales, inventario hidráulico y precios comprobados. El código utilizado y el enfoque agrícola ya fueron aportados. La contribución a eficiencia hídrica todavía no está cuantificada.

## Etapas posteriores

[Reporte final](reporte_final/README.md) y [presentación final](presentacion/README.md) corresponden al Avance 3 y conservan su contenido anterior sin rellenar. Tampoco se completan pruebas de usuarios, instalación en terreno, métricas de impacto, renders finales ni historial nativo Fusion 360. Los ejemplos numéricos de sus plantillas no son resultados de esta entrega.
