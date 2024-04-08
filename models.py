from random import *

class Joueur:
    nom = ' '
    manche_gagnee = ' '
    argent = 10000
    pokemons = ' '


    def __init__(self, nom, manche_gagnee, argent, pokemons):
        self.nom = nom
        self.manche_gagnee = manche_gagnee
        self.argent = argent
        self.pokemons = pokemons

    def choisir_pokemon(self):
        
        pokemons = ["Goupelin", "Amphinobi", "Xernéas", "Escroco", "Bruyverne", "Solgaléo", "Piafabec"]
        print(pokemons)
    
    def ajouter_pokemon(self):
        liste_joueur = []

        pokemon1 = int(input("Choisi le premier pokémon"))
        liste_joueur.append(self.pokemons[pokemon1])
        pokemon2 = int(input("Choisi le deuxième pokémon"))
        liste_joueur.append(self.pokemons[pokemon2])
        pokemon3 = int(input("Choisi le troisième pokémon"))
        liste_joueur.append(self.pokemons[pokemon3])

    def choisir_attaque(self, pokemon_adverse):
        ##attaque_pokemon_engagé = 
        i = int(input("Quelle attaque voulez-vous utiliser ?"))
        return self.pokemons[1].Pokemon.attaques[i]
        
    def recuperer_pokemon(self, pokemon):
        return self.ajouter_pokemon()

    def afficher_pokemon(self):
        print(f"Nom: {self.pokemons.nom}, Prix: {self.pokemons.prix}, Type: {self.pokemons.type}, PV: {self.pokemons.point_de_vie}, Niveau: {self.pokemons.niveau}, Attaque: {self.pokemons.attaque}, Attaque spéciale: {self.pokemons.Pokemon.attaque_speciale}, Défense: {self.pokemons.defense}, Défense spéciale: {self.pokemons.defense_speciale}, Vitesse: {self.pokemons.vitesse}")

    def afficher(self):
        print(f"Nom: {self.nom}, Manche gagnée: {self.manche_gagnee}, Argent: {self.argent}")


class Pokemon:
    nom = ' '
    prix = ' '
    type = ' '
    point_de_vie = 5000
    niveau = ' '
    attaque = ' '
    attaque_speciale = ' '
    defense = ' '
    defense_speciale = ' '
    vitesse = ' '
    attaques = []
    pokemon_combat = ' '

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

    def ajouter_attaque(self, Attaque):
        self.attaques.append(Attaque)

    def attaquer(self, pokemon_adverse, attaque_utilisee):
        return pokemon_adverse, attaque_utilisee

    def est_ko(self):
        if self.pokemons[1] < 0:
            return True
        else:
            return False
        
    def afficher_attaques(self):
        print(f"Nom: {self.pokemons[1].Attaque.nom}, Type: {self.pokemons[1].Attaque.type},  Catégorie: {self.pokemons[1].Attaque.categorie_attaque}, Précision: {self.pokemons[1].Attaque.precision}, Puissance: {self.pokemons[1].Attaque.puissance}, PP: {self.pokemons[1].Attaque.pp}")

    def afficher(self):
         print(f"Nom: {self.nom}, Prix: {self.prix}, Type: {self.type}, PV: {self.point_de_vie}, Niveau: {self.niveau}, Attaque: {self.attaque}, Attaque spéciale: {self.attaque_speciale}, Défense: {self.defense}, Défense spéciale: {self.defense_speciale}, Vitesse: {self.vitesse}")


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
        if type.attaque == pokemon_attaquant.type:
            stab = 1.5
        else:
            stab = 1
        pv_perdus = (((Pokemon.niveau*0.4 + 2)*Pokemon.attaque*self.puissance)/(Pokemon.defense*50)+2)*stab*(self.precision / 100)
        resultat = Pokemon.point_de_vie - pv_perdus
        print(resultat)


class Jeu:
    joueurs = []


    def jouer(self):
        joueur1 = 1
        joueur2 = 2
        joueur1 = []
        joueur2 = []
        self.joueurs.append(joueur1)
        self.joueurs.append(joueur2)
        i = 1

        for i in range (2):
            if i == 1:
                self.joueurs[i] = input("Quel est votre nom (joueur 1) ?")
                for i in range(3):
                    self.joueurs[i] = int(input("Choisissez un nombre pour choisir votre pokémon"))
                    ##self.joueurs[i] = 
                i = i + 1
            elif i == 2:
                self.joueurs[i] = input("Quel est votre nom (joueur 2) ?")
                self.joueurs[i] = input("Pouvez-vous acheter vos pokémons ?")