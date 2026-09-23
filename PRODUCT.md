# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Client prioritaire — particuliers et petits producteurs.** Ils achètent des
plants à l'unité ou en petite quantité (manguier greffé à 2 500 FCFA, moringa à
1 000 FCFA) et ont besoin d'un conseil de plantation en même temps que du plant.
Décision rapide, souvent depuis un téléphone, conversation directe plutôt que
processus d'achat. C'est leur réussite qui prime dans les arbitrages.

Autres publics servis, confirmés par le contenu du site mais non prioritaires :

- entreprises et porteurs de projets (vergers, reboisement, agroforesterie,
  commandes en gros) ;
- ONG et coopératives (formation de groupes, projets encadrés) ;
- investisseurs internationaux et diaspora, qui décident à distance ;
- producteurs cherchant des débouchés pour leurs récoltes.

## Product Purpose

AgriWin Togo est une entreprise d'expertise et de prestation de services
agricoles, de formation et d'écoulement de produits agricoles, avec une
spécialité de plants tropicaux. Fondée en 2025, basée à Kégué (Togo).

Six domaines : expertise et conseil agricole, prestations de services agricoles,
formation, écoulement de produits, pépinière et plants tropicaux, accompagnement
en élevage.

Mission telle qu'elle est écrite sur le site : « Rendre l'expertise agricole, les
plants de qualité et les débouchés commerciaux accessibles à tous les porteurs de
projets, quelle que soit leur taille, au Togo et au-delà. »

Vision : devenir une référence ouest-africaine de l'accompagnement agricole
intégré.

## Positioning

Le constat fondateur, repris sur la page À propos : les porteurs de projets
agricoles manquent de **trois** choses à la fois — un accompagnement technique
fiable, des plants de qualité, et des débouchés pour leurs récoltes. Une
pépinière vend des plants ; un consultant conseille ; un intermédiaire trouve des
acheteurs. AgriWin Togo répond aux trois dans une seule structure.

Deuxième élément de position, factuel : chaque plant est sélectionné et contrôlé
avant de quitter la pépinière de Kégué.

## Operating Context

- **WhatsApp est le canal principal.** Le site n'a pas de backend : le formulaire
  de contact compose un message et ouvre WhatsApp (`wa.me`) ou le client mail.
  Un bouton WhatsApp flottant est présent sur chaque page, et le téléphone
  figure dans la barre supérieure.
- Usage majoritairement mobile, en cohérence avec le client prioritaire.
- Horaires affichés : lundi–samedi, 8h–18h.
- Prix en FCFA (XOF).
- Contenu intégralement en français, sans version multilingue.
- Présence sociale : Facebook `/agriwintogo`, TikTok `@agriwintogo`.

## Capabilities and Constraints

- Site statique HTML/CSS/JS, **sans étape de build**. `site/` est la racine
  servie. Déploiement Cloudflare (Workers aujourd'hui, Pages documenté dans le
  README) ; `vercel.json` fourni comme alternative.
- Aucun backend à ce jour. Aucune donnée client n'est stockée : le formulaire ne
  fait que pré-remplir un message sortant.
- Catalogue : 12 produits, 4 catégories (fruitiers, forestiers et ornement,
  semences et intrants, élevage). Prix de 1 000 à 35 000 FCFA. États de stock
  « disponible » et « sur commande ». SKU au format `AWT-PL-00x`.
- `js/products.js` et `js/site-config.js` tentent `api/produits.json` et
  `api/parametres.json`, puis retombent sur des valeurs statiques intégrées. Ces
  fichiers d'API n'existent pas aujourd'hui ; le site fonctionne sans eux.
- **Phase 2 confirmée par le client** : panier e-commerce, paiement en ligne et
  panneau d'administration. Les fiches produits portent déjà `id`, `sku`,
  `price`, `stock` en prévision. Le travail de design doit ménager cette
  évolution — sans faire croire que la boutique est déjà ouverte.

## Brand Commitments

- Nom : **AgriWin Togo**. Signature : « Votre partenaire agricole ! »
- Fondateur : **KEGNON Emmanuel**, Fondateur & CEO. Sa citation est utilisée en
  page d'accueil et sur À propos.
- **Le symbole du logo ne se redessine pas.** Il est vectorisé depuis l'image
  fournie par le client. Une version redessinée a été rejetée par le client ;
  toute reprise doit passer par les portes L1–L4 de `brand/GATES-LOGO.md`.
- **Les couleurs ne s'inventent pas.** Elles viennent du bloc `:root` de
  `site/css/style.css` et sont reprises dans `brand/brandbook/tokens.json`. Un
  seul token a été ajouté, `gold-700` (#9A6412), pour des raisons de contraste.
- Typographies : Poppins (titres), Inter (texte courant), Playfair Display
  (accent).
- Design system qui fait foi : `brand/ds/project/`, publié comme artefact
  claude.ai. `design-system/MASTER.md` n'est qu'une fiche de référence rapide.
- Valeurs affichées : Fiabilité, Qualité, Proximité, Ouverture.

## Evidence on Hand

**Réel et utilisable :** coordonnées complètes, six services détaillés avec leurs
sous-prestations, catalogue de 12 produits avec prix et état de stock, identité
du fondateur et sa citation, année de création (2025), implantation (Kégué),
fichiers de logo, brand book A3 et design system.

**Placeholders, déclarés comme tels sur le site :** portrait du fondateur,
galerie de réalisations (pépinière, chantiers, formations), visuels produits
(SVG dans `site/images/placeholders/`).

**Statut des photos, confirmé par le client :** les vraies photos arriveront,
mais le design doit tenir sans elles, et des images de banque sont acceptées en
attendant. Une surface ne doit donc jamais dépendre d'une photographie de terrain
qui n'existe pas encore.

**Ce qui n'existe pas et ne doit pas être fabriqué :** aucun témoignage client,
aucune référence nommée, aucun chiffre de performance, aucune certification,
aucun partenariat. Les chiffres affichés (2025 / 6 domaines / 10+ variétés /
Togo + international) décrivent l'offre, pas des résultats.

## Product Principles

1. **Le petit acheteur d'abord.** Entre une mise en page qui rassure un
   investisseur et une qui permet à un particulier de commander trois plants
   depuis son téléphone, c'est la seconde qui gagne.
2. **La conversation est la conversion.** Tant qu'il n'y a pas de paiement en
   ligne, chaque surface doit mener à un échange WhatsApp ou téléphonique, pas à
   un formulaire qui disparaît dans le vide.
3. **Ne jamais fabriquer de preuve.** Le site signale lui-même ses placeholders.
   Cette honnêteté est un engagement, pas un défaut à masquer.
4. **Prêt pour la Phase 2 sans la simuler.** La structure accueille panier et
   administration ; rien ne doit laisser croire que la boutique est ouverte
   avant qu'elle le soit.
5. **L'identité est fixée et mesurée.** Symbole, palette et typographies sont
   arrêtés et vérifiés par des portes de contrôle. Le travail de design s'appuie
   dessus au lieu de les rouvrir.

## Accessibility & Inclusion

- Un audit WCAG AA de la palette a déjà été mené : deux combinaisons du site
  échouaient et ont été corrigées. `gold-600` (#C98A2B) ne donne que 2.94:1 sur
  blanc et ne peut porter aucun texte — d'où `gold-700`.
- Lien d'évitement « Aller au contenu » présent sur chaque page.
- Le mobile n'est pas une préférence mais la condition d'usage réelle du client
  prioritaire.
- Règle de projet : tout nouveau couple de couleurs se **mesure**, il ne
  s'estime pas.
