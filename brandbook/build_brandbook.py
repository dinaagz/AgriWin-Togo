#!/usr/bin/env python3
"""AgriWin Togo — génération du brand book A3 paysage (HTML prêt pour impression).

Toutes les valeurs viennent de brandbook/tokens.json, lui-même extrait du CSS
du site. Aucune couleur n'est écrite en dur dans les pages.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(HERE, "tokens.json"), encoding="utf-8"))
V = {n: e for g in T["tokens"].values() for n, e in g.items()}
C = {n: e["value"] for n, e in V.items()}
ROLE = {n: e["role"] for n, e in V.items()}

pages = []


def page(title, num_label, body, tone="light"):
    pages.append({"title": title, "label": num_label, "body": body, "tone": tone})


def swatch(name, on_dark=False):
    val = C[name]
    ink = "#FFFFFF" if name in ("green-950", "green-900", "green-800", "green-700",
                                "green-600", "ink-900", "ink-700") else C["green-950"]
    return f"""<div class="sw">
      <div class="sw-chip" style="background:{val}">
        <span style="color:{ink}">{val.upper()}</span>
      </div>
      <div class="sw-meta"><strong>--{name}</strong><span>{ROLE[name]}</span></div>
    </div>"""


def kv_table(rows, head=("", "")):
    body = "".join(f"<tr><th>{a}</th><td>{b}</td></tr>" for a, b in rows)
    return f"<table class='kv'><thead><tr><th>{head[0]}</th><th>{head[1]}</th></tr></thead><tbody>{body}</tbody></table>"


LOGO_H = "assets/agriwin-logo-horizontal.svg"
LOGO_V = "assets/agriwin-logo-principal.svg"
LOGO_I = "assets/agriwin-icone.svg"
LOGO_M = "assets/agriwin-logo-mono.svg"
LOGO_R = "assets/agriwin-logo-inverse.svg"
LOGO_G = "assets/agriwin-monogramme.svg"

# ======================================================================
# 01 — Couverture
# ======================================================================
pages.append({"cover": True})

# ======================================================================
# 02 — Sommaire
# ======================================================================
SUMMARY = [
    ("01", "La marque en une page", "Ce qu'AgriWin Togo est, pour qui, et ce qui ne change pas."),
    ("02", "Mission, vision, promesse", "Les trois phrases qui fondent tout le reste."),
    ("03", "Valeurs", "Fiabilité, qualité, proximité, ouverture."),
    ("04", "Territoire et publics", "Kégué, le Togo, la sous-région, l'international."),
    ("05", "Ton de voix", "Comment la marque écrit, et ce qu'elle n'écrit pas."),
    ("06", "Le symbole", "D'où vient le signe et comment il a été mis au propre."),
    ("07", "Les six variantes", "Principal, horizontal, symbole, monochrome, inversé, monogramme."),
    ("08", "Zone de protection et tailles", "L'air autour du logo, et jusqu'où il descend."),
    ("09", "Usages interdits", "Huit façons d'abîmer la marque."),
    ("10", "Palette verte", "Neuf verts, du plus sombre au plus clair."),
    ("11", "Or et neutres", "L'accent de terre et les encres de lecture."),
    ("12", "Répartition et contrastes", "Où va chaque couleur, et ce que dit le contrôle WCAG."),
    ("13", "Les trois polices", "Poppins, Inter, Playfair Display."),
    ("14", "Échelle typographique", "Dix-sept styles, du display au micro."),
    ("15", "Règles de composition", "Ce qui se met en capitales, et ce qui ne s'y met pas."),
    ("16", "Iconographie", "Grille de 24, trait de 2, jonctions arrondies."),
    ("17", "Photographie", "Le terrain, la lumière, le voile vert."),
    ("18", "Formes, ombres, mouvement", "Quatre rayons, trois ombres, deux dixièmes de seconde."),
    ("19", "Composants d'interface", "Les quatorze briques du système."),
    ("20", "Papeterie", "Carte de visite, en-tête, signature d'e-mail."),
    ("21", "Supports de terrain", "Panneau de pépinière, étiquette de plant, tenue, véhicule."),
    ("22", "Digital et réseaux sociaux", "Avatar, couverture, format de publication."),
    ("23", "Gouvernance de la marque", "Qui décide, qui fournit les fichiers, qui contrôle."),
]
rows = "".join(
    f"<li><span class='sum-n'>{n}</span><span class='sum-t'>{t}</span>"
    f"<span class='sum-d'>{d}</span></li>" for n, t, d in SUMMARY
)
page("Sommaire", "—", f"<ol class='summary'>{rows}</ol>")

# ======================================================================
# 03 — La marque en une page
# ======================================================================
page("La marque en une page", "01", f"""
<div class="two">
  <div>
    <p class="lead">AgriWin Togo est une entreprise d'expertise et de prestation de services
    agricoles, de formation et d'écoulement de produits agricoles, spécialisée dans les
    plants tropicaux. Fondée en 2025, basée à Kégué.</p>
    <p>Elle est née d'un constat simple : beaucoup de porteurs de projets agricoles manquent
    en même temps d'un accompagnement technique fiable, de plants de qualité et de débouchés
    pour leurs récoltes. AgriWin Togo répond aux trois dans une seule structure.</p>
    {kv_table([
        ("Raison sociale", "AgriWin Togo"),
        ("Signature", "Votre partenaire agricole !"),
        ("Création", "2025"),
        ("Siège", "Kégué, Togo"),
        ("Dirigeant", "KEGNON Emmanuel, fondateur & CEO"),
        ("Métiers", "Conseil · Formation · Pépinière · Écoulement · Élevage"),
        ("Portée", "Togo, Afrique de l'Ouest, international"),
        ("Contact", "+228 96 63 82 00 · agriwintogo@gmail.com"),
        ("Horaires", "Lun–Sam : 8h – 18h"),
    ], ("Repère", "Valeur"))}
  </div>
  <div>
    <div class="quote-block">
      <p class="quote">« Nous voulons que chaque client, qu'il soit à Kégué ou à
      l'international, reçoive des plants de qualité et un accompagnement dans lequel il
      peut avoir une confiance totale. »</p>
      <p class="cite">KEGNON Emmanuel — Fondateur &amp; CEO</p>
    </div>
    <h3>Les six domaines</h3>
    <div class="chips">
      <span>Expertise &amp; conseil</span><span>Formation agricole</span>
      <span>Pépinière &amp; plants tropicaux</span><span>Prestations agricoles</span>
      <span>Écoulement de produits</span><span>Accompagnement en élevage</span>
    </div>
    <h3>Ce qui ne change jamais</h3>
    <ul class="ticks">
      <li>Le nom s'écrit <strong>AgriWin Togo</strong> — deux majuscules internes, un espace avant Togo.</li>
      <li>La signature porte son point d'exclamation et son espace insécable.</li>
      <li>Le vert domine, l'or ponctue.</li>
      <li>Ce qui est promis est vérifiable.</li>
    </ul>
  </div>
