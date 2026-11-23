# Fuentes, librerías y uso de IA

Declaración de todo lo que el proyecto usa y que no fue escrito desde cero por el equipo, según la guía del Avance 3 de TEI201.

## 1. Librerías y dependencias

| Librería / herramienta | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| Núcleo Arduino-ESP32 (Espressif) | [completar: Herramientas → Placa → Gestor de tarjetas] | Soporte de la ESP32-S3 en Arduino IDE: `digitalRead`, `millis`, `micros`, `Serial` | https://github.com/espressif/arduino-esp32 |
| Arduino IDE | 1.8.19 | Compilar y cargar el firmware | https://www.arduino.cc/en/software |
| Web Serial API del navegador | Incluida en Chrome/Edge | `Panel_USB_Real.html` lee por USB las líneas que envía la ESP32 | https://developer.mozilla.org/es/docs/Web/API/Web_Serial_API |
| `WiFi.h` (núcleo ESP32) | Incluida en el núcleo | Red WiFi propia (modo AP) o conexión a hotspot | https://github.com/espressif/arduino-esp32/tree/master/libraries/WiFi |
| `WebServer.h` (núcleo ESP32) | Incluida en el núcleo | Servidor HTTP de la ESP32: rutas `/`, `/data`, `/cmd` | https://github.com/espressif/arduino-esp32/tree/master/libraries/WebServer |
| Dashboards web | — | HTML, CSS y JavaScript propios; gráficos dibujados en `<canvas>`, sin librerías externas | — |

`PruebaSensor.ino` y `RiegoMonitor_WiFi.ino` no usan librerías externas: solo el núcleo Arduino-ESP32 y sus librerías incluidas.

## 2. Código externo adaptado

No se copió código de tutoriales, foros ni otros repositorios. El firmware y los dashboards se desarrollaron con asistencia de IA (sección 3) a partir del firmware de Avance 2 del equipo. Las rutas del servidor web siguen el patrón de uso documentado de `WebServer.h` (`server.on`, `server.send`) en los ejemplos de Espressif.

## 3. Uso de Inteligencia Artificial

### Firmware de medición (`software/src/PruebaSensor/PruebaSensor.ino`)
- **Herramienta:** Claude (Anthropic), octubre y noviembre de 2026.
- **Uso:** estructura del programa, conteo de pulsos sin interrupciones con filtro anti-ruido, cálculo de caudal por ventana y lógica de los LED.
- **Adaptación del equipo:** se eligieron los pines según el cableado real (GPIO1 y GPIO2 para sensores, GPIO4, 5 y 6 para LED). Al ver ~1.300 pulsos falsos por segundo, el equipo identificó con pruebas que el ruido venía de la bomba y la alimentó por separado. La ventana se cambió de 3 s a 10 s porque la diferencia saltaba hasta 4,5 % sin cambios reales. K2 se calculó con conteos medidos por el equipo en el banco.
- **Comprensión:** la ESP32 lee los dos pines cada 0,2 ms y solo acepta un cambio de nivel si se mantiene 1 ms; así descarta picos de ruido. Cada 10 s calcula `Q = pulsos / s × 60 / K` (L/min) y `Dif = (Q1 − Q2) / Q1 × 100`. Si Q1 < 0,5 L/min no hay flujo; si Dif < 10 % enciende verde, entre 10 % y 25 % amarillo, y sobre 25 % rojo.

### Panel web por USB (`software/src/web/Panel_USB_Real.html`)
- **Herramienta:** Claude (Anthropic), noviembre de 2026.
- **Uso:** página que se conecta a la ESP32 por USB, muestra Q1, Q2, diferencia y estado, guarda las últimas lecturas y exporta CSV.
- **Adaptación del equipo:** [completar: qué cambiaron o cómo lo probaron con el prototipo].
- **Comprensión:** el navegador abre el puerto serie a 115200 baudios, lee cada línea que imprime la ESP32, extrae los números con una expresión regular y clasifica el estado con los mismos umbrales del firmware.

