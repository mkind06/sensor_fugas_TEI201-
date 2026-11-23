# Guion de la demo en vivo (Avance 3)

**Antes de empezar:** ESP32 con su fuente, sensores conectados (amarillo / rojo / negro), bomba sumergida sin aire, válvula de fuga cerrada, celular conectado a la red `RiegoMonitor` con `http://192.168.4.1` abierto y **Nueva sesión** pulsada.

| Min | Qué se muestra | Qué se dice |
|---|---|---|
| 0:00 | Banco: bidón → bomba → sensor 1 → tee con válvula → sensor 2 → bidón | El problema: pérdidas de agua en un tramo de riego; si sale menos de lo que entra, hay fuga |
| 1:00 | Caja abierta: ESP32 en cabezales, conectores de sensores, tapa con 4 tornillos | Diseño para la reparación: cada pieza se cambia sin desoldar |
| 2:00 | Celular del evaluador conectado a `RiegoMonitor` | La ESP32 funciona sola con su fuente y publica los datos cada segundo a cualquier dispositivo |
| 2:30 | Bomba encendida: caudal del sensor 2 en el dashboard | Medición real en L/min; el estado se calcula con un promedio de 5 s |
| 3:30 | Botones Normal → Advertencia → Fuga | Modo demo **simulado** (marcado en pantalla y CSV) mientras se repara el sensor 1: LED físicos y dashboard cambian juntos |
| 4:30 | Gráficos, eventos, tiempo por estado, agua perdida | La información que permite decidir: cuándo empezó la fuga, cuánta agua se pierde |
| 5:00 | Descargar CSV | Registro estructurado de cada lectura con su origen |
| 5:30 | Repositorio y página GitHub Pages | Código, esquemas, 3D, pruebas y fuentes |

**Plan B:** si falla el WiFi, conectar la ESP32 al notebook por USB y abrir `docs/index.html` (o GitHub Pages) → Conectar ESP32 por USB.
