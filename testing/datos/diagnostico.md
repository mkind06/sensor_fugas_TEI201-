# Testeo: registros históricos de diagnóstico

Transcripción del traspaso aportado. Las horas no se convierten en fechas ni se unen como un ensayo continuo.

### A. Logs iniciales de un sensor

Se recibieron estas líneas; la presencia o ausencia de agua no queda identificada para todo ese bloque:

```text
23:40:51.396 -> Pulsos del intervalo: 0 | Total: 0
23:40:52.404 -> Pulsos del intervalo: 0 | Total: 0
23:40:53.382 -> Pulsos del intervalo: 0 | Total: 0
23:40:54.376 -> Pulsos del intervalo: 0 | Total: 0
23:40:55.385 -> Pulsos del intervalo: 0 | Total: 0
```

Posteriormente el usuario indicó que no había agua y que el LED rojo estaba encendido; aparecieron:

```text
00:43:53.665 -> Pulsos del intervalo: 0 | Total: 0
00:43:54.656 -> Pulsos del intervalo: 0 | Total: 0
```

No presentar estos ceros como exactitud de medición: fueron parte del diagnóstico de cableado/LED.

### B. Dos sensores, bomba encendida, lecturas en cero

```text
12:35:11.236 -> Q1: 0.00 | Q2: 0.00 L/min | Dif: 0.0 % | Tot1: 0 | Tot2: 0 | Razon T2/T1: -
12:35:21.269 -> Q1: 0.00 | Q2: 0.00 L/min | Dif: 0.0 % | Tot1: 0 | Tot2: 0 | Razon T2/T1: -
12:35:31.251 -> Q1: 0.00 | Q2: 0.00 L/min | Dif: 0.0 % | Tot1: 0 | Tot2: 0 | Razon T2/T1: -
12:35:41.255 -> Q1: 0.00 | Q2: 0.00 L/min | Dif: 0.0 % | Tot1: 0 | Tot2: 0 | Razon T2/T1: -
```

El usuario señaló que la bomba estaba encendida y salía agua. Es evidencia de la fase con falta de detección, no prueba exitosa de ausencia de fuga. Las horas provienen de mensajes; no se añaden fechas a cada línea ni se asegura un único ensayo continuo entre bloques.

### C. Mediciones resumidas en el traspaso anterior

- `digitalRead` con agua: ambos sensores alternaban 0 y 1 según diagnóstico reportado.
- Ventana de 3 s y K2=288, llave cerrada: Q1 aproximadamente 1,53–1,60 L/min, Q2 aproximadamente 1,46–1,53 L/min; razón T2/T1 de 0,953–0,956.
- Se calculó entonces K2 ≈ 288 × 0,955 ≈ 275.
- Con derivación abierta: Q1 aproximadamente 1,48, Q2=0 y Dif=100 %. El sensor 2 dejó de girar al bajar el flujo.
- El equipo informó que los tres LED cambiaban al abrir la llave.

Son resúmenes aportados por el equipo; no crear filas crudas ficticias a partir de esos rangos.
