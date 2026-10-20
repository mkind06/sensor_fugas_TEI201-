# Documentación de Software

## Contenido

### Diagramas de Flujo
El diagrama de flujo del programa está en `software/` (sección *Arquitectura del Software*). Pendiente: exportarlo como imagen (draw.io → PNG).

### Documentación de Funciones

#### `muestrear(int i)`
- **Propósito:** contar los pulsos del sensor *i* descartando el ruido eléctrico del motor de la bomba.
- **Parámetros:** `i` (`int`) – índice del sensor: 0 = entrada, 1 = salida.
- **Retorna:** nada. Actualiza `nivel[i]`, `cuenta[i]` y `pulsos[i]`.
- **Funcionamiento:** si la lectura difiere del último nivel estable, incrementa un contador; solo acepta el cambio si se repite `ESTABLE` = 5 veces seguidas (1 ms a 0,2 ms por muestra). Cuenta un pulso en cada flanco de subida aceptado. Los picos de ruido duran microsegundos y se descartan; los pulsos reales duran decenas de ms.
- **Ejemplo de uso:**
```cpp
if (ahora - ultimaMuestra >= MUESTRA_US) {
  ultimaMuestra = ahora;
  muestrear(0);   // sensor de entrada
  muestrear(1);   // sensor de salida
}
```

#### `luces(bool v, bool a, bool r)`
- **Propósito:** mostrar el estado del tramo con los LED.
- **Parámetros:** `v`, `a`, `r` (`bool`) – encender verde, amarillo, rojo.
- **Retorna:** nada.
- **Ejemplo de uso:**
```cpp
luces(false, true, false);   // posible fuga: solo amarillo
```

#### `setup()`
- **Propósito:** inicializar Monitor Serie, pines de LED (apagados) y de sensores (entrada sin pull-up; el divisor externo fija el nivel).

#### `loop()`
- **Propósito:** muestrear ambos sensores sin bloquear y, cada `VENTANA_MS` (10 s), calcular:
  - `Q = pulsos / segundos × 60 / K` [L/min]
  - `Dif = (Q1 − Q2) / Q1 × 100` [%] (solo si Q1 ≥ 0,5 L/min)
  - Estado del LED y línea de reporte serie.

---

## Manual de Instalación
1. Instalar Arduino IDE y el soporte para ESP32 (ver `software/`).
2. Placa **ESP32S3 Dev Module**, **USB CDC On Boot: Enabled**.
3. Abrir `software/src/PruebaSensor/PruebaSensor.ino`, compilar y subir.
4. Abrir Monitor Serie a 115200.

---

## Manual de Operación

### Encendido del Sistema
1. Verificar el circuito hidráulico: **bomba → sensor 1 → llave de fuga → sensor 2 → recipiente**, con las uniones selladas con cinta.
2. Conectar la ESP32 por USB (PC o cargador).
3. Conectar la bomba a **su propio cargador**, nunca al mismo PC que la ESP32.
4. Esperar la primera lectura (10 s). Con flujo y llave cerrada debe encenderse el LED verde.

### Operación Normal
1. Observar el LED: verde = normal, amarillo = posible fuga, rojo = fuga, apagados = sin flujo.
2. Para simular una fuga, abrir gradualmente la llave de paso: los LED pasan de verde a amarillo y a rojo.
3. Revisar en el Monitor Serie los valores de Q1, Q2 y diferencia.
4. Considerar que el sistema responde en 10–20 s (una o dos ventanas de medición).

### Apagado del Sistema
1. Desconectar la bomba.
2. Esperar una ventana: los LED se apagan (sin flujo).
3. Desconectar la ESP32.
4. Vaciar mangueras y secar los sensores si se van a guardar.

---

## Troubleshooting

**Problema 1: No conecta a WiFi**
- Estado: la conectividad aún no está implementada.

**Problema 2: Sensor marca pulsos sin agua circulando**
- Causa probable: ruido del motor de la bomba entrando por la tierra USB compartida con el PC.
- Solución: alimentar la bomba con su propio cargador. El filtro por software (1 ms) ya descarta los picos restantes.

**Problema 3: Caudales irreales (decenas de L/min)**
- Causa probable: ruido sumado a flujo irregular.
- Solución: misma que el problema 2; verificar que la bomba esté sumergida y la boquilla sellada.

**Problema 4: Las turbinas no giran / Q = 0 con la bomba encendida**
- Causa probable: el agua se escapa en la unión bomba–manguera, o el caudal está bajo el mínimo del FS400A (1 L/min).
- Solución: sellar la boquilla dentro de la manguera con cinta.

**Problema 5: El Monitor Serie no muestra nada**
- Causa probable: *USB CDC On Boot* desactivado o baudrate distinto.
- Solución: activar *USB CDC On Boot: Enabled*, volver a subir y usar 115200.

**Problema 6: Error `redefinition of 'void setup()'` al compilar**
- Causa probable: dos programas en pestañas del mismo proyecto.
- Solución: dejar una sola pestaña por proyecto.

**Problema 7: LED amarillo sin fuga**
- Causa probable: sensores descalibrados entre sí.
- Solución: con la llave cerrada, leer `Razon T2/T1` y ajustar `K[1] = K[0] × razón`.
