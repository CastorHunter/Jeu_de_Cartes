class Carte :

    def __init__(self, coutmana = 0, nom = "Creature", description = ""):
        self.__coutmana = coutmana
        self.__nom = nom
        self.__description = description

    def getCoutmana(self):
        return self.__coutmana

class Mage :

    def __init__(self, totalmana, nom, pv, main = []):
        self.__mana = totalmana
        self.__totalmana = totalmana
        self.__nom = nom
        self.__pv = pv
        self.__defausse = []
        self.__main = main
        self.__zonedejeu = []
        self.__type = "mage"

    def jouerCarte(self, carte, ennemi):

        if int(carte.getCoutmana()) < self.__mana :
            self.__mana -= carte.getCoutmana()
            for i in range(len(self.__main)):
                if self.__main[i] == carte :
                    self.__zonedejeu.append(self.__main.pop(i)) 
            if carte.getType() == "cristal" :
                self.__totalmana += carte.getValeur()
            elif carte.getType() == "creature" :
                carte.attaquer(ennemi)
            elif carte.getType() == "blast" :
                ennemi.perdrePv(carte.getValeur())
                self.__defausse.append(self.__zonedejeu.pop(i)) 
                
    def recupererMana(self):
        self.__mana = self.__totalmana

    def augmenterMana(self, nmana):
        self.__totalmana += nmana

    def perdrePv(self, dmg):
        self.__pv -= dmg

    def getPv(self):
        return self.__pv
    
    def getZonedeJeu(self):
        return self.__zonedejeu

    def getMana(self):
        return self.__mana
    
    def getType(self):
        return self.__type

class Cristal(Carte) :

    def __init__(self, coutmana, nom, description, valeur):
        super().__init__(nom, description, coutmana)
        self.__valeur = valeur
        self.__type = 'cristal'

    def getValeur(self):
        return self.__valeur
    
    def getType(self):
        return self.__type
    

class Creature(Carte) :


    def __init__(self, coutmana, nom, description, pv, dmg):
        super().__init__(nom, coutmana, description)
        self.__dmg = dmg
        self.__pv = pv
        self.__type = 'creature'

    def getPV(self):
        return self.__pv

    def perdrePv(self, dmg):
        self.__pv -= dmg

    def getType(self):
        return self.__type
    
    def getAttaque(self):
        return self.__dmg
    
    def getDmg(self):
        return self.__dmg
    
    def attaquer(self, ennemi):
        ennemi.perdrePv(self.__dmg)
        if ennemi.getType() == "creature":
            self.perdrePv(ennemi.getDmg())

    
class Blast(Carte) :

    def __init__(self, coutmana, nom, description, valeur):
        super().__init__(nom, description, coutmana)
        self.__valeur = valeur
        self.__type = 'blast'
    
    def getValeur(self):
        return self.__valeur
    
    def getType(self):
        return self.__type
    
###################################################################
###########################_Bataille_##############################
###################################################################

#programme non terminé
'''

Troll1 = Creature("Troll", 500, "Un troll agressif", 200, 5000000)
Troll2 = Creature("Troll", 500, "Un troll agressif", 200, 50)

Zex = Mage(1000, "Zex", 1000, [Troll1])
Hagan = Mage(1500, "Hagan", 700, [Troll2])

Carteajouer = Troll1
Ennemiaattaquer = Hagan
while Zex.getPv()>0 and Hagan.getPv()>0:
    Zex.jouerCarte(Carteajouer,Ennemiaattaquer)
    if Zex.getZonedeJeu() != []:
        for i in range (len(Zex.getZonedeJeu())):
            if Zex.getZonedeJeu()[i].getType() == "cristal" :
                Zex.augmenterMana(Zex.getZonedeJeu()[i].getValeur())
            elif Zex.getZonedeJeu()[i].getType() == "creature" :
                Zex.getZonedeJeu()[i].attaquer(Ennemiaattaquer)

'''