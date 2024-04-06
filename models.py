from random import *

class Joueur:
    nom = ' '
    manche_gagnee = ' '
    argent = ' '
    pokemons = []
    i = 0

    pokemon_attaquant = random.randint(0, len(pokemons)-1)
    pokemon_attaquer = random.randint(0, len(pokemons)-1)

    def __init__(self, nom, manche_gagnee, argent, pokemons):
        self.nom = nom
        self.manche_gagnee = manche_gagnee
        self.argent = argent
        self.pokemons = pokemons

    def choisir_pokemon(self):
        
        for i in range(3):
            dresseur = int(input("Choisi 1 pokémon parmi la liste"))
            if dresseur == self.pokemons:
                i = i + 1
                print(dresseur)
                if i == 1:
                    premier = 1
                    return premier
                elif i == 2:
                    deuxieme = 2
                    return deuxieme
                elif i == 3:
                    troisieme = 3
                    return troisieme
    
    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def choisir_attaque(self, pokemon):
        print(Pokemon.attaque)
        joueur = input("Quelle attaque voulez-vous utiliser ?")
        if joueur == Pokemon.attaque:
            return Pokemon.attaques
        
    ##def recuperer_pokemon(self, premier, deuxieme, troisieme):

    def afficher_pokemon(self):
        print(self.pokemons)

    def afficher():
        print(Joueur)


class Pokemon:
    nom = ' '
    prix = ' '
    type = ' '
    point_de_vie = ' '
    niveau = ' '
    attaque = ' '
    attaque_speciale = ' '
    defense = ' '
    defense_speciale = ' '
    vitesse = ' '
    attaques = []

    def __init__(self, nom, prix, type, point_de_vie, niveau, attaque, attaque_speciale, defense, defense_speciale, vitesse, attaques):
        self.nom = nom
        self.prix = prix
        self.type = type
        self.point_de_vie = point_de_vie
        self.niveau = niveau
        self.attaque = attaque
        self.attaque_speciale = attaque_speciale
        self.defense = defense
        self.defense_speciale = defense_speciale
        self.vitesse = vitesse
        self.attaques = attaques

    def ajouter_attaque(self, attaquee):
        self.attaques.append(attaquee)

    ##def attaquer(self, feuricendre, boule_eleck):

    def est_ko(self):
        if Joueur.pokemons < self.point_de_vie:
            return True
        else:
            return False
        
    def afficher_attaques(self):
        print(Attaque)

    def afficher(self):
        print(Pokemon)


class Attaque:
    nom = ' '
    type = ' '
    categorie_attaque = ' '
    precision = ' '
    puissance = ' '
    pp = ' '

    def __init__(self, nom, type, categorie_attaque, precision, puissance, pp):
        self.nom = "Draco-queue"
        self.type = "dragon"
        self.categorie_attaque = "physique"
        self.precision = 90
        self.puissance = 60
        self.pp = 10

    def calculer_degats(self, pokemon_attaquant, pokemon_attaquer):
        pv_perdus = (((Pokemon.niveau*0.4 + 2)*Pokemon.attaque*self.puissance)/(Pokemon.defense*50)+2)
        resultat = Pokemon.point_de_vie - pv_perdus
        print(resultat)