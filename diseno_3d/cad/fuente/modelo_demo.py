"""Gemelo 3D de la demostración: banco de PVC 32 mm + estanque + caja con la electrónica.

Ejes: x a la derecha, y hacia el fondo, z hacia arriba; z = 0 es la mesa. Medidas en mm.
Las medidas del banco son aproximadas, tomadas de las fotos del prototipo.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cadquery as cq
from cadquery import Vector as V
import modelo_caja as modelo  # caja y electrónica (no exporta al importarse)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out_demo")
os.makedirs(OUT, exist_ok=True)

R_TUBO, R_FIT, ZC = 16.0, 20.0, 20.0   # PVC 32 mm, fittings y altura del eje


def cil(p1, p2, r):
    p1, p2 = V(*p1), V(*p2)
    d = p2 - p1
    return cq.Workplane().add(cq.Solid.makeCylinder(r, d.Length, p1, d.normalized()))


def tubo(pts, r=R_TUBO):
    s = None
    for a, b in zip(pts[:-1], pts[1:]):
        c = cil(a, b, r)
        s = c if s is None else s.union(c)
    return s


def codo(c, d1, d2):
    """Codo en el punto c con bocas hacia d1 y d2 (vectores unitarios)."""
    c = V(*c)
    s = cq.Workplane().add(cq.Solid.makeSphere(R_FIT, c, angleDegrees1=-90, angleDegrees2=90))
    for d in (V(*d1), V(*d2)):
        s = s.union(cil(c, c + d * 30, R_FIT))
    return s


def cable(pts, r=2.2):
    s = tubo(pts, r)
    for p in pts[1:-1]:
        s = s.union(cq.Workplane().add(cq.Solid.makeSphere(r, V(*p), angleDegrees1=-90, angleDegrees2=90)))
    return s


# ---------- Recorrido del agua ----------
XL, XR, YB, YT = -150.0, 150.0, -120.0, 130.0
tubos = (tubo([(-60, 175, ZC), (-60, YT, ZC), (XL, YT, ZC), (XL, YB, ZC), (XR, YB, ZC),
               (XR, YT, ZC), (60, YT, ZC), (60, YT, 110), (60, 185, 110)]))
fittings = None
for c, d1, d2 in [((-60, YT, ZC), (0, 1, 0), (-1, 0, 0)), ((XL, YT, ZC), (1, 0, 0), (0, -1, 0)),
                  ((XL, YB, ZC), (0, 1, 0), (1, 0, 0)), ((XR, YB, ZC), (-1, 0, 0), (0, 1, 0)),
                  ((XR, YT, ZC), (0, -1, 0), (-1, 0, 0)), ((60, YT, ZC), (1, 0, 0), (0, 0, 1)),
                  ((60, YT, 110), (0, 0, -1), (0, 1, 0))]:
    f = codo(c, d1, d2)
    fittings = f if fittings is None else fittings.union(f)
# coplas en los tramos rectos (como en las fotos)
for p, d in [((-75, YB, ZC), (1, 0, 0)), ((75, YB, ZC), (1, 0, 0)), ((XL, 70, ZC), (0, 1, 0)), ((XR, 70, ZC), (0, 1, 0))]:
    p, d = V(*p), V(*d)
    fittings = fittings.union(cil(p - d * 14, p + d * 14, R_FIT))
# tee al centro del tramo inferior, con la rama de fuga hacia el frente
tee = cil((-35, YB, ZC), (35, YB, ZC), R_FIT).union(cil((0, YB, ZC), (0, YB - 45, ZC), R_FIT))
rama = tubo([(0, YB - 45, ZC), (0, YB - 70, ZC)])
tubos = tubos.union(rama)

# ---------- Válvula de bola (fuga) ----------
YV = YB - 100
valvula = (cil((0, YV + 30, ZC), (0, YV - 30, ZC), 21)
           .union(cil((0, YV + 34, ZC), (0, YV + 26, ZC), 24))
           .union(cil((0, YV - 26, ZC), (0, YV - 40, ZC), 24))
           .union(cil((0, YV, ZC), (0, YV, ZC + 30), 5)))
manilla = cq.Workplane().box(70, 22, 6).translate((0, YV, ZC + 33))
boquilla = cil((0, YV - 40, ZC), (0, YV - 75, ZC), 11)

# ---------- Sensores FS400A ----------
sensores, tapas_s = None, None
for x in (XL, XR):
    cuerpo = (cil((x, -35, ZC), (x, 35, ZC), 19)
              .union(cil((x, -48, ZC), (x, -35, ZC), 21))
              .union(cil((x, 35, ZC), (x, 48, ZC), 21)))
    caja_h = cq.Workplane().box(30, 34, 22).edges("|Z").fillet(3).translate((x, 0, ZC + 26))
    s = cuerpo.union(caja_h)
    sensores = s if sensores is None else sensores.union(s)

# ---------- Estanque (bidón cortado) con agua y bomba ----------
estanque = (cq.Workplane().box(170, 170, 250, centered=(True, True, False)).edges("|Z").fillet(28)
            .translate((0, 265, 0)))
agua = (cq.Workplane().box(164, 164, 150, centered=(True, True, False)).edges("|Z").fillet(25)
        .translate((0, 265, 2)))
bomba = (cq.Workplane().box(40, 34, 32, centered=(True, True, False)).edges("|Z").fillet(5)
         .translate((-60, 205, 2)))

# ---------- Caja de la electrónica, girada para que los prensaestopas miren al banco ----------
BX, BY = 360.0, 0.0
def a_mesa(w):
    return w.rotate((0, 0, 0), (0, 0, 1), 180).translate((BX, BY, 0))

caja = {n: (a_mesa(s), c) for n, (s, c) in modelo.PIEZAS.items() if n != "tornillos"}

# ---------- Cables de los sensores hasta los prensaestopas ----------
G1, G2 = (BX - 98, BY + 15, ZC), (BX - 98, BY - 15, ZC)   # fin del tramo que sale de cada prensaestopas
cab_s1 = cable([(XL + 15, 0, ZC + 30), (XL + 45, -25, 4), (XR - 50, -75, 4), (XR - 25, -75, 44),
                (XR + 25, -75, 44), (XR + 50, -75, 4), (235, BY - 15, 4), G2])
cab_s2 = cable([(XR + 15, 0, ZC + 30), (XR + 45, 12, 4), (235, BY + 15, 4), G1])

# ---------- Mesa ----------
mesa = cq.Workplane().box(900, 760, 6, centered=(True, True, False)).translate((70, 20, -6))

PIEZAS = {
    "mesa": (mesa, (0.86, 0.82, 0.74)),
    "tubos": (tubos, (0.18, 0.56, 0.84)),
    "fittings": (fittings.union(tee), (0.15, 0.50, 0.78)),
    "valvula": (valvula, (0.45, 0.47, 0.50)),
    "manilla": (manilla, (0.10, 0.25, 0.75)),
    "boquilla": (boquilla, (0.93, 0.93, 0.92)),
    "sensores": (sensores, (0.10, 0.10, 0.11)),
    "estanque": (estanque, (0.85, 0.92, 0.95)),
    "agua": (agua, (0.45, 0.70, 0.90)),
    "bomba": (bomba, (0.12, 0.12, 0.13)),
    "cable_s1": (cab_s1, (0.10, 0.10, 0.10)),
    "cable_s2": (cab_s2, (0.10, 0.10, 0.10)),
}
for n, (s, c) in caja.items():
    PIEZAS["caja_" + n] = (s, c)

if __name__ == "__main__":
    asm = cq.Assembly(name="demo_detector_fugas")
    for n, (s, c) in PIEZAS.items():
        asm.add(s, name=n, color=cq.Color(*c))
        cq.exporters.export(s, os.path.join(OUT, f"{n}.stl"), tolerance=0.05, angularTolerance=0.15)
    asm.save(os.path.join(OUT, "gemelo_demo_completo.step"))
    print("ok")
