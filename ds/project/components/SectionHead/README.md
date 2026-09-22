# SectionHead

Ouvre une section : surtitre, titre, chapô.

Le mot d'accent passe en Playfair Display italique `gold-700` via `accent`. C'est le seul
endroit où la troisième police apparaît dans une interface, et jamais plus de trois mots.
`gold-700` (#9a6412) remplace ici le `gold-600` du site, qui ne donnait que 2.94:1 sur blanc.

Propriétés : `eyebrow`, `title`, `accent`, `lead`, `center`, `onDark`.

- `center` pour une section pleine largeur, aligné à gauche dans une colonne.
- Le chapô reste sous 220 caractères : au-delà, c'est un paragraphe de section.
- Un seul `h2` par section. Les sous-titres suivants sont des `h3`.
