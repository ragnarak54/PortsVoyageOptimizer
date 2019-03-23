import random


class Member:
    def __init__(self, morale, combat, seafaring, speed):
        self.morale = morale
        self.combat = combat
        self.seafaring = seafaring
        self.speed = speed

    def __repr__(self):
        return str([self.morale, self.combat, self.seafaring])


class Bow:
    def __init__(self, name, morale, combat, seafaring):
        self.name = name
        self.morale = morale
        self.combat = combat
        self.seafaring = seafaring


class Hull:
    def __init__(self, name, morale, combat, seafaring):
        self.name = name
        self.morale = morale
        self.combat = combat
        self.seafaring = seafaring


class OnDeck:
    def __init__(self, name, morale, combat, seafaring):
        self.name = name
        self.morale = morale
        self.combat = combat
        self.seafaring = seafaring


class Ship:
    def __init__(self, bow: Bow, hull: Hull, on_deck: OnDeck, rudder):
        self.bow = bow
        self.hull = hull
        self.on_deck = on_deck
        self.rudder = rudder


crew = []
captains = [Member(1000, 0, 0, 0), Member(0, 1000, 0, 0), Member(0, 0, 1000, 0),
            Member(500, 500, 500, 0), Member(0, 500, 500, 0)]

i = 0
while i < 25:
    crew.append(Member(random.randint(0, 2000), random.randint(0, 2000),
                       random.randint(0, 2000), random.randint(0, 2000)))
    i += 1
