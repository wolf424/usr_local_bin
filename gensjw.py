#!/usr/bin/python
# -*- coding: utf-8 -*-
# *****************************************************************************
# Host          : sarbecovirus
# File          : gensjw.py
# Author        : ALX
# Creation      : 2020-07-13
# Last Revision : 2020-07-18
# Release       : V1.02
# Description   : Générateur SJW
# *****************************************************************************

import os, sys
import random

phrases = ["On ne peut pas dissocier l'artiste de son oeuvre"]

intro1 = ["En tant que cis,",
          "En tant que non-racisé.e",
          "Nan mais là,",
          "Non mais juste,",
          "C'est trop abusé,",
          "Nan mais genre",
          "Ben tu vois, ce que tu fais là,",
          "Je refuse de discuter avec toi,",
          "Cette pratique a un nom :",
          "Ca me dég,",
          "T'as pas honte,",
          "Je me désolidarise des personnes comme toi,",
          "Ça me trigger,",
          "Je supporte trop pas,",
          "Tu te rends compte que",
          "OK Boomer,",
          "All men are trash,",
          "C'est de la réappropration,",
          "C'est de la récupération",
          "Tu te réappropries le mouvement,",
          "Ca va la fachosphère ?",
          "C'est la culture du viol,"]

intro2 = ["ceux sont des personnes dans ton genre qui répandent le",
          "tu entretiens la culture du",
          "c'est complètement du",
          "c'est trop du",
          "tu cherches à faire du",
          "bravo avec ton",
          "tu fais du",
          "ils utilisent nos habitudes de",
          "c'est du",
          "ce système est entré dans une ère de",
          "tu pratiques le",
          "ça s'appelle du",
          "ces personnes là alimentent le"]

mot1 = ["neuro",
        "man",
        "woman",
        "LGBTTQQIAAP+*",
        "victim",
        "gender",
        "age",
        "alter",
        "bi",
        "cis",
        "class",
        "econo",
        "fat",
        "hétéro",
        "homo",
        "slut",
        "TERF",
        "trigger",
        "cuck",
        "shit",
        "antifa",
        "green",
        "minority",
        "neuro-a",
        "bold-head",
        "nazi",
        "grosso",
        "slut",
        "straight",
        "white",
        "queer",
        "SJW",
        "body",
        "safe-place",
        "WASP",
        "intentional",
        "meta",
        "passive-agressive",
        "not-all-men",
        "additionnal",
        "TDS"]

mot2 = ["spreading",
        "splaining",
        "blinding",
        "propriating",
        "racialism",
        "sexism",
        "triggering",
        "warning",
        "ceiling",
        "derailling",
        "facism",
        "shaming",
        "slamming",
        "terrupting",
        "specism",
        "policing",
        "blaiming",
        "posting",
        "washing",
        "assaulting",
        "crossing",
        "talking",
        "reporting",
        "signaling",
        "centrism",
        "colonialism",
        "degendering",
        "patriarcat",
        "classism",
        "silencing",
        "traditionalism",
        "bashing",
        "overlooking",
        "listing",
        "flooding",
        "branding",
        "abolitionism",
        "assignating",
        "raping"]

random.seed()

i1 = intro1 [random.randint(0,len(intro1)-1)]
i2 = intro2 [random.randint(0,len(intro2)-1)]
m1 = mot1 [random.randint(0,len(mot1)-1)]
m2 = mot2 [random.randint(0,len(mot2)-1)]
connard = i1 + " " + i2 + " " + m1 + "-" + m2
print connard
