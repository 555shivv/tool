class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if data == self.data:
            return True
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end=' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end=' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end=' ')


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

    def pprint(self, head_node=0, _pre="", _last=True, term=False):

        head_node = self.root if head_node == 0 else head_node

        data = "*" if head_node is None else head_node.data

        print(_pre, "`- " if _last else "|- ", data, sep="")
        _pre += "   " if _last else "|  "

        if term:
            return

        for i, child in enumerate([head_node.leftChild, head_node.rightChild]):
            self.pprint(child,  _pre, bool(i) ,term=not(bool(child)))


def test_tree_operations(in1):
    tree = Tree()
    tree.insert(in1)
    tree.insert(12)
    tree.insert(5)
    tree.insert(in1)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(in1)
    tree.insert(in1)
    tree.pprint()
    
    # Test find method
    assert tree.find(1) == False
    assert tree.find(12) == True
    
    # Test preorder traversal
    expected_preorder = [10, 5, 4, 8, 7, 12, 20, 15, 13]
    preorder_result = []
    def store_preorder(node):
        if node:
            preorder_result.append(node.data)
            store_preorder(node.leftChild)
            store_preorder(node.rightChild)
    store_preorder(tree.root)
    assert expected_preorder == preorder_result
    
    # Test inorder traversal
    expected_inorder = [4, 5, 7, 8, 10, 12, 13, 15, 20]
    inorder_result = []
    def store_inorder(node):
        if node:
            store_inorder(node.leftChild)
            inorder_result.append(node.data)
            store_inorder(node.rightChild)
    store_inorder(tree.root)
    assert expected_inorder == inorder_result
    
    # Test postorder traversal
    expected_postorder = [4, 7, 8, 5, 13, 15, 20, 12, 10]
    postorder_result = []
    def store_postorder(node):
        if node:
            store_postorder(node.leftChild)
            store_postorder(node.rightChild)
            postorder_result.append(node.data)
    store_postorder(tree.root)
    assert expected_postorder == postorder_result

def main(in1):
    test_tree_operations(in1)
    print("All tests passed successfully!")
    # Deliberate error to trigger assertion error
    if random.randint(0, 1) == 1:
        assert False

if __name__ == '__main__':
    import random
    main(1)

