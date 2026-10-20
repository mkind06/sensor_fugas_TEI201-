# Código Fuente

## Archivos Principales

### `software/src/PruebaSensor/PruebaSensor.ino`
Archivo único del proyecto (equivale al `main.ino` de la plantilla). Está escrito para el núcleo Arduino-ESP32 y **no usa librerías externas**.

**Estructura:**
- **Encabezado:** descripción del sistema, placa, sensores, lógica y conexiones.
- **Constantes de configuración:** pines, calibración (`K[]`), filtro anti-ruido, ventana de medición y umbrales.
- **`setup()`:** inicia el Monitor Serie (115200), configura los LED como salida, los pines de sensores como entrada y lee el nivel inicial de cada sensor.
- **`loop()`:**
  1. Muestrea ambos sensores cada 0,2 ms (sin `delay()`).
  2. Cada 10 s calcula Q1, Q2 y la diferencia porcentual.
  3. Enciende el LED que corresponde al estado.
  4. Imprime una línea de reporte en el Monitor Serie.

### Funciones auxiliares
| Función | Descripción |
|---|---|
| `muestrear(int i)` | Lee el sensor *i* y cuenta un pulso por cada flanco de subida que se mantiene estable ≥ 1 ms (filtro anti-ruido). |
| `luces(bool v, bool a, bool r)` | Enciende solo los LED indicados (verde, amarillo, rojo). |

### Archivos previstos (Avance #3)
- `comunicacion.h / .cpp` – WiFi (página web local o envío a la nube). **Pendiente.**
- `config.h` – separar constantes de configuración si el código crece.

---

## Estándares de Código

### Comentarios
- Comentarios en español.
- Cada bloque de constantes explica **por qué** tiene ese valor (p. ej., por qué la ventana es de 10 s o por qué el filtro exige 1 ms estable).

```cpp
// Lee el sensor i y cuenta un pulso por cada flanco de subida estable.
void muestrear(int i) {
  int lectura = digitalRead(PIN_S[i]);
  if (lectura != nivel[i]) {
    cuenta[i]++;
    if (cuenta[i] >= ESTABLE) {     // el cambio duró al menos 1 ms: es real
      ...
```

### Nombres
- Variables: `camelCase` (`ultimaMuestra`, `ultimoReporte`)
- Constantes: `UPPER_SNAKE_CASE` (`VENTANA_MS`, `UMBRAL_ROJO`, `LED_VERDE`)
- Funciones: `camelCase()` (`muestrear()`, `luces()`)

---

## Testing y Debugging

### Monitor Serie
- Baudrate: **115200**
- Una línea cada 10 s con caudales, diferencia, totales acumulados y razón de pulsos:

```
Q1: 1.48 | Q2: 0.00 L/min | Dif: 100.0 % | Tot1: 1276 | Tot2: 996 | Razon T2/T1: 0.781
```

| Campo | Uso en depuración |
|---|---|
| `Q1`, `Q2` | Caudal de entrada y salida en la última ventana |
| `Dif` | % de agua que no llega al sensor 2 |
| `Tot1`, `Tot2` | Pulsos acumulados desde el arranque (detectar ruido: deben quedarse fijos sin flujo) |
| `Razon T2/T1` | Calibración relativa: con la llave cerrada debe ser ≈ 0,955 |

### Prueba de ruido
Con la bomba apagada, `Tot1` y `Tot2` no deben aumentar. Si aumentan, la bomba está compartiendo tierra con el PC (ver `hardware/`).
