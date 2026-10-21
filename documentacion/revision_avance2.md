# Revisión documento por documento - Avance 2

## Criterio y alcance

Se revisaron los 27 documentos Markdown existentes, el sketch aportado por el equipo, el panel, los dos CSV, las dos fotos y las referencias CAD contra la guía de nueve páginas del Avance 2 (fecha consignada: 19-10-2026). Esta matriz y el protocolo son documentos nuevos de apoyo para esta entrega. La base del repositorio revisada es 52483e5, posterior a la incorporación del enfoque agrícola y las fotos.

**Documentado:** contenido pertinente desarrollado y coherente con los archivos disponibles. **Parcial:** falta evidencia o precisión necesaria para respaldar por completo el criterio. **Otra etapa:** no se rellena; se identifica su alcance. Ninguno de estos estados asigna una nota ni equivale a certificar el funcionamiento físico.

## Resultado por documento existente

| Documento | Guía / estado | Resultado de la revisión y acción |
|---|---|---|
| [Resumen del proyecto](../README.md) | 3.1–3.4 / Documentado | Foco agrícola y ODS 6.4/2.4 coherentes; se añadió acceso a esta matriz y se precisó el alcance de plantillas |
| [Hardware](../hardware/README.md) | 3.1 y 3.4 / Documentado | Pines, fuentes, divisores y recorrido coinciden con el sketch; bomba manual y mediciones pendientes explícitas |
| [BOM](../hardware/bom/README.md) | 3.4 / Documentado con límites | Componentes reales separados de piezas propuestas. Precios e inventario definitivo pendientes; la guía actual no fija un presupuesto obligatorio |
| [Esquemas](../hardware/esquemas/README.md) | 3.4 / Documentado | Diagramas eléctrico e hidráulico, GPIO, resistencias y coordenadas completos según el cableado informado; no se afirma medición eléctrica |
| [Fotografías](../hardware/fotos/README.md) | 3.1 y 3.3 / Parcial | Dos originales finales y leyendas presentes; no prueban secuencia de LED ni duración continua |
| [Software general](../software/README.md) | 3.4 / Documentado | Fórmulas, arquitectura, valores 288/229, 10 s y umbrales coherentes; USB identificado sin atribuir WiFi |
| [Manual y funciones](../software/docs/README.md) | 3.4 / Documentado | Operación, funciones y diagnóstico desarrollados; se corrigió el límite amarillo a 10≤Dif<25 para evitar solapamiento con rojo |
| [Librerías](../software/librerias/README.md) | 3.4 / Documentado con límite | No requiere bibliotecas externas; falta registrar versión exacta Arduino-ESP32 para reproducibilidad completa |
| [Código fuente](../software/src/README.md) | 3.4 / Documentado con límite | Código aportado identificado y enlazado; monitor de la foto distinguido del HTML reconstruido; fuente HTML original pendiente |
| [Encapsulado](../diseno_3d/README.md) | 3.2 / Parcial | STEP, DXF, dimensiones, material, accesos y mantenimiento documentados; falta una vista clara de distribución interna contrastada con componentes reales |
| [Revisión CAD](../diseno_3d/cad/README.md) | 3.2 / Documentado con límite | Huellas y auditoría DXF respaldadas; revisión STEP anterior atribuida, sin afirmar encaje o fabricación |
| [Fusion 360 nativo](../diseno_3d/fusion360/README.md) | Otra etapa | Se añadió aviso de plantilla v3; F3D, historial y DHT22 de ejemplo no son archivos ni componentes acreditados del Alpha |
| [Planos finales](../diseno_3d/planos/README.md) | Otra etapa | Se añadió aviso; el DXF conceptual actual está en CAD, sin declarar planos v3 terminados |
| [Renders finales](../diseno_3d/renders/README.md) | Otra etapa | Se añadió aviso; cuatro renders y resolución de esa plantilla no son exigencias de esta guía |
| [Historial de iteraciones](../iteraciones/README.md) | 3.3 y 3.4 / Documentado | Problemas, decisiones, ajustes históricos y enfoque agrícola trazados; sin porcentajes ficticios de mejora |
| [Iteración 1](../iteraciones/iteracion_1/README.md) | Antecedente / referencia | Se añadió aviso histórico: fecha, v1 y causalidad del texto heredado no se presentan como corroborados; no se reconstruye la entrega oficial anterior |
| [Iteración 2](../iteraciones/iteracion_2/README.md) | 3.1–3.4 / Documentado con límites | Alpha, cambios y logros parciales coherentes; estado físico de cinco minutos y encaje siguen pendientes |
| [Iteración 3](../iteraciones/iteracion_3/README.md) | Otra etapa | Se añadió aviso antes de objetivos, marcas de logro y cifras ilustrativas; no se rellenan resultados futuros |
| [Testeo general](../testing/README.md) | 3.3 / Parcial | Se enlazaron fotos y protocolo; distingue siete mediciones, sintéticos y demo cualitativa; falta registro final continuo |
| [Datos de Testeo](../testing/datos/README.md) | 3.3 / Documentado | Siete filas conservadas, condición sin fuga intencional y amarillo explícitos; ajuste 228,75 coherente |
| [Diagnóstico](../testing/datos/diagnostico.md) | 3.3 y 3.4 / Documentado | Logs y resúmenes históricos separados, sin unirlos artificialmente en un ensayo |
| [Metodología de verde](../testing/datos/testeo_verde.md) | Apoyo a 3.3 / Documentado | Treinta escenarios de lógica identificados como sintéticos; no acreditan precisión ni cinco minutos físicos |
| [Evidencias de Testeo](../testing/evidencias/README.md) | 3.1 y 3.3 / Parcial | Se reemplazó la lista de nombres de archivos supuestamente obligatorios por evidencia disponible y requisito real de funcionamiento |
| [Reportes de usuarios](../testing/reportes/README.md) | Otra etapa | Se añadió aviso: encuestas, participantes y cifras de ejemplo no se presentan como realizados |
| [Estado documental](README.md) | 3.1–3.4 / Documentado con límites | Matriz de requisitos y pendientes conservada; se precisó que imprimir no es obligatorio y se enlazó esta revisión |
| [Presentación final](presentacion/README.md) | Otra etapa | Se añadió aviso Avance 3; su duración de diez minutos no corresponde a la demo actual de 5–7 minutos |
| [Reporte final](reporte_final/README.md) | Otra etapa | Se añadió aviso Avance 3; no se exige reporte de quince páginas para esta entrega |

