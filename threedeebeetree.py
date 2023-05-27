from __future__ import annotations
from typing import Generic, TypeVar, Tuple, Dict, Any
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]


@dataclass
class BeeNode:
    key: Point
    item: I
    subtree_size: int = 1
    nodes: dict = field(
        default_factory=lambda: {"+++": None, "++-": None, "+-+": None, "+--": None,
                                 "-++": None, "-+-": None, "--+": None, "---": None})

    def get_child_for_key(self, point: Point) -> BeeNode | None:
        """
            Explain:
            - Given a point, computes the correct key that gets the BeeNode that lies in the octant.

            Args:
            - point: a point in 3d space

            Returns:
            - the BeeNode that lies in the octant that contains the point, or None if there is no such BeeNode.

            Complexity:
            self.get_key(point) has a complexity of O(1);
            and accessing a dictionary is O(1) in the average case.
            - Worst case: O(1)
            - Best case: O(1)
       """
        key = self.get_key(point)
        return self.nodes[key]

    def get_key(self, point):
        """
        Explain:
            - given a point, return the key of the dictionary self.nodes that should contain it.
            - the key is a string of three characters, each of which is either "+" or "-".
            - the first character is "+" if the x-coordinate of the point is greater than the x-coordinate of the node,
            and "-" otherwise.
            - note that it does not matter if we use ">" or ">="; AND whether we output "+" or "-" when x is greater.
            in the above definition, as long as we are consistent.
            This is because this method is aa high level abstraction of the underlying implementation of the tree, and
            we frankly don't care which coordinate is used to compare the points, or whether we use ">" or ">=",
            as long as we are consistent.

        Complexity:
            Since we only use assignment, comparison and return statements, the complexity is always O(1).
            - Worst case: O(1)
            - Best case: O(1)
        """
        x_self, x_point = self.key[0], point[0]
        y_self, y_point = self.key[1], point[1]
        z_self, z_point = self.key[2], point[2]

        return ("+" if x_self <= x_point else "-") + ("+" if y_self <= y_point else "-") + (
            "+" if z_self <= z_point else "-")


