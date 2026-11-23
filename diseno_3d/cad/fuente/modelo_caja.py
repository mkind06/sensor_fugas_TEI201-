"""Gemelo 3D del encapsulado del detector de fugas (CadQuery).

Origen: centro de la base, z = 0 en el fondo exterior. Medidas en mm.
Genera STEP del ensamble (para importar en Fusion 360) y STL por pieza (para render).
"""
import os
import cadquery as cq

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

# ---------- Caja ----------
L, W, H = 120.0, 85.0, 40.0      # base exterior
PARED = 2.5
TAPA = 3.0
HOLG = 0.3                       # holgura del labio
BOSS = [(x, y) for x in (-54.0, 54.0) for y in (-36.5, 36.5)]
LEDS = [(10.0, -24.0, (0.18, 0.75, 0.35)), (26.0, -24.0, (0.98, 0.72, 0.10)), (42.0, -24.0, (0.90, 0.20, 0.15))]

base = cq.Workplane("XY").box(L, W, H, centered=(True, True, False)).edges("|Z").fillet(3)
cav = (cq.Workplane("XY").workplane(offset=PARED)
       .box(L - 2 * PARED, W - 2 * PARED, H, centered=(True, True, False)).edges("|Z").fillet(1))
base = base.cut(cav)
for x, y in BOSS:
    torre = cq.Workplane("XY").workplane(offset=PARED).center(x, y).circle(4).extrude(H - PARED)
    base = base.union(torre)
    base = base.cut(cq.Workplane("XY").workplane(offset=H - 12).center(x, y).circle(1.25).extrude(12))
# postes de la placa perforada (70 x 50, centro en x = -20)
POSTES = [(-52.0, -22.0), (-52.0, 22.0), (12.0, -22.0), (12.0, 22.0)]
for x, y in POSTES:
    base = base.union(cq.Workplane("XY").workplane(offset=PARED).center(x, y).circle(2.5).extrude(5))
    base = base.cut(cq.Workplane("XY").workplane(offset=PARED + 1).center(x, y).circle(0.8).extrude(5))
# ventana USB-C 12 x 7 en la pared izquierda, alineada con la ESP32 sobre cabezales
base = base.cut(cq.Workplane("XY").box(10, 12, 7).translate((-L / 2 + 1, 0, 20.5)))
# 2 agujeros para prensaestopas PG7 en la pared derecha
for y in (-15.0, 15.0):
    base = base.cut(cq.Workplane("YZ").workplane(offset=L / 2 - 5).center(y, 20).circle(6.25).extrude(10))

# ---------- Tapa ----------
tapa = cq.Workplane("XY").workplane(offset=H).box(L, W, TAPA, centered=(True, True, False)).edges("|Z").fillet(3)
li_ext = (L - 2 * PARED - 2 * HOLG, W - 2 * PARED - 2 * HOLG)
labio = (cq.Workplane("XY").workplane(offset=H - 2).rect(*li_ext).extrude(2)
         .cut(cq.Workplane("XY").workplane(offset=H - 2).rect(li_ext[0] - 3, li_ext[1] - 3).extrude(2)))
for x, y in BOSS:
    labio = labio.cut(cq.Workplane("XY").workplane(offset=H - 2).center(x, y).circle(4.5).extrude(2))
tapa = tapa.union(labio)
for x, y in BOSS:
    tapa = tapa.cut(cq.Workplane("XY").workplane(offset=H - 1).center(x, y).circle(1.7).extrude(6))
for x, y, _ in LEDS:
    tapa = tapa.cut(cq.Workplane("XY").workplane(offset=H - 1).center(x, y).circle(2.5).extrude(6))

# ---------- Electrónica (volúmenes referenciales) ----------
Z_PLACA = PARED + 5                       # cara inferior de la placa perforada
placa = cq.Workplane("XY").box(70, 50, 1.6, centered=(True, True, False)).translate((-20, 0, Z_PLACA))
Z_TOP = Z_PLACA + 1.6
cabezales = (cq.Workplane("XY").box(20, 2.5, 8.5, centered=(True, True, False)).translate((-43.5, -7.6, Z_TOP))
             .union(cq.Workplane("XY").box(20, 2.5, 8.5, centered=(True, True, False)).translate((-43.5, 7.6, Z_TOP))))
