# Alimentations de remplacement

Les blocs d'alimentation d'origine ont souvent 30 à 40 ans. La plupart ne sont pas régulés : ils sortent bien plus que la tension inscrite dessus, chauffent et s'usent. Une alimentation à découpage régulée moderne chauffe moins, fait moins de bruit dans l'image et protège mieux ta console.

## Les 4 règles

1. **Tension :** la même que l'originale (certaines consoles tolèrent un peu moins, c'est indiqué plus bas).
2. **Courant (A ou mA) :** égal ou **plus élevé** que l'original. La console ne prend que ce dont elle a besoin.
3. **Polarité :** doit être identique. **Une mauvaise polarité peut endommager la console.**
4. **Fiche :** même taille et même type. Ne force jamais une fiche qui n'entre pas.

!!! tip "Vérifie avant de brancher"
    Au multimètre, confirme la tension et quel contact est positif (bout ou manchon) avant la première mise sous tension.

## Nos choix

La série WSU de Triad Magnetics est la référence de la communauté : régulée, pas chère et offerte chez [Mouser.ca](https://www.mouser.ca). Dans le numéro de pièce, **-R** = centre négatif, sans -R = centre positif, **-13** = fiche 5,5 × 2,5 mm (sinon 5,5 × 2,1 mm).

### Blocs d'alimentation externes

| Console | Origine | Polarité · fiche | Notre choix |
|---|---|---|---|
| Atari 2600 | 9 V CC 500 mA | Bout positif · fiche mono 3,5 mm | **Same Sky (CUI) SWI6-9-N-P1** (9 V 670 mA, régulée) — [Mouser](https://www.mouser.ca/c/?q=SWI6-9-N-P1) · *fiche à confirmer en main* |
| Atari 5200 | 9,3–11,5 V CC 1,95 A | Bout positif · 5,5 × 2,5 mm | Triad **WSU090-2000-13** |
| Atari 7800 | 9 V CC 1 A | Fiche 2 broches à détrompeur | Bloc Atari d'origine en bon état |
| Atari Lynx | 9 V CC 1 A | Centre positif · 3,5 × 1,35 mm | Triad **WSU090-1300** + adaptateur 5,5 × 2,1 → 3,5 × 1,35 |
| Atari Jaguar / Jaguar CD | 9 V CC 1,2 A | Centre négatif · 5,5 × 2,1 mm | Triad **WSU090-1300-R** |
| NES (Amérique du Nord) | 9 V **CA** 1,2 A | Sans polarité · 5,5 × 2,1 mm | Triad **WSU090-1300-R** (la NES accepte le CC) |
| Famicom / AV Famicom | 10 V CC 850 mA | Centre négatif · 5,5 × 2,1 mm | Triad **WSU090-1300-R** |
| Super Nintendo (Amérique du Nord) | 10 V CC 850 mA | Centre négatif · fiche SNES 6,9 × 4,1 mm | Bloc Nintendo SNS-002 d'origine — pas d'équivalent chez Mouser (fiche propriétaire) |
| Super Famicom | 10 V CC 850 mA | Centre négatif · 5,5 × 2,1 mm | Triad **WSU090-1300-R** |
| Master System | 9 V CC 1 A | Centre négatif · 5,5 × 2,1 mm | Triad **WSU090-1300-R** |
| Genesis / Mega Drive modèle 1 | 9 V CC 1,2 A | Centre négatif · 5,5 × 2,1 mm | Triad **WSU090-1300-R** |
| Genesis modèle 2, 32X, Nomad | 10 V CC 850 mA | Centre positif · EIAJ-03 (4,75 × 1,7 mm) | Triad **WSU090-1300** (centre positif) avec une fiche EIAJ-03 — soudée, ou avec un adaptateur 5,5 × 2,1 → EIAJ-03 (4,75 × 1,7 mm). Le 9 V fonctionne très bien. **Le bout doit être positif.** |
| Genesis 3 | 10 V CC 300 mA | Centre positif · EIAJ-03 | Comme la Genesis modèle 2 |
| Game Gear (Amérique du Nord) | 10 V CC 850 mA | Centre positif · EIAJ-03 | Comme la Genesis modèle 2 |
| TurboGrafx-16 / PC Engine | 9–10,5 V CC 650–730 mA | Centre négatif · 5,5 × 2,1 mm | Triad **WSU090-1300-R** |
| Neo Geo AES | **5 V** 3 A (premières) **ou 10 V** 1 A (plus récentes) | Centre négatif · 5,5 × 2,1 mm | Triad **WSU050-3000-R** (5 V) ou **WSU090-1300-R** (10 V) — **vérifie d'abord l'étiquette de ta console** |
| PSone (PS1 mince) | 7,5 V CC 2 A | Centre positif · EIAJ-03 | Bloc Sony officiel — **jamais un bloc de PS2 mince** |
| PS2 mince (SCPH-7xxxx) | 8,5 V CC 5,65 A | Centre positif · EIAJ-03 | Bloc officiel SCPH-70100 ou une copie de qualité |
| Nintendo 64, GameCube, Wii | Propriétaire | Fiche à détrompeur | Bloc Nintendo d'origine (ou copie avec le même numéro de pièce) |

### Alimentation interne (cordon en 8)

La Saturn, la PlayStation (originale), la PlayStation 2 (grosse), la Dreamcast et la Xbox ont leur alimentation à l'intérieur. Il leur faut seulement un **cordon C7** (« en 8 »). Les consoles nord-américaines utilisent la version *polarisée* (un côté plat, un côté arrondi). Une alimentation interne peut lâcher : si la console ne s'allume plus, [écris-nous](mailto:support@pixelnet.ca).

### Portables

Game Boy, Game Boy Pocket / Color et Game Boy Advance fonctionnent avec des piles. La Game Boy Advance SP se recharge avec sa propre fiche (des câbles USB 5 V existent). La PSP prend une fiche 5 V CC EIAJ-02 ou l'USB.

---

Sources : [ConsoleMods — Comparison of Power Supplies](https://consolemods.org/wiki/Comparison_of_Power_Supplies) et tests de la communauté. Pas certain ? [support@pixelnet.ca](mailto:support@pixelnet.ca) — on teste chaque console qu'on répare avec nos propres alimentations.
