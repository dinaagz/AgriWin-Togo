# AgriWin Togo — identité de marque, design system et brand book

Projet monté pour Dina (Lomé, Togo). Tout est en français : le code, les
commentaires, les livrables et les échanges.

## Ce que contient ce dépôt

| Dossier | Rôle |
| --- | --- |
| `logo/` | Le symbole vectorisé et les six variantes du logo, en SVG et PNG |
| `logo/source/` | L'image du logo fournie par le client — **source de vérité du symbole** |
| `brandbook/` | Le brand book A3 paysage : générateur Python, CSS, tokens, assets |
| `ds/project/` | Le contenu du design system publié comme artefact claude.ai |
| `scripts/` | Génération, rendu et **vérificateurs** de tous les livrables |
| `out/` | Livrables produits (PDF, PPTX, archive des logos) |
| `GATES.md`, `GATES-LOGO.md` | Registres de portes de contrôle (voir plus bas) |

## Règles de travail sur ce projet

**Le symbole ne se redessine pas.** Il est vectorisé depuis
`logo/source/agriwin-symbole-source.png` par `scripts/trace_symbol.py`, qui
produit `logo/symbole-trace.json` (six couches de valeur, tracées en courbes de
Bézier avec potrace, remplies de couleurs de la palette). Une première version
du projet avait redessiné un éventail de sept lames droites : c'était un autre
signe, et cela a été rejeté par le client. Toute tentative de « redessiner
proprement » le plant doit passer par les portes L1 à L4.

**Les couleurs ne s'inventent pas.** Elles viennent du bloc `:root` du CSS du
site AgriWin Togo, repris dans `brandbook/tokens.json`. Un seul token a été
ajouté — `gold-700` (#9A6412) — parce que l'or du site (#C98A2B) ne donne que
2.94:1 sur blanc et ne pouvait porter aucun texte. La porte G7 vérifie que les
32 tokens du site sont repris à l'identique.

**Les chiffres se mesurent, ils ne se recopient pas.** Les ratios de contraste
du brand book sont recalculés à chaque génération. Les affirmations de forme
(« le symbole ressemble à l'original ») sont mesurées par recouvrement de
silhouette, pas jugées à l'œil.

## Chaîne de génération

```bash
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
refuse un livrable plus ancien que les fichiers de logo.

## Portes de contrôle

Deux registres, au format de la compétence `unlazy` :

- `GATES.md` — les livrables : variantes de logo valides, design system publié,
  PDF A3 ≥ 20 pages, PPTX A3 éditable, contrastes WCAG AA, tokens fidèles au
  site, fichiers remis, et un contrôle négatif qui prouve que les
  vérificateurs savent échouer.
- `GATES-LOGO.md` — la fidélité du symbole : recouvrement ≥ 0,72 avec
  l'original (mesuré à 0,9176), progrès net sur la version rejetée, structure
  conforme tranche par tranche, chèvre au trait présente, feuilles séparées en
  monochrome, livrables régénérés, documentation à jour, contrôles négatifs.

Pour les exécuter :

```bash
node <chemin>/unlazy/scripts/gate-check.mjs --status GATES.md    # lecture seule
node <chemin>/unlazy/scripts/gate-check.mjs --approve GATES.md   # exécution
```

Sans la compétence `unlazy`, chaque vérificateur se lance seul :
`python3 scripts/check_symbol_shape.py`, `node scripts/check-logo-svg.mjs`, etc.
Chacun affiche `L1_OK`, `G4_OK`… en cas de succès et sort en erreur sinon.

## Dépendances

Python : `pillow`, `numpy`, `scipy`, `potracer`, `python-pptx`, `playwright`,
`pypdfium2`. Chromium via Playwright pour le rendu PDF et la rasterisation.
Polices Poppins, Inter et Playfair Display installées sur le système (sinon le
rendu bascule sur des substituts et le brand book change d'allure).

## Artefacts publiés

Le design system est publié comme artefact claude.ai (type « Design System ») :
son URL est dans `out/artifact-url.txt`. Les fichiers de `ds/project/` en sont
la source ; les six logos y sont téléversés comme assets, leurs identifiants
figurent dans `ds/project/design-system.json`. Republier depuis un autre poste
suppose d'avoir accès à cet artefact.

## Historique court

1. Design system et brand book construits depuis le site AgriWin Togo existant.
2. Audit WCAG de la palette : deux combinaisons du site échouaient, corrigées
   et documentées comme telles.
3. Le symbole redessiné a été rejeté par le client — il ne ressemblait pas au
   logo. Il est désormais vectorisé depuis l'image d'origine, et la fidélité
   est vérifiée par mesure.

`logo/_previous/` conserve la version rejetée : elle sert de témoin à la porte
L2, qui exige un progrès mesurable. Ne pas la supprimer.
