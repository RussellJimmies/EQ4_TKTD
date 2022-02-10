class Modele():
    def __init__(self):
        self.largeur
        self.hauteur


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

class Controlleur():
    def __init__(self):
        self.modele = Modele(self)




if __name__ == '__main__':
    c= Controlleur()
