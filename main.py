
#!/usr/bin/python

import sys
from datetime import datetime



#----------------------------------------------------------------------------------------------------------


def ecrisListe(liste):
	res = "["
	for i in liste:
		res = res + str(i)
		if not(i == liste[-1]):
			res = res + ","
	res = res + "]"
	return res


class EnchereItemHdv:
	def __init__(self, prix1, prix2, prix3):
		self.idVente = ""
		self.stats = [("force",0)] # liste de couple [(str,int)], 1er elem c'est als stat deuxieme la valeur
		self.prix1 = prix1
		self.prix2 = prix2
		self.prix3 = prix3

	def __str__(self):
		#statsStr = map(lambda (nm,val):(ecrisStr(nm),val),(self.stats)) 
		return "(" + self.idVente + "," + self.prix1 + "," + self.prix2 + "," + self.prix3 + "," + ecrisListe(self.stats) + ")"

class ListeEnchereItemHdv:
	def __init__(self, nom, listeEnchere):
		self.nom = nom
		self.date = ""
		self.prixMoyen = -1
		#liste d objets de la classe enchere
		self.listeEnchere = listeEnchere

	def __str__(self):
		now = datetime.now()
		nowStr = now.strftime("(%Y,%m,%d,%H,%M,%S)")
		res = "("
		res = res + self.nom + ","
		res = res + nowStr + ","
		res = res + str(self.prixMoyen) + ","
		res = res + ecrisListe(self.listeEnchere)
		res = res + ")\n"
		return res


#------------------------------------------------------------------------------------------------------------------------


def ouvreFichierEtStockeListe(nomFichier):
	strFich = open(nomFichier, "r")
	res = strFich.readlines()
	strFich.close()
	return res

def ecrisFichier(contenu,nomFichier):
	f = open("datasDofus/" + nomFichier, "a")
	f.write(contenu)
	f.close()


#---------------------------------------------------------------------------------------------------------------------

#Prend que els mesasgeq ui commencent par ip ankama et enlever l ip au debut
def triMsgIp172(listeLog):
	res = []
	for i in listeLog:
		if i[:3] == "172" : 
			res.append(i.split(":",1)[1])
	return res

def corrige(ligne):
	while ligne[-2:] != ";." and ligne != "":
		ligne = ligne[:-1]
	if ("GDE" in ligne) or ("cMK" in ligne) or ("GM" in ligne) or ("GDF" in ligne) or ("EHP" in ligne):
		ligne = ligne[:-1]
		ligne = corrige(ligne)
	return ligne


# attention aux " " avant le nom de la requete, renvoie touite la chaine apres le nom de la requete
def selectRequete(idRequete,listeSansIp):
	longueur = len(idRequete)
	res = []
	for i in listeSansIp:
		if i[:longueur] == idRequete:
			tmp = i[longueur:]
			tmp = corrige(tmp)
			if tmp != "":
				res.append(tmp)
	return res


#---------------------------------------------------------------------------------------------------------------------


#parse la vente numero index item de l enchere resLigneRequete
def parseUneVente(stringLogVente):
	splittage = stringLogVente.split(";")
	prix1 = splittage[2]
	prix2 = splittage[3]
	prix3 = splittage[4]
	return EnchereItemHdv(prix1,prix2,prix3)

# prend le resultat d une ligne de requete item et cree une listeEnchereItemhdv
def parseItem(resLigneRequete):
	splittage = resLigneRequete.split("|")
	nom = splittage[0]
	venteParse = []
	for i in splittage[1:]:
		venteParse.append(parseUneVente(i))
	return ListeEnchereItemHdv(nom,venteParse)





#------------------------------------------------------------------------------------------

testOuvreFichier = ouvreFichierEtStockeListe("packets.log")

testTriMsg = triMsgIp172(testOuvreFichier)

testSelectRequete = selectRequete(" EHl",testTriMsg)

#--------------------------------------------------



def parseFichier():
	res = ""
	for i in testSelectRequete:
		testParse = parseItem(i)
		ecrisFichier(str(testParse),testParse.nom + ".data") 

parseFichier()








#print(testSelectRequete[10])
#test2 = (parseUneVente(testSelectRequete[0],0))







