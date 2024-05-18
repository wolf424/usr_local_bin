#!/bin/python
# -*- coding: utf-8 -*-
# *****************************************************************************
# Host          : sarbecovirus
# File          : genbovis.py
# Author        : ALX
# Creation      : 2022-01-13
# Last Revision : 2022-02-20
# Release       : V1.14
# Description   : Générateur de Bovis
# *****************************************************************************

# A ajouter
# - Tout semble montrer que
# - syntoniser
# - Cette méthode a de nombreuses fois été testée sur le terrain par une équipe d'ingénieurs et de méditants
# - des technologies génératrices d'ondes scalaires
# - reprogrammation indirecte et globale de l'ADN


# 'en tirant partie du'
# 'et'
# 'est lié à'
# chaque coordonnée + partitif
# chaque
# 
# 'tous les'

# adjectif = partitif + nom

import os, sys
import random
import argparse
import re

# GRAMMAIRE
# S -> VN
# VN -> SU V
# SU -> D N
# D -> le | un
# N -> chat | lion
# V -> mange | sort
# verbe (V), nom (N), déterminant (D), sujet (SU), noyau verbal (VN) ainsi que par l’axiome S

# percer les mystères de l'abondance
# intercède au niveau de ...
# La clef d'une énergie positive réside dans ..."

# prépositions : de, à, dans, en, pour, par, sur, avec

# article indéfini (exemple : 'la pomme tombe', 'il boit l'eau')
l_article_defini = \
[['le ', 'la ', 'les ', 'les '], # suivi de consonne
 ['l\'', 'l\'', 'les ', 'les ']] # suivi de voyelle

# article indéfini (exemple : 'un chien aboie', 'il ramasse des feuilles')
l_article_indefini = \
[['un ', 'une ', 'des ', 'des '], # suivi de consonne
 ['un ', 'une ', 'des ', 'des ']] # suivi de voyelle

# article partitif (exemple : 'il mange du pain', 'il trouve de l'or' - 'pain' et 'or' sont COD)
l_article_partitif = \
[['du', 'de la', 'des ', 'des '], # suivi de consonne
 ['de l\'', 'de l\'', 'des ', 'des ']] # suivi de voyelle

# préposition de + article défini (exemple : 'il parle du pain qu'il vient d'acheter' - pain est COI)
l_du_defini = \
[['du', 'de la', 'des ', 'des '], # suivi de consonne
 ['de l\'', 'de l\'', 'des ', 'des ']] # suivi de voyelle

# préposition de + article indéfini (exemple : il parle d'une musique qu'il a écoutée')
l_du_indefini = \
[['d\'un', 'd\'une', 'de', 'de '],  # suivi de consonne
 ['d\'un', 'd\'une', 'd\'', 'd\'']] # suivi de voyelle

l_a_defini = \
[['au', 'à la', 'aux', 'aux'],  # suivi de consonne
 ['à l\'', 'à l\'', 'aux', 'aux']]  # suivi de voyelle

# préposition à + article défini contracté : au (=à le), à la, à l', aux (à les)

l_dunompropre =  \
['d\'Apophis',
 'd\'Horus',
 'd\'Osiris',
 'de Gilgamesh',
 'd\'Albert Einstein',
 'de Déméter',
 'd\'Isaac Newton',
 'd\'Archimède',
 'de Copernic',
 'de Dirac',
 'de Schrödinger',
 'de Volta',
 'de Tcherenkov',
 'd\'Heisenberg',
 'd\'Alain Aspect',
 'de Ptolémée',
 'des géologues du XXe siècle',
 'd\'Aristote',
 'de Higgs',
 'du Christ cosmique',
 'de Planck',
 'De Bohm',
 'de Tellos',
 'de Râ',
 'de la Zone 51',
 'de Bugarache',
 'de Jean-Pierre Petit',
 'de Nassim Haramein',
 'd\'anticytère',
 'd\'Orion',
 'de Guido d\'Arezzo',
 'de Sylvain Durif',
 'des pyramides',
 'de Jacques Grimault',
 'd\'idriss Aberkane',
 'des laboratoires Boiron',
 'des savants russes',
 'du CNRS',
 'd\'Isaac Asimov',
 'des ummites',
 'de l\'humanité',
 'de la nature',
 'de Natacha Calestrémé',
 'de Bagdad']

