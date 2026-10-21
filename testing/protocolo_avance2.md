# Protocolo de respaldo del Alpha - Avance 2

**Estado: propuesto, pendiente de ejecutar y registrar.** Se organiza para respaldar los requisitos de la guía, no para declarar nuevos resultados. No se requiere una campaña con usuarios para esta entrega.

## Preparación y registro

Conservar el archivo .ino usado, K1/K2, ventana, umbrales, versión del núcleo, fecha y operador. Revisar conexiones y retorno de agua; alimentar bomba y placa como se documenta en [hardware](../hardware/README.md). Elegir Monitor Serie o panel para ocupar el puerto, no ambos simultáneamente.

El registro puede usar las columnas del CSV exportado por el panel, añadiendo por separado una bitácora con apertura de la derivación, LED físico observado, interrupciones y cambios de montaje. No completar registros retrospectivos con valores calculados como si se hubieran medido.

## Operación continua requerida por la guía

1. Iniciar registro continuo y, si se dispone de él, video con banco e indicadores visibles. Esperar la primera línea y anotar el inicio efectivo del ensayo.
2. Mantener el sistema integrado operando al menos cinco minutos continuos. Conservar datos e interrupciones; la ausencia de una línea no se interpreta como caudal cero.
3. Registrar la respuesta ante derivación cerrada, parcial y abierta, relacionando caudales, diferencia y LED físico. No existe una apertura que garantice por sí sola cada color: depende del flujo y del ajuste.
4. Cerrar la derivación y comprobar el estado posterior. Si una condición detiene una turbina, anotarlo como limitación de interpretación.
5. Guardar CSV completo y bitácora con el origen real. A 10 s nominales habrá aproximadamente treinta reportes en cinco minutos; contar treinta filas por sí solo no prueba continuidad o duración efectiva.

## Criterios de revisión

| Qué revisar | Criterio |
|---|---|
| Integración | Sensores → cálculo → LED y transmisión USB observables durante el mismo ensayo |
| Clasificación | Con Q1≥0,5: Dif<10 verde; 10≤Dif<25 amarillo; Dif≥25 rojo. Por debajo de Q_MIN: LED apagados |
| Coherencia | Comparar LED físico con valores y tener en cuenta el redondeo del panel |
| Continuidad | Tiempos, desconexiones y reinicios registrados; cinco minutos sin interrupciones si se declara cumplido |
| Alcance | Q2=0 a bajo caudal no demuestra pérdida total; sin referencia volumétrica no se declara precisión absoluta |

Como mejora de medición, recoger un volumen conocido y repetir permite estimar K=Δpulsos/litros por sensor. Es una prueba adicional propuesta; no se presenta como realizada ni como requisito de ensayos con usuarios.
