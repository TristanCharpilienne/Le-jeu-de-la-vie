from tkinter import *

def damier(): #fonction dessinant le tableau
    ligne_vert()
    ligne_hor()
        
def ligne_vert():
    c_x = 0
    while c_x != width:
        can1.create_line(c_x,0,c_x,height,width=1,fill='black')
        c_x+=c
        
def ligne_hor():
    c_y = 0
    while c_y != height:
        can1.create_line(0,c_y,width,c_y,width=1,fill='black')
        c_y+=c

def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='black')
    dico_case[x,y]=1

def click_droit(event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can1.create_rectangle(x, y, x+c, y+c, fill='white')
    dico_case[x,y]=0

def change_vit(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
    global vitesse
    vitesse = int(eval(entree.get()))
    print(vitesse)


def go():
    "démarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
        #play()
        
def stop():
    "arrêt de l'animation"
    global flag    
    flag =0

def erase():
    "effacement de la grille"
    global flag    
    flag =0
    for k,v in dico_case.items():
        dico_case[k] = 0
        x = k[0]
        y = k[1]
        can1.create_rectangle(x, y, x+c, y+c, fill='white')
    dessine_grille()
    
#les différentes variables:

# taille de la grille
height = 400
width = 400
nb_tours = 0
population = 0

#taille des cellules
c = 10

#vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
vitesse=50

flag=0
dico_etat = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
dico_case = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
i=0
while i!= width/c: #assigne une valeur 0(morte) a chaque coordonnées(cellules) (valeur par défault en quelque sorte ^^)
    j=0
    while j!= height/c:
        x=i*c
        y=j*c
        dico_case[x,y]=0
        j+=1
    i+=1

#programme "principal" 
fen1 = Tk()

can1 = Canvas(fen1, width =width, height =height, bg ='white')
can1.bind("<Button-1>", click_gauche)
can1.bind("<Button-3>", click_droit)
can1.pack(side =TOP, padx =5, pady =5)

damier()

b1 = Button(fen1, text ='Go!', command =go)
b2 = Button(fen1, text ='Stop', command =stop)
b3 = Button(fen1, text ='Erase', command =erase)
b1.pack(side =LEFT, padx =3, pady =3)
b2.pack(side =LEFT, padx =3, pady =3)
b3.pack(side =LEFT, padx =3, pady =3)

entree = Entry(fen1)
entree.bind("<Return>", change_vit)
entree.pack(side =RIGHT)
chaine = Label(fen1)
chaine.configure(text = "Attente entre chaque étape (ms) :")
chaine.pack(side =RIGHT)

fen1.mainloop()
