# Planos Técnicos - Caja v3

**Archivo:** [planos_caja_v3.pdf](planos_caja_v3.pdf) (3 hojas A3)

| Hoja | Contenido |
|---|---|
| 1 · Conjunto | Vista explosionada e isométrica de referencia, lista de piezas, dimensiones generales (120 × 85 × 43 mm) y cómo se desarma para reparar |
| 2 · Base | Planta, vistas laterales izquierda (ventana USB-C 12 × 7 a 20,5 mm) y derecha (2 × Ø12,5 para PG7), alzado frontal; cotas de torretas M3, postes de la placa y paredes de 2,5 mm. Escala 1:1 |
| 3 · Tapa | Planta con 4 pasantes Ø3,4 y 3 agujeros Ø5 para LED, sección A-A del labio (holgura 0,3 mm por lado) y detalle del agujero de LED. Escala 1:1 |

Unidades en mm, tolerancia general ±0,2 mm, material PETG, proyección ISO (primer diedro).

**Procedencia:** las cotas salen de los parámetros de [`modelo_caja.py`](../cad/fuente/modelo_caja.py), el mismo script que genera los STEP. El PDF se regenera con [`planos.py`](../cad/fuente/planos.py) (`python planos.py`, requiere matplotlib). Las medidas de la electrónica son referenciales; verificar el ajuste con una impresión de prueba antes de fabricar.
