# AgriWin Togo — site, identité de marque, design system et brand book

Projet monté pour Dina (Lomé, Togo). Tout est en français : le code, les
commentaires, les livrables et les échanges.

## Ce que contient ce dépôt

| Dossier | Rôle |
| --- | --- |
| `site/` | **Le site AgriWin Togo à déployer** — HTML/CSS/JS statique, sans étape de build. C'est la racine à servir (voir README.md pour l'hébergement). |
| `brand/logo/` | Le symbole vectorisé et les six variantes du logo, en SVG et PNG — **source de vérité des fichiers de logo** |
| `brand/logo/source/` | L'image du logo fournie par le client — source de vérité du *symbole* |
| `brand/logo/_previous/` | La version du logo rejetée par le client — témoin de la porte L2, ne pas supprimer |
| `brand/brandbook/assets/` | Copie de travail des six SVG de `brand/logo/`, lue par `build_brandbook.py` en chemins relatifs |
| `brand/brandbook/` | Le brand book A3 paysage : générateur Python, CSS, tokens |
| `brand/ds/project/` | Le contenu du design system publié comme artefact claude.ai |
| `brand/scripts/` | Génération, rendu et **vérificateurs** de tous les livrables de marque — *voir « État du dépôt » ci-dessous* |
| `brand/out/` | Livrables de marque produits : PDF, PPTX, et une archive des logos (copie figée de `brand/logo/` au moment de la livraison) |
| `brand/GATES.md`, `brand/GATES-LOGO.md` | Registres de portes de contrôle (voir plus bas) |
| `wrangler.toml`, `vercel.json`, `package.json` | Configuration de déploiement de `site/` |

Les six SVG du logo existent donc à trois endroits (`brand/logo/`,
`brand/brandbook/assets/`, `brand/out/logos/`) : ce n'est pas une dérive,
chacun sert un rôle différent (source, entrée du générateur, archive livrée).
Après toute modification de `brand/logo/`, les deux copies doivent être
resynchronisées à la main tant que `brand/scripts/` est absent — voir
« État du dépôt ».

`brand/brandbook/tokens.json` et `brand/ds/project/tokens.json` portent les
mêmes valeurs dans deux schémas différents (l'un plat pour le générateur du
brand book, l'autre en tableau pour l'artefact design system) : une
différence de forme entre les deux fichiers est normale, une différence de
valeur ne l'est pas.

