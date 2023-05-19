from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil, floor
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")


class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.items = BinarySearchTree()

    def add_point(self, item: T):
        """
            Explain:
            - Adds a point to the BST

            Args:
            - item, a point to store in BST

            Raises:
            - None

            Returns:
            - None

            Complexity:
            - Worst case: O(__setitem__())(worst) = O(CompK * D) inserting at the bottom of the tree
                        - where D is the depth of the tree
                        - CompK is the complexity of comparing the keys
                        - All assignments, numerical operations, return statements are constant time, O(1).

            - Best case: O(__setitem__())(best) = O(CompK) inserts the item at the root.
                        - CompK is the complexity of comparing the keys
                        - All assignments, numerical operations, return statements are constant time, O(1).
       """
        self.items[item] = item

    def remove_point(self, item: T):
        """
      `     Explain:
            - Removes a point from the BST

            Args:
            - item, a point to store in BST

            Raises:
            - None

            Returns:
            - None

            Complexity:
            - Worst case: O()
            - Best case: O()
       """
        del self.items[item]

    def ratio(self, x, y):
        """
            Explain:
            - Computes a list of all items fitting the larger than/smaller than criteria.
            - This list doesn't need to be sorted.

            Args:
            -

            Raises:
            -

            Returns:
            -

            Complexity:
            - Worst case:
            - Best case:
       """
        nth_smaller = ceil(x / 100 * len(self.items)) +1                # how many from left to remove
        nth_larger = len(self.items) - ceil(y / 100 * len(self.items))  # how many from right to remove, -1 to account for 0 index
        # todo fix edge case

        num_smaller = self.items.kth_smallest(nth_smaller, self.items.root).key
        num_larger = self.items.kth_smallest(nth_larger, self.items.root).key
        def inorder_aux(current: T, f, _min, _max) -> None:
            """
                Explain:
                -

                Args:
                -

                Raises:
                -

                Returns:
                -

                Complexity:
                - Worst case:
                - Best case:
           """
            if current is not None:  # if not a base case
                if _min <= current.key <= _max:
                    f(current.item)
                    inorder_aux(current.left, f, _min, _max)
                    inorder_aux(current.right, f, _min, _max)
                elif current.key < _min:
                    inorder_aux(current.right, f, _min, _max)
                elif current.key > _max:
                    inorder_aux(current.left, f, _min, _max)
        out = []
        inorder_aux(self.items.root, lambda item: out.append(item), num_smaller, num_larger)
        return out



if __name__ == "__main__":
    points = list(range(50))
    import random

    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))