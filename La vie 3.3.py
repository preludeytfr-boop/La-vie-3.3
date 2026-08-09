#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════╗
║          La vie    ║
╚══════════════════════════════════════════════════════════════════════╝
"""

import random
import time
import os
import sys
import json
import math

# ═══════════════════════════════════════════════════════════════════════
#  DONNÉES DE BASE
# ═══════════════════════════════════════════════════════════════════════

COUNTRIES = [
    "France", "USA", "Canada", "Japon", "Brésil", "Australie",
    "Allemagne", "Maroc", "Russie", "Chine", "Italie", "Espagne",
    "Mexique", "Argentine", "Suisse", "Émirats Arabes Unis", "Singapour"
]

SUBJECTS = [
    "Mathématiques", "Français", "Sciences", "Arts", "Sport",
    "Musique", "Informatique", "Droit", "Économie", "Philosophie"
]

PET_TYPES = ["Chien", "Chat", "Hamster", "Perroquet", "Serpent",
             "Tigre", "Lion", "Dauphin", "Cheval", "Tortue géante"]

FIRST_NAMES_M = [
    "Jean", "Pierre", "Marc", "Thomas", "Lucas", "Adam", "Arthur",
    "Kevin", "David", "Ryan", "Luca", "Matteo", "Hugo", "Théo",
    "Maxime", "Antoine", "Baptiste", "Clément", "Raphaël", "Alexis"
]
FIRST_NAMES_F = [
    "Marie", "Sophie", "Julie", "Léa", "Emma", "Chloé", "Sarah",
    "Inès", "Camille", "Zoé", "Clara", "Lucie", "Alice", "Manon",
    "Jade", "Lola", "Anaïs", "Pauline", "Laura", "Margot"
]
LAST_NAMES = [
    "Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard",
    "Petit", "Durand", "Leroy", "Moreau", "Simon", "Laurent",
    "Lefebvre", "Michel", "Garcia", "David", "Bertrand", "Roux",
    "Vincent", "Fournier"
]

# ─── Marchés boursiers ───────────────────────────────────────────────
STOCKS = {
    "TechCorp":    {"price": 100,  "volatility": 0.20, "sector": "Tech"},
    "GreenEnergy": {"price": 50,   "volatility": 0.40, "sector": "Énergie"},
    "OilGiant":    {"price": 200,  "volatility": 0.10, "sector": "Pétrole"},
    "BioHealth":   {"price": 75,   "volatility": 0.50, "sector": "Santé"},
    "SpaceXplore": {"price": 500,  "volatility": 0.60, "sector": "Aérospatial"},
    "LuxuryGroup": {"price": 350,  "volatility": 0.15, "sector": "Luxe"},
    "CryptoChain": {"price": 1000, "volatility": 0.90, "sector": "Crypto"},
    "AgriFood":    {"price": 80,   "volatility": 0.25, "sector": "Agroalimentaire"},
    "MediaStream": {"price": 120,  "volatility": 0.35, "sector": "Médias"},
    "RealEstateFund": {"price": 60, "volatility": 0.12, "sector": "Immobilier"},
}

# ─── Catalogue de biens de luxe ──────────────────────────────────────
LUXURY_VEHICLES = {
    "Voitures": [
        {"name": "Renault Clio",     "price": 15_000,    "maintenance": 800,   "insurance": 600,   "prestige": 1},
        {"name": "BMW Série 3",      "price": 45_000,    "maintenance": 2_000, "insurance": 1_500, "prestige": 3},
        {"name": "Porsche 911",      "price": 130_000,   "maintenance": 5_000, "insurance": 4_000, "prestige": 7},
        {"name": "Ferrari 488",      "price": 280_000,   "maintenance": 15_000,"insurance": 12_000,"prestige": 12},
        {"name": "Bugatti Chiron",   "price": 3_000_000, "maintenance": 50_000,"insurance": 80_000,"prestige": 20},
        {"name": "Lamborghini Urus", "price": 220_000,   "maintenance": 12_000,"insurance": 10_000,"prestige": 11},
    ],
    "Yachts": [
        {"name": "Voilier 8m",       "price": 80_000,    "maintenance": 5_000, "insurance": 3_000, "prestige": 4},
        {"name": "Yacht 20m",        "price": 500_000,   "maintenance": 30_000,"insurance": 20_000,"prestige": 10},
        {"name": "Superyacht 50m",   "price": 5_000_000, "maintenance": 200_000,"insurance": 150_000,"prestige": 18},
        {"name": "Mégayacht 100m",   "price": 50_000_000,"maintenance": 1_000_000,"insurance": 800_000,"prestige": 25},
    ],
    "Avions": [
        {"name": "Cessna 172",       "price": 300_000,   "maintenance": 20_000,"insurance": 15_000,"prestige": 6},
        {"name": "Jet Privé Léger",  "price": 3_000_000, "maintenance": 150_000,"insurance": 100_000,"prestige": 14},
        {"name": "Gulfstream G700",  "price": 75_000_000,"maintenance": 2_000_000,"insurance": 1_500_000,"prestige": 22},
        {"name": "Airbus A380 Privé","price": 400_000_000,"maintenance": 10_000_000,"insurance": 8_000_000,"prestige": 30},
    ],
}

LUXURY_COLLECTIBLES = {
    "Montres": [
        {"name": "Swatch",           "price": 100,       "appreciation": 0.00, "prestige": 0},
        {"name": "Tissot",           "price": 500,       "appreciation": 0.02, "prestige": 1},
        {"name": "TAG Heuer",        "price": 3_000,     "appreciation": 0.03, "prestige": 2},
        {"name": "Rolex Submariner", "price": 12_000,    "appreciation": 0.08, "prestige": 5},
        {"name": "Patek Philippe",   "price": 80_000,    "appreciation": 0.12, "prestige": 9},
        {"name": "Richard Mille",    "price": 500_000,   "appreciation": 0.15, "prestige": 14},
    ],
    "Bijoux": [
        {"name": "Bague argent",     "price": 200,       "appreciation": 0.01, "prestige": 0},
        {"name": "Collier or",       "price": 2_000,     "appreciation": 0.04, "prestige": 2},
        {"name": "Diamant 1 carat",  "price": 10_000,    "appreciation": 0.06, "prestige": 4},
        {"name": "Parure Cartier",   "price": 50_000,    "appreciation": 0.09, "prestige": 8},
        {"name": "Collier Hope",     "price": 250_000,   "appreciation": 0.10, "prestige": 13},
    ],
    "Instruments": [
        {"name": "Guitare acoustique","price": 300,      "appreciation": 0.01, "prestige": 1},
        {"name": "Piano Steinway",   "price": 80_000,    "appreciation": 0.05, "prestige": 6},
        {"name": "Stradivarius",     "price": 5_000_000, "appreciation": 0.20, "prestige": 20},
        {"name": "Orgue Hammond",    "price": 15_000,    "appreciation": 0.03, "prestige": 4},
    ],
}

REAL_ESTATE_CATALOG = [
    {"name": "Studio",          "price": 100_000,   "rent": 500,   "maintenance": 200,  "prestige": 1},
    {"name": "Appartement T3",  "price": 250_000,   "rent": 1_200, "maintenance": 400,  "prestige": 2},
    {"name": "Maison",          "price": 500_000,   "rent": 2_500, "maintenance": 800,  "prestige": 4},
    {"name": "Villa",           "price": 2_000_000, "rent": 8_000, "maintenance": 3_000,"prestige": 8},
    {"name": "Manoir",          "price": 8_000_000, "rent": 25_000,"maintenance": 10_000,"prestige": 14},
    {"name": "Château",         "price": 30_000_000,"rent": 80_000,"maintenance": 40_000,"prestige": 20},
    {"name": "Penthouse NYC",   "price": 15_000_000,"rent": 50_000,"maintenance": 20_000,"prestige": 18},
    {"name": "Île privée",      "price": 100_000_000,"rent": 0,    "maintenance": 200_000,"prestige": 30},
]

VACATION_DESTINATIONS = [
    {"name": "Week-end à Paris",    "cost": 500,     "happiness": 10, "fame": 0},
    {"name": "Ibiza",               "cost": 2_000,   "happiness": 20, "fame": 2},
    {"name": "Maldives",            "cost": 10_000,  "happiness": 30, "fame": 5},
    {"name": "Safari Kenya",        "cost": 15_000,  "happiness": 35, "fame": 5},
    {"name": "Tour du monde",       "cost": 80_000,  "happiness": 50, "fame": 10},
    {"name": "Station spatiale",    "cost": 5_000_000,"happiness": 80,"fame": 30},
]

RESTAURANT_TYPES = [
    {"name": "Fast-food",           "cost": 10,      "happiness": 3},
    {"name": "Brasserie",           "cost": 50,      "happiness": 8},
    {"name": "Restaurant gastronomique","cost": 300, "happiness": 15},
    {"name": "Table étoilée Michelin","cost": 1_000, "happiness": 25},
    {"name": "Dîner privé chef",    "cost": 10_000,  "happiness": 40},
]

NIGHTCLUB_EVENTS = [
    "Vous avez passé une nuit folle en boîte.",
    "Vous avez rencontré une célébrité en boîte.",
    "Vous avez dansé jusqu'à l'aube.",
    "Vous avez organisé une soirée VIP.",
    "Un scandale a éclaté lors de votre soirée.",
]

# ─── Modèles d'entreprise ─────────────────────────────────────────────
BUSINESS_MODELS = {
    "Startup Tech":     {"startup_cost": 50_000,   "growth_rate": (0.05, 0.50), "risk": 0.40, "ipo_mult": 8},
    "Franchise":        {"startup_cost": 200_000,  "growth_rate": (0.03, 0.15), "risk": 0.15, "ipo_mult": 4},
    "Industrie Lourde": {"startup_cost": 5_000_000,"growth_rate": (0.02, 0.10), "risk": 0.10, "ipo_mult": 3},
    "Agence":           {"startup_cost": 30_000,   "growth_rate": (0.04, 0.25), "risk": 0.25, "ipo_mult": 5},
    "Foncière":         {"startup_cost": 1_000_000,"growth_rate": (0.03, 0.12), "risk": 0.08, "ipo_mult": 3},
    "Restaurant":       {"startup_cost": 80_000,   "growth_rate": (0.02, 0.20), "risk": 0.30, "ipo_mult": 3},
    "Médias/Streaming": {"startup_cost": 100_000,  "growth_rate": (0.05, 0.60), "risk": 0.45, "ipo_mult": 10},
    "Pharma/Biotech":   {"startup_cost": 2_000_000,"growth_rate": (0.01, 0.80), "risk": 0.55, "ipo_mult": 12},
}

C_LEVEL_ROLES = ["CEO", "CFO", "CTO", "COO", "CMO", "CHRO"]

CRISIS_TYPES = [
    "Scandale financier",
    "Grève générale des employés",
    "Rappel massif de produits",
    "Cyberattaque majeure",
    "Enquête réglementaire",
    "Faillite d'un fournisseur clé",
    "Catastrophe industrielle",
    "Procès collectif",
]

# ─── Voies académiques spécialisées ──────────────────────────────────
SPECIALIZED_SCHOOLS = [
    {"name": "École Militaire",    "cost": 0,       "duration": 4, "edu_level": 3, "bonus": "militaire",  "req_health": 80},
    {"name": "Conservatoire",      "cost": 5_000,   "duration": 4, "edu_level": 3, "bonus": "musique",    "req_smarts": 50},
    {"name": "École des Beaux-Arts","cost": 3_000,  "duration": 3, "edu_level": 3, "bonus": "arts",       "req_smarts": 40},
    {"name": "Grande École de Commerce","cost": 30_000,"duration": 5,"edu_level": 4,"bonus": "commerce",  "req_smarts": 75},
    {"name": "École d'Ingénieurs", "cost": 20_000,  "duration": 5, "edu_level": 4, "bonus": "ingénierie", "req_smarts": 80},
    {"name": "Académie Sportive",  "cost": 2_000,   "duration": 3, "edu_level": 2, "bonus": "sport",      "req_health": 85},
    {"name": "École de Cinéma",    "cost": 15_000,  "duration": 3, "edu_level": 3, "bonus": "cinéma",     "req_looks": 60},
    {"name": "Université de Droit","cost": 10_000,  "duration": 5, "edu_level": 4, "bonus": "droit",      "req_smarts": 70},
]

# ─── Événements aléatoires enrichis ──────────────────────────────────
RANDOM_EVENTS_POOL = [
    {"text": "On vous propose une cigarette étrange.",    "type": "addict",   "val": "Drogues",    "prob": 0.3},
    {"text": "On vous propose un verre de whisky.",       "type": "addict",   "val": "Alcool",     "prob": 0.3},
    {"text": "Vous ressentez une douleur thoracique.",    "type": "maladie",  "val": "Problèmes Cardiaques","prob": 0.3},
    {"text": "Vous vous sentez triste sans raison.",      "type": "maladie",  "val": "Dépression", "prob": 0.3},
    {"text": "Un inconnu vous propose de l'argent.",      "type": "argent",   "val": 5000,         "prob": 0.3},
    {"text": "Vous trouvez un billet de loterie gagnant.","type": "loto",     "val": 0,            "prob": 0.05},
    {"text": "Vous êtes victime d'une arnaque en ligne.", "type": "vol",      "val": 2000,         "prob": 0.2},
    {"text": "Un ami vous propose d'investir dans sa startup.", "type": "invest", "val": 10000,   "prob": 0.25},
    {"text": "Vous êtes impliqué dans un accident de voiture.", "type": "accident","val": 0,      "prob": 0.1},
    {"text": "Vous recevez un héritage inattendu.",       "type": "heritage", "val": 0,            "prob": 0.05},
    {"text": "Un journaliste vous contacte pour un scandale.", "type": "scandale","val": 0,        "prob": 0.15},
    {"text": "Vous êtes convoqué au tribunal.",           "type": "proces",   "val": 0,            "prob": 0.1},
    {"text": "Votre maison est cambriolée.",              "type": "cambriolage","val": 0,          "prob": 0.08},
    {"text": "Vous rencontrez quelqu'un d'intéressant.",  "type": "rencontre","val": 0,            "prob": 0.3},
    {"text": "Vous gagnez un prix dans votre domaine.",   "type": "prix",     "val": 0,            "prob": 0.1},
]

# ═══════════════════════════════════════════════════════════════════════
#  CLASSES DE SOUTIEN (ORIGINALES + AMÉLIORÉES)
# ═══════════════════════════════════════════════════════════════════════

class Person:
    """Représente un PNJ avec jauge relationnelle, beauté, intelligence et autonomie."""
    def __init__(self, name, relation_type):
        self.name = name
        self.type = relation_type
        self.relationship = random.randint(40, 80)
        self.beauty = random.randint(20, 100)
        self.intelligence = random.randint(20, 100)
        self.is_alive = True
        self.money_given = 0
        self.age = random.randint(18, 60)
        self.job = random.choice(["Employé", "Médecin", "Artiste", "Entrepreneur", "Chômeur"])
        self.is_married = False
        self.has_diploma = random.random() < 0.5
        self.mood = random.choice(["Heureux", "Neutre", "Stressé", "Triste"])
        # Autonomie PNJ
        self._years_since_event = 0

    def autonomous_update(self):
        """Simule la vie autonome du PNJ chaque année."""
        self._years_since_event += 1
        self.age += 1
        # Chance de se marier
        if not self.is_married and self.age > 22 and random.random() < 0.05:
            self.is_married = True
        # Chance d'obtenir un diplôme
        if not self.has_diploma and self.age < 30 and random.random() < 0.03:
            self.has_diploma = True
        # Humeur fluctuante
        self.mood = random.choice(["Heureux", "Neutre", "Stressé", "Triste"])
        # Décès naturel
        if self.age > 75 and random.random() < 0.05:
            self.is_alive = False

    def __str__(self):
        status = "Marié(e)" if self.is_married else "Célibataire"
        return (f"{self.name} ({self.type}) | Âge: {self.age} | "
                f"Relation: {self.relationship}/100 | Beauté: {self.beauty} | "
                f"Intel: {self.intelligence} | {status} | Humeur: {self.mood}")


class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.type = pet_type
        self.relationship = 100
        self.age = 0
        self.health = 100


class Child(Person):
    def __init__(self, name, parent_name=""):
        super().__init__(name, "Enfant")
        self.age = 0
        self.parent_name = parent_name
        self.education_level = 0
        self.grades = random.randint(40, 90)
        self.is_playable = False  # Devient True pour l'héritage générationnel

    def grow_up(self):
        self.age += 1
        if self.age < 18:
            self.grades = max(0, min(100, self.grades + random.randint(-5, 8)))
        if self.age == 18:
            self.is_playable = True


class Partner(Person):
    def __init__(self, name, gender):
        super().__init__(name, "Partenaire")
        self.gender = gender
        self.loyalty = random.randint(30, 100)
        self.happiness = 70
        self.is_married = False
        self.is_engaged = False


class Colleague(Person):
    """PNJ collègue de travail avec interactions spécifiques."""
    def __init__(self, name, job_title):
        super().__init__(name, "Collègue")
        self.job_title = job_title
        self.is_seduced = False
        self.has_rumor = False


class ExPartner(Person):
    """Représente un ex-partenaire avec historique."""
    def __init__(self, name, gender, reason_breakup):
        super().__init__(name, "Ex")
        self.gender = gender
        self.reason_breakup = reason_breakup
        self.bitterness = random.randint(0, 100)


class Asset:
    """Bien patrimonial générique (véhicule, objet de collection, immobilier)."""
    def __init__(self, name, category, purchase_price, maintenance, insurance_cost, prestige, appreciation=0.0):
        self.name = name
        self.category = category
        self.purchase_price = purchase_price
        self.current_value = purchase_price
        self.maintenance = maintenance          # coût annuel
        self.insurance_cost = insurance_cost    # coût annuel
        self.prestige = prestige                # 0-30
        self.appreciation = appreciation        # taux annuel de valorisation
        self.is_insured = False
        self.age_years = 0
        self.is_on_display = False              # exposé dans zoo/musée

    def annual_update(self):
        """Mise à jour annuelle de la valeur."""
        self.age_years += 1
        # Appréciation ou dépréciation
        if self.appreciation > 0:
            self.current_value *= (1 + self.appreciation + random.uniform(-0.02, 0.02))
        else:
            # Dépréciation standard pour véhicules
            self.current_value *= random.uniform(0.92, 0.98)
        self.current_value = max(1, self.current_value)

    def __str__(self):
        insured = "Assuré" if self.is_insured else "Non assuré"
        return (f"{self.name} ({self.category}) | "
                f"Valeur: {self.current_value:,.0f}€ | "
                f"Entretien: {self.maintenance:,.0f}€/an | "
                f"Prestige: {self.prestige} | {insured}")


class RealEstateProperty:
    """Bien immobilier avec loyer, entretien et assurance."""
    def __init__(self, data):
        self.name = data["name"]
        self.purchase_price = data["price"]
        self.current_value = data["price"]
        self.rent = data["rent"]
        self.maintenance = data["maintenance"]
        self.prestige = data["prestige"]
        self.is_insured = False
        self.is_rented = False
        self.insurance_cost = int(data["price"] * 0.003)
        self.age_years = 0
        self.mortgage = 0  # dette hypothécaire restante

    def annual_update(self):
        self.age_years += 1
        # Marché immobilier aléatoire
        change = random.uniform(-0.05, 0.10)
        self.current_value *= (1 + change)
        if self.mortgage > 0:
            payment = min(self.mortgage, int(self.current_value * 0.05))
            self.mortgage -= payment

    def __str__(self):
        rented = "En location" if self.is_rented else "Résidence/Vide"
        insured = "Assuré" if self.is_insured else "Non assuré"
        return (f"{self.name} | Valeur: {self.current_value:,.0f}€ | "
                f"Loyer: {self.rent:,.0f}€/mois | {rented} | {insured}")


class Museum:
    """Musée personnel pour exposer les objets de collection."""
    def __init__(self, name):
        self.name = name
        self.items = []         # liste d'Asset
        self.admission_fee = 10
        self.visitors_per_year = 0
        self.prestige = 0
        self.operating_cost = 50_000  # annuel

    def add_item(self, asset):
        self.items.append(asset)
        asset.is_on_display = True
        self.prestige += asset.prestige

    def annual_revenue(self):
        self.visitors_per_year = int(self.prestige * 500 * random.uniform(0.8, 1.2))
        return self.visitors_per_year * self.admission_fee - self.operating_cost

    def __str__(self):
        return (f"Musée '{self.name}' | {len(self.items)} objets | "
                f"Prestige: {self.prestige} | "
                f"Visiteurs/an: {self.visitors_per_year:,}")


class Zoo:
    """Zoo personnel pour exposer les animaux exotiques."""
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.admission_fee = 20
        self.visitors_per_year = 0
        self.prestige = 0
        self.operating_cost = 100_000

    def add_animal(self, pet):
        self.animals.append(pet)
        exotic = ["Tigre", "Lion", "Dauphin", "Cheval", "Tortue géante"]
        self.prestige += 5 if pet.type in exotic else 1

    def annual_revenue(self):
        self.visitors_per_year = int(self.prestige * 1000 * random.uniform(0.8, 1.2))
        return self.visitors_per_year * self.admission_fee - self.operating_cost

    def __str__(self):
        return (f"Zoo '{self.name}' | {len(self.animals)} animaux | "
                f"Prestige: {self.prestige} | "
                f"Visiteurs/an: {self.visitors_per_year:,}")


# ─── Entreprise enrichie ─────────────────────────────────────────────

class Business:
    """Entreprise individuelle ou filiale d'une holding."""
    def __init__(self, name, model_name, startup_cost):
        self.name = name
        self.model_name = model_name
        model = BUSINESS_MODELS.get(model_name, BUSINESS_MODELS["Startup Tech"])
        self.value = startup_cost
        self.revenue = 0
        self.expenses = int(startup_cost * 0.1)
        self.employees = 1
        self.age = 0
        self.growth_rate = model["growth_rate"]
        self.risk = model["risk"]
        self.ipo_mult = model["ipo_mult"]
        self.is_public = False          # coté en bourse
        self.share_price = 0
        self.shares_outstanding = 0
        self.r_and_d_budget = 0
        self.c_level = {}               # {rôle: nom}
        self.crisis = None              # crise en cours
        self.crisis_turns = 0
        self.reputation = 70            # 0-100
        self.market_share = random.uniform(0.01, 0.05)
        self.dividends = 0
        self.debt = 0
        self.cash_reserve = startup_cost * 0.2

    def annual_update(self):
        """Calcul des revenus annuels de l'entreprise."""
        self.age += 1
        # Croissance
        low, high = self.growth_rate
        growth = random.uniform(low, high)
        # Bonus R&D
        if self.r_and_d_budget > 0:
            growth += self.r_and_d_budget / self.value * 0.5
        # Malus crise
        if self.crisis:
            growth -= 0.30
            self.reputation -= 10
            self.crisis_turns -= 1
            if self.crisis_turns <= 0:
                self.crisis = None
        # Calcul profit
        self.revenue = int(self.value * growth)
        self.expenses = int(self.value * 0.05) + self.r_and_d_budget
        profit = self.revenue - self.expenses
        self.value = max(1000, self.value + profit)
        self.cash_reserve += profit
        # Dividendes si coté
        if self.is_public:
            self.dividends = int(profit * 0.30)
            self.share_price = self.value / max(1, self.shares_outstanding)
        # Chance de crise
        if not self.crisis and random.random() < self.risk * 0.1:
            self.crisis = random.choice(CRISIS_TYPES)
            self.crisis_turns = random.randint(1, 3)
        return profit

    def launch_ipo(self):
        """Introduction en bourse."""
        if self.is_public:
            return 0, "Déjà cotée en bourse."
        self.is_public = True
        self.shares_outstanding = 1_000_000
        self.share_price = self.value * self.ipo_mult / self.shares_outstanding
        proceeds = int(self.share_price * self.shares_outstanding * 0.20)
        self.value += proceeds
        return proceeds, f"IPO réussie ! Prix par action : {self.share_price:.2f}€"

    def hire_c_level(self, role, name):
        self.c_level[role] = name
        bonus = {"CEO": 0.05, "CFO": 0.03, "CTO": 0.08, "COO": 0.04, "CMO": 0.06, "CHRO": 0.02}
        return bonus.get(role, 0.02)

    def __str__(self):
        public = f"[COTÉE: {self.share_price:.2f}€/action]" if self.is_public else ""
        crisis = f" ⚠ CRISE: {self.crisis}" if self.crisis else ""
        return (f"{self.name} ({self.model_name}) | "
                f"Valeur: {self.value:,.0f}€ | "
                f"Employés: {self.employees} | "
                f"Réputation: {self.reputation}{public}{crisis}")


