from __future__ import annotations
from typing import Generic, TypeVar, Tuple
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1

    def __init__(self, key, item):  # i made this
        self.nodes = {"+++": None, "++-": None, "+-+": None, "+--": None, "-++": None, "-+-": None, "--+": None, "---": None}
        self.key = key
        self.item = item

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        x_self, x_point = self.key[0], point[0]
        y_self, y_point = self.key[1], point[1]
        z_self, z_point = self.key[2], point[2]

        # makes a string such as +++ if the point is greater than the node's key in all dimensions
        strng = ("+" if x_self < x_point else "-") + ("+" if y_self < y_point else "-") + ("+" if z_self < z_point else "-")

        return self.nodes[strng]


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        return self.get_tree_node_by_key_aux(self.root, key)

    # below function added by me
    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        if key == current.key:
            return current
        return self.get_tree_node_by_key_aux(current.get_child_for_key(key), key)

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item=item)
            current.subtree_size -= 1  # init() sets it to 1 already
            self.length += 1
        elif key == current.key:
            print(key, current.key)
            raise ValueError('Inserting duplicate item')
        else:
            x_self, x_point = current.key[0], key[0]
            y_self, y_point = current.key[1], key[1]
            z_self, z_point = current.key[2], key[2]

            # makes a string such as +++ if the point is greater than the node's key in all dimensions
            strng = ("+" if x_self < x_point else "-") + ("+" if y_self < y_point else "-") + ("+" if z_self < z_point else "-")
            current.nodes[strng] = self.insert_aux(current.nodes[strng], key, item)

        current.subtree_size += 1
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        return all(value is None for value in current.nodes.values())


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2
