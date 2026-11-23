# Iteración 3 - Prototipo IoT (Avance 3)

**Fecha:** 22–23 de noviembre de 2026 · **Versión:** v3

## Qué cambió respecto a v2

| Área | v2 (Alpha) | v3 | Por qué |
|---|---|---|---|
| Banco hidráulico | Mangueras y depósito | PVC 32 mm, dos FS400A, tee con válvula de bola | Circuito rígido y repetible; la válvula da fugas controladas |
| Electrónica | 2 protoboards con jumpers | Placa perforada soldada, ESP32 en cabezales hembra, conectores de 3 pines por sensor | Conexiones firmes y piezas reemplazables sin desoldar |
| Alimentación | USB del computador | Fuente propia en 5V/GND; bomba con fuente aparte | Opera sin computador; evita reinicios por la bomba |
| Conectividad | USB serie | Red WiFi propia + servidor web en la ESP32 (y USB) | Los datos se ven en cualquier celular o PC |
| Firmware | Sondeo cada 0,2 ms, ventana fija de 10 s | Interrupciones con antirrebote 2 ms, publicación cada 1 s, promedio móvil de 5 s | Respuesta más rápida sin perder estabilidad |
| Dashboard | Panel USB básico | Dashboard con semáforo, indicadores, gráficos, eventos, tiempo por estado, calibración y CSV | Convierte los datos en información para decidir |
| Encapsulado | Concepto con protoboards | Caja v3 con placa perforada, tapa atornillada, PG7 y LED en la tapa | Diseño para la reparación ([diseño 3D](../../diseno_3d/README.md)) |

## Problemas de esta iteración

Los cuatro problemas del soldado y la integración (LED amarillo sin tierra, reinicios por la bomba, sensor 2 en el pin equivocado y sensor 1 sin lectura) están analizados en [testing/resultados_avance3.md](../../testing/resultados_avance3.md).

## Estado al cierre

- Funcionando: ESP32 con fuente propia, red WiFi y dashboard en otro dispositivo, tres LED, sensor 2, firmware publicando cada segundo, registro CSV.
- Pendiente: reparar el divisor del sensor 1 para medir la diferencia entrada-salida con agua; calibración contra volumen conocido; histórico en la nube.
