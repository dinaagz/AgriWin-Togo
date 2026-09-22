AgriWin Togo est une entreprise agricole togolaise fondée en 2025 à Kégué : conseil,
formation, pépinière de plants tropicaux, écoulement des récoltes et accompagnement en
élevage. Elle parle à des particuliers, des coopératives, des entreprises, des ONG et des
investisseurs internationaux. Le système sert tous ses supports : site, réseaux sociaux,
documents commerciaux, signalétique de pépinière, véhicules.

## Ce que la marque promet

« Votre partenaire agricole ! » — la signature est une promesse d'accompagnement, pas un
slogan de vente. Trois idées la portent partout : un accompagnement technique fiable, des
plants de qualité contrôlés, des débouchés commerciaux réels.

Les quatre valeurs sont **fiabilité, qualité, proximité, ouverture**. Elles s'écrivent avec
ces mots-là, dans cet ordre, et se déclinent en `ValueCard`. N'en ajoutez pas pour remplir
une grille.

## Comment la marque parle

Écrivez en français, vouvoiement, phrases courtes, présent de l'indicatif. Le client est
« vous », l'entreprise est « nous ». Le ton est celui d'un technicien qui explique, pas
d'un commercial qui vend.

- Promettez ce qui est vérifiable : « chaque plant est contrôlé avant de quitter notre
  pépinière », pas « les meilleurs plants d'Afrique de l'Ouest ».
- Nommez les choses par leur nom d'usage agricole : manguier greffé, avocatier Hass, teck,
  moringa, sachet de 3 L, taux de reprise.
- Les prix sont en francs CFA, séparateur de milliers en espace fine, symbole après le
  nombre : `3 500 F`. Jamais « FCFA » collé au chiffre.
- Le numéro s'écrit `+228 96 63 82 00`, groupé par deux chiffres, et sert aussi pour
  WhatsApp. L'adresse est « Kégué, Togo ». Les horaires : « Lun–Sam : 8h – 18h ».
- Pas d'emoji dans les supports de marque. Sur les réseaux sociaux, un seul par
  publication au maximum.
- « AgriWin Togo » s'écrit avec deux majuscules internes et un espace avant Togo. Jamais
  « Agriwin », « AGRIWIN » ni « AgriWin-Togo ».

## Couleur

La marque tient sur une famille de verts végétaux et un or de terre. Le vert domine, l'or
ponctue : sur une page, l'or ne dépasse pas un dixième de la surface colorée.

- Fond de page : `white`. Alternez les sections avec `bg-soft`, et `green-50` pour les
  blocs de valeurs.
- Titres : `green-950`. Texte courant : `ink-700`. Texte secondaire : `ink-500`.
- Aplats de marque : `green-900`, ou le dégradé `green-900 → green-700` (bande de
  chiffres) et `green-900 → green-600` (bandeau d'appel à l'action).
- Actions : `green-700` pour le vert plein, `gold-500` pour l'action de conversion.
- Bordures et séparateurs : `border-soft`.
- `whatsapp` est une couleur de service imposée par la plateforme : elle ne sert qu'au
  bouton WhatsApp et n'entre jamais dans une composition graphique.

Deux règles de lisibilité, issues d'un contrôle WCAG de la palette d'origine :

- Tout texte or sur fond clair prend `gold-700`. `gold-600` ne donne que 2.94:1 sur blanc
  et reste réservé aux aplats et aux filets épais.
- Le surtitre en pastille prend `green-900` sur `green-100` (6.83:1). La combinaison
  `green-700` sur `green-100` du site d'origine ne donnait que 4.45:1.

`gold-500` sur `green-900` tient 3.69:1 : réservé au grand texte, comme le chiffre de 34px
de `StatBand`. Le rouge d'erreur `#B3261E` est hors palette, réservé aux messages de
validation.

## Typographie

Trois polices, trois rôles, pas d'exception.

- **Poppins** — titres, surtitres, boutons, navigation, chiffres. Graisses 500 à 800.
- **Inter** — tout le texte courant, les formulaires, les tableaux. Graisses 400 à 600.
- **Playfair Display italique** — un à trois mots d'accent dans un titre, et la signature
  « Votre partenaire agricole ! ». Rien d'autre. Un paragraphe entier en Playfair est une
  faute.

Les styles sont nommés dans les tokens : `display`, `h1`, `h2`, `h3`, `h4`, `eyebrow`,
`button`, `nav`, `stat` pour Poppins ; `lead`, `body`, `body-sm`, `caption`, `micro` pour
Inter ; `accent-italic`, `signature`, `quote` pour Playfair. Les tailles des titres sont
fluides : la valeur du token est le maximum, la borne basse est indiquée dans sa note.