</div>""")

# ======================================================================
# 04 — Mission, vision, promesse
# ======================================================================
page("Mission, vision, promesse", "02", f"""
<div class="three">
  <div class="pillar">
    <span class="pillar-k">Mission</span>
    <p>Rendre l'expertise agricole, les plants de qualité et les débouchés commerciaux
    accessibles à tous les porteurs de projets, quelle que soit leur taille, au Togo et au-delà.</p>
  </div>
  <div class="pillar">
    <span class="pillar-k">Vision</span>
    <p>Devenir une référence ouest-africaine de l'accompagnement agricole intégré, reconnue
    pour la qualité de ses plants tropicaux et le sérieux de ses prestations.</p>
  </div>
  <div class="pillar pillar-gold">
    <span class="pillar-k">Promesse</span>
    <p class="promise">Votre partenaire agricole&nbsp;!</p>
    <p>Un partenaire, pas un fournisseur : quelqu'un qui reste après la livraison.</p>
  </div>
</div>
<div class="note-band">
  <h3>Comment la promesse se prouve</h3>
  <div class="proofs">
    <div><strong>Avant</strong><span>Diagnostic du terrain et devis détaillé : variétés,
    quantités, calendrier, prix.</span></div>
    <div><strong>Pendant</strong><span>Plants sélectionnés et contrôlés un par un avant de
    quitter la pépinière de Kégué.</span></div>
    <div><strong>Après</strong><span>Suivi technique de la reprise et mise en relation avec
    des acheteurs pour la récolte.</span></div>
  </div>
</div>""")

# ======================================================================
# 05 — Valeurs
# ======================================================================
VALUES = [
    ("Fiabilité", "Des engagements tenus, des délais respectés, un accompagnement suivi.",
     "On annonce une date de livraison et on la tient — ou on prévient avant."),
    ("Qualité", "Des plants et des prestations sélectionnés selon des standards exigeants.",
     "Un plant qui ne passe pas le contrôle ne quitte pas la pépinière."),
    ("Proximité", "Une équipe à l'écoute, disponible par téléphone et WhatsApp au quotidien.",
     "Un numéro unique, une réponse le jour même en semaine."),
    ("Ouverture", "Une clientèle locale et internationale, servie avec la même exigence.",
     "Le particulier de Kégué et l'ONG internationale ont le même interlocuteur."),
]
cards = "".join(
    f"<div class='value'><span class='value-n'>{i+1}</span><h3>{n}</h3>"
    f"<p>{d}</p><p class='value-proof'>{p}</p></div>"
    for i, (n, d, p) in enumerate(VALUES)
)
page("Valeurs", "03", f"""
<p class="lead">Quatre valeurs, dans cet ordre. Elles s'écrivent avec ces mots-là : chaque
valeur est suivie de la preuve qui la rend vérifiable, sans quoi elle n'est qu'un mot.</p>
<div class="values">{cards}</div>
<p class="foot-note">Ces quatre valeurs sont la liste complète. N'en ajoutez pas pour
remplir une grille, et ne les reformulez pas d'un support à l'autre.</p>""")

# ======================================================================
# 06 — Territoire et publics
# ======================================================================
page("Territoire et publics", "04", f"""
<div class="two">
  <div>
    <h3>Cinq publics, un même interlocuteur</h3>
    {kv_table([
        ("Particuliers", "Un jardin, un verger familial, quelques plants. Besoin : le bon plant et le bon conseil."),
        ("Petits producteurs", "Une parcelle à planter ou à replanter. Besoin : volume, prix, calendrier."),
        ("Entreprises", "Reboisement, aménagement, plantation industrielle. Besoin : prestation complète et facturation."),
        ("ONG et projets", "Programmes agricoles et environnementaux. Besoin : traçabilité, formation, reporting."),
        ("Investisseurs internationaux", "Projet agricole au Togo. Besoin : un partenaire local fiable sur place."),
    ], ("Public", "Ce qu'il vient chercher"))}
  </div>
  <div>
    <h3>Trois cercles</h3>
    <div class="rings">
      <div class="ring ring-1"><strong>Kégué</strong><span>La pépinière, l'atelier, le terrain.
      C'est d'ici que part chaque plant.</span></div>
      <div class="ring ring-2"><strong>Togo &amp; Afrique de l'Ouest</strong><span>Le marché
      principal : plants tropicaux recherchés, prestations, formation.</span></div>
      <div class="ring ring-3"><strong>International</strong><span>Investisseurs et ONG qui
      cherchent un partenaire agricole au Togo.</span></div>
    </div>
    <h3>Ce que cela change dans les supports</h3>
    <ul class="ticks">
      <li>Le français est la langue de référence de tous les supports.</li>
      <li>Les prix s'affichent en francs CFA ; une conversion n'apparaît que sur demande.</li>
      <li>Le numéro est toujours au format international : +228 96 63 82 00.</li>
      <li>WhatsApp est un canal de contact de premier rang, pas un canal de secours.</li>
    </ul>
  </div>
</div>""")

# ======================================================================
# 07 — Ton de voix
# ======================================================================
page("Ton de voix", "05", f"""
<p class="lead">Le ton d'AgriWin Togo est celui d'un technicien qui explique, pas d'un
commercial qui vend. Français, vouvoiement, phrases courtes, présent de l'indicatif.
Le client est « vous », l'entreprise est « nous ».</p>
<div class="do-dont">
  <div class="do">
    <h3>On écrit</h3>
    <ul>
      <li>« Chaque plant est contrôlé avant de quitter notre pépinière. »</li>
      <li>« Manguier greffé Kent, en sachet de 3 L — 3 500 F le plant. »</li>
      <li>« Nous vous rappelons sous 24 h ouvrées. »</li>
      <li>« Décrivez-nous votre besoin : surface, localisation, variétés. »</li>
      <li>« Demander un devis », « Voir le catalogue ».</li>
    </ul>
  </div>
  <div class="dont">
    <h3>On n'écrit pas</h3>
    <ul>
      <li>« Les meilleurs plants d'Afrique de l'Ouest » — invérifiable.</li>
      <li>« 100 % de clients satisfaits » — un chiffre sans source.</li>
      <li>« Nous mettons un point d'honneur à… » — du remplissage.</li>
      <li>« Cliquez ici » — un libellé qui ne dit pas ce qui se passe.</li>
      <li>« AGRIWIN TOGO » en capitales dans une phrase.</li>
    </ul>
  </div>