class Holding:
    """Holding regroupant plusieurs entreprises."""
    def __init__(self, name):
        self.name = name
        self.subsidiaries = []      # liste de Business
        self.total_value = 0
        self.consolidated_revenue = 0
        self.tax_rate = 0.25

    def add_subsidiary(self, business):
        self.subsidiaries.append(business)

    def annual_consolidation(self):
        """Consolide les résultats annuels de toutes les filiales."""
        total_profit = 0
        self.total_value = 0
        self.consolidated_revenue = 0
        for b in self.subsidiaries:
            profit = b.annual_update()
            total_profit += profit
            self.total_value += b.value
            self.consolidated_revenue += b.revenue
        after_tax = int(total_profit * (1 - self.tax_rate))
        return after_tax

    def __str__(self):
        return (f"Holding '{self.name}' | "
                f"{len(self.subsidiaries)} filiales | "
                f"Valeur totale: {self.total_value:,.0f}€")


class Party:
    def __init__(self, name, ideology):
        self.name = name
        self.ideology = ideology
        self.members = 1
        self.funds = 0
        self.popularity = 10


# ─── Testament ────────────────────────────────────────────────────────

class Testament:
    """Testament du personnage pour la transmission de patrimoine."""
    def __init__(self):
        self.heirs = {}         # {nom: pourcentage}
        self.special_bequests = []  # [(objet, bénéficiaire)]
        self.is_written = False

    def add_heir(self, name, percentage):
        self.heirs[name] = percentage

    def __str__(self):
        if not self.is_written:
            return "Aucun testament rédigé."
        lines = ["Testament :"]
        for name, pct in self.heirs.items():
            lines.append(f"  {name}: {pct}%")
        return "\n".join(lines)


# ═══════════════════════════════════════════════════════════════════════
#  CLASSE PRINCIPALE DU PERSONNAGE (ÉTENDUE)
# ═══════════════════════════════════════════════════════════════════════

class Character:
    def __init__(self, name, gender, country):
        self.name = name
        self.gender = gender
        self.country = country
        self.age = 0
        self.is_alive = True
        self.cause_of_death = ""

        # ─ Stats de base ─────────────────────────────────────────────
        self.happiness = random.randint(60, 95)
        self.health = random.randint(80, 100)
        self.smarts = random.randint(20, 100)
        self.looks = random.randint(20, 100)
        self.fertility = random.randint(50, 100)
        self.fame = 0
        self.stress = 0             # 0-100
        self.charisma = random.randint(20, 80)
        self.fitness = random.randint(20, 80)
        self.karma = 50             # 0-100

        # ─ Finances ──────────────────────────────────────────────────
        self.bank_balance = 0
        self.salary = 0
        self.portfolio = {name: 0 for name in STOCKS}
        self.real_estate = []           # liste de RealEstateProperty
        self.assets = []                # liste d'Asset (véhicules, luxe, etc.)
        self.business = None            # Business principal (rétrocompat)
        self.holding = None             # Holding
        self.debt = 0
        self.credit_score = random.randint(600, 850)
        self.insurance_policies = {}    # {type: coût annuel}
        self.loto_tickets = 0

        # ─ Social ────────────────────────────────────────────────────
        self.partner = None
        self.children = []
        self.parents = [
            Person(f"{random.choice(FIRST_NAMES_M)} {name.split()[-1]}", "Père"),
            Person(f"{random.choice(FIRST_NAMES_F)} {name.split()[-1]}", "Mère")
        ]
        self.siblings = [
            Person(
                f"{random.choice(FIRST_NAMES_M if random.random() > 0.5 else FIRST_NAMES_F)} {name.split()[-1]}",
                "Frère/Sœur"
            ) for _ in range(random.randint(0, 3))
        ]
        self.friends = []
        self.pets = []
        self.lovers = []
        self.colleagues = []
        self.ex_partners = []
        self.in_laws = []               # belle-famille
        self.mail_order_spouses = []    # épouses/époux par correspondance

        # ─ Scolarité ─────────────────────────────────────────────────
        self.favorite_subject = random.choice(SUBJECTS)
        self.grades = random.randint(50, 90)
        self.specialized_school = None
        self.driver_license = False
        self.driver_license_age = None

        # ─ Carrière ──────────────────────────────────────────────────
        self.job = None
        self.education_level = 0
        self.education_name = "Aucune"
        self.career_type = None         # "militaire", "athlète", "freelance", "temps_partiel", etc.
        self.military_rank = 0
        self.athlete_sport = None
        self.freelance_clients = 0
        self.work_performance = 70      # 0-100
        self.raise_attempts = 0
        self.political_rank = 0
        self.political_party = None
        self.public_approval = 50
        self.laws_passed = []
        self.years_in_job = 0

        # ─ Légal ─────────────────────────────────────────────────────
        self.criminal_record = False
        self.in_prison = False
        self.prison_years = 0
        self.lawsuits = []              # procès en cours
        self.fines = 0

        # ─ Santé avancée ─────────────────────────────────────────────
        self.addictions = []
        self.diseases = []
        self.mental_health = 80         # 0-100
        self.bmi = random.uniform(18, 28)
        self.last_checkup = 0

        # ─ Réseaux sociaux & célébrité ───────────────────────────────
        self.social_media = {
            "Instagram": {"followers": 0, "active": False},
            "TikTok":    {"followers": 0, "active": False},
            "YouTube":   {"followers": 0, "active": False},
        }
        self.is_verified = False

        # ─ Patrimoine & collections ───────────────────────────────────
        self.museum = None
        self.zoo = None
        self.testament = Testament()
        self.prestige_score = 0         # somme des prestige de tous les assets

        # ─ Journal ───────────────────────────────────────────────────
        self.logs = [f"Vous êtes né(e) à {country}."]
        self.life_events = []           # événements marquants

    # ─── Calcul du prestige total ─────────────────────────────────────
    def compute_prestige(self):
        score = 0
        for a in self.assets:
            score += a.prestige
        for r in self.real_estate:
            score += r.prestige
        if self.museum:
            score += self.museum.prestige // 2
        if self.zoo:
            score += self.zoo.prestige // 2
        self.prestige_score = score
        return score

    # ─── Coûts annuels du patrimoine ─────────────────────────────────
    def annual_patrimony_costs(self):
        total_cost = 0
        total_income = 0
        for a in self.assets:
            a.annual_update()
            total_cost += a.maintenance
            if a.is_insured:
                total_cost += a.insurance_cost
        for r in self.real_estate:
            r.annual_update()
            total_cost += r.maintenance
            if r.is_insured:
                total_cost += r.insurance_cost
            if r.is_rented:
                total_income += r.rent * 12
        if self.museum:
            rev = self.museum.annual_revenue()
            total_income += max(0, rev)
            if rev < 0:
                total_cost += abs(rev)
        if self.zoo:
            rev = self.zoo.annual_revenue()
            total_income += max(0, rev)
            if rev < 0:
                total_cost += abs(rev)
        return total_cost, total_income

    # ─── Affichage des statistiques ──────────────────────────────────
    def display_stats(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.in_prison:
            status = "EN PRISON"
        elif self.political_rank == 4:
            status = "PRÉSIDENT"
        elif self.career_type == "militaire":
            ranks = ["Soldat", "Caporal", "Sergent", "Lieutenant", "Capitaine", "Colonel", "Général"]
            status = f"Militaire - {ranks[min(self.military_rank, 6)]}"
        elif self.job:
            status = self.job['name']
        else:
            status = "Sans emploi"

        prestige = self.compute_prestige()
        net_worth = (self.bank_balance
                     + sum(a.current_value for a in self.assets)
                     + sum(r.current_value for r in self.real_estate)
                     + sum(STOCKS[s]['price'] * q for s, q in self.portfolio.items() if q > 0))

        print("╔" + "═"*68 + "╗")
        print(f"║ {self.name.upper():^66} ║")
        print(f"║ {self.gender + ' | ' + self.country + ' | ' + str(self.age) + ' ans':^66} ║")
        print(f"║ Statut : {status:^57} ║")
        print("╠" + "═"*68 + "╣")
        print(f"║ Solde bancaire : {self.bank_balance:>15,.0f} €".ljust(69) + "║")
        print(f"║ Patrimoine net : {net_worth:>15,.0f} €".ljust(69) + "║")
        if self.debt > 0:
            print(f"║ Dettes         : {self.debt:>15,.0f} €".ljust(69) + "║")
        print(f"║ Prestige       : {prestige:>15,}  pts".ljust(69) + "║")
        print(f"║ Famille : {len(self.children)} enfant(s) | Partenaire: {self.partner.name if self.partner else 'Aucun'}".ljust(69) + "║")
        if self.diseases:
            print(f"║ Maladies : {', '.join(self.diseases)}".ljust(69) + "║")
        if self.addictions:
            print(f"║ Addictions : {', '.join(self.addictions)}".ljust(69) + "║")
        total_followers = sum(p["followers"] for p in self.social_media.values())
        if total_followers > 0:
            verif = " ✔" if self.is_verified else ""
            print(f"║ Followers: {total_followers:,}{verif}".ljust(69) + "║")
        if self.holding:
            print(f"║ Holding: {self.holding.name} ({len(self.holding.subsidiaries)} filiales)".ljust(69) + "║")
        print("╠" + "═"*68 + "╣")
        self._draw_bar("BONHEUR  ", self.happiness)
        self._draw_bar("SANTÉ    ", self.health)
        self._draw_bar("INTELL.  ", self.smarts)
        self._draw_bar("BEAUTÉ   ", self.looks)
        self._draw_bar("STRESS   ", self.stress)
        self._draw_bar("MENTAL   ", self.mental_health)
        if self.fame > 0:
            self._draw_bar("CÉLÉBRITÉ", self.fame)
        print("╚" + "═"*68 + "╝")

    def _draw_bar(self, label, value):
        bar_len = 25
        val = max(0, min(100, int(value)))
        filled = int(val / 100 * bar_len)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"║  {label.ljust(10)} : [{bar}] {val:3d}%".ljust(69) + "║")

    # ─── Vieillissement annuel ────────────────────────────────────────
    def age_up(self, game):
        self.age += 1
        self.years_in_job += 1 if self.job else 0

        # Prison
        if self.in_prison:
            self.prison_years -= 1
            self.happiness -= 10
            self.health -= 5
            self.mental_health -= 8
            if self.prison_years <= 0:
                self.in_prison = False
                self.logs.append("Vous êtes sorti(e) de prison.")

        # Vieillissement naturel
        if self.age > 50:
            self.health -= random.randint(1, 3)
        if self.age > 70:
            self.health -= random.randint(2, 6)
        if self.age > 80:
            self.health -= random.randint(3, 10)

        # Stress et santé mentale
        if self.stress > 70:
            self.mental_health -= random.randint(2, 5)
            self.health -= 1
        if self.mental_health < 30 and "Dépression" not in self.diseases:
            self.diseases.append("Dépression")
            self.logs.append("Votre santé mentale s'est dégradée : vous souffrez de dépression.")

        # Maladies et addictions
        for d in self.diseases:
            self.health -= random.randint(2, 5)
            self.happiness -= 2
        for a in self.addictions:
            self.health -= random.randint(3, 7)
            self.happiness += random.randint(-5, 5)
            self.stress += 5

        # Procès en cours
        for lawsuit in self.lawsuits[:]:
            self.logs.append(f"Procès '{lawsuit['reason']}' en cours...")
            if random.random() < lawsuit.get('win_chance', 0.5):
                self.logs.append(f"Vous avez gagné le procès '{lawsuit['reason']}' !")
                self.lawsuits.remove(lawsuit)
            else:
                fine = lawsuit.get('fine', 10000)
                self.bank_balance -= fine
                self.logs.append(f"Procès perdu ! Amende : {fine:,.0f}€")
                self.lawsuits.remove(lawsuit)

        # Réseaux sociaux
        total_followers = 0
        for p in self.social_media.values():
            if p["active"]:
                p["followers"] = int(p["followers"] * 0.95)
                total_followers += p["followers"]

        # Pression célébrité
        if self.fame > 50 or total_followers > 1_000_000:
            self.happiness -= random.randint(2, 8)
            self.stress += 5
            if random.random() < 0.1 and "Dépression" not in self.diseases:
                self.diseases.append("Dépression")
                self.logs.append("La pression de la célébrité vous a plongé dans la dépression.")

        # Mort naturelle
        if self.health <= 0 or (self.age > 70 and random.random() < (self.age - 70) * 0.02):
            self.is_alive = False
            self.cause_of_death = "Causes naturelles"
            return

        # Famille et animaux
        for child in self.children:
            child.grow_up()
        for pet in self.pets[:]:
            pet.age += 1
            pet.health -= random.randint(2, 10)
            if pet.health <= 0:
                self.logs.append(f"Votre {pet.type} {pet.name} est décédé(e).")
                self.pets.remove(pet)
                self.happiness -= 20

        # Autonomie des PNJ
        for person in (self.parents + self.siblings + self.friends + self.colleagues):
            if person.is_alive:
                person.autonomous_update()
                if not person.is_alive:
                    self.logs.append(f"{person.name} ({person.type}) est décédé(e).")
                    self.happiness -= 15

        # Argent de poche (enfance)
        if self.age < 18:
            pocket_money = random.randint(5, 50)
            self.bank_balance += pocket_money
            self.logs.append(f"Vos parents vous ont donné {pocket_money}€ d'argent de poche.")

        # Revenus professionnels
        income = 0
        if self.job:
            income += self.job['salary']
            # Bonus performance
            if self.work_performance > 80:
                bonus = int(self.job['salary'] * 0.10)
                income += bonus
                self.logs.append(f"Bonus de performance : +{bonus:,.0f}€")
        if self.career_type == "freelance":
            freelance_income = self.freelance_clients * random.randint(2000, 8000)
            income += freelance_income
        if self.career_type == "temps_partiel" and self.job:
            income = int(income * 0.5)

        # Revenus immobiliers et patrimoniaux
        patrimony_costs, patrimony_income = self.annual_patrimony_costs()
        self.bank_balance -= patrimony_costs
        self.bank_balance += patrimony_income
        if patrimony_costs > 0:
            self.logs.append(f"Coûts patrimoniaux annuels : -{patrimony_costs:,.0f}€")
        if patrimony_income > 0:
            self.logs.append(f"Revenus patrimoniaux : +{patrimony_income:,.0f}€")

        # Holding
        if self.holding:
            holding_profit = self.holding.annual_consolidation()
            self.bank_balance += holding_profit
            if holding_profit > 0:
                self.logs.append(f"Holding '{self.holding.name}' : +{holding_profit:,.0f}€ de bénéfices nets.")
            # Crises dans les filiales
            for b in self.holding.subsidiaries:
                if b.crisis:
                    self.logs.append(f"⚠ Crise chez {b.name} : {b.crisis}")
        elif self.business:
            profit = int(self.business.value * random.uniform(-0.1, 0.3))
            self.bank_balance += profit
            self.business.value += profit
            self.business.age += 1
            if profit > 0:
                self.logs.append(f"Votre entreprise a généré {profit:,.0f}€ de bénéfices.")

        self.bank_balance += income

        # Bourse
        for stock, amount in self.portfolio.items():
            if amount > 0:
                change = random.uniform(-STOCKS[stock]['volatility'], STOCKS[stock]['volatility'])
                STOCKS[stock]['price'] = max(0.01, STOCKS[stock]['price'] * (1 + change))

        # Loto
        if self.loto_tickets > 0:
            for _ in range(self.loto_tickets):
                if random.random() < 0.000001:
                    win = random.randint(1_000_000, 50_000_000)
                    self.bank_balance += win
                    self.logs.append(f"🎉 JACKPOT LOTO ! Vous avez gagné {win:,.0f}€ !")
                    self.happiness += 50
            self.loto_tickets = 0

        # Stress naturel
        self.stress = max(0, self.stress - 5)

        # Événements aléatoires
        game.event_mgr.trigger_random_event(self)


# ═══════════════════════════════════════════════════════════════════════
#  MINI-JEUX TEXTUELS TACTIQUES
# ═══════════════════════════════════════════════════════════════════════

