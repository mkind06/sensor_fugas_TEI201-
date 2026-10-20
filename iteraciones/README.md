# Historial de Iteraciones

## Propósito
Documenta la evolución del detector de fugas a lo largo del curso.

---

## Estructura de Carpetas
```
iteraciones/
├── iteracion_1/    # Primer montaje en protoboard
├── iteracion_2/    # Prototipo Alpha IoT – Avance #2 (actual)
└── iteracion_3/    # Versión final – Avance #3 (pendiente)
```

---

## Tabla Comparativa de Iteraciones

| Aspecto | v1 | v2 (actual) | v3 |
|---|---|---|---|
| **Fecha** | [fecha] | [fecha Avance #2] | Pendiente |
| **Sensores** | 2 × FS400A | 2 × FS400A calibrados entre sí (K1 = 288, K2 = 275) | Sensores ajustados al caudal real de la línea |
| **Actuadores** | 3 LED (con fallas de conexión) | 3 LED respondiendo según umbrales | 3 LED + alerta remota |
| **Conectividad** | USB / Monitor Serie | USB / Monitor Serie | WiFi (pendiente) |
| **Filtro de ruido** | No | Filtro de estabilidad 1 ms + bomba con cargador propio | — |
| **Ventana de medición** | 3 s | 10 s | — |
| **Encapsulado** | ❌ | Modelo 3D (PETG, 120 × 85 × 43 mm) | Impreso e instalado |
| **Testing** | Solo equipo | Pruebas de banco con llave de fuga | Pendiente |

---

## Evolución del Diseño

### Versión 1 – Primer montaje
**Estado:** prueba de concepto en protoboard.

**Características:**
- Dos FS400A en serie con la llave de paso entre ellos; LED como indicador.
- Problemas: LED mal conectados, error de compilación por dos programas en el mismo proyecto, pulsos falsos (~1300/s sin agua) y caudales irreales (hasta 49 L/min), turbinas detenidas por fuga en la boquilla de la bomba.
- Aprendizaje clave: las lecturas había que contrastarlas con lo físicamente posible antes de confiar en ellas.

### Versión 2 – Prototipo Alpha IoT (Avance #2)
**Estado:** prototipo funcional en banco.

**Mejoras implementadas:**
- Bomba con cargador propio + filtro por software → 0 pulsos sin flujo.
- Calibración relativa de sensores (K2 = 275).
- Ventana de 10 s → diferencia estable.
- Modelo 3D del encapsulado con componentes.

**Problemas pendientes:**
- Conectividad WiFi.
- Prueba de estabilidad de 5 minutos.
- Caudal de la bomba (~1,5 L/min) cerca del mínimo del sensor (1 L/min).
- K1 sin calibrar con volumen real.
- Diagrama de circuito en imagen.

### Versión 3 – Versión Final
Pendiente (ver `iteraciones/iteracion_3/`).

---

## Justificación de Cambios

### Hardware
**De v1 a v2:**
- Cambio: bomba alimentada con cargador propio, separada del PC.
- Razón: el motor inyectaba ruido por la tierra USB compartida.
- Impacto: de ~1300 pulsos/s falsos a 0 pulsos sin flujo.

- Cambio: corrección del cableado de LED (GND real y LED orientado).
- Impacto: los 3 LED responden correctamente.

- Cambio: boquilla de la bomba sellada dentro de la manguera.
- Impacto: flujo continuo; las turbinas dejaron de detenerse.

### Software
**De v1 a v2:**
- Filtro de estabilidad: muestreo cada 0,2 ms, cambio aceptado si dura ≥ 1 ms.
- Calibración K2 = 288 × 0,955 ≈ 275: ambos sensores pasan a marcar lo mismo sin fuga (antes ~4,5 % de diferencia).
- Ventana de 3 s → 10 s: la diferencia ya no salta entre 0 y 4,5 %.
- Proyecto con una sola pestaña: compila sin errores.

### Diseño 3D
**De v1 a v2:**
- Primer encapsulado: caja PETG con LED en la tapa, ventana USB-C, prensaestopas PG7, burlete y tornillos M3.

---

## Incorporación de Feedback

### Feedback del Avance #1 → Cambios en v2
1. [Completar con comentarios del profesor/ayudante]
   - Acción tomada: [completar]

### Feedback del Avance #2 → Cambios en v3
1. [Completar tras la presentación]

---

## Métricas de Mejora (medidas)

| Métrica | v1 | v2 | Mejora |
|---|---|---|---|
| Pulsos falsos sin flujo | ~1300 /s | 0 /s | ↓ 100 % |
| Caudal máx. leído con bomba de ~1,5 L/min | hasta 49 L/min | ~1,5 L/min | Lecturas coherentes |
| Diferencia sin fuga | ~4,5 % (saltaba entre 0 y 4,5 %) | Ambos sensores marcan lo mismo | ✅ |
| Tiempo de respuesta | 3 s (inestable) | 10–20 s (estable) | Más lento, pero confiable |

---

## Lecciones Aprendidas

### Técnicas
- Separar la alimentación de cargas inductivas (motores) del microcontrolador.
- Filtrar por software la señal de sensores de pulsos.
- Contrastar cada lectura con lo físicamente posible antes de confiar en ella.
- Calibrar los sensores entre sí antes de compararlos.

### De Proceso
- Aislar las causas cambiando una variable a la vez (bomba desenchufada / en el PC / con cargador propio).
- Registrar cada problema con causa, solución y resultado.

### De Trabajo en Equipo
- [Completar]
