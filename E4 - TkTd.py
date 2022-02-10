import tkinter.messagebox
from tkinter import *
from tkinter import simpledialog
import time
import re


class Vue():
    def __init__(self, parent):
        self.parent = parent
        self.modele = self.parent.modele
        self.root = Tk()
        self.root.geometry("1200x900")
        self.root.title("Carre Rouge, Vers1.0")
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



        btn_tour_jaune = Button(frame_bouttons_row1, text="TOUR JAUNE", width=20)

        btn_tour_vert = Button(frame_bouttons_row1, text="TOUR VERTE", width=20)
        btn_tour_rouge = Button(frame_bouttons_row1, text="TOUR ROUGE", width=20)



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
        frame_bouttons_row1.pack( fill=X, side=TOP)



        # le canevas de jeu
        self.canevas = Canvas(self.root, width=1200, height=600, bg="#D9F7FA", highlightthickness=0)
        #self.canevas.tag_bind("pion", "<Button>", self.debuter_partie)


        # visualiser

        self.frame_stats.pack(fill=X)

        self.canevas.pack()
        self.frame_bas.pack(expand=1, fill=BOTH)


        self.afficher_partie()


    def recibler_pion(self, evt):
        x = evt.x
        y = evt.y
        self.parent.recibler_pion(x, y)

    def afficher_partie(self):

        self.canevas.create_polygon(0,200, 240,200, 240,50, 840,50, 840,440, 1200,440, 1200,590, 840,590, 690,590,
                                    690,440, 690,200, 390,200, 390,350, 240,350, 0,350,
                                    fill="#51361a", tags=("poteau"))




class Modele():
    def __init__(self, parent):
        self.parent = parent

        self.largeur = 450
        self.hauteur = 450
        self.debut = None
        self.duree = 0
        self.pion = Pion(self)
        self.poteau = Cadre(self)
        self.sentinelles = []




##################################################################################
#classes par William C et sebastian P


class Creeps():
    def __init__(self):
        self.vie_creep = 0
        self.position_x_creep = 0
        self.position_y_creep = 0
        self.valeur_monetaire_creep = 0
        self.vitesse_creep=0

        self.est_cible = False
        self.est_vivant = False
        self.est_en_attente = False
        self.faiblesse_a = False
        self.faiblesse_b = False
        self.faiblesse_c = False

        self.objectif_position = []


    def deplacement(self):
        pass
        # ça prend la liste pes points du polygone
        # on fais une boucle sur la liste pour passer au travers


class Creeps_vert(Creeps):
    # la vitesse est a titre indicatif 1 = plus lent 10 = plus vite
    # couleur vert easy one
    def __init__(self):
        Creeps.__init__(self)
        self.vie_creep = 60
        self.valeur_monetaire_creep = 50
        self.vitesse_creep = 4
        self.faiblesse_c = True

class Creeps_jaune(Creeps):
    # couleur jaune medium one
    def __init__(self):
        Creeps.__init__(self)
        self.vie_creep = 90
        self.valeur_monetaire_creep = 100
        self.vitesse_creep = 6
        self.faiblesse_a = True

class Creeps_rouge(Creeps):
    # couleur rouge hard one
    def __init__(self):
        Creeps.__init__(self)
        self.vie_creep = 150
        self.valeur_monetaire_creep = 150
        self.vitesse_creep = 3
        self.faiblesse_a = True

class Boss(Creeps):
    def __init__(self):
        Creeps.__init__(self)
        self.vie_creep= 450
        self.valeur_monetaire_creep = 300


class Tour():
    def __init__(self):

        self.position_x_tour = 0
        self.position_y_tour = 0
        self.valeur_monnetaire_tour = 0
        self.range = 0
        self.valeur_vente = 0

        self.placement_valide= False

    def verification_range(self):
        pass

    def tirer_creep(self):
        self.projectile = Projectile(1,1,1)
    # ça appelle projectile

class Tour_Bleu(Tour):
    # bleu, rapide mais moins forte, tour initial
    def __init__(self):
        Tour.__init__(self)
        self.valeur_monnetaire_tour = 500

class Tour_Mauve(Tour):
    # mauve, plus lente mais un peu plus forte et degat en zone
    # on verifie la zone d'effet(angle avec helper library)
    def __init__(self):
        Tour.__init__(self)
        self.valeur_monnetaire_tour = 700

class Tour_blanche(Tour):
    # blanc, zap, beaucoup plus lent mais degats accrus. Touche 5 creeps en meme temps,
    def __init__(self):
        Tour.__init__(self)
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





# CADRE NOIR
class Cadre():
    def __init__(self, parent):
        self.parent = parent
        self.x = 0
        self.y = 0
        self.demitaille = 50