</div>
<div class="note-band">
  <h3>Sept règles d'écriture</h3>
  <div class="rules">
    <div><strong>Nom</strong><span>AgriWin Togo. Jamais Agriwin, AGRIWIN ni AgriWin-Togo.</span></div>
    <div><strong>Prix</strong><span>3 500 F — espace fine, symbole après. Jamais « 3500FCFA ».</span></div>
    <div><strong>Numéro</strong><span>+228 96 63 82 00, groupé par deux chiffres.</span></div>
    <div><strong>Horaires</strong><span>Lun–Sam : 8h – 18h, avec un tiret demi-cadratin.</span></div>
    <div><strong>Vocabulaire</strong><span>Les mots du métier : greffé, sachet de 3 L, taux de reprise.</span></div>
    <div><strong>Emoji</strong><span>Aucun dans les supports de marque ; un seul par publication sociale.</span></div>
    <div><strong>Ponctuation</strong><span>Espace insécable avant : ; ! ? et avant le symbole monétaire.</span></div>
  </div>
</div>""")

# ======================================================================
# 08 — Le symbole
# ======================================================================
page("Le symbole", "06", f"""
<div class="two two-wide-left">
  <div class="logo-stage">
    <img src="{LOGO_I}" alt="Symbole AgriWin Togo" style="height:150mm">
  </div>
  <div>
    <h3>Ce que le signe raconte</h3>
    <p>Un plant de sisal à six feuilles, et une chèvre à son pied. Les deux
    métiers d'AgriWin Togo — la culture et l'élevage — tiennent dans un seul
    signe, sans qu'aucun mot soit nécessaire.</p>
    <h3>Comment il a été mis au propre</h3>
    <p>Le signe n'a pas été redessiné : le logo d'origine a été vectorisé, puis
    ses valeurs ont été ramenées sur la palette de marque. Le plant, la chèvre
    et leurs proportions sont exactement ceux que l'entreprise utilise déjà.</p>
    {kv_table([
        ("Origine", "Logo fourni par AgriWin Togo, vectorisé en courbes de Bézier."),
        ("Structure", "Six feuilles : deux hampes centrales presque verticales, "
                      "deux latérales montantes, deux extérieures retombantes."),
        ("Proportions", "Rapport largeur / hauteur de 0,64 — le signe est plus haut que large."),
        ("Modelé", "Six valeurs de vert, de green-400 pour les nervures éclairées "
                   "à green-950 pour les contours."),
        ("Chèvre", "Dessin au trait à intérieur évidé, au pied de la feuille droite, "
                   "environ un cinquième de la hauteur du signe."),
        ("Une seule encre", "Silhouette pleine, contours d'origine repeints dans la "
                            "couleur du fond : les feuilles restent séparées."),
        ("Fichier", "SVG vectoriel, six couches superposées de la plus claire à la plus sombre."),
    ], ("Élément", "Règle"))}
    <p class="foot-note">Le symbole est un fichier, pas un dessin à reproduire. Ne le
    redessinez pas : prenez le SVG dans le groupe Logos du design system.</p>
  </div>
</div>""")

# 09 — Les six variantes
# ======================================================================
page("Les six variantes", "07", f"""
<div class="variants">
  <figure><div class="vbox"><img src="{LOGO_V}" alt="Logo principal"></div>
    <figcaption><strong>Principal — vertical</strong>Format carré ou portrait : affiche,
    couverture de document, publication sociale.</figcaption></figure>
  <figure><div class="vbox"><img src="{LOGO_H}" alt="Logo horizontal"></div>
    <figcaption><strong>Horizontal</strong>En-tête de site, papeterie, bandeau,
    signature d'e-mail.</figcaption></figure>
  <figure><div class="vbox"><img src="{LOGO_I}" alt="Symbole seul"></div>
    <figcaption><strong>Symbole seul</strong>Quand le nom est déjà écrit à côté :
    tampon, filigrane, motif.</figcaption></figure>
  <figure><div class="vbox"><img src="{LOGO_M}" alt="Monochrome"></div>
    <figcaption><strong>Monochrome</strong>Une seule encre, green-950 : gravure,
    sérigraphie une couleur, télécopie.</figcaption></figure>
  <figure><div class="vbox vbox-dark"><img src="{LOGO_R}" alt="Version inversée"></div>
    <figcaption><strong>Inversé</strong>Sur aplat green-900 ou photo foncée.
    Le fond fait partie du fichier.</figcaption></figure>
  <figure><div class="vbox"><img src="{LOGO_G}" alt="Monogramme"></div>
    <figcaption><strong>Monogramme</strong>Favicon, avatar de réseau social,
    tuile d'application.</figcaption></figure>
</div>""")

# ======================================================================
# 10 — Zone de protection et tailles
# ======================================================================
page("Zone de protection et tailles", "08", f"""
<div class="two">
  <div>
    <h3>La zone de protection</h3>
    <p>L'unité <strong>x</strong> est la hauteur de la hampe centrale divisée par quatre.
    Cette marge est libre sur les quatre côtés : aucun texte, aucun filet, aucune image,
    aucun bord de page n'y entre.</p>
    <div class="clearspace">
      <div class="cs-frame">
        <span class="cs-label cs-top">x</span>
        <span class="cs-label cs-left">x</span>
        <span class="cs-label cs-right">x</span>
        <span class="cs-label cs-bottom">x</span>
        <div class="cs-inner"><img src="{LOGO_H}" alt="Zone de protection"></div>
      </div>
    </div>
  </div>
  <div>
    <h3>Tailles minimales</h3>
    {kv_table([
        ("Horizontal — impression", "28 mm de large"),
        ("Horizontal — écran", "120 px de large"),
        ("Principal vertical — impression", "22 mm de large"),
        ("Principal vertical — écran", "96 px de large"),
        ("Symbole seul — écran", "32 px"),
        ("Monogramme — favicon", "16, 32 et 180 px"),
    ], ("Variante", "Taille minimale"))}
    <h3>En dessous de ces tailles</h3>
    <p>La chèvre et les nervures se referment et le signe devient une tache. Passez alors au
    monogramme, qui est dessiné pour cette échelle.</p>
    <div class="scale-row">
      <div><img src="{LOGO_H}" style="width:118px"><span>120 px — limite basse</span></div>
      <div><img src="{LOGO_G}" style="width:44px"><span>44 px — monogramme</span></div>
      <div><img src="{LOGO_G}" style="width:32px"><span>32 px — favicon</span></div>
    </div>
  </div>
