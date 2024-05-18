#!/usr/bin/python
# -*- coding: utf-8 -*-
# *****************************************************************************
# Host          : centroleninae
# File          : genpanther.py
# Author        : ALX
# Creation      : 2019-04-07
# Last Revision : 2019-05-10
# Release       : V1.06
# Description   : Générateur de panthère
# *****************************************************************************

import os, sys
import random

witz = ["Je suis à deux doigts de décompenser","xkill",
        "La vision nocturne","xeyes",
        "C'est du pénal","cgam.py",
        "Trouble à l'ordre public","eog /usr/local/bin/bearlik1.jpg"]

phrases = ["La vision globale",
           "Cherche pas, on y est",
           "Les aspergers, on les utilise en Israël",
           "Une balle, un mort",
           "Papier, crayon",
           "Tout simplement",
           "C'est parfaitment rationnel",
           "Ni plus, ni moins",
           "Exactement",
           "Tout simplement",
           "Merci, tu m'as bien aidée",
           "Cherche pas, t'as vu un lynx",
           "Malplaquet, c'est des mormons",
           "Le café, c'est mon anxiolytique",
           "Ni plus, ni moins",
           "Action, réaction !",
           "Merci, tu m'as bien aidée",
           "Au micron !"]

inventions = ["Le four à micro-ondes",
              "La diode électroluminescente",
              "La pile",
              "Le filament",
              "Le programme spatial",
              "Le projet Manhattan",
              "Le gauffrier",
              "La pilule contraceptive",
              "L'ordinateur quantique",
              "Le tokamak",
              "Le thermomix",
              "L'antenne parabollique",
              "Le mouvement perpétuel",
              "L'énergie libre",
              "Le cyclotron",
              "L'électrophorèse",
              "La stimulation transcrânienne",
              "Le bypass",
              "La greffe de tête",
              "Le projet HAARP",
              "Les chemtrails",
              "Les missiles ballistiques",
              "L'alidade de tir vertical",
              "La machine à vapeur",
              "Le nombre d'or",
              "Les proportions stoechiométriques",
              "La gravité quantique à boucle",
              "Les liaisons covalentes",
              "L'échelle",
              "Le syndrome",
              "La navette spatiale",
              "La scie à onglet",
              "Le télescope",
              "Le pangolin",
              "L'auto-cuiseur",
              "Les hybrides F1",
              "Le grand confinement",
              "La mandragore",
              "La presse hydraulique",
              "Le bon sens populaire",
              "Le Nouvel Ordre Mondial",
              "L'expérience",
              "le FAMAS",
              "L'électrolyse",
              "Le bassin de l'emploi",
              "La mémoire de l'eau",
              "La poussée",
              "La myxomatose",
              "Le pain",
              "La décompensation",
              "La crise de la quarantaine",
              "La forge",
              "L'autisme",
              "L'effet photo-électrique",
              "Le syndrôme",
              "Le gazoduc",
              "La pierre philosophale",
              "La prise PERITEL",
              "La dynamite",
              "La craquette",
              "Le brun-brun",
              "Le polynôme",
              "La révolution",
              "L'effet Venturi",
              "Le WD-40",
              "Les pastilles d'iode",
              "Le papyrus",
              "Les momies",
              "Le métamorphe",
              "La vis sans fin",
              "Les propriétés quantiques"]

localite = ["d'Alexandrie",
            "de Syracuse",
            "d'Israël",
            "de Sparte",
            "de la zone 51",
            "de l'empire Maya",
            "de Babylone",
            "de la dynastie Ming",
            "de Mésopotamie",
            "de l'Atlantide",
            "des Aztèques",
            "de Ramsès II",
            "d'Akenaton",
            "des Vikings",
            "des anciens architectes",
            "des hommes-lézards",
            "de Vladimir Poutine",
            "de Tesla",
            "des camps FEMA",
            "des rats-taupes-nus",
            "des tardigrades",
            "de Tchernobyl",
            "de Pripyat",
            "d'Hiroshima",
            "de Stockholm",
            "de Stendhal",
            "de Geodis",
            "du Struthof",
            "de Varicor",
            "de Jacob",
            "de la Bruche",
            "des pinpins",
            "des alchimistes",
            "de Milgram",
            "d'Alfred Nobel",
            "d'Archimède",
            "de Monsanto",
            "des pyramides",
            "de l'Acropole",
            "de Constantinople",
            "de Rambo",
            "de Persépolis",
            "de Birkenau",
            "de Jérusalem",
            "de Judée-Samarie",
            "de Gaza",
            "du docteur Simonin",
            "des pharaons",
            "de Kheops",
            "de Nazca",
            "du réseau Arpanet"]

random.seed()

n = random.randint(0,9)

if (n == 0):
    i = random.randint(1,len(witz)/2)-1
    s = witz [2*i]
    print s
    os.system(witz[2*i+1])
    
if (n == 1):
    s = phrases [random.randint(0,len(phrases)-1)]
    print s
    
if (n > 1):
    s1 = inventions [random.randint(0,len(inventions)-1)]
    s2 = localite [random.randint(0,len(localite)-1)]
    s = s1 + " " + s2
    print s
