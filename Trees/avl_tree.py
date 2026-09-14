from numbers import Number


class AVLTree:

    class AVLNode:
        def __init__(self, value):
            self.__value: Number = value
            self.__left_child: "AVLTree.AVLNode | None" = None
            self.__right_child: "AVLTree.AVLNode | None" = None
            self.__height: Number = 0

        def set_right_child(self, value: "Number | AVLTree.AVLNode") -> None:

            if isinstance(value, Number):
                self.__right_child = AVLTree.AVLNode(value)
            elif (isinstance(value, AVLTree.AVLNode) or not value):
                self.__right_child = value
            else:
                raise TypeError("Value should be AVLNode or Number")

        def set_left_child(self, value: "Number | AVLTree.AVLNode") -> None:

            if isinstance(value, Number):
                self.__left_child = AVLTree.AVLNode(value)
            elif (isinstance(value, AVLTree.AVLNode) or not value):
                self.__left_child = value
            else:
                raise TypeError("Value should be AVLNode or Number")

        def set_height(self, value: "Number | AVLTree.AVLNode") -> None:
            self.__height = value

        def get_value(self) -> Number:
            return self.__value

        def get_left_child(self) -> "AVLTree.AVLNode | None":
            return self.__left_child

        def get_right_child(self) -> "AVLTree.AVLNode | None":
            return self.__right_child

        def get_height(self) -> Number:
            return self.__height

        def __str__(self):
            return f"Node({self.__value})"

    def __init__(self):
        self.__root: "AVLTree.AVLNode | None" = None

    def set_root(self, value: Number) -> None:
        self.__root = AVLTree.AVLNode(value)

    def get_root(self) -> "AVLTree.AVLNode | None":
        return self.__root

    @staticmethod
    def __get_height(node) -> Number:
        """
        Return stored node height.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        return node.get_height() if node else -1

    def insert(self, value) -> None:
        """
        Insert a value into the AVL tree.

        Time Complexity:
            O(log n) average/worst because AVL keeps the tree balanced.

        Space Complexity:
            O(log n) because recursive insertion uses call stack space.
        """
        self.__root = self.__insert(value, self.__root)

    def __insert(self, value, root):
        """
        Recursive AVL insertion.

        Steps:
            1. Insert like a normal BST.
            2. Update height.
            3. Check balance factor.
            4. Apply rotation if needed.

        Time Complexity:
            O(log n)

        Space Complexity:
            O(log n)
        """
        if root is None:
            return AVLTree.AVLNode(value)

        if value < root.get_value():
            root.set_left_child(self.__insert(value, root.get_left_child()))

        elif value > root.get_value():
            root.set_right_child(self.__insert(value, root.get_right_child()))

        else:
            return root

        left_height, right_height = self.__get_child_height(root)
        self.__reset_node_height(root, left_height, right_height)

        if self.__is_right_heavy(left_height, right_height):

            right_child = root.get_right_child()
            rlh, rrh = self.__get_child_height(right_child)

            # Right-Left case
            if rlh - rrh > 0:
                root.set_right_child(self.__rotate_right(right_child))

            return self.__rotate_left(root)

        if self.__is_left_heavy(left_height, right_height):

            left_child = root.get_left_child()
            llh, lrh = self.__get_child_height(left_child)

            # Left-Right case
            if llh - lrh < 0:
                root.set_left_child(self.__rotate_left(left_child))

            return self.__rotate_right(root)

        return root

    def __rotate_left(self, root):
        """
        Perform left rotation.

        Used for:
            Right-Right case
            Right-Left case after right rotation on right child

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        new_root = root.get_right_child()
        root.set_right_child(new_root.get_left_child())
        new_root.set_left_child(root)

        lh, rh = self.__get_child_height(root)
        self.__reset_node_height(root, lh, rh)

        lh, rh = self.__get_child_height(new_root)
        self.__reset_node_height(new_root, lh, rh)

        return new_root

    def __rotate_right(self, root):
        """
        Perform right rotation.

        Used for:
            Left-Left case
            Left-Right case after left rotation on left child

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """
        new_root = root.get_left_child()
        root.set_left_child(new_root.get_right_child())
        new_root.set_right_child(root)

        lh, rh = self.__get_child_height(root)
        self.__reset_node_height(root, lh, rh)

        lh, rh = self.__get_child_height(new_root)
        self.__reset_node_height(new_root, lh, rh)

        return new_root

    def __get_child_height(self, root):
        left_child = root.get_left_child()
        right_child = root.get_right_child()

        left_height = AVLTree.__get_height(left_child)
        right_height = AVLTree.__get_height(right_child)

        return left_height, right_height

    def __reset_node_height(self, root,  left_height, right_height):
        root.set_height(max(left_height, right_height) + 1)

    def __balance_factor(self, left_height, right_height) -> Number:
        """
        Balance factor = left subtree height - right subtree height.

        If balance factor > 1:
            node is left-heavy.

        If balance factor < -1:
            node is right-heavy.

        Time Complexity:
            O(1)

        Space Complexity:
            O(1)
        """

        return (
            left_height -
            right_height
        )

    def __is_right_heavy(
            self,
            left_height,
            right_height
    ) -> bool:

        is_less_than1 = (self.__balance_factor(
            left_height,
            right_height
        ) < -1)

        return (is_less_than1)

    def __is_left_heavy(
            self,
            left_height,
            right_height
    ) -> bool:

        is_more_than_one = (self.__balance_factor(
            left_height,
            right_height
        ) > 1)

        return (is_more_than_one)

    def print_tree(self) -> None:
        self.__print_tree(self.__root, "", True)

    def __print_tree(self, node, indent, is_last):

        if node is None:
            return

        print(indent, end="")

        if is_last:
            print("└── ", end="")
            indent += "    "
        else:
            print("├── ", end="")
            indent += "│   "

        print(
            f"({node.get_value()}) "
            f"(h={node.get_height()}) "
            f"(hLeft={AVLTree.__get_height(node.get_left_child())}) "
            f"(hRight={AVLTree.__get_height(node.get_right_child())})"
        )

        left = node.get_left_child()
        right = node.get_right_child()

        if left:
            self.__print_tree(left, indent, right is None)

        if right:
            self.__print_tree(right, indent, True)


if __name__ == "__main__":
    tree = AVLTree()

    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(10)
    tree.insert(25)
    tree.insert(35)
    tree.insert(50)
    tree.insert(5)
    tree.insert(15)
    tree.insert(45)
    tree.insert(50)
    tree.insert(46)

    tree.print_tree()
