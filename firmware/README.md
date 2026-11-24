# Firmware

El código de la ESP32 está en [`software/src/`](../software/src/README.md):

| Archivo | Uso |
|---|---|
| [`RiegoMonitor_WiFi/RiegoMonitor_WiFi.ino`](../software/src/RiegoMonitor_WiFi/RiegoMonitor_WiFi.ino) | **Firmware final (Avance 3):** mide ambos sensores, enciende los LED, crea la red WiFi `RiegoMonitor` y sirve el dashboard |
| [`PruebaSensor/PruebaSensor.ino`](../software/src/PruebaSensor/PruebaSensor.ino) | Firmware del Avance 2 (solo USB), antecedente |

Instrucciones de carga en el [README principal](../README.md#cómo-usarlo). No requiere librerías externas ([detalle](../software/librerias/README.md)).