## Archivos de respaldo revisados

| Archivo / grupo | Comprobación y límite |
|---|---|
| Sketch actual e histórico | Solo se usan GPIO1/2 y LED4/5/6, 115200, K actual 288/229, 200 µs, cinco muestras, 10 s y umbrales 0,5/10/25. El histórico con 275 conserva extensión .txt. No se modifica lógica ni se declara compilación |
| Panel HTML | Parser y estados corresponden al formato serie; se corrigió únicamente una etiqueta que seguía llamando reconstruido al sketch ya aportado. El propio panel conserva su etiqueta de reconstrucción |
| CSV reales y sintéticos | Siete lecturas sin cambios y treinta escenarios con procedencia separada. El porcentaje real transmitido no se reemplaza por un recálculo de valores redondeados |
| JPEG finales | Originales conservados; las leyendas se limitan a lo visible y a la identificación de montaje final dada por el equipo |
| STEP y DXF | Archivos conceptuales accesibles, con sus huellas; no se presentan como caja impresa ni ensamble físico validado |

## Requisitos que la documentación todavía no puede acreditar

| Guía | Estado y evidencia que resolvería el pendiente |
|---|---|
| 3.1: lecturas precisas y consistentes | Hay mediciones y ajuste relativo, sin referencia volumétrica independiente. Falta respaldo de precisión en las condiciones de uso |
| 3.1: actuación coherente | Código y demo informada cubren los tres estados; falta registro legible que vincule lecturas y LED físicos |
| 3.1: conectividad estable | USB y monitor visibles/documentados. Falta registro continuo; no hay confirmación del feedback docente sobre aceptación de USB para el criterio IoT |
| 3.1: mínimo cinco minutos | La demo fue informada como exitosa, pero no se guardó el registro final. No se marca el requisito como demostrado documentalmente. [Protocolo propuesto](../testing/protocolo_avance2.md) |
| 3.2: volumen e integración | Concepto y justificación disponibles; completar visualización de componentes en el volumen y contrastar medidas reales. No hace falta imprimir para esta entrega |
| 3.3: iteración y aporte ODS | Problemas, mejoras y aporte parcial agrícola documentados; ahorro y rendimiento no medidos no se atribuyen como logros |
| 3.4: replicabilidad | Código, funciones, dependencias y circuitos disponibles; versión exacta del núcleo y HTML original por aportar |
| 4 y 5: participación y preparación | Faltan roles reales, ensayos previos, tiempos y feedback documentados. Las recomendaciones de tres pruebas y checklist de dos ensayos no se marcan realizados sin respaldo |

## Comunicación de esta entrega

La guía indica demo de 5–7 minutos más 2 de feedback y participación de todos. Un orden de apoyo, sin afirmar que fue el realizado, es: problema agrícola y aporte ODS; flujo sensor→cálculo→LED→USB; funcionamiento del banco; concepto de caja; iteraciones, límites y próximos pasos. La operación puede mantenerse en paralelo durante la explicación para mostrar integración. Falta registrar quién realizó cada función y el feedback recibido; no se inventan roles retrospectivos.

La rúbrica publicada asigna 36 % a funcionalidad, 21 % a integración, 14 % a encapsulado, 14 % a iteración/testeo, 7 % a documentación y 7 % a comunicación. Se conservan los valores publicados aunque sumen 99 %. Esta revisión no predice la nota: identifica contenido corregido y evidencia que el evaluador tendría que observar o recibir.
