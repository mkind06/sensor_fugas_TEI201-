# Detector de fugas mediante comparación de caudales

TEI201 · Taller de Diseño en Ingeniería · Universidad Adolfo Ibáñez.

## Avance 2: primer prototipo físico Alpha

El banco recircula agua por dos sensores FS400A y permite abrir una derivación entre ellos. Una ESP32-S3 Super Mini estima los caudales, compara su diferencia y activa un LED verde, amarillo o rojo. La comunicación disponible es USB serie al computador. La bomba se enciende manualmente y tiene alimentación independiente.

La demostración ya se realizó: el equipo informó que se observaron los tres estados. No se conservó el registro final. Esta entrega documenta el montaje, las mediciones disponibles, las decisiones de diseño y el concepto de encapsulado.

| Contenido de esta entrega | Documento |
|---|---|
| Montaje y alimentación | [Hardware](hardware/README.md) |
| Componentes confirmados | [BOM](hardware/bom/README.md) |
| Diagrama y coordenadas de protoboards | [Circuito](hardware/esquemas/README.md) |
| Código y comunicación USB | [Software](software/README.md) |
| Instalación y operación | [Manual](software/docs/README.md) |
| Modelo STEP, plano DXF y justificación | [Encapsulado conceptual](diseno_3d/README.md) |
| Problemas, soluciones y cambios | [Iteraciones](iteraciones/README.md) |
| Mediciones y procedencia del testeo | [Testeo](testing/README.md) |
| Revisión de requisitos de la guía | [Estado de la entrega](documentacion/README.md) |

## Alcance y evidencia

Se distinguen siete lecturas físicas anteriores al ajuste, registros de diagnóstico, un testeo de lógica con datos sintéticos y el resultado cualitativo comunicado por el equipo. Ninguno sustituye un registro físico continuo de cinco minutos. El STEP y el DXF son archivos de diseño conceptual; la impresión y el ensamble con componentes reales quedan por verificar.

El problema de origen es la pérdida de agua en distribución, inicialmente contextualizado en Recoleta; el banco permite estudiar un solo tramo y el traspaso plantea una aplicación posterior a riego. El aporte actual es advertir una diferencia para que una persona inspeccione. La relación propuesta con eficiencia hídrica y ODS 6 no equivale a un ahorro medido; falta confirmar la meta formal del equipo.

## Entregas posteriores

Las carpetas de [versión final](iteraciones/iteracion_3/README.md), [presentación final](documentacion/presentacion/README.md), [reporte final](documentacion/reporte_final/README.md), [Fusion 360 nativo](diseno_3d/fusion360/README.md), [planos finales](diseno_3d/planos/README.md), [renders](diseno_3d/renders/README.md) y [reportes de usuarios](testing/reportes/README.md) conservan su contenido anterior. Sus listas y cifras de ejemplo son plantillas para otras etapas, no resultados del Alpha.
