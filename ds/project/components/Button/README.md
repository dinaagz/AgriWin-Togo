# Button

Déclenche l'action principale d'un bloc : devis, catalogue, appel, WhatsApp.

Une seule action or (`primary`) par écran visible : c'est elle qui porte la conversion.
Le fond est `gold-500`, le texte `green-950` — 5.79:1. N'utilisez jamais `gold-600`
comme fond de bouton : le texte blanc n'y passe pas.

| Variante | Quand |
| --- | --- |
| `primary` | Action de conversion : devis, commande, catalogue |
| `green` | Action principale d'un bloc secondaire, fond `green-700` |
| `outline` | Sur aplat vert uniquement — le contour est blanc |
| `outline-green` | Action secondaire sur fond clair |
| `call` | Appel téléphonique, fond blanc et contour `green-700` |
| `whatsapp` | Uniquement pour WhatsApp, avec le vert de service `whatsapp` |

Propriétés : `variant`, `label`, `size` (`md` par défaut, `sm` en barre d'en-tête),
`icon`, `href`, `block`, `disabled`, `onClick`. Avec `href`, le composant rend un `<a>`.

- Libellé à l'infinitif ou à l'impératif, jamais « Cliquez ici » : « Demander un devis »,
  « Voir le catalogue ».
- Le rayon est toujours `radius-pill`. Ne le remplacez pas par `radius-md`.
- Une paire de boutons se pose dans un `.aw-btn-group` (gouttière `space-3`).
- Le focus clavier affiche un contour `green-700` de 3px : ne le supprimez pas.
