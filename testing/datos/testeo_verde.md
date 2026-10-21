# Testeo de verde: metodología

Se creó una serie nueva para comprobar la lógica de normalidad. El CSV exacto de la sesión anterior mencionado en el traspaso no estaba disponible; esta serie se identifica como reconstrucción de escenarios y no como recuperación de aquel archivo ni registro del prototipo.

Generación en Python mediante random.Random(201): 30 filas con tiempos virtuales 10,20,…,300 s; Q1=round(uniform(1.29,1.40),2); primera diferencia −3,0 %, última 5,0 %, y diferencias intermedias round(uniform(−3,5),1). Para cada fila Q2=Q1×(1−Dif/100), exportado con seis decimales. La semilla no implica identidad con otro generador o secuencia anterior.

Las 30 filas llevan origen=DATOS_SINTETICOS, estado_esperado=NORMAL y led_esperado=VERDE. Se comprueba que Q1≥0,5 y Dif<10, además del rango −3 a 5 % y la fórmula de Q2. Las diferencias negativas quedan verdes según la lógica archivada; esto no valida su significado hidráulico.

Los 300 s son tiempo virtual. No existen pulsos acumulados, hora de captura física, ensayo de estabilidad ni precisión experimental asociados a esta serie. Las [mediciones reales](lecturas_preajuste.csv) permanecen separadas.
