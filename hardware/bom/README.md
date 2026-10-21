# Bill of Materials (BOM) - Avance 2

## Materiales confirmados

| Cantidad | Componente | Identificación y uso |
|---|---|---|
| 1 | ESP32-S3 Super Mini | Placa USB-C de procesamiento |
| 2 | FS400A G1 | Rosca nominal 1 pulgada; rojo 5 V, negro GND, amarillo señal |
| 1 | Mini bomba sumergible blanca | Modelo no legible; 3–6 V informado, uso con USB 5 V |
| 2 | Mini protoboards | Negra para LED y blanca para sensores; 17 filas |
| 3 | LED | Uno verde, uno amarillo y uno rojo |
| 3 | Resistencias 330 Ω | Limitación de corriente de LED |
| 2 | Resistencias 10 kΩ | Rama superior de divisores |
| 2 | Resistencias 20 kΩ | Rama inferior de divisores |
| 2 usados | WAGO 221-412 | Un empalme por conductor de bomba; paquete adquirido de 6 |
| Longitud pendiente | Cable SPT 2 × 20 AWG | Rollo adquirido de 10 m; uso real sin medir |
| Por contar | Jumpers | Conexión de placa y protoboards |
| 1 | Cable USB-C de datos | Placa a computador |
| 1 | Fuente USB 5 V independiente | Bomba; modelo y corriente nominal por registrar |
| Inventario pendiente | Depósito, mangueras, T, llave, adaptadores y sellos | Circuito hidráulico; medidas definitivas por registrar |

Fabricantes, proveedores, SKU no identificados, precios unitarios y comprobantes quedan pendientes. No hay respaldo para calcular el costo total real; el presupuesto orientativo de la propuesta inicial no representa gasto realizado.

## Elementos propuestos para el encapsulado

PETG, dos prensaestopas PG7, tres alojamientos de LED, cuatro tornillos M3×10 y burlete de 2 mm forman parte del concepto. No se contabilizan como comprados, impresos o montados. La batería y módulo 18650 son antecedentes de pruebas, no componentes de alimentación del Alpha funcional.

## Referencia de los sensores

La ficha comercial compartida anuncia 5–18 V DC, 10 mA a 5 V, salida TTL 0–Vcc, 1–60 L/min, 5–80 °C, precisión ±5 %, presión máxima 1,2 MPa y dimensiones 42 × 42 × 73 mm. No se dispone de ficha de fabricante identificada ni de ensayos que confirmen esos límites. La ficha contiene 280 pulsos/L y también f=4,8×Q, equivalente a 288 pulsos/L; se tomó este último como referencia inicial, pendiente de calibración absoluta.
