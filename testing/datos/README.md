# Testeo: datos disponibles del Alpha

## Mediciones físicas previas al ajuste

[lecturas_preajuste.csv](lecturas_preajuste.csv) transcribe las siete filas del monitor conservadas en el traspaso. Condición: sin fuga intencional; K1=288 y K2=275 pulsos/L; ventana nominal 10 s. No se conoce la fecha individual de adquisición, por eso solo se conserva la hora recibida.

| Hora | Q1 L/min | Q2 L/min | Dif % | Tot1 | Tot2 | Razón |
|---|---:|---:|---:|---:|---:|---:|
| 12:38:21.249 | 1,35 | 1,18 | 13,0 | 470 | 411 | 0,874 |
| 12:38:31.283 | 1,37 | 1,16 | 15,9 | 536 | 464 | 0,866 |
| 12:38:41.267 | 1,35 | 1,09 | 19,4 | 601 | 514 | 0,855 |
| 12:38:51.247 | 1,29 | 1,05 | 18,9 | 663 | 562 | 0,848 |
| 12:39:01.286 | 1,29 | 1,07 | 17,2 | 725 | 611 | 0,843 |
| 12:39:11.254 | 1,33 | 1,11 | 16,5 | 789 | 662 | 0,839 |
| 12:39:21.251 | 1,35 | 1,18 | 13,0 | 854 | 716 | 0,838 |

**Estado indicado en todas las filas:** POSIBLE FUGA / AMARILLO. Esto no confirma una fuga física. Dif conserva el porcentaje transmitido, que puede diferir del recalculado a partir de caudales redondeados. Tot1/Tot2 son pulsos acumulados.

## Ajuste posterior

Entre la primera y última fila: ΔTot1=384 y ΔTot2=305. K2=288×305/384=228,75≈229 pulsos/L. El ajuste iguala relativamente la respuesta bajo el supuesto de caudal equivalente; K1 también queda por calibrar con volumen conocido.

## Testeo de verde

[testeo_verde.csv](testeo_verde.csv) contiene 30 escenarios nuevos con origen DATOS_SINTETICOS y tiempo virtual 10–300 s. El CSV anterior mencionado en el traspaso no se encontró y no se afirma haberlo recuperado. Ver [metodología y límites](testeo_verde.md). Las filas no tienen totales, pulsos o fechas físicas inventadas.

Los [logs de diagnóstico](diagnostico.md) y los resúmenes históricos se conservan separados. No hay un CSV continuo de la presentación, hojas de usuarios ni comparativas de ahorro disponibles.
