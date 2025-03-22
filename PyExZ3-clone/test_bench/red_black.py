import random

class Node:
    def __init__(self, data, parent=None, color="red"):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None)
        self.root = self.NIL

    def insert(self, key):
        new_node = Node(key)
        new_node.parent = None
        new_node.data = key
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.color = "red"

        parent = None
        current = self.root
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        if new_node.parent is None:
            new_node.color = "black"
            return

        if new_node.parent.parent is None:
            return

        self.fix_insert(new_node)

    def fix_insert(self, k):
        while k != self.root and k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def inorder(self, node, result):
        if node != self.NIL:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)

    def print_tree(self):
        result = []
        self.inorder(self.root, result)
        print(result)

    def search(self, node, key):
        if node == self.NIL or key == node.data:
            return node

        if key < node.data:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def find(self, key):
        return self.search(self.root, key)


def test_red_black_tree(in1):
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(in1)
    rbt.insert(40)
    rbt.insert(50)
    rbt.insert(60)
    rbt.insert(in1)
    rbt.insert(80)
    rbt.insert(90)
    rbt.insert(in1)

    assert rbt.find(40).data == 40
    assert rbt.find(101) is None
    assert rbt.find(20).data == 20
    assert rbt.find(100).data == 100
    assert rbt.find(10).data == 10

    # Introduce randomness to trigger assertion violations sometimes
    if random.randint(0, 1) == 1:
        assert False


def main(in1):
    test_red_black_tree(in1)
    rbt = RedBlackTree()
    rbt.insert(10)
    rbt.insert(20)
    rbt.insert(30)
    rbt.insert(40)
    rbt.insert(50)
    rbt.insert(60)
    rbt.insert(70)
    rbt.insert(80)
    rbt.insert(90)
    rbt.insert(100)
    rbt.print_tree()


if __name__ == "__main__":
    main(1)