Le texte courant reste autour de 65 caractères par ligne. Les surtitres sont en capitales
avec 0.08em d'interlettrage ; rien d'autre n'est en capitales.

## Logo

Le symbole est un plant de sisal à six feuilles — deux hampes centrales presque verticales, deux feuilles latérales montantes et deux feuilles extérieures retombantes — avec une chèvre au trait à leur pied.
L'agriculture et l'élevage, les deux métiers d'AgriWin Togo, tiennent dans un seul signe. Il n'a
pas été redessiné : le logo d'origine a été vectorisé, et seules ses valeurs de couleur
ont été ramenées sur la palette. Les fichiers sont dans le
groupe d'assets **Logos** : version principale verticale, version horizontale, symbole seul,
monochrome, version inversée, monogramme.

- Zone de protection : la hauteur de la hampe centrale divisée par quatre, de tous les côtés.
  Rien n'y entre, pas même un filet.
- Taille minimale : 28 mm de large à l'impression, 120 px à l'écran pour le verrouillage
  horizontal ; en dessous, utilisez le monogramme.
- Sur fond clair, la version en dégradé de verts. Sur photo ou aplat foncé, la version
  inversée. En une seule encre, la version monochrome `green-950`.
- Le symbole ne se déforme pas, ne se recadre pas, ne change pas de couleur, et ne se pose
  pas sur une photo chargée sans aplat de protection.
- La signature accompagne le nom dans l'en-tête et le pied de page. Elle disparaît sur les
  usages très réduits (favicon, avatar), où seul le monogramme subsiste.

## Iconographie

Pictogrammes au trait, grille de 24px, trait de 2px, extrémités et jonctions arrondies,
couleur héritée du texte. Le jeu fourni par `Icon` couvre les besoins du site : `leaf`,
`school`, `users`, `shield`, `target`, `arrow`, `phone`, `mail`, `pin`, `calendar`,
`check`, `search`. Ce sont les tracés du site AgriWin Togo, repris tels quels ; pour un
besoin nouveau, dessinez dans la même grille plutôt que d'importer un autre jeu.

Dans une carte service, le pictogramme est blanc dans un carré de 58px rempli du dégradé
`green-700 → green-500`. Partout ailleurs, il est au trait, de la couleur du texte voisin.
Les pictogrammes ne remplacent jamais un libellé : ils l'accompagnent.

## Photographie

Des photos de terrain, prises à hauteur d'homme, en lumière naturelle : mains dans la
pépinière, mise en terre, plateaux de jeunes plants, marché. Des gens au travail, pas des
poses. Les verts de la photo doivent pouvoir voisiner les verts de la marque sans jurer.

Sur une photo qui porte du texte, posez le dégradé `rgba(15,61,23,.55) → rgba(15,61,23,.82)`
du haut vers le bas : c'est ce qui garantit le contraste du titre blanc.

Le site utilise encore des images d'ambiance en attendant les photos de la pépinière et de
l'équipe. Toute image de substitution porte une mention explicite sous le bloc ; retirez la
mention en même temps que l'image.

## Formes, ombres, mouvement

Quatre rayons seulement : `radius-sm` pour les champs, `radius-md` pour les pictogrammes et
les blocs, `radius-lg` pour les cartes et les bandeaux, `radius-pill` pour les boutons et les
pastilles. Trois ombres, toujours teintées de vert foncé : `shadow-sm` au repos,
`shadow-md` au survol, `shadow-lg` pour les éléments flottants.

Le mouvement est court et utilitaire : 0.15 à 0.2 s en `ease`. Une carte cliquable se lève
de 5px au survol, un bouton se comprime de 3 % au clic, la flèche d'un lien avance de 4px.
Rien d'autre ne bouge.

## Accessibilité

- Tout texte atteint 4.5:1 sur son fond ; 3:1 à partir de 24px ou en gras à 19px.
- Le focus clavier reste visible : contour `green-700` de 3px, décalé de 2px. Ne le
  supprimez jamais.
- L'état d'une puce de filtre passe par `aria-pressed`, pas par une classe.
- Chaque champ a un libellé lié par `id`. Le placeholder n'est pas un libellé.
- Un message d'erreur dit ce qui ne va pas et comment corriger.

## Mise en page

Contenu centré sur `container` (1180px), marge latérale de 20px. En-tête fixe de `header-h`
(78px). Sections à 64px de padding vertical, 40px pour une section courte. Grilles de deux,
trois ou quatre colonnes avec une gouttière de `space-7` (26px), qui repassent à une colonne
sous 640px.

Une page se construit dans cet ordre : hero, preuve (chiffres ou citation), offre (cartes
service), spécialité, catalogue, ambiance, bandeau d'appel à l'action. Un seul `CtaBand`
par page, tout en bas.
