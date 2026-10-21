# Código Fuente - Avance 2

## Archivos disponibles

| Archivo | Procedencia |
|---|---|
| [PruebaSensor.ino](PruebaSensor/PruebaSensor.ino) | Reconstrucción documental desde el sketch del commit ed744f1 y el ajuste K2=229 del traspaso; conserva lógica de muestreo y decisión |
| [PruebaSensor_historico.ino.txt](historico/PruebaSensor_historico.ino.txt) | Copia íntegra del sketch del commit ed744f1, con K2=275; extensión .txt para evitar compilación conjunta |
| [Panel_USB_Real.html](web/Panel_USB_Real.html) | Nuevo panel de consulta reconstruido en esta revisión; no es recuperación del HTML original mencionado en el traspaso |

El paquete de la sesión previa, su HTML y su CSV sintético exacto no estaban presentes en los archivos locales encontrados. Los originales no se declaran recuperados. El firmware exacto cargado en la demostración sigue pendiente de cotejo; no cargar automáticamente esta reconstrucción sobre una placa funcional.

## Estructura del sketch

`setup()` inicializa Serial, LED y entradas sin pull-up. `muestrear(i)` acepta un cambio tras cinco lecturas opuestas consecutivas y cuenta solo cambios a HIGH. `luces(v,a,r)` aplica las salidas. `loop()` intenta muestrear cada 200 µs; cada 10 s calcula caudales por incrementos de pulsos, decide el estado y transmite los valores.

```text
Q1: 1.35 | Q2: 1.18 L/min | Dif: 13.0 % | Tot1: 470 | Tot2: 411 | Razon T2/T1: 0.874
```

La razón puede ser `-` si Tot1=0. Esta línea es una lectura histórica preajuste, no un resultado de la reconstrucción con K2=229. Los comandos n/a/f pertenecen a una prueba anterior y no forman parte del sketch actual.

Para cargar: abrir únicamente la carpeta `PruebaSensor`, seleccionar ESP32S3 Dev Module y USB CDC On Boot Enabled, comprobar el puerto y usar 115200 para consultar. No se ejecutó una compilación Arduino ni una prueba física en esta revisión.
