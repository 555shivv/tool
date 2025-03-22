class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if not node.left:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def inorder_traversal(self):
        if not self.root:
            return []
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.data)
            self._inorder_traversal(node.right, result)

    def preorder_traversal(self):
        if not self.root:
            return []
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_traversal(node.left, result)
            self._preorder_traversal(node.right, result)

    def postorder_traversal(self):
        if not self.root:
            return []
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, node, result):
        if node:
            self._postorder_traversal(node.left, result)
            self._postorder_traversal(node.right, result)
            result.append(node.data)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph.get(node, []):
            if neighbor not in visited:
                self._dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            current = queue.pop(0)
            print(current, end=" ")
            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx <= 0:
            return
        elif self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._percolate_up(parent_idx)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._percolate_down(0)
        return min_val

    def _percolate_down(self, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        smallest = idx
        if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[smallest]:
            smallest = left_idx
        if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[smallest]:
            smallest = right_idx
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._percolate_down(smallest)


def test_binary_tree():
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(3)
    bt.insert(7)
    bt.insert(12)
    bt.insert(20)

    assert bt.inorder_traversal() == [3, 5, 7, 10, 12, 15, 20]
    assert bt.preorder_traversal() == [10, 5, 3, 7, 15, 12, 20]
    assert bt.postorder_traversal() == [3, 7, 5, 12, 20, 15, 10]
    print("Binary Tree Tests Passed!")


def test_graph():
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    assert g.graph == {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}

    print("Graph Tests Passed!")


def test_min_heap():
    mh = MinHeap()
    mh.insert(10)
    mh.insert(5)
    mh.insert(15)
    mh.insert(3)
    mh.insert(7)

    assert mh.heap == [3, 5, 15, 10, 7]
    assert mh.extract_min() == 3
    assert mh.heap == [5, 7, 15, 10]

    print("Min Heap Tests Passed!")


def main(in1):
    test_binary_tree()
    test_graph()
    test_min_heap()

    print("\nBinary Tree Traversals:")
    bt = BinaryTree()
    bt.insert(in1)
    bt.insert(5)
    bt.insert(in1)
    bt.insert(3)
    bt.insert(7)
    bt.insert(in1)
    bt.insert(in1)
    print("Inorder Traversal:", bt.inorder_traversal())
    print("Preorder Traversal:", bt.preorder_traversal())
    print("Postorder Traversal:", bt.postorder_traversal())

    print("\nGraph DFS:")
    g = Graph()
    g.add_edge(0, in1)
    g.add_edge(0, 2)
    g.add_edge(in1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, in1)
    g.add_edge(3, 3)
    print("DFS:", end=" ")
    g.dfs(2)

    print("\n\nGraph BFS:")
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(in1, 2)
    g.add_edge(1, in1)
    g.add_edge(2, 0)
    g.add_edge(in1, 3)
    g.add_edge(3, 3)
    print("BFS:", end=" ")
    g.bfs(2)

    print("\n\nMin Heap:")
    mh = MinHeap()
    mh.insert(in1)
    mh.insert(5)
    mh.insert(15)
    mh.insert(in1)
    mh.insert(7)
    print("Extract Min:", mh.extract_min())
    print("Heap:", mh.heap)


if __name__ == "__main__":
    main(10)
