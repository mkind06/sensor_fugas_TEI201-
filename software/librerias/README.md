# Librerías y entorno - Avance 2

| Dependencia | Versión conocida | Uso |
|---|---|---|
| Arduino IDE | 1.8.19; Windows Store 1.8.57.0 informado | Edición y carga del sketch |
| Núcleo Arduino-ESP32 | Versión exacta pendiente | GPIO, temporización y Serial de ESP32-S3 |
| Bibliotecas externas de sensores | Ninguna | Los FS400A se leen como señales digitales |
| Bibliotecas web externas | Ninguna en el panel reconstruido | HTML/CSS/JavaScript y Web Serial |

Configuración usada: ESP32S3 Dev Module, USB CDC On Boot Enabled y Monitor Serie 115200. El registro previo indica flash 4 MB, QIO 80 MHz, CPU 240 MHz y carga 921600; no sustituye registrar la versión del núcleo. No hace falta instalar una biblioteca FS400A ni WiFi para este programa.

No hay librerías personalizadas que copiar manualmente. Las versiones pendientes deben obtenerse del entorno real antes de declarar reproducibilidad exacta de la compilación.
