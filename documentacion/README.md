# Estado de la entrega - Avance 3

Revisión frente al checklist de la guía del Avance 3 (23-11-2026).

| Checklist de la guía | Estado | Dónde |
|---|---|---|
| Captura continua de datos | ✅ Sensor 2 y firmware publicando cada 1 s · ⚠️ sensor 1 en reparación | [testing](../testing/resultados_avance3.md) |
| Repositorio persistente | ✅ CSV estructurado exportado desde el dashboard · nube como siguiente paso | [software](../software/README.md#persistencia-de-los-datos) |
| Dashboard funcional | ✅ Por WiFi desde la ESP32 y por USB; publicado en [GitHub Pages](https://mkind06.github.io/sensor_fugas_TEI201-/) | [software](../software/README.md) |
| Información útil (alertas, indicadores) | ✅ Semáforo, % de diferencia, agua perdida, eventos, tiempo por estado | [software](../software/README.md#información-que-genera-el-dashboard) |
| Código comentado en GitHub | ✅ | [software/src](../software/src/README.md) |
| Justificación de componentes | ✅ | [hardware](../hardware/README.md#justificación-de-componentes) |
| Esquemático actualizado | ✅ [Esquemático en PDF](../hardware/esquemas/esquematico_v3.pdf) y coordenadas de la placa soldada | [esquemas](../hardware/esquemas/README.md) |
| BOM con costos | ✅ | [bom](../hardware/bom/README.md) |
| Fotos del prototipo (3 ángulos) | ✅ Banco, sistema integrado y placa soldada (ambas caras) | [fotos](../hardware/fotos/README.md) |
| Encapsulado reparable | ✅ Tapa con 4 tornillos, ESP32 en cabezales, conectores | [diseño 3D](../diseno_3d/README.md) |
| Archivo Fusion 360 (.f3d) | ✅ `caja_v3.f3d` con caja, placa, ESP32, LED, prensaestopas y tornillos | [fusion360](../diseno_3d/fusion360/README.md) |
| Renders | ✅ 4 renders | [renders](../diseno_3d/renders/README.md) |
| Planos en PDF | ✅ 3 hojas A3: conjunto, base y tapa con cotas | [planos](../diseno_3d/planos/README.md) |
| Protocolo y resultados de pruebas | ✅ | [testing](../testing/README.md) |
| Falla analizada y resuelta | ✅ Cuatro fallas | [resultados](../testing/resultados_avance3.md#fallas-encontradas-y-cómo-se-resolvieron) |
| Conexión con el problema | ✅ | [resultados](../testing/resultados_avance3.md#validación-contra-el-problema) |
| FUENTES.md | ✅ | [FUENTES.md](../FUENTES.md) |
| README completo | ✅ | [README](../README.md) |
| Slides de la presentación | ✅ 14 diapositivas | [presentacion_avance3.pptx](presentacion/presentacion_avance3.pptx) |
| Guion de la demo | ✅ | [guion](presentacion/guion_demo.md) |
| Estructura de carpetas (firmware, hardware, 3D, testing, docs) | ✅ `firmware/` enlaza al código en `software/src/` | [README](../README.md#estructura-del-repositorio) |
| URL del repositorio en los slides | ✅ Slide final | — |

---

# Estado documental - Avance 2 (antecedente)

## Revisión frente a la guía

El resultado de la revisión individual de los 27 documentos y de sus archivos de respaldo está en la [matriz de revisión](revision_avance2.md). Los estados describen documentación y evidencia disponible; no constituyen una nota ni certifican pruebas físicas.

Se revisó la guía completa de nueve páginas, fechada 19-10-2026. La entrega es una demostración presencial de Alpha de 5–7 minutos más 2 de feedback, con participación de todos. Las recomendaciones de ensayo no se registran como actividades realizadas sin evidencia.

| Requisito de Avance 2 | Evidencia disponible y límite |
|---|---|
| Sensores en tiempo real | Dos FS400A, lecturas y diagnóstico en [Testeo](../testing/README.md); precisión absoluta pendiente |
| Actuación visible | LED verde/amarillo/rojo según lógica; resultado cualitativo comunicado por equipo |
| Conectividad verificable | USB serie a computador; WiFi/Bluetooth no implementados y sin feedback docente que confirme aceptación específica del criterio |
| Integración y estabilidad ≥5 min | Demostración informada como exitosa; falta registro continuo final de cinco minutos |
| Encapsulado conceptual | [STEP, DXF y justificación](../diseno_3d/README.md); modelo conceptual disponible; distribución interna visual y dimensiones reales por contrastar. La impresión no es obligatoria |
| Iteración y resolución parcial | [Cambios y aprendizajes](../iteraciones/README.md); alerta local de posible pérdida, sin ahorro medido |
| Código y dependencias | [Fuentes y procedencia](../software/src/README.md); código aportado por el equipo como el utilizado; versión exacta del núcleo pendiente |
| Circuito completo | [Diagrama y coordenadas](../hardware/esquemas/README.md) |

## Fuentes y trazabilidad

La revisión usa la guía aportada, TRASPASO_CODEX.md, el repositorio actual (base 181590e), el sketch histórico del commit ed744f1 y los CAD locales. Las instrucciones y ejemplos de documentos se evaluaron como contexto; las exigencias de etapas posteriores no se incorporaron como tareas de esta entrega.

El enfoque actual, confirmado por el equipo, es la detección de pérdidas en conducciones de riego agrícola, con aplicación prevista para agricultores y profesionales de agronomía. Se acota a un tramo con recorrido conocido para reducir variables y facilitar el ensayo. La propuesta urbana anterior es un antecedente histórico, no el contexto actual. La selección de ODS es 6/meta 6.4 como vínculo principal y 2/meta 2.4 como complemento; su justificación y fuentes están en el [resumen del proyecto](../README.md). El montaje utiliza ESP32-S3, FS400A y bomba USB. Los integrantes identificados en antecedentes son Andrés García, Pablo Miranda, Macarena Kuperman y Mathias Kind; falta confirmar roles actuales y profesor.

El código fuente utilizado por el equipo fue compartido directamente por el usuario después de la primera revisión. Sus instrucciones ejecutables coinciden con la reconstrucción anterior: K1=288, K2=229 y ventana de 10000 ms. Se actualizó su procedencia y se corrigió el comentario que decía 3 s a 10 s, sin modificar la lógica. El archivo no se extrajo de la placa y no se ejecutó una prueba física durante esta revisión. El CSV sintético y HTML reconstruidos mantienen su procedencia anterior; no se presentan como originales de la demo.

## Pendientes de esta evidencia

Registro continuo de cinco minutos, feedback, versión Arduino-ESP32, medidas reales, inventario hidráulico y precios comprobados. Ya se incorporaron dos [fotografías del montaje final](../hardware/fotos/README.md) aportadas por el equipo: una muestra el monitor web junto al CAD. El código utilizado y el enfoque agrícola también fueron aportados. Aún faltan capturas legibles de los tres estados y el HTML original del monitor utilizado. La contribución a eficiencia hídrica todavía no está cuantificada.

## Etapas posteriores

El [reporte final](reporte_final/README.md) es un índice de las secciones del repositorio y la [presentación final](presentacion/README.md) incluye los slides y el guion. No se hicieron pruebas con usuarios, instalación en terreno ni métricas de impacto.
