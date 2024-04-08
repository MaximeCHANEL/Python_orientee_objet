from random import *

class Joueur:
    nom = ' '
    manche_gagnee = ' '
    argent = 1220
    pokemons = ' '


    def __init__(self, nom, manche_gagnee, argent, pokemons):
        self.nom = nom
        self.manche_gagnee = manche_gagnee
        self.argent = argent
        self.pokemons = pokemons

    def choisir_pokemon(self):
        
        pokemons = []
        print(pokemons)
    
    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

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

#Tout les Pokemeon
Type_feu = Type("feu")
Type_eau = Type("Eau")
Type_fée = Type("Fée")
Type_ténèbres = Type("ténèbres")
Type_Dragon = Type("dragon")
Type_Psy = Type("Psy")
Type_inconnu = Type("Inconnu")

Attaque_feu = Attaque("Nitrocharge", Type_feu, "Physique", 50, 100, 20)
Attaque_eau =Attaque("Sheauriken", Type_eau, "Physique", 100, 15, 20)
Attaque_fée = Attaque("Eclair magique", Type_fée, "Spécial", 80, 100, 10)
Attaque_Ténèbres = Attaque("Bombe puante", Type_ténèbres, "Spécial", 100, 70, 8)
Attaque_Dragon = Attaque("Dragon céleste", Type_Dragon, "Spécial", 100, 228422, 22842 )
Attaque_Psy = Attaque("Boutefeu", Type_fée, "Spécial", 100, 120, 15)
Attaque_Inconnu = Attaque("Enfantin", Type_inconnu, "Physique", 50, 6000, 2)

Pokemon_Goupelin = Pokemon("Goupelin", 75, [Type_feu], 354, 46, 69, 72, 74, 100 , 104)
Pokemon_Amphinobi = Pokemon("Amphinobi", 80, [Type_eau], 348, 50, 95, 67, 103, 71, 122)
Pokemon_Xernéas = Pokemon("Xernéas", 100, [Type_fée], 456, 20, 131, 95, 131, 98, 99)
Pokemon_Tokodombi = Pokemon("Toko dombi", 10, [Type_ténèbres], 1492, 105, 60, 60, 70, 95)
Pokemon_neduj = Pokemon("neduj", 1000, [Type_Dragon], 374, 1, 73, 70, 73, 115 , 67)
Pokemon_Solgaléo = Pokemon("Solgaléo", 120, [Type_Psy], 478, 15, 137, 107, 113, 89, 97)
Pokemon_Norman = Pokemon("Norman", 16, {Type_inconnu}, 470, 36, 73, 115, 100, 144, 20)

Pokemon_Goupelin.ajouter_attaque(Attaque_feu)
Pokemon_Amphinobi.ajouter_attaque(Attaque_eau)
Pokemon_Xernéas.ajouter_attaque(Attaque_fée)
Pokemon_Tokodombi.ajouter_attaque(Attaque_Ténèbres)
Pokemon_neduj.ajouter_attaque(Attaque_Dragon)
Pokemon_Solgaléo.ajouter_attaque(Attaque_Psy)
Pokemon_Norman.ajouter_attaque(Attaque_Inconnu)

Pokemon_disponible = [Pokemon_Goupelin, Pokemon_Amphinobi, Pokemon_Xernéas, Pokemon_Tokodombi, Pokemon_neduj, Pokemon_Solgaléo, Pokemon_Norman]
