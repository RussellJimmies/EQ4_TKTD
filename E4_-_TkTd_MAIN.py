import tkinter.messagebox
from tkinter import *
from tkinter import simpledialog
import time
from helper import *



class Vue():
    def __init__(self, parent):
        self.parent = parent
        self.modele = self.parent.modele
        self.root = Tk()
        self.root.geometry("1200x900")
        self.root.title("TKTD, Vers1.0")
        self.creer_interface()

    def creer_interface(self):

        self.var_duree = StringVar()
        self.best_time_vue = StringVar()
        self.best_time_entree = StringVar()

        #TOP FRAME
        self.frame_stats = Frame(self.root, bg="#7FB069")

        #SCORE, EXP, $, ET TEMPS
        frame_stats1 = Frame(self.frame_stats, bg="#f5f5f5")
        frame_stats2 = Frame(self.frame_stats, bg="#f5f5f5")
        frame_stats3 = Frame(self.frame_stats, bg="#f5f5f5")
        frame_stats4 = Frame(self.frame_stats, bg="#f5f5f5")

        frame_stats1.pack(side=LEFT, expand=1)
        frame_stats2.pack(side=LEFT, expand=1)
        frame_stats3.pack(side=LEFT, expand=1)
        frame_stats4.pack(side=LEFT, expand=1)

        label_time = Label(frame_stats1, text="          Temps:          \n -", bg="#FFFBBD", borderwidth=3, relief="sunken")
        label_score = Label(frame_stats2, text="          Score:          \n -", bg="#FFFBBD", borderwidth=3, relief="sunken")
        label_sagesse = Label(frame_stats3, text="          Sagesse:         \n - ", bg="#FFFBBD", borderwidth=3, relief="sunken")
        label_argent = Label(frame_stats4, text="          Argent:          \n -", bg="#FFFBBD", borderwidth=3, relief="sunken")

        label_time.pack(expand=1)
        label_score.pack(expand=1)
        label_sagesse.pack(expand=1)
        label_argent.pack(expand=1)

        #BOTTOM FRAME
        self.frame_bas = Frame(self.root, bg="#7FB069")

        #INFOS PARTIE, INFO TOUR, BOUTONS
        frame_infos_partie = Frame(self.frame_bas, borderwidth=3, relief="sunken")
        frame_infos_tour = Frame(self.frame_bas, borderwidth=3, relief="sunken")
        frame_bouttons = Frame(self.frame_bas, borderwidth=3, relief="sunken")
        frame_bouttons_row1 = Frame(frame_bouttons)


        frame_infos_partie.pack(expand=1, fill=BOTH, side=LEFT)
        frame_infos_tour.pack(expand=1, fill=BOTH, side=LEFT)
        frame_bouttons.pack(expand=1, fill=BOTH, side=LEFT)



        btn_tour_jaune = Button(frame_bouttons_row1, text="TOUR BLEUE", width=20)

        btn_tour_vert = Button(frame_bouttons_row1, text="TOUR MAUVE", width=20)
        btn_tour_rouge = Button(frame_bouttons_row1, text="TOUR BLANCHE", width=20)
        btn_debuter_partie = Button(frame_bouttons_row1, text="DÉBUTER PARTIE", width=20)



        label_map = Label(frame_infos_partie, text="INFO PARTIE: \n"
                          "Niveau: \n"
                          "# Vague: \n"
                          "# Bombes: \n"
                          "Kill Count: \n",
                          bg="#FFFBBD")
        label_tours = Label(frame_infos_tour, text="INFO TOUR \n À venir ", bg="#FFFBBD")
        label_acheter_tours = Label(frame_bouttons, text="Acheter tours: ", bg="#FFFBBD")




        label_map.pack(side=LEFT, expand=1)
        label_tours.pack(side=LEFT, expand=1)
        label_acheter_tours.pack(fill=X)
        btn_tour_jaune.pack(side=LEFT, fill=X)
        btn_tour_rouge.pack(side=LEFT, fill=X)
        btn_tour_vert.pack(side=LEFT, fill=X)
        btn_debuter_partie.pack(side=LEFT, fill=X, expand=1)
        frame_bouttons_row1.pack( fill=X, side=TOP)



        # le canevas de jeu
        self.canevas = Canvas(self.root, width=1200, height=600, bg="#D9F7FA", highlightthickness=0)
        #self.canevas.tag_bind("pion", "<Button>", self.debuter_partie)

        self.canevas.bind("<Button-1>", self.creer_tour_bleu)
        btn_debuter_partie.bind("<Button-1>", self.parent.debuter_partie)

        # visualiser

        self.frame_stats.pack(fill=X)

        self.canevas.pack()
        self.frame_bas.pack(expand=1, fill=BOTH)


        #self.afficher_partie()

    def creer_tour_bleu(self, evt):
        tour_creee = self.parent.creer_tour_bleu()
        self.canevas.create_oval(evt.x - tour_creee.rayon, evt.y - tour_creee.rayon,
                                 evt.x + tour_creee.rayon, evt.y + tour_creee.rayon,
                                 fill=None, tags=("statique"))
        self.canevas.create_rectangle(evt.x + tour_creee.demitaillex, evt.y + tour_creee.demitailley,
                                      evt.x - tour_creee.demitaillex, evt.y - tour_creee.demitailley,
                                      fill="blue", tags=("statique"))

    def recibler_pion(self, evt):
        x = evt.x
        y = evt.y
        self.parent.recibler_pion(x, y)

    def afficher_partie(self):

        self.canevas.delete("dynamique")

        for i in self.modele.sentier[0]:
            self.canevas.create_line(i,width = 40, fill = "brown", tags=("sentier",))

        # self.canevas.create_polygon(0,200, 240,200, 240,50, 840,50, 840,440, 1200,440, 1200,590, 840,590, 690,590,
        #                             690,440, 690,200, 390,200, 390,350, 240,350, 0,350,
        #                             fill="#51361a", tags=("poteau"))

        #                     posx1 , posy1 , posx2 ,posy2

        for i in self.modele.partie.niveau.liste_creep_a_l_ecran:
            x = i.x1
            y = i.y1

            self.canevas.create_oval(i.x1-i.rayon, i.y1-i.rayon, i.x1+i.rayon, i.y1+i.rayon, fill=i.couleur, tags=("dynamique",))



class Modele():
    def __init__(self, parent):

        self.parent = parent
        self.partie = None  #Partie(self)
        self.sentier =  [[
                        [[0,275],[240,275]],
                        [[240, 275], [240,50]],
                        [[240,50], [840,50]],
                        [[840,50], [840,515]],
                        [[840,515], [1200,515]]
                        ]]

        self.chemins = [[0,275, 315,275, 315,50, 840,50, 840,440, 1200,440, 1200,515,
                         840,515, 765,515,765,440, 765,125, 390,125, 390,350, 240,350, 0,350,]]

        self.largeur = 1200
        self.hauteur = 600
        self.debut = None
        self.duree = 0

        # self.creeps = Creeps(parent)


        self.liste_tours = []



    def creer_partie(self):
        self.partie = Partie(self)
        print("Partie créée")



    def creer_tour_bleu(self):
        tour_creee = Tour_Bleu(self, 300, 400)
        tour_creee.verification_range() ## à regarder si l'emplacement est ici?.
        self.liste_tours.append(tour_creee)
        return tour_creee

    def jouer_tour(self):
        self.partie.jouer_tour()


class Partie():
    def __init__(self,parent):
        self.parent = parent
        self.total_creep_tues = 0
        self.total_points = 0
        self.total_vie = 100
        self.total_argent = 1000
        self.total_sagesse = 0
        self.niveau_actuel = 0
        self.niveau = Niveau(self, self.niveau_actuel )





    def creer_niveau(self, evt ):
        self.niveau_actuel += 1
        self.niveau = Niveau(self, self.niveau_actuel)
        self.niveau.creer_creep()


    def jouer_tour(self):
        self.niveau.jouer_tour()


class Niveau():
    def __init__(self, parent, niveau_actuel):
        self.parent = parent
        self.niveau_actuel = niveau_actuel
        self.ratio_creep = 50.0
        self.nombre_creep_total = self.ratio_creep * self.niveau_actuel
        self.liste_creep_attente = []
        self.liste_creep_a_l_ecran = []
        self.niveau_est_parfait = True
        self.bonus_niveau_parfait = 50
        self.sagesse_du_niveau = 50 * self.niveau_actuel
        self.ratio_creep_vert = 0.9
        self.ratio_creep_jaune = 0.1
        self.ratio_creep_rouge = 0.0
        # self.creeps = Creeps(parent)
        self.delai = 0
        self.delai_nouveau_creep = 20
        self.creer_creeps()


    def jouer_tour(self):
        for i in self.liste_creep_a_l_ecran:
            i.jouer_tour()

        if self.delai < 1:
            if self.liste_creep_attente:
                rep = self.liste_creep_attente.pop(0)
                self.liste_creep_a_l_ecran.append(rep)
                self.delai = self.delai_nouveau_creep
        else:
            self.delai -= 1

    def creer_creeps(self):
        #
        # if self.ratio_creep_vert > 0:
        #     for i in range (int (self.ratio_creep * self.ratio_creep_vert)):
        #         self.liste_creep_attente.append(Creeps_vert())
        #
        # for i in range(int(self.ratio_creep * self.ratio_creep_jaune)):
        #     self.liste_creep_attente.append(Creeps_jaune())
        #
        # for i in range(int (self.ratio_creep * self.ratio_creep_rouge)):
        #     self.liste_creep_attente.append(Creeps_rouge())

        for i in range(10):
            self.liste_creep_attente.append(Creep(self))

        self.ratio_creep_vert -= 0.05
        self.ratio_creep_jaune += 0.1
        self.ratio_creep_rouge += 0.05


    def incrementer_niveau(self, evt):
        if len(self.liste_creep_attente) <= 0 and len(self.liste_creep_a_l_ecran) <= 0:
            self.niveau_actuel += 1


    def mettre_creeps_en_jeu(self):
        if len(self.liste_creep_attente) >= 0:
            tmp = self.liste_creep_attente.pop(0)
            self.liste_creep_a_l_ecran.append(tmp)














##################################################################################
#classes par William C et sebastian P


class Creep():
    def __init__(self,parent):
        self.parent = parent
        self.vie_creep = 42
        self.x1 = 0
        self.y1 = 275
        self.rayon = 15
        self.valeur_monetaire_creep = 0
        self.vitesse_creep_X = 5
        self.vitesse_creep_Y = 5
        self.troncon = 0

        self.max1 = 237
        self.max2 = 55
        self.max3 = 835
        self.max4 = 505
        self.max5 = 1210


        self.couleur = "green"
        self.est_cible = False
        self.est_vivant = False
        self.est_en_attente = False
        self.faiblesse_a = False
        self.faiblesse_b = False
        self.faiblesse_c = False
        #self.creep_vert = Creeps_vert(self)

    def jouer_tour(self):
        self.deplacement()

    def deplacement(self):



        if self.x1 < self.max1:
            self.x1 += self.vitesse_creep_X
        elif self.x1 >= self.max1 and self.y1 >= self.max2 and self.x1 < 400:
            self.y1 -= self.vitesse_creep_Y
        elif self.y1 <= self.max2 and self.x1 <= self.max3:
            self.x1 += self.vitesse_creep_X
        elif self.x1 >= self.max3 and self.y1 <= self.max4 and self.x1 > 400:
            self.y1 += self.vitesse_creep_Y
        elif self.y1 <= self.max3 and self.x1 <= self.max5 and self.x1 > 400:
            self.x1 += self.vitesse_creep_X


        # self.objectif_position = [
        #     [0, 312.5], [202.5, 312.5],
        #     [202.5, 87.5], [802.5, 87.5],
        #     [802.5, 477.5], [1200, 477.5]
        # ]
        # ça prend la liste pes points du polygone
        # on fais une boucle sur la liste pour passer au travers




class Creep_vert(Creep):
    # la vitesse est a titre indicatif 1 = plus lent 10 = plus vite
    # couleur vert easy one
    def __init__(self):
        Creep.__init__(self, Creep)
        self.vie_creep = 60
        self.valeur_monetaire_creep = 50
        self.vitesse_creep = 4
        self.faiblesse_c = True
        self.valeur_points = 100