# 1:masculin, 2:féminin, 3:pluriel masculin, 4;pluriel féminin
l_adjectif = \
[['à boucle', 'à boucle', 'à boucle', 'à boucle'],
 ['à distance', 'à distance', 'à distance', 'à distance'],
 ['à l\'échelle quantique', 'à l\'échelle quantique', 'à l\'échelle quantique', 'à l\'échelle quantique'],
 ['alchimique', 'alchimique', 'alchimiques', 'alchimiques'],
 ['antroposophique', 'antroposophique', 'antroposophiques', 'antroposophiques'],
 ['ARK', 'ARK', 'ARK', 'ARK'],
 ['astral', 'astrale', 'astraux', 'astrales'],
 ['en rotation', 'en rotation', 'en rotation', 'en rotation'],
 ['biochimique', 'biochimique', 'biochimiques', 'biochimiques'],
 ['bio-énergétique', 'bio-énergétique', 'bio-énergétiques', 'bio-énergétiques'],
 ['bio-générateur', 'bio-génératrice', 'bio-générateurs', 'bio-génératrices'],
 ['céleste', 'céleste', 'célestes', 'célestes'],
 ['charriant l\'universel', 'charriant l\'universel', 'charriant l\'universel', 'charriant l\'universel'],
 ['cohérent', 'cohérente', 'cohérents',  'cohérentes'],
 ['contenu', 'contenue', 'contenus', 'contenues'],
 ['cosmique', 'cosmique', 'cosmiques', 'cosmiques'],
 ['cosmologique', 'cosmologique', 'cosmologiques', 'cosmologiques'],
 ['cosmotellurique', 'cosmotellurique', 'cosmotelluriques', 'cosmotelluriques'],
 ['cristallin', 'cristalline', 'cristallins', 'cristallines'],
 ['de la conscience', 'de la conscience', 'de la conscience', 'de la conscience'],
 ['de l\'abondance', 'de l\'abondance', 'de l\'abondance', 'de l\'abondance'],
 ['de l\'univers', 'de l\'univers', 'de l\'univers', 'de l\'univers'],
 ['de notre univers', 'de notre univers', 'de notre univers', 'de notre univers'],
 ['d\'antimatière', 'd\'antimatière', 'd\'antimatière', 'd\'antimatière'],
 ['du champ unifié', 'du champ unifié', 'du champ unifié', 'du champ unifié'],
 ['du point zéro', 'du point zéro', 'du point zéro', 'du point zéro'],
 ['électro-photonique', 'électro-photonique', 'électro-photoniques', 'électro-photoniques'],
 ['électrosensible', 'électrosensible', 'électrosensibles', 'électrosensibles'],
 ['énergétique', 'énergétique', 'énergétiques', 'énergétiques'],
 ['fondamental', 'fondamentale', 'fondamentaux', 'fondamentales'],
 ['fractal', 'fractale', 'fractals', 'fractales'],
 ['fréquentiel', 'fréquentielle', 'fréquentiels', 'fréquentielles'],
 ['harmonique', 'harmonique', 'harmoniques', 'harmoniques'],
 ['harmonisateur', 'harmonisatrice', 'harmonisateurs', 'harmonisatrices'],
 ['holistique', 'holistique', 'holistiques', 'holistiques'],
 ['holographique', 'holographique', 'holographiques', 'holographiques'],
 ['homéopathique', 'homéopathique', 'homéopathiques', 'homéopathiques'],
 ['hyperbolique', 'hyperbolique', 'hyperboliques', 'hyperboliques'],
 ['hyperdimensionnel', 'hyperdimensionnelle', 'hyperdimensionnels', 'hyperdimensionnelles'],
 ['intra-terrestre', 'intra-terrestre', 'intra-terrestres', 'intra-terrestres'],
 ['intégratif', 'intégrative', 'intégratifs', 'intégratives'],
 ['inversé', 'inversée', 'inversés', 'inversées'],
 ['ionisé', 'ionisée', 'ionisés', 'ionisées'],
 ['isotrope', 'isotrope', 'isotropes', 'isotropes'],
 ['local', 'locale', 'locaux', 'locales'],
 ['lumineux', 'lumineuse', 'lumineux', 'lumineuses'],
 ['moléculaire', 'moléculaire', 'moléculaires', 'moléculaires'],
 ['morphogénétique', 'morphogénétique', 'morphogénétiques', 'morphogénétiques'],
 ['naturopathique', 'naturopathique', 'naturopathiques', 'naturopathiques'],
 ['négatif', 'négative', 'négatifs', 'négatives'],
 ['neutralisé', 'neutralisée', 'neutralisés', 'neutralisées'],
 ['non enseigné par la médecine actuelle', 'non enseignée par la médecine actuelle', \
  'non enseignés par la médecine actuelle', 'non enseignées par la médecine actuelle'],
 ['omniscient', 'omnisciente', 'omniscients', 'omniscientes'],
 ['ondulatoire', 'ondulatoire', 'ondulatoires', 'ondulatoires'],
 ['originel', 'originelle', 'originels',  'originelles'],
 ['oscillatoire', 'oscillatoire', 'oscillatoires', 'oscillatoires'],
 ['ouranien', 'ouranienne', 'ouraniens',  'ouraniennes'],
 ['pinéal', 'pinéale', 'pinéaux', 'pinéales'],
 ['planétique', 'planétique', 'planétiques', 'planétiques'],
 ['primordial', 'primordiale', 'primordiaux', 'primordiales'],
 ['positif', 'positive', 'positifs', 'positives'],
 ['profond', 'profonde', 'profonds', 'profondes'],
 ['quantique', 'quantique', 'quantiques', 'quantiques'],
 ['quasi-illimité', 'quasi-illimitée', 'quasi-illimités', 'quasi-illimitées'],
 ['que nous voyons', 'que nous voyons', 'que nous voyons', 'que nous voyons'],
 ['régénérateur', 'régénératrice', 'régénérateurs', 'régénératrices'],
 ['reptilien', 'reptilienne', 'reptiliens', 'reptiliennes'],
 ['rétroactif', 'rétroactive', 'rétroactives', 'rétroactives'],
 ['scalaire', 'scalaire', 'scalaires', 'scalaires'],
 ['sensoriel', 'sensorielle', 'sensoriels', 'sensorielles'],
 ['spécifique', 'spécifique', 'spécifiques', 'spécifiques'],
 ['spécifique de la nature', 'spécifique de la nature', 'spécifiques de la nature', 'spécifiques de la nature'],
 ['structurel', 'structurelle', 'structurels', 'structurelles'],
 ['sub-atomique', 'sub-atomique', 'sub-atomiques', 'sub-atomiques'],
 ['superfluide', 'superfluide', 'superfluides', 'superfluides'],
 ['supralumineux', 'supralumineuse', 'supralumineux', 'supralumineuses'],
 ['supraluminique', 'supraluminique', 'supraluminiques', 'supraluminiques'],
 ['tellurique', 'tellurique', 'telluriques', 'telluriques'],
 ['thermodynamique', 'thermodynamique', 'thermodynamiques', 'thermodynamiques'],
 ['topocentrique', 'topocentrique', 'topocentriques', 'topocentriques'],
 ['toroïdal', 'toroïdale', 'toroïdaux', 'toroïdales'],
 ['torique', 'torique', 'toriques', 'toriques'],
 ['transcendant', 'transcendante', 'transcendants', 'transcendantes'],
 ['transcendental', 'transcendentale', 'transcendentaux', 'transcendentales'],
 ['unifié','unifiée','unifiés','unifiées'],
 ['vectoriel', 'vectorielle', 'vectoriels', 'vectorielles'],
 ['vibrationnel', 'vibrationnelle', 'vibrationnels', 'vibrationnelles'],
 ['vibratoire', 'vibratoires', 'vibratoires', 'vibratoires'],
 ['virtuel', 'virtuelle', 'virtuels', 'virtueles'],
 ['vivifiant', 'vivifiante', 'viviviants', 'vivifiantes'],
 ['zététique', 'zététique', 'zététiques', 'zététiques']]