### Firmware final (`software/src/RiegoMonitor_WiFi/RiegoMonitor_WiFi.ino`)
- **Herramienta:** Claude (Anthropic), 22 y 23 de noviembre de 2026.
- **Uso:** conteo por interrupciones con antirrebote de 2 ms, publicación cada 1 s con promedio móvil de 5 s, lectura JSON, red WiFi propia con servidor web que entrega el dashboard, comandos `n/a/f/x/R/K1=/K2=` y modo demo identificado.
- **Adaptación del equipo:** se definieron los pines según la placa soldada (S1 movido a GPIO 8 durante el diagnóstico, S2 en GPIO 2, LED 4/5/6), se mantuvieron K1/K2 y umbrales de Avance 2, y se probó en la placa real: compiló y publicó una lectura por segundo. El reinicio `TG0WDT` al encender la bomba se resolvió separando su alimentación.
- **Comprensión:** cada pulso del sensor dispara una interrupción que suma 1 si pasaron al menos 2 ms desde el anterior. Cada segundo se guardan los pulsos del segundo en un arreglo circular de 5 posiciones; con su suma se calcula `Q = pulsos × 60 / (K × segundos)` y `Dif = (Q1 − Q2)/Q1 × 100`, que define el estado y el LED. La lectura se guarda como texto JSON que se imprime por USB y se entrega en `GET /data`; la página la pide cada segundo con `fetch`.

### Dashboards (`software/src/web/`, `docs/index.html`)
- **Herramienta:** Claude (Anthropic), 22 y 23 de noviembre de 2026.
- **Uso:** semáforo de estado, indicadores (caudales, diferencia, agua perdida), gráficos en `<canvas>`, tiempo por estado, eventos, ayuda de calibración, exportación CSV y conexión por WiFi (`fetch`) o USB (Web Serial).
- **Adaptación del equipo:** se definieron los indicadores útiles para el problema (agua perdida, tiempo en fuga, eventos) y los umbrales del proyecto. Antes de la presentación se probaron contra una ESP32 simulada con el mismo formato JSON del firmware real; la prueba con la placa se registra en [testing](testing/resultados_avance3.md).
- **Comprensión:** la página recibe una lectura por segundo, integra los caudales en el tiempo para estimar litros (`L += Q × Δt / 60`), acumula segundos por estado y registra un evento cuando el estado cambia. El K2 sugerido es `K1 × (pulsos2 / pulsos1)` medidos con la válvula cerrada.

### Encapsulado y gemelo 3D (`diseno_3d/`)
- **Herramienta:** Claude (Anthropic), noviembre de 2026, con CadQuery (Python).
- **Uso:** modelo de la caja (STEP), planos DXF, ensamble con volúmenes referenciales de los componentes, gemelo de la demo completa, renders y visor web. Los scripts están en `diseno_3d/cad/fuente/`.
- **Adaptación del equipo:** se definieron los requisitos: tapa atornillada para reparar, ventana USB-C, prensaestopas para los sensores y LED visibles en la tapa. [Completar: cambios hechos en Fusion 360].
- **Comprensión:** la caja mide 120 × 85 × 43 mm. La tapa se fija con 4 tornillos M3 en torretas, así se abre sin romper nada. La ESP32 va en cabezales hembra sobre la placa perforada y se reemplaza sin desoldar.

### Documentación y presentación
- **Herramienta:** Claude (Anthropic), octubre y noviembre de 2026.
- **Uso:** borradores de README, informe, esquema de conexiones, protocolo y resultados de pruebas de Avance 3, guion de la demo y presentación final. Los resultados de pruebas se redactaron a partir de los registros y observaciones del equipo.
- **Adaptación del equipo:** los datos, mediciones, costos y decisiones de diseño son del equipo; se revisaron y corrigieron antes de entregar.

## Declaración

El equipo puede explicar cada función del código, incluidas las generadas con IA.
