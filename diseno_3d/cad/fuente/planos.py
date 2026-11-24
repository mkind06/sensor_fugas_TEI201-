"""Planos técnicos de la caja v3 (A3) a partir de las medidas de modelo_caja.py."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import matplotlib.image as mpimg

L, W, H, PARED, TAPA, HOLG = 120.0, 85.0, 40.0, 2.5, 3.0, 0.3
BOSS = [(x, y) for x in (-54.0, 54.0) for y in (-36.5, 36.5)]
POSTES = [(-52.0, -22.0), (-52.0, 22.0), (12.0, -22.0), (12.0, 22.0)]
LEDS = [(10.0, -24.0), (26.0, -24.0), (42.0, -24.0)]
LIP = (L - 2 * PARED - 2 * HOLG, W - 2 * PARED - 2 * HOLG)

A3 = (420, 297)
MM = 1 / 25.4
LW, THIN = 0.7, 0.3
INK, DIM, HID, CEN = "#111111", "#1a4d8f", "#555555", "#aa3333"
RENDERS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "renders") + os.sep


def sheet():
    fig = plt.figure(figsize=(A3[0] * MM, A3[1] * MM))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, A3[0]); ax.set_ylim(0, A3[1]); ax.set_aspect("equal"); ax.axis("off")
    ax.add_patch(Rectangle((10, 10), A3[0] - 20, A3[1] - 20, fill=False, lw=1.0, ec=INK))
    return fig, ax


def cajetin(ax, titulo, hoja, escala="1:1", notas=()):
    x0, y0, w, h = 250, 10, 160, 42
    ax.add_patch(Rectangle((x0, y0), w, h, fill=False, lw=0.8, ec=INK))
    for yy in (y0 + 14, y0 + 28):
        ax.plot([x0, x0 + w], [yy, yy], lw=0.5, c=INK)
    ax.plot([x0 + 100, x0 + 100], [y0, y0 + 28], lw=0.5, c=INK)
    ax.text(x0 + 3, y0 + 35, "Riego Monitor · Caja v3 del detector de fugas", fontsize=10, weight="bold", va="center")
    ax.text(x0 + 3, y0 + 21, titulo, fontsize=9, va="center")
    ax.text(x0 + 103, y0 + 21, f"Hoja {hoja} de 3", fontsize=8, va="center")
    ax.text(x0 + 3, y0 + 9.5, "TEI201 · UAI · García, Miranda, Kuperman, Kind", fontsize=6.5, va="center")
    ax.text(x0 + 3, y0 + 4, "Unidades: mm · Tol. general ±0,2 · Material: PETG · 23-11-2026", fontsize=6.5, va="center")
    ax.text(x0 + 103, y0 + 9.5, f"Escala {escala} (A3)", fontsize=7.5, va="center")
    ax.text(x0 + 103, y0 + 4, "Proyección ISO (1.er diedro)", fontsize=6.5, va="center")
    ny = 60
    for n in reversed(notas):
        ax.text(250, ny, n, fontsize=6.8, va="bottom", color="#333")
        ny += 5


def rrect(ax, cx, cy, w, h, r, **kw):
    ax.add_patch(FancyBboxPatch((cx - w / 2 + r, cy - h / 2 + r), w - 2 * r, h - 2 * r,
                                boxstyle=f"round,pad={r}", fill=False, **kw))


def circ(ax, cx, cy, d, **kw):
    ax.add_patch(Circle((cx, cy), d / 2, fill=False, **kw))


def centro(ax, cx, cy, s=4):
    ax.plot([cx - s, cx + s], [cy, cy], lw=0.25, c=CEN, ls=(0, (6, 2, 1, 2)))
    ax.plot([cx, cx], [cy - s, cy + s], lw=0.25, c=CEN, ls=(0, (6, 2, 1, 2)))


def cota(ax, p1, p2, off, texto, horiz=True, fs=6.5):
    (x1, y1), (x2, y2) = p1, p2
    if horiz:
        y = y1 + off
        ax.plot([x1, x1], [y1, y + (1.5 if off > 0 else -1.5)], lw=THIN, c=DIM)
        ax.plot([x2, x2], [y2, y + (1.5 if off > 0 else -1.5)], lw=THIN, c=DIM)
        ax.annotate("", (x1, y), (x2, y), arrowprops=dict(arrowstyle="<|-|>", lw=THIN, color=DIM, mutation_scale=5))
        ax.text((x1 + x2) / 2, y + 0.8, texto, ha="center", va="bottom", fontsize=fs, color=DIM)
    else:
        x = x1 + off
        ax.plot([x1, x + (1.5 if off > 0 else -1.5)], [y1, y1], lw=THIN, c=DIM)
        ax.plot([x2, x + (1.5 if off > 0 else -1.5)], [y2, y2], lw=THIN, c=DIM)
        ax.annotate("", (x, y1), (x, y2), arrowprops=dict(arrowstyle="<|-|>", lw=THIN, color=DIM, mutation_scale=5))
        ax.text(x - 0.8, (y1 + y2) / 2, texto, ha="right", va="center", fontsize=fs, color=DIM, rotation=90)


def etiqueta(ax, x, y, tx, ty, texto):
    ax.annotate(texto, (x, y), (tx, ty), fontsize=6.3, color=DIM,
                arrowprops=dict(arrowstyle="-|>", lw=THIN, color=DIM, mutation_scale=5))


def titulo_vista(ax, x, y, t):
    ax.text(x, y, t, fontsize=8, weight="bold", ha="center")


# ------------------------------------------------------------------ HOJA 1: BASE
def hoja_base(pdf):
    fig, ax = sheet()
    # Planta (vista superior) centrada en (110, 200)
    cx, cy = 105, 195
    rrect(ax, cx, cy, L, W, 3, lw=LW, ec=INK)
    rrect(ax, cx, cy, L - 2 * PARED, W - 2 * PARED, 1, lw=THIN, ec=INK)
    for x, y in BOSS:
        circ(ax, cx + x, cy + y, 8, lw=THIN, ec=INK); circ(ax, cx + x, cy + y, 2.5, lw=THIN, ec=INK); centro(ax, cx + x, cy + y, 5.5)
    for x, y in POSTES:
        circ(ax, cx + x, cy + y, 5, lw=THIN, ec=INK); circ(ax, cx + x, cy + y, 1.6, lw=THIN, ec=INK); centro(ax, cx + x, cy + y, 4)
    # placa referencial
    ax.add_patch(Rectangle((cx - 20 - 35, cy - 25), 70, 50, fill=False, lw=0.3, ec="#888", ls=(0, (2, 2))))
    ax.text(cx - 20, cy, "Placa perforada 70 × 50\n(referencia, sobre 4 postes)", fontsize=5.8, color="#777", ha="center", va="center")
    # ventana USB (oculta en planta)
    ax.add_patch(Rectangle((cx - L / 2, cy - 6), PARED, 12, fill=False, lw=0.4, ec=HID, ls=(0, (3, 2))))
    for y in (-15, 15):
        ax.add_patch(Rectangle((cx + L / 2 - PARED, cy + y - 6.25), PARED, 12.5, fill=False, lw=0.4, ec=HID, ls=(0, (3, 2))))
    cota(ax, (cx - L / 2, cy + W / 2), (cx + L / 2, cy + W / 2), 10, "120")
    cota(ax, (cx - L / 2, cy - W / 2), (cx - L / 2, cy + W / 2), -10, "85", horiz=False)
    cota(ax, (cx - 54, cy - W / 2), (cx + 54, cy - W / 2), -8, "108 (torretas)")
    cota(ax, (cx + L / 2, cy - 36.5), (cx + L / 2, cy + 36.5), 9, "73", horiz=False)
    cota(ax, (cx - 52, cy - W / 2), (cx + 12, cy - W / 2), -15, "64 (postes)")
    cota(ax, (cx + 12, cy - 22), (cx + 12, cy + 22), 20, "44", horiz=False)
    etiqueta(ax, cx + 54, cy + 36.5, cx + 40, cy + 58, "4× torreta Ø8, piloto Ø2,5 × 12 (M3)")
    etiqueta(ax, cx - 52, cy + 22, cx - 62, cy + 58, "4× poste Ø5 × 5, piloto Ø1,6")
    etiqueta(ax, cx + L / 2 - 1, cy - W / 2 + 1, cx + 66, cy - 55, "Pared 2,5 · radio exterior 3")
    titulo_vista(ax, cx, cy + W / 2 + 26, "PLANTA (vista superior)")

    # Alzado lateral izquierdo (pared con USB), vista desde -X: eje horizontal = Y, vertical = Z
    lx, ly = 255, 160
    ax.add_patch(Rectangle((lx - W / 2, ly), W, H, fill=False, lw=LW, ec=INK))
    ax.plot([lx - W / 2, lx + W / 2], [ly + PARED, ly + PARED], lw=0.4, c=HID, ls=(0, (3, 2)))
    ax.add_patch(Rectangle((lx - 6, ly + 20.5 - 3.5), 12, 7, fill=False, lw=LW, ec=INK))
    centro(ax, lx, ly + 20.5, 8)
    cota(ax, (lx - W / 2, ly + H), (lx + W / 2, ly + H), 7, "85")
    cota(ax, (lx - W / 2, ly), (lx - W / 2, ly + H), -7, "40", horiz=False)
    cota(ax, (lx - 6, ly), (lx + 6, ly), -6, "12")
    cota(ax, (lx + 6, ly + 17), (lx + 6, ly + 24), 14, "7", horiz=False)
    cota(ax, (lx + W / 2, ly), (lx + W / 2, ly + 20.5), 8, "20,5", horiz=False)
    etiqueta(ax, lx + 6, ly + 20.5, lx + 22, ly + 52, "Ventana USB-C 12 × 7")
    titulo_vista(ax, lx, ly + H + 20, "VISTA LATERAL IZQUIERDA (USB)")

    # Alzado lateral derecho (prensaestopas)
    rx, ry = 360, 160
    ax.add_patch(Rectangle((rx - W / 2, ry), W, H, fill=False, lw=LW, ec=INK))
    for y in (-15, 15):
        circ(ax, rx + y, ry + 20, 12.5, lw=LW, ec=INK); centro(ax, rx + y, ry + 20, 9)
    cota(ax, (rx - 15, ry + H), (rx + 15, ry + H), 7, "30")
    cota(ax, (rx + W / 2, ry), (rx + W / 2, ry + 20), 8, "20", horiz=False)
    etiqueta(ax, rx + 15 + 4.4, ry + 20 + 4.4, rx + 22, ry + 52, "2× Ø12,5 para PG7")
    titulo_vista(ax, rx, ry + H + 20, "VISTA LATERAL DERECHA (cables)")

    # Alzado frontal con corte de cavidad
    fx, fy = 105, 62
    ax.add_patch(Rectangle((fx - L / 2, fy), L, H, fill=False, lw=LW, ec=INK))
    ax.plot([fx - L / 2 + PARED, fx - L / 2 + PARED], [fy + PARED, fy + H], lw=0.4, c=HID, ls=(0, (3, 2)))
    ax.plot([fx + L / 2 - PARED, fx + L / 2 - PARED], [fy + PARED, fy + H], lw=0.4, c=HID, ls=(0, (3, 2)))
    ax.plot([fx - L / 2 + PARED, fx + L / 2 - PARED], [fy + PARED, fy + PARED], lw=0.4, c=HID, ls=(0, (3, 2)))
    cota(ax, (fx - L / 2, fy), (fx + L / 2, fy), -6, "120")
    cota(ax, (fx + L / 2, fy), (fx + L / 2, fy + PARED), 6, "2,5", horiz=False)
    titulo_vista(ax, fx, fy + H + 8, "ALZADO FRONTAL (ocultas: cavidad)")

    cajetin(ax, "BASE · plano de pieza", 2, notas=(
        "Notas: medidas tomadas del modelo CadQuery (diseno_3d/cad/fuente/modelo_caja.py).",
        "Impresión sugerida: PETG, capa 0,2 mm, 3 perímetros, relleno 30 %.",
        "Las medidas de la electrónica son referenciales: verificar antes de imprimir.",
    ))
    pdf.savefig(fig); plt.close(fig)


# ------------------------------------------------------------------ HOJA 2: TAPA
def hoja_tapa(pdf):
    fig, ax = sheet()
    cx, cy = 105, 190
    rrect(ax, cx, cy, L, W, 3, lw=LW, ec=INK)
    ax.add_patch(Rectangle((cx - LIP[0] / 2, cy - LIP[1] / 2), *LIP, fill=False, lw=0.4, ec=HID, ls=(0, (3, 2))))
    ax.add_patch(Rectangle((cx - LIP[0] / 2 + 1.5, cy - LIP[1] / 2 + 1.5), LIP[0] - 3, LIP[1] - 3, fill=False, lw=0.4, ec=HID, ls=(0, (3, 2))))
    for x, y in BOSS:
        circ(ax, cx + x, cy + y, 3.4, lw=LW, ec=INK); centro(ax, cx + x, cy + y, 4)
    for x, y in LEDS:
        circ(ax, cx + x, cy + y, 5, lw=LW, ec=INK); centro(ax, cx + x, cy + y, 4.5)
    cota(ax, (cx - L / 2, cy + W / 2), (cx + L / 2, cy + W / 2), 10, "120")
    cota(ax, (cx - L / 2, cy - W / 2), (cx - L / 2, cy + W / 2), -10, "85", horiz=False)
    cota(ax, (cx + 10, cy - 24), (cx + 42, cy - 24), -24, "2 × 16 = 32 (LED)")
    cota(ax, (cx, cy - W / 2), (cx + 10, cy - W / 2), -8, "10")
    cota(ax, (cx + 42, cy - 24), (cx + 42, cy), 26, "24", horiz=False)
    ax.plot([cx - L / 2 + 3, cx + L / 2 - 3], [cy, cy], lw=0.25, c=CEN, ls=(0, (6, 2, 1, 2)))
    ax.plot([cx, cx], [cy - W / 2 + 3, cy + W / 2 - 3], lw=0.25, c=CEN, ls=(0, (6, 2, 1, 2)))
    etiqueta(ax, cx + 54, cy + 36.5, cx + 72, cy + 52, "4× Ø3,4 pasante (M3 × 10)")
    etiqueta(ax, cx + 26, cy - 24, cx + 55, cy - 62, "3× Ø5 para LED 5 mm (verde, amarillo, rojo)")
    etiqueta(ax, cx - LIP[0] / 2, cy + 10, cx - 85, cy + 55, "Labio 114,4 × 79,4 × 2, ancho 1,5 (oculto)")
    titulo_vista(ax, cx, cy + W / 2 + 22, "PLANTA (vista superior)")

    # Sección A-A
    sx, sy = 300, 175
    ax.add_patch(Rectangle((sx - L / 2, sy + 2), L, TAPA, fill=True, fc="#e8e8e8", lw=LW, ec=INK, hatch="////"))
    for side in (-1, 1):
        x_out = sx + side * LIP[0] / 2
        x_in = x_out - side * 1.5
        ax.add_patch(Rectangle((min(x_out, x_in), sy), 1.5, 2, fill=True, fc="#e8e8e8", lw=LW, ec=INK, hatch="////"))
    cota(ax, (sx - L / 2, sy + 5), (sx + L / 2, sy + 5), 8, "120")
    cota(ax, (sx + L / 2, sy + 2), (sx + L / 2, sy + 5), 8, "3", horiz=False)
    cota(ax, (sx + L / 2, sy), (sx + L / 2, sy + 2), 16, "2", horiz=False)
    cota(ax, (sx - LIP[0] / 2, sy), (sx + LIP[0] / 2, sy), -7, "114,4")
    etiqueta(ax, sx - LIP[0] / 2 + 0.7, sy + 1, sx - 40, sy - 22, "Holgura 0,3 por lado con la base")
    titulo_vista(ax, sx, sy + 26, "SECCIÓN A-A (eje Y = 0)")

    # Detalle LED escala 2:1
    dx, dy = 300, 90
    ax.add_patch(Rectangle((dx - 20, dy), 40, TAPA * 2, fill=True, fc="#e8e8e8", lw=LW, ec=INK, hatch="////"))
    ax.add_patch(Rectangle((dx - 5, dy - 0.2), 10, TAPA * 2 + 0.4, fill=True, fc="white", lw=0))
    ax.plot([dx - 5, dx - 5], [dy, dy + 6], lw=LW, c=INK); ax.plot([dx + 5, dx + 5], [dy, dy + 6], lw=LW, c=INK)
    cota(ax, (dx - 5, dy + 6), (dx + 5, dy + 6), 6, "Ø5")
    cota(ax, (dx + 20, dy), (dx + 20, dy + 6), 6, "3", horiz=False)
    titulo_vista(ax, dx, dy + 20, "DETALLE B: agujero de LED (escala 2:1)")

    cajetin(ax, "TAPA · plano de pieza", 3, notas=(
        "Notas: la tapa se fija con 4 tornillos M3 × 10 a las torretas de la base.",
        "Los LED se pegan desde el interior; sus patas van a la placa por cable.",
        "Medidas del modelo CadQuery; verificar ajuste del labio con una impresión de prueba.",
    ))
    pdf.savefig(fig); plt.close(fig)


# ------------------------------------------------------------------ HOJA 3: CONJUNTO
def hoja_conjunto(pdf):
    fig, ax = sheet()
    for i, (img, ext) in enumerate([("02_caja_explosionada.png", [20, 200, 150, 280]),
                                     ("01_caja_exterior.png", [215, 410, 150, 280])]):
        im = mpimg.imread(RENDERS + img)
        h, w = im.shape[:2]
        x0, x1, y0, y1 = ext
        bw, bh = x1 - x0, y1 - y0
        s = min(bw / w, bh / h)
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        ax.imshow(im, extent=[cx - w * s / 2, cx + w * s / 2, cy - h * s / 2, cy + h * s / 2], zorder=1)
    titulo_vista(ax, 110, 143, "VISTA EXPLOSIONADA (referencia)")
    titulo_vista(ax, 312, 143, "VISTA ISOMÉTRICA (referencia)")

    filas = [("N°", "Pieza", "Cant.", "Material / especificación"),
             ("1", "Base 120 × 85 × 40", "1", "PETG impreso"),
             ("2", "Tapa 120 × 85 × 3 con labio", "1", "PETG impreso"),
             ("3", "Tornillo M3 × 10 cabeza cilíndrica", "4", "Acero"),
             ("4", "Prensaestopa PG7 (cable Ø3–6,5)", "2", "Nylon"),
             ("5", "LED 5 mm verde / amarillo / rojo", "3", "Con resistencia en la placa"),
             ("6", "Placa perforada 5 × 7 cm soldada", "1", "FR4, sobre 4 postes"),
             ("7", "ESP32-S3 Super Mini", "1", "En cabezales hembra"),
             ("8", "Conectores de 3 pines para sensores", "2", "Tira hembra 2,54 mm")]
    x0, y0, rh = 20, 125, 7.5
    cols = [0, 10, 95, 112, 200]
    for i, f in enumerate(filas):
        y = y0 - i * rh
        ax.add_patch(Rectangle((x0, y - rh), cols[-1], rh, fill=(i == 0), fc="#eef2f6", lw=0.5, ec=INK))
        for j, t in enumerate(f):
            ax.text(x0 + cols[j] + 1.5, y - rh / 2, t, fontsize=6.8, va="center", weight="bold" if i == 0 else "normal")
    for c in cols[1:-1]:
        ax.plot([x0 + c, x0 + c], [y0, y0 - len(filas) * rh], lw=0.5, c=INK)
    ax.text(x0, y0 + 3, "LISTA DE PIEZAS DE LA CAJA", fontsize=8, weight="bold")

    ax.text(235, 125, "Dimensiones generales del conjunto: 120 × 85 × 43 mm (base 40 + tapa 3)\n"
            "más prensaestopas: 131 mm en X.", fontsize=7, va="top")
    ax.text(235, 108, "Diseño para la reparación:\n"
            "• La tapa sale quitando 4 tornillos.\n"
            "• La ESP32 se retira de sus cabezales sin desoldar.\n"
            "• Cada sensor se desconecta de su conector de 3 pines.\n"
            "• Ventana USB-C para reprogramar sin abrir la caja.", fontsize=7, va="top")
    cajetin(ax, "CONJUNTO · vistas de referencia y lista de piezas", 1, escala="S/E")
    pdf.savefig(fig); plt.close(fig)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "planos", "planos_caja_v3.pdf")
    with PdfPages(out) as pdf:
        hoja_conjunto(pdf)
        hoja_base(pdf)
        hoja_tapa(pdf)
        d = pdf.infodict(); d["Title"] = "Planos caja v3 - Riego Monitor"; d["Author"] = "Equipo TEI201"
    print(out)