l_origine = ['de Planck', 'de Salomon', 'de Sion', 'de spin', 'de Tesla', 'de vie', 'du sous-Planck', 'd\'or']

# 0:masculin, 1:féminin, 2:pluriel masculin, 3:pluriel féminin
l_nom = \
[['', 'acupression', '', ''],
 ['', 'acupuncture', '', ''],
 ['ADN', '', '', ''],
 ['aimant circulaire', '', 'aimants circulaires', ''],
 ['', 'alchimie', '', 'alchmies'],
 ['amouron', '', 'amourons', ''],
 ['', '', '', 'anciennes civilisations'],
 ['', 'anomalie', '', 'anomalies'],
 ['anneau', '', '', ''],
 ['', 'apocalypse', '', ''],
 ['', 'aura', '', 'auras'],
 ['axiome', '', 'axiomes', ''],
 ['', 'base de données compilées', '', 'bases de données compilées'],
 ['', 'biodynamie', '', ''],
 ['', 'bio-énergétique', '', ''],
 ['bio-feedback', '', '', ''],
 ['', 'bio-fréquence', '', 'bio-fréquences'],
 ['bio-photon', '', 'bio-photons', ''],
 ['', 'bio-structure', '', 'bio-structures'],
 ['bit d\'information', '', 'bits d\'information', ''],
 ['boson', '', 'bosons', ''],
 ['bouclier', '', 'boucliers', ''],
 ['Bovis', '', 'Bovis', ''],
 ['', 'bulle de réalité', '', 'bulles de réalité'],
 ['', 'bulle univers', '', 'bulle univers'],
 ['cash-flow positif', '', '', ''],
 ['', 'cellule', '', 'cellules'],
 ['', 'cheminée cosmotellurique', '', 'cheminées cosmotelluriques'],
 ['champ', '', 'champs', ''],
 ['champ cohérent harmonique', '', '', ''],
 ['champ du point zéro', '', '', ''],
 ['champ d\'information', '', 'champs d\'information', ''],
 ['champ morphogénétique', '', 'champs morphogénétiques', ''],
 ['chakra', '', 'chakras', ''],
 ['chakra racine', '', '', ''],
 ['', 'cité de lumière', '', 'cités de lumière'],
 ['', 'confrérie', '', 'confréries'],
 ['', 'cohérence', '', ''],
 ['', 'conception', '', ''],
 ['', 'confrérie', '', 'confréries'],
 ['', 'confrérie secrète', '', 'confréries secrètes'],
 ['', 'conscience', '', ''],
 ['', 'conscience de soi', '', ''],
 ['contrôle de la gravité', '', '', ''],
 ['', 'corolle', '', 'corolles'],
 ['corps miroir', '', '', ''],
 ['', 'cosmologie', '', 'cosmologies'],
 ['cosmos', '', '', ''],
 ['', 'couleur vibratoire', '', 'couleurs vibratoires'],
 ['couplage', '', '', ''],
 ['créateur', '', '', ''],
 ['créateur de bonheur', '', '', ''],
 ['cristal', '', 'cristaux', ''],
 ['cristal de quartz', '', 'cristaux de quartz', ''],
 ['crop circle', '', 'crop circles', ''],
 ['cycle', '', 'cycles', ''],
 ['', '', 'cycles profonds', ''],
 ['', '', '', 'dernières techniques géochimiques'],
 ['', 'distorsion quantique', '', 'distorsions quantiques'],
 ['', 'distorsion', '', 'distorsions'],
 ['', 'dualité', '', ''],
 ['', 'dynamique', '', ''],
 ['échange informationnel', '', 'échanges informationnels', ''],
 ['', 'eau', '', ''],
 ['', 'eau informée', '', ''],
 ['', 'équation', '', 'équations'],
 ['équilibre', '', 'équilibres', ''],
 ['électromagnétisme', '', '', ''],
 ['', 'énergie', '', 'énergies'],
 ['', 'énergie du point zéro', '', 'énergies du point zéro'],
 ['', 'énergie du vide', '', 'énergies du vide'],
 ['', 'énergie vitale', '', 'énergies vitales'],
 ['', 'équation holographique', '', 'équations holographiques'],
 ['', '', 'enfants indigos', ''],
 ['épi-phéonomène', '', 'épi-phéonomènes', ''],
 ['espace-mémoire', '', '', ''],
 ['espace-temps', '', '', ''],
 ['', 'essence de la création', '', ''],
 ['extracteur de jus', '', 'extracteurs de jus', ''],
 ['', '', 'faits troublants', ''],
  ['', '', '', 'fleurs de Bach'],
 ['', 'fluctuation', '', 'fluctuations'],
 ['', 'fluctuation du vide', '', 'fluctuations du vide'],
 ['flux', '', 'flux', ''],
 ['flux d\'information', '', 'flux d\'information', ''],
 ['flux d\'information de la conscience', '', 'flux d\'information de la conscience', ''],
 ['', 'force', '', 'forces'],
 ['', 'force intérieure', '', ''],
 ['', 'fractale', '', 'fractales'],
 ['', 'fréquence', '', 'fréquences'],
 ['', 'fréquence correctrice', '', 'fréquences correctrices'],
 ['', 'fuite mentale', '', 'fuites mentales'],
 ['', 'gamme', '', 'gammes'],
 ['', 'géométrie', '', 'géométries'],
 ['harmonie', '', '', ''],
 ['', 'homéopathie', '', ''],
 ['hyper-espace', '', '', ''],
 ['', 'hyperbole', '', 'hyperboles'],
 ['hypercube', '', 'hypercubes', ''],
 ['', 'information', '', ''],
 ['', 'interaction', '', 'interactions'],
 ['', 'iridiologie', '', ''],
 ['', 'mécanique interne', '', ''],
 ['', 'lentille de Nimrod', '', ''],
 ['libre arbitre', '', '', ''],
 ['LIDAR', '', 'LIDARs', ''],
 ['', 'lune creuse', '', ''],
 ['manuscrit', '', 'manuscrits', ''],
 ['', 'matrice', '', 'matrices'],
 ['', 'matrice originelle', '', ''],
 ['mécanisme', '', 'mécanisme', ''],
 ['', 'médecine quantique', '', 'médecines quantiques'],
 ['', 'médoucine', '', 'médoucines'],
 ['mégalithe', '', 'mégalithes', ''],
 ['', 'mémoire', '', 'mémoires'],
 ['méridien', '', 'méridiens', ''],
 ['', 'méthode révolutionnaire', '', 'méthodes révolutionnaires'],
 ['', 'métrique', '', 'métriques'],
 ['micro-trou de ver', '', 'micro-trous de vers', ''],
 ['mindset', '', '', ''],
 ['mode', '', 'modes', ''],
 ['modèle Janus', '', '', ''],
 ['', 'molécule', '', 'molécules'],
 ['moteur à distorsion spatiale', '', 'moteurs à distorsion spatiale', ''],
 ['', 'mutation', '', 'mutations'],
 ['multivers', '', '', ''],
 ['mystère', '', '', ''],
 ['', 'nano-structure', '', 'nano-structures'],
 ['', '', '', 'nanotechnologies'],
 ['', 'naturopathie', '', ''],
 ['niveau', '', 'niveaux', ''],
 ['nombre d\'or', '', '', ''],
 ['oeuf', '', 'oeufs', ''],
 ['', 'onde', '', 'ondes'],
 ['', 'onde scalaire', '', 'ondes scalaires'],
 ['ordre bénédictin', '', 'ordres bénédictins', ''],
 ['', 'origine', '', 'origines'],
 ['oscillateur', '', 'oscillateurs', ''],
 ['oscillateur de Planck', '', 'oscillateurs de Planck', ''],
 ['', 'oscillation', '', 'oscillations'],
 ['paradigme', '', 'paradigmes', ''],
 ['', 'particule', '', 'particules'],
 ['pattern', '', '', ''],
 ['pendule', '', 'pendules', ''],
 ['photon', '', 'photons', ''],
 ['', 'physicalité', '', ''],
 ['', 'physique mondiale', '', ''],
 ['', 'pierre', '', 'pierres'],
 ['', 'pierre bleue', '', 'pierres bleues'],
 ['', 'pierre zététique', '', ''],
 ['plasma', '', 'plasmas', ''],
 ['point zéro', '', '', ''],
 ['', 'polarisation', '', 'polarisations'],
 ['positron', '', 'positrons', ''],
 ['principe fondamental', '', 'principes fondamentaux', ''],
 ['prisme', '', 'prismes', ''],
 ['processus', '', 'processus', ''],
 ['', 'propriété', '', 'propriétés'],
 ['', 'propriété originelle', '', 'propriétés originelles'],
 ['', 'protection', '', 'protections'],
 ['proton', '', 'protons', ''],
 ['', 'purification', '', ''],
 ['', 'qualité', '', 'qualités'],
 ['rayonnement', '', 'rayonnements', ''],
 ['rebirth', '', '', ''],
 ['reseau géométrique', '', 'reseaux géométriques', ''],
 ['', 'quadrature', '', ''],
 ['', 'radionique', '', ''],
 ['', '', 'radicaux libres', ''],
 ['', 'réalité', '', ''],
 ['', 'regéneration', '', ''],
 ['réseau', '', 'réseau', ''],
 ['réseau de trous de vers', '', 'réseaux de trous de vers', ''],
 ['résonateur', '', 'résonateurs', ''],
 ['résonateur de flux harmonique', '',  'résonateurs de flux harmonique', ''],
 ['', 'résonance', '', 'résonances'],
 ['rosaire sacré', '', 'rosaires sacrés', ''],
 ['', 'résonance', '', 'résonances'],
 ['', '', '', 'sensations'],
 ['septième chakra', '', '', ''],
 ['', 'signature vibratoire', '', 'signatures vibratoires'],
 ['', 'source', '', ''],
 ['', 'source d\'amour divin', '', ''],
 ['schéma', '', 'schémas', ''],
 ['séminaire', '', 'séminaires', ''],
 ['', 'sphère', '', 'sphères'],
 ['spin', '', 'spins', ''],
 ['', 'spire', '', 'spires'],
 ['', 'structure', '', 'structures'],
 ['', 'structure de l\'univers', '', ''],
 ['', 'structure du vide', '', 'structures du vide'],
 ['', 'structure rétroactive', '', 'structures rétroactives'],
 ['système corporel', '', '', ''],
 ['', '', 'systèmes évolutionnaires', ''],
 ['taux vibratoire', '', 'taux vibratoires', ''],
 ['', 'terre plate', '', ''],
 ['', 'terre creuse', '', ''],
 ['tesseract', '', '', ''],
 ['tetrahèdre', '', 'tetrahèdres', ''],
 ['tetrahèdron', '', '', ''],
 ['tetragain', '', 'tetragains', ''],
 ['thème astral', '', '', ''],
 ['', 'théorie', '', 'théories'],
 ['', 'théorie du champ unifié', '', 'théories du champ unifié'],
 ['', 'théosophie', '', ''],
 ['', '', '', 'toutes les âmes et toutes les plantes'],
 ['troisième oeil', '', '', ''],
 ['trou de vers', '', 'trous de vers', ''],
 ['vaisseau de lumière', '', 'vaisseaux de lumière', ''],
 ['', 'variable zêta', '', ''],
 ['', 'vérité', '', ''],
 ['', 'vérité de la réalité', '', ''],
 ['', 'vibration', '', 'vibrations'],
 ['', 'vibrologie', '', ''],
 ['vide', '', '', ''],
 ['vitaliseur', '', 'vitaliseurs', ''],
 ['', 'vitesse inimaginable', '', 'vitesses inimaginables'],
 ['vortex', '', 'vortex', ''],
 ['', '5D', '', ''],
 ['', '5G', '', '']]
       
