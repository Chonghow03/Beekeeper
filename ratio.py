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
        # code below adds a point to the tree
        self.items[item] = item

    def remove_point(self, item: T):
        del self.items[item]

    def ratio(self, x, y):
        nth_smaller = ceil(x / 100 * len(self.items)) +1                # how many from left to remove
        nth_larger = len(self.items) - ceil(y / 100 * len(self.items))  # how many from right to remove, -1 to account for 0 index
        # todo fix edge case

        num_smaller = self.items.kth_smallest(nth_smaller, self.items.root).key
        num_larger = self.items.kth_smallest(nth_larger, self.items.root).key
        def inorder_aux(current: T, f, _min, _max) -> None:
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