class MiniGame:
    """Collection de mini-jeux textuels pour les situations à risque."""

    @staticmethod
    def navigation_tempete():
        """Mini-jeu : naviguer lors d'une tempête en mer."""
        print("\n╔══════════════════════════════════════╗")
        print("║   TEMPÊTE EN MER — MINI-JEU          ║")
        print("╚══════════════════════════════════════╝")
        print("Votre yacht est pris dans une tempête violente !")
        print("Vous devez prendre 3 décisions rapides.\n")
        score = 0
        questions = [
            ("Que faites-vous en premier ?",
             ["Réduire les voiles", "Accélérer pour fuir", "Appeler les secours"],
             0),
            ("La coque commence à prendre l'eau. Vous...",
             ["Pompez l'eau", "Abandonnez le bateau", "Cherchez la fuite"],
             0),
            ("Le moteur lâche. Vous...",
             ["Utilisez les voiles de secours", "Paniquez", "Attendez"],
             0),
        ]
        for q, opts, correct in questions:
            print(f"→ {q}")
            for i, o in enumerate(opts):
                print(f"  {i+1}. {o}")
            ans = input("Votre choix : ").strip()
            if ans == str(correct + 1):
                score += 1
                print("  ✓ Bonne décision !\n")
            else:
                print(f"  ✗ Mauvais choix. La bonne réponse était : {opts[correct]}\n")
        return score

    @staticmethod
    def debat_politique(smarts, public_approval):
        """Mini-jeu : débat politique avec répliques."""
        print("\n╔══════════════════════════════════════╗")
        print("║   DÉBAT POLITIQUE — MINI-JEU         ║")
        print("╚══════════════════════════════════════╝")
        scenarios = [
            {
                "question": "Adversaire : 'Vous avez augmenté les impôts !'",
                "options": [
                    "C'est pour financer les services publics.",
                    "C'est faux, vérifiez vos chiffres.",
                    "Je n'ai rien à dire là-dessus.",
                ],
                "best": 0,
            },
            {
                "question": "Adversaire : 'Votre bilan économique est catastrophique !'",
                "options": [
                    "Nous avons créé 50 000 emplois cette année.",
                    "Vous mentez !",
                    "C'est une situation difficile pour tout le monde.",
                ],
                "best": 0,
            },
            {
                "question": "Journaliste : 'Que proposez-vous pour la jeunesse ?'",
                "options": [
                    "Un plan d'investissement massif dans l'éducation.",
                    "Je vais y réfléchir.",
                    "La jeunesse doit travailler plus dur.",
                ],
                "best": 0,
            },
        ]
        score = 0
        for s in scenarios:
            print(f"\n{s['question']}")
            for i, o in enumerate(s["options"]):
                print(f"  {i+1}. {o}")
            ans = input("Votre réplique : ").strip()
            if ans == str(s["best"] + 1):
                score += 1
                print("  ✓ Excellente réplique ! Le public applaudit.")
            else:
                print(f"  ✗ Réplique faible. Meilleure option : {s['options'][s['best']]}")
        approval_change = (score - 1) * 10
        return approval_change

    @staticmethod
    def negociation_affaires(smarts):
        """Mini-jeu : négociation commerciale."""
        print("\n╔══════════════════════════════════════╗")
        print("║   NÉGOCIATION — MINI-JEU             ║")
        print("╚══════════════════════════════════════╝")
        print("Vous négociez un contrat majeur.")
        target_price = random.randint(500_000, 5_000_000)
        print(f"Prix demandé par le client : {target_price:,.0f}€")
        print(f"Votre objectif : obtenir au moins {int(target_price * 0.85):,.0f}€\n")
        rounds = 3
        current_offer = int(target_price * 0.70)
        for r in range(rounds):
            print(f"Tour {r+1}/{rounds} — Offre actuelle : {current_offer:,.0f}€")
            print("1. Accepter | 2. Contre-proposer | 3. Bluffer | 4. Abandonner")
            choice = input("> ").strip()
            if choice == "1":
                print(f"Contrat signé pour {current_offer:,.0f}€ !")
                return current_offer
            elif choice == "2":
                counter = int(input("Votre contre-proposition : ").replace(" ", "").replace(",", "") or "0")
                if counter >= target_price:
                    print("Le client accepte !")
                    return counter
                else:
                    current_offer = int((current_offer + counter) / 2)
                    print(f"Le client propose un compromis : {current_offer:,.0f}€")
            elif choice == "3":
                if random.random() < smarts / 150:
                    current_offer = int(current_offer * 1.15)
                    print(f"Bluff réussi ! Nouvelle offre : {current_offer:,.0f}€")
                else:
                    print("Bluff raté ! Le client est offensé.")
                    current_offer = int(current_offer * 0.90)
            elif choice == "4":
                print("Négociation abandonnée.")
                return 0
        print(f"Négociation terminée. Contrat final : {current_offer:,.0f}€")
        return current_offer

    @staticmethod
    def course_automobile():
        """Mini-jeu : circuit de course automobile."""
        print("\n╔══════════════════════════════════════╗")
        print("║   CIRCUIT DE COURSE — MINI-JEU       ║")
        print("╚══════════════════════════════════════╝")
        print("Vous participez à une course sur circuit !")
        print("Gérez 5 virages critiques.\n")
        position = 5  # départ en 5e position
        for i in range(5):
            print(f"Virage {i+1}/5 — Position actuelle : {position}e")
            print("1. Freiner tôt (sûr) | 2. Freiner tard (risqué) | 3. Couper la corde (très risqué)")
            choice = input("> ").strip()
            if choice == "1":
                position = max(1, position + random.randint(-1, 1))
            elif choice == "2":
                if random.random() < 0.6:
                    position = max(1, position - 2)
                    print("  Beau dépassement !")
                else:
                    position = min(10, position + 2)
                    print("  Trop risqué, vous perdez des places !")
            elif choice == "3":
                if random.random() < 0.35:
                    position = max(1, position - 3)
                    print("  Manœuvre audacieuse réussie !")
                else:
                    position = min(10, position + 3)
                    print("  Sortie de piste ! Vous perdez beaucoup de places.")
        prize = {1: 500_000, 2: 200_000, 3: 100_000}
        reward = prize.get(position, 10_000)
        print(f"\nRésultat final : {position}e place — Gain : {reward:,.0f}€")
        return position, reward


# ═══════════════════════════════════════════════════════════════════════
#  MOTEUR DE JEU PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════

