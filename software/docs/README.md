# Documentación de Software - Avance 2

## Funciones

| Función | Responsabilidad |
|---|---|
| setup() | Inicia Serial a 115200, LED apagados e INPUT para sensores |
| muestrear(i) | Lee el canal 0 o 1; actualiza nivel, cuenta y pulsos tras cinco lecturas consecutivas |
| luces(v,a,r) | Escribe HIGH/LOW en GPIO4/5/6 |
| loop() | Programa muestreo, calcula cada 10 s nominales, clasifica y reporta |

El filtro exige estabilidad de varias muestras; no demuestra que todo ruido se descarte ni que se cubra toda la frecuencia del rango comercial del sensor. La [arquitectura](../README.md) describe fórmulas, parámetros y límites.

## Instalación y operación

1. Revisar [conexiones](../../hardware/esquemas/README.md), polaridad, uniones hidráulicas y recorrido de la derivación. La bomba debe estar sumergida y tener retorno de agua.
2. Conectar ESP32 al computador con USB de datos y alimentar la bomba desde fuente USB independiente. La bomba se acciona manualmente.
3. Consultar el Monitor Serie a 115200 o abrir el [panel reconstruido](../src/web/Panel_USB_Real.html), descargarlo y ejecutarlo en un contexto que permita Web Serial. Si el archivo local no habilita la API, servir la carpeta desde localhost.
4. Para usar el panel, cerrar Monitor Serie y otras páginas que ocupen el puerto. Pulsar Conectar, seleccionar la placa y esperar unos 10–15 s para la primera línea; conectar puede reiniciar la placa.
5. Con la derivación cerrada observar las lecturas; abrirla gradualmente y contrastar diferencia, LED y agua desviada. Verde significa Dif<10 %, amarillo 10–25 % y rojo desde 25 %, siempre que Q1≥0,5. Una lectura negativa también es verde según esta lógica.
6. Exportar CSV antes de cerrar. El panel reconstruido conserva hasta 3600 registros locales, distingue desconexión, espera y datos vencidos a los 25 s, y etiqueta USB como ESP32_USB_REAL. No incluye el gráfico ni todas las funciones del panel anterior no localizado.
7. Apagar primero la bomba, desconectar placa y vaciar/secar el montaje para guardarlo.

## Diagnóstico

| Síntoma | Comprobación y acción |
|---|---|
| COM ocupado | Cerrar monitor y otras aplicaciones del puerto; reconectar |
| Sin salida USB | Revisar cable de datos, puerto, 115200 y USB CDC On Boot |
| setup/loop redefinidos | Separar programas completos en carpetas diferentes |
| Pulsos sin flujo | Revisar cableado y alimentación; hubo asociación con bomba conectada al PC |
| Q=0 con bomba encendida | Revisar boquilla, aire, sentido y si giran las turbinas; puede haber caudal insuficiente |
| Amarillo sin pérdida intencional | Comparar incrementos simultáneos y revisar ajuste; no forzar verde cambiando umbrales |
| LED incorrecto | Comprobar GND real y orientación de ánodo/cátodo |

La ventana de 10 s no prueba un tiempo de respuesta de 10–20 s. Q2=0 puede responder a flujo bajo; el rojo por sí solo no cuantifica una pérdida total. El panel clasifica números redondeados, por lo que cerca de umbrales puede diferir del cálculo interno de la placa.
