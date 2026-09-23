# StepList

Déroule un processus dans l'ordre : pastille numérotée, titre, explication.

La numérotation n'est pas décorative — ne l'utilisez que pour une suite d'étapes réellement
ordonnées. Pour une liste sans ordre, utilisez des `ValueCard` ou des `ServiceCard`.

Propriétés : `steps` — `{ title, text }` dans l'ordre d'exécution.

- Trois à cinq étapes. Au-delà, le lecteur décroche.
- Le titre d'étape est une action du point de vue du client : « Vous décrivez votre projet ».
- La pastille est un disque `green-900` de 42px : elle ne change ni de forme ni de couleur
  selon l'étape.
