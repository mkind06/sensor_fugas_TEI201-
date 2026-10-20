# Detector de fugas con dos sensores de flujo para riego agrícola

**Curso:** TEI201 – Taller de Diseño en Ingeniería · **Avance #2 (Prototipo Alpha IoT)**
**ODS:** 6 – Agua limpia y saneamiento (meta 6.4) · relacionado con ODS 2

Dos sensores de flujo en serie miden el caudal al inicio y al final de un tramo de la línea de riego. Una ESP32-S3 compara ambos caudales cada 10 s: si sale menos agua de la que entra, la diferencia se está perdiendo entre los dos puntos y el sistema enciende un LED de alerta.

| LED | Condición | Significado |
|---|---|---|
| Apagados | Q1 < 0,5 L/min | Sin flujo |
| Verde | Diferencia < 10 % | Normal |
| Amarillo | 10 % ≤ diferencia < 25 % | Posible fuga |
| Rojo | Diferencia ≥ 25 % | Fuga |

**Diferencia (%) = (Q1 − Q2) / Q1 × 100**

---

## 1. Problema y aporte al ODS
- **Problema:** en líneas de riego largas de huertos (avellanos, cerezos), las fugas por roturas o uniones sueltas pasan inadvertidas y desperdician agua.
- **Qué resuelve el prototipo:** detecta automáticamente que el agua que sale de un tramo es menor que la que entra, y alerta visualmente.
- **Aporte al ODS 6.4:** uso eficiente del agua; reducir pérdidas en riego agrícola.
- **Próximos pasos:** conectividad remota, varios tramos monitoreados, alimentación solar y sensores ajustados al caudal real de la línea.

## 2. Arquitectura
```
 Bomba ──► Sensor 1 (FS400A) ──► Llave de fuga ──► Sensor 2 (FS400A) ──► Recipiente
              │ pulsos                                 │ pulsos
              ▼                                        ▼
         divisor 10k/20k                         divisor 10k/20k
              │                                        │
              └──────► ESP32-S3 Super Mini ◄───────────┘
                       (GPIO1, GPIO2)
                             │
              ┌──────────────┼──────────────┐
           GPIO4          GPIO5          GPIO6
         LED verde     LED amarillo     LED rojo
                             │
                    USB → Monitor Serie
               (WiFi: pendiente, ver estado)
```

## 3. Estado frente a la guía del Avance #2
| Requisito | Estado |
|---|---|
| Sensor capturando datos en tiempo real | ✅ Listo |
| Actuador respondiendo al sensor (LED) | ✅ Listo |
| Conectividad (WiFi/Bluetooth) y transmisión de datos | ❌ Pendiente |
| Sistema estable mínimo 5 minutos | ⚠️ Por medir |
| Modelo 3D del encapsulado con justificación | ✅ Listo |
| Código comentado | ✅ Listo |
| Diagrama de circuito | ⚠️ Esquema en texto; falta imagen (Fritzing/Wokwi) |
| Registro de iteraciones | ✅ Listo |

## 4. Mapa del repositorio
| Archivo / carpeta | Contenido |
|---|---|
| `firmware/PruebaSensor/PruebaSensor.ino` | Código comentado del prototipo |
| `Código Fuente`, `Software - Documentación`, `Documentación de Software`, `Librerías` | Software: estructura, instalación, funciones, operación |
| `Hardware - Documentación`, `Esquemas de Circuito`, `Bill of Materials (BOM)`, `Fotografías del Prototipo` | Hardware: pines, conexiones, materiales |
| `Diseño 3D - Documentación`, `Archivos Fusion 360`, `Planos Técnicos`, `Renders de Alta Calidad` | Encapsulado |
| `Historial de Iteraciones`, `Iteración 1…`, `Iteración 2…`, `Iteración 3…` | Evolución del prototipo |
| `Testing y Validación`, `Datos de Testing`, `Reportes de Testing`, `Evidencias de Testing` | Pruebas y resultados |
| `Documentación del Proyecto`, `Reporte Final del Proyecto`, `Presentación Final` | Entregables y demo |

## 5. Inicio rápido
1. Arduino IDE → placa **ESP32S3 Dev Module**, **USB CDC On Boot: Enabled**.
2. Abrir y subir `firmware/PruebaSensor/PruebaSensor.ino` (no requiere librerías externas).
3. Monitor Serie a **115200** baudios.
4. Alimentar la bomba con **su propio cargador** (nunca desde el mismo PC que la ESP32).

## Licencia
MIT – ver `LICENSE`.
