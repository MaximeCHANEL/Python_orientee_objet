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
        
        pokemons = ["Brindibou", "Efflèche", "Archéduc", "Flamiaou", "Matoufeu", "Félinferno", "Otaquin", "Oterlette", "Oratoria", "Picassaut", "Piclairon", "Bazoucan", "Manglouton", "Argouste", "Larvibule", "Chrysapile", "Lucanon", "Crabagarre", "Crabominable", "Plumeline", "Bombydou", "Rubombelle", "Rocabot", "Lougaroc", "Froussardine", "Vorastérie", "Prédastérie", "Tiboudet", "Bourrinos", "Araqua", "Tarenbulle", "Mimantis", "Floramantis", "Spododo", "Lampignon", "Tritox", "Malamandre", "Nounourson", "Chelours", "Croquine", "Candine", "Sucreine", "Guérilande", "Gouroutan", "Quartermac", "Sovkipou", "Sarmuraï", "Bacabouh", "Trépassable", "Concombaffe", "Silvallié", "Météno", "Dodoala", "Boumata", "Togedemaru", "Mimiqui", "Denticrisse", "Draïeul"]
        print(pokemons)
    
    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def choisir_attaque(self, pokemon_adverse):
        print(Pokemon.pokemon_combat)
        i = int(input("Quelle attaque voulez-vous utiliser ?"))
        return Pokemon.pokemon_combat.attaques[i]
        
    ##def recuperer_pokemon(self, premier, deuxieme, troisieme):

    def afficher_pokemon(self):
        print(self.pokemons)

    def afficher():
        print(Joueur)


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
        self.pokemon_combat = Jeu.joueur1[1]

    def ajouter_attaque(self, attaquee):
        self.attaques.append(attaquee)

    def attaquer(self, pokemon_adverse, attaque_utilisee):
        return pokemon_adverse, attaque_utilisee

    def est_ko(self):
        if self.pokemon_combat < 0:
            return True
        else:
            return False
        
    def afficher_attaques(self):
        print(f"Nom: {self.pokemon_combat.Attaque.nom}, Type: {self.pokemon_combat.Attaque.type},  Catégorie: {self.pokemon_combat.Attaque.categorie_attaque}, Précision: {self.pokemon_combat.Attaque.precision}, Puissance: {self.pokemon_combat.Attaque.puissance}, PP: {self.pokemon_combat.Attaque.pp}")

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