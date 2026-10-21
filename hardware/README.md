# Hardware - Avance 2

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
