# ProductCard

Entrée du catalogue : visuel, étiquette, prix, deux actions.

Le prix est en `green-800` et en Poppins 20px ; l'unité qui suit est en `ink-500` 12.5px.
Le badge d'angle (`badge`) est en `gold-500` sur `green-950` et sert à un seul message à
la fois : « Nouveau », « Volume », « Saison ».

Propriétés : `media`, `title`, `text`, `tag`, `price`, `unit`, `badge`,
`primaryLabel` (« Commander »), `secondaryLabel` (« Détails »).

- Le prix s'écrit en francs CFA avec une espace fine comme séparateur de milliers :
  `3 500 F`. Jamais « FCFA » collé au nombre.
- Les deux boutons sont de taille `sm` et partagent la largeur à parts égales.
- Sans visuel, la carte affiche l'aplat `green-100` : c'est prévu, ne bouchez pas le trou
  avec une image générique.