class Game:
    def __init__(self):
        self.player = None
        self.event_mgr = EventManager()
        self.generation = 1
        self.dynasty_name = ""
        self.jobs = [
            {"name": "Ouvrier",            "salary": 22_000,    "req_edu": 2,  "req_smarts": 0},
            {"name": "Informaticien",      "salary": 55_000,    "req_edu": 3,  "req_smarts": 70,  "pref": "Informatique"},
            {"name": "Avocat",             "salary": 110_000,   "req_edu": 4,  "req_smarts": 80,  "pref": "Droit"},
            {"name": "Médecin",            "salary": 140_000,   "req_edu": 4,  "req_smarts": 90,  "pref": "Sciences"},
            {"name": "Designer",           "salary": 45_000,    "req_edu": 3,  "req_smarts": 50,  "pref": "Arts"},
            {"name": "Athlète Pro",        "salary": 200_000,   "req_edu": 2,  "req_health": 90,  "pref": "Sport"},
            {"name": "Trader",             "salary": 180_000,   "req_edu": 3,  "req_smarts": 85,  "pref": "Mathématiques"},
            {"name": "Écrivain",           "salary": 40_000,    "req_edu": 3,  "req_smarts": 60,  "pref": "Français"},
            {"name": "Star de Cinéma",     "salary": 1_000_000, "req_edu": 2,  "req_looks": 90,   "req_fame": 50},
            {"name": "Pop Star Mondiale",  "salary": 2_000_000, "req_edu": 2,  "req_looks": 85,   "req_fame": 60},
            {"name": "Militaire",          "salary": 30_000,    "req_edu": 2,  "req_health": 80,  "career": "militaire"},
            {"name": "Freelance",          "salary": 0,         "req_edu": 2,  "req_smarts": 50,  "career": "freelance"},
            {"name": "Temps Partiel",      "salary": 15_000,    "req_edu": 1,  "req_smarts": 0,   "career": "temps_partiel"},
            {"name": "Ingénieur",          "salary": 75_000,    "req_edu": 4,  "req_smarts": 75,  "pref": "Informatique"},
            {"name": "Architecte",         "salary": 65_000,    "req_edu": 4,  "req_smarts": 70,  "pref": "Arts"},
            {"name": "Chef Cuisinier",     "salary": 50_000,    "req_edu": 2,  "req_smarts": 40},
            {"name": "Pilote de Ligne",    "salary": 120_000,   "req_edu": 3,  "req_health": 85},
            {"name": "Journaliste",        "salary": 38_000,    "req_edu": 3,  "req_smarts": 65,  "pref": "Français"},
            {"name": "Professeur",         "salary": 35_000,    "req_edu": 4,  "req_smarts": 70},
            {"name": "Entrepreneur",       "salary": 0,         "req_edu": 2,  "req_smarts": 60,  "career": "entrepreneur"},
        ]

    # ─── Démarrage ────────────────────────────────────────────────────
    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔" + "═"*50 + "╗")
        print("║" + " La vie ".center(50) + "║")
        print("║" + " Version 3.3 ".center(50) + "║")
        print("╚" + "═"*50 + "╝\n")
        name = input("Nom complet de votre personnage : ").strip() or "Jean Dupont"
        gender_input = input("Genre (H/F) : ").upper().strip()
        gender = "Homme" if gender_input == "H" else "Femme"
        country = random.choice(COUNTRIES)
        self.dynasty_name = name.split()[-1] if " " in name else name
        self.player = Character(name, gender, country)
        print(f"\nBienvenue dans le monde, {name} ! Né(e) en {country}.")
        input("Appuyez sur Entrée pour commencer votre vie...")

        while self.player.is_alive:
            self._main_loop()

        self.end_game()

    def _main_loop(self):
        self.player.display_stats()
        if self.player.logs:
            print(f"\n📋 Journal : {self.player.logs[-1]}")

        print("\n" + "─"*40)
        print("1.  Vieillir (+1 an)")
        print("2.  Relations (Famille, Amis, Partenaire, Collègues)")
        print("3.  Activités & Santé & Bien-être")
        if self.player.age < 18:
            print("4.  École & Études")
        if self.player.age >= 16:
            print("5.  Permis de conduire")
        if self.player.age >= 18:
            print("6.  Carrière & Politique & Études supérieures")
            print("7.  Patrimoine (Biens, Véhicules, Collections)")
            print("8.  Business, Bourse & Holding")
            print("9.  Crime & Illégal")
            print("10. Réseaux Sociaux & Célébrité")
            print("11. Casino, Loto & Jeux")
            print("12. Vie Sociale (Boîte, Vacances, Restaurant)")
            print("13. Testament & Héritage")
        print("0.  Quitter")
        print("─"*40)

        choice = input("\nAction : ").strip()

        if choice == "1":
            self.player.age_up(self)
        elif choice == "2":
            self.menu_relations()
        elif choice == "3":
            self.menu_activites()
        elif choice == "4" and self.player.age < 18:
            self.menu_ecole()
        elif choice == "5" and self.player.age >= 16:
            self.menu_permis()
        elif choice == "6" and self.player.age >= 18:
            self.menu_carriere()
        elif choice == "7" and self.player.age >= 18:
            self.menu_patrimoine()
        elif choice == "8" and self.player.age >= 18:
            self.menu_economie()
        elif choice == "9" and self.player.age >= 18:
            self.menu_crime()
        elif choice == "10" and self.player.age >= 18:
            self.menu_reseaux_sociaux()
        elif choice == "11" and self.player.age >= 18:
            self.menu_casino()
        elif choice == "12" and self.player.age >= 18:
            self.menu_vie_sociale()
        elif choice == "13" and self.player.age >= 18:
            self.menu_testament()
        elif choice == "0":
            self.player.is_alive = False
            self.player.cause_of_death = "Retraite (fin de partie)"

    # ─── MENU RELATIONS ───────────────────────────────────────────────
    def menu_relations(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.player.display_stats()
            print("\n─── RELATIONS ───")
            print("1.  Parents")
            print("2.  Frères & Sœurs")
            print("3.  Amis")
            print("4.  Animaux de compagnie")
            print("5.  Partenaire / Amants")
            print("6.  Enfants")
            print("7.  Collègues")
            print("8.  Belle-famille")
            print("9.  Ex-partenaires")
            print("10. Époux/Épouse par correspondance")
            print("0.  Retour")

            c = input("Choix : ").strip()
            if c == "1":
                self.submenu_famille(self.player.parents)
            elif c == "2":
                self.submenu_famille(self.player.siblings)
            elif c == "3":
                self.submenu_amis()
            elif c == "4":
                self.submenu_animaux()
            elif c == "5":
                self.submenu_partenaire()
            elif c == "6":
                self.submenu_famille(self.player.children)
            elif c == "7":
                self.submenu_collegues()
            elif c == "8":
                self.submenu_belle_famille()
            elif c == "9":
                self.submenu_ex_partenaires()
            elif c == "10":
                self.submenu_epoux_correspondance()
            elif c == "0":
                break

    def submenu_famille(self, members):
        if not members:
            print("Aucun membre.")
            input("...")
            return
        for i, m in enumerate(members):
            alive = "" if m.is_alive else " [DÉCÉDÉ]"
            print(f"{i+1}. {m}{alive}")
        idx = input("Choisir quelqu'un (0 pour annuler) : ").strip()
        if not idx.isdigit() or int(idx) == 0:
            return
        idx = int(idx) - 1
        if idx >= len(members):
            return
        m = members[idx]
        if not m.is_alive:
            print(f"{m.name} est décédé(e).")
            input("...")
            return
        print(f"\nActions avec {m.name} :")
        print("1. Passer du temps ensemble (+Relation, +Bonheur)")
        print("2. Demander de l'argent")
        print("3. Offrir un cadeau (-Argent, +Relation)")
        print("4. Se disputer (-Relation)")
        print("5. Lancer une rumeur sur lui/elle")
        act = input("Action : ").strip()
        if act == "1":
            m.relationship = min(100, m.relationship + 10)
            self.player.happiness = min(100, self.player.happiness + 5)
            print(f"Moment agréable avec {m.name}. Relation : {m.relationship}/100")
        elif act == "2":
            if m.relationship > 70:
                gift = random.randint(10, 500)
                self.player.bank_balance += gift
                print(f"{m.name} vous a donné {gift}€ !")
            else:
                print(f"{m.name} a refusé. Améliorez votre relation d'abord.")
        elif act == "3":
            try:
                amount = int(input("Montant du cadeau (€) : "))
                if self.player.bank_balance >= amount:
                    self.player.bank_balance -= amount
                    m.relationship = min(100, m.relationship + int(amount / 50))
                    print(f"Cadeau offert ! Relation avec {m.name} : {m.relationship}/100")
                else:
                    print("Fonds insuffisants.")
            except ValueError:
                pass
        elif act == "4":
            m.relationship = max(0, m.relationship - 20)
            self.player.happiness -= 5
            print(f"Dispute avec {m.name}. Relation : {m.relationship}/100")
        elif act == "5":
            if random.random() < 0.5:
                m.relationship = max(0, m.relationship - 30)
                print(f"La rumeur sur {m.name} s'est répandue. Relation très endommagée.")
            else:
                print(f"La rumeur n'a pas pris. {m.name} a découvert votre tentative !")
                m.relationship = max(0, m.relationship - 10)
        input("...")

    def submenu_amis(self):
        print("\n─── AMIS ───")
        print(f"Vous avez {len(self.player.friends)} ami(s).")
        print("1. Chercher de nouveaux amis")
        print("2. Gérer mes amis")
        print("0. Retour")
        c = input("> ").strip()
        if c == "1":
            name = f"{random.choice(FIRST_NAMES_M if random.random() > 0.5 else FIRST_NAMES_F)} {random.choice(LAST_NAMES)}"
            if random.random() < (self.player.charisma / 100):
                self.player.friends.append(Person(name, "Ami"))
                print(f"Vous êtes maintenant ami(e) avec {name} !")
            else:
                print("Vous n'avez pas réussi à vous lier d'amitié.")
        elif c == "2":
            if self.player.friends:
                self.submenu_famille(self.player.friends)
            else:
                print("Vous n'avez pas encore d'amis.")
        input("...")

    def submenu_animaux(self):
        print("\n─── ANIMAUX DE COMPAGNIE ───")
        print("1. Acheter un animal")
        print("2. Voir mes animaux")
        print("3. Créer un zoo (si animaux exotiques)")
        print("0. Retour")
        c = input("> ").strip()
        if c == "1":
            print("Types disponibles :")
            for i, t in enumerate(PET_TYPES):
                print(f"  {i+1}. {t}")
            idx = input("Choisir : ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(PET_TYPES):
                t = PET_TYPES[int(idx) - 1]
                name = input(f"Nom pour votre {t} : ").strip() or t
                costs = {"Chien": 500, "Chat": 300, "Hamster": 50, "Perroquet": 200,
                         "Serpent": 400, "Tigre": 50_000, "Lion": 60_000,
                         "Dauphin": 100_000, "Cheval": 20_000, "Tortue géante": 30_000}
                cost = costs.get(t, 1000)
                if self.player.bank_balance >= cost:
                    self.player.bank_balance -= cost
                    self.player.pets.append(Pet(name, t))
                    print(f"Bienvenue à {name} le {t} !")
                else:
                    print(f"Fonds insuffisants. Coût : {cost:,.0f}€")
        elif c == "2":
            if not self.player.pets:
                print("Vous n'avez pas d'animaux.")
            for p in self.player.pets:
                print(f"- {p.name} ({p.type}) | Santé: {p.health}% | Âge: {p.age} ans")
                if input("  Passer du temps ? (o/n) ").strip().lower() == "o":
                    p.relationship = min(100, p.relationship + 10)
                    self.player.happiness = min(100, self.player.happiness + 5)
        elif c == "3":
            exotic = ["Tigre", "Lion", "Dauphin", "Cheval", "Tortue géante"]
            exotic_pets = [p for p in self.player.pets if p.type in exotic]
            if not exotic_pets:
                print("Vous n'avez pas d'animaux exotiques pour ouvrir un zoo.")
            elif self.player.zoo:
                print(f"Vous avez déjà un zoo : {self.player.zoo}")
            elif self.player.bank_balance >= 500_000:
                zoo_name = input("Nom de votre zoo : ").strip() or "Mon Zoo"
                self.player.bank_balance -= 500_000
                self.player.zoo = Zoo(zoo_name)
                for p in exotic_pets:
                    self.player.zoo.add_animal(p)
                print(f"Zoo '{zoo_name}' ouvert avec {len(exotic_pets)} animaux !")
            else:
                print("Il faut 500 000€ pour ouvrir un zoo.")
        input("...")

    def submenu_partenaire(self):
        p = self.player
        print("\n─── VIE AMOUREUSE ───")
        if p.partner:
            partner = p.partner
            print(f"Partenaire : {partner.name} | Relation: {partner.relationship}/100 | Fidélité: {partner.loyalty}/100")
            print("1. Passer du temps ensemble")
            print("2. Relations intimes (risque de grossesse)")
            print("3. Proposer les fiançailles")
            print("4. Se marier")
            print("5. Rompre")
            print("6. Tromper (aventure secrète)")
            print("7. Trio (si relation > 80)")
            print("8. Demander le divorce")
            act = input("> ").strip()
            if act == "1":
                partner.relationship = min(100, partner.relationship + 10)
                partner.happiness = min(100, partner.happiness + 10)
                p.happiness = min(100, p.happiness + 5)
                print(f"Moment romantique avec {partner.name}.")
            elif act == "2":
                if random.random() < (p.fertility / 100) * 0.3:
                    child_name = f"{random.choice(FIRST_NAMES_M if random.random() > 0.5 else FIRST_NAMES_F)} {p.name.split()[-1]}"
                    p.children.append(Child(child_name, p.name))
                    print(f"🍼 Naissance de {child_name} !")
                    p.happiness += 20
                else:
                    print("Pas de grossesse cette fois.")
            elif act == "3":
                if not partner.is_engaged:
                    if partner.relationship >= 70:
                        partner.is_engaged = True
                        print(f"{partner.name} a dit OUI aux fiançailles ! 💍")
                    else:
                        print(f"{partner.name} n'est pas encore prêt(e). Améliorez votre relation.")
                else:
                    print("Vous êtes déjà fiancé(e)s.")
            elif act == "4":
                if partner.is_engaged:
                    partner.is_married = True
                    p.in_laws = [
                        Person(f"{random.choice(FIRST_NAMES_M)} {partner.name.split()[-1]}", "Beau-père"),
                        Person(f"{random.choice(FIRST_NAMES_F)} {partner.name.split()[-1]}", "Belle-mère"),
                    ]
                    print(f"🎊 Félicitations ! Vous êtes marié(e) avec {partner.name} !")
                    p.happiness += 30
                else:
                    print("Vous devez d'abord vous fiancer.")
            elif act == "5":
                ex = ExPartner(partner.name, partner.gender, "Rupture volontaire")
                p.ex_partners.append(ex)
                p.partner = None
                p.happiness -= 15
                print("Vous êtes maintenant célibataire.")
            elif act == "6":
                lover_name = f"{random.choice(FIRST_NAMES_F if p.gender == 'Homme' else FIRST_NAMES_M)} {random.choice(LAST_NAMES)}"
                p.lovers.append(lover_name)
                if random.random() < 0.3:
                    partner.loyalty -= 30
                    partner.relationship -= 40
                    print(f"⚠ {partner.name} a découvert votre infidélité ! Relation très endommagée.")
                else:
                    print(f"Aventure secrète avec {lover_name}. Votre partenaire ne sait rien.")
                p.happiness += 10
            elif act == "7":
                if partner.relationship >= 80:
                    print("Soirée à trois... une expérience mémorable.")
                    p.happiness += 15
                    partner.relationship -= 5
                else:
                    print(f"{partner.name} n'est pas à l'aise avec cette idée.")
            elif act == "8":
                if partner.is_married:
                    cost = random.randint(5_000, 50_000)
                    print(f"Procédure de divorce. Coût estimé : {cost:,.0f}€")
                    if input("Confirmer ? (o/n) ").strip().lower() == "o":
                        p.bank_balance -= cost
                        ex = ExPartner(partner.name, partner.gender, "Divorce")
                        p.ex_partners.append(ex)
                        p.partner = None
                        p.happiness -= 20
                        print("Divorce prononcé.")
                else:
                    print("Vous n'êtes pas marié(e).")
        else:
            print("Vous êtes célibataire.")
            print("1. Chercher l'amour (rencontre classique)")
            print("2. Application de rencontres")
            print("3. Coup d'un soir")
            print("0. Retour")
            act = input("> ").strip()
            if act in ("1", "2"):
                chance = (p.looks + p.charisma) / 200
                if random.random() < chance:
                    name = f"{random.choice(FIRST_NAMES_F if p.gender == 'Homme' else FIRST_NAMES_M)} {random.choice(LAST_NAMES)}"
                    p.partner = Partner(name, "Femme" if p.gender == "Homme" else "Homme")
                    print(f"❤ Vous avez rencontré {name} !")
                else:
                    print("Pas de chance cette fois. Travaillez votre charme.")
            elif act == "3":
                name = f"{random.choice(FIRST_NAMES_F if p.gender == 'Homme' else FIRST_NAMES_M)} {random.choice(LAST_NAMES)}"
                p.lovers.append(name)
                p.happiness += 10
                if random.random() < 0.1:
                    child_name = f"{random.choice(FIRST_NAMES_M if random.random() > 0.5 else FIRST_NAMES_F)} {p.name.split()[-1]}"
                    p.children.append(Child(child_name, p.name))
                    print(f"Surprise ! Suite à cette nuit, {child_name} est né(e).")
                else:
                    print(f"Nuit mémorable avec {name}.")
        input("...")

    def submenu_collegues(self):
        print("\n─── COLLÈGUES ───")
        if not self.player.job:
            print("Vous n'avez pas d'emploi.")
            input("...")
            return
        if not self.player.colleagues:
            # Générer des collègues
            for _ in range(random.randint(2, 5)):
                name = f"{random.choice(FIRST_NAMES_M if random.random() > 0.5 else FIRST_NAMES_F)} {random.choice(LAST_NAMES)}"
                self.player.colleagues.append(Colleague(name, self.player.job['name']))
        for i, c in enumerate(self.player.colleagues):
            print(f"{i+1}. {c.name} | Relation: {c.relationship}/100 | Beauté: {c.beauty}")
        idx = input("Choisir un collègue (0 pour annuler) : ").strip()
        if not idx.isdigit() or int(idx) == 0:
            return
        idx = int(idx) - 1
        if idx >= len(self.player.colleagues):
            return
        col = self.player.colleagues[idx]
        print(f"\nActions avec {col.name} :")
        print("1. Déjeuner ensemble (+Relation)")
        print("2. Séduire (+Relation, risque)")
        print("3. Lancer une rumeur sur lui/elle")
        print("4. Demander de l'aide sur un projet")
        act = input("> ").strip()
        if act == "1":
            col.relationship = min(100, col.relationship + 15)
            print(f"Bon déjeuner avec {col.name}.")
        elif act == "2":
            if random.random() < (self.player.looks / 100):
                col.is_seduced = True
                col.relationship = min(100, col.relationship + 25)
                print(f"{col.name} est sensible à votre charme !")
                if random.random() < 0.2:
                    print("Attention : rumeur de bureau !")
                    self.player.work_performance -= 10
            else:
                col.relationship = max(0, col.relationship - 10)
                print(f"{col.name} n'a pas apprécié votre tentative.")
        elif act == "3":
            col.has_rumor = True
            if random.random() < 0.5:
                print(f"La rumeur sur {col.name} circule. Sa réputation est entamée.")
                self.player.work_performance -= 5
            else:
                print(f"La rumeur est revenue à vos oreilles. {col.name} est furieux(se).")
                col.relationship = max(0, col.relationship - 30)
        elif act == "4":
            if col.relationship > 50:
                self.player.work_performance = min(100, self.player.work_performance + 10)
                print(f"{col.name} vous a aidé. Performance au travail améliorée.")
            else:
                print(f"{col.name} a refusé de vous aider.")
        input("...")

    def submenu_belle_famille(self):
        if not self.player.in_laws:
            print("Vous n'avez pas de belle-famille (mariez-vous d'abord).")
            input("...")
            return
        self.submenu_famille(self.player.in_laws)

    def submenu_ex_partenaires(self):
        if not self.player.ex_partners:
            print("Vous n'avez pas d'ex-partenaires.")
            input("...")
            return
        for i, ex in enumerate(self.player.ex_partners):
            print(f"{i+1}. {ex.name} | Raison: {ex.reason_breakup} | Amertume: {ex.bitterness}/100")
        idx = input("Choisir (0 pour annuler) : ").strip()
        if not idx.isdigit() or int(idx) == 0:
            return
        idx = int(idx) - 1
        if idx >= len(self.player.ex_partners):
            return
        ex = self.player.ex_partners[idx]
        print(f"\nActions avec {ex.name} :")
        print("1. Reprendre contact")
        print("2. Demander de renouer")
        act = input("> ").strip()
        if act == "1":
            ex.relationship = min(100, ex.relationship + 10)
            print(f"Vous avez repris contact avec {ex.name}.")
        elif act == "2":
            if ex.bitterness < 40 and ex.relationship > 60:
                self.player.partner = Partner(ex.name, ex.gender)
                self.player.ex_partners.remove(ex)
                print(f"Vous êtes de nouveau en couple avec {ex.name} !")
            else:
                print(f"{ex.name} n'est pas prêt(e) à renouer.")
        input("...")

    def submenu_epoux_correspondance(self):
        print("\n─── ÉPOUX/ÉPOUSE PAR CORRESPONDANCE ───")
        if self.player.partner:
            print("Vous êtes déjà en couple.")
            input("...")
            return
        print("Chercher un(e) partenaire à l'étranger via une agence matrimoniale.")
        countries_available = [c for c in COUNTRIES if c != self.player.country]
        for i, c in enumerate(countries_available[:6]):
            print(f"  {i+1}. {c}")
        idx = input("Choisir un pays (0 pour annuler) : ").strip()
        if not idx.isdigit() or int(idx) == 0:
            return
        cost = 5_000
        if self.player.bank_balance < cost:
            print(f"Il faut {cost:,.0f}€ pour les frais d'agence.")
            input("...")
            return
        self.player.bank_balance -= cost
        name = f"{random.choice(FIRST_NAMES_F if self.player.gender == 'Homme' else FIRST_NAMES_M)} {random.choice(LAST_NAMES)}"
        partner = Partner(name, "Femme" if self.player.gender == "Homme" else "Homme")
        partner.relationship = random.randint(30, 60)
        self.player.partner = partner
        self.player.mail_order_spouses.append(name)
        print(f"Vous avez été mis en contact avec {name}. Relation initiale : {partner.relationship}/100")
        input("...")

    # ─── MENU ÉCOLE ───────────────────────────────────────────────────
    def menu_ecole(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.player.display_stats()
        print(f"\n─── ÉCOLE ───")
        print(f"Matière préférée : {self.player.favorite_subject}")
        print(f"Notes actuelles  : {self.player.grades}/100")
        print(f"Niveau scolaire  : {self.player.education_name}")
        print("\n1. Étudier dur (+Notes, +Intelligence)")
        print("2. Chahuter (-Notes, +Bonheur)")
        print("3. Se faire des amis")
        print("4. Participer à une activité parascolaire")
        print("5. Harceler un camarade (Karma -)")
        print("6. Défendre un camarade (Karma +)")
        c = input("Choix : ").strip()
        if c == "1":
            self.player.grades = min(100, self.player.grades + 5)
            self.player.smarts = min(100, self.player.smarts + 2)
            print("Vous avez bien révisé. Notes améliorées.")
        elif c == "2":
            self.player.grades = max(0, self.player.grades - 10)
            self.player.happiness = min(100, self.player.happiness + 10)
            print("Quelle rigolade !")
        elif c == "3":
            name = f"{random.choice(FIRST_NAMES_M if random.random() > 0.5 else FIRST_NAMES_F)} {random.choice(LAST_NAMES)}"
            self.player.friends.append(Person(name, "Ami d'école"))
            print(f"Nouvel(le) ami(e) : {name} !")
        elif c == "4":
            activities = ["Club de théâtre", "Équipe de foot", "Orchestre", "Club d'informatique", "Club de débat"]
            act = random.choice(activities)
            print(f"Vous rejoignez le {act}.")
            self.player.happiness = min(100, self.player.happiness + 8)
            self.player.smarts = min(100, self.player.smarts + 1)
        elif c == "5":
            self.player.karma = max(0, self.player.karma - 10)
            self.player.happiness += 5
            print("Vous avez harcelé un camarade. Karma -10.")
        elif c == "6":
            self.player.karma = min(100, self.player.karma + 10)
            self.player.happiness += 8
            print("Vous avez défendu un camarade. Karma +10.")

        # Passage au lycée / bac
        if self.player.age == 18 and self.player.education_level == 0:
            if self.player.grades >= 50:
                self.player.education_level = 2
                self.player.education_name = "Baccalauréat"
                print("\n🎓 Vous avez obtenu votre Baccalauréat !")
            else:
                print("\nVous n'avez pas obtenu votre Baccalauréat. Redoublement possible.")
        input("...")

    # ─── MENU PERMIS DE CONDUIRE ──────────────────────────────────────
    def menu_permis(self):
        if self.player.driver_license:
            print(f"Vous avez déjà votre permis de conduire (obtenu à {self.player.driver_license_age} ans).")
            input("...")
            return
        print("\n─── PERMIS DE CONDUIRE ───")
        print("Passer le permis de conduire (coût : 1 500€)")
        print("1. Passer l'examen | 0. Annuler")
        c = input("> ").strip()
        if c == "1":
            if self.player.bank_balance >= 1_500:
                self.player.bank_balance -= 1_500
                chance = 0.5 + (self.player.smarts / 200)
                if random.random() < chance:
                    self.player.driver_license = True
                    self.player.driver_license_age = self.player.age
                    print(f"🚗 Permis obtenu à {self.player.age} ans !")
                else:
                    print("Échec à l'examen. Réessayez l'année prochaine.")
            else:
                print("Fonds insuffisants.")
        input("...")

    # ─── MENU ACTIVITÉS & SANTÉ ───────────────────────────────────────
    def menu_activites(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.player.display_stats()
            print("\n─── ACTIVITÉS & SANTÉ & BIEN-ÊTRE ───")
            print("1.  Salle de sport (+Santé, +Beauté, +Fitness)")
            print("2.  Bibliothèque (+Intelligence)")
            print("3.  Santé & Médecine")
            print("4.  Chirurgie Esthétique")
            print("5.  Méditation (+Bonheur, -Stress)")
            print("6.  Yoga (+Santé, -Stress)")
            print("7.  Thérapie (+Santé Mentale)")
            print("8.  Régime alimentaire")
            print("9.  Spa & Bien-être (+Bonheur, -Stress)")
            print("10. Cours de développement personnel")
            print("0.  Retour")

            c = input("Choix : ").strip()
            if c == "1":
                self.player.health = min(100, self.player.health + 5)
                self.player.looks = min(100, self.player.looks + 2)
                self.player.fitness = min(100, self.player.fitness + 5)
                self.player.stress = max(0, self.player.stress - 5)
                print("Excellente séance ! Santé et beauté améliorées.")
            elif c == "2":
                self.player.smarts = min(100, self.player.smarts + 5)
                print("Vous vous sentez plus intelligent(e).")
            elif c == "3":
                self.menu_sante()
                continue
            elif c == "4":
                self.menu_chirurgie()
                continue
            elif c == "5":
                self.player.happiness = min(100, self.player.happiness + 10)
                self.player.stress = max(0, self.player.stress - 15)
                self.player.mental_health = min(100, self.player.mental_health + 5)
                print("Zen... Votre esprit est apaisé.")
            elif c == "6":
                self.player.health = min(100, self.player.health + 3)
                self.player.stress = max(0, self.player.stress - 10)
                self.player.fitness = min(100, self.player.fitness + 3)
                print("Séance de yoga terminée. Corps et esprit alignés.")
            elif c == "7":
                cost = 200
                if self.player.bank_balance >= cost:
                    self.player.bank_balance -= cost
                    self.player.mental_health = min(100, self.player.mental_health + 15)
                    self.player.happiness = min(100, self.player.happiness + 10)
                    if "Dépression" in self.player.diseases and random.random() < 0.4:
                        self.player.diseases.remove("Dépression")
                        print("Votre dépression s'est envolée grâce à la thérapie !")
                    else:
                        print("Séance de thérapie bénéfique.")
                else:
                    print("Fonds insuffisants (200€).")
            elif c == "8":
                print("1. Régime végétarien | 2. Régime keto | 3. Jeûne intermittent")
                d = input("> ").strip()
                self.player.health = min(100, self.player.health + 3)
                self.player.looks = min(100, self.player.looks + 2)
                self.player.happiness -= 3
                print("Régime en cours. Santé et apparence améliorées légèrement.")
            elif c == "9":
                cost = 500
                if self.player.bank_balance >= cost:
                    self.player.bank_balance -= cost
                    self.player.happiness = min(100, self.player.happiness + 20)
                    self.player.stress = max(0, self.player.stress - 20)
                    print("Journée spa magnifique ! Vous vous sentez régénéré(e).")
                else:
                    print("Fonds insuffisants (500€).")
            elif c == "10":
                cost = 1_000
                if self.player.bank_balance >= cost:
                    self.player.bank_balance -= cost
                    self.player.charisma = min(100, self.player.charisma + 5)
                    self.player.smarts = min(100, self.player.smarts + 3)
                    print("Formation terminée. Charisme et intelligence améliorés.")
                else:
                    print("Fonds insuffisants (1 000€).")
            elif c == "0":
                break
            input("...")

    def menu_sante(self):
        print("\n─── SANTÉ & MÉDECINE ───")
        print("1. Consulter un médecin généraliste (500€)")
        print("2. Spécialiste (2 000€)")
        print("3. Cure de désintoxication (5 000€)")
        print("4. Psychologue (200€)")
        print("5. Bilan de santé complet (1 000€)")
        print("6. Traitement expérimental (10 000€, risqué)")
        s = input("Choix : ").strip()
        if s == "1":
            if self.player.bank_balance >= 500:
                self.player.bank_balance -= 500
                self.player.last_checkup = self.player.age
                if self.player.diseases:
                    if random.random() < 0.3:
                        d = self.player.diseases.pop()
                        print(f"Guéri(e) de : {d} !")
                    else:
                        print("Le médecin n'a pas pu vous soigner complètement.")
                else:
                    self.player.health = min(100, self.player.health + 5)
                    print("Vous êtes en bonne santé. Légère amélioration.")
            else:
                print("Fonds insuffisants.")
        elif s == "2":
            if self.player.bank_balance >= 2_000:
                self.player.bank_balance -= 2_000
                if self.player.diseases:
                    if random.random() < 0.5:
                        d = self.player.diseases.pop()
                        print(f"Spécialiste : guéri(e) de {d} !")
                    else:
                        print("Le spécialiste recommande un suivi.")
                else:
                    print("Aucune maladie détectée.")
            else:
                print("Fonds insuffisants.")
        elif s == "3":
            if self.player.bank_balance >= 5_000:
                self.player.bank_balance -= 5_000
                if self.player.addictions:
                    self.player.addictions = []
                    self.player.health = min(100, self.player.health + 10)
                    print("Sevrage complet ! Vous êtes libéré(e) de toutes vos addictions.")
                else:
                    print("Vous n'avez pas d'addictions.")
            else:
                print("Fonds insuffisants.")
        elif s == "4":
            if self.player.bank_balance >= 200:
                self.player.bank_balance -= 200
                self.player.happiness = min(100, self.player.happiness + 20)
                self.player.mental_health = min(100, self.player.mental_health + 15)
                if "Dépression" in self.player.diseases and random.random() < 0.5:
                    self.player.diseases.remove("Dépression")
                    print("Dépression surmontée grâce au psychologue !")
                else:
                    print("Séance bénéfique pour votre santé mentale.")
            else:
                print("Fonds insuffisants.")
        elif s == "5":
            if self.player.bank_balance >= 1_000:
                self.player.bank_balance -= 1_000
                self.player.last_checkup = self.player.age
                print("Bilan complet effectué.")
                print(f"  Santé physique : {self.player.health}/100")
                print(f"  Santé mentale  : {self.player.mental_health}/100")
                print(f"  Maladies       : {', '.join(self.player.diseases) or 'Aucune'}")
                print(f"  Addictions     : {', '.join(self.player.addictions) or 'Aucune'}")
                if self.player.age > 40 and random.random() < 0.1:
                    new_disease = random.choice(["Diabète type 2", "Hypertension", "Cholestérol"])
                    if new_disease not in self.player.diseases:
                        self.player.diseases.append(new_disease)
                        print(f"  ⚠ Diagnostic : {new_disease} détecté.")
            else:
                print("Fonds insuffisants.")
        elif s == "6":
            if self.player.bank_balance >= 10_000:
                self.player.bank_balance -= 10_000
                if random.random() < 0.4:
                    if self.player.diseases:
                        d = self.player.diseases.pop()
                        self.player.health = min(100, self.player.health + 20)
                        print(f"Traitement révolutionnaire ! Guéri(e) de {d} !")
                    else:
                        self.player.health = min(100, self.player.health + 15)
                        print("Traitement réussi. Santé considérablement améliorée.")
                else:
                    self.player.health -= 20
                    print("Effets secondaires graves ! Santé -20.")
            else:
                print("Fonds insuffisants.")
        input("...")

    def menu_chirurgie(self):
        print("\n─── CHIRURGIE ESTHÉTIQUE ───")
        procedures = [
            ("Botox",                2_000,   0,  5, "Rides atténuées."),
            ("Rhinoplastie",        10_000,   0, 15, "Nouveau nez, nouvelle confiance."),
            ("Liposuccion",         15_000,  10, 10, "Corps sculpté."),
            ("Implants capillaires", 8_000,   0, 10, "Chevelure retrouvée."),
            ("Lifting complet",     25_000,   0, 20, "Rajeunissement spectaculaire."),
            ("Augmentation mammaire",12_000,  0, 12, "Silhouette transformée."),
            ("Abdominoplastie",     18_000,   5,  8, "Ventre plat."),
        ]
        for i, (name, cost, h, l, _) in enumerate(procedures):
            print(f"{i+1}. {name} ({cost:,.0f}€) → Santé +{h}, Beauté +{l}")
        ch = input("Choix (0 pour annuler) : ").strip()
        if not ch.isdigit() or int(ch) == 0:
            return
        idx = int(ch) - 1
        if idx >= len(procedures):
            return
        name, cost, h, l, msg = procedures[idx]
        if self.player.bank_balance >= cost:
            self.player.bank_balance -= cost
            if random.random() < 0.05:  # Complication chirurgicale
                self.player.health -= 15
                print(f"Complication post-opératoire ! Santé -15.")
            else:
                self.player.health = min(100, self.player.health + h)
                self.player.looks = min(100, self.player.looks + l)
                print(f"Opération réussie ! {msg}")
        else:
            print(f"Fonds insuffisants ({cost:,.0f}€ requis).")
        input("...")

    # ─── MENU CARRIÈRE ────────────────────────────────────────────────
    def menu_carriere(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.player.display_stats()
            print("\n─── CARRIÈRE & ÉTUDES ───")
            job_str = self.player.job['name'] if self.player.job else "Sans emploi"
            print(f"Emploi actuel : {job_str}")
            print(f"Niveau d'études : {self.player.education_name}")
            print(f"Performance : {self.player.work_performance}/100")
            print("\n1.  Chercher un emploi")
            print("2.  Carrière Politique")
            print("3.  Université (Licence, Master, Doctorat)")
            print("4.  École spécialisée")
            print("5.  Carrière Militaire")
            print("6.  Carrière d'Athlète Professionnel")
            print("7.  Freelance")
            print("8.  Temps partiel")
            if self.player.job:
                print("9.  Demander une augmentation")
                print("10. Démissionner")
                print("11. Améliorer sa performance")
            print("0.  Retour")
            c = input("Choix : ").strip()
            if c == "1":
                self._chercher_emploi()
            elif c == "2":
                self.menu_politique()
            elif c == "3":
                self._menu_universite()
            elif c == "4":
                self._menu_ecoles_specialisees()
            elif c == "5":
                self._menu_militaire()
            elif c == "6":
                self._menu_athlete()
            elif c == "7":
                self._menu_freelance()
            elif c == "8":
                self._menu_temps_partiel()
            elif c == "9" and self.player.job:
                self._demander_augmentation()
            elif c == "10" and self.player.job:
                self._demissionner()
            elif c == "11" and self.player.job:
                self._ameliorer_performance()
            elif c == "0":
                break
            input("...")

    def _chercher_emploi(self):
        print("\n─── OFFRES D'EMPLOI ───")
        available = []
        for j in self.jobs:
            if (self.player.smarts >= j.get('req_smarts', 0) and
                    self.player.looks >= j.get('req_looks', 0) and
                    self.player.health >= j.get('req_health', 0) and
                    self.player.education_level >= j.get('req_edu', 0)):
                available.append(j)
        if not available:
            print("Aucune offre disponible avec votre profil actuel.")
            return
        for i, j in enumerate(available):
            bonus = f" (Bonus: {j['pref']})" if 'pref' in j else ""
            salary_str = f"{j['salary']:,.0f}€/an" if j['salary'] > 0 else "Variable"
            print(f"{i+1}. {j['name']} — {salary_str}{bonus}")
        try:
            idx = int(input("Postuler (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(available):
                return
            job = available[idx]
            chance = 0.5
            if 'pref' in job and job['pref'] == self.player.favorite_subject:
                chance += 0.3
            if self.player.grades > 80:
                chance += 0.2
            if self.player.charisma > 70:
                chance += 0.1
            if random.random() < chance:
                self.player.job = job
                self.player.career_type = job.get('career', 'standard')
                self.player.years_in_job = 0
                self.player.work_performance = 70
                # Générer des collègues
                self.player.colleagues = []
                for _ in range(random.randint(2, 5)):
                    name = f"{random.choice(FIRST_NAMES_M if random.random() > 0.5 else FIRST_NAMES_F)} {random.choice(LAST_NAMES)}"
                    self.player.colleagues.append(Colleague(name, job['name']))
                print(f"✅ Engagé(e) comme {job['name']} !")
            else:
                print("❌ Candidature rejetée. Améliorez vos compétences.")
        except (ValueError, IndexError):
            pass

    def _menu_universite(self):
        print("\n─── UNIVERSITÉ ───")
        levels = [
            ("Licence (3 ans)", 3, 3, 10_000, 70),
            ("Master (5 ans)",  4, 5, 20_000, 75),
            ("Doctorat (8 ans)",5, 8, 30_000, 85),
            ("MBA",             4, 2, 40_000, 80),
        ]
        for i, (name, lvl, years, cost, req) in enumerate(levels):
            owned = " ✓" if self.player.education_level >= lvl else ""
            print(f"{i+1}. {name} — {cost:,.0f}€ — Req. Intelligence: {req}{owned}")
        try:
            idx = int(input("Choisir (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(levels):
                return
            name, lvl, years, cost, req = levels[idx]
            if self.player.education_level >= lvl:
                print("Vous avez déjà ce niveau d'études.")
                return
            if self.player.smarts < req:
                print(f"Intelligence insuffisante (requis: {req}).")
                return
            total_cost = cost * years
            if self.player.bank_balance < total_cost:
                print(f"Fonds insuffisants ({total_cost:,.0f}€ requis).")
                return
            self.player.bank_balance -= total_cost
            self.player.education_level = lvl
            self.player.education_name = name.split(" (")[0]
            self.player.smarts = min(100, self.player.smarts + 10)
            print(f"🎓 Félicitations ! Vous avez obtenu votre {self.player.education_name} !")
        except (ValueError, IndexError):
            pass

    def _menu_ecoles_specialisees(self):
        print("\n─── ÉCOLES SPÉCIALISÉES ───")
        for i, s in enumerate(SPECIALIZED_SCHOOLS):
            cost_str = f"{s['cost']:,.0f}€" if s['cost'] > 0 else "Gratuit"
            print(f"{i+1}. {s['name']} ({s['duration']} ans) — {cost_str}")
        try:
            idx = int(input("Choisir (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(SPECIALIZED_SCHOOLS):
                return
            school = SPECIALIZED_SCHOOLS[idx]
            # Vérification des prérequis
            if self.player.smarts < school.get('req_smarts', 0):
                print(f"Intelligence insuffisante.")
                return
            if self.player.health < school.get('req_health', 0):
                print(f"Santé insuffisante.")
                return
            if self.player.looks < school.get('req_looks', 0):
                print(f"Apparence insuffisante.")
                return
            total_cost = school['cost'] * school['duration']
            if self.player.bank_balance < total_cost:
                print(f"Fonds insuffisants ({total_cost:,.0f}€).")
                return
            self.player.bank_balance -= total_cost
            self.player.education_level = max(self.player.education_level, school['edu_level'])
            self.player.specialized_school = school['name']
            self.player.education_name = school['name']
            bonus = school['bonus']
            if bonus == "militaire":
                self.player.career_type = "militaire"
                self.player.health = min(100, self.player.health + 15)
                self.player.fitness = min(100, self.player.fitness + 20)
            elif bonus == "sport":
                self.player.health = min(100, self.player.health + 10)
                self.player.fitness = min(100, self.player.fitness + 15)
            elif bonus in ("musique", "arts", "cinéma"):
                self.player.fame = min(100, self.player.fame + 5)
            elif bonus in ("commerce", "ingénierie", "droit"):
                self.player.smarts = min(100, self.player.smarts + 10)
            print(f"🎓 Diplôme de {school['name']} obtenu ! Bonus : {bonus}")
        except (ValueError, IndexError):
            pass

    def _menu_militaire(self):
        print("\n─── CARRIÈRE MILITAIRE ───")
        if self.player.career_type != "militaire" and self.player.health < 80:
            print("Santé insuffisante pour une carrière militaire (min 80).")
            return
        ranks = ["Soldat", "Caporal", "Sergent", "Lieutenant", "Capitaine", "Colonel", "Général"]
        current = ranks[min(self.player.military_rank, 6)]
        print(f"Grade actuel : {current}")
        print("1. S'enrôler / Continuer la carrière")
        print("2. Demander une promotion")
        print("3. Participer à une mission (risqué)")
        c = input("> ").strip()
        if c == "1":
            self.player.career_type = "militaire"
            salary = 30_000 + self.player.military_rank * 8_000
            self.player.job = {"name": f"Militaire - {current}", "salary": salary, "req_edu": 2}
            print(f"Enrôlé(e) comme {current}. Salaire : {salary:,.0f}€/an")
        elif c == "2":
            if self.player.military_rank < 6:
                if self.player.work_performance > 75 and random.random() < 0.4:
                    self.player.military_rank += 1
                    new_rank = ranks[self.player.military_rank]
                    salary = 30_000 + self.player.military_rank * 8_000
                    self.player.job = {"name": f"Militaire - {new_rank}", "salary": salary, "req_edu": 2}
                    print(f"🎖 Promotion ! Vous êtes maintenant {new_rank}.")
                else:
                    print("Promotion refusée. Améliorez votre performance.")
            else:
                print("Vous avez atteint le grade maximum : Général.")
        elif c == "3":
            print("Mission de combat... ")
            time.sleep(1)
            if random.random() < 0.7:
                reward = random.randint(10_000, 50_000)
                self.player.bank_balance += reward
                self.player.fame = min(100, self.player.fame + 5)
                self.player.work_performance = min(100, self.player.work_performance + 10)
                print(f"Mission réussie ! Prime : {reward:,.0f}€. Héros national !")
            else:
                self.player.health -= random.randint(20, 40)
                print("Mission difficile. Vous avez été blessé(e).")
                if self.player.health <= 0:
                    self.player.is_alive = False
                    self.player.cause_of_death = "Mort au combat"

    def _menu_athlete(self):
        print("\n─── ATHLÈTE PROFESSIONNEL ───")
        sports = ["Football", "Tennis", "Basketball", "Natation", "Athlétisme", "Boxe", "Golf"]
        if not self.player.athlete_sport:
            print("Choisir un sport :")
            for i, s in enumerate(sports):
                print(f"  {i+1}. {s}")
            idx = input("> ").strip()
            if idx.isdigit() and 1 <= int(idx) <= len(sports):
                self.player.athlete_sport = sports[int(idx) - 1]
                self.player.career_type = "athlète"
                base_salary = 200_000 if self.player.health >= 90 else 80_000
                self.player.job = {"name": f"Athlète Pro ({self.player.athlete_sport})", "salary": base_salary, "req_edu": 2}
                print(f"Carrière d'athlète lancée en {self.player.athlete_sport} !")
        else:
            print(f"Sport : {self.player.athlete_sport}")
            print("1. S'entraîner intensément (+Santé, +Performance)")
            print("2. Participer à une compétition")
            print("3. Négocier un contrat publicitaire")
            c = input("> ").strip()
            if c == "1":
                self.player.health = min(100, self.player.health + 5)
                self.player.fitness = min(100, self.player.fitness + 8)
                self.player.work_performance = min(100, self.player.work_performance + 5)
                print("Entraînement intensif terminé.")
            elif c == "2":
                pos, reward = MiniGame.course_automobile() if self.player.athlete_sport in ["Athlétisme"] else (random.randint(1, 10), random.randint(10_000, 500_000))
                self.player.bank_balance += reward
                self.player.fame = min(100, self.player.fame + 5)
                print(f"Compétition terminée. Gain : {reward:,.0f}€")
            elif c == "3":
                if self.player.fame > 20:
                    contract = random.randint(50_000, 2_000_000)
                    self.player.bank_balance += contract
                    print(f"Contrat publicitaire signé : {contract:,.0f}€ !")
                else:
                    print("Votre notoriété est insuffisante pour attirer des sponsors.")

    def _menu_freelance(self):
        print("\n─── FREELANCE ───")
        print(f"Clients actuels : {self.player.freelance_clients}")
        print("1. Prospecter de nouveaux clients")
        print("2. Travailler sur un projet")
        print("3. Augmenter ses tarifs")
        c = input("> ").strip()
        if c == "1":
            self.player.career_type = "freelance"
            self.player.job = {"name": "Freelance", "salary": 0, "req_edu": 2}
            if random.random() < (self.player.charisma / 100):
                new_clients = random.randint(1, 3)
                self.player.freelance_clients += new_clients
                print(f"+{new_clients} nouveau(x) client(s) !")
            else:
                print("Prospection infructueuse.")
        elif c == "2":
            if self.player.freelance_clients > 0:
                income = self.player.freelance_clients * random.randint(2_000, 8_000)
                self.player.bank_balance += income
                self.player.stress = min(100, self.player.stress + 10)
                print(f"Projets livrés. Revenus : {income:,.0f}€")
            else:
                print("Vous n'avez pas de clients.")
        elif c == "3":
            if self.player.freelance_clients > 0:
                if random.random() < 0.5:
                    print("Vos clients acceptent la hausse tarifaire.")
                else:
                    lost = random.randint(1, max(1, self.player.freelance_clients // 2))
                    self.player.freelance_clients -= lost
                    print(f"{lost} client(s) ont quitté suite à la hausse.")

    def _menu_temps_partiel(self):
        print("\n─── TEMPS PARTIEL ───")
        jobs_tp = ["Serveur/Serveuse", "Livreur", "Caissier", "Baby-sitter", "Agent de sécurité"]
        for i, j in enumerate(jobs_tp):
            print(f"  {i+1}. {j} (7 500€/an)")
        idx = input("Choisir (0 pour annuler) : ").strip()
        if idx.isdigit() and 1 <= int(idx) <= len(jobs_tp):
            self.player.job = {"name": jobs_tp[int(idx) - 1], "salary": 15_000, "req_edu": 1}
            self.player.career_type = "temps_partiel"
            print(f"Emploi à temps partiel : {jobs_tp[int(idx) - 1]}")

    def _demander_augmentation(self):
        print("\n─── DEMANDE D'AUGMENTATION ───")
        self.player.raise_attempts += 1
        if self.player.work_performance > 80 and random.random() < 0.5:
            raise_pct = random.randint(5, 20)
            old_salary = self.player.job['salary']
            self.player.job['salary'] = int(old_salary * (1 + raise_pct / 100))
            print(f"Augmentation accordée ! +{raise_pct}% → {self.player.job['salary']:,.0f}€/an")
        elif self.player.raise_attempts > 2:
            print("Votre insistance agace votre employeur.")
            self.player.work_performance -= 10
        else:
            print("Demande refusée. Améliorez votre performance d'abord.")

    def _demissionner(self):
        print(f"Démissionner de {self.player.job['name']} ?")
        if input("Confirmer (o/n) : ").strip().lower() == "o":
            print(f"Vous avez quitté votre poste de {self.player.job['name']}.")
            self.player.job = None
            self.player.career_type = None
            self.player.colleagues = []
            self.player.raise_attempts = 0

    def _ameliorer_performance(self):
        print("\n─── AMÉLIORER SA PERFORMANCE ───")
        print("1. Formation professionnelle (2 000€)")
        print("2. Coaching (1 000€)")
        print("3. Travailler plus dur (gratuit, -Bonheur)")
        c = input("> ").strip()
        if c == "1":
            if self.player.bank_balance >= 2_000:
                self.player.bank_balance -= 2_000
                self.player.work_performance = min(100, self.player.work_performance + 15)
                self.player.smarts = min(100, self.player.smarts + 3)
                print("Formation terminée. Performance +15.")
            else:
                print("Fonds insuffisants.")
        elif c == "2":
            if self.player.bank_balance >= 1_000:
                self.player.bank_balance -= 1_000
                self.player.work_performance = min(100, self.player.work_performance + 10)
                self.player.charisma = min(100, self.player.charisma + 5)
                print("Coaching terminé. Performance +10.")
            else:
                print("Fonds insuffisants.")
        elif c == "3":
            self.player.work_performance = min(100, self.player.work_performance + 5)
            self.player.happiness -= 10
            self.player.stress = min(100, self.player.stress + 10)
            print("Vous avez travaillé dur. Performance +5 mais bonheur -10.")

    # ─── MENU POLITIQUE ───────────────────────────────────────────────
    def menu_politique(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.player.display_stats()
            print("\n─── VIE POLITIQUE ───")
            ranks = ["Citoyen", "Maire", "Député", "Ministre", "Président"]
            print(f"Rang         : {ranks[self.player.political_rank]}")
            print(f"Parti        : {self.player.political_party.name if self.player.political_party else 'Aucun'}")
            print(f"Approbation  : {self.player.public_approval}%")
            print(f"Lois votées  : {len(self.player.laws_passed)}")
            print("\n1. Créer un Parti Politique (50 000€)")
            print("2. Lancer une Campagne Électorale")
            if self.player.political_rank > 0:
                print("3. Proposer une Loi")
                print("4. Faire un Discours (mini-jeu)")
                print("5. Scandale politique")
                print("6. Émettre un décret")
            print("0. Retour")

            c = input("Choix : ").strip()
            if c == "1":
                if self.player.bank_balance >= 50_000:
                    name = input("Nom du parti : ").strip() or "Parti Nouveau"
                    ideo = input("Idéologie (Libéral/Conservateur/Écologiste/Socialiste) : ").strip()
                    self.player.bank_balance -= 50_000
                    self.player.political_party = Party(name, ideo)
                    print(f"Le parti '{name}' ({ideo}) a été fondé !")
                else:
                    print("Fonds insuffisants (50 000€).")
            elif c == "2":
                if not self.player.political_party:
                    print("Créez ou rejoignez un parti d'abord.")
                elif self.player.political_rank < 4:
                    next_rank = ranks[self.player.political_rank + 1]
                    costs = [10_000, 100_000, 500_000, 2_000_000]
                    cost = costs[self.player.political_rank]
                    print(f"Campagne pour : {next_rank} | Coût : {cost:,.0f}€")
                    if self.player.bank_balance >= cost:
                        if input("Confirmer ? (o/n) ").strip().lower() == "o":
                            self.player.bank_balance -= cost
                            chance = (self.player.smarts + self.player.public_approval + self.player.fame) / 300
                            if random.random() < chance:
                                self.player.political_rank += 1
                                self.player.fame = min(100, self.player.fame + 20)
                                self.player.public_approval = 50
                                print(f"🗳 VICTOIRE ! Vous êtes le/la nouveau/nouvelle {next_rank} !")
                            else:
                                self.player.public_approval = max(0, self.player.public_approval - 10)
                                print("Défaite électorale...")
                    else:
                        print("Budget insuffisant pour la campagne.")
            elif c == "3" and self.player.political_rank > 0:
                self.menu_lois()
            elif c == "4" and self.player.political_rank > 0:
                change = MiniGame.debat_politique(self.player.smarts, self.player.public_approval)
                self.player.public_approval = max(0, min(100, self.player.public_approval + change))
                print(f"Approbation publique : {self.player.public_approval}%")
            elif c == "5" and self.player.political_rank > 0:
                print("Un scandale éclate ! (corruption, affaire personnelle...)")
                self.player.public_approval = max(0, self.player.public_approval - random.randint(10, 30))
                self.player.fame += 5
                print(f"Approbation chute à {self.player.public_approval}%")
            elif c == "6" and self.player.political_rank >= 3:
                decrees = ["Nationalisation d'une industrie", "Réforme fiscale d'urgence",
                           "État d'urgence sanitaire", "Dissolution du parlement"]
                for i, d in enumerate(decrees):
                    print(f"  {i+1}. {d}")
                idx = input("Décret : ").strip()
                if idx.isdigit() and 1 <= int(idx) <= len(decrees):
                    print(f"Décret '{decrees[int(idx)-1]}' promulgué !")
                    self.player.public_approval += random.randint(-15, 20)
            elif c == "0":
                break
            input("...")

    def menu_lois(self):
        print("\n─── PROPOSER UNE LOI ───")
        laws = [
            ("Baisser les impôts",           "Popularité +15, Budget -"),
            ("Augmenter le salaire minimum", "Popularité +10, Inflation +"),
            ("Légaliser les drogues douces", "Crime -, Santé -"),
            ("Interdire les réseaux sociaux","Santé Mentale +, Fame -"),
            ("Investir dans l'éducation",    "Popularité +8, Budget -"),
            ("Plan de relance économique",   "Popularité +12, Dette +"),
            ("Réforme de la retraite",       "Popularité -10, Budget +"),
            ("Loi sur l'environnement",      "Popularité +5, Industrie -"),
        ]
        for i, (l, desc) in enumerate(laws):
            print(f"{i+1}. {l} ({desc})")
        try:
            idx = int(input("Loi à proposer : ")) - 1
            law_name = laws[idx][0]
            print(f"Vote au parlement pour : {law_name}...")
            time.sleep(0.5)
            if random.random() < (self.player.public_approval / 100):
                print(f"✅ LOI ADOPTÉE : {law_name} !")
                self.player.laws_passed.append(law_name)
                effects = {0: -0.1, 1: 0, 2: 0, 3: -20, 4: 0, 5: 0, 6: 0, 7: 0}
                if idx == 0:
                    self.player.bank_balance = int(self.player.bank_balance * 0.9)
                elif idx == 3:
                    self.player.fame -= 20
                self.player.public_approval = min(100, self.player.public_approval + 8)
            else:
                print("❌ La loi a été rejetée par le parlement.")
                self.player.public_approval = max(0, self.player.public_approval - 5)
        except (ValueError, IndexError):
            pass

    # ─── MENU PATRIMOINE ──────────────────────────────────────────────
    def menu_patrimoine(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("─── PATRIMOINE & BIENS ───")
            print(f"Solde : {self.player.bank_balance:,.0f}€ | Prestige : {self.player.compute_prestige()} pts")
            print("\n1.  Véhicules (Voitures, Yachts, Avions)")
            print("2.  Montres & Bijoux de luxe")
            print("3.  Instruments de musique")
            print("4.  Immobilier")
            print("5.  Voir tout mon patrimoine")
            print("6.  Assurer un bien")
            print("7.  Vendre un bien")
            print("8.  Musée personnel")
            print("9.  Zoo personnel")
            print("10. Circuit de course (mini-jeu)")
            print("0.  Retour")
            c = input("Choix : ").strip()
            if c == "1":
                self._menu_vehicules()
            elif c == "2":
                self._menu_collections("Montres")
                self._menu_collections("Bijoux")
            elif c == "3":
                self._menu_collections("Instruments")
            elif c == "4":
                self._menu_immobilier()
            elif c == "5":
                self._afficher_patrimoine()
            elif c == "6":
                self._assurer_bien()
            elif c == "7":
                self._vendre_bien()
            elif c == "8":
                self._menu_musee()
            elif c == "9":
                print("Gérez votre zoo depuis le menu Animaux.")
            elif c == "10":
                has_car = any(a.category == "Voitures" for a in self.player.assets)
                if has_car:
                    pos, reward = MiniGame.course_automobile()
                    self.player.bank_balance += reward
                    self.player.fame = min(100, self.player.fame + 3)
                else:
                    print("Vous avez besoin d'une voiture pour participer à une course.")
            elif c == "0":
                break
            input("...")

    def _menu_vehicules(self):
        print("\n─── VÉHICULES ───")
        for cat, items in LUXURY_VEHICLES.items():
            print(f"\n{cat} :")
            for i, item in enumerate(items):
                print(f"  {i+1}. {item['name']} — {item['price']:,.0f}€ | "
                      f"Entretien: {item['maintenance']:,.0f}€/an | Prestige: {item['prestige']}")
        cat_choice = input("Catégorie (Voitures/Yachts/Avions) : ").strip().capitalize()
        if cat_choice not in LUXURY_VEHICLES:
            return
        items = LUXURY_VEHICLES[cat_choice]
        try:
            idx = int(input("Numéro : ")) - 1
            if idx < 0 or idx >= len(items):
                return
            item = items[idx]
            if self.player.bank_balance >= item['price']:
                self.player.bank_balance -= item['price']
                asset = Asset(
                    item['name'], cat_choice,
                    item['price'], item['maintenance'],
                    item['insurance'], item['prestige']
                )
                self.player.assets.append(asset)
                print(f"🚗 Achat de {item['name']} pour {item['price']:,.0f}€ !")
            else:
                print(f"Fonds insuffisants ({item['price']:,.0f}€ requis).")
        except (ValueError, IndexError):
            pass

    def _menu_collections(self, category):
        catalog = LUXURY_COLLECTIBLES.get(category, [])
        if not catalog:
            return
        print(f"\n─── {category.upper()} ───")
        for i, item in enumerate(catalog):
            print(f"  {i+1}. {item['name']} — {item['price']:,.0f}€ | "
                  f"Appréciation: +{item['appreciation']*100:.0f}%/an | Prestige: {item['prestige']}")
        try:
            idx = int(input("Numéro (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(catalog):
                return
            item = catalog[idx]
            if self.player.bank_balance >= item['price']:
                self.player.bank_balance -= item['price']
                asset = Asset(
                    item['name'], category,
                    item['price'], 0, 0,
                    item['prestige'], item['appreciation']
                )
                self.player.assets.append(asset)
                print(f"✨ Achat de {item['name']} pour {item['price']:,.0f}€ !")
            else:
                print(f"Fonds insuffisants ({item['price']:,.0f}€).")
        except (ValueError, IndexError):
            pass

    def _menu_immobilier(self):
        print("\n─── IMMOBILIER ───")
        print("1. Acheter un bien")
        print("2. Voir mes biens immobiliers")
        print("3. Mettre en location")
        print("4. Acheter avec hypothèque (crédit)")
        c = input("> ").strip()
        if c == "1":
            for i, prop in enumerate(REAL_ESTATE_CATALOG):
                print(f"  {i+1}. {prop['name']} — {prop['price']:,.0f}€ | "
                      f"Loyer: {prop['rent']:,.0f}€/mois | Prestige: {prop['prestige']}")
            try:
                idx = int(input("Choisir (0 pour annuler) : ")) - 1
                if idx < 0 or idx >= len(REAL_ESTATE_CATALOG):
                    return
                prop = REAL_ESTATE_CATALOG[idx]
                if self.player.bank_balance >= prop['price']:
                    self.player.bank_balance -= prop['price']
                    self.player.real_estate.append(RealEstateProperty(prop))
                    print(f"🏠 Achat de {prop['name']} pour {prop['price']:,.0f}€ !")
                else:
                    print(f"Fonds insuffisants ({prop['price']:,.0f}€).")
            except (ValueError, IndexError):
                pass
        elif c == "2":
            if not self.player.real_estate:
                print("Vous ne possédez aucun bien immobilier.")
            for r in self.player.real_estate:
                print(f"  - {r}")
        elif c == "3":
            if not self.player.real_estate:
                print("Aucun bien à louer.")
                return
            for i, r in enumerate(self.player.real_estate):
                print(f"  {i+1}. {r.name} | En location: {'Oui' if r.is_rented else 'Non'}")
            try:
                idx = int(input("Choisir : ")) - 1
                if 0 <= idx < len(self.player.real_estate):
                    r = self.player.real_estate[idx]
                    r.is_rented = not r.is_rented
                    print(f"{r.name} : {'Mis en location' if r.is_rented else 'Retiré de la location'}.")
            except (ValueError, IndexError):
                pass
        elif c == "4":
            print("Achat avec hypothèque (apport 20%, crédit 80%)")
            for i, prop in enumerate(REAL_ESTATE_CATALOG):
                apport = int(prop['price'] * 0.20)
                print(f"  {i+1}. {prop['name']} — Apport: {apport:,.0f}€")
            try:
                idx = int(input("Choisir (0 pour annuler) : ")) - 1
                if idx < 0 or idx >= len(REAL_ESTATE_CATALOG):
                    return
                prop = REAL_ESTATE_CATALOG[idx]
                apport = int(prop['price'] * 0.20)
                if self.player.bank_balance >= apport:
                    self.player.bank_balance -= apport
                    new_prop = RealEstateProperty(prop)
                    new_prop.mortgage = int(prop['price'] * 0.80)
                    self.player.real_estate.append(new_prop)
                    self.player.debt += new_prop.mortgage
                    print(f"🏠 {prop['name']} acheté avec hypothèque. Dette : {new_prop.mortgage:,.0f}€")
                else:
                    print(f"Apport insuffisant ({apport:,.0f}€ requis).")
            except (ValueError, IndexError):
                pass

    def _afficher_patrimoine(self):
        print("\n─── MON PATRIMOINE ───")
        total = self.player.bank_balance
        print(f"Solde bancaire : {self.player.bank_balance:,.0f}€")
        if self.player.assets:
            print("\nBiens & Collections :")
            for a in self.player.assets:
                print(f"  - {a}")
                total += a.current_value
        if self.player.real_estate:
            print("\nImmobilier :")
            for r in self.player.real_estate:
                print(f"  - {r}")
                total += r.current_value
        portfolio_val = sum(STOCKS[s]['price'] * q for s, q in self.player.portfolio.items() if q > 0)
        if portfolio_val > 0:
            print(f"\nPortefeuille boursier : {portfolio_val:,.0f}€")
            total += portfolio_val
        if self.player.holding:
            print(f"\n{self.player.holding}")
            total += self.player.holding.total_value
        print(f"\n{'─'*40}")
        print(f"PATRIMOINE NET TOTAL : {total:,.0f}€")
        print(f"Prestige total       : {self.player.compute_prestige()} pts")

    def _assurer_bien(self):
        all_assets = [(a.name, "asset", i) for i, a in enumerate(self.player.assets) if not a.is_insured]
        all_assets += [(r.name, "real_estate", i) for i, r in enumerate(self.player.real_estate) if not r.is_insured]
        if not all_assets:
            print("Tous vos biens sont déjà assurés.")
            return
        for i, (name, t, idx) in enumerate(all_assets):
            print(f"  {i+1}. {name}")
        try:
            choice = int(input("Assurer (0 pour annuler) : ")) - 1
            if choice < 0 or choice >= len(all_assets):
                return
            name, t, idx = all_assets[choice]
            if t == "asset":
                obj = self.player.assets[idx]
                annual_cost = obj.insurance_cost
            else:
                obj = self.player.real_estate[idx]
                annual_cost = obj.insurance_cost
            print(f"Assurance pour {name} : {annual_cost:,.0f}€/an")
            if input("Confirmer ? (o/n) ").strip().lower() == "o":
                obj.is_insured = True
                print(f"{name} est maintenant assuré(e).")
        except (ValueError, IndexError):
            pass

    def _vendre_bien(self):
        all_items = ([(a.name, "asset", i, a.current_value) for i, a in enumerate(self.player.assets)] +
                     [(r.name, "real_estate", i, r.current_value) for i, r in enumerate(self.player.real_estate)])
        if not all_items:
            print("Vous n'avez aucun bien à vendre.")
            return
        for i, (name, t, idx, val) in enumerate(all_items):
            print(f"  {i+1}. {name} — Valeur actuelle : {val:,.0f}€")
        try:
            choice = int(input("Vendre (0 pour annuler) : ")) - 1
            if choice < 0 or choice >= len(all_items):
                return
            name, t, idx, val = all_items[choice]
            # Négociation
            neg_val = MiniGame.negociation_affaires(self.player.smarts)
            final_val = max(int(val * 0.70), min(int(val * 1.20), neg_val if neg_val > 0 else int(val * 0.85)))
            self.player.bank_balance += final_val
            if t == "asset":
                self.player.assets.pop(idx)
            else:
                self.player.real_estate.pop(idx)
            print(f"Vente de {name} pour {final_val:,.0f}€ !")
        except (ValueError, IndexError):
            pass

    def _menu_musee(self):
        print("\n─── MUSÉE PERSONNEL ───")
        if not self.player.museum:
            collectibles = [a for a in self.player.assets if a.category in ("Montres", "Bijoux", "Instruments")]
            if not collectibles:
                print("Vous n'avez pas d'objets de collection pour ouvrir un musée.")
                return
            if self.player.bank_balance < 1_000_000:
                print("Il faut 1 000 000€ pour ouvrir un musée.")
                return
            museum_name = input("Nom de votre musée : ").strip() or "Mon Musée"
            self.player.bank_balance -= 1_000_000
            self.player.museum = Museum(museum_name)
            for a in collectibles:
                self.player.museum.add_item(a)
            print(f"🏛 Musée '{museum_name}' ouvert avec {len(collectibles)} objets !")
        else:
            print(f"{self.player.museum}")
            print("1. Ajouter un objet")
            print("2. Modifier le prix d'entrée")
            c = input("> ").strip()
            if c == "1":
                available = [a for a in self.player.assets if not a.is_on_display and
                             a.category in ("Montres", "Bijoux", "Instruments")]
                if not available:
                    print("Aucun objet disponible à exposer.")
                    return
                for i, a in enumerate(available):
                    print(f"  {i+1}. {a.name}")
                try:
                    idx = int(input("Ajouter : ")) - 1
                    if 0 <= idx < len(available):
                        self.player.museum.add_item(available[idx])
                        print(f"{available[idx].name} ajouté au musée.")
                except (ValueError, IndexError):
                    pass
            elif c == "2":
                try:
                    fee = int(input("Nouveau prix d'entrée (€) : "))
                    self.player.museum.admission_fee = fee
                    print(f"Prix d'entrée : {fee}€")
                except ValueError:
                    pass

    # ─── MENU ÉCONOMIE (BOURSE + HOLDING) ────────────────────────────
    def menu_economie(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("─── ÉCONOMIE, BOURSE & HOLDING ───")
            print(f"Solde : {self.player.bank_balance:,.0f}€")
            print("\n1.  Bourse (Acheter/Vendre actions)")
            print("2.  Cryptomonnaies")
            print("3.  Créer une entreprise")
            print("4.  Gérer ma holding")
            print("5.  Spéculation immobilière")
            print("6.  Fonds d'investissement")
            print("0.  Retour")
            c = input("Choix : ").strip()
            if c == "1":
                self._menu_bourse()
            elif c == "2":
                self._menu_crypto()
            elif c == "3":
                self._menu_creer_entreprise()
            elif c == "4":
                self._menu_holding()
            elif c == "5":
                self._speculation_immobiliere()
            elif c == "6":
                self._menu_fonds_investissement()
            elif c == "0":
                break
            input("...")

    def _menu_bourse(self):
        print("\n─── BOURSE ───")
        for s, data in STOCKS.items():
            qty = self.player.portfolio.get(s, 0)
            val = data['price'] * qty
            print(f"  {s:20s} {data['price']:>10.2f}€ | Possédé: {qty:5d} ({val:,.0f}€) | Secteur: {data['sector']}")
        print("\n1. Acheter | 2. Vendre | 3. Analyse de marché")
        action = input("> ").strip()
        if action in ("1", "2"):
            name = input("Nom de l'action : ").strip()
            if name not in STOCKS:
                print("Action inconnue.")
                return
            try:
                qty = int(input("Quantité : "))
                if qty <= 0:
                    return
                price = STOCKS[name]['price']
                if action == "1":
                    cost = qty * price
                    if self.player.bank_balance >= cost:
                        self.player.bank_balance -= cost
                        self.player.portfolio[name] = self.player.portfolio.get(name, 0) + qty
                        print(f"Achat de {qty} actions {name} pour {cost:,.0f}€.")
                    else:
                        print("Fonds insuffisants.")
                else:
                    owned = self.player.portfolio.get(name, 0)
                    if owned >= qty:
                        gain = qty * price
                        self.player.bank_balance += gain
                        self.player.portfolio[name] -= qty
                        print(f"Vente de {qty} actions {name} pour {gain:,.0f}€.")
                    else:
                        print(f"Vous ne possédez que {owned} actions.")
            except ValueError:
                pass
        elif action == "3":
            print("\nAnalyse de marché :")
            for s, data in STOCKS.items():
                trend = "📈 Haussier" if data['volatility'] < 0.3 else ("📉 Baissier" if data['volatility'] > 0.5 else "➡ Stable")
                print(f"  {s}: {trend} (Volatilité: {data['volatility']*100:.0f}%)")

    def _menu_crypto(self):
        print("\n─── CRYPTOMONNAIES ───")
        crypto = STOCKS.get("CryptoChain", {"price": 1000, "volatility": 0.9})
        owned = self.player.portfolio.get("CryptoChain", 0)
        print(f"CryptoChain : {crypto['price']:.2f}€ | Possédé: {owned}")
        print("⚠ Très volatile ! Gains et pertes massifs possibles.")
        print("1. Acheter | 2. Vendre")
        action = input("> ").strip()
        if action in ("1", "2"):
            try:
                qty = int(input("Quantité : "))
                price = crypto['price']
                if action == "1":
                    cost = qty * price
                    if self.player.bank_balance >= cost:
                        self.player.bank_balance -= cost
                        self.player.portfolio["CryptoChain"] = owned + qty
                        print(f"Achat de {qty} CryptoChain pour {cost:,.0f}€.")
                    else:
                        print("Fonds insuffisants.")
                else:
                    if owned >= qty:
                        gain = qty * price
                        self.player.bank_balance += gain
                        self.player.portfolio["CryptoChain"] -= qty
                        print(f"Vente pour {gain:,.0f}€.")
                    else:
                        print("Quantité insuffisante.")
            except ValueError:
                pass

    def _menu_creer_entreprise(self):
        print("\n─── CRÉER UNE ENTREPRISE ───")
        print("Modèles disponibles :")
        models = list(BUSINESS_MODELS.keys())
        for i, m in enumerate(models):
            data = BUSINESS_MODELS[m]
            print(f"  {i+1}. {m} — Investissement min: {data['startup_cost']:,.0f}€ | "
                  f"Risque: {int(data['risk']*100)}% | Mult. IPO: x{data['ipo_mult']}")
        try:
            idx = int(input("Choisir un modèle (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(models):
                return
            model_name = models[idx]
            min_cost = BUSINESS_MODELS[model_name]['startup_cost']
            name = input("Nom de l'entreprise : ").strip() or "Ma Société"
            try:
                invest = int(input(f"Investissement initial (min {min_cost:,.0f}€) : ").replace(" ", "").replace(",", ""))
            except ValueError:
                invest = 0
            if invest < min_cost:
                print(f"Investissement minimum : {min_cost:,.0f}€")
                return
            if self.player.bank_balance < invest:
                print("Fonds insuffisants.")
                return
            self.player.bank_balance -= invest
            new_biz = Business(name, model_name, invest)
            # Ajouter à la holding ou créer une holding
            if not self.player.holding:
                holding_name = input("Nom de votre holding (ou Entrée pour holding automatique) : ").strip()
                holding_name = holding_name or f"Holding {self.player.name.split()[0]}"
                self.player.holding = Holding(holding_name)
            self.player.holding.add_subsidiary(new_biz)
            # Rétrocompatibilité
            if not self.player.business:
                self.player.business = new_biz
            print(f"✅ Entreprise '{name}' ({model_name}) créée et ajoutée à {self.player.holding.name} !")
        except (ValueError, IndexError):
            pass

    def _menu_holding(self):
        if not self.player.holding:
            print("Vous n'avez pas encore de holding. Créez d'abord une entreprise.")
            return
        h = self.player.holding
        print(f"\n─── {h.name.upper()} ───")
        print(f"Filiales : {len(h.subsidiaries)} | Valeur totale : {h.total_value:,.0f}€")
        for i, b in enumerate(h.subsidiaries):
            print(f"  {i+1}. {b}")
        print("\n1. Gérer une filiale")
        print("2. Recruter un cadre C-Level")
        print("3. Lancer une IPO")
        print("4. Gérer une crise")
        print("5. Augmenter le budget R&D")
        print("6. Vendre une filiale")
        c = input("> ").strip()
        if c == "1":
            try:
                idx = int(input("Numéro de filiale : ")) - 1
                if 0 <= idx < len(h.subsidiaries):
                    b = h.subsidiaries[idx]
                    print(f"\n{b}")
                    print(f"Trésorerie : {b.cash_reserve:,.0f}€ | R&D : {b.r_and_d_budget:,.0f}€/an")
                    print(f"C-Level : {b.c_level or 'Aucun'}")
                    if b.crisis:
                        print(f"⚠ CRISE EN COURS : {b.crisis} ({b.crisis_turns} tours restants)")
            except (ValueError, IndexError):
                pass
        elif c == "2":
            try:
                biz_idx = int(input("Filiale (numéro) : ")) - 1
                if 0 <= biz_idx < len(h.subsidiaries):
                    b = h.subsidiaries[biz_idx]
                    print("Rôles disponibles :", ", ".join(C_LEVEL_ROLES))
                    role = input("Rôle : ").strip().upper()
                    if role in C_LEVEL_ROLES:
                        exec_name = f"{random.choice(FIRST_NAMES_M)} {random.choice(LAST_NAMES)}"
                        salary = random.randint(100_000, 500_000)
                        if self.player.bank_balance >= salary:
                            self.player.bank_balance -= salary
                            bonus = b.hire_c_level(role, exec_name)
                            b.growth_rate = (b.growth_rate[0], b.growth_rate[1] + bonus)
                            print(f"✅ {exec_name} recruté(e) comme {role}. Croissance +{bonus*100:.0f}%")
                        else:
                            print(f"Fonds insuffisants (salaire : {salary:,.0f}€).")
            except (ValueError, IndexError):
                pass
        elif c == "3":
            try:
                biz_idx = int(input("Filiale à introduire en bourse (numéro) : ")) - 1
                if 0 <= biz_idx < len(h.subsidiaries):
                    b = h.subsidiaries[biz_idx]
                    proceeds, msg = b.launch_ipo()
                    if proceeds > 0:
                        self.player.bank_balance += proceeds
                        self.player.fame = min(100, self.player.fame + 10)
                        print(f"🚀 {msg}")
                        print(f"Produit de l'IPO : {proceeds:,.0f}€")
                    else:
                        print(msg)
            except (ValueError, IndexError):
                pass
        elif c == "4":
            crises = [b for b in h.subsidiaries if b.crisis]
            if not crises:
                print("Aucune crise en cours.")
                return
            for b in crises:
                print(f"  {b.name} : {b.crisis}")
                print("  1. Gérer la crise (coûteux) | 2. Ignorer")
                choice = input("  > ").strip()
                if choice == "1":
                    cost = random.randint(100_000, 2_000_000)
                    if self.player.bank_balance >= cost:
                        self.player.bank_balance -= cost
                        b.crisis = None
                        b.reputation = min(100, b.reputation + 20)
                        print(f"  Crise résolue pour {cost:,.0f}€.")
                    else:
                        print(f"  Fonds insuffisants ({cost:,.0f}€).")
        elif c == "5":
            try:
                biz_idx = int(input("Filiale (numéro) : ")) - 1
                if 0 <= biz_idx < len(h.subsidiaries):
                    b = h.subsidiaries[biz_idx]
                    budget = int(input("Budget R&D annuel (€) : ").replace(" ", "").replace(",", "") or "0")
                    if self.player.bank_balance >= budget:
                        self.player.bank_balance -= budget
                        b.r_and_d_budget = budget
                        print(f"Budget R&D de {b.name} : {budget:,.0f}€/an")
                    else:
                        print("Fonds insuffisants.")
            except (ValueError, IndexError):
                pass
        elif c == "6":
            try:
                biz_idx = int(input("Filiale à vendre (numéro) : ")) - 1
                if 0 <= biz_idx < len(h.subsidiaries):
                    b = h.subsidiaries[biz_idx]
                    sale_price = int(b.value * random.uniform(0.8, 1.3))
                    print(f"Vente de {b.name} pour {sale_price:,.0f}€ ?")
                    if input("Confirmer (o/n) : ").strip().lower() == "o":
                        self.player.bank_balance += sale_price
                        h.subsidiaries.remove(b)
                        if self.player.business == b:
                            self.player.business = h.subsidiaries[0] if h.subsidiaries else None
                        print(f"Filiale vendue pour {sale_price:,.0f}€.")
            except (ValueError, IndexError):
                pass

    def _speculation_immobiliere(self):
        print("\n─── SPÉCULATION IMMOBILIÈRE ───")
        if not self.player.real_estate:
            print("Vous ne possédez aucun bien immobilier.")
            return
        for i, r in enumerate(self.player.real_estate):
            print(f"  {i+1}. {r.name} | Valeur: {r.current_value:,.0f}€ | Achat: {r.purchase_price:,.0f}€")
        print("\nLe marché peut faire monter ou descendre les prix.")
        print("1. Attendre (vieillir) | 2. Rénover pour valoriser | 3. Vendre maintenant")
        c = input("> ").strip()
        if c == "2":
            try:
                idx = int(input("Bien à rénover (numéro) : ")) - 1
                if 0 <= idx < len(self.player.real_estate):
                    r = self.player.real_estate[idx]
                    reno_cost = int(r.current_value * 0.10)
                    if self.player.bank_balance >= reno_cost:
                        self.player.bank_balance -= reno_cost
                        r.current_value *= random.uniform(1.10, 1.30)
                        r.rent = int(r.rent * 1.15)
                        print(f"Rénovation terminée ! Nouvelle valeur : {r.current_value:,.0f}€")
                    else:
                        print(f"Fonds insuffisants ({reno_cost:,.0f}€).")
            except (ValueError, IndexError):
                pass
        elif c == "3":
            self._vendre_bien()

    def _menu_fonds_investissement(self):
        print("\n─── FONDS D'INVESTISSEMENT ───")
        funds = [
            {"name": "Fonds Obligataire",   "return": 0.04, "risk": 0.05, "min": 10_000},
            {"name": "Fonds Actions",       "return": 0.08, "risk": 0.20, "min": 25_000},
            {"name": "Fonds Immobilier",    "return": 0.06, "risk": 0.10, "min": 50_000},
            {"name": "Fonds Spéculatif",    "return": 0.20, "risk": 0.50, "min": 100_000},
            {"name": "Fonds Souverain",     "return": 0.03, "risk": 0.02, "min": 500_000},
        ]
        for i, f in enumerate(funds):
            print(f"  {i+1}. {f['name']} — Rendement: {f['return']*100:.0f}%/an | "
                  f"Risque: {f['risk']*100:.0f}% | Min: {f['min']:,.0f}€")
        try:
            idx = int(input("Investir dans (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(funds):
                return
            f = funds[idx]
            amount = int(input(f"Montant (min {f['min']:,.0f}€) : ").replace(" ", "").replace(",", "") or "0")
            if amount < f['min']:
                print(f"Montant minimum : {f['min']:,.0f}€")
                return
            if self.player.bank_balance < amount:
                print("Fonds insuffisants.")
                return
            self.player.bank_balance -= amount
            # Simulation sur 1 an
            actual_return = f['return'] + random.uniform(-f['risk'], f['risk'])
            gain = int(amount * actual_return)
            self.player.bank_balance += amount + gain
            if gain > 0:
                print(f"Investissement rentable ! Gain : +{gain:,.0f}€ ({actual_return*100:.1f}%)")
            else:
                print(f"Perte sur l'investissement : {gain:,.0f}€ ({actual_return*100:.1f}%)")
        except (ValueError, IndexError):
            pass

    # ─── MENU CRIME ───────────────────────────────────────────────────
    def menu_crime(self):
        print("\n─── ACTIVITÉS ILLÉGALES ───")
        print("1. Vol à l'étalage (Facile)")
        print("2. Cambriolage (Moyen)")
        print("3. Braquage de banque (Difficile)")
        print("4. Trafic de drogue (Risqué)")
        print("5. Meurtre (Extrême)")
        print("6. Fraude fiscale")
        print("7. Blanchiment d'argent")
        print("8. Hacking")
        c = input("Choix : ").strip()
        crimes = {
            "1": (0.10, 500,      1),
            "2": (0.30, 5_000,    3),
            "3": (0.60, 100_000,  10),
            "4": (0.50, 20_000,   5),
            "5": (0.80, 0,        25),
            "6": (0.25, 50_000,   2),
            "7": (0.35, 30_000,   4),
            "8": (0.40, 15_000,   2),
        }
        if c not in crimes:
            return
        risk, reward, prison_years = crimes[c]
        if random.random() > risk:
            if c == "5":
                print("Meurtre commis. Karma effondré.")
                self.player.karma = max(0, self.player.karma - 30)
                self.player.happiness -= 20
            else:
                self.player.bank_balance += reward
                self.player.happiness += 10
                self.player.karma = max(0, self.player.karma - 5)
                print(f"Succès ! Vous avez gagné {reward:,.0f}€.")
        else:
            print("🚨 ARRÊTÉ(E) PAR LA POLICE !")
            self.player.in_prison = True
            self.player.prison_years = prison_years
            self.player.criminal_record = True
            self.player.happiness -= 30
            fine = random.randint(1_000, 50_000)
            self.player.bank_balance -= fine
            self.player.lawsuits.append({
                "reason": f"Crime : {c}",
                "win_chance": 0.2,
                "fine": fine
            })
            print(f"Condamné(e) à {prison_years} an(s) de prison. Amende : {fine:,.0f}€")
        input("...")

    # ─── MENU RÉSEAUX SOCIAUX ─────────────────────────────────────────
    def menu_reseaux_sociaux(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.player.display_stats()
            print("\n─── RÉSEAUX SOCIAUX & CÉLÉBRITÉ ───")
            for plat, data in self.player.social_media.items():
                status = f"{data['followers']:,} followers" if data['active'] else "Inactif"
                print(f"  - {plat}: {status}")

            print("\n1. Ouvrir un compte")
            print("2. Poster du contenu")
            print("3. Acheter des faux followers (Risqué)")
            print("4. Monétiser (Sponsorships)")
            if self.player.fame > 20:
                print("5. Activités de Célébrité")
            print("0. Retour")

            c = input("Choix : ").strip()
            if c == "1":
                print("1. Instagram | 2. TikTok | 3. YouTube")
                p = input("Plateforme : ").strip()
                plat = {"1": "Instagram", "2": "TikTok", "3": "YouTube"}.get(p)
                if plat:
                    self.player.social_media[plat]["active"] = True
                    print(f"Compte {plat} créé !")
            elif c == "2":
                print("1. Photo (+Beauté) | 2. Vidéo drôle | 3. Vlog (+Fame) | 4. Tutoriel (+Smarts)")
                post_type = input("Type de post : ").strip()
                base_gain = int(random.randint(10, 100) * (self.player.looks / 50) * (self.player.fame / 10 + 1))
                for plat_name, p in self.player.social_media.items():
                    if p["active"]:
                        p["followers"] += base_gain
                        if random.random() < 0.05:
                            viral_gain = base_gain * 50
                            p["followers"] += viral_gain
                            print(f"🔥 POST VIRAL sur {plat_name} ! +{viral_gain:,} followers !")
                            self.player.fame = min(100, self.player.fame + 5)
                self.player.happiness = min(100, self.player.happiness + 5)
                print(f"Post publié ! +{base_gain:,} followers.")
            elif c == "3":
                cost = 1_000
                if self.player.bank_balance >= cost:
                    self.player.bank_balance -= cost
                    for p in self.player.social_media.values():
                        if p["active"]:
                            p["followers"] += 5_000
                    if random.random() < 0.3:
                        print("⚠ Détecté ! Vos comptes ont été suspendus.")
                        for p in self.player.social_media.values():
                            p["active"] = False
                            p["followers"] = 0
                    else:
                        print("+5 000 followers achetés.")
                else:
                    print("Fonds insuffisants.")
            elif c == "4":
                total = sum(p["followers"] for p in self.player.social_media.values())
                if total > 10_000:
                    gain = int(total * 0.01)
                    if self.player.is_verified:
                        gain *= 2
                    self.player.bank_balance += gain
                    self.player.happiness -= 5
                    self.player.stress = min(100, self.player.stress + 5)
                    print(f"💰 Sponsorship : +{gain:,.0f}€ !")
                    self.player.fame = min(100, self.player.fame + 1)
                    if total > 1_000_000 and not self.player.is_verified:
                        if random.random() < 0.5:
                            self.player.is_verified = True
                            print("✔ Badge vérifié obtenu !")
                else:
                    print("Il faut au moins 10 000 followers pour les sponsors.")
            elif c == "5" and self.player.fame > 20:
                self.menu_celebrite()
            elif c == "0":
                break
            input("...")

    def menu_celebrite(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("─── ZONE VIP & CÉLÉBRITÉ ───")
        print("1. Émission TV (+Fame, +Argent)")
        print("2. Livre autobiographique (+Argent)")
        print("3. Tournée mondiale (si artiste)")
        print("4. Publicité (+Argent, -Bonheur)")
        print("5. Ligne de produits dérivés")
        print("6. Collaboration avec une autre célébrité")
        c = input("Choix : ").strip()
        if c == "1":
            self.player.fame = min(100, self.player.fame + 10)
            self.player.bank_balance += 50_000
            print("Vous étiez la star du show ! +50 000€ +10 Fame")
        elif c == "2":
            gain = int(self.player.fame * 1_000)
            self.player.bank_balance += gain
            print(f"Votre livre est un best-seller ! +{gain:,.0f}€")
        elif c == "3":
            if self.player.job and ("Star" in self.player.job["name"] or "Athlète" in self.player.job["name"]):
                gain = 500_000
                self.player.bank_balance += gain
                self.player.happiness -= 20
                self.player.health -= 10
                self.player.stress = min(100, self.player.stress + 20)
                self.player.fame = min(100, self.player.fame + 15)
                print(f"Tournée épuisante mais lucrative ! +{gain:,.0f}€")
            else:
                print("Vous n'êtes pas une star de la scène.")
        elif c == "4":
            self.player.bank_balance += 100_000
            self.player.happiness -= 5
            print("Publicité tournée. +100 000€")
        elif c == "5":
            if self.player.fame > 40:
                revenue = int(self.player.fame * 5_000)
                self.player.bank_balance += revenue
                print(f"Ligne de produits dérivés lancée ! +{revenue:,.0f}€/an")
            else:
                print("Votre notoriété est insuffisante pour des produits dérivés.")
        elif c == "6":
            celeb_name = f"{random.choice(FIRST_NAMES_M + FIRST_NAMES_F)} {random.choice(LAST_NAMES)}"
            gain_fame = random.randint(5, 20)
            gain_money = random.randint(50_000, 500_000)
            self.player.fame = min(100, self.player.fame + gain_fame)
            self.player.bank_balance += gain_money
            print(f"Collaboration avec {celeb_name} ! +{gain_fame} Fame, +{gain_money:,.0f}€")
        input("...")

    # ─── MENU CASINO & LOTO ───────────────────────────────────────────
    def menu_casino(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("─── CASINO ROYALE & JEUX ───")
            print(f"Solde : {self.player.bank_balance:,.0f}€")
            print("\n1. Roulette")
            print("2. Blackjack (mini-jeu)")
            print("3. Machine à sous")
            print("4. Poker")
            print("5. Acheter des tickets de loto")
            print("6. Paris sportifs")
            print("0. Retour")
            c = input("Choix : ").strip()
            if c == "1":
                self._casino_roulette()
            elif c == "2":
                self._casino_blackjack()
            elif c == "3":
                self._casino_slots()
            elif c == "4":
                self._casino_poker()
            elif c == "5":
                self._acheter_loto()
            elif c == "6":
                self._paris_sportifs()
            elif c == "0":
                break
            input("...")

    def _casino_roulette(self):
        print("\n─── ROULETTE ───")
        try:
            bet = int(input("Mise (0 pour annuler) : ").replace(" ", "").replace(",", "") or "0")
            if bet <= 0 or self.player.bank_balance < bet:
                print("Mise invalide ou fonds insuffisants.")
                return
            self.player.bank_balance -= bet
            print("1. Rouge/Noir (x2) | 2. Numéro exact (x36) | 3. Pair/Impair (x2)")
            choice = input("> ").strip()
            if choice == "1":
                if random.random() < 0.48:
                    win = bet * 2
                    self.player.bank_balance += win
                    print(f"GAGNÉ ! +{win:,.0f}€")
                    self.player.happiness += 10
                else:
                    print(f"PERDU ! -{bet:,.0f}€")
                    self.player.happiness -= 5
            elif choice == "2":
                number = random.randint(0, 36)
                guess = input(f"Votre numéro (0-36) : ").strip()
                if guess.isdigit() and int(guess) == number:
                    win = bet * 36
                    self.player.bank_balance += win
                    print(f"JACKPOT ! Le numéro était {number} ! +{win:,.0f}€")
                    self.player.happiness += 30
                else:
                    print(f"PERDU ! Le numéro était {number}.")
            elif choice == "3":
                if random.random() < 0.48:
                    win = bet * 2
                    self.player.bank_balance += win
                    print(f"GAGNÉ ! +{win:,.0f}€")
                else:
                    print(f"PERDU ! -{bet:,.0f}€")
        except ValueError:
            pass
        # Risque d'addiction
        if random.random() < 0.1 and "Jeu" not in self.player.addictions:
            self.player.addictions.append("Jeu")
            print("⚠ Vous commencez à être accro aux jeux d'argent...")

    def _casino_blackjack(self):
        print("\n─── BLACKJACK ───")
        try:
            bet = int(input("Mise : ").replace(" ", "").replace(",", "") or "0")
            if bet <= 0 or self.player.bank_balance < bet:
                print("Mise invalide.")
                return
            self.player.bank_balance -= bet
            player_score = random.randint(12, 20)
            dealer_score = random.randint(15, 21)
            print(f"Votre main : {player_score}")
            print("1. Rester | 2. Tirer une carte")
            choice = input("> ").strip()
            if choice == "2":
                card = random.randint(1, 11)
                player_score += card
                print(f"Vous tirez un {card}. Total : {player_score}")
            if player_score > 21:
                print(f"Bust ! Vous avez dépassé 21. Dealer : {dealer_score}")
            elif player_score > dealer_score or dealer_score > 21:
                win = bet * 2
                self.player.bank_balance += win
                print(f"GAGNÉ ! Vous : {player_score} vs Dealer : {dealer_score}. +{win:,.0f}€")
                self.player.happiness += 10
            elif player_score == dealer_score:
                self.player.bank_balance += bet
                print(f"Égalité ! Mise remboursée.")
            else:
                print(f"PERDU ! Vous : {player_score} vs Dealer : {dealer_score}.")
        except ValueError:
            pass

    def _casino_slots(self):
        print("\n─── MACHINE À SOUS ───")
        try:
            bet = int(input("Mise (min 10€) : ").replace(" ", "").replace(",", "") or "0")
            if bet < 10 or self.player.bank_balance < bet:
                print("Mise invalide.")
                return
            self.player.bank_balance -= bet
            symbols = ["🍒", "🍋", "🔔", "⭐", "💎", "7️⃣"]
            reels = [random.choice(symbols) for _ in range(3)]
            print(f"  {' | '.join(reels)}")
            if reels[0] == reels[1] == reels[2]:
                mult = {"💎": 100, "7️⃣": 50, "⭐": 20, "🔔": 10, "🍒": 5, "🍋": 3}.get(reels[0], 5)
                win = bet * mult
                self.player.bank_balance += win
                print(f"JACKPOT ! x{mult} ! +{win:,.0f}€")
                self.player.happiness += 20
            elif reels[0] == reels[1] or reels[1] == reels[2]:
                win = bet * 2
                self.player.bank_balance += win
                print(f"Deux identiques ! +{win:,.0f}€")
            else:
                print(f"PERDU ! -{bet:,.0f}€")
        except ValueError:
            pass

    def _casino_poker(self):
        print("\n─── POKER ───")
        try:
            bet = int(input("Mise : ").replace(" ", "").replace(",", "") or "0")
            if bet <= 0 or self.player.bank_balance < bet:
                print("Mise invalide.")
                return
            self.player.bank_balance -= bet
            # Simulation simplifiée
            player_hand = random.randint(1, 10)
            opponent_hand = random.randint(1, 10)
            bluff = input("Bluffer ? (o/n) ").strip().lower() == "o"
            if bluff and random.random() < (self.player.charisma / 100):
                win = bet * 3
                self.player.bank_balance += win
                print(f"Bluff réussi ! +{win:,.0f}€")
            elif player_hand > opponent_hand:
                win = bet * 2
                self.player.bank_balance += win
                print(f"Vous gagnez ! Main : {player_hand} vs {opponent_hand}. +{win:,.0f}€")
            else:
                print(f"Vous perdez. Main : {player_hand} vs {opponent_hand}.")
        except ValueError:
            pass

    def _acheter_loto(self):
        print("\n─── LOTO ───")
        cost_per_ticket = 2
        try:
            n = int(input("Nombre de tickets (2€ chacun) : ") or "0")
            total = n * cost_per_ticket
            if self.player.bank_balance >= total:
                self.player.bank_balance -= total
                self.player.loto_tickets += n
                print(f"{n} ticket(s) achetés. Résultats au prochain vieillissement.")
            else:
                print("Fonds insuffisants.")
        except ValueError:
            pass

    def _paris_sportifs(self):
        print("\n─── PARIS SPORTIFS ───")
        events = [
            ("Match de foot (cote 2.0)", 2.0),
            ("Course hippique (cote 5.0)", 5.0),
            ("Combat de boxe (cote 3.0)", 3.0),
            ("Tournoi de tennis (cote 4.0)", 4.0),
        ]
        for i, (name, cote) in enumerate(events):
            print(f"  {i+1}. {name}")
        try:
            idx = int(input("Choisir (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(events):
                return
            event_name, cote = events[idx]
            bet = int(input("Mise : ").replace(" ", "").replace(",", "") or "0")
            if bet <= 0 or self.player.bank_balance < bet:
                print("Mise invalide.")
                return
            self.player.bank_balance -= bet
            win_chance = 1 / cote
            if random.random() < win_chance:
                win = int(bet * cote)
                self.player.bank_balance += win
                print(f"GAGNÉ ! +{win:,.0f}€")
                self.player.happiness += 15
            else:
                print(f"PERDU ! -{bet:,.0f}€")
        except (ValueError, IndexError):
            pass

    # ─── MENU VIE SOCIALE ─────────────────────────────────────────────
    def menu_vie_sociale(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("─── VIE SOCIALE ───")
            print("1. Boîte de nuit")
            print("2. Vacances")
            print("3. Restaurant")
            print("4. Émigrer dans un autre pays")
            print("5. Organiser une fête")
            print("6. Club privé / Cercle d'élite")
            print("0. Retour")
            c = input("Choix : ").strip()
            if c == "1":
                self._menu_boite_nuit()
            elif c == "2":
                self._menu_vacances()
            elif c == "3":
                self._menu_restaurant()
            elif c == "4":
                self._emigrer()
            elif c == "5":
                self._organiser_fete()
            elif c == "6":
                self._club_prive()
            elif c == "0":
                break
            input("...")

    def _menu_boite_nuit(self):
        print("\n─── BOÎTE DE NUIT ───")
        cost = random.randint(50, 500)
        if self.player.bank_balance < cost:
            print("Pas assez d'argent pour sortir.")
            return
        self.player.bank_balance -= cost
        event = random.choice(NIGHTCLUB_EVENTS)
        print(f"Nuit en boîte (-{cost}€) : {event}")
        self.player.happiness = min(100, self.player.happiness + 15)
        self.player.stress = max(0, self.player.stress - 10)
        # Chance de rencontre romantique
        if random.random() < 0.3 and not self.player.partner:
            name = f"{random.choice(FIRST_NAMES_F if self.player.gender == 'Homme' else FIRST_NAMES_M)} {random.choice(LAST_NAMES)}"
            print(f"Vous avez rencontré {name} en boîte !")
            if random.random() < 0.5:
                self.player.partner = Partner(name, "Femme" if self.player.gender == "Homme" else "Homme")
                print(f"Coup de foudre ! Vous êtes en couple avec {name}.")
            else:
                self.player.lovers.append(name)
                print(f"Coup d'un soir avec {name}.")
        # Risque d'addiction
        if random.random() < 0.05 and "Alcool" not in self.player.addictions:
            self.player.addictions.append("Alcool")
            print("⚠ Vous buvez de plus en plus...")

    def _menu_vacances(self):
        print("\n─── VACANCES ───")
        for i, dest in enumerate(VACATION_DESTINATIONS):
            print(f"  {i+1}. {dest['name']} — {dest['cost']:,.0f}€ | "
                  f"+{dest['happiness']} Bonheur | +{dest['fame']} Fame")
        try:
            idx = int(input("Choisir (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(VACATION_DESTINATIONS):
                return
            dest = VACATION_DESTINATIONS[idx]
            if self.player.bank_balance >= dest['cost']:
                self.player.bank_balance -= dest['cost']
                self.player.happiness = min(100, self.player.happiness + dest['happiness'])
                self.player.fame = min(100, self.player.fame + dest['fame'])
                self.player.stress = max(0, self.player.stress - 20)
                self.player.health = min(100, self.player.health + 3)
                print(f"✈ Vacances à {dest['name']} ! Magnifique séjour.")
                self.player.life_events.append(f"Vacances à {dest['name']} à {self.player.age} ans.")
            else:
                print(f"Fonds insuffisants ({dest['cost']:,.0f}€).")
        except (ValueError, IndexError):
            pass

    def _menu_restaurant(self):
        print("\n─── RESTAURANT ───")
        for i, r in enumerate(RESTAURANT_TYPES):
            print(f"  {i+1}. {r['name']} — {r['cost']:,.0f}€ | +{r['happiness']} Bonheur")
        try:
            idx = int(input("Choisir (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(RESTAURANT_TYPES):
                return
            r = RESTAURANT_TYPES[idx]
            guests = 1
            if self.player.partner:
                guests = 2
                print(f"Dîner avec {self.player.partner.name}.")
            total = r['cost'] * guests
            if self.player.bank_balance >= total:
                self.player.bank_balance -= total
                self.player.happiness = min(100, self.player.happiness + r['happiness'])
                if self.player.partner:
                    self.player.partner.relationship = min(100, self.player.partner.relationship + 5)
                print(f"Repas au {r['name']} pour {total:,.0f}€. Délicieux !")
            else:
                print(f"Fonds insuffisants ({total:,.0f}€).")
        except (ValueError, IndexError):
            pass

    def _emigrer(self):
        print("\n─── ÉMIGRATION ───")
        print(f"Pays actuel : {self.player.country}")
        available = [c for c in COUNTRIES if c != self.player.country]
        for i, c in enumerate(available):
            print(f"  {i+1}. {c}")
        try:
            idx = int(input("Émigrer vers (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(available):
                return
            cost = random.randint(5_000, 30_000)
            new_country = available[idx]
            print(f"Coût d'émigration vers {new_country} : {cost:,.0f}€")
            if input("Confirmer ? (o/n) ").strip().lower() == "o":
                if self.player.bank_balance >= cost:
                    self.player.bank_balance -= cost
                    old_country = self.player.country
                    self.player.country = new_country
                    self.player.happiness = min(100, self.player.happiness + 10)
                    self.player.logs.append(f"Émigration de {old_country} vers {new_country}.")
                    self.player.life_events.append(f"Émigré(e) vers {new_country} à {self.player.age} ans.")
                    print(f"Bienvenue en {new_country} !")
                else:
                    print("Fonds insuffisants.")
        except (ValueError, IndexError):
            pass

    def _organiser_fete(self):
        print("\n─── ORGANISER UNE FÊTE ───")
        types = [
            ("Soirée intime (10 personnes)", 500,    5),
            ("Fête d'anniversaire",          2_000,  15),
            ("Soirée VIP",                   10_000, 25),
            ("Gala de charité",              50_000, 40),
        ]
        for i, (name, cost, fame) in enumerate(types):
            print(f"  {i+1}. {name} — {cost:,.0f}€ | +{fame} Fame")
        try:
            idx = int(input("Choisir (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(types):
                return
            name, cost, fame = types[idx]
            if self.player.bank_balance >= cost:
                self.player.bank_balance -= cost
                self.player.fame = min(100, self.player.fame + fame)
                self.player.happiness = min(100, self.player.happiness + 20)
                # Chance de rencontrer quelqu'un
                if random.random() < 0.4:
                    new_friend = f"{random.choice(FIRST_NAMES_M + FIRST_NAMES_F)} {random.choice(LAST_NAMES)}"
                    self.player.friends.append(Person(new_friend, "Ami de soirée"))
                    print(f"Vous avez rencontré {new_friend} à la fête !")
                print(f"Fête réussie ! +{fame} Fame")
            else:
                print(f"Fonds insuffisants ({cost:,.0f}€).")
        except (ValueError, IndexError):
            pass

    def _club_prive(self):
        print("\n─── CLUB PRIVÉ / CERCLE D'ÉLITE ───")
        prestige = self.player.compute_prestige()
        if prestige < 20 and self.player.bank_balance < 1_000_000:
            print("Votre prestige ou fortune est insuffisant pour accéder aux cercles d'élite.")
            return
        clubs = [
            ("Club de Golf",       10_000, "Réseau d'affaires étendu"),
            ("Cercle des Arts",    20_000, "Contacts dans le monde culturel"),
            ("Yacht Club",         50_000, "Accès aux événements maritimes"),
            ("Club des Milliardaires", 500_000, "Réseau ultra-élite"),
        ]
        for i, (name, fee, benefit) in enumerate(clubs):
            print(f"  {i+1}. {name} — {fee:,.0f}€/an | {benefit}")
        try:
            idx = int(input("Rejoindre (0 pour annuler) : ")) - 1
            if idx < 0 or idx >= len(clubs):
                return
            name, fee, benefit = clubs[idx]
            if self.player.bank_balance >= fee:
                self.player.bank_balance -= fee
                self.player.charisma = min(100, self.player.charisma + 5)
                self.player.fame = min(100, self.player.fame + 5)
                # Chance d'opportunité business
                if random.random() < 0.4:
                    opportunity = random.randint(50_000, 500_000)
                    self.player.bank_balance += opportunity
                    print(f"Opportunité d'affaires via le {name} ! +{opportunity:,.0f}€")
                print(f"Membre du {name}. {benefit}")
            else:
                print(f"Fonds insuffisants ({fee:,.0f}€).")
        except (ValueError, IndexError):
            pass

    # ─── MENU TESTAMENT ───────────────────────────────────────────────
    def menu_testament(self):
        print("\n─── TESTAMENT & HÉRITAGE ───")
        print(f"Testament actuel : {self.player.testament}")
        print("\n1. Rédiger/Modifier le testament")
        print("2. Ajouter un légataire")
        print("3. Legs spéciaux (objets)")
        print("0. Retour")
        c = input("Choix : ").strip()
        if c == "1":
            self.player.testament.is_written = True
            print("Testament rédigé.")
        elif c == "2":
            if not self.player.testament.is_written:
                print("Rédigez d'abord votre testament.")
                return
            name = input("Nom du légataire : ").strip()
            try:
                pct = int(input("Pourcentage (%) : "))
                total = sum(self.player.testament.heirs.values()) + pct
                if total > 100:
                    print(f"Total dépasse 100% ({total}%). Ajustez les pourcentages.")
                else:
                    self.player.testament.add_heir(name, pct)
                    print(f"{name} : {pct}% de l'héritage.")
            except ValueError:
                pass
        elif c == "3":
            if not self.player.assets:
                print("Vous n'avez pas d'objets à léguer.")
                return
            for i, a in enumerate(self.player.assets):
                print(f"  {i+1}. {a.name}")
            try:
                idx = int(input("Objet à léguer (numéro) : ")) - 1
                if 0 <= idx < len(self.player.assets):
                    beneficiary = input("Bénéficiaire : ").strip()
                    self.player.testament.special_bequests.append((self.player.assets[idx].name, beneficiary))
                    print(f"{self.player.assets[idx].name} légué à {beneficiary}.")
            except (ValueError, IndexError):
                pass
        input("...")

    # ─── FIN DE PARTIE & HÉRITAGE GÉNÉRATIONNEL ──────────────────────
    def end_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        net_worth = (self.player.bank_balance
                     + sum(a.current_value for a in self.player.assets)
                     + sum(r.current_value for r in self.player.real_estate))
        prestige = self.player.compute_prestige()

        print("╔" + "═"*60 + "╗")
        print(f"║ {'CI-GÎT':^58} ║")
        print(f"║ {self.player.name.upper():^58} ║")
        print(f"║ {'Né(e) en ' + self.player.country:^58} ║")
        print(f"║ {str(self.player.age) + ' ANS':^58} ║")
        print("╠" + "═"*60 + "╣")
        print(f"║ Cause du décès : {self.player.cause_of_death:<42} ║")
        print(f"║ Fortune finale : {net_worth:>20,.0f} €".ljust(61) + "║")
        print(f"║ Prestige       : {prestige:>20,} pts".ljust(61) + "║")
        print(f"║ Enfants        : {len(self.player.children):<42} ║")
        print(f"║ Lois votées    : {len(self.player.laws_passed):<42} ║")
        print(f"║ Casier judic.  : {'Oui' if self.player.criminal_record else 'Non':<42} ║")
        if self.player.holding:
            print(f"║ Holding        : {self.player.holding.name:<42} ║")
        if self.player.laws_passed:
            print(f"║ Lois passées   : {', '.join(self.player.laws_passed[:3]):<42} ║")
        print("╠" + "═"*60 + "╣")
        # Épitaphe selon le karma
        if self.player.karma > 70:
            epitaphe = "Une vie exemplaire, source d'inspiration pour tous."
        elif self.player.karma > 40:
            epitaphe = "Une vie avec ses hauts et ses bas, comme tout le monde."
        else:
            epitaphe = "Une vie controversée dont on parlera longtemps..."
        print(f"║ {epitaphe[:58]:^58} ║")
        print("╚" + "═"*60 + "╝")

        # Événements marquants
        if self.player.life_events:
            print("\n─── MOMENTS MARQUANTS ───")
            for ev in self.player.life_events[-5:]:
                print(f"  • {ev}")

        # Héritage générationnel
        playable_children = [c for c in self.player.children if c.is_playable]
        if playable_children and net_worth > 0:
            print(f"\n─── HÉRITAGE GÉNÉRATIONNEL ───")
            print(f"Vos enfants héritent d'un patrimoine de {net_worth:,.0f}€.")
            if self.player.testament.is_written and self.player.testament.heirs:
                print(f"\nDistribution selon votre testament :")
                for heir, pct in self.player.testament.heirs.items():
                    amount = int(net_worth * pct / 100)
                    print(f"  {heir} : {pct}% → {amount:,.0f}€")
            print(f"\nEnfants jouables ({len(playable_children)}) :")
            for i, child in enumerate(playable_children):
                print(f"  {i+1}. {child.name} | Âge: {child.age} | Notes: {child.grades}/100")
            choice = input("\nIncarner un enfant pour continuer la dynastie ? (numéro ou 0) : ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(playable_children):
                child = playable_children[int(choice) - 1]
                self._start_new_generation(child, net_worth)
                return

        print("\nMerci d'avoir joué à Ultra BitLife Clone !")
        input("Appuyez sur Entrée pour quitter...")

    def _start_new_generation(self, child, inherited_wealth):
        """Démarre une nouvelle génération avec un enfant héritier."""
        self.generation += 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"╔══════════════════════════════════════════════╗")
        print(f"║  GÉNÉRATION {self.generation} — HÉRITAGE DYNASTIQUE    ║")
        print(f"╚══════════════════════════════════════════════╝")

        # Calculer l'héritage
        if self.player.testament.is_written and child.name in self.player.testament.heirs:
            pct = self.player.testament.heirs[child.name]
            inheritance = int(inherited_wealth * pct / 100)
        else:
            # Partage égal entre enfants
            n_children = max(1, len(self.player.children))
            inheritance = int(inherited_wealth / n_children)

        print(f"\nVous incarnez {child.name}, enfant de {self.player.name}.")
        print(f"Héritage reçu : {inheritance:,.0f}€")
        print(f"Âge de départ : {child.age} ans")
        input("Appuyez sur Entrée pour commencer votre nouvelle vie...")

        # Créer le nouveau personnage
        gender_input = input(f"Genre de {child.name} (H/F) : ").upper().strip()
        gender = "Homme" if gender_input == "H" else "Femme"

        new_char = Character(child.name, gender, self.player.country)
        new_char.age = child.age
        new_char.bank_balance = inheritance
        new_char.education_level = child.education_level
        new_char.grades = child.grades
        new_char.smarts = min(100, self.player.smarts // 2 + random.randint(10, 40))
        new_char.looks = min(100, self.player.looks // 2 + random.randint(10, 40))

        # Transmettre une partie du patrimoine physique
        if self.player.real_estate:
            for r in self.player.real_estate[:2]:  # Max 2 biens transmis
                new_char.real_estate.append(r)
        if self.player.holding:
            new_char.holding = self.player.holding

        # Ajouter les parents décédés comme référence
        parent_ref = Person(self.player.name, "Parent décédé")
        parent_ref.is_alive = False
        new_char.parents.append(parent_ref)

        new_char.logs.append(f"Vous êtes l'héritier(e) de la famille {self.dynasty_name}.")
        new_char.life_events.append(f"Héritage de {inheritance:,.0f}€ à {child.age} ans.")

        self.player = new_char

        print(f"\nBienvenue dans la peau de {new_char.name} !")
        print(f"Patrimoine hérité : {inheritance:,.0f}€")
        input("Appuyez sur Entrée pour continuer...")

        # Relancer la boucle principale
        while self.player.is_alive:
            self._main_loop()

        self.end_game()


# ═══════════════════════════════════════════════════════════════════════
#  GESTIONNAIRE D'ÉVÉNEMENTS ENRICHI
# ═══════════════════════════════════════════════════════════════════════

class EventManager:
    def trigger_random_event(self, player):
        if random.random() > 0.35:
            return  # Pas d'événement cette année

        event = random.choice(RANDOM_EVENTS_POOL)

        # Filtrer selon probabilité
        if random.random() > event["prob"]:
            return

        print(f"\n📢 ÉVÉNEMENT : {event['text']}")
        ev_type = event["type"]

        if ev_type in ("addict", "maladie", "argent", "invest"):
            ans = input("Que faites-vous ? (o = accepter / n = refuser) : ").strip().lower()
        else:
            ans = "auto"

        if ev_type == "addict":
            if ans == "o":
                if event["val"] not in player.addictions:
                    player.addictions.append(event["val"])
                player.happiness = min(100, player.happiness + 20)
                print(f"Vous avez cédé. Nouvelle addiction : {event['val']}.")
            else:
                print("Vous avez refusé. Sage décision.")

        elif ev_type == "maladie":
            if ans == "o":
                if event["val"] not in player.diseases:
                    player.diseases.append(event["val"])
                player.health -= 30
                print(f"Diagnostic : {event['val']}.")
            else:
                print("Vous ignorez les symptômes. Risqué...")
                if random.random() < 0.3:
                    if event["val"] not in player.diseases:
                        player.diseases.append(event["val"])
                    print(f"Trop tard ! {event['val']} s'est aggravé.")

        elif ev_type == "argent":
            if ans == "o":
                player.bank_balance += event["val"]
                if random.random() < 0.3:
                    player.criminal_record = True
                    print(f"Vous avez accepté {event['val']}€... mais c'était suspect.")
                else:
                    print(f"Vous avez reçu {event['val']:,.0f}€.")

        elif ev_type == "loto":
            win = random.randint(100_000, 10_000_000)
            player.bank_balance += win
            player.happiness = min(100, player.happiness + 40)
            player.life_events.append(f"Gagné {win:,.0f}€ au loto à {player.age} ans !")
            print(f"🎉 VOUS AVEZ GAGNÉ {win:,.0f}€ AU LOTO !")

        elif ev_type == "vol":
            if player.bank_balance >= event["val"]:
                player.bank_balance -= event["val"]
                player.happiness -= 20
                print(f"Vous avez été arnaqué(e) de {event['val']:,.0f}€ !")
            else:
                print("L'arnaqueur n'a rien pu vous prendre.")

        elif ev_type == "invest":
            if ans == "o":
                amount = event["val"]
                if player.bank_balance >= amount:
                    player.bank_balance -= amount
                    if random.random() < 0.5:
                        gain = amount * random.randint(2, 10)
                        player.bank_balance += gain
                        print(f"Investissement gagnant ! +{gain:,.0f}€")
                    else:
                        print(f"Investissement perdu. -{amount:,.0f}€")
                else:
                    print("Fonds insuffisants pour investir.")

        elif ev_type == "accident":
            player.health -= random.randint(10, 30)
            cost = random.randint(1_000, 20_000)
            player.bank_balance -= cost
            player.happiness -= 15
            print(f"Accident ! Santé -{random.randint(10, 30)}, Frais : {cost:,.0f}€")
            # Assurance ?
            if player.assets and any(a.is_insured for a in player.assets):
                refund = int(cost * 0.8)
                player.bank_balance += refund
                print(f"Votre assurance vous rembourse {refund:,.0f}€.")

        elif ev_type == "heritage":
            amount = random.randint(10_000, 500_000)
            player.bank_balance += amount
            player.happiness = min(100, player.happiness + 10)
            player.life_events.append(f"Héritage inattendu de {amount:,.0f}€ à {player.age} ans.")
            print(f"Héritage inattendu de {amount:,.0f}€ !")

        elif ev_type == "scandale":
            player.fame = min(100, player.fame + 10)
            player.public_approval = max(0, player.public_approval - 15)
            player.happiness -= 10
            print("Un scandale vous éclabousse. Fame +10 mais approbation -15.")

        elif ev_type == "proces":
            fine = random.randint(5_000, 100_000)
            print(f"Vous êtes convoqué(e) au tribunal. Amende potentielle : {fine:,.0f}€")
            player.lawsuits.append({
                "reason": "Procès civil",
                "win_chance": 0.4 + player.smarts / 200,
                "fine": fine
            })

        elif ev_type == "cambriolage":
            if player.real_estate:
                loss = random.randint(5_000, 50_000)
                player.bank_balance -= loss
                player.happiness -= 20
                insured = any(r.is_insured for r in player.real_estate)
                if insured:
                    refund = int(loss * 0.9)
                    player.bank_balance += refund
                    print(f"Cambriolage ! Perte : {loss:,.0f}€. Assurance : +{refund:,.0f}€")
                else:
                    print(f"Cambriolage ! Perte : {loss:,.0f}€. Assurez vos biens !")

        elif ev_type == "rencontre":
            new_person_name = f"{random.choice(FIRST_NAMES_M + FIRST_NAMES_F)} {random.choice(LAST_NAMES)}"
            new_person = Person(new_person_name, "Connaissance")
            player.friends.append(new_person)
            print(f"Vous avez rencontré {new_person_name}. Nouvelle connaissance !")

        elif ev_type == "prix":
            prize_money = random.randint(1_000, 50_000)
            player.bank_balance += prize_money
            player.fame = min(100, player.fame + 5)
            player.happiness = min(100, player.happiness + 15)
            print(f"Vous avez reçu un prix dans votre domaine ! +{prize_money:,.0f}€, +5 Fame")

        input("...")


# ═══════════════════════════════════════════════════════════════════════
#  POINT D'ENTRÉE
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    game = Game()
    game.start()
