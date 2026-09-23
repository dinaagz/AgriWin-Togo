# AgriWin Togo

Site web et identité de marque d'**AgriWin Togo** (Kégué, Togo) : conseil
agricole, formation, plants tropicaux, écoulement de produits et
accompagnement en élevage. Tout le contenu est en français.

**Site en ligne :** https://agriwin-togo.dinaagouze19.workers.dev/

## Structure du dépôt

| Dossier | Contenu |
| --- | --- |
| `site/` | **Le site à déployer** — HTML/CSS/JS statique, aucune étape de build. C'est la racine à servir. |
| `brand/` | Identité de marque : logo vectorisé, brand book A3, design system, livrables. Référence, pas déployé. |
| `design-system/` | Fiche de référence rapide (`MASTER.md`) générée par la skill Claude « design-system » ; corrigée pour reprendre les vraies couleurs/typographies AgriWin. Le design system publié qui fait foi reste `brand/ds/project/`. |
| `CLAUDE.md` | Règles de travail et documentation détaillée du projet. |
| `wrangler.toml`, `vercel.json`, `package.json` | Configuration de déploiement (voir ci-dessous). |

`site/` ne dépend d'aucune API : `js/products.js` et `js/site-config.js`
essaient `api/produits.json` et `api/parametres.json` (pour un futur panneau
d'administration), et retombent proprement sur des valeurs statiques intégrées
si ces fichiers n'existent pas — ce qui est le cas ici. Le site fonctionne
donc tel quel sur un hébergeur purement statique.

## Déployer — Cloudflare Pages (recommandé, gratuit)

Choisi parce que c'est gratuit sans carte bancaire, sans limite de bande
passante, sans restriction d'usage commercial, avec domaine `.pages.dev` et
HTTPS inclus, déploiement automatique à chaque `git push`, et une voie de
migration native vers du dynamique (Cloudflare Pages Functions / Workers)
le jour où `api/produits.json` devra devenir une vraie API — sans changer
d'hébergeur.

**Par le tableau de bord** (le plus simple) :
1. [dash.cloudflare.com](https://dash.cloudflare.com) → Workers & Pages → *Create* → *Pages* → *Connect to Git* → ce dépôt.
2. Dans *Build settings*, renseigner exactement :
   - Framework preset : **None**
   - Build command : *(laisser vide)*
   - Build output directory : **site**
   - Root directory : `/`
3. Chaque push sur `main` redéploie automatiquement.

> **Si le build échoue** : Cloudflare Pages détecte un `package.json` à la
> racine et lance `npm ci` puis, selon le preset choisi, `npm run build` —
> deux échecs classiques sur un site 100 % statique : `npm ci` sans
> `package-lock.json` commité, ou un script `build` absent. Les deux sont
> réglés dans ce dépôt (`package-lock.json` commité, script `build` no-op).
> Si le build échoue quand même, vérifier dans *Build settings* que le
> *Framework preset* est bien **None** et que *Build command* est vide —
> un preset auto-détecté peut l'écraser.
>
> **Si le déploiement échoue avec `Missing entry-point to Worker script or
> to assets directory`** : le projet Cloudflare a été créé comme un
> **Worker** (nouveau modèle unifié Workers/Pages) plutôt qu'un Pages
> classique — sa *Deploy command* est alors `npx wrangler deploy`, pas
> `npx wrangler pages deploy`. `wrangler.toml` gère déjà ce cas (`[assets]
> directory = "./site"`), donc un nouveau déploiement doit suffire. Pour
> repasser en Pages classique : dans les réglages du projet, *Settings* →
> *Build* → changer la *Deploy command* en `npx wrangler pages deploy site`.

**En ligne de commande** :
```bash
npm run deploy:cloudflare
# ou directement :
npx wrangler pages deploy site --project-name=agriwin-togo
```

## Alternative — Vercel

`vercel.json` (racine) pointe déjà `outputDirectory` vers `site`. Gratuit
pour un usage personnel ; au-delà, l'offre gratuite de Vercel est réservée
aux projets non commerciaux — à garder en tête pour un site d'entreprise.

```bash
npx vercel        # première fois : suit les invites
npx vercel --prod
```

## Migrer ailleurs

Le site est du HTML/CSS/JS statique sans dépendance de build : il se
redéploie tel quel sur n'importe quel hébergeur statique (Netlify, GitHub
Pages, un simple serveur avec `site/` comme racine…). Aucun verrou
propriétaire.

## Développement local

```bash
npm run dev   # sert site/ sur http://localhost:3000
```

## Identité de marque

Voir [`brand/`](./brand/) et [`CLAUDE.md`](./CLAUDE.md) pour le logo, le
design system publié comme artefact claude.ai, et le brand book A3 (PDF et
PowerPoint dans `brand/out/`).