</div>""")

# ======================================================================
# 11 — Usages interdits
# ======================================================================
DONTS = [
    ("Déformer", "scaleX(1.5)", "Le symbole garde son ratio. Redimensionnez toujours proportionnellement."),
    ("Incliner", "rotate(-14deg)", "Le logo est horizontal. Aucune rotation, même « dynamique »."),
    ("Recolorer", "hue-rotate(160deg)", "Les verts sont fixés. Pour changer d'encre, changez de fichier."),
    ("Ombrer", "drop-shadow(4px 6px 5px rgba(0,0,0,.55))", "Pas d'ombre portée, pas de relief, pas de contour."),
    ("Délaver", "opacity(.35)", "Le logo reste à pleine opacité. Pour un filigrane, utilisez le symbole seul."),
    ("Inverser les valeurs", "invert(1)", "Sur fond sombre, prenez la version inversée fournie."),
    ("Étouffer", "none", "La zone de protection est libre : rien ne s'en approche."),
    ("Poser sur du chargé", "none", "Sur une photo texturée, posez d'abord un aplat green-900."),
]
items = ""
for i, (t, filt, d) in enumerate(DONTS):
    if t == "Étouffer":
        inner = (f"<div class='dt-crowd'><img src='{LOGO_H}'>"
                 f"<span>PROMO<br>−20 %</span></div>")
    elif t == "Poser sur du chargé":
        inner = ("<div class='dt-busy'><img src='" + LOGO_H + "'></div>")
    else:
        style = f"filter:{filt}" if filt != "none" else ""
        if t == "Déformer":
            style = "transform:scaleX(1.55)"
        elif t == "Incliner":
            style = "transform:rotate(-14deg)"
        inner = f"<img src='{LOGO_H}' style='{style}'>"
    items += (f"<figure class='dont-card'><div class='dt-box'>{inner}"
              f"<span class='dt-cross'>✕</span></div>"
              f"<figcaption><strong>{t}</strong>{d}</figcaption></figure>")
page("Usages interdits", "09", f"""
<p class="lead">Huit façons d'abîmer la marque. Chacune s'est déjà produite quelque part :
la liste est là pour qu'elle ne se produise pas ici.</p>
<div class="donts">{items}</div>""")

# ======================================================================
# 12 — Palette verte
# ======================================================================
greens = "".join(swatch(n) for n in T["tokens"]["couleur-vert"])
page("Palette verte", "10", f"""
<p class="lead">Neuf verts, du plus sombre au plus clair. Le vert est la couleur de la
marque : sur une page, il occupe l'essentiel de la surface colorée.</p>
<div class="swatches">{greens}</div>
<div class="gradients">
  <div style="background:linear-gradient(135deg,{C['green-900']},{C['green-700']})">
    <span>green-900 → green-700 · bande de chiffres</span></div>
  <div style="background:linear-gradient(135deg,{C['green-900']},{C['green-600']})">
    <span>green-900 → green-600 · bandeau d'appel à l'action</span></div>
  <div style="background:linear-gradient(135deg,{C['green-700']},{C['green-500']})">
    <span>green-700 → green-500 · pictogramme de carte service</span></div>
