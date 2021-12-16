import os
import sys

class Facade:
    def __init__(self) :
        self.gestionnaireMagasin = None
        self.gestionnaireMouillage = None

    def getMouillage(self):
        mouillageForVue = mouillageViewMouillage()
        #flotteur
        flotteur = ElementViewMouillage(100,"FSAB 1200",1.25,"\Pictures\Floats\FSAB 1200.bmp",False,486)
        mouillageForVue.add(flotteur)
        #terminal
        terminal = ElementViewMouillage(101.25,"Shackle5/8",0.05,"\Pictures\Terminals\shackle2.bmp",False,-0.635)
        mouillageForVue.add(terminal)
        #rope
        rope1 = ElementViewMouillage(101.30,"Dyneema 6mm",1000,"\Pictures\Ropes\cable.bmp",False,0.0005)
        mouillageForVue.add(rope1)

        return mouillageForVue

class mouillageViewMouillage:
    def __init__(self) :
        self.elements = list()

    def add(self,elementViewMouillage):
        self.elements.append(elementViewMouillage)
        return self

class ElementViewMouillage:
    def __init__(self,position,nom,longueur,image,isClampe,poid) :
        self.position = position
        self.nom = nom
        self.longueur = longueur
        self.image = image
        self.isclampe = isClampe
        self.poid = poid
