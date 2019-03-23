import member
from itertools import combinations
from typing import List
import random
import datetime


class Voyage:
    def __init__(self, morale, combat, seafaring, time):
        self.morale = morale
        self.combat = combat
        self.seafaring = seafaring
        self.time = time


members = member.crew


def percent(crew: List[member.Member], voyage: Voyage):
    morale = sum([x.morale for x in crew])
    combat = sum([x.combat for x in crew])
    seafaring = sum([x.seafaring for x in crew])
    return min(morale / voyage.morale, combat / voyage.combat, seafaring / voyage.seafaring)


def optimal_crew(voyage: Voyage):
    best = members[:5] + [random.choice(member.captains)]
    for combo in combinations(members, 5):
        for captain in member.captains:
            if percent(best, voyage) < percent(list(combo) + [captain], voyage):
                best = list(combo) + [captain]
    return best


now = datetime.datetime.now()
best_crew = optimal_crew(Voyage(14400, 14400, 9000, 0))
print(best_crew, percent(best_crew, Voyage(14400, 14400, 9000, 0)))
print(f'time elapsed: {(datetime.datetime.now() - now)}')

