from random import *

class Joueur:

    def __init__(self, nom, manche_gagnee, argent):
        self.nom = nom
        self.manche_gagnee = manche_gagnee
        self.argent = argent
        self.pokemons = []

    def choisir_pokemon(self, pokemons_disponibles):
        
        print("Liste des Pokemons disponibles:")
        for i, pokemon in enumerate(pokemons_disponibles):
            print(f"{i + 1}. {pokemon.nom}")
        choix = int(input("Choisissez un numéro de Pokemon: ")) - 1
        pokemon_choisi = pokemons_disponibles[choix]
        self.pokemons.append(pokemon_choisi)
        pokemons_disponibles.remove(pokemon_choisi)
    
    def ajouter_pokemon(self, pokemon):

        if len(self.pokemons) < 3:
            self.pokemons.append(pokemon)
            print(f"{pokemon.nom} a été ajouté à votre équipe !")
        else:
            print("Vous avez déjà 3 Pokémon dans votre équipe.")

    def choisir_attaque(self, pokemon):

        print(f"Liste des attaques de {pokemon.nom}:")
        for i, attaque in enumerate(pokemon.attaques):
            print(f"{i + 1}. {attaque.nom}")

        choix = int(input("Choisissez un numéro d'attaque: ")) - 1
        if 0 <= choix < len(pokemon.attaques):
            return pokemon.attaques[choix]
        else:
            print("Numéro d'attaque invalide. Veuillez choisir à nouveau.")
            return self.choisir_attaque(pokemon)
        
    """def recuperer_pokemon(self, pokemon):
        return self.pokemon()"""

    def afficher_pokemon(self, pokemon):

        print("Pokémons dans l'équipe de", self.nom + ":")
        for i in range(1, len(self.pokemons)- 1):
            print(f"Nom: {pokemon.nom}, Prix: {pokemon.prix}, type: {pokemon.type}, PV: {pokemon.point_de_vie}, Niveau: {pokemon.niveau}, Attaque: {pokemon.attaque}, Attaque spéciale: {pokemon.attaque_speciale}, Défense: {pokemon.defense}, Défense spéciale: {pokemon.defense_speciale}, Vitesse: {pokemon.vitesse}")

    def afficher(self):
        print(f"Nom: {self.nom}, Manche gagnée: {self.manche_gagnee}, Argent: {self.argent}")


class Pokemon:

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
        self.attaques = []

    def ajouter_attaque(self, attaque):
        if len(self.attaques) < 3:
            self.attaques.append(attaque)
            print(f"{attaque.nom} a été ajouté à pokémon !")
        else:
            print("Vous avez déjà 3 attaques pour ce pokémon.")

    def attaquer(self, pokemon, attaque):
        return pokemon, attaque
    
    def est_ko(self, pokemon):
        if pokemon.point_de_vie < 0:
            return True
        else:
            return False
        
    def afficher_attaques(self, attaque):
        print("Attaques du pokémon", self.nom + ":")
        for i in range(1, len(self.attaques)- 1):
            print(f"Nom: {attaque.nom}, type: {attaque.type},  Catégorie: {attaque.categorie_attaque}, Précision: {attaque.precision}, Puissance: {attaque.puissance}, PP: {attaque.pp}")

    def afficher(self, pokemon):
        for i in range(1, len(self.pokemons)- 1):
            print(f"Nom: {pokemon.nom}, Prix: {pokemon.prix}, type: {pokemon.type}, PV: {pokemon.point_de_vie}, Niveau: {pokemon.niveau}, Attaque: {pokemon.attaque}, Attaque spéciale: {pokemon.attaque_speciale}, Défense: {pokemon.defense}, Défense spéciale: {pokemon.defense_speciale}, Vitesse: {pokemon.vitesse}")


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
"""
type_feu = type("feu")
type_eau = type("Eau")
type_fée = type("Fée")
type_ténèbres = type("ténèbres")
type_Dragon = type("dragon")
type_Psy = type("Psy")
type_inconnu = type("Inconnu")

Attaque_feu = Attaque("Nitrocharge", type_feu, "Physique", 50, 100, 20)
Attaque_eau =Attaque("Sheauriken", type_eau, "Physique", 100, 15, 20)
Attaque_fée = Attaque("Eclair magique", type_fée, "Spécial", 80, 100, 10)
Attaque_Ténèbres = Attaque("Bombe puante", type_ténèbres, "Spécial", 100, 70, 8)
Attaque_Dragon = Attaque("Dragon céleste", type_Dragon, "Spécial", 100, 228422, 22842 )
Attaque_Psy = Attaque("Boutefeu", type_fée, "Spécial", 100, 120, 15)
Attaque_Inconnu = Attaque("Enfantin", type_inconnu, "Physique", 50, 6000, 2)

Pokemon_Goupelin = Pokemon("Goupelin", 75, [type_feu], 354, 46, 69, 72, 74, 100 , 104)
Pokemon_Amphinobi = Pokemon("Amphinobi", 80, [type_eau], 348, 50, 95, 67, 103, 71, 122)
Pokemon_Xernéas = Pokemon("Xernéas", 100, [type_fée], 456, 20, 131, 95, 131, 98, 99)
Pokemon_Tokodombi = Pokemon("Toko dombi", 10, [type_ténèbres], 1492, 105, 60, 60, 70, 95)
Pokemon_neduj = Pokemon("neduj", 1000, [type_Dragon], 374, 1, 73, 70, 73, 115 , 67)
Pokemon_Solgaléo = Pokemon("Solgaléo", 120, [type_Psy], 478, 15, 137, 107, 113, 89, 97)
Pokemon_Norman = Pokemon("Norman", 16, {type_inconnu}, 470, 36, 73, 115, 100, 144, 20)

Pokemon_Goupelin.ajouter_attaque(Attaque_feu)
Pokemon_Amphinobi.ajouter_attaque(Attaque_eau)
Pokemon_Xernéas.ajouter_attaque(Attaque_fée)
Pokemon_Tokodombi.ajouter_attaque(Attaque_Ténèbres)
Pokemon_neduj.ajouter_attaque(Attaque_Dragon)
Pokemon_Solgaléo.ajouter_attaque(Attaque_Psy)
Pokemon_Norman.ajouter_attaque(Attaque_Inconnu)

Pokemon_disponible = [Pokemon_Goupelin, Pokemon_Amphinobi, Pokemon_Xernéas, Pokemon_Tokodombi, Pokemon_neduj, Pokemon_Solgaléo, Pokemon_Norman]
"""