class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT

            Complexity:
            O(1) Constant time
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Explain:
            - Checks to see if the 3DBT is empty

            Args:
            - None

            Raises:
            - None

            Returns:
            - Boolean
                - true, if the length of the 3DBT is 0.
                - false, if the length is not empty.

            Complexity:
            - Worst case: O(1), return and if statement
            - Best case: O(1), return and if statement
       """
        return len(self) == 0

    def __len__(self) -> int:
        """
            Explain:
            - Get the length of the 3DBT

            Args:
            - None

            Raises:
            - None

            Returns:
            - the length of the tree

            Complexity:
            - Worst case: O(1), return statement
            - Best case: O(1), return statement
       """
        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Explain:
            - Checks to see if the key is in the 3DBT.

            Args:
            - key, the point have to find.

            Raises:
            - KeyError, if the key is not exist.

            Returns:
            - Boolean
                - true, if the key is in the 3DBT.
                - false, if the key is not in the 3DBT.

            Complexity:
            Since get_tree_node_by_key has a complexity of O(log n)
            - Worst case:O(CompK * D) where D is the depth of the tree
                        - In balanced BST case: O(log(N) * (Comp== + Comp< or Comp>))
                            - Where N is the number of node in BST
                        - In unbalanced BST case: O(N * (Comp== + Comp< or Comp>))
                            - Where N is the number of node in BST

            - Best case:In balanced and unbalanced BST case: O(Comp==)
                    - Return statement is constant time, O(1).
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Explain:
            - Attempts to get an item in the tree, it uses the Key to attempt to find it

            Args:
            - key, a point

            Returns:
            - a BeeNode

            Complexity: O(Comp(get_tree_node_by_key)). See the function.
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        """
            Explain:
            - Get the BeeNode by using get_tree_node_by_key_aux method to search.

            Args:
            - key, the point to determine the node in 3DBT

            Raises:
            - None

            Returns:
            - A BeeNode which is the target node by given key

            Complexity: O(Comp(get_tree_node_by_key_aux)). See the function.
        """
        return self.get_tree_node_by_key_aux(self.root, key)

    # below function added by me
    def get_tree_node_by_key_aux(self, current: BeeNode, key: Point) -> BeeNode:
        """
            Explain:
            - Search the node located in the subtree rooted at current

            Args:
            - current
            - key

            Raises:
            - KeyError, if the key is not found.

            Returns:
            - A BeeNode which is the target node by given key.

            Complexity:
            We know get_child_for_key has a complexity of O(1). Hence this complexity
            is the same as the complexity of the bst.py's get_node_by_key_aux method.

            - Worst case: O(CompK * D) where D is the depth of the tree
                - In balanced BST case: O(log(N) * (Comp== + Comp< or Comp>))
                    - Where N is the number of node in BST
                    - When the target node is a leaf
                    - Since the BST is balanced, so we have to traverse nearly half of the node for checking each node.

                - In unbalanced BST case: O(N * (Comp== + Comp< or Comp>))
                    - Where N is the number of node in BST
                    - When the target node is a leaf or key not found
                    - Since the BST is unbalanced, so we have to traverse almost every node for checking.
                    - Return statement is constant time, O(1).

            - Best case:
                - In balanced and unbalanced BST case: O(Comp==)
                    - When the target node is the root,
                    - thus it just have to compare for checking the key once and directly return.
                    - Return statement is constant time, O(1).
        """
        if current is None:
            raise KeyError('Key not found: {0}'.format(key))
        if key == current.key:
            return current
        return self.get_tree_node_by_key_aux(current.get_child_for_key(key), key)

    def __setitem__(self, key: Point, item: I) -> None:
        """
            Explain:
            - Attempts to insert an item into the tree, it uses the Key to insert it

            Args:
            - key, the key of the node have to insert
            - item, the item of the node have to store

            Returns:
            - current, the root of the 3DBT

            Complexity:
            similar to that of BST's insert_aux method, with the only difference being that
            we call get_key() on the point to get the key to insert into the tree.


            - Worst case: O(CompK * D) inserting at the bottom of the tree
                        - where CompK is the complexity of comparing the keys
                Balanced tree:
                        - O(log(N) * (Comp< or Comp>))
                        - where D is the depth of the tree
                Unbalanced tree:
                        - O(N * (Comp< or Comp>))
                        - All assignments, numerical operations, return statements are constant time, O(1).

            - Best case: O(1 * CompK), when all the N nodes are at one side of the tree, and we insert at the other side
                        - Note that this only happens if the tree is unbalanced
                        - CompK is the complexity of comparing the keys
                        - All assignments, numerical operations, return statements are constant time, O(1).
        """
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Explain:
            - Attempts to insert an item into the tree, it uses the Key to insert it

            Args:
            - current, BeeNode which is the root of the 3DBT
            - key, the key of the node have to insert
            - item, the item of the node have to store

            Raises:
            - ValueError, if the item is already existed

            Returns:
            - current, the root of the 3DBT

            Complexity:
            similar to that of BST's insert_aux method, with the only difference being that
            we call get_key() on the point to get the key to insert into the tree.


            - Worst case: O(CompK * D) inserting at the bottom of the tree
                        - where CompK is the complexity of comparing the keys
                Balanced tree:
                        - O(log(N) * (Comp< or Comp>))
                        - where D is the depth of the tree
                Unbalanced tree:
                        - O(N * (Comp< or Comp>))
                        - All assignments, numerical operations, return statements are constant time, O(1).

            - Best case: O(1 * CompK), when all the N nodes are at one side of the tree, and we insert at the other side
                        - Note that this only happens if the tree is unbalanced
                        - CompK is the complexity of comparing the keys
                        - All assignments, numerical operations, return statements are constant time, O(1).
        """
        if current is None:  # base case: at the leaf
            current = BeeNode(key, item=item)
            self.length += 1
        elif key == current.key:
            raise ValueError('Inserting duplicate item')
        else:
            k_ = current.get_key(key)
            current.subtree_size += 1
            current.nodes[k_] = self.insert_aux(current.nodes[k_], key, item)
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """
            Explain:
            - Simple check whether the node is a leaf. It looks at the nodes' dictionary, and if all of the
            values are None, then it is a leaf.

            Args:
            - current, the node to check

            Returns:
            - boolean, whether the node is a leaf

            Complexity: O(1)
            - worst = best = O(1)
                -return statement is constant time, O(1).
                -if comparison is constant time, O(1).
        """
        return current.subtree_size == 1


if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2



