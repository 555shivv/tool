import random

class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    # for setting left node
    def setLeft(self, node):
        self.left = node

    # for setting right node
    def setRight(self, node):
        self.right = node

    # for getting the left node
    def getLeft(self):
        return self.left

    # for getting right node
    def getRight(self):
        return self.right

    # for setting data of a node
    def setData(self, data):
        self.data = data

    # for getting data of a node
    def getData(self):
        return self.data


# in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData(), end=' ')
        inorder(Tree.getRight())


# in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
def preorder(Tree):
    if Tree:
        print(Tree.getData(), end=' ')
        preorder(Tree.getLeft())
        preorder(Tree.getRight())


# in this we first traverse to the leftmost node and then to the rightmost node and then print the data
def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData(), end=' ')


def test_tree_traversals(in1):
    root = Node(1)
    root.setLeft(Node(2))
    root.setRight(Node(in1))
    root.left.setLeft(Node(in1))

    inorder_output = []
    preorder_output = []
    postorder_output = []

    def store_inorder(Tree):
        if Tree:
            store_inorder(Tree.getLeft())
            inorder_output.append(Tree.getData())
            store_inorder(Tree.getRight())

    def store_preorder(Tree):
        if Tree:
            preorder_output.append(Tree.getData())
            store_preorder(Tree.getLeft())
            store_preorder(Tree.getRight())

    def store_postorder(Tree):
        if Tree:
            store_postorder(Tree.getLeft())
            store_postorder(Tree.getRight())
            postorder_output.append(Tree.getData())

    store_inorder(root)
    store_preorder(root)
    store_postorder(root)

    assert inorder_output == [in1, 2, 1, in1]
    assert preorder_output == [1, 2, 4, 3]
    assert postorder_output == [4, in1, 3, 1]
    #assert inorder_output[0]==in1
    #assert preorder_output[0]==1
    #assert postorder-output[-1]==1

    # Introduce randomness to trigger assertion violations sometimes
    if random.randint(0, 1) == 1:
        assert False


def main(in1):
    test_tree_traversals(in1)

    root = Node(1)
    root.setLeft(Node(2))
    root.setRight(Node(3))
    root.left.setLeft(Node(4))

    print('Inorder  Traversal:')
    inorder(root)
    print('\nPreorder Traversal:')
    preorder(root)
    print('\nPostorder Traversal:')
    postorder(root)


if __name__ == '__main__':
    main(1)

