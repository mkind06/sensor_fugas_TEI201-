# Evidencias de Testing

## Evidencia recibida del montaje final - Avance 2

El equipo aportó dos fotografías originales, conservadas en [hardware/fotos](../../hardware/fotos/README.md). Permiten observar el banco completo y, en una de ellas, el monitor web con gráfico junto al concepto CAD. Las fotos no sustituyen registros de los tres estados ni una prueba continua de cinco minutos.

## Contenido Requerido (estado)

### Fotografías de banco (Avance #2)
| Archivo | Contenido | Estado |
|---|---|---|
| [Dos vistas del montaje final](../../hardware/fotos/README.md) | Banco hidráulico, sensores, llave, recipiente, electrónica y computador | Recibidas; ver alcance en sus leyendas |
| `banco_led_verde.jpg` | Llave cerrada → verde | ⏳ |
| `banco_led_amarillo.jpg` | Apertura parcial → amarillo | ⏳ |
| `banco_led_rojo.jpg` | Llave abierta → rojo | ⏳ |
| `monitor_serie_sin_fuga.png` | Q1 ≈ Q2, Dif ≈ 0 % | ⏳ |
| `monitor_serie_fuga.png` | Q2 = 0, Dif = 100 % | ⏳ |

### Videos
| Archivo | Contenido | Estado |
|---|---|---|
| `demo_fuga_gradual.mp4` | Abrir la llave de a poco: verde → amarillo → rojo, con Monitor Serie visible | ⏳ (sirve de plan B para la demo) |
| `estabilidad_5min.mp4` | Sistema funcionando 5 min seguidos | ⏳ |

### Sesiones con usuarios e instalación en terreno (Avance #3)
- `sesion_U01_[fecha].jpg` … `sesion_U05_[fecha].jpg`
- `instalacion_linea_riego_[fecha].jpg`

---

## Privacidad y Consentimiento
- [ ] Consentimiento informado de cada usuario
- [ ] Explicar uso académico de las imágenes
- [ ] Ofrecer anonimato (difuminar rostros, usar iniciales)

---

## Organización de Archivos
```
evidencias/
├── fotos/
│   ├── banco/
│   ├── sesiones_usuarios/
│   └── instalacion_terreno/
├── videos/
└── consentimientos/
```

## Nomenclatura
`[tipo]_[identificador]_[YYYYMMDD].jpg` → p. ej. `banco_led_rojo_20261020.jpg`
