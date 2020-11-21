##Initialisation
from upemtk import *

from tkinter import *

##Fonctions

def init_plateau(n):#Création de la matrice 8X8
    '''
    Fonction qui crée une matrice de taille ligne*colonne représentant le plateau du jeu. 
    Param. reçu : n : int
    Param. renvoyé: lstp : lst
    '''
    ligne=n

    colonne=n

    lstp=[]

    for n in range(ligne):

        lst=[0]*ligne

        lstp.append(lst)

    return lstp







def env_jeu(plt):#Plateau de jeu en fonction de la matrice

    '''
    Affichage du plateau de jeu et des premiers pions déjà placés.
    Param. reçu : plt : lst
    Param. renvoyé:(x,y) : int
    '''
    pas=50

    for i in range (len(plt)):

        y=i*pas

        for j in range (len(plt)):

            x=j*pas

            ligne(x,y,x,y+pas,couleur='black',epaisseur=1.5)

            ligne(x,y,x+pas,y,couleur='black',epaisseur=1.5)

            mise_a_jour()

    

    return False   

    

         

def pions(plt):#Création de pions 
    '''Fonction recevant la matrice plateau et place un pion blanc ou noir selon le tour dans la case i j.
    Param. reçu : plt : lst
    Param. renvoyé : tuple : (i,j)'''


    pas=50

    for i in range(len(plt)):

        y=(i*pas)

        for j in range(len(plt)):

            x=(j*pas)

            if plt[i][j]==1:

                cercle(x-pas//2,y-pas//2,15,remplissage='black')

                mise_a_jour()

            elif plt[i][j]==-1:

                cercle(x-pas//2,y-pas//2,15,couleur='white',remplissage='white')

                mise_a_jour()

    

    return (i,j)

            

def croix(plt):
    '''Fonction qui dessinent des croix dans les cases de possibilités.
    Param. reçu : plt :lst
    Param. renvoyé : None'''

    pas=50

    for i in range(len(plt)):

        y=(i*pas)

        for j in range(len(plt)):

            x=(j*pas) 

            if plt[i][j]==2 :

                croix=image(x-pas//2,y-pas//2,'croix.png')
                mise_a_jour()
            
            
                

            if plt[i][j]==3:

                croix=image(x-pas//2,y-pas//2,'croix.png')
                mise_a_jour()
            
                    

            

            

def crea_pion(plt):

    '''Fonction qui, après le jeu du joueur, remplace les cases de 2 par 1 et de 3 par -1. 
    Param. reçu : (x,y): tuple (coordonnées renvoyés après le click)
    Param. renvoyé: plt : lst'''
    
    pas=50

    (x,y)=attend_clic_gauche()

    j=int(x/pas+1)

    i=int(y/pas+1)

    

    if plt[i][j]==2 :

       plt[i][j]=1

    
    elif plt[i][j]==3:

        plt[i][j]=-1


    else:

        t=texte(50,100,'Vous ne pouvez pas mettre un pion dans cette case!',couleur='red',taille=15)

        attend_clic_gauche()

        efface(t) 

        mise_a_jour

        

    return i,j    

    

def re_init(plt):
    '''Après la fonction possibilités, celle-ci remplace les possibilités 2 ou 3 par des cases vides pour le tour suivant.
    Param. reçu : plt : lst
    Param. renvoyé : plt : lst'''
    
    for i in range (len(plt)):

        for j in range(len(plt)):

            if plt[i][j]==2 :

                plt[i][j]=0

            elif plt[i][j]==3:

                plt[i][j]=0




def possibilites(plt,joueur):

    '''Après la fonction possibilités, celle-ci remplace les possibilités 2 ou 3 par des cases vides pour le tour suivant.
    Param. reçu : plt : lst
    Param. renvoyé : plt : lst'''

    if joueur==1:

        pa=-1 #pions adverses
        pos=2 #possibilités

    elif joueur==-1:

        pa=1 #pions adverses
        pos=3 #possibilités

    for i in range (len(plt)):


        for j in range(len(plt)):

            if plt[i][j]==joueur:

                x=1

                y=2

                a=1

                b=2

                while x<8-i and y<8-i and a<8-j and b<8-j:

                    if (i==1 or i==2) and (j==1 or j==2) :

                        
                        if plt[i+x][j+a]==pa and plt[i+y][j+b]==0:#Diagonale

                            plt[i+y][j+b]=pos

                            

                        elif plt[i+x][j]==pa and plt[i+y][j]==0:#Verticale

                            plt[i+y][j]=pos

                            

                        elif plt[i][j+a]==pa and plt[i][j+b]==0:#Horizontale

                            plt[i][j+b]=pos

                    

                    elif (i==1 or i==2) and (j==7 or j==8):

                        if plt[i+x][j-a]==pa and plt[i+y][j-b]==0:#Diagonale

                            plt[i+y][j-b]=pos

                        

                        elif plt[i+x][j]==pa and plt[i+y][j]==0:#Verticale

                            plt[i+y][j]=pos

                        

                        elif plt[i][j-a]==pa and plt[i][j-b]==0:#Horizontale

                            plt[i][j-b]=pos

                        

                    

                    

                    elif (i==7 or i==8)  and (j==1 or j==2):

                        if plt[i-x][j+a]==pa and plt[i-y][j+b]==0:#Diagonale

                            plt[i-y][j+b]=pos

                            

                        elif plt[i-x][j]==pa and plt[i-y][j]==0:#Verticale

                            plt[i-y][j]=pos

                            

                        elif plt[i][j+a]==pa and plt[i][j+b]==0:#Horizontale

                            plt[i][j+b]=pos

                    

                    

                    elif (i==7 or i==8)  and (j==7 or j==8):    

                        if plt[i-x][j-a]== pa and plt[i-y][j-b]==0:#Diagonale

                            plt[i-y][j-b]=pos

                        

                        elif plt[i-x][j]==pa and plt[i-y][j]==0:#Verticale

                            plt[i-y][j]=pos

                            

                        

                        elif plt[i][j-a]==pa and plt[i][j-b]==0:#Horizontale

                            plt[i][j-b]=pos

                            

                    

                    elif i > 2 and i < 7 and j > 2 and j < 7:

                        

                        #Diagonale

                        if plt[i-x][j-a] == pa and plt[i-y][j-b] == 0:

                            plt[i-y][j-b] = pos

                        elif plt[i+x][j+a] == pa and plt[i+y][j+b] == 0:

                            plt[i+y][j+b] = pos

                        elif plt[i+x][j-a] == pa and plt[i+y][j-b] == 0:

                            plt[i+y][j-b]=pos

                        elif plt[i-x][j+a]==pa and plt[i-y][j+b]==0:

                            plt[i-y][j+b]=pos

                        

                        

                        #Horizontale    

                        elif plt[i][j+a]==pa and plt[i][j+b]==0:

                            plt[i][j+b]=pos

                                

                        elif plt[i][j-a]==pa and plt[i][j-b]==0:

                            plt[i][j-b]=pos

                            

                                    

                        #Verticale

                        elif plt[i+x][j]==pa and plt[i+y][j]==0:

                            plt[i+y][j]=pos

                        elif plt[i-x][j]==pa and plt[i-y][j]==0:

                            plt[i-y][j]=pos

                    
                    else:

                        return False

                    x=x+1

                    y=y+1

    return plt



def switch(plt,joueur):


    if joueur==1:

        pa=-1

    elif joueur==-1:

        pa=1

    for i in range (len(plt)):

        

        for j in range(len(plt)):

            if plt[i][j]==joueur:

                x=1

                y=2

                a=1

                b=2

                while x<8-i and y<8-i and a<8-j and b<8-j:

                    if (i==1 or i==2) and (j==1 or j==2) :#Bords du plateau

                        

                        if plt[i+x][j+a]==pa and plt[i+b][j+y]==joueur:#Diagonale

                            plt[i+y][j+a]=joueur

                            

                        elif plt[i+x][j]==pa and plt[i+y][j]==joueur:#Verticale

                            plt[i+x][j]=joueur

                            

                        elif plt[i][j+a]==pa and plt[i][j+b]==joueur:#Horizontale

                            plt[i][j+a]=joueur

                    

                    elif (i==1 or i==2) and (j==7 or j==8):

                        if plt[i+x][j-a]==pa and plt[i+y][j-b]==joueur:#Diagonale

                            plt[i+x][j-a]=joueur

                        

                        elif plt[i+x][j]==pa and plt[i+y][j]==joueur:#Verticale

                            plt[i+x][j]=joueur

                        

                        elif plt[i][j-a]==pa and plt[i][j-b]==joueur:#Horizontale

                            plt[i][j-a]=joueur

                        

                    

                    

                    elif (i==7 or i==8)  and (j==1 or j==2):

                        if plt[i-x][j+a]==pa and plt[i-y][j+b]==joueur:#Diagonale

                            plt[i-x][j+a]=joueur

                            

                        elif plt[i-x][j]==pa and plt[i-y][j]==joueur:#Verticale

                            plt[i-x][j]=joueur

                            

                        elif plt[i][j+a]==pa and plt[i][j+b]==joueur:#Horizontale

                            plt[i][j+a]=joueur

                    

                    

                    elif (i==7 or i==8)  and (j==7 or j==8):    

                        if plt[i-x][j-a]== pa and plt[i-y][j-b]==joueur:#Diagonale

                            plt[i-x][j-a]=joueur

                        

                        elif plt[i-x][j]==pa and plt[i-y][j]==joueur:#Verticale

                            plt[i-x][j]=joueur

                            

                        

                        elif plt[i][j-a]==pa and plt[i][j-b]==joueur:#Horizontale

                            plt[i][j-a]=joueur

                            

                    

                    elif (i>2 or i<7) and (j>2 or j<7):

                        #Diagonale

                        if plt[i-x][j-a]== pa and plt[i-y][j-b]==joueur:

                            plt[i-x][j-a]=joueur

                        elif plt[i+x][j+a]==pa and plt[i+y][j+b]==joueur:

                            plt[i+x][j+a]=joueur

                        elif plt[i+x][j-a]==pa and plt[i+y][j-b]==joueur:

                            plt[i+x][j-a]=joueur

                        elif plt[i-x][j+a]==pa and plt[i-y][j+b]==joueur:

                            plt[i-x][j+a]=joueur

                        

                        

                        #Horizontale    

                        elif plt[i][j+a]==pa and plt[i][j+b]==joueur:

                            plt[i][j+a]=joueur

                                

                        elif plt[i][j-a]==pa and plt[i][j-b]==joueur:

                            plt[i][j-a]=joueur

                            

                                    

                        #Verticale

                        elif plt[i+x][j]==pa and plt[i+y][j]==joueur:

                            plt[i+x][j]=joueur

                        elif plt[i-x][j]==pa and plt[i-y][j]==joueur:

                            plt[i-x][j]=joueur

                    else:

                        return False

                    

                    x=x+1

                    y=y+1

                    

                    

                    

    return plt

    

    

def pass_tour(can):
    '''
En analysant le plateau de jeu, cette fonction détecte les cas où l’un des joueurs doit passer son tour, c’est à dire, quand il est dans l’impossibilité d’encadrer les pions du joueur adverse. 
Param. reçu : can : Booléen
Param. renvoyé: None '''
  
    if can==False:

        if joueur==-1:

            joueur=1

        elif joueur==1:

            joueur=-1

        t2=texte(50,100,'Vous devez passer votre tour',taille=10, couleur="black")

        attend_clic_gauche()

        efface()

        mise_a_jour



def score1(plt):

    '''
A la fin de la partie, cette fonction parcourt le plateau et compte le nombre de pions noirs, elle affichera par la suite le score le plus élevé.
Param. reçu : lstp : lst
Param. renvoyé: score : int '''
    

    score1=0

    for i in range(len(plt)):

        for j in range (len(plt[i])):

            if plt[i][j] == 1:

                score1=score1+1

            

    return score1


def score2(plt):
    '''A la fin de la partie, cette fonction parcourt le plateau et compte le nombre de pions blancs , elle affichera par la suite le score le plus élevé.
    Param. reçu : lstp : lst
    Param. renvoyé: score : int 
        '''

    score2=0

    for i in range(len(plt)):

        for j in range (len(plt[i])):

            if plt[i][j]==-1:

                score2=score2+1

    return score2

##Fenêtre

cree_fenetre(400,400)

rectangle(0,0,400, 400,remplissage='dark green')#Fond vert du plateau

##Messages de bienvenue

tb1=texte(200, 150, 'OTHELLO \n   Reversi',

      police='Times', taille=40, couleur="green",

      ancrage='center')

attend_clic_gauche()



tb2=texte(200, 280, "Règle du jeu :\n-Pions initiaux déjà posés.\n-Les joueurs posent les pions chacun à son \n tour dans les cases marquées d'une croix.\nBut du jeu :\n-Le joueur avec le plus de pions\n sur le plateau gagne.\n Joueur 1: pions noirs.\n Joueur2: pions blancs" ,

      police='Courier', taille=10, couleur="black",

      ancrage='center')

attend_clic_gauche()



tb3=texte(275, 380, 'HAPPY REVERSI!',

      police='Times', taille=15, couleur="light green",

      ancrage='center')



attend_clic_gauche()

efface_tout()

rectangle(0,0,950, 950,remplissage='dark green')



mise_a_jour

##Programme principal 

pas=50 #taille de la case 



plt=init_plateau(8)

#Dépôt des 4 premiers pions 

plt[4][4]=-1

plt[4][5]=1

plt[5][4]=1

plt[5][5]=-1


#Joueur1:pions noirs

#Joueur2:pions blancs

env=env_jeu(plt)#plateau de jeu 8x8
pions(plt)
mise_a_jour()

print(plt)

#Premier à jouer : joueur1 
joueur=1


while True:


    if joueur>0:

        can1=possibilites(plt,joueur)#Possibilités de jeu du joueur1

        croix(plt)

        crea_pion(plt)

        pions(plt)

        switch(plt,joueur)

        print(switch(plt,joueur)) 

        

        joueur=joueur*(-1)

        re_init(plt)    

        

    if joueur<0:

        can2=possibilites(plt,joueur)#Possiblités de jeu du joueur2 

        croix(plt)

        crea_pion(plt)

        pions(plt)

        switch(plt,joueur) 

        print(switch(plt,joueur)) 

        joueur=joueur*(-1)

        re_init(plt) 

        
##Fin du jeu

    if can1==False and can2==False:

        efface_tout()

        score1=score1(plt)

        score2=score2(plt)

        texte(100, 100,'Le Score du Joueur 1 :' +str(score1),

      police='Courier', taille=10, couleur="black",

      ancrage='center')

        texte(100, 200,'Le Score du Joueur 2 :' +str(score2),

      police='Courier', taille=10, couleur="black",

      ancrage='center')

        if score1<score2:

            texte(100, 300,'Le Joueur 2 a gagné !',

      police='Courier', taille=10, couleur="black",

      ancrage='center')

        elif score2<score1:

            texte(100, 300,'Le Joueur 1 a gagné !',

      police='Courier', taille=10, couleur="black",

      ancrage='center')

    

    

attend_fermeture()

mise_a_jour()