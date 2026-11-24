# Archivos Fusion 360

**Archivo:** [`caja_v3.f3d`](caja_v3.f3d): ensamble completo de la caja v3 con sus componentes internos.

| Componente en el navegador de Fusion | Qué representa |
|---|---|
| base, tapa | Caja de PETG 120 × 85 × 43 mm y tapa con labio |
| tornillos | 4 tornillos M3 × 10 que cierran la tapa |
| placa | Placa perforada 5 × 7 cm sobre 4 postes |
| cabezales, esp_pcb, esp_chip, usbc | ESP32-S3 Super Mini montada en cabezales hembra, con su conector USB-C frente a la ventana |
| resistencias, borneras | Divisores 10 kΩ / 20 kΩ, resistencias de los LED y conectores de los sensores |
| led1, led2, led3 | LED verde, amarillo y rojo en la tapa |
| prensaestopas, cables | 2 prensaestopas PG7 y los cables de los sensores |

## Cómo abrirlo

En Fusion 360: **Archivo → Abrir → Abrir desde mi equipo** y elegir `caja_v3.f3d`. Para ver el interior, ocultar la tapa con el ojo del navegador (componente `tapa`).

## Origen

Se generó importando en Fusion 360 [`../cad/caja_v3_ensamble_electronica.step`](../cad/caja_v3_ensamble_electronica.step) y exportándolo como `.f3d`. El modelo proviene de los scripts CadQuery en [`../cad/fuente/`](../cad/fuente), por lo que no trae historial paramétrico de Fusion; las medidas de origen están en `modelo_caja.py` y en los [planos](../planos/README.md). Las medidas de la ESP32, la placa y las borneras son referenciales.