l_nomG = \
[['corps subtil', '', '', ''],
 ['sceau', '', '', ''],
 ['', 'thérapie', '', 'thérapies'],
 ['', 'thérapie fréquentielle', '', '']]
       
l_nomD = \
[['bien-être', '', '', ''],
 ['corps physique', '', '', ''],
 ['', 'glande', '', 'glandes'],
 ['', 'glande pinéale', '', ''],
 ['', 'guérison', '', ''],
 ['', '', '', 'mitochondries'],
 ['', 'spiritualité', '', '']]

l_verbe = \
[['annule', 'annulent'],
 ['appréhende', 'appréhendent'],
 ['atteint', 'atteignent'],
 ['attire', 'attirent'],
 ['connecte', 'connectent'],
 ['confirme', 'confirment'],
 ['crée', 'créent'],
 ['délimite', 'délimitent'],
 ['démontre', 'démontrent'],
 ['déstabilise', 'déstabilisent'],
 ['développe', 'développent'],
 ['diffuse', 'diffusent'],
 ['divise', 'divisent'],
 ['éclaire', 'éclairent'],
 ['enrichit', 'enrichissent'],
 ['excite', 'excitent'],
 ['fond', 'fondent'],
 ['fracture', 'fracturent'],
 ['harmonise', 'harmonisent'],
 ['réalise', 'réalisent'],
 ['reconnecte', 'reconnectent'],
 ['rééquilibre', 'rééquilibrent'],
 ['régénère', 'régénèrent'],
 ['intrique', 'intriquent'],
 ['multiplie', 'multiplient'],
 ['nettoie', 'nettoient'],
 ['organise', 'organisent'],
 ['oxygène', 'oxygènent'],
 ['passe par', 'passent par'],
 ['polarise', 'polarisent'],
 ['protège', 'protègent'],
 ['purifie', 'purifient'],
 ['réharmonise', 'réharmonisent'],
 ['restructure', 'restructurent'],
 ['résoud', 'résolvent'],
 ['révèle', 'révèlent'],
 ['soutient', 'soutiennent'],
 ['stabilise', 'stabilisent'],
 ['structure', 'structurent'],
 ['synchronise', 'synchronisent'],
 ['transcende', 'transcendent'],
 ['transmute', 'transmutent'],
 ['unifie', 'unifient'],
 ['vivifie', 'vivifient']]

