# Código Fuente - Avance 2

## Archivos disponibles

| Archivo | Procedencia |
|---|---|
| [PruebaSensor.ino](PruebaSensor/PruebaSensor.ino) | Código compartido directamente por el usuario como el utilizado por el equipo; K1=288/K2=229. Coincide en lógica con la reconstrucción anterior; comentarios aclarados |
| [PruebaSensor_historico.ino.txt](historico/PruebaSensor_historico.ino.txt) | Copia íntegra del sketch del commit ed744f1, con K2=275; extensión .txt para evitar compilación conjunta |
| [Panel_USB_Real.html](web/Panel_USB_Real.html) | Nuevo panel de consulta reconstruido en esta revisión; no es recuperación del HTML original mencionado en el traspaso |

El usuario aportó el sketch utilizado por el equipo. Se verificó que sus constantes, funciones, condiciones y formato serie coinciden con la lógica ya archivada. El comentario de VENTANA_MS decía evaluar cada 3 s, aunque 10000 ms corresponden a 10 s: se corrigió solo el comentario. La identificación de uso procede del equipo; no de una extracción o lectura de la memoria del ESP32. El HTML y CSV sintético exactos de la sesión previa siguen sin estar disponibles, por lo que las reconstrucciones de esos dos recursos mantienen esa etiqueta.

## Monitor web utilizado por el equipo

La [fotografía del montaje final](../../hardware/fotos/README.md) muestra un monitor web con indicadores y gráfico junto al CAD. Es evidencia visual de la interfaz utilizada por el equipo; sus valores no se transcriben como una serie de mediciones por falta de legibilidad. El HTML original de ese monitor aún no fue aportado. Por eso el archivo Panel_USB_Real.html de este repositorio sigue identificado como reconstruido, con su propio alcance documentado en el [manual](../docs/README.md); no se afirma que reproduzca exactamente la interfaz de la fotografía.

## Estructura del sketch

`setup()` inicializa Serial, LED y entradas sin pull-up. `muestrear(i)` acepta un cambio tras cinco lecturas opuestas consecutivas y cuenta solo cambios a HIGH. `luces(v,a,r)` aplica las salidas. `loop()` intenta muestrear cada 200 µs; cada 10 s calcula caudales por incrementos de pulsos, decide el estado y transmite los valores.

```text
Q1: 1.35 | Q2: 1.18 L/min | Dif: 13.0 % | Tot1: 470 | Tot2: 411 | Razon T2/T1: 0.874
```

La razón puede ser `-` si Tot1=0. Esta línea es una lectura histórica preajuste, no un resultado posterior al ajuste K2=229. Los comandos n/a/f pertenecen a una prueba anterior y no forman parte del sketch actual.

Para cargar: abrir únicamente la carpeta `PruebaSensor`, seleccionar ESP32S3 Dev Module y USB CDC On Boot Enabled, comprobar el puerto y usar 115200 para consultar. No se ejecutó una compilación Arduino ni una prueba física en esta revisión.
