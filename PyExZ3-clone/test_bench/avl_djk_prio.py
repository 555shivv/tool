class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if not root:
            return AVLTreeNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)
        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)
        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def preorder_traversal(self, root):
        if not root:
            return []
        result = [root.data]
        result.extend(self.preorder_traversal(root.left))
        result.extend(self.preorder_traversal(root.right))
        return result


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph.get(node, []):
            if neighbor[0] not in visited:
                self._dfs(neighbor[0], visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        while queue:
            current = queue.pop(0)
            print(current, end=" ")
            for neighbor in self.graph.get(current, []):
                if neighbor[0] not in visited:
                    visited.add(neighbor[0])
                    queue.append(neighbor[0])

    def dijkstra(self, start):
        distances = {node: float("inf") for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_node = min(priority_queue)
            priority_queue.remove((current_distance, current_node))
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    priority_queue.append((distance, neighbor))
        return distances


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(reverse=True)

    def pop(self):
        if self.queue:
            return self.queue.pop()[1]
        return None


def test_avl_tree():
    avl = AVLTree()
    root = None
    root = avl.insert(root, 10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)
    root = avl.insert(root, 40)
    root = avl.insert(root, 50)
    root = avl.insert(root, 25)

    assert avl.preorder_traversal(root) == [30, 20, 10, 25, 40, 50]
    print("AVL Tree Tests Passed!")


def test_graph():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 0, 2)

    assert g.graph == {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: [(4, 3)], 4: [(0, 2)]}

    print("Graph Tests Passed!")


def test_dijkstra():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 0, 2)

    assert g.dijkstra(0) == {0: 0, 1: 3, 2: 1, 3: 4, 4: 6}

    print("Dijkstra Tests Passed!")


def main():
    test_avl_tree()
    test_graph()
    test_dijkstra()

    print("\nAVL Tree Preorder Traversal:")
    avl = AVLTree()
    root = None
    root = avl.insert(root, 10)
    root = avl.insert(root, 20)
    root = avl.insert(root, 30)
    root = avl.insert(root, 40)
    root = avl.insert(root, 50)
    root = avl.insert(root, 25)
    print(avl.preorder_traversal(root))

    print("\nGraph DFS:")
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 0, 2)
    print("DFS:", end=" ")
    g.dfs(2)

    print("\n\nGraph BFS:")
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 0, 2)
    print("BFS:", end=" ")
    g.bfs(2)

    print("\n\nDijkstra's Shortest Path:")
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 0, 2)
    print("Shortest Distances from Node 0:", g.dijkstra(0))


if __name__ == "__main__":
    main()