Z_ESP = Z_TOP + 8.5
esp_pcb = cq.Workplane("XY").box(23, 18, 1.0, centered=(True, True, False)).translate((-43.5, 0, Z_ESP))
esp_chip = cq.Workplane("XY").box(7, 7, 0.9, centered=(True, True, False)).translate((-41, 0, Z_ESP + 1))
usbc = (cq.Workplane("YZ").rect(9, 3.2).extrude(7.3).edges("|X").fillet(1.4)
        .translate((-55.5, 0, Z_ESP + 1 + 1.6)))
resist = None
for i in range(7):
    r = (cq.Workplane("XZ").circle(1.15).extrude(6).translate((-24 + i * 5.5, 13, Z_TOP + 1.2)))
    resist = r if resist is None else resist.union(r)
borneras = (cq.Workplane("XY").box(7.5, 10, 10, centered=(True, True, False)).translate((9, -15, Z_TOP))
            .union(cq.Workplane("XY").box(7.5, 10, 10, centered=(True, True, False)).translate((9, 15, Z_TOP))))

leds = []
for x, y, col in LEDS:
    cuerpo = cq.Workplane("XY").workplane(offset=H - 4).center(x, y).circle(2.5).extrude(6.5)
    domo = cq.Workplane("XY").sphere(2.5).translate((x, y, H + 2.5))
    aro = cq.Workplane("XY").workplane(offset=H - 4).center(x, y).circle(2.9).extrude(1)
    leds.append((cuerpo.union(domo).union(aro), col))

prensas = None
for y in (-15.0, 15.0):
    tuerca = cq.Workplane("YZ").workplane(offset=L / 2 - PARED - 4).center(y, 20).polygon(6, 17).extrude(4)
    cuerpo = cq.Workplane("YZ").workplane(offset=L / 2).center(y, 20).polygon(6, 17).extrude(5)
    domo = cq.Workplane("YZ").workplane(offset=L / 2 + 5).center(y, 20).circle(7).extrude(6).faces(">X").edges().fillet(3)
    p = tuerca.union(cuerpo).union(domo)
    prensas = p if prensas is None else prensas.union(p)
cables = None
for y in (-15.0, 15.0):
    c = cq.Workplane("YZ").workplane(offset=L / 2 + 8).center(y, 20).circle(2.2).extrude(30)
    cables = c if cables is None else cables.union(c)

tornillos = None
for x, y in BOSS:
    t = (cq.Workplane("XY").workplane(offset=H + TAPA - 10).center(x, y).circle(1.5).extrude(10)
         .union(cq.Workplane("XY").workplane(offset=H + TAPA).center(x, y).circle(2.75).extrude(3)))
    tornillos = t if tornillos is None else tornillos.union(t)

PIEZAS = {
    "base": (base, (0.17, 0.36, 0.33)),
    "tapa": (tapa, (0.21, 0.43, 0.40)),
    "placa": (placa, (0.78, 0.62, 0.38)),
    "cabezales": (cabezales, (0.10, 0.10, 0.11)),
    "esp_pcb": (esp_pcb, (0.08, 0.10, 0.16)),
    "esp_chip": (esp_chip, (0.75, 0.76, 0.78)),
    "usbc": (usbc, (0.80, 0.81, 0.83)),
    "resistencias": (resist, (0.86, 0.78, 0.60)),
    "borneras": (borneras, (0.15, 0.55, 0.85)),
    "prensaestopas": (prensas, (0.12, 0.12, 0.13)),
    "cables": (cables, (0.55, 0.57, 0.58)),
    "tornillos": (tornillos, (0.72, 0.73, 0.75)),
}
for i, (led, col) in enumerate(leds):
    PIEZAS[f"led{i+1}"] = (led, col)

if __name__ == "__main__":
    asm = cq.Assembly(name="detector_fugas")
    for n, (s, c) in PIEZAS.items():
        asm.add(s, name=n, color=cq.Color(*c))
        cq.exporters.export(s, os.path.join(OUT, f"{n}.stl"), tolerance=0.03, angularTolerance=0.1)
    asm.save(os.path.join(OUT, "gemelo_3d_ensamble.step"))
    cq.exporters.export(base, os.path.join(OUT, "caja_base.step"))
    cq.exporters.export(tapa, os.path.join(OUT, "caja_tapa.step"))
    print("ok")
