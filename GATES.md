# Gates: AgriWin Togo — design system + brand book A3

OWNS: logo/**, brandbook/**, scripts/**, out/**

Scope: livrer le logo AgriWin Togo revectorisé en 6 variantes SVG, un design system web publié comme artefact claude.ai, un brand book A3 paysage en PDF d'au moins 20 pages, et sa version PowerPoint A3 éditable.

- [x] G1: les six variantes de logo existent en SVG bien formé et non trivial
  CHECK: node scripts/check-logo-svg.mjs
  EXPECT: G1_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=d2160e32f3fc5b314e6b5d3a291991eb785868b5a3912b256c5eacb9929596db; exit=0; EXPECT=matched; output-sha256=bb48a0a26beec301a59b303556f6f509575e9ca9e1bd958aa92381f165bed664; output-bytes=32; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G2: chaque variante de logo se rasterise en PNG non trivial
  CHECK: node scripts/check-logo-png.mjs
  EXPECT: G2_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=b0134eb2ea66a9c4e77dad061dbd4855a303f7516100b14590a61a1edaf275bf; exit=0; EXPECT=matched; output-sha256=e5b8c8b724475f86f425a26f2bc163af8ac23ac7ae4dec81b37f6901ccf185bb; output-bytes=31; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G3: le design system est publié et son URL d'artefact est enregistrée
  CHECK: node scripts/check-artifact-url.mjs
  EXPECT: G3_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=363d7087b8a3f5651030f2f74c564462d273851ff23f29a17dec0b924e80310a; exit=0; EXPECT=matched; output-sha256=d5e953dd429b3d98176b2ef5b6d47a92b9f893e812ea269cc739dc0baeb36aa1; output-bytes=58; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G4: le brand book PDF compte au moins 20 pages au format A3 paysage
  CHECK: python3 scripts/check_pdf.py
  EXPECT: G4_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=0c0f01f1e07c7252a42651e8a4a38ef3421c2570e114a536f91567f3a93e1356; exit=0; EXPECT=matched; output-sha256=101863ebc39189854601b97b52dd4daaadf83bd72a89ccce600bed6ff413dc86; output-bytes=45; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G5: le PPTX est en A3 paysage, compte au moins 20 diapositives et du texte natif éditable
  CHECK: python3 scripts/check_pptx.py
  EXPECT: G5_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=d9f1b9817c882cdead7eb4cca08a3c8cb5187a3cef24e93d44c64fd0858bfa0c; exit=0; EXPECT=matched; output-sha256=a4bb40fbb59c78e1f561a1d403b7920a810ae47ecc58ccf6976a7ca8038349b0; output-bytes=78; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G6: chaque paire couleur texte/fond documentée atteint le ratio WCAG annoncé
  CHECK: python3 scripts/check_contrast.py
  EXPECT: G6_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=e351cc8fdd237e09d8db88bd919f434b6519c839f890500b1b21d28d4c29536d; exit=0; EXPECT=matched; output-sha256=e5253169bf8780a702ffb9a2132d4790ea8c93b77d17011d7e03ec6c93a68d79; output-bytes=60; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G7: les tokens du design system reprennent à l'identique ceux du site existant
  CHECK: python3 scripts/check_tokens.py
  EXPECT: G7_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=f6625407dc8f1e124e369c03217514328cab6479c931cb79f71a16d94602958e; exit=0; EXPECT=matched; output-sha256=562d7a2f9074c21c0c79d2d50c2c405f963d066e4989ddbad5b8c4a6c5d2667e; output-bytes=65; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G8: les fichiers livrables sont déposés pour l'utilisateur avec une taille plausible
  CHECK: node scripts/check-deliverables.mjs
  EXPECT: G8_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=1222a8f971b66d38f44a97d5d415054643b0516cfd1e00ec517864b79a119eb4; exit=0; EXPECT=matched; output-sha256=adfb960724098bdb48c79121671e538244bf498de9a2645396bbbc48ef829e50; output-bytes=26; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] G9: les scripts de vérification échouent réellement sur un cas négatif connu
  CHECK: node scripts/check-controls.mjs
  EXPECT: G9_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=14b51628caa8ebc7d258800023f57e3a14b338a9d76324255447712a964ddb32; exit=0; EXPECT=matched; output-sha256=ddea47ef956bbab47ecf067f7bd2ac1f28f33914c54c039b18c6ca4210b31ca4; output-bytes=190; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries
