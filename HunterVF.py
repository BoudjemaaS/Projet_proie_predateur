from tkiteasy import * 
import random
import matplotlib.pyplot as pyplt
g = ouvrirFenetre(600,600)
import sys
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit())



def grille ():
    """
    Fonction :
        dessine la grille sur laquelle se déroule le jeu
    """
    
    
    for i in range (0,600,20):
        g.dessinerLigne(i,0,i,600,'white')
    for j in range (0,600,20):
        g.dessinerLigne(0,j,600,j,'white')






def repro (a_po,a_pr,liste):
    """
    Fonction :
        Rajoute une nouvelle proie sur le cadrillage lorsque 2 autres proies se trouve côte à côte dans le quadrillage
        Ou lance la fonction manger si un prédateur est à cote d'une proie
    Paramètres :
        a_po: l'âge des proies
        liste : la liste des individus
        a_pr : l'âge des prédateurs
    Retour :
         une proie en moins si mangée
         une proie en plus si reproduction
    """
    
    
    check=True
    if check and len(liste)<899:

        
        for rang in range(len(liste)):
            for indiv in liste:

                if rang<len(liste) and indiv['x']==liste[rang]['x']:
                    if indiv['y'] in range (int(liste[rang]['y']-20),int(liste[rang]['y']+20)) and indiv['y']!=liste[rang]['y']: #on regarde si les deux individus sont voisins
                        if indiv['genre']!=liste[rang]['genre']: #si ils sont differents, alors le predateur mange la proie
                            
                            check=True
                            
                            manger(a_pr,indiv,rang,liste)
      
                            if rang>=len(liste):
                                
                                check=False
                       
                        elif indiv['genre']=="proie" and liste[rang]['genre']==indiv['genre']: #si ce sont deux proies, alors il y a reproduction
                                
                            check=True
                           
                            apparition_proie(1,a_po,liste)
                            if rang >=len(liste):
                                check=False
                             
                            
                if rang<len(liste) and indiv['y']==liste[rang]['y']:
                    if indiv['x'] in range (int(liste[rang]['x']-20),int(liste[rang]['x']+20)) and indiv['x']!=liste[rang]['x']: #on regarde si les deux individus sont voisins
                        if indiv['genre']!=liste[rang]['genre']: #si ils sont differents, alors le predateur mange la proie

     
                            check=True
                            manger(a_pr,indiv,rang,liste)
                                
                            if rang>=len(liste):
                              
                                check=False
                        
                                
                        elif indiv['genre']=='proie' and liste[rang]['genre']==indiv['genre']:  #si ce sont deux proies, alors il y a reproduction

                            check=True
                            apparition_proie(1,a_po,liste)

                            if rang >=len(liste) :
                                check=False
                             
                        
        

def manger(a_pr, indiv,rang,liste):
    """
    Fonction :
        donne de l'énergie à un prédateur si celui-ci mange une proie
    Paramètres :
        indiv : un individu
        rang : position de l'individu vérifié
        liste : liste de positions des individus 
        a_pr : age des prédateurs
    """

    
    if indiv['genre']=='proie':
        
        rg=liste[rang]['age']                     #
        liste[rang]['age']+=1                       #                                          
        g.supprimer (indiv['individu'])              #
        if indiv in liste:                           #
            del liste[liste.index(indiv)]            #  
        if rg%5==0:                                  # 
            apparition_pred(1,a_pr,liste)            #
                                                      #  un predateur qui mange 5 proie se reproduit,
                                                       # un nouveau predateur apparait aleatoirement
    else:                                             #  la proie est supprimmée du plateau
        indiv['age']+=1                              #   la proie est supprimmée de la liste de d'individu
        g.supprimer (liste[rang]['individu'])        #                                                                               
        del liste[rang]                              #    
        if indiv['age']%5==0:                        #                                        
            apparition_pred(1,a_pr,liste)           #
                                                  #                 
                                                                                            
                    

def age(liste):
    """
    Fonction: 
        incrémenter l'âge de chaque individu
    Paramètre:
        liste: liste de positions des individus
    """
    
    for indiv in liste:

         
        indiv['age']-=1 # on retire 1vie à chaque individu à chaque tour
            
        if indiv['age']<1: # si l'age est à zéro, l'individu disparait
                
            g.supprimer(indiv['individu'])
            del liste [liste.index(indiv) ]           
            
           
 
    

def deplacement (a_po,a_pr,liste):
    """
    Fonction:
        la fonction permet de déplacer chaque individu en fonction de son genre: 
        si c'est une proie, elle se déplace de manière aléatoire.
        si c'est un prédateur, il cherche à se diriger vers la proie la plus proche.
    Paramètres :
        a_po : l'âge des proies
        a_pr : l'âge des prédateurs
        liste : liste de positions des individus
    """

    import random

    for indiv1 in liste:
        if indiv1['genre']=='predateur':
            distance = (((indiv1['x']-liste[0]['x'])**2)+((indiv1['y']-liste[0]['y'])**2))**1/2  #on évalu la distance entre deux individus
            for indiv2 in liste:                                                      

                if (((indiv1['x']-indiv2['x'])**2)+((indiv1['y']-indiv2['y'])**2))**1/2 < distance and indiv2['genre']=='proie': #le predateur cherche seulement a se rapprocher des proies
                    distance = (((indiv1['x']-indiv2['x'])**2)+((indiv1['y']-indiv2['y'])**2))**1/2 #on determine la distance la plus courte

                    distance_x= indiv2['x']-indiv1['x'] 
                    distance_y= indiv2['y']-indiv1['y']

                    if distance_x!=0:           #
                        if distance_x<0:          #
                            mouv_x = -20           #
                        else:                      #                           
                            mouv_x = 20            #
                    else:                          #
                        mouv_x=0                    #   on détermine le 'signe' de la distance
                                                     #  pour déterminer dans quel sens doit
                    if distance_y!=0:               #   évoluer le prédateur
                        if distance_y<0:           #  
                            mouv_y = -20           #
                        else:                      #
                            mouv_y = 20           #
                    else:                         #
                        mouv_y=0                #

                    nv_x = indiv1['x']+mouv_x
                    nv_y = indiv1['y']+mouv_y
                    p=False
                    t=False
                    if nv_x<600 and nv_y<600 and nv_x>0 and nv_y>0 :
                        p=True
                        for i in liste:
                            if i["x"]!=nv_x and i["y"]!=nv_y:
                                t=True # on vérifie que la nouvelle position soit bien sur le plateau
                    if p and t:
                        g.deplacer(indiv1['individu'],mouv_x,mouv_y) #on déplace l'individu et on met à jour ses informations
                        indiv1['x']=nv_x
                        indiv1['y']=nv_y
                    


        else :
            


            mouv_x=random.randrange(-20,21,20) #on genere une position aléatoire
            mouv_y=random.randrange(-20,21,20)
            nv_x = mouv_x+indiv1['x']
            nv_y = mouv_y+indiv1['y']
            p=False
            t=False
            if nv_x<600 and nv_y<600 and nv_x>0 and nv_y>0 : # on vérifie que la nouvelle position est dans le cadre
                p=True
                for i in liste:
                    if i["x"]!=nv_x and i["y"]!=nv_y: # on vérifi    que la nouvelle position ne soit pas ocuppée
                        t=True 
                            
            if p and t:           
                g.deplacer(indiv1['individu'],mouv_x,mouv_y) #on déplace l'individu et on met à jour ses informations
                indiv1['x']=nv_x
                indiv1['y']=nv_y

        
        
      

def apparition_pred(nb_pr,a_pr,liste):
    """
    Fonction :
        fait apparaître des prédateurs sur le quadrillage
    Paramètres :
        fpre: le nombre de prédateur apparaissant
        nb_pr : nombre de prédateur à faire apparaitre
        a_pr : l'age des prédateurs
        liste : la liste des individus
    """
    import random
    
    r=0
    while r!=nb_pr:
        vide=True 
        random_x=random.randrange(10,591,20) 
        random_y=random.randrange(10,591,20) #on génère une position aléatoire dans le cadre du plateau
        for indiv in liste:
            if random_x!=indiv['x'] and random_y!=indiv['y']: #on vérifie que la position n'est pas déja occuppée 
                vide=True
            else:
                vide=False

            
        if vide:  #on a parcouru toute la liste
            
            individu=g.dessinerDisque(random_x,random_y,5,'red') #on place l'individu sur le plateau
            liste.append({'genre':'predateur','individu':individu,'x':random_x,'y':random_y,'age':a_pr})
            r+=1
                    
    

def apparition_proie(nb_po,a_po,liste):
    """
    Fonction:  
        faire apparaitre un nombre fpro de proie
    Parametres: 
        nb_po : nombre de proie à faire apparaitre 
        a_po : l'âge des proies
        liste : la liste des individus
    """

    import random
    
    r=0
    while r!=nb_po and len(liste)<899: 
        vide=None
        random_x=random.randrange(10,591,20)
        random_y=random.randrange(10,591,20) #on génère une position aléatoire
        for indiv in liste:
            if random_x!=indiv['x'] and random_y!=indiv['y']: #on vérifie que la position n'est pas déja occuppée
                vide=True 
            else:
                vide=False
            if len(liste)>899:
                break
                
        if vide:   #on a parcouru toute la liste
              
            individu=g.dessinerDisque(random_x,random_y,5,'white') #on place l'individu sur le plateau
            liste.append({'genre':'proie','individu':individu,'x':random_x,'y':random_y,'age':a_po}) #on renseigne ses informations dans le tableau de positions
            r+=1
        
                    
                    

                    
       
   
    
    
def graph (lnpe,lnpr,ltps):
    """
    Fonction: 
        la fonction dessine le graphique représentant le nombre 
        de chaque types d'individu en fonction du nombre de tours
    Paramètres: 
        lnpe: liste du nombre de proies a chaque tour
        lnpr: liste du nombre de prédateurs a chaque tour
        ltp: liste des unités de temps utile à la construction du graphique
    """

    pyplt.plot(ltps,lnpe,'black',label="proies")       # on crée les courbes
    pyplt.plot(ltps,lnpr,'orange',label='predateurs')
    pyplt.legend()
    pyplt.title('nb proie/predateur en fonction du temps') #on ajoute un titre
    pyplt.show()

def compte(liste,tour,lnpe,lnpr,ltps,tps):
    """
    Fonction: 
        compte le nombre de proies et de prédateurs a chaque tour
        et stock les infos dans deux tableaux lnpe et lnpr
    Paramètre : 
        liste : liste de positions des individus
        tour : nombre de tour que doit effectuer le jeu
        lnpe : liste du nombre de proie à chaque tour
        lnpr : liste du nombre de predateur à chaque tour
        ltps : liste des unités de temps 
        tps : compteur de temps

    """

    npe=0
    npr=0
    
    for g in liste: 
        if g['genre']=='proie':
            npe+=1
        else:
            npr+=1
        
    lnpe.append(npe)  #
    lnpr.append(npr)  # on rempli les listes
    ltps.append(tps)  #
    
    if tps==tour: #une fois la fin du jeu, on dessine le graphique
        graph (lnpe,lnpr,ltps)  #du nombre de proies et de predateurs en focntion du nombre de tours
        

        
    
def lancement(tour,nb_po,a_po,nb_pr,a_pr):
    """ 
    Fonction: 
        lancement du jeu
    Paramètres : 
        tour : nombre de tour qu'effectuera le jeu
        a_po : age des proies
        a_pr : age des prédateurs
        nb_po : nombre de proies
        nb_pr: nombre de predateurs
    """
   

    tps=0
    lnpe=[]
    lnpr=[]
    ltps=[]
    
    tour = menu('nombre de tour',50)      #
    nb_po = menu('nombre de proie',150)    #
    a_po = menu('age proie',250)            # on affiche les saisies
    nb_pr = menu('nombre predateur',350)   #
    a_pr = menu('age predateur',450)      #

    g.pause(0.2)
    g.dessinerRectangle(0,0,900,900,'black')
    g.afficherTexte('PRESSEZ ENTREE',300,300,'white')
    g.actualiser()
    input('Pressez entrée')

    
    g.pause(0.2)
    g.dessinerRectangle(0,0,900,900,'green')
    g.actualiser()
    

    grille()

    individu=g.dessinerDisque(-10,-10,5,'black')
    pos = [{'genre':'predateur','individu':individu,'x':-10 ,'y':-10, 'age':1}]
    apparition_pred(nb_pr,a_pr,pos)
    apparition_proie(nb_po,a_po,pos)

    for t in range (tour):                  #
        g.pause(0.01)                         #
        apparition_pred(1,a_pr,pos)           #
        apparition_proie(5,a_po,pos)          # 
        age(pos)                               #  partie de la fonction qui fait tourner le jeu
        deplacement(a_po,a_pr,pos)            #  
        repro(a_po,a_pr,pos)                  #
        tps+=1                                #
        print('##################',tps)     #  <--- on suit l'avancé du jeu
        compte(pos,tour,lnpe,lnpr,ltps,tps)    
        g.actualiser()                      
    
       



def menu(txt,position):
    ''' Fonction:
            fonction de création du menu de sélection des valeurs
        Paramètres:
                txt : saisie de l'utilisateur
                position : position du texte
    '''
      
    p=(800-len(txt)*15)/3
    for i in txt:
        g.pause(0.05)
        g.afficherTexte(i,p,position,'white')
        p+=15
        g.actualiser()
    entrée=int(input(txt))
    txt=str(entrée)
    p=(800-len(txt)*15)/2.5
    for i in txt:
        g.pause(0.2)
        g.afficherTexte(i,p,position+50,'white')
        p+=15
        g.actualiser()
    return int(entrée)
    

lancement(1000,40,10,20,10)

while g.recupererClic()==None:
    continue

g.fermerFenetre