l_gverbal = \
[['booste le système immunitaire'],
 ['boostent le système immunitaire']]

l_introduction = \
['Comme le disait Einstein, tout est relatif. En effet, ',
 'Selon les découvertes d\'une prestigieuse université américaine, ',
 'J\'ai une ce moment de révélation : ',
 'Ce qu\'il est important de comprendre, c\'est que ',
 'Mais oui c\'est clair ! ',
 'J\'ai passé la majeure partie de ma vie à faire des recherches. ',
 'Selon les experts, ',
 'Ce que nous soutenons, et non sans raison, c\'est que ',
 'Je suis journaliste scientifique. ',
 'Je suis docteur en mathématiques. ',
 'Depuis la nuit des temps, ',
 'Nous ne sommes pas fous : ',
 'Avec du recul, la seule chose dont je suis sûr, c\'est que ',
 'Si les recherches peuvent nous prouver ce qu\'il nous dit, ',
 'Faites vos propres recherches : ',
 'J\'ai écrit les équations : ',
 'Vous voyez de manière évidente que ',
 'Ces études le démontrent clairement. ',
 'Selon la resonance academy, ',
 'La théorie quantique est incomplète dans sa compréhension de la matière. ',
 'Cette information ne constitue pas une théorie standard, mais ',
 'Je ne sais pas pour vous mais dans ma vie, ',
 'Les théories que nous avons en ce moment sont incomplètes : ',
 'Tous les physiciens l\'admettent : ',
 'À un niveau très profond, ',
 'Les autorités ne veulent pas que vous le sachiez, mais ',
 'Prenez de quoi noter : ',
 'Ce que votre médecin vous cache, c\'est que ',
 'Nos équations le démontrent clairement, ',
 'La nature révele de nombreuses solutions. ',
 'Cette technologie antique laisse les scientifiques sans voix : ',
 'Selon la science unifiée, ',
 'J\'ai conscience que ces belles équations mathématiques peuvent être difficiles à comprendre pour certains, cependant ',
 'J\'ai écrit plusieurs articles scientifiques qui emmènent les mathématiques à un niveau supérieur. ',
 'Il ne contredit pas les lois de la physique de penser que ',
 'je suis coach en NOM_ADJECTIF et j\'affirme que '
]

