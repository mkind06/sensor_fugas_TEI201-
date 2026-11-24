"""Esquemático del Riego Monitor v3 (placa perforada soldada).

Genera esquematico_v3.pdf, .svg y .png en esta carpeta.
Uso:  pip install schemdraw matplotlib  y luego  python esquematico.py
Pines según software/src/RiegoMonitor_WiFi/RiegoMonitor_WiFi.ino.
"""
import os
import schemdraw
import schemdraw.elements as elm

AQUI = os.path.dirname(os.path.abspath(__file__))
schemdraw.config(fontsize=11, lw=1.4)

with schemdraw.Drawing(show=False) as d:
    esp = elm.Ic(
        pins=[
            elm.IcPin(name="GND", side="left"),
            elm.IcPin(name="GPIO2", side="left"),
            elm.IcPin(name="GPIO8", side="left"),
            elm.IcPin(name="5V", side="left"),
            elm.IcPin(name="GPIO6", side="right"),
            elm.IcPin(name="GPIO5", side="right"),
            elm.IcPin(name="GPIO4", side="right"),
            elm.IcPin(name="USB", side="top"),
        ],
        size=(6.2, 12.0), pinspacing=3.0, edgepadW=0.5, edgepadH=1.2, label="",
    ).at((15, 0)).anchor("center")
    d += esp
    cx = esp.USB[0]
    d += elm.Label().at((cx, (esp["GPIO8"][1] + esp["GPIO2"][1]) / 2)).label("ESP32-S3\nSuper Mini\n(en cabezales\nhembra)", fontsize=11)

    y5, yg = esp["5V"][1], esp.GND[1] - 2.0

    # USB (programación / alimentación de respaldo)
    d += elm.Line().at(esp.USB).up(1.0)
    d += elm.Label().at((cx, esp.USB[1] + 1.1)).label("USB-C: programar y alimentar (5 V)", loc="top", fontsize=10)

    # Rieles +5 V y GND
    d += elm.Line().at(esp["5V"]).tox(3.0)
    d += elm.Label().at((3.0, y5)).label("+5 V", loc="left", fontsize=11)
    d += elm.Line().at(esp.GND).left(0.4)
    d += elm.Line().toy(yg).dot()
    d += elm.Ground().at((esp.GND[0] - 0.4, yg))
    d += elm.Line().at((esp.GND[0] - 0.4, yg)).tox(3.0)
    d += elm.Label().at((3.0, yg)).label("GND común", loc="left", fontsize=11)

    # Sensores con divisor 10 kΩ / 20 kΩ
    for i, (gpio, nombre) in enumerate([("GPIO8", "FS400A\nentrada\n(S1)"), ("GPIO2", "FS400A\nsalida\n(S2)")]):
        gx, gy = esp[gpio]
        x0, x1, y0, y1 = -0.6, 1.6, gy - 1.1, gy + 1.1
        d += elm.Line().at((x0, y0)).tox(x1)
        d += elm.Line().toy(y1)
        d += elm.Line().tox(x0)
        d += elm.Line().toy(y0)
        d += elm.Label().at(((x0 + x1) / 2 - 0.2, gy)).label(nombre, fontsize=10)
        xv, xg = 3.0 + 0.8 * i, 3.4 + 0.8 * i
        # +5 V (rojo)
        d += elm.Line().at((x1, gy + 0.7)).tox(xv)
        d += elm.Label().at((x1 + 0.35, gy + 0.7)).label("+5V", loc="top", fontsize=8)
        d += elm.Line().at((xv, gy + 0.7)).toy(y5).dot()
        # GND (negro)
        d += elm.Line().at((x1, gy - 0.7)).tox(xg)
        d += elm.Label().at((x1 + 0.35, gy - 0.7)).label("GND", loc="top", fontsize=8)
        d += elm.Line().at((xg, gy - 0.7)).toy(yg).dot()
        # Señal (amarillo) -> 10 kΩ -> nodo -> GPIO ; nodo -> 20 kΩ -> GND
        d += elm.Line().at((x1, gy)).tox(5.4)
        d += elm.Label().at((x1 + 0.35, gy)).label("SIG", loc="top", fontsize=8)
        d += elm.Resistor().right(2.4).label("10 kΩ", fontsize=10)
        nodo = (8.6 + 1.8 * i, gy)
        d += elm.Line().at((7.8, gy)).tox(nodo[0])
        d += elm.Dot().at(nodo)
        d += elm.Line().at(nodo).tox(gx)
        d += elm.Resistor().at(nodo).down(2.0).label("20 kΩ", loc="bottom", fontsize=10)
        d += elm.Line().toy(yg).dot()

    d += elm.Label().at((-0.6, yg - 1.0)).label(
        "Cada FS400A: rojo = +5 V · negro = GND · amarillo = señal (SIG).\n"
        "Divisor: 5 V × 20 / (10 + 20) ≈ 3,3 V en el GPIO (la ESP32 trabaja a 3,3 V).",
        loc="right", fontsize=9, halign="left")

    # LED con resistencia
    for gpio, color in [("GPIO4", "verde"), ("GPIO5", "amarillo"), ("GPIO6", "rojo")]:
        d += elm.Line().at(esp[gpio]).right(0.5)
        d += elm.Resistor().right(2.2).label("330 Ω", fontsize=10)
        d += elm.LED().right(1.8).label(f"LED {color}", loc="bottom", fontsize=10)
        d += elm.Line().right(0.5)
        d += elm.Ground()

    # Bomba con fuente independiente
    bx, by = esp["GPIO6"][0] + 1.5, yg - 1.2
    d += elm.SourceV().at((bx, by)).up(2.0).label("Fuente 5 V\nde la bomba", loc="left", fontsize=10)
    d += elm.Line().right(1.2)
    d += elm.Motor().down(2.0).label("Bomba\nsumergible", loc="bottom", fontsize=10)
    d += elm.Line().left(1.2)
    d += elm.Label().at((bx + 0.6, by - 0.9)).label("Circuito separado: sin conexión eléctrica con la ESP32", fontsize=9)

    # Cajetín
    d += elm.Label().at((-0.6, yg - 3.4)).label(
        "Riego Monitor v3 · Esquemático eléctrico · TEI201 Taller de Diseño en Ingeniería · UAI · 23-11-2026\n"
        "Pines según software/src/RiegoMonitor_WiFi/RiegoMonitor_WiFi.ino. Coordenadas en la placa: README.md de esta carpeta.",
        loc="right", fontsize=9, halign="left")

    d.save(os.path.join(AQUI, "esquematico_v3.svg"))
    d.save(os.path.join(AQUI, "esquematico_v3.pdf"))
    d.save(os.path.join(AQUI, "esquematico_v3.png"), dpi=160)
print("ok")
