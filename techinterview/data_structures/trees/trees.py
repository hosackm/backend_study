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
        newnode = Node(value)
        if not self.root:
            self.root = newnode
        else:
            self.recursive_add_node(self.root, newnode)

    def delete_node(self, value):
        if self.root:
            self.root = self.recursive_delete_node(self.root, value)

    def recursive_add_node(self, node, newnode):
        if newnode.value < node.value:
            if not node.left:
                node.left = newnode
                newnode.parent = node
            else:
                self.recursive_add_node(node.left, newnode)
        else:
            if not node.right:
                node.right = newnode
                newnode.parent = node
            else:
                self.recursive_add_node(node.right, newnode)

    def recursive_delete_node(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.recursive_delete_node(node.left, value)
        elif value > node.value:
            node.right = self.recursive_delete_node(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            min_node_in_right_subtree = self.get_min_node_in_subtree(node.right)
            node.value = min_node_in_right_subtree.value
            node.right = self.recursive_delete_node(node.right, min_node_in_right_subtree.value)

        return node

    def get_min_node_in_subtree(self, node):
        if node.left is None:
            return node
        return self.get_min_node_in_subtree(node.left)

    def traverse(self, order=PREORDER):
        print("Tree:")
        if order == self.PREORDER:
            self._trav_preorder(self.root)
        elif order == self.INORDER:
            self._trav_inorder(self.root)
        elif order == self.POSTORDER:
            self._trav_postorder(self.root)

    def _trav_preorder(self, node):
        if node.left:
            self._trav_preorder(node.left)
        if node.right:
            self._trav_preorder(node.right)
        if node:
            print(node)

    def _trav_inorder(self, node):
        if node.left:
            self._trav_inorder(node.left)
        if node:
            print(node)
        if node.right:
            self._trav_inorder(node.right)

    def _trav_postorder(self, node):
        if node:
            print(node)
        if node.left:
            self._trav_postorder(node.left)
        if node.right:
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
