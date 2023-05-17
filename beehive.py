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

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.max_beehives = max_beehives
        self.beehives = []
        self.heap = MaxHeap(self.max_beehives)


    def set_all_beehives(self, hive_list: List[Beehive]):

    
    def add_beehive(self, hive: Beehive):

    
    def harvest_best_beehive(self):
        raise NotImplementedError()

    def calculate_value(self, hive: Beehive) -> float:
        a_1, a_2, a_3 = 1.0, 1.0, 1.0 
        return a_1 * hive.x + a_2 * hive.y + a_3 * hive.z