</div>""")

# ======================================================================
# 13 — Or et neutres
# ======================================================================
golds = "".join(swatch(n) for n in T["tokens"]["couleur-or"])
inks = "".join(swatch(n) for n in T["tokens"]["couleur-neutre"])
wa = "".join(swatch(n) for n in T["tokens"]["couleur-service"])
page("Or et neutres", "11", f"""
<div class="two">
  <div>
    <h3>L'accent de terre</h3>
    <p>L'or vient de la terre et de la récolte. Il ponctue : sur une page, il ne dépasse pas
    un dixième de la surface colorée. Une seule action or par écran visible.</p>
    <div class="swatches sw-tight">{golds}</div>
    <p class="foot-note"><strong>gold-700 est un ajout de ce système.</strong> L'or du site
    (gold-600) ne donne que 2.94:1 sur blanc : il ne pouvait pas porter de texte. gold-700
    (#9A6412) atteint 4.99:1 et reprend tous les usages textuels de l'or.</p>
    <h3>Couleur de service</h3>
    <div class="swatches sw-tight">{wa}</div>
  </div>
  <div>
    <h3>Encres et fonds</h3>
    <div class="swatches sw-tight">{inks}</div>
    <p class="foot-note">ink-300 est déjà semi-transparent dans la source du site
    (#8A938890, soit 56 % d'opacité) : c'est volontaire, il sert aux séparateurs et au texte
    désactivé, jamais au texte lu.</p>
  </div>
</div>""")

# ======================================================================
# 14 — Répartition et contrastes
# ======================================================================
pairs = T["contrast_pairs"]
rows_ok = "".join(
    f"<tr><td>{p['name']}</td><td><span class='dot' style='background:{p['bg']};"
    f"color:{p['fg']}'>Aa</span></td><td><code>{p['fg_token']}</code></td>"
    f"<td><code>{p['bg_token']}</code></td><td class='num'>{p['ratio']}:1</td>"
    f"<td>{'AA' if p['usage'] == 'texte' else ('AA grand texte' if p['usage'] == 'grand-texte' else 'AA composant')}</td></tr>"
    for p in pairs
)
bad = "".join(
    f"<tr><td>{b['name']}</td><td class='num'>{b['ratio']}:1</td><td>{b['correctif']}</td></tr>"
    for b in T["contrast_interdits"]
)
page("Répartition et contrastes", "12", f"""
<div class="two two-wide-left">
  <div>
    <h3>Les {len(pairs)} paires validées</h3>
    <table class="contrast">
      <thead><tr><th>Association</th><th>Aperçu</th><th>Texte</th><th>Fond</th>
      <th>Ratio</th><th>Niveau</th></tr></thead>
      <tbody>{rows_ok}</tbody>
    </table>
  </div>
  <div>
    <h3>Répartition sur une page</h3>
    <div class="ratio-bar">
      <span style="flex:60;background:{C['white']};color:{C['green-950']};border:1px solid {C['border-soft']}">Blanc et fonds doux · 60 %</span>
      <span style="flex:30;background:{C['green-900']};color:{C['white']}">Verts de marque · 30 %</span>
      <span style="flex:10;background:{C['gold-500']};color:{C['green-950']}">Or · 10 %</span>
    </div>
    <h3>Deux combinaisons corrigées</h3>
    <table class="kv"><thead><tr><th>Combinaison du site</th><th>Mesure</th><th>Correctif</th></tr></thead>
    <tbody>{bad}</tbody></table>
    <p class="foot-note">Seuils appliqués : WCAG 2.1 AA — 4.5:1 pour le texte courant,
    3:1 à partir de 24 px, en gras à partir de 19 px, et pour tout élément d'interface
    porteur de sens. Chaque ratio de ce tableau est recalculé à la génération du document.</p>
  </div>
</div>""")

# ======================================================================
# 15 — Les trois polices
# ======================================================================
page("Les trois polices", "13", f"""
<div class="fonts">
  <div class="font-card">
    <div class="font-spec" style="font-family:Poppins;font-weight:800">Aa</div>
    <h3>Poppins</h3>
    <p class="font-role">Titres, surtitres, boutons, navigation, chiffres.</p>
    <p class="font-glyphs" style="font-family:Poppins;font-weight:600">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 àéèêçùôî ! ? &amp;</p>
    <p class="font-weights">Graisses utilisées : 500 · 600 · 700 · 800</p>
  </div>
  <div class="font-card">
    <div class="font-spec" style="font-family:Inter;font-weight:600">Aa</div>
    <h3>Inter</h3>
    <p class="font-role">Texte courant, formulaires, tableaux, légendes.</p>
    <p class="font-glyphs" style="font-family:Inter">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 àéèêçùôî ! ? &amp;</p>
    <p class="font-weights">Graisses utilisées : 400 · 500 · 600</p>
  </div>
  <div class="font-card">
    <div class="font-spec" style="font-family:'Playfair Display';font-style:italic;font-weight:600">Aa</div>
    <h3>Playfair Display <em>Italique</em></h3>
    <p class="font-role">Un à trois mots d'accent, et la signature de marque. Rien d'autre.</p>
    <p class="font-glyphs" style="font-family:'Playfair Display';font-style:italic">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 àéèêçùôî ! ? &amp;</p>
    <p class="font-weights">Graisses utilisées : 500 · 600 — italique uniquement</p>
  </div>
</div>
<div class="note-band">
  <h3>Substitutions</h3>
  <div class="rules">
    <div><strong>Poppins absente</strong><span>Segoe UI, puis Arial. Jamais une autre géométrique.</span></div>
    <div><strong>Inter absente</strong><span>Segoe UI, puis Arial.</span></div>
    <div><strong>Playfair absente</strong><span>Georgia italique. Sans serif disponible, supprimez l'accent plutôt que de le composer en sans.</span></div>
    <div><strong>Bureautique</strong><span>Word et PowerPoint : installez les trois polices. À défaut, Calibri remplace Inter et Poppins.</span></div>
  </div>
</div>""")

# ======================================================================
# 16 — Échelle typographique
# ======================================================================
FAM = {"Poppins": "Poppins", "Inter": "Inter",
       "Playfair Display Italic": "'Playfair Display'"}
rows_t = ""
for s in T["echelle_typographique"]:
    fam = FAM[s["police"]]
    ital = "font-style:italic;" if "Italic" in s["police"] else ""
    size = s["taille"]
    px = size.split(",")[-1].replace(")", "").strip() if "clamp" in size else size
    rows_t += (
        f"<tr><td class='ts-name'>{s['nom']}</td>"
        f"<td class='ts-sample' style=\"font-family:{fam};{ital}font-weight:{s['graisse']};"
        f"font-size:min({px}, 44px);line-height:{s['interligne']}\">AgriWin Togo</td>"
        f"<td><code>{size}</code></td><td class='num'>{s['graisse']}</td>"
        f"<td class='num'>{s['interligne']}</td><td>{s['police']}</td>"
        f"<td class='ts-use'>{s['usage']}</td></tr>"
    )
page("Échelle typographique", "14", f"""
<p class="lead">Dix styles nommés couvrent tous les supports. Les tailles de titre sont
fluides : la valeur indiquée est le maximum, la borne basse s'applique sur mobile.</p>
<table class="typescale">
  <thead><tr><th>Style</th><th>Aperçu</th><th>Taille</th><th>Graisse</th>
  <th>Interligne</th><th>Police</th><th>Usage</th></tr></thead>
  <tbody>{rows_t}</tbody>
</table>""")

# ======================================================================
# 17 — Règles de composition
# ======================================================================
page("Règles de composition", "15", f"""
<div class="two">
  <div>
    <h3>Longueur et rythme</h3>
    <ul class="ticks">
      <li>Le texte courant reste autour de <strong>65 caractères</strong> par ligne.</li>
      <li>Interligne 1,6 pour le texte, 1,2 pour les titres, 1,08 pour le display.</li>
      <li>Un seul niveau de titre par bloc : un h2 par section, des h3 ensuite.</li>
      <li>Le chapô tient sous 220 caractères ; au-delà, c'est un paragraphe.</li>
    </ul>
    <h3>Capitales et interlettrage</h3>
    <ul class="ticks">
      <li>Seuls les surtitres sont en capitales, avec 0,08 em d'interlettrage.</li>
      <li>Le nom de la marque ne se met jamais en capitales dans une phrase.</li>
      <li>Les titres en display prennent −0,02 em pour resserrer les blancs.</li>
      <li>Aucun texte courant en capitales : la lecture chute.</li>
    </ul>
    <h3>L'accent Playfair</h3>
    <p>Un à trois mots dans un titre de section, en italique gold-700. Un seul par page.
    Un paragraphe entier en Playfair est une faute.</p>
  </div>
  <div>
    <h3>Trois compositions types</h3>
    <div class="spec-demo">
      <span class="sd-eyebrow">CE QUE NOUS FAISONS</span>
      <h2 class="sd-h2">Une expertise agricole complète, <em>sur le terrain</em></h2>
      <p class="sd-lead">Conseil, formation, pépinière et écoulement des récoltes : une seule
      structure pour les quatre besoins d'un projet agricole.</p>
    </div>
    <div class="spec-demo spec-dark">
      <h2 class="sd-h2" style="color:#fff">Un projet agricole en tête ?</h2>
      <p class="sd-lead" style="color:rgba(255,255,255,.9)">Décrivez-nous votre besoin :
      nos experts vous répondent avec un devis clair.</p>
    </div>
    <div class="spec-demo">
      <h3 class="sd-h3">Pépinière &amp; plants tropicaux</h3>
      <p class="sd-body">Manguiers, avocatiers, cocotiers, agrumes, teck, moringa — chaque
      plant est contrôlé avant de quitter la pépinière de Kégué.</p>
    </div>
  </div>
</div>""")

# ======================================================================
# 18 — Iconographie
# ======================================================================
ICON_PATHS = {
    "leaf": ["M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10z",
             "M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"],
    "school": ["M22 10 12 5 2 10l10 5 10-5Z", "M6 12v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"],
    "users": ["M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2",
              "M23 21v-2a4 4 0 0 0-3-3.87", "M16 3.13a4 4 0 0 1 0 7.75"],
    "shield": ["M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"],
    "target": ["M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Z", "M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10Z"],
    "arrow": ["M5 12h14", "M12 5l7 7-7 7"],
    "phone": ["M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"],
    "mail": ["M3 5h18v14H3z", "M21 6 12 13 3 6"],
    "pin": ["M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z", "M12 13a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"],
    "calendar": ["M3 4h18v18H3z", "M16 2v4", "M8 2v4", "M3 10h18"],
    "check": ["M20 6 9 17l-5-5"],
    "search": ["M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14Z", "M20 20l-4-4"],
}
ICON_USE = {
    "leaf": "Conseil, pépinière, nature", "school": "Formation",
    "users": "Élevage, équipe, proximité", "shield": "Fiabilité, garantie",
    "target": "Qualité, mission", "arrow": "Lien, progression",
    "phone": "Téléphone, WhatsApp", "mail": "E-mail",
    "pin": "Adresse, localisation", "calendar": "Horaires, date",
    "check": "Confirmation, validation", "search": "Recherche du catalogue",
}


def icon_svg(name, size=30, color="currentColor"):
    paths = "".join(f'<path d="{d}"/>' for d in ICON_PATHS[name])
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
            f'stroke="{color}" stroke-width="2" stroke-linecap="round" '
            f'stroke-linejoin="round">{paths}</svg>')


grid = "".join(
    f"<div class='ic'><div class='ic-box'>{icon_svg(n)}</div>"
    f"<strong>{n}</strong><span>{ICON_USE[n]}</span></div>"
    for n in ICON_PATHS
)
page("Iconographie", "16", f"""
<div class="two two-wide-left">
  <div>
    <div class="icongrid">{grid}</div>
  </div>
  <div>
    <h3>La règle de tracé</h3>
    {kv_table([
        ("Grille", "24 × 24, marge optique de 2 unités"),
        ("Trait", "2 unités, jamais de remplissage"),
        ("Extrémités", "Arrondies (round cap et round join)"),
        ("Couleur", "Héritée du texte voisin (currentColor)"),
        ("Angles", "Rayon minimal de 2 unités ; pas d'angle vif"),
    ], ("Paramètre", "Valeur"))}
    <h3>Deux traitements</h3>
    <div class="icon-treat">
      <div><div class="aw-icon-demo">{icon_svg('leaf', 28, '#fff')}</div>
      <span><strong>En carte service</strong>Blanc dans un carré de 58 px, rayon radius-md,
      dégradé green-700 → green-500.</span></div>
      <div><div class="aw-icon-plain">{icon_svg('phone', 26, C['green-700'])}</div>
      <span><strong>Partout ailleurs</strong>Au trait, de la couleur du texte à côté duquel
      il se place.</span></div>
    </div>
    <p class="foot-note">Ces douze tracés sont ceux du site AgriWin Togo. Pour un besoin
    nouveau, dessinez dans la même grille plutôt que d'importer un autre jeu d'icônes.
    Un pictogramme ne remplace jamais un libellé : il l'accompagne.</p>
  </div>
</div>""")

# ======================================================================
# 19 — Photographie
# ======================================================================
page("Photographie", "17", f"""
<div class="two">
  <div>
    <h3>Ce que l'on photographie</h3>
    <ul class="ticks">
      <li>Des mains au travail : semis, repiquage, greffe, mise en terre.</li>
      <li>Des plateaux de jeunes plants, en rangs, dans la pépinière.</li>
      <li>Des gens réels de l'équipe et des clients — pas des poses.</li>
      <li>Le marché et la distribution : la récolte qui trouve son débouché.</li>
      <li>Le terrain avant et après : la preuve d'une prestation.</li>
    </ul>
    <h3>Comment on la prend</h3>
    {kv_table([
        ("Lumière", "Naturelle, tôt le matin ou en fin d'après-midi. Pas de flash direct."),
        ("Hauteur", "À hauteur d'homme, ou à hauteur de plant pour la pépinière."),
        ("Profondeur", "Un sujet net, un arrière-plan doux — jamais tout net."),
        ("Verts", "Les verts de l'image doivent pouvoir voisiner green-700 sans jurer."),
        ("Format", "3:2 pour les bandeaux, 4:3 pour les cartes, 1:1 pour le social."),
    ], ("Paramètre", "Règle"))}
  </div>
  <div>
    <h3>Le voile vert</h3>
    <p>Sur toute photo qui porte du texte, posez ce dégradé du haut vers le bas. C'est lui
    qui garantit la lisibilité du titre blanc, quelle que soit l'image.</p>
    <div class="veil-demo">
      <div class="veil-img"></div>
      <div class="veil-grad"></div>
      <div class="veil-text">
        <span class="veil-badge">Fondée en 2025 — Kégué, Togo</span>
        <h2>Chaque plant compte.</h2>
        <p>AgriWin Togo accompagne particuliers, entreprises et ONG.</p>
      </div>
    </div>
    <p class="foot-note"><code>linear-gradient(180deg, rgba(15,61,23,.55), rgba(15,61,23,.82))</code>
    — soit green-950 à 55 % puis 82 %.</p>
    <h3>Images de substitution</h3>
    <p>Tant que les photos de la pépinière et de l'équipe ne sont pas disponibles, les
    images d'ambiance portent une mention explicite sous le bloc. Retirez la mention en
    même temps que l'image.</p>
  </div>
</div>""")

# ======================================================================
# 20 — Formes, ombres, mouvement
# ======================================================================
radii = "".join(
    f"<div class='shape'><div class='shape-box' style='border-radius:{C[n]}'></div>"
    f"<strong>--{n}</strong><span>{C[n]}</span><span class='shape-use'>{ROLE[n]}</span></div>"
    for n in T["tokens"]["rayon"]
)
shadows = "".join(
    f"<div class='shape'><div class='shape-box shape-white' style='box-shadow:{C[n]}'></div>"
    f"<strong>--{n}</strong><span class='shape-use'>{ROLE[n]}</span></div>"
    for n in T["tokens"]["ombre"]
)
spacing_rows = "".join(
    f"<div class='sp'><span class='sp-bar' style='width:{s}px'></span>"
    f"<span class='sp-val'>{s} px</span></div>" for s in T["espacement"]
)
page("Formes, ombres, mouvement", "18", f"""
<div class="three three-uneven">
  <div>
    <h3>Rayons</h3>
    <div class="shapes">{radii}</div>
    <p class="foot-note">Quatre rayons, pas un de plus. Un rayon choisi hors de cette liste
    se voit immédiatement dans une grille de cartes.</p>
  </div>
  <div>
    <h3>Ombres</h3>
    <div class="shapes">{shadows}</div>
    <p class="foot-note">Les trois ombres sont teintées de green-950 (15, 61, 23) : une ombre
    grise neutre fait sale sur les fonds verts.</p>
  </div>
  <div>
    <h3>Espacement</h3>
    <div class="spacing">{spacing_rows}</div>
    <h3>Mouvement</h3>
    {kv_table([
        ("Durée", "0,15 s pour un bouton, 0,2 s pour une carte, 0,4 s pour une image"),
        ("Courbe", "ease — pas de rebond, pas d'élastique"),
        ("Carte au survol", "Monte de 5 px et prend shadow-md"),
        ("Bouton au clic", "Se comprime à 97 %"),
        ("Flèche de lien", "Avance de 4 px"),
    ], ("Paramètre", "Valeur"))}
  </div>
</div>""")

# ======================================================================
# 21 — Composants d'interface
# ======================================================================
COMPONENTS = [
    ("Button", "Six variantes, deux tailles. Une seule action or par écran."),
    ("Eyebrow", "Surtitre en pastille green-100, texte green-900."),
    ("SectionHead", "Surtitre, titre, mot d'accent Playfair, chapô."),
    ("Card", "Carte de base : bordure border-soft, rayon radius-lg."),
    ("ServiceCard", "Pictogramme en dégradé, titre, promesse, lien."),
    ("ValueCard", "Valeur de marque, centrée sur green-50."),
    ("ProductCard", "Entrée de catalogue : visuel, badge, prix, deux actions."),
    ("StatBand", "Chiffres clés en gold-500 sur dégradé vert."),
    ("CtaBand", "Bandeau de fin de page, un seul par page."),
    ("Field", "Libellé au-dessus, aide ou erreur en dessous."),
    ("FilterChip", "Filtre du catalogue, état porté par aria-pressed."),
    ("ContactCard", "Coordonnées sur aplat green-950."),
    ("StepList", "Étapes numérotées — uniquement pour une vraie séquence."),
    ("Brand", "Symbole, nom, signature, sur fond clair ou sombre."),
]
comp_rows = "".join(
    f"<div class='comp'><strong>{n}</strong><span>{d}</span></div>" for n, d in COMPONENTS
)
page("Composants d'interface", "19", f"""
<p class="lead">Quatorze composants couvrent l'ensemble du site AgriWin Togo. Chacun est
documenté dans le design system, avec ses propriétés, ses états et un aperçu vivant.</p>
<div class="comps">{comp_rows}</div>
<div class="demo-strip">
  <div class="d-btn d-primary">Demander un devis</div>
  <div class="d-btn d-green">Voir le catalogue</div>
  <div class="d-btn d-outline">En savoir plus</div>
  <div class="d-eyebrow">NOTRE ENGAGEMENT</div>
  <div class="d-tag">Pépinière</div>
  <div class="d-chip d-chip-on">Fruitiers</div>
  <div class="d-chip">Forestiers</div>
  <div class="d-badge">NOUVEAU</div>
</div>
<p class="foot-note">Les composants vivent dans le design system, pas dans ce document :
c'est là qu'ils sont à jour, avec leur code et leurs règles d'usage.</p>""")

# ======================================================================
# 22 — Papeterie
# ======================================================================
page("Papeterie", "20", f"""
<div class="stationery">
  <figure>
    <div class="biz">
      <div class="biz-front">
        <img src="{LOGO_V}" style="height:26mm">
      </div>
      <div class="biz-back">
        <div class="biz-name">KEGNON Emmanuel</div>
        <div class="biz-role">Fondateur &amp; CEO</div>
        <div class="biz-lines">
          <span>+228 96 63 82 00</span>
          <span>agriwintogo@gmail.com</span>
          <span>Kégué, Togo</span>
        </div>
        <img src="{LOGO_H}" class="biz-logo">
      </div>
    </div>
    <figcaption><strong>Carte de visite — 85 × 55 mm</strong>Recto : logo vertical centré sur
    blanc, ou en inversé sur green-900. Verso : nom en Poppins 700, fonction en ink-500,
    coordonnées en Inter 8 pt.</figcaption>
  </figure>
  <figure>
    <div class="letter">
      <img src="{LOGO_H}" class="letter-logo">
      <div class="letter-lines">
        <span class="l-long"></span><span class="l-long"></span><span class="l-mid"></span>
        <span class="l-long"></span><span class="l-long"></span><span class="l-short"></span>
        <span class="l-long"></span><span class="l-mid"></span>
      </div>
      <div class="letter-foot">AgriWin Togo · Kégué, Togo · +228 96 63 82 00 · agriwintogo@gmail.com</div>
    </div>
    <figcaption><strong>En-tête A4</strong>Logo horizontal en haut à gauche, à 18 mm des
    bords. Filet gold-500 de 2 mm au pied. Coordonnées en caption ink-500, centrées.</figcaption>
  </figure>
  <figure>
    <div class="sig">
      <img src="{LOGO_H}">
      <div>
        <strong>KEGNON Emmanuel</strong>
        <em>Fondateur &amp; CEO — AgriWin Togo</em>
        <span>+228 96 63 82 00 · agriwintogo@gmail.com</span>
        <span class="sig-tag">Votre partenaire agricole&nbsp;!</span>
      </div>
    </div>
    <figcaption><strong>Signature d'e-mail</strong>Logo à 120 px de large, nom en Poppins 600,
    fonction en Playfair italique, coordonnées en 12 px ink-700. Pas d'image de fond, pas de
    citation ajoutée.</figcaption>
  </figure>
</div>""")

# ======================================================================
# 23 — Supports de terrain
# ======================================================================
page("Supports de terrain", "21", f"""
<div class="field-kit">
  <figure>
    <div class="signboard">
      <img src="{LOGO_R}" style="width:100%">
      <div class="sb-body">
        <strong>Pépinière de Kégué</strong>
        <span>Plants tropicaux · Conseil · Formation</span>
        <span class="sb-tel">+228 96 63 82 00</span>
      </div>
    </div>
    <figcaption><strong>Panneau de pépinière</strong>Version inversée en haut, aplat
    green-900 sur toute la surface, numéro en gold-400 lisible à dix mètres. Hauteur de
    caractère minimale du numéro : un vingtième de la largeur du panneau.</figcaption>
  </figure>
  <figure>
    <div class="plant-tag">
      <img src="{LOGO_I}" style="height:14mm">
      <strong>Manguier greffé</strong>
      <span>Variété Kent · Sachet 3 L</span>
      <span class="pt-lot">Lot 2026-04 · Kégué</span>
    </div>
    <figcaption><strong>Étiquette de plant</strong>45 × 90 mm, symbole seul en haut, espèce
    en Poppins 600, variété et contenant en caption. Le numéro de lot rend le plant
    traçable : il est obligatoire.</figcaption>
  </figure>
  <figure>
    <div class="shirt">
      <div class="shirt-body"><span class="shirt-collar"></span><img src="{LOGO_R}" style="width:56%"></div>
    </div>
    <figcaption><strong>Tenue d'équipe</strong>Polo vert green-900, logo inversé brodé à
    gauche de la poitrine, 70 mm de large. Dos : symbole seul en blanc, 180 mm. Pas de
    slogan supplémentaire.</figcaption>
  </figure>
  <figure>
    <div class="van">
      <div class="van-body">
        <img src="{LOGO_H}" style="width:58%">
        <span class="van-tel">+228 96 63 82 00 · agriwintogo@gmail.com</span>
      </div>
      <div class="van-wheel w1"></div><div class="van-wheel w2"></div>
    </div>
    <figcaption><strong>Véhicule</strong>Portière blanche : logo horizontal, coordonnées en
    dessous. Sur une carrosserie verte, version inversée. La zone de protection s'applique
    aussi aux poignées et aux joints.</figcaption>
  </figure>
</div>""")

# ======================================================================
# 24 — Digital et réseaux sociaux
# ======================================================================
page("Digital et réseaux sociaux", "22", f"""
<div class="two two-wide-left">
  <div>
    <div class="social">
      <figure>
        <div class="post">
          <div class="post-media">
            <span class="post-eyebrow">CATALOGUE</span>
            <h3>Manguier greffé Kent</h3>
            <span class="post-price">3 500 F <em>/ plant</em></span>
          </div>
          <div class="post-foot"><img src="{LOGO_G}" style="height:9mm">
          <span>@agriwintogo</span></div>
        </div>
        <figcaption><strong>Publication 1:1</strong>Aplat green-900, surtitre en pastille,
        prix en gold-500. Monogramme et identifiant en pied.</figcaption>
      </figure>
      <figure>
        <div class="cover-fb">
          <img src="{LOGO_R}" style="width:100%;height:100%;object-fit:cover">
        </div>
        <figcaption><strong>Couverture Facebook</strong>1640 × 624 px. Version inversée
        centrée, zone de protection doublée sur les bords, rien dans le quart inférieur
        gauche (photo de profil).</figcaption>
      </figure>
      <figure>
        <div class="avatars">
          <img src="{LOGO_G}" style="width:22mm;border-radius:50%">
          <img src="{LOGO_G}" style="width:14mm;border-radius:50%">
          <img src="{LOGO_G}" style="width:9mm;border-radius:50%">
        </div>
        <figcaption><strong>Avatar</strong>Monogramme uniquement. Recadré en cercle par les
        plateformes : le symbole est centré pour rester entier.</figcaption>
      </figure>
    </div>
  </div>
  <div>
    <h3>Formats</h3>
    {kv_table([
        ("Avatar", "512 × 512 px — monogramme"),
        ("Couverture Facebook", "1640 × 624 px — version inversée"),
        ("Publication carrée", "1080 × 1080 px"),
        ("Story / TikTok", "1080 × 1920 px"),
        ("Bannière de site", "1920 × 1280 px, voile vert obligatoire"),
        ("Favicon", "16, 32 et 180 px — monogramme"),
    ], ("Support", "Dimensions"))}
    <h3>Comptes officiels</h3>
    <ul class="ticks">
      <li>Facebook : facebook.com/agriwintogo</li>
      <li>TikTok : @agriwintogo</li>
      <li>WhatsApp : wa.me/22896638200</li>
      <li>Site : agriwintogo.com</li>
    </ul>
    <h3>Règles de publication</h3>
    <ul class="ticks">
      <li>Une photo de terrain vaut mieux qu'une image de banque.</li>
      <li>Un prix affiché est un prix tenu : il est daté dans la légende.</li>
      <li>Un emoji au maximum par publication.</li>
      <li>Le numéro apparaît en clair, pas seulement en lien.</li>
    </ul>
  </div>
</div>""")

# ======================================================================
# 25 — Gouvernance
# ======================================================================
page("Gouvernance de la marque", "23", f"""
<div class="two">
  <div>
    <h3>Où se trouvent les fichiers</h3>
    <p>La source de vérité est le <strong>design system AgriWin Togo</strong>, publié comme
    artefact sur claude.ai. Il contient les {sum(len(g) for g in T['tokens'].values())} tokens,
    les 14 composants avec leurs aperçus vivants, et les six fichiers de logo en SVG.</p>
    <p>Ce brand book est une photographie de ce système à un instant donné. En cas de
    divergence, <strong>le design system fait foi</strong>.</p>
    {kv_table([
        ("Tokens", "tokens.json — couleurs, typographie, espacement, rayons, ombres"),
        ("Composants", "14 fiches, chacune avec propriétés, états et aperçu"),
        ("Logos", "6 fichiers SVG dans le groupe d'assets Logos"),
        ("Règles d'écriture", "README du design system"),
    ], ("Élément", "Emplacement"))}
  </div>
  <div>
    <h3>Qui décide quoi</h3>
    {kv_table([
        ("Nom, signature, valeurs", "Direction — aucune modification sans décision formelle"),
        ("Logo et déclinaisons", "Direction, sur proposition du responsable communication"),
        ("Palette et typographie", "Responsable communication, dans les limites de ce document"),
        ("Nouveau composant", "Responsable communication + intégrateur, ajouté au design system"),
        ("Supports courants", "Toute personne, en appliquant ce document"),
    ], ("Décision", "Qui"))}
    <h3>Avant de diffuser un support</h3>
    <ul class="ticks">
      <li>Le logo vient-il d'un fichier du design system, et non d'une capture d'écran ?</li>
      <li>La zone de protection est-elle respectée ?</li>
      <li>Les trois polices sont-elles utilisées dans leurs rôles ?</li>
      <li>Le texte atteint-il 4.5:1 sur son fond ?</li>
      <li>L'or reste-t-il sous un dixième de la surface colorée ?</li>
      <li>Chaque promesse chiffrée est-elle vérifiable ?</li>
    </ul>
    <div class="contact-final">
      <strong>AgriWin Togo</strong>
      <span>Kégué, Togo · +228 96 63 82 00 · agriwintogo@gmail.com</span>
      <span>Lun–Sam : 8h – 18h · agriwintogo.com</span>
    </div>
  </div>
</div>""")

# ======================================================================
# Rendu
# ======================================================================
CSS = open(os.path.join(HERE, "brandbook.css"), encoding="utf-8").read()
CSS = CSS.replace("/*TOKENS*/", "\n".join(
    f"    --{n}: {v};" for n, v in C.items()))

html = [
    "<!DOCTYPE html><html lang='fr'><head><meta charset='utf-8'>",
    "<title>AgriWin Togo — Brand Book</title>",
    f"<style>{CSS}</style></head><body>",
]

total = len(pages)
for i, p in enumerate(pages, 1):
    if p.get("cover"):
        html.append(f"""<section class="page cover">
  <div class="cover-art">
    <div class="cb cb1"></div><div class="cb cb2"></div>
    <div class="cb cb3"></div><div class="cb cb4"></div>
    <img src="{LOGO_I}" class="cover-symbol" alt="">
  </div>
  <div class="cover-text">
    <span class="cover-kicker">Charte de marque · Édition 1.0 · 2026</span>
    <h1>AgriWin<br>Togo</h1>
    <p class="cover-sign">Votre partenaire agricole&nbsp;!</p>
    <p class="cover-sub">Identité, design system et règles d'application.<br>
    Kégué, Togo — expertise agricole, plants tropicaux, formation.</p>
  </div>
  <div class="cover-foot"><span>AgriWin Togo</span><span>agriwintogo.com · +228 96 63 82 00</span></div>
</section>""")
        continue
    html.append(f"""<section class="page">
  <header class="ph">
    <img src="{LOGO_H}" alt="">
    <div class="ph-title"><span>{p['label']}</span><h2>{p['title']}</h2></div>
    <span class="ph-num">{i:02d} / {total:02d}</span>
  </header>
  <div class="pb">{p['body']}</div>
  <footer class="pf"><span>AgriWin Togo — Charte de marque 1.0</span>
  <span>Votre partenaire agricole&nbsp;!</span></footer>
</section>""")

html.append("</body></html>")
out = os.path.join(HERE, "brandbook.html")
open(out, "w", encoding="utf-8").write("\n".join(html))
print(f"{out} : {total} pages")
