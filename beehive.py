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
        """
        Calculate the number of emeralds that can be harvested from this beehive.
        Follows the formula given in the assignment specification.

        Returns:
            The number of emeralds that can be harvested from this beehive.

        Complexity:
            O(1) Constant time
        """
        emerald = min(self.capacity, self.volume) * self.nutrient_factor
        return emerald

    def __lt__(self, other):
        """
        Complexity:
            O(1) Constant time
        """
        if self.calculate_emerald() < other.calculate_emerald():
            return True
        return False

    def __gt__(self, other):
        """
        Complexity:
            O(1) Constant time
        """
        if self.calculate_emerald() > other.calculate_emerald():
            return True
        return False

    def __le__(self, other):
        """
        Complexity:
            O(1) Constant time
        """
        if self.calculate_emerald() <= other.calculate_emerald():
            return True
        return False

    def __ge__(self, other):
        """
        Complexity:
            O(1) Constant time
        """
        if self.calculate_emerald() >= other.calculate_emerald():
            return True
        return False

class BeehiveSelector:
    """
    A class that stores a list of beehives, and allow us to select the best beehives for the day
    by calculating the number of emeralds that can be harvested from each beehive.
    """

    def __init__(self, max_beehives: int):
        """
        Explain:
            - Initialises a MaxHeap to store the beehives
        Args:
            - max_beehives: the maximum number of beehives that can be stored in the MaxHeap
        Complexity:
            O(1) Constant time
        """
        self.max_beehives = max_beehives
        self.heap = MaxHeap(self.max_beehives)

    def set_all_beehives(self, hive_list: List[Beehive]):
        """
        Explain:
            - Updates all the beehives in the list to the MaxHeap

        Args:
            - hive_list: the list of beehives to be added to the MaxHeap

        Complexity:
            -Worst: O(heap.heapify()) = O(M) where M is the length of the hive_list.
            -Best = Worst
        """
        self.heap.heapify(hive_list)
    
    def add_beehive(self, hive: Beehive):
        """
        Explain:
            - Adds a beehive to the MaxHeap
        Args:
            - hive: the beehive to be added to the MaxHeap
        Complexity:
            - Best: O(1) Constant time because of heap add() has a complexity of O(1)
                    - when the element is added to the bottom of the heap without rising up

            - Worst: O(log n) Logarithmic time because of heap add() has a complexity of O(log n)
                    - when the element is added to the top of the heap and has to rise up
        """
        self.heap.add(hive)
    
    def harvest_best_beehive(self):
        """
        Explain:
            - List to store the values of the linear equation for each beehive
            - Calculate the value of the linear equation for each beehive and store it in the list
            - Replace with the appropriate values for each beehive
            - Sort the list of values in descending order
            - Return the kth largest value
            - Return None if k is out of range

        Complexity:
            -Worst = O(log n)
                - heap get_max() has a complexity of O(log n) where n is the number of nodes in the heap.
                - calculate_emerald() - O(1)
                - update volume - O(1)
                - add_beehive() - O(log n)
                - return emerald - O(1)

            -Best = O(1)
                - heap get_max() has a complexity of O(1) where n is the number of nodes in the heap.
                - When all the elements value in the heap are the same.
                - calculate_emerald() - O(1)
                - update volume - O(1)
                - add_beehive() - O(log n)
                - return emerald - O(1)
        """
        best_beehive = self.heap.get_max()
        emerald = best_beehive.calculate_emerald()
        if best_beehive.volume < best_beehive.capacity:
            best_beehive.volume = 0
        else:
            best_beehive.volume -= best_beehive.capacity
        self.add_beehive(best_beehive)
        return emerald

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
    # s = BeehiveSelector(5)
    # b1, b2, b3, b4, b5 = (
    #     Beehive(15, 12, 13, capacity=40, nutrient_factor=5, volume=15),
    #     Beehive(25, 22, 23, capacity=15, nutrient_factor=8, volume=40),
    #     Beehive(35, 32, 33, capacity=40, nutrient_factor=3, volume=40),
    #     Beehive(45, 42, 43, capacity=1, nutrient_factor=85, volume=10),
    #     Beehive(55, 52, 53, capacity=400, nutrient_factor=5000, volume=0),
    # )
    # for hive in [b1, b2, b3, b4, b5]:
    #     s.add_beehive(hive)

    # all_emeralds = []
    # for _ in range(15):
    #     all_emeralds.append(s.harvest_best_beehive())
    # print(all_emeralds)
    #
    # expected = [
    #     # Choices are:
    #     120,  # Beehive b2 or b3
    #     120,  # Beehive b2 or b3
    #     120,  # Beehive b2
    #     # Now, b3 has volume 0 and b2 has volume 10
    #     85,  # Pick b4 10 times
    #     85,
    #     85,
    #     85,
    #     85,
    #     85,
    #     85,
    #     85,
    #     85,
    #     85,
    #     80,  # b2
    #     75,  # b1
    # ]

    s = BeehiveSelector(10)
    s.set_all_beehives([Beehive(15, 12, 13, capacity=40, nutrient_factor=5, volume=15),
                        Beehive(25, 22, 23, capacity=15, nutrient_factor=8, volume=40),
                        Beehive(35, 32, 33, capacity=40, nutrient_factor=3, volume=40),
                        Beehive(45, 42, 43, capacity=1, nutrient_factor=85, volume=10),
                        Beehive(55, 52, 53, capacity=400, nutrient_factor=5000, volume=0)])
    for i in s.heap.the_array:
        print(i)
    assert s.heap.the_array[1] == Beehive(35, 32, 33, capacity=40, nutrient_factor=3, volume=40)
    assert s.heap.the_array[2] == Beehive(25, 22, 23, capacity=15, nutrient_factor=8, volume=40)
    assert s.heap.the_array[3] == Beehive(15, 12, 13, capacity=40, nutrient_factor=5, volume=15)
    assert s.heap.the_array[4] == Beehive(45, 42, 43, capacity=1, nutrient_factor=85, volume=10)
    assert s.heap.the_array[5] == Beehive(55, 52, 53, capacity=400, nutrient_factor=5000, volume=0)
    assert s.heap.length == 5
    assert len(s.heap.the_array) == 11


    # for i in s.heap.the_array:
    #     print(i)

    # s.set_all_beehives([
    #     Beehive(45, 33, 22, capacity=403, nutrient_factor=35, volume=135),
    #     Beehive(324, 245, 44, capacity=1533, nutrient_factor=38, volume=4),
    #     Beehive(324, 33, 33, capacity=403, nutrient_factor=3, volume=403),
    #     Beehive(4, 43, 433, capacity=1, nutrient_factor=85, volume=10324),
    #     Beehive(53245, 532, 554, capacity=432, nutrient_factor=5000324, volume=122)])

    # print("____")
    # for i in s.heap.the_array:
    #     print(i)
