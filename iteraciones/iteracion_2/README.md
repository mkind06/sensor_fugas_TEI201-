# Iteración 2 - Primer prototipo físico Alpha

**Entrega:** Avance 2 · TEI201. **Fecha de evaluación consignada en la guía:** 19-10-2026. La demostración fue informada como realizada; no se asignan fechas no documentadas a cada ensayo.

## Objetivo y cambios

El Alpha compara dos puntos de caudal en un banco con agua real y deriva una indicación visible. Se corrigieron el montaje de LED, la organización de sketches y una unión hidráulica; se separó la alimentación de la bomba y se añadió filtrado por estabilidad. El ajuste relativo pasó por K2=275 y posteriormente por K2≈229, con K1=288. La comunicación disponible es USB serie, con visualización de caudales en computador; no se controla la bomba por software.

El concepto de caja propone base de 120×85×40 mm, tapa con placa de 3 mm y labio, acceso USB-C, dos PG7 y tres LED. Los archivos [STEP y DXF](../../diseno_3d/README.md) están disponibles. No se presenta como impresión terminada ni ensamble con toda la electrónica.

## Testeo

Se conservan [siete mediciones](../../testing/datos/lecturas_preajuste.csv) de la condición sin fuga intencional que el algoritmo clasificó amarillo antes del último ajuste. Sus incrementos sustentan K2=228,75. El equipo comunicó que la demo mostró normalidad, advertencia y fuga. El testeo sintético de normalidad comprueba únicamente las condiciones de la lógica; no reemplaza el registro físico final perdido.

## Logros y límites

Se integraron sensores, cálculo, LED y transmisión USB en un banco de demostración. El aporte al problema es advertir una posible pérdida entre dos puntos para facilitar inspección. No se cuantificaron ahorro, precisión absoluta, consumo, latencia ni usabilidad; no hay pruebas de usuarios o terreno aportadas.

El funcionamiento continuo mínimo de cinco minutos requerido por la guía queda sin registro verificable. El bajo caudal puede detener el sensor 2, por lo que Q2=0 no prueba que toda el agua se haya perdido. El detalle de decisiones está en el [historial](../README.md).

## Pendientes de evidencia y próximos pasos

- Incorporar fotos originales del montaje presentado y cotejar el archivo realmente cargado.
- Guardar CSV físico continuo de cinco minutos y ensayos de derivación cerrada, parcial y abierta.
- Calibrar con volumen conocido y medir respuesta en vez de inferirla del período de reporte.
- Verificar encaje con medidas reales y completar inventario/precios con comprobantes.
- Registrar feedback, integrantes con roles y meta ODS formal cuando se disponga de ellos.

Las mejoras futuras se enumeran como planificación; no se rellena la versión final del proyecto.
