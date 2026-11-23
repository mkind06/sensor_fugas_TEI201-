# Manual de instalación y operación - Avance 3

## Cargar el firmware

1. Instalar Arduino IDE y el soporte para ESP32 (Gestor de tarjetas → *esp32* de Espressif).
2. Abrir `software/src/RiegoMonitor_WiFi/RiegoMonitor_WiFi.ino`.
3. Herramientas → Placa **ESP32S3 Dev Module**, **USB CDC On Boot: Enabled**, elegir el puerto COM.
4. Cerrar el Monitor Serie y pulsar **Subir**. Si no conecta: mantener **BOOT** mientras se enchufa el USB y volver a subir.
5. Abrir el Monitor Serie a 115200: debe aparecer `WiFi: red propia "RiegoMonitor" ... Abre http://192.168.4.1` y luego una línea JSON por segundo.

Opcional: completar `HOTSPOT_SSID` y `HOTSPOT_PASS` con un hotspot de 2,4 GHz para que la ESP32 se una a esa red; la IP aparece en el Monitor Serie.

## Operar con WiFi (sin computador)

1. Alimentar la ESP32 con su fuente por los pines **5V** y **GND** (no conectar fuente y USB a la vez). La bomba usa su propia fuente.
2. Conectar los sensores al conector de la placa: **amarillo** (señal, a la altura de la resistencia de 10 kΩ), **rojo** (5 V) y **negro** (GND).
3. Desde un celular o PC conectarse a la red **RiegoMonitor** (clave `riego1234`) y abrir **http://192.168.4.1**. Varias personas pueden verlo a la vez.
4. Pulsar **Nueva sesión**, encender la bomba con la llave de fuga cerrada y comprobar que ambos caudales suben.
5. Abrir la llave de fuga gradualmente y observar diferencia, estado y LED.
6. Al terminar pulsar **Descargar CSV**.

## Operar por cable USB (respaldo o GitHub Pages)

Conectar la ESP32 al computador, abrir [docs/index.html](../../docs/index.html) (o la página de GitHub Pages) en Chrome o Edge y pulsar **Conectar ESP32 por USB**. Funciona con el mismo firmware.

## Modo demo

Los botones **Normal / Advertencia / Fuga** fijan caudales simulados en la placa (3,80 → 3,75 / 3,30 / 2,60 L/min), mueven los LED físicos y el dashboard, y quedan marcados como `DEMO SIMULADO` en pantalla y en el CSV. **Datos reales** vuelve a los sensores.

## Diagnóstico rápido

| Síntoma | Acción |
|---|---|
| No aparece la red RiegoMonitor | Revisar alimentación (LED rojo de la placa) y reiniciar |
| 192.168.4.1 no carga | El celular se cambió a otra red: volver a RiegoMonitor y escribir `http://` completo |
| Caudal 0 con bomba encendida | Aire en la bomba, flecha del sensor al revés o caudal bajo el mínimo del FS400A |
| La ESP32 se reinicia al encender la bomba (`rst:0x7 TG0WDT`) | Alimentar la bomba con fuente independiente y alejar sus cables de la placa |
| Un sensor no cuenta ni al soplarlo | Enchufarlo en el conector del otro sensor: si allí cuenta, la falla está en la placa (divisor o cable de señal) |

---

# Documentación de Software - Avance 2 (antecedente)

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
5. Con la derivación cerrada observar las lecturas; abrirla gradualmente y contrastar diferencia, LED y agua desviada. Verde significa Dif<10 %, amarillo 10≤Dif<25 % y rojo Dif≥25 %, siempre que Q1≥0,5. Una lectura negativa también es verde según esta lógica.
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
