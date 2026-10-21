# Detector de pérdidas de agua en sistemas de riego agrícola

TEI201 · Taller de Diseño en Ingeniería · Universidad Adolfo Ibáñez.

## Avance 2: primer prototipo físico Alpha

El banco recircula agua por dos sensores FS400A y permite abrir una derivación entre ellos. Una ESP32-S3 Super Mini estima los caudales, compara su diferencia y activa un LED verde, amarillo o rojo. La comunicación disponible es USB serie al computador. La bomba se enciende manualmente y tiene alimentación independiente.

La demostración ya se realizó: el equipo informó que se observaron los tres estados. No se conservó el registro final. Esta entrega documenta el montaje, las mediciones disponibles, las decisiones de diseño y el concepto de encapsulado.

| Contenido de esta entrega | Documento |
|---|---|
| Montaje y alimentación | [Hardware](hardware/README.md) |
| Componentes confirmados | [BOM](hardware/bom/README.md) |
| Fotografías del montaje final y monitor web | [Evidencia fotográfica](hardware/fotos/README.md) |
| Diagrama y coordenadas de protoboards | [Circuito](hardware/esquemas/README.md) |
| Código y comunicación USB | [Software](software/README.md) |
| Instalación y operación | [Manual](software/docs/README.md) |
| Modelo STEP, plano DXF y justificación | [Encapsulado conceptual](diseno_3d/README.md) |
| Problemas, soluciones y cambios | [Iteraciones](iteraciones/README.md) |
| Mediciones y procedencia del testeo | [Testeo](testing/README.md) |
| Revisión de requisitos de la guía | [Estado de la entrega](documentacion/README.md) |
| Revisión documento por documento | [Matriz del Avance 2](documentacion/revision_avance2.md) |

## Alcance y evidencia

Se distinguen siete lecturas físicas anteriores al ajuste, registros de diagnóstico, un testeo de lógica con datos sintéticos y el resultado cualitativo comunicado por el equipo. Ninguno sustituye un registro físico continuo de cinco minutos. El STEP y el DXF son archivos de diseño conceptual; la impresión y el ensamble con componentes reales quedan por verificar.

## Problema y enfoque agrícola

El proyecto se enfoca en pérdidas de agua en conducciones de riego agrícola y su detección mediante comparación de caudal antes y después de un tramo. Sus usuarios previstos son agricultores, encargados de riego y profesionales de agronomía. La alerta permite advertir una diferencia y orientar una inspección del tramo; el Alpha no localiza el punto exacto de la fuga ni cierra el agua automáticamente.

El equipo acotó el desarrollo a un tramo agrícola con recorrido conocido para trabajar con menos ramificaciones, consumos simultáneos y variables desconocidas que las de una red urbana completa. Esta simplificación corresponde al alcance elegido, no a afirmar que todo sistema agrícola sea simple. En una aplicación real deben considerarse presión, rango de caudal, aire, sedimentos, válvulas y salidas de riego. Una salida legítima entre sensores también produce una diferencia: las salidas normales deben quedar fuera del tramo vigilado o medirse por separado.

## Objetivos de Desarrollo Sostenible

- **ODS principal: 6, Agua limpia y saneamiento; meta 6.4.** El proyecto se vincula con el uso eficiente del agua al advertir posibles pérdidas en la conducción de riego y facilitar su revisión. [Meta oficial de Naciones Unidas](https://sdgs.un.org/goals/goal6).
- **ODS complementario: 2, Hambre cero; meta 2.4.** Su aplicación prevista apoya prácticas agrícolas sostenibles mediante un mejor cuidado del agua destinada al riego. Esta relación es indirecta y no constituye evidencia de mayor producción o resiliencia de cultivos. [Meta oficial de Naciones Unidas](https://sdgs.un.org/goals/goal2).

El logro de Avance 2 es la detección y señalización en banco. Aún no se midieron ahorro de agua, rendimiento agrícola ni cambios en los indicadores oficiales de estas metas.

## Entregas posteriores

Las carpetas de [versión final](iteraciones/iteracion_3/README.md), [presentación final](documentacion/presentacion/README.md), [reporte final](documentacion/reporte_final/README.md), [Fusion 360 nativo](diseno_3d/fusion360/README.md), [planos finales](diseno_3d/planos/README.md), [renders](diseno_3d/renders/README.md) y [reportes de usuarios](testing/reportes/README.md) conservan su contenido de referencia, identificado al inicio como plantilla de otra etapa. Sus listas y cifras de ejemplo no son resultados del Alpha.
