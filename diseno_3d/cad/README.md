# CAD conceptual: procedencia y revisión

Archivos copiados sin editar desde Descargas del usuario: STEP 393715 bytes y DXF 80255 bytes. El DXF disponible localmente se llama caja_planos.dxf; el traspaso lo mencionaba con sufijo _1 y el mismo tamaño. No se asume igualdad por tamaño: se registra la huella del archivo realmente recibido.

## SHA-256 de los archivos incorporados

- `caja_impresion_1.step`: `41e4ca94621f8dfe97b68f6377611a129c6ba2bd34c2a666ac074ab2be1b21a5`
- `caja_planos.dxf`: `ab68fc5f01b4664782b224abe6d93f00f3d9eedc5f0ab0a9407113d3ad0dc727`

## Revisión anterior comunicada en el traspaso

El traspaso informa dos sólidos STEP válidos con envolventes de 120×85×40 y 120×85×5 mm; DXF AC1024, unidades mm, auditoría sin errores, 11 LWPOLYLINE, 25 CIRCLE, 27 LINE, 20 DIMENSION y 15 TEXT. Se atribuye esa revisión a la sesión anterior, no a una nueva ejecución de Open CASCADE en esta sesión.

En esta revisión se comprobó la copia byte a byte y se ejecutó ezdxf sobre el DXF local: AC1024, unidades 4 (mm), cero errores y cero correcciones; el conteo de entidades coincide con el informado arriba. No se volvió a ejecutar el lector geométrico de STEP. El STEP contiene piezas separadas para impresión, no un ensamble de electrónica. No se verificaron tolerancias, encaje con componentes físicos, resistencia, estanqueidad o impresión. La [justificación](../README.md) distingue dimensiones de diseño y referencias típicas.
