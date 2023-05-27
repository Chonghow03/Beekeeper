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
            complexity is the same as BST's insertion.
            - Worst case: O(BST.__setitem__())(worst) = O(CompK * D) = O(CompK * log(N))
                        - when inserting at the bottom of the tree
                        - where D is the depth of the tree (log(N) for a balanced tree; N for an unbalanced tree)
                        - CompK is the complexity of comparing the keys
                        - All assignments, numerical operations, return statements are constant time, O(1).

            - Best case: O(BST.__setitem__())(best) = O(CompK) inserts the item at the root.
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
            complexity is the same as BST's deletion.
            - Worst case:  O(BST.__delitem__())(worst) = O(Comp(K) * D)
                    - where D is the depth of the tree (log(N) for a balanced tree; N for an unbalanced tree)
                    - CompK is the complexity of comparing the keys
                    - All assignments, numerical operations, return statements are constant time, O(1).
            - Best case:  O(BST.__delitem__())(best) = O(Comp(K))
       """
        del self.items[item]

    def ratio(self, x, y):
        """
            Explain:
            - Computes a list of all items fitting the larger than/smaller than criteria.
            - This list doesn't need to be sorted, but it is in this implementation, due to the nature of the BST,
            and our usage of the inorder traversal.

            Args:
            - x, the lower bound of the range in percentage
            - y, the upper bound of the range in percentage

            Returns:
            - a list of all items fitting the within the bounds of x and y

            Complexity:
            for this implementation, we use the assumption that the BST is bounded by a time complexity of O(log(N)),
            as given by the assignment instructions.

            - Expected complexity: (O(log(N)) + O(O * comp(f))) = O(log(N) + O)
                - getting min/max (calling kth_smallest()): O(2 * log(N)) = O(log(N))
                - calling inorder_aux_bounded(): O(O * comp(f)) as the average case
                    - f, the callable function that is called on each item, is an append() function,
                    and is assumed to be O(1).
                - All assignments, numerical operations, return statements are constant time, O(1).

            - Worst case: O(N)
                - getting min/max (calling kth_smallest()): O(2 * log(N)) = O(log(N))
                - calling inorder_aux_bounded(): O(N * comp(f)) when the entire tree is traversed through;
                    that is, when x=0, y=0, implying that _min is the smallest item in the tree,
                    and _max is the largest item in the tree.
                f, the callable function that is called on each item, is an append() function, and is assumed to be O(1).

                - All assignments, numerical operations, return statements are constant time, O(1).

                Hence, the overall complexity is O(log(N) + N * comp(f)) = O(N * comp(f)) = O(N)

            - Best case: O(1) if the range is empty
                - this happens when x + y >= 100, in which case there will be no elements satisfying the criteria
                we will then return an empty list, without having to traverse the tree.
                - All assignments, numerical operations, return statements are constant time, O(1).
       """

        # nth_smaller is the first leftmost item that we want
        # nth_larger is the last rightmost item that we want
        nth_smaller = ceil(x / 100 * len(self.items)) + 1
        nth_larger = len(self.items) - ceil(y / 100 * len(self.items))

        # if nth_smaller > nth_larger, then there are no items in the range to return
        if nth_larger < nth_smaller:
            return []

        # get the min and max values of the range using the kth_smallest method
        _min = self.items.kth_smallest(nth_smaller, self.items.root).key
        _max = self.items.kth_smallest(nth_larger, self.items.root).key

        def inorder_aux_bounded(current: T, f) -> None:
            """
                Explain:
                - Traverses through the BST in order, and calls the function f on each item. Inorder traversal
                means that the left subtree is traversed first, then the current node, then the right subtree.
                - However, we only traverse through the nodes that are within the range of _min and _max.
                This means inorder is an efficient way to traverse through the BST, as we don't need to traverse
                through the entire tree.
                e.g. when current.key > _min, we don't need to traverse through the right subtree, as all the
                items in the right subtree will be larger than _min, and thus not within the range.

                Args:
                - current, the current node in the BST
                - f, the callable to call on each item

                Returns:
                - None

                Complexity:

                - Average complexity: O(O * comp(f)), where O is the number of items within the range; i.e. number
                    of points that will be returned.

                - Worst case: O(N * comp(f)) when the entire tree is traversed through, and all items are within the range.
                    - This occurs when _min is the smallest item in the tree, and _max is the largest item in the tree.
                    - comp(f) is the time complexity of the function f.
                - Best case: O(1 * comp(f)) when in the first recursive call,
                    _min <= current.key <= _max, as we don't need to traverse through the
                    left and right subtrees.



           """
            if current is not None:  # if not a base case
                if current.key > _min:
                    inorder_aux_bounded(current.left, f)
                if _min <= current.key <= _max:
                    f(current.item)
                if current.key < _max:
                    inorder_aux_bounded(current.right, f)

        out = []
        # returns a list of all items in the range, that is also sorted
        inorder_aux_bounded(self.items.root, lambda item: out.append(item))
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