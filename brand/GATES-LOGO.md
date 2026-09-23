# Gates: AgriWin Togo — correction du symbole

OWNS: logo/**, brandbook/**, scripts/**, ds/**, out/**

Scope: redessiner le symbole pour qu'il reprenne fidèlement le plant d'origine (feuilles larges et incurvées, deux hampes centrales presque verticales, feuilles extérieures retombantes, chèvre au trait en bas à droite), puis répercuter le nouveau logo dans les six variantes, le design system, le brand book PDF et le PowerPoint.

- [x] L1: la silhouette du nouveau symbole ressemble nettement à l'originale (IoU ≥ 0.72)
  CHECK: python3 scripts/check_symbol_shape.py
  EXPECT: L1_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=5e9ef8399de900b0f5e1cf1c62761000cdea995152ad82dea5112c5b7dfc3814; exit=0; EXPECT=matched; output-sha256=8df171dc2ea0385fe5d791e36673177ca3f76cfe95783002fad2c77657c5dea9; output-bytes=28; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L2: le nouveau symbole est plus proche de l'original que la version précédente
  CHECK: python3 scripts/check_symbol_better.py
  EXPECT: L2_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=8ff64fefa02e9568a588791cecfbc62b0315332251d669611f7888ceb69f2ffb; exit=0; EXPECT=matched; output-sha256=75141463601fdd70b934af69ff10b0f4177e64a50c732856987580f8cee50ebc; output-bytes=43; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L3: la structure du plant est respectée — sommet étroit, base étroite, feuilles extérieures atteignant les bords à mi-hauteur
  CHECK: python3 scripts/check_symbol_structure.py
  EXPECT: L3_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=98c365e920f135983228b8513cf11fe6e90dc1d55a03d7e801983d374031ba12; exit=0; EXPECT=matched; output-sha256=9dab7b74efbab95ae1be709724f9e3eb88e827763f89991c0a44b3d00b053a6e; output-bytes=44; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L4: la chèvre est présente, au trait, dans le quart inférieur droit du symbole
  CHECK: python3 scripts/check_goat.py
  EXPECT: L4_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=429fb52f1129270b24feabba3d05a32e83bd1095f9227870973ca864c7937695; exit=0; EXPECT=matched; output-sha256=9858c9bd7fc2af3bf1b84e90052afe278da3194f7cf8d994f0c5457f21f22e40; output-bytes=101; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L5: les six variantes existent, sont valides et se rasterisent
  CHECK: node scripts/check-logo-svg.mjs && node scripts/check-logo-png.mjs
  EXPECT: G2_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=d36c99cc34a8a4d39ec4b9df2db2b3d8721e34184c5f8485c84176a0f12085ac; exit=0; EXPECT=matched; output-sha256=5a9ee4bac9cbfee4e37be5a5dfdcd2de8df1753b66520d849663b6e7d07b2f2e; output-bytes=63; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L6: en monochrome et en inversé, les feuilles restent séparées les unes des autres
  CHECK: python3 scripts/check_mono_separation.py
  EXPECT: L6_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=d30400e83b537b712e78e6a5955bff3519b7a2aa72fb8eb96182f06a5f88f40d; exit=0; EXPECT=matched; output-sha256=68c43e294a28eaa45217ca53cb4a39b37b1ddb83b878b54db38a6d4dadc49743; output-bytes=65; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L7: le brand book PDF et le PowerPoint sont régénérés avec le nouveau logo et restent conformes
  CHECK: python3 scripts/check_regenerated.py
  EXPECT: L7_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=10daafad0005a0ca08c38790a13ad8c355c114b2f28686b761b9722a526e85ce; exit=0; EXPECT=matched; output-sha256=3b3e42c26e88b3698bc772f2359e54812795c935ee0437814ff9bbb5c168d0f8; output-bytes=68; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L8: la fiche « Le symbole » du brand book décrit la construction réellement dessinée
  CHECK: python3 scripts/check_symbol_doc.py
  EXPECT: L8_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=8dc1245b8db0c3db5a07243ba2740e75f011b4e62673f3f1c9c34861265df17d; exit=0; EXPECT=matched; output-sha256=65862d426bcd74e9997e0f6ddb9b3a52cf6c064963c2912f0d03f6e29251e57c; output-bytes=99; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries

- [x] L9: les vérificateurs de forme échouent bien sur un cas négatif connu
  CHECK: python3 scripts/check_logo_controls.py
  EXPECT: L9_OK
  EVIDENCE: automatic-evidence=v1; definition-sha256=1cac7f352cbec64548dfaa025dd45501739ab13949d09ce9375cb897b3529611; exit=0; EXPECT=matched; output-sha256=f20ebd14bd874ce633767ba5929dee2c6d0077eac7f4addaae8d1a8db2f99654; output-bytes=175; shell=/bin/sh; cwd=/home/claude/agriwin; path=4815f3331132/58 entries
