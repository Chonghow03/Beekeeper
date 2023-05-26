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
        nth_smaller = ceil(x / 100 * len(self.items)) + 1                # how many from left to remove
        nth_larger = len(self.items) - ceil(y / 100 * len(self.items))  # how many from right to remove, -1 to account for 0 index

        if nth_larger < nth_smaller:
            return []
        # if nth_larger == 0 or nth_smaller == len(self.items) +1:
        #     return []

        _min = self.items.kth_smallest(nth_smaller, self.items.root).key
        _max = self.items.kth_smallest(nth_larger, self.items.root).key

        print(_min, _max)
        def inorder_aux(current: T, f) -> None:
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
                if current.key > _min:
                    inorder_aux(current.left, f)
                if _min <= current.key <= _max:
                    f(current.item)
                if current.key < _max:
                    inorder_aux(current.right, f)


        out = []
        inorder_aux(self.items.root, lambda item: out.append(item))
        return out



if __name__ == "__main__":
    # points = list(range(50))
    # import random
    #
    # random.shuffle(points)
    # p = Percentiles()
    # for point in points:
    #     p.add_point(point)
    # # Numbers from 8 to 16.
    # print(p.ratio(15, 66))

    BST = BinarySearchTree()
    BST[88] = 1
    BST[70] = 2
    BST[60] = 3
    BST[75] = 2
    BST[50] = 3
    BST[64] = 2
    BST[73] = 3
    BST[78] = 2
    BST[40] = 3
    BST[53] = 2
    BST[61] = 3
    BST[65] = 2
    BST[72] = 3
    BST[74] = 2
    BST[77] = 3
    BST[80] = 1
    BST[115] = 2
    BST[98] = 3
    BST[120] = 2
    BST[96] = 3
    BST[105] = 2
    BST[117] = 3
    BST[145] = 2
    BST[95] = 3
    BST[97] = 2
    BST[99] = 3
    BST[107] = 2
    BST[116] = 3
    BST[118] = 2
    BST[130] = 3
    BST[199] = 0
    #
    # r = Percentiles()
    # r.add_point(88)
    # r.add_point(70)
    # r.add_point(60)
    # r.add_point(75)
    # r.add_point(50)
    # r.add_point(64)
    # r.add_point(73)
    # r.add_point(78)
    # r.add_point(40)
    # r.add_point(53)
    # r.add_point(61)
    # r.add_point(65)
    # r.add_point(72)
    # r.add_point(74)
    # r.add_point(77)
    # r.add_point(80)
    # r.add_point(115)
    # r.add_point(98)
    # r.add_point(120)
    #
    # print(r.ratio(0, 0))
    # print(r.ratio(70, 20))
