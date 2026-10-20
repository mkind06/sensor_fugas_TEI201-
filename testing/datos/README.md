# Datos de Testing

## Archivos de Datos

### `datos_sensores_testing.csv` (formato del prototipo)
El firmware imprime una línea cada 10 s por el Monitor Serie. Para generar el CSV, copiar el Monitor Serie (o usar un registrador serie) y convertir a columnas:

```csv
timestamp, q1_lmin, q2_lmin, dif_pct, tot1, tot2, razon_t2_t1, led, evento
[hh:mm:ss], 1.48, 0.00, 100.0, 1276, 996, 0.781, ROJO, llave_abierta
```

Ejemplo de línea real del Monitor Serie:
```
Q1: 1.48 | Q2: 0.00 L/min | Dif: 100.0 % | Tot1: 1276 | Tot2: 996 | Razon T2/T1: 0.781
```

---

### Datos medidos en banco (Avance #2)

#### Ruido eléctrico
| Condición | Pulsos sin flujo |
|---|---|
| Bomba desenchufada | 0 |
| Bomba en el mismo PC (filtro 2 ms) | ~330 /s |
| Sin filtro, bomba en el mismo PC | ~1300 /s |
| Bomba con cargador propio + filtro 1 ms | 0 |

#### Calibración (llave cerrada, sin fuga)
| Variable | Rango medido |
|---|---|
| Q1 | 1,53 – 1,60 L/min |
| Q2 | 1,46 – 1,53 L/min |
| Razón de pulsos T2/T1 | 0,953 – 0,956 |
| K1 (fabricante) | 288 pulsos/L |
| K2 (calibrado) | 288 × 0,955 ≈ 275 pulsos/L |

#### Fuga simulada
| Llave | Q1 | Q2 | Dif | LED |
|---|---|---|---|---|
| Cerrada | 1,53–1,60 L/min | 1,46–1,53 L/min (antes de calibrar; tras calibrar K2 ambos marcan lo mismo) | — | Verde |
| Apertura gradual | — | — | 10–25 % | Amarillo |
| Abierta por completo | 1,48 L/min | 0 | 100 % | Rojo |

> Pendiente: registrar valores numéricos de varias aperturas intermedias y de una corrida continua ≥ 5 min.

---

### `datos_cuantitativos.xlsx` (testing con usuarios)
Pendiente. Hojas sugeridas: Datos de usuarios · Métricas de usabilidad · Métricas ODS (tiempo de detección, fuga mínima detectable) · Feedback cualitativo.

---

### `comparativa_versiones.xlsx`
| Métrica | v1 | v2 | v3 |
|---|---|---|---|
| Pulsos falsos sin flujo | ~1300 /s | 0 | — |
| Diferencia sin fuga | 0–4,5 % | Ambos sensores marcan lo mismo | — |
| Ventana de medición | 3 s | 10 s | — |

---

## Análisis Estadístico
Para la corrida continua y las pruebas con usuarios calcular media, mediana, desviación estándar, mínimo y máximo de Q1, Q2 y Dif.

---

## Visualización de Datos
- `grafico_q1_q2_tiempo.png` – Q1 y Q2 vs. tiempo al abrir la llave (pendiente)
- `grafico_dif_tiempo.png` – diferencia % con líneas en 10 % y 25 % (pendiente)