class Pion():
    def __init__(self, parent):
        self.parent = parent
        self.x = 225
        self.y = 225
        self.demitaille = 20
        self.isCollision = False

    def recibler(self, x, y):
        self.x = x
        self.y = y
        self.tester_collision()

    def tester_collision(self):

        x1 = self.x - self.demitaille
        y1 = self.y - self.demitaille
        x2 = self.x + self.demitaille
        y2 = self.y + self.demitaille

        pot = self.parent.poteau
        pot_top_x1 = pot.x - pot.demitaille
        pot_top_y1 = pot.y - pot.demitaille
        pot_top_x2 = 500 + pot.demitaille
        pot_top_y2 = pot.y + pot.demitaille

        pot_bottom_x1 = pot.x - pot.demitaille
        pot_bottom_y1 = 450 - pot.demitaille
        pot_bottom_x2 = 500 + pot.demitaille
        pot_bottom_y2 = 500 + pot.demitaille

        pot_left_x1 = pot.x - pot.demitaille
        pot_left_y1 = pot.y - pot.demitaille
        pot_left_x2 = pot.x + pot.demitaille
        pot_left_y2 = 500 + pot.demitaille

        pot_right_x1 = 450 - pot.demitaille
        pot_right_y1 = pot.y - pot.demitaille
        pot_right_x2 = 500 + pot.demitaille
        pot_right_y2 = 500 + pot.demitaille

        for i in self.parent.sentinelles:
            i_x1 = i.x - i.dt1
            i_y1 = i.y - i.dt2
            i_x2 = i.x + i.dt1
            i_y2 = i.y + i.dt2

            if (x2 > i_x1 and x1 < i_x2) and (y2 > i_y1 and y1 < i_y2):
                self.isCollision = True

        if (x2 > pot_top_x1 and x1 < pot_top_x2) and (y2 > pot_top_y1 and y1 < pot_top_y2):
            self.isCollision = True

        if (x2 > pot_bottom_x1 and x1 < pot_bottom_x2) and (y2 > pot_bottom_y1 and y1 < pot_bottom_y2):
            self.isCollision = True

        if (x2 > pot_left_x1 and x1 < pot_left_x2) and (y2 > pot_left_y1 and y1 < pot_left_y2):
            self.isCollision = True

        if (x2 > pot_right_x1 and x1 < pot_right_x2) and (y2 > pot_right_y1 and y1 < pot_right_y2):
            self.isCollision = True


class Sentinelles():
    def __init__(self, parent, x, y, dt1, dt2, vitesse_x, vitesse_y):
        self.parent = parent
        self.x = x
        self.y = y
        self.dt1 = dt1
        self.dt2 = dt2
        self.vitesse_x = vitesse_x
        self.vitesse_y = vitesse_y

    def move(self):

        self.x += self.vitesse_x
        self.y -= self.vitesse_y

        self.x1 = self.x - self.dt1
        self.y1 = self.y - self.dt2
        self.x2 = self.x + self.dt1
        self.y2 = self.y + self.dt2

        if self.x1 <= 0 or self.x2 >= 450:
            self.vitesse_x *= -1
        if self.y1 <= 0 or self.y2 >= 450:
            self.vitesse_y *= -1

    def incrementer_vitesse(self):
        absX = abs(self.vitesse_x)
        absY = abs(self.vitesse_y)

        absX += 0.01
        absY += 0.01

        if self.vitesse_x < 0:
            self.vitesse_x = absX * -1
        else:
            self.vitesse_x = absX

        if self.vitesse_y < 0:
            self.vitesse_y = absY * -1
        else:
            self.vitesse_y = absY


class Controleur():
    def __init__(self):
        self.partie_en_cours = 0
        self.modele = Modele(self)
        self.vue = Vue(self)
        self.vue.root.mainloop()

    def recibler_pion(self, x, y):
        self.modele.recibler_pion(x, y)

    def debuter_partie(self):
        self.modele.debut = time.time()
        self.partie_en_cours = 1
        self.modele.pion.isCollision = False
        self.jouer_partie()

    def reset_partie(self):

        self.modele.reset_partie()

    def reset_partie_pop_up(self):
        self.modele.reset_partie_pop_up()

    def jouer_partie(self):
        if self.partie_en_cours:
            self.modele.jouer_tour()
            for i in self.modele.sentinelles:
                i.move()
                i.incrementer_vitesse()

        self.vue.afficher_partie()

        if (self.modele.pion.isCollision):
            self.reset_partie_pop_up()
            self.reset_partie()
            self.modele.pion.isCollision = False
            self.vue.arreter_jeu(self)
            self.partie_en_cours = 0

        if self.partie_en_cours:
            self.vue.root.after(40, self.jouer_partie)


if __name__ == '__main__':
    c = Controleur()
    print("L'application se termine")
