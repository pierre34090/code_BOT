#Import
import sys





#Duree des waits

p = 0.3
m = 0.5
g = 1
h = 3


#Variable Globales

def crash():
    print(Region(365,13,74,49).find(Region(2816,1130,613,72)).getScore())


#Dans le menu hdv

#cartouche Pos menu déroulant

rCartouchePosG = Region(2391,401,28,555)
#menuGx contient la ligne x vignette exclue de haut en bas
rMenuG1 = Region(1954,418,26,10)
rMenuG2 = Region(1975,464,24,15)
rMenuG3 = Region(1994,508,15,10)
rMenuG4 = Region(2025,556,28,10)
rMenuG5 = Region(2000,602,21,11)
rMenuG6 = Region(2052,648,9,6) 
rMenuG7 = Region(1993,696,16,11)
rMenuG8 = Region(2025,740,9,15)
rMenuG9 = Region(2002,785,16,11)
rMenuG10 = Region(2019,838,14,9)
rMenuG11 = Region(2025,882,14,12)
rMenuG12 = Region(2040,931,10,14)
rMenuGListe = [rMenuG1,rMenuG2,rMenuG3,rMenuG4,rMenuG5,rMenuG6,rMenuG7,rMenuG8,rMenuG9,rMenuG10,rMenuG11,rMenuG12]
#objet pris sur le menu déroulant gauche
rCat = Region(2064,349,19,8)

#Menu déroulant des catégories de haut en bas, à prendre sur l hdv ressource
rCat1 = Region(2025,391,18,14)
rCat2 = Region(2041,444,13,10)
rCat3 = Region(2074,485,10,13)
rCat4 = Region(2034,536,11,8)
rCat5 = Region(2040,582,19,10)
rCat6 = Region(2043,628,22,10)
rCat7 = Region(2031,676,23,6)
rCat8 = Region(2049,722,33,9)
rCat9 = Region(2055,769,25,7)
rCat10 = Region(2046,815,20,9)
rCatListe = [rCat1,rCat2,rCat3,rCat4,rCat5,rCat6,rCat7,rCat8,rCat9,rCat10]





#Tests

rTestMenuEsc = Region(2328,421,503,401)

capTestMenuEsc = "capMenuEsc.png"
rTestSousMenuEsc = Region(2627,679,236,42)
capTestSousMenuEsc = "capTestSousMenuEsc.png"

rTestMenuHdv = Region(1773,185,624,45)
capTestMenuHdv = "capTestMenuHdv.png"
rTestMilice = Region(2103,148,953,225)
capTestMilice = "capTestMenuZaapi.png"





    
def suisJeEsc():
    try:
        print("Res test d'esc")
        print(rTestMenuEsc.find(capTestMenuEsc).getScore())
        return rTestMenuEsc.find(capTestMenuEsc).getScore()>0.9
    except:
        return False

def suisJeSousMenuEsc():
    try:
        print("Res test sous menu esc")
        print(rTestSousMenuEsc.find(capTestSousMenuEsc).getScore())
        return rTestSousMenuEsc.find(capTestSousMenuEsc).getScore()>0.9
    except:
        return False
    
def suisJeMenuHdv():
    try:
        print("Res test MenuHdv")
        print(rTestMenuHdv.find(capTestMenuHdv).getScore())
        return rTestMenuHdv.find(capTestMenuHdv).getScore()>0.9
    except:
        return False

def suisJeMenuZaapiMilice():
    try:
        print("Res test zaapiMilice")
        print(rTestMilice.find(capTestMilice).getScore())
        return rTestMilice.find(capTestMilice).getScore()>0.9
    except:
        return False

def scroll2(cartouchePos,wheelDir):
    mouseMove(cartouchePos)
    prev = capture(cartouchePos)
    wheel(wheelDir, 1)
    sleep(0.1)
    try:
        return (cartouchePos.find(prev).getScore() > 0.99)
    except:
        return False
    
def scrollToutEnHaut(cartouchePos):
    i = 0
    while(not(scroll2(cartouchePos,WHEEL_UP))):
        i = i + 1

def crashTestHdv():
    if suisJeMenuHdv() :
        print("je suis bien en menu hdv")
    else:
        crash()

