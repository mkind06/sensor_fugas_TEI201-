# Hardware - Avance 3

## Cambios respecto a Avance 2

| Avance 2 | Avance 3 | Motivo |
|---|---|---|
| Dos mini protoboards con jumpers | Placa perforada 5 × 7 cm soldada | Conexiones firmes que no se sueltan al mover el banco (requisito de montaje y de la guía) |
| ESP32 enchufada en protoboard | ESP32 sobre **cabezales hembra soldados** | Se retira y reemplaza sin desoldar (diseño para la reparación) |
| Sensores directo a la protoboard | **Conectores de 3 pines** por sensor + cables macho-macho | Cada sensor se desconecta en segundos para cambiarlo o moverlo |
| ESP32 alimentada por el USB del PC | **Fuente propia** por pines 5V/GND; USB solo para programar | El sistema opera sin computador |
| Comunicación USB serie | **WiFi propio** con dashboard en el navegador + USB | Los datos se ven en otro dispositivo |
| Banco con mangueras | Banco de PVC 32 mm con válvula de bola como fuga | Circuito rígido, repetible ([fotos](fotos/README.md)) |
| S1 en GPIO 1 | S1 en GPIO 8 | Cambio durante el diagnóstico de la placa soldada (ver [testing](../testing/resultados_avance3.md)) |

## Justificación de componentes

| Componente | Por qué |
|---|---|
| ESP32-S3 Super Mini | WiFi integrado para el dashboard, interrupciones por hardware para contar pulsos de dos sensores, 3,3 V lógicos, tamaño 22 × 18 mm que cabe en la caja, bajo costo (~CLP 10.000) |
| 2 × FS400A G1 (efecto Hall) | Rosca de 1" compatible con tubería de riego, salida de pulsos proporcional al caudal (lectura digital sin ADC), rango comercial 1–60 L/min y ±5 % según la ficha, alimentación 5–18 V. Usar dos sensores iguales permite comparar entrada y salida del tramo |
| Divisores 10 kΩ / 20 kΩ | La salida del FS400A va a 5 V y el GPIO tolera 3,3 V: 5 × 20/30 = 3,33 V. Las resistencias altas consumen < 0,2 mA |
| LED verde / amarillo / rojo con resistencia en serie | Alerta local visible en terreno sin necesidad de pantalla; cada LED a ~2–3 mA desde un GPIO |
| Cabezales hembra y conectores de 3 pines | Permiten reemplazar la ESP32 o un sensor sin herramientas |
| Mini bomba sumergible 5 V con fuente aparte | Simula el riego en el banco; su fuente independiente evita el ruido y los reinicios observados al compartir alimentación |
| Válvula de bola en una tee entre sensores | Fuga controlada y repetible para validar los tres estados |

## Alimentación

- **ESP32 y sensores:** fuente de 5 V a los pines **5V** y **GND** de la placa; los sensores toman 5 V desde la misma línea. No conectar la fuente y el USB del computador al mismo tiempo.
- **Bomba:** powerbank / fuente USB propia con empalmes WAGO, sin conexión eléctrica con la placa.

## Diseño para la reparación

| Pieza | Cómo se cambia |
|---|---|
| ESP32 | Se desenchufa de los cabezales hembra |
| Sensor de flujo | Se desconectan sus 3 cables del conector y se desenrosca del PVC |
| Placa completa | Sale de la caja quitando los 4 tornillos M3 de la tapa ([diseño 3D](../diseno_3d/README.md)) |
| Bomba | Conexión por WAGO, se suelta sin herramientas |

Los detalles de cada soldadura, el esquema y las coordenadas están en [esquemas](esquemas/README.md).

---

# Hardware - Avance 2 (antecedente)

## Sistema construido

Dos FS400A G1 envían pulsos a una ESP32-S3 Super Mini. Tres LED muestran la clasificación. El banco hidráulico sigue el recorrido depósito → bomba → sensor 1 → derivación con llave → sensor 2 → retorno al depósito. La salida lateral introduce una pérdida controlada entre los sensores; debe recogerse o conducirse según el montaje. Las flechas de ambos sensores siguen el flujo.

La placa se conecta al computador mediante USB-C de datos; su pin 5 V alimenta los sensores. La bomba blanca de modelo no identificado utiliza una fuente USB de 5 V independiente. El rango 3–6 V de la bomba fue informado en los materiales de la universidad. La batería y módulo 18650 se probaron durante el desarrollo, pero no son la alimentación funcional actual.

| Pin | Función |
|---|---|
| GPIO1 | Señal S1 mediante divisor 10 kΩ / 20 kΩ |
| GPIO2 | Señal S2 mediante divisor 10 kΩ / 20 kΩ |
| GPIO4 | LED verde con 330 Ω |
| GPIO5 | LED amarillo con 330 Ω |
| GPIO6 | LED rojo con 330 Ω |
| 5 V / GND | Alimentación y retorno de sensores |

## Ensamblaje

1. Montar el recorrido hidráulico y verificar la unión de boquilla y manguera. Mantener los empalmes eléctricos fuera del agua.
2. Cablear los divisores, LED y tierra común según el [esquema y las coordenadas](esquemas/README.md).
3. Unir GND de placa, sensores y ambas protoboards. Cada señal amarilla pasa por 10 kΩ al nodo GPIO, y desde ese nodo por 20 kΩ a GND. A 5 V nominales se obtienen 3,33 V nominales; no se midió la tensión efectiva.
4. Conectar positivo USB de la bomba a su rojo y retorno a negro mediante dos empalmes WAGO separados. Los dos puertos de cada WAGO 221-412 están unidos: cada conector corresponde a una sola polaridad.
5. Alimentar placa por USB de datos y bomba por su fuente independiente; seguir el [manual](../software/docs/README.md).

No conectar señal de 5 V directamente al GPIO, ni alimentar la bomba desde un GPIO o 3V3. El divisor documentado corresponde a sensores alimentados a 5 V; no conserva compatibilidad si se aumenta su alimentación a 12 o 18 V.

## Decisiones y problemas resueltos

Se corrigieron el retorno de un LED conectado a 3V3 y la polaridad del rojo. Se separó la alimentación de la bomba después de observar conteos espurios asociados a su conexión al computador. Se añadió un filtro por estabilidad y se selló una unión hidráulica que dejaba escapar agua antes de impulsar las turbinas. El mecanismo eléctrico del ruido no fue medido con instrumental.

Los FS400A se identifican por el modelo real del montaje. Su ficha comercial anuncia 1–60 L/min y precisión ±5 %; esas cifras son del vendedor, no desempeño verificado. El banco opera cerca del límite inferior anunciado: una turbina detenida puede producir Q2=0 aunque siga circulando agua.

Consumo, potencia, peso, corriente de la fuente y dimensiones físicas finales están pendientes de medición. El [encapsulado](../diseno_3d/README.md) es conceptual; no se declara fabricado ni estanco.
