""" Binary Search Tree ADT.
    Defines a Binary Search Tree with linked nodes.
    Each node contains a key and item as well as references to the children.
"""

from __future__ import annotations

__author__ = 'Brendon Taylor, modified by Alexey Ignatiev, further modified by Jackson Goerner'
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from node import TreeNode
import sys


# generic types
K = TypeVar('K')
I = TypeVar('I')
T = TypeVar('T')


class BinarySearchTree(Generic[K, I]):
    """ Basic binary search tree. """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Explain:
            - Checks to see if the bst is empty

            Args:
            - None

            Raises:
            - None

            Returns:
            - Boolean
                -true - if the root is None
                -false - if the root is not None

            Complexity:
            - Worst case: O(1), return statement
            - Best case: O(1), return statement
       """
        return self.root is None

    def __len__(self) -> int:
        """
            Explain:
            - Returns the number of nodes in the tree.

            Args:
            - None

            Raises:
            - None

            Returns:
            - length of the BST

            Complexity:
            - Worst case: O(1), return statement
            - Best case: O(1), return statement
       """
        return self.length

    def __contains__(self, key: K) -> bool:
        """
            Explain:
            - Checks to see if the key is in the BST

            Args:
            - K, key of the node

            Raises:
            - KeyError, if the key is not occur.

            Returns:
            - Boolean
                - true, if the node of the key is contained in the BST.
                - false, if the node of the key is not contained in the BST.

            Complexity:
            - Worst case: O(__getitem__())(worst) = O(CompK * D)
                        - when item is not found, where D is the depth of the tree
                        - CompK is the complexity of comparing the keys

            - Best case: O(__getitem__())(best) = O(CompK)
                        - when finds the item in the root of the tree
                        - CompK is the complexity of comparing the keys
       """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> I:
        """
            Explain:
            - Attempts to get an item in the tree, it uses the Key to attempt to find it.

            Args:
            - K, key of the node

            Raises:
            - None

            Returns:
            - item of the node with key K

            Complexity:
            - Worst case: O(CompK)
                        - when finding the item in the root of the tree
                        - CompK is the complexity of comparing the keys

            - Best case: O(CompK * D)
                        - when item is not found, where D is the depth of the tree
                        - CompK is the complexity of comparing the keys
       """
        return self.get_tree_node_by_key(key).item

    def get_tree_node_by_key(self, key: K) -> TreeNode:
        """
            Explain:
            - get the node with the key by calling self.get_tree_node_by_key_aux() function.

            Args:
            - K, key of the node

            Raises:
            - None

            Returns:
            - A TreeNode by given key

            Complexity:
            - Worst case: O(get_tree_node_by_key_aux()) (worst)
            - Best case: O(get_tree_node_by_key_aux()) (best)
            - Return statement is constant time, O(1).
       """
        return self.get_tree_node_by_key_aux(self.root, key)

    def get_tree_node_by_key_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
            Explain:
            - find the node by given key and current

            Args:
            - current = A Treenode which is the root of the tree
            - key = The key of the finding node

            Raises:
            - KeyError, if the key is not found in the Tree.

            Returns:
            - A TreeNode by given key

            Complexity:
            - Worst case: O(CompK * D) where D is the depth of the tree
                - In balanced BST case: O(log(N) * (Comp== + Comp< + Comp>))
                    - Where N is the number of node in BST
                    - When the target node is a leaf
                    - Since the BST is balanced, so we have to traverse nearly half of the node for checking each node.

                - In unbalanced BST case: O(N * (Comp== + Comp< + Comp>))
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
        elif key == current.key:
            return current
        elif key < current.key:
            return self.get_tree_node_by_key_aux(current.left, key)
        else:  # key > current.key
            return self.get_tree_node_by_key_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        """
            Explain:
            - set the root to the result of the function insert_aux

            Args:
            - K, key of the node
            - I, item have to store in the BST with certain node

            Raises:
            - None

            Returns:
            - None

            Complexity:
            - Worst case: O(insert_aux()) (worst)
            - Best case: O(insert_aux()) (best)
            - Assignment is constant time, O(1)
       """
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: TreeNode, key: K, item: I) -> TreeNode:
        """
            Explain:
            - Attempts to insert an item into the tree, it uses the Key to insert it

            Args:
            - current, TreeNode which is the root of the BST
            - key, the key of the node have to insert
            - item, the item of the node have to store

            Raises:
            - ValueError, if the item is already existed

            Returns:
            - current, the root of the BST

            Complexity:
            - Worst case: O(CompK * D) inserting at the bottom of the tree
                        - where D is the depth of the tree
                        - CompK is the complexity of comparing the keys
                        - All assignments, numerical operations, return statements are constant time, O(1).

            - Best case: O(CompK) inserts the item at the root.
                        - CompK is the complexity of comparing the keys
                        - All assignments, numerical operations, return statements are constant time, O(1).
       """
        if current is None:  # base case: at the leaf
            current = TreeNode(key, item=item)
            current.subtree_size -= 1  # init() sets it to 1d already
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')

        current.subtree_size += 1
        return current

    def __delitem__(self, key: K) -> None:
        """
            Explain:
            -

            Args:
            - K, the key of the node have to delete

            Raises:
            - None

            Returns:
            - None

            Complexity:
            - Worst case: O(delete_aux()) (worst)
            - Best case: O(delete_aux()) (best)
       """
        self.root = self.delete_aux(self.root, key)

    def delete_aux(self, current: TreeNode, key: K) -> TreeNode:
        """
            Explain:
            - Attempts to delete an item from the tree, it uses the Key to determine the node to delete.

            Args:
            - current, TreeNode which is the root of the BST.
            - K, the key of the node to determine the node to delete.

            Raises:
            - ValueError, if the key is not found that means the node is not occur.

            Returns:
            - A TreeNode which is the root of the BST

            Complexity:
            - Worst case:
            - Best case:
       """
        if current is None:
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left  = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        current.subtree_size -= 1

        return current

    def get_successor(self, current: TreeNode) -> TreeNode:
        """
            Explain:
            - Get successor of the current node.
            - It should be a child node having the smallest key among all the larger keys.

            Args:
            - current, a Treenode.
            Raises:
            - ValueError, if there is no existing item.

            Returns:
            - A TreeNode which is the successor of the current node.

            Complexity:
            - Worst case: O(D)
                        - where D is the leftmost depth of the current.right subtree.
                        - Since we have to find the successor of the current node
                        - which located at the left bottom of the current.right,
                        - thus we have to traverse D times to get the successor node.

            - Best case: O(1)
                        - When the current node does not have right child node
                        - All assignments, if statements and return statement are constant time, O(1)
       """
        if current is None:
            raise ValueError('non existing item')
        if current.right is None:
            return None
        current = current.right
        while current.left is not None:
            current = current.left
        return current

    def get_minimal(self, current: TreeNode) -> TreeNode:
        """
            Explain:
            - Get a node having the smallest key in the current sub-tree.

            Args:
            - current, a TreeNode.

            Raises:
            - ValueError, if there is no existing item.

            Returns:
            - A TreeNode which has the minimum key.

            Complexity:
            - Worst case: O(L)
                        - Where L is the total number of leftmost node in BST
                        - Since the minimal node is located at the left bottom of the tree.
                        - We just have to traverse the leftmost node, so its depends on how long of the leftmost node.

            - Best case: O(log(N))
                        - Where N is the total number of the node in the tree.
                        - Since the minimal node is located at the left bottom of the tree.
                        - When the tree is balanced,
                        - we have to traverse the nodes of each left subtree for checking each node.
                        - Thus, almost half of the nodes of subtree does not require to check.

       """
        if current is None:
            raise ValueError('non existing item')
        while current.left is not None:
            current = current.left
        return current


    def is_leaf(self, current: TreeNode) -> bool:
        """
            Explain:
            - Simple check whether or not the node is a leaf.

            Args:
            - current, a TreeNode

            Raises:
            - None

            Returns:
            - Boolean
                - true, if the node does not have any child node
                - false, if the node has at least one child node

            Complexity:
            - Worst case: O(1), return statement
            - Best case: O(1), return statement
       """
        return current.left is None and current.right is None

    def draw(self, to=sys.stdout):
        """ Draw the tree in the terminal. """

        # get the nodes of the graph to draw recursively
        self.draw_aux(self.root, prefix='', final='', to=to)

    def draw_aux(self, current: TreeNode, prefix='', final='', to=sys.stdout) -> K:
        """ Draw a node and then its children. """

        if current is not None:
            real_prefix = prefix[:-2] + final
            print('{0}{1}'.format(real_prefix, str(current.key)), file=to)

            if current.left or current.right:
                self.draw_aux(current.left,  prefix=prefix + '\u2551 ', final='\u255f\u2500', to=to)
                self.draw_aux(current.right, prefix=prefix + '  ', final='\u2559\u2500', to=to)
        else:
            real_prefix = prefix[:-2] + final
            print('{0}'.format(real_prefix), file=to)

    def kth_smallest(self, k: int, current: TreeNode) -> TreeNode:
        """
            Explain:
            - Finds the kth smallest value by key in the subtree rooted at current.

            Args:
            - k, an integer which is the number of how smallest by key in the subtree.
            - current, a treenode which is the root of the subtree.

            Raises:
            - ValueError, if the node is not occur or k is larger than the number of the tree or subtree.

            Returns:
            - A TreeNode which is the kth smallest value by key in the subtree rooted at current.

            Complexity:
            - Worst case:
            - Best case:
       """
        if current is None:
            raise ValueError('node is None')

        if current.left:
            left_size = current.left.subtree_size
        else:
            left_size = 0

        if k == left_size + 1:
            return current
        elif k < left_size + 1:
            return self.kth_smallest(k, current.left)
        else:
            if not current.right:
                raise ValueError('k is too large')
            return self.kth_smallest(k - left_size - 1, current.right)

if __name__ == "__main__":
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

    for i in range(1, 32):
        kth = BST.kth_smallest(i, BST.root)
        print(i, ",", kth.key)