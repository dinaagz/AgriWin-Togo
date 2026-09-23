# Field

Champ de formulaire : libellé, contrôle, aide ou erreur.

Le libellé est en Poppins 600 13.5px `ink-900`, au-dessus du champ — jamais à l'intérieur.
Le champ au repos est `bg-soft` bordé de `border-soft` ; au focus il passe en `white`
bordé de `green-500` avec un halo de 3px. Le placeholder n'est pas un libellé : il montre
un exemple de saisie.

Propriétés : `label`, `id`, `as` (`input` par défaut, `textarea`, `select`), `type`,
`options`, `placeholder`, `value`, `note`, `error`, `required`, `disabled`, `rows`.

Le consommateur fournit `id` (obligatoire pour lier le libellé), la valeur et la
validation ; le composant ne valide rien lui-même.

- Le message d'erreur dit ce qui ne va pas et comment corriger : « Adresse incomplète :
  il manque le domaine », pas « Champ invalide ».
- `note` et `error` ne coexistent jamais : l'erreur remplace l'aide.
- Le rouge d'erreur `#B3261E` est hors palette de marque, réservé à cet usage — il tient
  6.54:1 sur blanc.
- Les champs obligatoires portent une astérisque ; indiquez-le une fois en haut du formulaire.