def litMenuGauche():
    crashTestHdv()
    sleep(m)
    click(rMenuG1)
    sleep(p)
    scrollToutEnHaut(rCartouchePosG)
    #On lit les 3 premiers
    i = 0
    while (i < 3):
        click(rMenuGListe[i])
        sleep(m)
        i = i + 1
        
    #On scroll, à chaque itération, on lit les 3 premiers    
    i=0
    while(not(scroll2(rCartouchePosG,WHEEL_DOWN))):
        i = 0
        crashTestHdv()
        while (i < 3):
           click(rMenuGListe[i])
           sleep(p)
           i = i + 1
    #On a fini, on lit les 7 derniers
    i = 3
    crashTestHdv()
    while (i < 12):
        click(rMenuGListe[i])
        sleep(p)
        i = i + 1   

def litMenuCat (nbCat):
    i=0
    #lit le début
    while((i < nbCat) and (i < 10)):
        sleep(p)
        click(rCat)
        sleep(p)
        click(rCatListe[i])
        sleep(p)
        litMenuGauche()
        sleep(p)
        i = i + 1
    #scroll et lit jusqu à al fin (potentiellement on lit deux fois les derniers)
    nbScroll = 1 
    while ( i < nbCat):
        click(rCat)
        sleep(p)
        mouseMove(rCat1)
        sleep(p)
        wheel(WHEEL_DOWN, nbScroll)
        sleep(p)
        click(rCat8)
        sleep(p)
        litMenuGauche()
        sleep(p)
        click(rCat)
        mouseMove(rCat1)
        sleep(p)
        wheel(WHEEL_DOWN, nbScroll)
        sleep(p)
        click(rCat9)
        sleep(p)
        litMenuGauche()
        click(rCat)
        mouseMove(rCat1)
        sleep(p)
        wheel(WHEEL_DOWN, nbScroll)
        sleep(p)
        click(rCat10)
        sleep(p)
        litMenuGauche()
        nbScroll = nbScroll + 1
        i = i+3 
    pos = i
    if i > nbCat: 
        pos = i - 3
    j=0
    while(pos+j<nbCat):
        rCurr = rCatListe[9-j]
        sleep(p)
        click(rCat)
        sleep(p)
        mouseMove(rCat1)
        sleep(p)
        wheel(WHEEL_DOWN, nbScroll)
        sleep(p)
        click(rCurr)
        sleep(p)
        litMenuGauche()
        j = j + 1





#8<-------------------------------------------------------------------------------------------------------

#Zaapi

#General
rMenuHdvZaapi = Region(2406,295,26,10)
rCartoucheZaapi = Region(3004,621,4,17)




rPopoBonta = Region(2942,1272,16,15)



#par Map


rZaapiMilice = Region(2546,461,13,20)
rTransportMilice = Region(2596,538,16,12)
rOngletHdvZaapi = Region(2435,296,6,10)

#Bijou

rTpBijou = Region(2437,512,19,14)
nbScrollBijou = 0
rVenBijou = Region(2318,601,8,8)
rAchatBijou = Region(2364,713,15,10)
nbCatBijou = 2


#Alchi

rTpAlchi = Region(2343,393,19,13)
nbScrollAlchi = 0
rVenAlchi = Region(3123,647,8,7)
rAchatAlchi = Region(3172,764,20,19)
nbCatAlchi = 10


#Animaux

rTpAnimaux = Region(2410,451,18,11)
nbScrollAnimaux = 0
rVenAnimaux = Region(3027,988,11,14)
rAchatAnimaux = Region(3080,1093,17,9)
nbCatAnimaux = 6

#Bucherons

rTpBuch = Region(2494,746,10,16)
nbScrollBuch = 0
rVenBuch = Region(2692,819,7,7)
rAchatBuch = Region(2740,936,14,9)
nbCatBuch = 6

#Bouchers
rTpBoucher = Region(2450,560,33,21)
nbScrollBouch = 0
rVenBouch = Region(2693,864,8,9)
rAchatBouch = Region(2740,982,13,8)
nbCatBouch = 3

#Boulangers
rTpBoulangers = Region(2474,627,14,15)
nbScrollBoulanger = 0

rVenBoulanger = Region(2262,644,7,15)
rAchatBoulanger = Region(2321,769,6,6)
nbCatBoulanger = 2
#Cordo

rTpCordo = Region(2455,802,17,14)
nbScrollCordo = 0
rVenCordo = Region(2312,768,6,9)
rAchatCordo = Region(2366,886,10,8)
nbCatCordo = 2

#Forgerons

