from dataclasses import dataclass

from typing import List

from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def calculate_emerald(self):
        emerald = min(self.capacity, self.volume) * self.nutrient_factor
        return emerald

    def __lt__(self, other):
        if self.calculate_emerald() < other.calculate_emerald():
            return True
        return False

    def __gt__(self, other):
        if self.calculate_emerald() > other.calculate_emerald():
            return True
        return False

    def __le__(self, other):
        if self.calculate_emerald() <= other.calculate_emerald():
            return True
        return False

    def __ge__(self, other):
        if self.calculate_emerald() >= other.calculate_emerald():
            return True
        return False

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.max_beehives = max_beehives
        self.heap = MaxHeap(self.max_beehives)


    def set_all_beehives(self, hive_list: List[Beehive]):
        for beehive in hive_list:
            self.add_beehive(beehive)
    
    def add_beehive(self, hive: Beehive):
        self.heap.add(hive)

    
    def harvest_best_beehive(self):
        best_beehive = self.heap.get_max()
        emerald = best_beehive.calculate_emerald()
        best_beehive.volume -= best_beehive.capacity
        self.add_beehive(best_beehive)
        return emerald


