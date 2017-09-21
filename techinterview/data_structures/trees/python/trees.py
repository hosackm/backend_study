class Node:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node({})".format(self.value)


class BinarySearchTree:
    PREORDER = 0
    INORDER = 1
    POSTORDER = 2

    def __init__(self):
        self.root = None

    def add_node(self, value):
        """
        Inserts a new node into the tree with value equal to value
        """
        newnode = Node(value)
        if not self.root:
            self.root = newnode
        else:
            self._recursive_add_node(self.root, newnode)

    def delete_node(self, value):
        """
        Removes the first node that that has the value equal to value
        """
        if self.root:
            self.root = self._recursive_delete_node(self.root, value)

    def _recursive_add_node(self, node, newnode):
        """
        Helper function to recursively search through tree until it finds a location to add the new node
        """
        if newnode.value < node.value:
            if not node.left:
                node.left = newnode
                newnode.parent = node
            else:
                self._recursive_add_node(node.left, newnode)
        else:
            if not node.right:
                node.right = newnode
                newnode.parent = node
            else:
                self._recursive_add_node(node.right, newnode)

    def _recursive_delete_node(self, node, value):
        """
        Helper function to recursively search through a tree and find the node to delete
        """
        if node is None:
            return None

        if value < node.value:
            node.left = self._recursive_delete_node(node.left, value)
        elif value > node.value:
            node.right = self._recursive_delete_node(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            min_node_in_right_subtree = self._get_min_node(node.right)
            node.value = min_node_in_right_subtree.value
            node.right = self._recursive_delete_node(node.right, min_node_in_right_subtree.value)

        return node

    def _get_min_node(self, node):
        """
        Helper function to find the minimum value in a tree
        """
        if node.left is None:
            return node
        return self._get_min_node(node.left)

    def traverse(self, order=PREORDER):
        """
        Traverses a tree and prints a node on a single line.  You can choose which order to traverse the tree
        """
        print("Tree:")
        if order == self.PREORDER:
            self._trav_preorder(self.root)
        elif order == self.INORDER:
            self._trav_inorder(self.root)
        elif order == self.POSTORDER:
            self._trav_postorder(self.root)

    def _trav_preorder(self, node):
        """
        Helper function to traverse a tree recursively in preorder
        """
        if node:
            self._trav_preorder(node.left)
            self._trav_preorder(node.right)
            print(node)

    def _trav_inorder(self, node):
        """
        Helper function to traverse a tree recursively in inorder
        """
        if node:
            self._trav_inorder(node.left)
            print(node)
            self._trav_inorder(node.right)

    def _trav_postorder(self, node):
        """
        Helper function to traverse a tree recursively in postorder
        """
        if node:
            print(node)
            self._trav_postorder(node.left)
            self._trav_postorder(node.right)


if __name__ == "__main__":
    t = BinarySearchTree()
    t.add_node(50)
    t.add_node(30)
    t.add_node(20)
    t.add_node(40)
    t.add_node(70)
    t.add_node(60)
    t.add_node(80)

    t.traverse(BinarySearchTree.INORDER)  # 20->30->40->50->60->70->80

    t.delete_node(20)
    t.traverse(BinarySearchTree.INORDER)  # 30->40->50->60->70->80

    t.delete_node(30)
    t.traverse(BinarySearchTree.INORDER)  # 40->50->60->70->80

    t.delete_node(50)
    t.traverse(BinarySearchTree.INORDER)  # 40->60->70->80
