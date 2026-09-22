# FilterChip

Filtre le catalogue par famille de produits.

L'état actif est porté par `aria-pressed`, pas par une classe : le lecteur d'écran annonce
« activé ». Actif, la puce passe en `green-700` sur blanc — 5.13:1.

Propriétés : `label`, `active`, `onToggle`.

- Une puce « Tous » en première position, active par défaut.
- Le libellé est un nom de famille, au pluriel, sans compteur : le nombre de résultats
  s'affiche sous la barre de filtres.
- Six puces au maximum sur une ligne ; au-delà, regroupez les familles.
