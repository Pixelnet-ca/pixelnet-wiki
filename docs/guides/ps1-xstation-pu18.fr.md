# PlayStation : installer le XStation (carte PU-18)

Le **XStation** est un émulateur de lecteur optique (ODE) : il prend la place du lecteur de disque de la PlayStation, et les jeux se lancent à partir d'une **carte microSD**. Chargements plus rapides, fini le laser usé, et toute votre collection dans une seule console.

!!! warning "Ce guide est pour les cartes PU-18 seulement"
    L'installation change selon la **révision de la carte mère**. Sur une **PU-18**, il y a une étape de plus que les autres cartes n'ont pas : il faut **soulever 8 pattes** de la puce Sony **CXD2545Q** (IC701). Sur une PU-8, suivez le guide XStation pour cette carte. Les PU-20, PU-22, PU-23 et la PSone (PM-41) **ne sont pas compatibles**.

## Compatibilité

| Carte | Modèles typiques | XStation |
|---|---|---|
| **PU-18** | Toutes les SCPH-5xxx (5501, 5001…), très rarement SCPH-7001 à 7003 | ✅ Ce guide |
| **PU-8** (early ou late) | SCPH-100x, la plupart des SCPH-3xxx | ✅ Autre guide (étapes différentes) |
| **PU-20**, **PU-22**, **PU-23** | La plupart des SCPH-7xxx, SCPH-750x, SCPH-900x | ❌ |
| **PM-41** | PSone (SCPH-10x) | ❌ |

## Trouver votre carte

Ouvrez la console : la révision (**PU-18**, **PU-8**…) est imprimée sur la carte mère. Le numéro de modèle (SCPH-…) sur l'étiquette sous la console donne un bon premier indice, mais seule la carte elle-même est certaine.

![Carte mère PU-18 avec le blindage du dessus soulevé : IC701 est en bas à droite](../assets/guides/ps1-xstation/ps1-pu18-board.jpg){ .pn-photo }

![La révision imprimée sur la carte : PU-18](../assets/guides/ps1-xstation/ps1-pu18-revision.jpg){ .pn-photo }


## Ce qu'il vous faut

- La trousse **XStation** : carte principale, **QSB** (Quick Solder Board) pour PU-18, nappe et entretoises
- Un fer à souder à pointe fine avec contrôle de température, du flux, de la soudure fine et de la tresse à dessouder
- Une **aiguille fine** ou un couteau de précision (X-Acto) pour soulever les pattes
- Du **grossissement** (loupe, casque-loupe ou microscope) : les pattes d'IC701 sont minuscules
- Un multimètre, des pinces fines, de l'alcool isopropylique
- Une carte microSD pour vos jeux

## Étapes

!!! danger "Avant de commencer"
    Débranchez le cordon d'alimentation et **retirez tous les câbles du bloc d'alimentation**. Il faut démonter complètement la PlayStation pour atteindre la carte mère.

### 1. Trouver IC701 (CXD2545Q)

Sur le **dessus** de la carte mère, trouvez **IC701**, la puce Sony marquée **CXD2545Q**, dans le coin inférieur droit.

![IC701 : Sony CXD2545Q. Les numéros de pattes 1, 30, 31, 50, 51, 80, 81 et 100 sont imprimés autour](../assets/guides/ps1-xstation/ps1-ic701-cxd2545q.jpg){ .pn-photo }


### 2. Soulever 8 pattes d'IC701

C'est l'étape délicate. Soulevez **seulement** ces pattes : **45, 46, 47, 56, 74, 77, 78 et 80**.

Pour chaque patte : un peu de flux, touchez la patte avec la pointe du fer pour faire fondre la soudure, puis soulevez-la **doucement** par en dessous avec l'aiguille ou la lame. Une patte à la fois, sous grossissement. Tourner la carte peut vous donner un meilleur angle.

![Pattes soulevées sur la rangée du haut, près de la patte 80](../assets/guides/ps1-xstation/ps1-ic701-lifted-legs.jpg){ .pn-photo }


!!! tip "Vérifiez chaque patte"
    Chaque patte soulevée doit être **complètement** libre : aucun contact avec son pad ni avec la carte. Vérifiez-les une par une sous grossissement (et au multimètre en cas de doute). Ne soulevez aucune autre patte.

### 3. Préparer le dessous pour la QSB

Retournez la carte **à l'envers**. La QSB va dans la zone indiquée dans le guide XStation. Avant de souder, **grattez légèrement** les pads de via à gauche et à droite de cette zone pour que la soudure prenne bien.

### 4. Souder la QSB

Placez la QSB sur ses pads (les repères sur la QSB aident à l'aligner) et soudez-la.

### 5. Retirer la résistance et brancher APLL

Dessoudez et retirez la **petite résistance à côté de l'oscillateur** marqué **V67.737 KDS** (voir le guide officiel pour sa position exacte). Branchez ensuite le pad **APLL** de la QSB au point indiqué juste au-dessus de la résistance retirée.

### 6. Préparer le boîtier

Sur la **moitié du bas** du boîtier, coupez le **petit tenon de plastique** indiqué dans le guide XStation. Sinon, la nappe peut se briser à la fermeture de la console.

### 7. Brancher et faire passer la nappe

Branchez la nappe dans le connecteur de la QSB, **côté bleu vers le haut**, et refermez le loquet. Faites sortir la nappe par la **fente du blindage du dessus**.

### 8. Fixer le XStation

Enfoncez les **3 entretoises** dans la carte XStation (coins inférieur droit, supérieur droit et supérieur gauche, vu de dessus). Branchez l'autre bout de la nappe au XStation, pliez-la comme dans le guide, puis fixez le XStation sur les **poteaux du lecteur d'origine**.

![Le XStation fixé à la place du lecteur, nappe branchée](../assets/guides/ps1-xstation/ps1-xstation-installed.jpg){ .pn-photo }

![Le XStation de plus près](../assets/guides/ps1-xstation/ps1-xstation-closeup.jpg){ .pn-photo }


### 9. Tester avant de fermer

Remontez la console juste assez pour l'allumer, insérez la carte microSD avec un jeu et vérifiez que le menu s'affiche et que le jeu démarre. Remontez ensuite la PlayStation au complet.

## Guide officiel XStation

Les étapes ci-dessus résument le guide officiel, qui a une photo pour chaque étape (position des pattes, emplacement de la QSB, résistance à retirer). Gardez-le ouvert pendant l'installation. Il est en anglais.

[Guide officiel XStation PU-18 :material-open-in-new:](https://github.com/x-station/xstation-releases/wiki/xStation-ODE-installation-guide-for-the-PU-18-Playstation-1-motherboard){ .md-button target=_blank }

## Résultat

Votre PlayStation démarre sur le menu du XStation, et chaque jeu se lance à partir de la carte microSD. Le lecteur de disque d'origine n'est plus nécessaire : gardez-le en lieu sûr si jamais vous voulez revenir en arrière.

Pas à l'aise de soulever des pattes de puce ? PixelNet peut [l'installer pour vous](https://pixelnet.ca/collections/installation). Questions : [support@pixelnet.ca](mailto:support@pixelnet.ca)