l_conclusion = \
['Et cela intrigue les scientifiques du monde entier',
 'L\'univers ne fait pas ça',
 'Ce sera dans mon prochain film',
 'Tout cela est très sérieux',
 'Cela est particulièrement impressionnant',
 'Et ce phénomène intrigue les physiciens depuis des millions d\'années',
 'Les trolls me haïssent pour cela',
 'Et jusqu\'à ce jour, cela reste inexpliqué',
 'C\'est une vérité scientifique',
 'C\'est extrèmement troublant',
 'Cela m\'a été révélé',
 'Je ne suis pas physicien, mais c\'est ce que je peux en dire.',
 'C\'est mathématique',
 'Je ne suis pas attaquable, je ne suis pas thérapeute',
 'Il y a des gens qui réfléchissent, quand même',
 'Tout cela nous démontre quelque chose de profond',
 'Faites vos propres recherches',
 'Cela pourrait avoir un énorme impact pour l\'humanité',
 'Ce phénomène est loin d\'être un cas isolé',
 'C\'est quelque chose que j\'ai compris intuitivement',
 'En tant que messie, je suis vecteur de cette clef que j\'ai découverte sur mon chemin de vie',
 'Mais les choses sont en train de changer',
 'Ces révélations proviennent d\'une quête qui durera plus de 10 ans',
 'C\'est la base de beaucoup de mes recherches',
 'C\'est évident si on se base sur ce que j\'ai découvert',
 'C\'est confirmé par des études expérimentales',
 'Ça se construit et se connecte tout seul',
 'N\'attendez plus pour reprendre votre santé en main',
 'Et cela nous emmène vers la théorie de l\'unification des forces',
 'Et cela va nous permettre de vivre le monde supralumineux du libre-arbitre',
 'Et cela déroute encore les archéologues',
 'Ce qui laisse les chercheurs totalement perplexes face à une telle technologie',
 'Et cela est encore peu connu du grand public',
 'Certaines personnes ont essayé de me faire taire',
 'La science officielle se refuse à reconnaître ces phénomènes']

