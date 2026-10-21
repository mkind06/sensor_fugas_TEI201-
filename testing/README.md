# Testeo - Avance 2

## Propósito

Documentar las pruebas de mesa, los problemas detectados y las evidencias disponibles del Alpha. La evaluación actual exige funcionamiento real, integración e iteración; no convierte las plantillas de encuestas y usuarios de etapas posteriores en resultados.

| Evidencia | Procedencia y alcance |
|---|---|
| Logs iniciales | Diagnóstico de un sensor y lecturas cero de dos sensores; [transcripción](datos/diagnostico.md) |
| Siete lecturas físicas | Condición sin fuga intencional, K1=288/K2=275, ventana 10 s; [CSV](datos/lecturas_preajuste.csv) |
| Ajuste relativo | 288×(716−411)/(854−470)=228,75≈229 pulsos/L |
| Testeo de verde | 30 escenarios sintéticos nuevos, claramente identificados; [metodología](datos/testeo_verde.md) |
| Presentación | Equipo informó que funcionaron normalidad, advertencia y fuga; observación cualitativa sin CSV final |

## Interpretación

Las siete mediciones transmiten diferencias de 13,0–19,4 %, por lo que el algoritmo indicó POSIBLE FUGA / AMARILLO. Como no se introdujo una fuga en esa condición, el resultado mostró la necesidad de revisar la relación entre sensores. Se conservan los números originales, incluidos sus redondeos.

El ajuste relativo usa incrementos del mismo intervalo (384 y 305 pulsos), no la razón acumulada desde arranque. Supone flujo equivalente por ambos sensores y no reemplaza una calibración absoluta con litros recogidos. El resultado de la demo se informa por separado; no se atribuye un registro inexistente a esa presentación.

## Comprobaciones pendientes

Para respaldar la estabilidad mínima de cinco minutos de la guía falta una corrida física continua de la configuración final. Debe registrar hora, Q1/Q2, diferencia, pulsos, estado, apertura de derivación e interrupciones. Repetir con llave cerrada, parcialmente abierta y abierta, contrastando el agua desviada mediante recipiente de referencia.

No se midieron exactitud absoluta, demora, corriente, tasa de falsas alarmas, ahorro de agua ni satisfacción. Un sensor detenido a bajo caudal puede indicar Q2=0 sin pérdida total. Las [evidencias visuales](evidencias/README.md) y los [reportes de usuarios](reportes/README.md) conservan sus pendientes anteriores; no se inventan sesiones ni participantes.
