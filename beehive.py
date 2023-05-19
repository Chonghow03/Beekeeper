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
        self.heap = MaxHeap(self.max_beehives)
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

    # List to store the values of the linear equation for each beehive
    # Calculate the value of the linear equation for each beehive and store it in the list
    # Replace with the appropriate values for each beehive
    # Sort the list of values in descending order
    # Return the kth largest value
    # Return None if k is out of range

    def kth_largest(self,k: int, a_1: float, a_2: float, a_3: float):
        hives = []

        for index in range(1,self.heap.length+1):
            beehive = self.heap.the_array[index]
            b_x, b_y, b_z = beehive.x, beehive.y, beehive.z
            value = a_1 * b_x + a_2 * b_y + a_3 * b_z
            hives.append(value)

        hives.sort(reverse=True)

        if 0 < k <= len(hives):
            return hives[k - 1]
        else:
            return None


if __name__ == "__main__":
    s = BeehiveSelector(5)
    b1, b2, b3, b4, b5 = (
        Beehive(15, 12, 13, capacity=40, nutrient_factor=5, volume=15),
        Beehive(25, 22, 23, capacity=15, nutrient_factor=8, volume=40),
        Beehive(35, 32, 33, capacity=40, nutrient_factor=3, volume=40),
        Beehive(45, 42, 43, capacity=1, nutrient_factor=85, volume=10),
        Beehive(55, 52, 53, capacity=400, nutrient_factor=5000, volume=0),
    )
    for hive in [b1, b2, b3, b4, b5]:
        s.add_beehive(hive)
    print(s.kth_largest(4,1.0,1.0,1.0))