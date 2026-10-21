# Encapsulado conceptual - Avance 2

## Archivos disponibles

- [caja_impresion_1.step](cad/caja_impresion_1.step): base y tapa dispuestas para impresión, 393715 bytes.
- [caja_planos.dxf](cad/caja_planos.dxf): plano conceptual, 80255 bytes.
- [Procedencia y revisión](cad/README.md).

El modelo se generó con CadQuery y se exportó a STEP/DXF. No se dispone de archivo nativo Fusion 360 con historial ni de un ensamble que incorpore toda la electrónica. El CAD representa un concepto de protección y distribución; no acredita fabricación o encaje físico.

## Dimensiones y distribución propuesta

| Elemento | Dimensiones / ubicación conceptual |
|---|---|
| Base | 120×85×40 mm; paredes y fondo 2,5 mm; esquinas radio 3 mm |
| Tapa | Placa 3 mm + labio interior 2 mm; envolvente de pieza 5 mm |
| Labio | Holgura nominal 0,3 mm; ancho 1,5 mm |
| Cierre | Cuatro torretas Ø8, pilotos Ø2,5; tapa Ø3,4 para M3×10 |
| ESP32 de referencia | 23×18 mm sobre cuatro postes Ø3,6×5 mm, piloto Ø1,6 |
| Protoboards de referencia | Dos de 47×35 mm; centros (−25,14) y (27,14) mm |
| USB-C | Ventana 12×7 mm en pared izquierda, centro a altura 10,4 mm |
| Cables de sensores | Dos pasos PG7 Ø12,5 mm en derecha, altura 18 mm |
| LED | Tres agujeros Ø5 en tapa; X=10,26,42 e Y=−24 mm |

Los tamaños de placa y protoboards son referencias típicas, no mediciones del equipo. Verificar también si la placa real permite la fijación por postes. El labio entra en la base; no se suman las envolventes de las piezas separadas para afirmar una altura total de 45 mm. El encaje final está pendiente.

## Justificación

La planta permite distribuir placa, protoboards y cables en una zona seca independiente de bomba y sensores. La altura deja margen para conexiones y acceso a los indicadores de tapa. La ventana USB facilita consulta y reprogramación; los pasos laterales ordenan cables y la tapa desmontable permite mantenimiento.

Se propone PETG como material de impresión para la caja. Su elección y la nota de relleno del 30 % del plano son decisiones de diseño; no existe impresión confirmada ni parámetros completos de máquina. Se plantean burlete de 2 mm, prensaestopas y montaje sobre las mangueras con lazos de goteo. No se declara grado IP, resistencia al exterior ni estanqueidad probada.

La bomba queda fuera y no hay etapa de potencia interna; la necesidad de ventilación y el calentamiento deben comprobarse con el montaje real. Antes de fabricar: medir piezas, revisar tolerancias, paso del conector USB, compatibilidad de fijaciones, mantenimiento y protección frente a salpicaduras.

Las carpetas [Fusion 360](fusion360/README.md), [planos finales](planos/README.md) y [renders finales](renders/README.md) conservan sus plantillas de otras etapas. Esta guía exige el modelo conceptual y su justificación; la impresión no es obligatoria.
