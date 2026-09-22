# Card

Conteneur de contenu : fond `white`, bordure `border-soft`, rayon `radius-lg`.

C'est la brique de toutes les grilles du site. Au survol, elle se lève de 5px et prend
`shadow-md` — le mouvement signale qu'elle est cliquable ; une carte non cliquable ne
doit donc pas l'avoir.

Propriétés : `media` (URL), `mediaAlt`, `badge`, `tag`, `title`, `text`, `children`, `className`.

Le consommateur fournit l'image et le texte ; la carte impose le cadrage 4/3 du média,
le padding de 22px du corps et la gouttière de 10px entre les blocs.

- Étiquette (`tag`) : une seule, la famille du produit ou du service.
- Le titre tient sur deux lignes au maximum à 18px.
- N'empilez pas bordure, ombre et fond coloré sur la même carte : la bordure suffit au
  repos, l'ombre au survol.
