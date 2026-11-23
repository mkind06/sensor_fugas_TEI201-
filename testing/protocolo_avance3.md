# Protocolo de pruebas - Avance 3

Objetivo general: comprobar que el sistema mide el caudal en la entrada y la salida de un tramo, detecta una pérdida entre ambos sensores, la señala con los LED y la muestra en un dashboard en otro dispositivo, y que los datos quedan registrados.

**Condiciones comunes:** banco de PVC 32 mm con recirculación desde el bidón; bomba sumergible 5 V con fuente propia; ESP32-S3 con firmware `RiegoMonitor_WiFi.ino` (K1 = 288, K2 = 229, ventana 5 s, publicación 1 s); válvula de bola en la tee entre los sensores como fuga controlada.

| ID | Prueba | Procedimiento | Criterio de éxito | Evidencia |
|---|---|---|---|---|
| P1 | Salidas LED | Cargar un programa que encienda GPIO 4, 5 y 6 en secuencia (0,5 s cada uno) | Cada LED enciende en su turno y solo él | Foto / video corto |
| P2 | Lectura de cada sensor | Sin bomba, soplar o girar la turbina de cada sensor por separado mirando los pulsos | Solo aumentan los pulsos del sensor soplado | Captura del Monitor Serie o dashboard |
| P3 | Firmware y publicación | Cargar el firmware y abrir el Monitor Serie | Una línea JSON por segundo, `seq` correlativo, `SIN_FLUJO` sin agua | Captura del Monitor Serie |
| P4 | Inmunidad al ruido de la bomba | Encender y apagar la bomba 5 veces con la placa energizada | Sin reinicios (`rst:`) y sin pulsos con las turbinas detenidas | Log serie |
| P5 | Caudal sin fuga | Válvula de fuga cerrada; bomba encendida 2 min; luego Descargar CSV | Q1 y Q2 > 0,5 L/min; diferencia < 10 % → verde. Si no, recalibrar K2 con la razón T2/T1 | CSV + captura |
| P6 | Fuga controlada | Abrir la válvula a ½ y luego completa, 1 min cada una; recoger el agua desviada en un recipiente y medir el volumen | Diferencia sube y el estado pasa a amarillo / rojo; el volumen perdido estimado por el dashboard se compara con el recogido | CSV + volumen medido |
| P7 | Dashboard en otro dispositivo | Celular conectado a `RiegoMonitor`, abrir 192.168.4.1; cronometrar desde que se cambia la válvula hasta que cambia el estado | Datos visibles en el celular; cambio de estado en ≤ 6 s (1 s de publicación + 5 s de ventana) | Video / captura |
| P8 | Estabilidad | Sistema funcionando 5 min seguidos con bomba encendida | Sin cortes de datos ni reinicios; eventos registrados | CSV de 5 min |
| P9 | Modo demo identificado | Pulsar Normal / Advertencia / Fuga / Datos reales | LED y dashboard cambian; el CSV marca esas filas `ESP32_DEMO_SIMULADO` | CSV |

Los resultados se registran en [resultados_avance3.md](resultados_avance3.md) y los CSV en [datos/](datos/README.md).
