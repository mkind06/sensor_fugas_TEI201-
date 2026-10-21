# Historial de Iteraciones - Avance 2

La evolución técnica siguiente corresponde al desarrollo del Alpha. No reconstruye ni modifica la entrega oficial de Avance 1 y no declara una versión final realizada.

| Etapa | Observación o problema | Cambio y aprendizaje |
|---|---|---|
| Prueba de LED | Retorno a 3V3 y rojo invertido | Conectar retorno a GND y corregir polaridad |
| Programas iniciales | setup/loop y constantes redefinidos | Una carpeta por programa completo |
| Un sensor | Logs de cero y diagnóstico digital | Separar fallo de señal de indicación LED |
| Dos sensores | Conteos espurios asociados a bomba y placa en PC | Fuente independiente para bomba y filtro por estabilidad |
| Hidráulica | Agua escapaba por unión de boquilla; turbinas detenidas | Sellar unión y comprobar paso por sensores |
| Ajuste inicial | Razón de pulsos aproximada 0,955, K1=288 | K2 histórico≈275; ajuste relativo inicial |
| Lecturas posteriores | Amarillo sin fuga intencional con K2=275 | Siete lecturas físicas y revisión por incrementos |
| Ajuste posterior | ΔTot1=384 y ΔTot2=305 | K2=288×305/384=228,75≈229 provisional |
| Alpha presentado | Equipo informó normalidad, advertencia y fuga | Resultado cualitativo; no se conservó CSV final |
| Encapsulado | Necesidad de separar agua y electrónica y permitir acceso | Concepto STEP/DXF con base, tapa, USB y pasos de cable |

La ventana evolucionó de 3 s en pruebas anteriores a 10 s nominales. El sondeo usa 200 µs y cinco lecturas consecutivas; estos tiempos de configuración no son mediciones de latencia. La explicación del ruido eléctrico es una hipótesis de diagnóstico respaldada por su asociación con la bomba; no hubo ensayo instrumental del mecanismo.

## Ajuste del enfoque del proyecto

El equipo orientó la aplicación a sistemas agrícolas y agronomía en el campo. Acotar el banco a una conducción de riego y un tramo conocido permite estudiar el balance con menos variables desconocidas que una red urbana completa. No se afirma que todos los sistemas de riego tengan la misma complejidad: antes de instalar deben identificarse consumos, derivaciones y condiciones hidráulicas. La relación principal es ODS 6/meta 6.4, con ODS 2/meta 2.4 como vínculo complementario. El código utilizado fue aportado por el equipo y coincide con la lógica archivada con K2=229.

## Estado de esta iteración

La [iteración 2](iteracion_2/README.md) documenta el Alpha actual. El [testeo](../testing/README.md) conserva los datos preajuste, el cálculo relativo y el reporte de demostración, sin porcentajes inventados de mejora. La [iteración 1](iteracion_1/README.md) conserva el documento anterior; sus afirmaciones deben leerse en su contexto histórico. La [iteración 3](iteracion_3/README.md) queda pendiente.

El feedback textual del profesor, la distribución de roles y las métricas de impacto no fueron aportados. Los pasos siguientes son guardar una corrida física continua de cinco minutos con la configuración final, calibrar mediante volumen conocido y verificar medidas de componentes antes de fabricar la caja.
