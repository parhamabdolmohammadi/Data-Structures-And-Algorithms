from numbers import Number
import sys


class BinaryTree:
    """
    Binary Search Tree (BST)

    Average Case:
        Search: O(log n)
        Insert: O(log n)
        Delete: O(log n)

    Worst Case when tree becomes unbalanced:
        Search: O(n)
        Insert: O(n)
        Delete: O(n)

    Space Complexity:
        O(n), because the tree stores n nodes.
    """

    class Node:
        def __init__(self, value: Number):
            """
            Create a tree node.

            Time: O(1)
            Space: O(1)
            """
            self.__value = value
            self.__left_child: BinaryTree.Node | None = None
            self.__right_child: BinaryTree.Node | None = None

        def get_value(self) -> Number:
            """Return node value. Time: O(1), Space: O(1)."""
            return self.__value

        def set_left_child(self, value: Number) -> None:
            """Create and assign left child. Time: O(1), Space: O(1)."""
            self.__left_child = BinaryTree.Node(value)

        def set_right_child(self, value: Number) -> None:
            """Create and assign right child. Time: O(1), Space: O(1)."""
            self.__right_child = BinaryTree.Node(value)

        def get_left_child(self) -> "BinaryTree.Node | None":
            """Return left child node. Time: O(1), Space: O(1)."""
            return self.__left_child

        def get_right_child(self) -> "BinaryTree.Node | None":
            """Return right child node. Time: O(1), Space: O(1)."""
            return self.__right_child

    def __init__(self):
        """Create an empty tree. Time: O(1), Space: O(1)."""
        self.__root: "BinaryTree.Node | None" = None

    def get_root(self) -> "BinaryTree.Node | None":
        """Return root node. Time: O(1), Space: O(1)."""
        return self.__root if self.__root else None

    def set_root(self, val) -> None:
        """Create and assign root node. Time: O(1), Space: O(1)."""
        self.__root = BinaryTree.Node(val)

    def insert(self, value) -> None:
        """
        Insert a value into the BST.

        Average Time:
            O(log n)

        Worst Time:
            O(n)

        Space:
            O(1), because this implementation is iterative.
        """

        if self.get_root() is None:
            self.set_root(value)
            return

        current = self.get_root()

        while True:
            if current.get_value() > value:
                left_child = current.get_left_child()

                if not left_child:
                    current.set_left_child(value)
                    break
                else:
                    current = left_child
            elif current.get_value() < value:
                right_child = current.get_right_child()

                if not right_child:
                    current.set_right_child(value)
                    break
                else:
                    current = right_child
            else:
                break

            def find(self, value) -> bool:
                """
                Search for a value in the BST.

                Average Time:
                    O(log n)

                Worst Time:
                    O(n)

                Space:
                    O(1), because this implementation is iterative.

                Note:
                    This method is currently indented inside insert().
                    If you want to call tree.find(...), move it outside insert().
                """
                current = self.get_root()

                while current:
                    current_val = current.get_value()

                    if value > current_val:
                        current = current.get_right_child()
                    elif value < current_val:
                        current = current.get_left_child()
                    else:
                        return True

                return False

    def display(self) -> None:
        """
        Display the tree visually.

        Time:
            O(n)

        Space:
            O(h), because of recursive call stack.

        h = height of tree.
        """
        self.__display(self.__root, "", True)

    def __display(self, node, indent, is_last):
        """
        Recursive helper for display().

        Time:
            O(n)

        Space:
            O(h)
        """

        if node is None:
            return

        print(indent, end="")

        if is_last:
            print("└── ", end="")
            indent += "    "
        else:
            print("├── ", end="")
            indent += "│   "

        print(node.get_value())

        left = node.get_left_child()
        right = node.get_right_child()

        if left or right:

            if left:
                self.__display(left, indent, right is None)

            if right:
                self.__display(right, indent, True)

    def pre_order_traversal(self) -> list:
        """
        Pre-order DFS traversal.

        Order:
            Root -> Left -> Right

        Time:
            O(n)

        Space:
            O(h), because of recursive call stack.
        """
        visited = list()

        self.__pre_order_traversal(self.get_root(), visited)

        return visited

    def __pre_order_traversal(self, root, visited):
        """
        Recursive helper for pre-order traversal.

        Time:
            O(n)

        Space:
            O(h)
        """

        if root is None:
            return

        visited.append(root.get_value())

        self.__pre_order_traversal(
            root.get_left_child(),
            visited
        )

        self.__pre_order_traversal(
            root.get_right_child(),
            visited
        )

    def height(self) -> Number:
        """
        Return height of the tree.

        Time:
            O(n)

        Space:
            O(h)

        Note:
            Empty tree height is treated as -1.
            Leaf node height is 0.
        """
        return self.__height(self.__root)

    def __height(self, node):
        """
        Recursive helper for height().

        Time:
            O(n)

        Space:
            O(h)
        """
        if node is None:
            return -1
        else:
            return (1 +
                    max(
                        self.__height(node.get_left_child()),
                        self.__height(node.get_right_child())
                    ))

    def min_val(self):
        """
        Return minimum value in the tree.

        Current implementation checks the entire tree.

        Time:
            O(n)

        Space:
            O(h)

        Interview note:
            In a BST, the optimized version would keep going left.
            That would be O(log n) average and O(n) worst.
        """
        return self.__min_val(self.__root)

    def __min_val(self, root):
        """
        Recursive helper for min_val().

        Time:
            O(n)

        Space:
            O(h)
        """
        if root is None:
            return sys.maxsize

        return min(
            root.get_value(),
            self.__min_val(root.get_left_child()),
            self.__min_val(root.get_right_child())
        )

    @staticmethod
    def equality(tree1, tree2):
        """
        Check if two trees are equal.

        Equal means:
            Same structure
            Same values at matching nodes

        Time:
            O(n)

        Space:
            O(h)
        """
        root1 = tree1.get_root()
        root2 = tree2.get_root()
        return BinaryTree.__equality(root1, root2)

    @staticmethod
    def __equality(root1, root2):
        """
        Recursive helper for equality().

        Time:
            O(n)

        Space:
            O(h)
        """
        if (not root1 and not root2):
            return True

        if not (root1 and root2):
            return False

        if root1.get_value() != root2.get_value():
            return False

        return (BinaryTree.__equality(
            root1.get_left_child(),
            root2.get_left_child())
            and
            BinaryTree.__equality(
            root1.get_right_child(),
            root2.get_right_child())
        )

    @staticmethod
    def validation_of_binary_search_tree(
            root: "BinaryTree.Node",
            least_val=-sys.maxsize - 1,
            most_val=sys.maxsize
    ) -> bool:
        """
        Validate whether a tree is a valid BST.

        Uses ancestor bounds:
            least_val < node value < most_val

        Time:
            O(n)

        Space:
            O(h)
        """
        if root is None:
            return True

        root_value = root.get_value()

        if not (least_val < root_value < most_val):
            return False

        leftchild = root.get_left_child()
        rightchild = root.get_right_child()

        return (
            BinaryTree.validation_of_binary_search_tree(
                leftchild,
                least_val,
                root_value
            )
            and
            BinaryTree.validation_of_binary_search_tree(
                rightchild,
                root_value,
                most_val
            )
        )

    @staticmethod
    def nodes_at_k_distance(
        root,
        distance
    ) -> None:
        """
        Print all nodes k edges away from root.

        Time:
            O(n)

        Space:
            O(h)
        """

        if root is None:
            return

        if distance == 0:
            print(root.get_value(), end=", ")
            return

        BinaryTree.nodes_at_k_distance(root.get_left_child(), distance - 1)
        BinaryTree.nodes_at_k_distance(root.get_right_child(), distance - 1)

    def level_order_traversal(self):
        """
        Level-order traversal / Breadth-First Search.

        Time:
            O(n)

        Space:
            O(w)

        w = maximum width of the tree.

        Note:
            queue.pop(0) on a Python list is O(n).
            For real BFS efficiency, collections.deque is better.
        """
        queue = list()

        root = self.__root

        if not root:
            return

        queue.append(root)

        print("[", end="")
        while queue:
            current_node = queue.pop(0)
            print(current_node.get_value(), end=", ")

            if current_node.get_left_child():
                queue.append(current_node.get_left_child())

            if current_node.get_right_child():
                queue.append(current_node.get_right_child())
        print("]", end="")


