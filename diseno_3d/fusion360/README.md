# Archivos Fusion 360

**Estado:** pendiente de subir `caja_v3.f3d` (lo exporta el equipo desde Fusion 360; no se puede generar fuera del programa).

## Cómo generarlo (≈ 5 minutos)

1. En Fusion 360: **Archivo → Abrir → Abrir desde mi equipo** y elegir [`../cad/caja_v3_ensamble_electronica.step`](../cad/caja_v3_ensamble_electronica.step).
2. Revisar que aparezcan base, tapa, placa, ESP32, LED, prensaestopas y tornillos como componentes.
3. Asignar material: base y tapa **PETG** (Modificar → Administrar materiales).
4. **Archivo → Exportar → Tipo: Archivos de archivado de Fusion 360 (.f3d)** y guardar como `caja_v3.f3d`.
5. Subirlo a esta carpeta (`diseno_3d/fusion360/`) desde GitHub: **Add file → Upload files**.

El modelo proviene de los scripts CadQuery en [`../cad/fuente/`](../cad/fuente), por lo que el `.f3d` importado no trae historial paramétrico de Fusion; las medidas de origen están en `modelo_caja.py` y en los [planos](../planos/README.md).
