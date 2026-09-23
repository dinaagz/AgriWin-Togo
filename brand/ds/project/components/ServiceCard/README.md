# ServiceCard

Présente un service : pictogramme, titre, promesse, lien.

Le pictogramme est un carré de 58px en `radius-md`, rempli du dégradé `green-700 → green-500`,
trait blanc de 2px. C'est la seule occurrence de dégradé à petite échelle du système ;
partout ailleurs, les dégradés sont réservés aux grands aplats.

Propriétés : `icon` (`leaf`, `school`, `users`, `shield`, `target`, `phone`, `mail`, `pin`,
`calendar`, `check`, `search`), `title`, `text`, `linkLabel`, `href`.

- Les services vont par trois ou par six : la grille est en trois colonnes.
- Le texte tient en une phrase. Le détail va sur la page service, pas dans la carte.
- La flèche du lien avance de 4px au survol de la carte entière, pas du seul lien.
