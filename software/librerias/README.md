# Librerías y entorno - Avance 3

| Dependencia | Versión | Uso |
|---|---|---|
| Arduino IDE | 1.8.19 (Windows Store 1.8.57.0) | Compilar y cargar |
| Núcleo Arduino-ESP32 (Espressif) | 2.x o 3.x (el firmware solo usa `attachInterrupt`, `WiFi.softAP` y `WebServer`, presentes en ambas) | GPIO, interrupciones, `Serial` |
| `WiFi.h` | Incluida en el núcleo ESP32 | Red propia (modo AP) o conexión a hotspot (modo STA) |
| `WebServer.h` | Incluida en el núcleo ESP32 | Servidor HTTP: rutas `/`, `/data`, `/cmd` |
| Web Serial API | Chrome / Edge | Dashboard por USB |

No se instalan librerías externas. Los dashboards usan solo HTML, CSS y JavaScript propios (gráficos dibujados en `<canvas>`), por lo que funcionan sin internet.

---

# Librerías y entorno - Avance 2 (antecedente)

| Dependencia | Versión conocida | Uso |
|---|---|---|
| Arduino IDE | 1.8.19; Windows Store 1.8.57.0 informado | Edición y carga del sketch |
| Núcleo Arduino-ESP32 | 2.x o 3.x | GPIO, temporización y Serial de ESP32-S3 |
| Bibliotecas externas de sensores | Ninguna | Los FS400A se leen como señales digitales |
| Bibliotecas web externas | Ninguna en el panel reconstruido | HTML/CSS/JavaScript y Web Serial |

Configuración usada: ESP32S3 Dev Module, USB CDC On Boot Enabled y Monitor Serie 115200. El registro previo indica flash 4 MB, QIO 80 MHz, CPU 240 MHz y carga 921600. No hace falta instalar una biblioteca FS400A ni WiFi para este programa.

No hay librerías personalizadas que copiar manualmente.
