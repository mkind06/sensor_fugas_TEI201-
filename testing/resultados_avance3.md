# Resultados de pruebas - Avance 3

Pruebas realizadas por el equipo los días 22 y 23 de noviembre de 2026 durante el soldado de la placa perforada y la integración del firmware final. Los valores provienen de los registros del Monitor Serie y de lo observado en el banco; no se agregan cifras que no se hayan medido.

## Resumen

| ID | Prueba | Resultado | Observaciones |
|---|---|---|---|
| P1 | Salidas LED | ✅ Los tres LED encienden en secuencia | El amarillo falló al principio (ver falla F1) |
| P2 | Lectura de cada sensor | ⚠️ Sensor 2 OK, sensor 1 falla | Ambos sensores contaron al soplarlos después de corregir F4. El sensor 2 sigue funcionando (confirmado el 23-11); el sensor 1 dejó de contar (falla F3) |
| P3 | Firmware y publicación | ✅ | Compiló y cargó; una lectura JSON por segundo (`seq` 7 → 16 en 9 s), `SIN_FLUJO` sin agua |
| P4 | Ruido de la bomba | ✅ con fuente separada | Con alimentación compartida la ESP32 se reinició (`rst:0x7 (TG0WDT_SYS_RST)`). Con la bomba en su propia fuente no hubo reinicios (falla F2) |
| P5 | Caudal con bomba | ⚠️ Parcial | Con agua circulando, el sensor 1 sumó de 1.788 a 1.972 pulsos en 11 s (≈ 16,7 pulsos/s → **≈ 3,5 L/min** con K1 = 288; en segundos individuales 9–20 pulsos/s, 1,9–4,2 L/min). En esa misma prueba el sensor 2 se quedó en 29 pulsos; luego volvió a contar al revisar sus conexiones, por lo que no se obtuvo una medición simultánea de ambos |
| P6 | Fuga controlada | Pendiente | Requiere ambos sensores operativos |
| P7 | Dashboard en otro dispositivo | Se muestra en vivo en la presentación | Dashboard probado contra una ESP32 simulada: estados y botones de demo responden |
| P8 | Estabilidad 5 min | No ejecutada | Se hará con ambos sensores operativos, después de reparar F3 |
| P9 | Modo demo | ✅ | Los tres estados se muestran con datos marcados como simulados en pantalla y en el CSV |

## Fallas encontradas y cómo se resolvieron

**F1 · LED amarillo no encendía.** El verde funcionaba con el mismo código, así que la ESP32, el código y la tierra común estaban bien. Al unir con un jumper las soldaduras J12 y J15 el amarillo encendía de forma intermitente: el puente de tierra (una patita de resistencia) estaba apoyado sobre las soldaduras sin fundirse con ellas. *Solución:* cable aislado J12 → J15 soldado en ambos extremos. Resultado: los tres LED encienden. *Aprendizaje:* los puentes de tierra se hacen con cable aislado y se comprueban tirando suavemente.

**F2 · Reinicios al encender la bomba.** El Monitor Serie mostró `rst:0x7 (TG0WDT_SYS_RST)` justo al conectar la bomba. *Causa probable:* caída de tensión y ruido del motor al compartir la fuente. *Solución:* bomba con fuente independiente y cables alejados de la placa; además el firmware filtra pulsos separados por menos de 2 ms. Resultado: sin reinicios.

**F3 · Sensor 1 sin lectura (abierta).** El sensor 1 dejó de contar con aire y con agua, aunque su turbina gira. Pruebas: (1) cable de señal nuevo desde el divisor a la ESP32: sin cambio; (2) señal llevada a otro pin (GPIO 8, X10) con el firmware ajustado: sin cambio; (3) **el sensor 2, que funciona, conectado en el conector del sensor 1 tampoco cuenta**. Conclusión: la falla está en la placa, entre el conector B9 y el nodo del divisor (resistencia de 10 kΩ, puente F9–F7 o el pin del conector), no en el sensor ni en la ESP32. *Siguiente paso:* medir continuidad B9–C9, F9–F7 y F7–X10 con tester; si no se encuentra, rehacer el divisor en filas libres como el del sensor 2, que funciona.

**F4 · Pulsos del sensor 2 sin agua.** Aparecieron 1.433 pulsos al manipular la bomba y ninguno con agua circulando. El cable de señal del sensor 2 estaba soldado en la columna X (GPIO 12) y no en R15 (GPIO 2), por lo que el GPIO leído quedaba sin conexión y captaba ruido. *Solución:* cable movido a R15. Resultado: después del cambio ambos sensores contaron al soplarlos; el sensor 2 se mantiene operativo.

## Validación contra el problema

El problema planteado es detectar pérdidas de agua en un tramo de riego comparando el caudal al entrar y al salir. Con la configuración actual se verificó la cadena completa en cada etapa por separado: medición de caudal real con el FS400A (≈ 3,5 L/min con la bomba del banco), clasificación y señalización con los LED, y publicación de las lecturas a otro dispositivo por WiFi. Falta la prueba P6 con ambos sensores simultáneos, que es la que mide la diferencia entrada-salida con una fuga real; queda bloqueada por la falla F3. Hasta repararla, los tres estados se muestran con el modo demo, identificado como simulado en pantalla y en el CSV.

## Mejoras propuestas

1. Reparar el divisor del sensor 1 y ejecutar P5, P6 y P8 con registro CSV.
2. Calibrar cada sensor contra un volumen conocido (recipiente graduado y cronómetro) en vez del ajuste relativo K2/K1.
3. Agregar detección de falla de sensor: si un sensor marca 0 mientras el otro mide flujo durante varios segundos, mostrar "revisar sensor" en vez de "fuga".
4. Enviar las lecturas a una base de datos en la nube (por ejemplo Aiven PostgreSQL vía un servidor en Railway) para tener histórico entre sesiones y acceso remoto.
