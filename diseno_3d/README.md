# Diseño 3D

## Avance 3: caja v3 y gemelo de la demostración

| Archivo | Contenido |
|---|---|
| [caja_v3_base.step](cad/caja_v3_base.step), [caja_v3_tapa.step](cad/caja_v3_tapa.step) | Caja v3 en PETG, base y tapa por separado |
| [caja_v3_ensamble_electronica.step](cad/caja_v3_ensamble_electronica.step) | Caja con placa perforada 5 × 7 cm, ESP32 en cabezales, resistencias, borneras, LED, prensaestopas y tornillos |
| [gemelo_demo_completo.step](cad/gemelo_demo_completo.step) | Banco de demostración completo: estanque, PVC 32 mm, 2 FS400A, válvula de fuga y caja con cables |
| [fuente/](cad/fuente) | Scripts CadQuery que generan los STEP (`modelo_caja.py`, `modelo_demo.py`) y los planos (`planos.py`) |
| [renders/](renders/README.md) | 4 renders de la caja y de la demo |
| [visor/visor_3d.html](visor/visor_3d.html) | Visor web del gemelo: girar, acercar y abrir la caja |
| [planos/planos_caja_v3.pdf](planos/planos_caja_v3.pdf) | Planos técnicos A3: conjunto con lista de piezas, base y tapa con cotas |

Cambios respecto del concepto del Avance 2:
- La electrónica pasa de dos protoboards a una placa perforada soldada sobre 4 postes; la ESP32 va en cabezales hembra y se reemplaza sin desoldar.
- La ventana USB-C sube a 20,5 mm de altura (centro) para alinearse con la ESP32 montada en cabezales.
- Se mantienen la tapa con 4 tornillos M3 × 10, los 2 prensaestopas PG7 y los 3 LED de 5 mm en la tapa.

**Fusion 360:** [`fusion360/caja_v3.f3d`](fusion360/README.md), el mismo ensamble con la electrónica. Las medidas de la ESP32, la placa, las borneras y el banco son referenciales; confirmarlas antes de imprimir.

## Avance 2: encapsulado conceptual

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

En el Avance 3 estas carpetas ya tienen su contenido final: [Fusion 360](fusion360/README.md), [planos](planos/README.md) y [renders](renders/README.md).