rTpForg =Region(2443,924,16,7)
nbScrollForg = 0
rVenForg = Region(1982,819,9,6)
rAchatForg = Region(2040,936,10,9)
nbCatForg = 7


#Mineurs

rTpMineurs = Region(2454,507,19,16)
nbScrollMineur = 10
rVenMineur = Region(2071,697,8,12)
rAchatMineur = Region(2122,809,15,11)
nbCatMineur = 5

#Tailleurs
rTpTailleur = Region(2481,859,12,14)
nbScrollTailleur = 10
rVenTailleur = Region(2318,650,8,10)
rAchatTailleur = Region(2370,766,10,9)
nbCatTailleur = 3

#Ressources

rTpRess = Region(2471,691,25,8)
nbScrollRess = 10
rVenRess = Region(2077,719,7,11)
rAchatRess = Region(2136,842,8,10)
nbCatRess = 23



#Position des hdv dans le menu zaapi milice





rTpBrico = Region(2458,686,18,11)


rTpDoc = Region(2482,857,21,13)


rTpPaysans = Region(2475,571,23,14)
rTpPoissoniers = Region(2484,624,21,12)

rTpRunes = Region(2430,737,20,17)
rTpSuclp = Region(2490,802,18,16)

rTpAme = Region(2427,921,17,9)










class HDV:
    def __init__(self,nom,rVen,rAchat,nbCat,rTp,nbScroll):
        self.nom = nom
        self.rVen = rVen
        self.nbCat = nbCat
        self.rAchat = rAchat
        self.rTp = rTp
        self.nbScroll = nbScroll
        
    def join(self):
        mouseMove(rCartoucheZaapi)
        wheel(WHEEL_DOWN, self.nbScroll)
        sleep(p)
        if suisJeMenuZaapiMilice() :
            click(self.rTp)
        else:
            crash()
        
            
    def ouvre(self):
        mouseMove(self.rVen)
        sleep(p)
        click(self.rVen)
        sleep(p)
        click(self.rAchat)

    def scan(self):
        self.join()
        sleep(h)
        self.ouvre()
        sleep(m)
        if suisJeMenuHdv() :
            litMenuCat(self.nbCat)
        else:
            crash()
        
        




#Declaration des hdv

bijou = HDV("bijoutiers",rVenBijou,rAchatBijou,nbCatBijou,rTpBijou,nbScrollBijou)
alchi = HDV("alchimistes",rVenAlchi,rAchatAlchi,nbCatAlchi,rTpAlchi,nbScrollBijou)
animaux = HDV("animaux",rVenAnimaux,rAchatAnimaux,nbCatAnimaux,rTpAnimaux,nbScrollAnimaux)
buch = HDV("bucherons",rVenBuch,rAchatBuch,nbCatBuch,rTpBuch,nbScrollBuch)
cordo = HDV("cordonniers",rVenCordo,rAchatCordo,nbCatCordo,rTpCordo,nbScrollCordo)
forg = HDV("forgerons",rVenForg,rAchatForg,nbCatForg,rTpForg,nbScrollForg)
mineur = HDV("mineurs",rVenMineur,rAchatMineur, nbCatMineur, rTpMineurs, nbScrollMineur)
tailleur = HDV("tailleurs",rVenTailleur,rAchatTailleur,nbCatTailleur,rTpTailleur,nbScrollTailleur)
ress = HDV("ressources",rVenRess,rAchatRess,nbCatRess,rTpRess,nbScrollRess)

listeHdv = [bijou,cordo,tailleur,ress]



    
def ouvreZaapiMilice():
    mouseMove(rZaapiMilice)
    sleep(p)
    click(rZaapiMilice)
    sleep(p)
    click(rTransportMilice)
    sleep(h)
    click(rOnglet)

#Fonction de deplacement

def retourneEtatMilice():
    mouseMove(rMenuG1)
    sleep(g)
    type(Key.ESC)
    sleep(h)
    if suisJeEsc():
        type(Key.ESC)
        sleep(h)
    if suisJeSousMenuEsc():
        click(rTestSousMenuEsc)
        sleep(h)
    doubleClick(rPopoBonta)
    sleep(h)
    click(rZaapiMilice)
    sleep(p)
    click(rTransportMilice)
    sleep(h)
    click(rMenuHdvZaapi)
    

print(sys.argv[1])
i=int(sys.argv[1])

click(Region(2207,27,28,7))
retourneEtatMilice()
listeHdv[i].scan()
    
    