`site/js/products.js` et `site/js/site-config.js` essaient `api/produits.json`
et `api/parametres.json` (pensés pour un futur panneau d'administration) et
retombent sur des valeurs statiques intégrées si ces fichiers n'existent pas
— ce qui est le cas actuellement. Le site fonctionne tel quel sans API ;
ajouter cette API est un projet à part, pas un correctif de structure.

## État du dépôt

Ce dépôt tel que livré ne contient **pas** de dossier `brand/scripts/`, alors
que la « Chaîne de génération » ci-dessous et les deux registres de portes
(`brand/GATES.md`, `brand/GATES-LOGO.md`) le référencent partout :
`trace_symbol.py`, `rasterize.py`, `build_tokens.py`, `build_ds_tokens.py`,
`build_ds_components.py`, `render_pdf.py`, `build_pptx.py`, et tous les
vérificateurs `check_*.py` / `check-*.mjs`. Les cases cochées de
`brand/GATES.md` et `brand/GATES-LOGO.md` sont les preuves qu'ils ont tourné
avec succès sur un autre poste (`cwd=/home/claude/agriwin` dans leurs
preuves) ; elles ne peuvent pas être rejouées depuis ce checkout tant que
`brand/scripts/` n'y est pas restauré. `brand/logo/`, `brand/brandbook/`,
`brand/ds/project/` et `brand/out/` contiennent donc les **derniers
livrables de marque générés**, pas une chaîne reproductible sur cette
machine. Restaurer `brand/scripts/` (depuis une sauvegarde ou en le
reconstruisant) est un préalable à toute nouvelle génération ou vérification
de porte — ça ne bloque pas le déploiement de `site/`, qui n'en dépend pas.

## Règles de travail sur ce projet

**Le symbole ne se redessine pas.** Il est vectorisé depuis
`brand/logo/source/agriwin-symbole-source.png` par `brand/scripts/trace_symbol.py`,
qui produit `brand/logo/symbole-trace.json` (six couches de valeur, tracées en
courbes de Bézier avec potrace, remplies de couleurs de la palette). Une
première version du projet avait redessiné un éventail de sept lames
droites : c'était un autre signe, et cela a été rejeté par le client. Toute
tentative de « redessiner proprement » le plant doit passer par les portes
L1 à L4.

**Les couleurs ne s'inventent pas.** Elles viennent du bloc `:root` du CSS du
site AgriWin Togo (`site/css/style.css`), repris dans
`brand/brandbook/tokens.json`. Un seul token a été ajouté — `gold-700`
(#9A6412) — parce que l'or du site (#C98A2B) ne donne que 2.94:1 sur blanc et
ne pouvait porter aucun texte. La porte G7 vérifie que les 32 tokens du site
sont repris à l'identique.

**Les chiffres se mesurent, ils ne se recopient pas.** Les ratios de contraste
du brand book sont recalculés à chaque génération. Les affirmations de forme
(« le symbole ressemble à l'original ») sont mesurées par recouvrement de
silhouette, pas jugées à l'œil.

## Chaîne de génération (identité de marque)

```bash
cd brand
python3 scripts/trace_symbol.py        # image source -> logo/symbole-trace.json
python3 logo/build_logo.py             # -> les 6 SVG de logo/
python3 scripts/rasterize.py logo      # -> logo/png/ (Chromium via Playwright)
python3 scripts/build_tokens.py        # CSS du site -> brandbook/tokens.json
python3 scripts/build_ds_tokens.py     # -> ds/project/tokens.json
python3 scripts/build_ds_components.py # -> ds/project/components/**
python3 brandbook/build_brandbook.py   # -> brandbook/brandbook.html (25 pages A3)
python3 scripts/render_pdf.py          # -> out/…-A3.pdf (Chromium, A3 paysage)
python3 scripts/build_pptx.py          # -> out/…-A3.pptx (formes natives)
```

Après toute modification du logo, **régénérer le PDF et le PPTX** : la porte L7
refuse un livrable plus ancien que les fichiers de logo. `scripts/build_tokens.py`
lit `site/css/style.css` : toute modification des couleurs se fait là, jamais
directement dans `brand/brandbook/tokens.json`.

## Portes de contrôle

Deux registres, dans `brand/`, au format de la compétence `unlazy` :

- `brand/GATES.md` — les livrables : variantes de logo valides, design system
  publié, PDF A3 ≥ 20 pages, PPTX A3 éditable, contrastes WCAG AA, tokens
  fidèles au site, fichiers remis, et un contrôle négatif qui prouve que les
  vérificateurs savent échouer.
- `brand/GATES-LOGO.md` — la fidélité du symbole : recouvrement ≥ 0,72 avec
  l'original (mesuré à 0,9176), progrès net sur la version rejetée, structure
  conforme tranche par tranche, chèvre au trait présente, feuilles séparées en
  monochrome, livrables régénérés, documentation à jour, contrôles négatifs.

Pour les exécuter (depuis `brand/`) :

```bash
node <chemin>/unlazy/scripts/gate-check.mjs --status GATES.md    # lecture seule
node <chemin>/unlazy/scripts/gate-check.mjs --approve GATES.md   # exécution
```

Sans la compétence `unlazy`, chaque vérificateur se lance seul :
`python3 scripts/check_symbol_shape.py`, `node scripts/check-logo-svg.mjs`, etc.
Chacun affiche `L1_OK`, `G4_OK`… en cas de succès et sort en erreur sinon.

## Dépendances

Génération de la marque (Python) : `pillow`, `numpy`, `scipy`, `potracer`,
`python-pptx`, `playwright`, `pypdfium2` (`brand/requirements.txt`). Chromium
via Playwright pour le rendu PDF et la rasterisation. Polices Poppins, Inter
et Playfair Display installées sur le système (sinon le rendu bascule sur des
substituts et le brand book change d'allure). Le site (`site/`) n'a aucune
dépendance : HTML/CSS/JS pur, aucun build.

## Déploiement du site

Voir [`README.md`](./README.md) — Cloudflare Pages est l'hébergement gratuit
recommandé (`site/` comme racine de build, pas de commande de build).
`vercel.json` reste fourni comme alternative portable.

## Artefacts publiés

Le design system est publié comme artefact claude.ai (type « Design System ») :
son URL est dans `brand/out/artifact-url.txt`. Les fichiers de
`brand/ds/project/` en sont la source ; les six logos y sont téléversés comme
assets, leurs identifiants figurent dans `brand/ds/project/design-system.json`.
Republier depuis un autre poste suppose d'avoir accès à cet artefact.

## Historique court

1. Design system et brand book construits depuis le site AgriWin Togo existant.
2. Audit WCAG de la palette : deux combinaisons du site échouaient, corrigées
   et documentées comme telles.
3. Le symbole redessiné a été rejeté par le client — il ne ressemblait pas au
   logo. Il est désormais vectorisé depuis l'image d'origine, et la fidélité
   est vérifiée par mesure.
4. Le code du site a été ajouté au dépôt (`site/`) puis le dépôt a été
   réorganisé pour ressembler à un dépôt de déploiement : `site/` déployable
   à la racine, `brand/` regroupant tout le travail d'identité, config de
   déploiement Cloudflare Pages / Vercel à la racine.

`brand/logo/_previous/` conserve la version rejetée : elle sert de témoin à
la porte L2, qui exige un progrès mesurable. Ne pas la supprimer.