l_adverbe = \
['énergétiquement']

def pickrandom_in_list (l):
    i = random.randint(0,len(l)-1)
    return l[i], i

# pick random item in list of lists
# return item and index of its list
def pickrandom (ll):
    ok = False
    while not(ok):
        ii = random.randint(0,len(ll)-1)
        item, i = pickrandom_in_list (ll[ii])
        ok = (item != '')
    return item, i

def pickrandom2 (ll, i):
    ok = False
    while not(ok):
        ii = random.randint(0,len(ll)-1)
        item = ll[ii][i]
        ok = (item != '')
    return item

def necessite_article_contracte (mot):
    p = mot[0]
    voyelles = "àaeéèêhiouyAEHIOUY"
    return p in voyelles

def article_defini (mot, genre):
    if necessite_article_contracte (mot):
        return l_article_defini[1][genre]
    else:
        return l_article_defini[0][genre]
    
def article_indefini (mot, genre):
    if necessite_article_contracte (mot):
        return l_article_indefini[1][genre]
    else:
        return l_article_indefini[0][genre]
    
def article_partitif (mot, genre):
    if necessite_article_contracte (mot):
        return l_article_partitif[1][genre]
    else:
        return l_article_partitif[0][genre]

def nom_adjectif ():
    (nom, genre) = pickrandom (l_nom + l_nomG)
    adjectif = pickrandom2 (l_adjectif, genre)
    return nom + " " + adjectif
    
