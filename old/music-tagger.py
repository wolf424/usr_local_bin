#!/usr/bin/python
# -*-coding:Latin-1 -*
# music-tagger ************************************************************************

from Tkinter import *
import os
from datetime import datetime

master = Tk()

def var_states():
  text = str("")
  for j in range(nbcol):
    for i in range(nblgn[j]):
      if i>0:
        if var[j][i].get()>0:
          text=text+titre[j][i]
  maintenant = datetime.now()
  text=text+"\n[MP3Tagger:"+str(maintenant.year)+"-"+str(maintenant.month)+"-"+str(maintenant.day)+"]";
  print("%s" % (text))
  r = Tk()
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(text)
  r.destroy()      
def query_winamp():
  text = str("")
  first = 1
  for j in range(nbcol):
    for i in range(nblgn[j]):
      if i>0:
        if var[j][i].get()>0:
          if first>0:
            first=0
          else:
            text = text + " AND "
          text = text + "comment HAS \"" + titre[j][i] + "\""
  print("%s" % (text))
  r = Tk()
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(text)
  r.destroy()      
  
def playlist():
  text = str("")
  for j in range(nbcol):
    for i in range(nblgn[j]):
      if i>0:
        if var[j][i].get()>0:
          pattern = titre[j][i]
          pattern = pattern.replace("[","\\[")
          pattern = pattern.replace("]","\\]")
          pattern = pattern.replace("+","\\+")
          pattern = pattern.replace("<","\\<")
          pattern = pattern.replace(">","")
          pattern = pattern.replace("$","\\\\$")
          text = text + "\"" + pattern + "\" "
  r = Tk()
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(text)
  r.destroy()      
  repository = "/mnt/music.s/jukebox"
  print ("music-searchtag.py \"" + repository + "\" " + text)
  os.system ("music-searchtag.py \"" + repository + "\" " + text)

def clearoptions():
  for j in range(nbcol):
    for i in range(nblgn[j]):
      if i>0:
        var[j][i].set(0)

titre=[
    ["NOTE","$","$$","$$$","$$$$","$$$$$"],
    ["USAGE","[bdsm1]","[bdsm2]","[bdsm3]","[#sunyata]","[#shiva]","[#chirps]","[#inanna]","[#cthulhu]","[#mother]","[#mouche]","[#tarantella]","[#lmnbarb]","[#medElec]","[#flowerpower]"],
    ["TAGS","<Def+>","<Def++>","<Calm+>","<Calm++>","<Dark+>","<Dark++>","<Deep+>","<Deep++>","<Goth+>","<Goth++>","<Humour+>","<Humour++>","<Live+>","<Live++>","<Medit+>","<Medit++>","<Psy+>","<Psy++>"],
    ["REGIONS","[BLK]","[CLT]","[ORI]","[TZI]","[LAT]","[ENG]"],
    ["SS-GENRE","[blues]","[marche]","[ragga]","[tango]","[valse]","[wave]"],
    ["AMBIANCE","[aerien]","[baroque]","[chillout]","[equestre]","[kitsch]","[martial]","[medieval]","[religieux]","[sensuel]","[solennel]","[tribal]","[30s]","[70s]","[80s]","[love]"],
    ["EFFETS","[acid]","[arpegiateur]","[climax]","[distorsion]","[drones]","[enveloppe]","[groove]","[hypnotique]","[nappes]","[nokick]","[reverb]","[uplifting]","[vocaltrance]"],
    ["INSTRUMENTS","[basse]","[batterie]","[choeur]","[guitare]","[harmonica]","[orchestre]","[orgue]","[piano]","[trompette]","[violon]","[vocal]","[vocal+]","[vocodeur]","[scratch]","[wahwah]"],
    ["THEME","[drug]","[alcool]","[ecstasy]","[heroine]","[lgbt]","[sex]","[flowerpower]"],
    ["AUTORADIO","[autoradio]"],
    ["(AUTRES)","MND Europe de l'Ouest / France","MND Europe de l'Ouest / Allemagne","MND Amérique du Nord / USA","MND Europe de l'Ouest / Grande-bretagne","MND Europe de l'Est / Russie","#"]
    ]

var=[]
nbcol=len(titre)
nblgn=[]
for j in range(nbcol):
  nblgn.append(len(titre[j]))
  var.append([])

for j in range(nbcol):
  for i in range(nblgn[j]):
    var[j].append(0)

  for i in range(nblgn[j]):
    if i>0:
      var[j][i] = IntVar()
      Checkbutton(master, text=titre[j][i], variable=var[j][i]).grid(column=j+1, row=i+1, sticky=W)
    else:
      Label(master, text=titre[j][i]).grid(column=j+1, row=i+1, sticky=W)
  
Button(master, text='Quit', command=master.quit).grid(column=0, row=1, sticky=W, pady=4)
Button(master, text='Clear', command=clearoptions).grid(column=0, row=2, sticky=W, pady=4)
Button(master, text='Query Winamp', command=query_winamp).grid(column=0, row=3, sticky=W, pady=4)
Button(master, text='Copy', command=var_states).grid(column=0, row=4, sticky=W, pady=4)
Button(master, text='->playlist', command=playlist).grid(column=0, row=5, sticky=W, pady=4)
mainloop()