class Creep_jaune(Creep):
    # couleur jaune medium one
    def __init__(self):
        Creep.__init__(self, Creep)
        self.vie_creep = 90
        self.valeur_monetaire_creep = 100
        self.vitesse_creep = 6
        self.faiblesse_a = True
        self.valeur_points = 200

class Creep_rouge(Creep):
    # couleur rouge hard one
    def __init__(self):
        Creep.__init__(self, Creep)
        self.vie_creep = 150
        self.valeur_monetaire_creep = 150
        self.vitesse_creep = 3
        self.faiblesse_a = True
        self.valeur_points = 300

class Boss(Creep):
    def __init__(self):
        Creep.__init__(self)
        self.vie_creep= 450
        self.valeur_monetaire_creep = 300


class Tour():
    def __init__(self, parent, x, y):
        self.parent = parent
        self.position_x_tour = x
        self.position_y_tour = y
        self.demitaillex = 25
        self.demitailley = 50
        self.valeur_monnetaire_tour = 0
        self.rayon = 150
        self.valeur_vente = 0

        self.placement_valide= False

    def verification_range(self):

        liste = self.parent.list
        for i in liste:  ##ici on prendra la liste creep active.
        #print("i.x :", i.x1)
            distance =Helper.calcDistance(i.x1,i.y1,self.position_x_tour,self.position_y_tour)
            somme_rayon = i.rayon + self.rayon
            if distance <= somme_rayon :
                i.est_cible = True
                print ("le creep est ciblé")


    def tirer_creep(self):
        self.projectile = Projectile(1,1,1)
    # ça appelle projectile

class Tour_Bleu(Tour):
    # bleu, rapide mais moins forte, tour initial
    def __init__(self, parent, x, y):
        Tour.__init__(self, parent, x, y)
        self.valeur_monnetaire_tour = 500

class Tour_Mauve(Tour):
    # mauve, plus lente mais un peu plus forte et degat en zone
    # on verifie la zone d'effet(angle avec helper library)
    def __init__(self, parent, x, y):
        Tour.__init__(self, parent, x, y)
        self.valeur_monnetaire_tour = 700

class Tour_blanche(Tour):
    # blanc, zap, beaucoup plus lent mais degats accrus. Touche 5 creeps en meme temps,
    def __init__(self, parent, x, y):
        Tour.__init__(self, parent, x, y)
        self.valeur_monnetaire_tour = 1000



class Projectile():
    def __init__(self, position_projectile_x, position_projectile_y):

        self.position_projectile_x = position_projectile_x
        self.position_projectile_y = position_projectile_y
        self.degats = 0
        self.vitesse_projectile = 0

class Projectil_a(Projectile):
    def __init__(self):
        Projectile.__init__(self)
        self.degats = 30
        self.vitesse_projectile = 6

class Projectil_b(Projectile):
    def __init__(self):
        Projectile.__init__(self)
        self.degats = 45
        self.vitesse_projectile = 4

class Projectil_c(Projectile):
    def __init__(self):
        Projectile.__init__(self)
        self.degats = 60
        self.vitesse_projectile = 2


    def tester_collision_projectile(self):
        pass
    ##vers la cible la plus loin.


class Controleur():
    def __init__(self):
        self.partie_en_cours = 0
        self.modele = Modele(self)
        self.vue = Vue(self)
        #self.debuter_partie()
        self.vue.root.mainloop()

    def mettre_creeps_en_jeu(self):
        self.modele.partie.niveau.mettre_creeps_en_jeu()

    def debuter_partie(self,tt):
        #self.modele.debut = time.time()
        self.partie_en_cours = 1
        #CREER PARTIE
        self.modele.creer_partie()
        self.jouer_partie()

    def jouer_partie(self):

        self.modele.jouer_tour()
        self.vue.afficher_partie()
        self.vue.root.after(40, self.jouer_partie)




    def creer_tour_bleu(self):
        return self.modele.creer_tour_bleu()

    def creer_creep(self):
        return  self.modele.creer_creep()

    def afficher_tour(self):
        self.vue.afficher_tour()


if __name__ == '__main__':
    c = Controleur()
    print("L'application se termine")