tree1 = BinaryTree()

tree1.insert(7)
tree1.insert(4)
tree1.insert(9)
tree1.insert(1)
tree1.insert(6)
tree1.insert(8)
tree1.insert(10)
tree1.insert(2)
tree1.insert(3)
tree1.insert(5)
tree1.insert(12)
tree1.insert(11)
tree1.insert(15)
tree1.insert(13)
tree1.insert(14)
tree1.insert(16)
tree1.insert(0)
tree1.insert(-1)
tree1.insert(20)
tree1.insert(18)


tree2 = BinaryTree()

tree2.insert(7)
tree2.insert(4)
tree2.insert(9)
tree2.insert(1)
tree2.insert(6)
tree2.insert(8)
tree2.insert(10)
tree2.insert(2)
tree2.insert(3)
tree2.insert(5)
tree2.insert(12)
tree2.insert(11)
tree2.insert(15)
tree2.insert(13)
tree2.insert(14)
tree2.insert(16)
tree2.insert(0)
tree2.insert(-1)
tree2.insert(20)
tree2.insert(16)

tree1.display()
print(tree1.pre_order_traversal())
print(tree1.height())
print(tree1.min_val())
print(BinaryTree.equality(tree1, tree2))
print(BinaryTree.validation_of_binary_search_tree(tree1.get_root()),
      BinaryTree.validation_of_binary_search_tree(tree2.get_root()))
BinaryTree.nodes_at_k_distance(tree1.get_root(), 1)
print()
tree1.level_order_traversal()
