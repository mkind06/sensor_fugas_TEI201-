# Fuentes, librerías y uso de IA

Declaración de todo lo que el proyecto usa y que no fue escrito desde cero por el equipo, según la guía del Avance 3 de TEI201.

## 1. Librerías y dependencias

| Librería / herramienta | Versión | Uso en el proyecto | Fuente |
|---|---|---|---|
| Núcleo Arduino-ESP32 (Espressif) | [completar: Herramientas → Placa → Gestor de tarjetas] | Soporte de la ESP32-S3 en Arduino IDE: `digitalRead`, `millis`, `micros`, `Serial` | https://github.com/espressif/arduino-esp32 |
| Arduino IDE | 1.8.19 | Compilar y cargar el firmware | https://www.arduino.cc/en/software |
| Web Serial API del navegador | Incluida en Chrome/Edge | `Panel_USB_Real.html` lee por USB las líneas que envía la ESP32 | https://developer.mozilla.org/es/docs/Web/API/Web_Serial_API |
| [completar: librerías del tablero Riego Monitor] | | Tablero con gráficos y registro CSV | |

`PruebaSensor.ino` no usa librerías externas: solo el núcleo Arduino-ESP32.

## 2. Código externo adaptado

[Completar si usaron fragmentos de tutoriales, GitHub o foros. Si no usaron ninguno, dejar escrito: "No se usó código externo fuera de lo declarado en la sección 3."]

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

### Tablero Riego Monitor
- **Herramienta:** [completar: herramienta usada, o "escrito por el equipo"].
- **Uso:** [completar].

### Encapsulado y gemelo 3D (`diseno_3d/`)
- **Herramienta:** Claude (Anthropic), noviembre de 2026, con CadQuery (Python).
- **Uso:** modelo de la caja (STEP), planos DXF, ensamble con volúmenes referenciales de los componentes, gemelo de la demo completa, renders y visor web. Los scripts están en `diseno_3d/cad/fuente/`.
- **Adaptación del equipo:** se definieron los requisitos: tapa atornillada para reparar, ventana USB-C, prensaestopas para los sensores y LED visibles en la tapa. [Completar: cambios hechos en Fusion 360].
- **Comprensión:** la caja mide 120 × 85 × 43 mm. La tapa se fija con 4 tornillos M3 en torretas, así se abre sin romper nada. La ESP32 va en cabezales hembra sobre la placa perforada y se reemplaza sin desoldar.

### Documentación y presentación
- **Herramienta:** Claude (Anthropic), octubre y noviembre de 2026.
- **Uso:** borradores de README, informe, esquema de conexiones y presentación final.
- **Adaptación del equipo:** los datos, mediciones, costos y decisiones de diseño son del equipo; se revisaron y corrigieron antes de entregar.

## Declaración

El equipo puede explicar cada función del código, incluidas las generadas con IA.
