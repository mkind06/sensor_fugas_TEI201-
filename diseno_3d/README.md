# Diseño 3D - Documentación

## ⚠️ REQUISITO CRÍTICO – estado
El modelo `ensamble_componentes.step` incluye la caja con los componentes internos:
- ✅ Encapsulado exterior (base + tapa)
- ✅ ESP32-S3 Super Mini (23 × 18 mm) sobre 4 postes
- ✅ Dos mini protoboards (47 × 35 mm c/u)
- ✅ LED en la tapa con portaLED
- ✅ Prensaestopas PG7 para los cables de los sensores
- ✅ Ventana USB-C
- ⚠️ Sensores FS400A y bomba: van **fuera** de la caja, sobre la línea de riego
- ⚠️ Cableado: routing aproximado por agregar si se exige
- ✅ Sistema de cierre: 4 tornillos M3 + burlete

---

## Carpetas / archivos
| Archivo | Contenido |
|---|---|
| `diseno_3d/fusion360/ensamble_componentes.step` | Modelo 3D con componentes (para mostrar) |
| `diseno_3d/fusion360/caja_base.step`, `caja_tapa.step` | Piezas separadas |
| `diseno_3d/fusion360/caja_impresion.3mf` / `.stl` | Archivos para imprimir |
| `diseno_3d/planos/caja_planos.dxf` | Planos acotados |
| `renders/` | Imágenes (ver `diseno_3d/renders/`) |

---

## Especificaciones
**Software:** AutoCAD (exportado a STEP, abrible en Fusion 360)
**Unidades:** milímetros
**Escala:** 1:1

**Dimensiones externas:** 120 × 85 × 43 mm
**Interior útil:** 115 × 80 × 37 mm
**Paredes:** 2,5 mm · **Tapa:** 3 mm
**Peso estimado:** pendiente
**Material:** PETG

### Justificación de dimensiones
La ESP32 (23 × 18 mm) y las dos protoboards (47 × 35 mm cada una) caben lado a lado en el fondo con margen para cables. La altura deja espacio para la protoboard (8,5 mm), las resistencias y los cables de los LED hacia la tapa.

### Justificación del material
PETG resiste mejor la humedad, la radiación UV y el calor que el PLA, y es fácil de imprimir: adecuado para uso en el campo.

---

## Consideraciones de Diseño

### Funcionales
- [x] Acceso a USB/alimentación: ventana USB-C de 12 × 7 mm, reprogramar sin abrir la caja.
- [x] Ventilación: no se requiere (bajo consumo, sin componentes de potencia; la bomba queda fuera).
- [x] Protección de componentes: prensaestopas sellan los cables; componentes elevados del fondo por si entra humedad.
- [x] Mantenimiento: tapa con 4 tornillos M3.
- [x] Condiciones ambientales: burlete de 2 mm en el labio; caja montada por encima de la línea de riego con **lazo de goteo** en los cables (bajan antes de subir al prensaestopas).
- [x] Visibilidad: 3 LED en la tapa (agujeros de 5 mm con portaLED), visibles desde lejos.

### Integración hardware-encapsulado
- ESP32 sobre 4 postes de 5 mm, alineada con la ventana USB.
- Protoboard blanca (divisores) cerca de los prensaestopas para acortar los cables de los sensores.

### Fabricación
- [x] Grosor de pared ≥ 2 mm (2,5 mm)
- [ ] Verificar tolerancias de ensamble (+0,2 mm) en postes y agujeros
- [ ] Verificar overhangs < 45° en la ventana USB y prensaestopas

---

## Configuración de Impresión 3D
**Impresora:** [completar]
**Material:** PETG
**Calidad de capa:** [completar]
**Relleno:** [completar]
**Soportes:** [completar]
**Temperatura nozzle:** [completar]
**Temperatura cama:** [completar]
**Velocidad:** [completar]

**Tiempo estimado de impresión:** [completar]
**Peso de material:** [completar]
