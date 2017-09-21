from collections import namedtuple


class Node:
    """
    Node is the structure that represents one node within a tree
    """
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary tree is a structure that contains a root Node.  Each leaf may have up to two children leaves
    labeled left and right
    """
    INORDER = 0
    PREORDER = 1
    POSTORDER = 2

    def __init__(self):
        self.root = None

    def push(self, value):
        """
        Add a value to the tree
        """
        if not self.root:  # first leaf
            self.root = Node(value, None)
        else:
            self._push(value, self.root)

    def traverse(self, order=INORDER):
        """
        Traverse the tree in either inorder, preorderm or, postoder
        """
        order_funcs = {
            self.INORDER: self._inorder,
            self.PREORDER: self._preorder,
            self.POSTORDER: self._postorder
        }

        if order not in order_funcs:
            raise Exception("Traversal order value not valid")

        if self.root:
            selected = order_funcs[order]
            selected(self.root)

    # Private Helper Functions
    def _push(self, value, leaf):
        """
        Recursive helper function to find correct spot in tree
        """
        if value < leaf.value:
            if not leaf.left:
                leaf.left = Node(value, leaf)
            else:
                self._push(value, leaf.left)
        else:
            if not leaf.right:
                leaf.right = Node(value, leaf)
            else:
                self._push(value, leaf.right)

    @staticmethod
    def _inorder(leaf):
        if leaf.left:
            BinaryTree._inorder(leaf.left)
        print(leaf.value)
        if leaf.right:
            BinaryTree._inorder(leaf.right)

    @staticmethod
    def _preorder(leaf):
        print(leaf.value)
        if leaf.left:
            BinaryTree._preorder(leaf.left)
        if leaf.right:
            BinaryTree._preorder(leaf.right)

    @staticmethod
    def _postorder(leaf):
        if leaf.left:
            BinaryTree._postorder(leaf.left)
        if leaf.right:
            BinaryTree._postorder(leaf.right)
        print(leaf.value)


if __name__ == "__main__":
    tree = BinaryTree()
    tree.push(6)
    tree.push(1)
    tree.push(7)
    tree.push(2)
    print("inorder:")
    tree.traverse(tree.INORDER)  # 2, 1, 6, 7
    print("preorder:")
    tree.traverse(tree.PREORDER)  # 6, 1, 2, 7
    print("postorder:")
    tree.traverse(tree.POSTORDER)  # 2, 1, 7, 6