# Read command line parameters (cf https://docs.python.org/fr/3/howto/argparse.html)
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--cow", help="use cowsay to display", action="store_true")
parser.add_argument("-s", "--tts", help="enable text to speech", action="store_true")
parser.add_argument("--cowfile", help=".cow")
args = parser.parse_args()

# Init random seed
random.seed()

# Build sentence
(introduction, i) = pickrandom_in_list (l_introduction)
introduction = introduction.replace ("NOM_ADJECTIF", nom_adjectif())
(sujet, genreS) = pickrandom (l_nom + l_nomG)
if (random.random() > 0.5):
    articleS = article_defini (sujet, genreS)
else:
    articleS = article_indefini (sujet, genreS)
if (random.random() > 0.9):
    adjectifS,i = pickrandom_in_list (l_dunompropre)
else:
    adjectifS = pickrandom2 (l_adjectif, genreS)
if (genreS>1):
    plur = 1
else:
    plur = 0
verbe = pickrandom2 (l_verbe, plur)
(cod, genreCOD) = pickrandom (l_nom + l_nomD)
articleCOD = article_defini (cod, genreCOD)
if (random.random() > 0.9):
    adjectifCOD,i = pickrandom_in_list (l_dunompropre)
else:
    adjectifCOD = pickrandom2 (l_adjectif, genreCOD)
(conclusion, i) = pickrandom_in_list (l_conclusion)

s = ''
if (random.random() > 0):
    s = introduction
match = re.search("[\.!] $", introduction)
if match:
    s += articleS.capitalize ()
else:
    s += articleS
s += sujet
s += ' '
s += adjectifS
s += ' '
s += verbe
s += ' '
s += articleCOD
s += cod
s += ' '
s += adjectifCOD
s += '.'

if (random.random() > 0.6):
    s += ' '
    s += conclusion
    s += '.'

# Display sentence
if args.cow:
    if (args.cowfile):
        os.system ("cowsay -W 60 -f " + args.cowfile + " \"" + s + "\"")
    else:
        os.system ("cowsay -W 60 \"" + s + "\"")
else:
    print (s)
if args.tts:
    os.system ("tts-fr " + "\"" + s + "\"")
