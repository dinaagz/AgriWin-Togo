#!/usr/bin/env python3
"""AgriWin Togo — génération des variantes de logo en SVG vectoriel.

Le symbole n'est pas redessiné : il est vectorisé à partir du logo fourni par
le client (scripts/trace_symbol.py), puis décliné. Le plant de sisal, la
chèvre et leurs proportions sont donc exactement ceux de la marque ; seules
les valeurs de couleur sont ramenées sur la palette AgriWin Togo.
"""
import json
import os

OUT = os.path.dirname(os.path.abspath(__file__))

# ---- Palette de marque -------------------------------------------------
G950, G900, G700, G500, G400 = "#0F3D17", "#1B5E20", "#2E7D32", "#4E9F3D", "#66BB6A"
GOLD5, CREAM, WHITE = "#E0A83D", "#CFE6C9", "#FFFFFF"

# ---- Symbole vectorisé -------------------------------------------------
TRACE = json.load(open(os.path.join(OUT, "symbole-trace.json"), encoding="utf-8"))
SW, SH = TRACE["box"]
LAYERS = TRACE["layers"]
SILHOUETTE = LAYERS[0]["d"]   # la couche la plus claire couvre tout le signe
CONTOURS = LAYERS[-1]["d"]    # la plus sombre : contours des feuilles et chèvre


def symbol_tonal():
    """Le symbole en dégradé de verts, pour les fonds clairs."""
    return "\n  ".join(
        f'<path d="{l["d"]}" fill="{l["fill"]}" fill-rule="evenodd"/>'
        for l in LAYERS
    )


def symbol_flat(ink, ground):
    """Le symbole à une seule encre.

    La silhouette est remplie d'un aplat, puis les contours d'origine sont
    repeints dans la couleur du fond : les feuilles restent séparées les unes
    des autres, ce qu'un simple aplat de silhouette ne donnerait pas.
    """
    return (f'<path d="{SILHOUETTE}" fill="{ink}" fill-rule="evenodd"/>\n'
            f'  <path d="{CONTOURS}" fill="{ground}" fill-rule="evenodd"/>')


def wordmark(x, y, size, col_main, col_sub, anchor="middle"):
    return (
        f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
        f'font-family="Poppins, Segoe UI, Arial, sans-serif" font-weight="800" '
        f'font-size="{size}" letter-spacing="{-size * 0.014:.2f}" fill="{col_main}">'
        f'AgriWin Togo</text>\n'
        f'<text x="{x}" y="{y + size * 0.60:.1f}" text-anchor="{anchor}" '
        f'font-family="Playfair Display, Georgia, serif" font-style="italic" '
        f'font-weight="500" font-size="{size * 0.375:.1f}" '
        f'letter-spacing="{size * 0.010:.2f}" fill="{col_sub}">'
        f'Votre partenaire agricole !</text>'
    )


def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}" role="img" aria-label="{title}">\n'
            f'<title>{title}</title>\n{body}\n</svg>\n')


def write(name, content):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(content)


# 1 — Symbole seul ------------------------------------------------------
write("agriwin-icone.svg",
      svg(round(SW, 1), round(SH, 1), "  " + symbol_tonal(),
          "AgriWin Togo — symbole"))

# 2 — Logo principal, verrouillage vertical -----------------------------
write("agriwin-logo-principal.svg", svg(
    460, 600,
    f'<g transform="translate({(460 - SW) / 2:.1f} 6)">{symbol_tonal()}</g>\n'
    + wordmark(230, 528, 60, G900, G950),
    "AgriWin Togo — logo principal"))

# 3 — Logo horizontal ---------------------------------------------------
HS = 0.47                      # le symbole occupe 221 unités de haut
write("agriwin-logo-horizontal.svg", svg(
    740, 250,
    f'<g transform="translate(18 14) scale({HS})">{symbol_tonal()}</g>\n'
    + wordmark(182, 118, 54, G900, G950, anchor="start"),
    "AgriWin Togo — logo horizontal"))

# 4 — Monochrome, une seule encre --------------------------------------
write("agriwin-logo-mono.svg", svg(
    740, 250,
    f'<g transform="translate(18 14) scale({HS})">{symbol_flat(G950, WHITE)}</g>\n'
    + wordmark(182, 118, 54, G950, G950, anchor="start"),
    "AgriWin Togo — monochrome"))

# 5 — Version inversée --------------------------------------------------
write("agriwin-logo-inverse.svg", svg(
    740, 250,
    f'<rect width="740" height="250" fill="{G900}"/>\n'
    f'<g transform="translate(18 14) scale({HS})">{symbol_flat(WHITE, G900)}</g>\n'
    + wordmark(182, 118, 54, WHITE, CREAM, anchor="start"),
    "AgriWin Togo — version inversée"))

# 6 — Monogramme / avatar ----------------------------------------------
MS = 0.40                      # 188 unités de haut dans un carré de 240
write("agriwin-monogramme.svg", svg(
    240, 240,
    f'<rect width="240" height="240" rx="54" fill="{G900}"/>\n'
    f'<g transform="translate({(240 - SW * MS) / 2:.1f} 26) scale({MS})">'
    f'{symbol_flat(WHITE, G900)}</g>',
    "AgriWin Togo — monogramme"))

print("SVG générés :", sorted(f for f in os.listdir(OUT) if f.endswith(".svg")))
