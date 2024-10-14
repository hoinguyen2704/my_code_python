class Graph:
    def __init__(self):
        self.closed: list = []
        self.graph: dict[str, list] = {}
        self.goal: list = []
        self.open: list = []
        self.parent: dict = {}
        self.path: list = []


def add_node(self, u, v):
    if self.graph.get(u) is None:
        self.graph[u] = []
    self.graph[u].append(v)


def travel_bfs(self, start):
    self.open.append(start)
    self.closed.append(start)
    while len(self.open) > 0:
        node = self.open.pop(0)
        self.closed.append(node)
        if node in self.goal:
            return node
        if self.graph.get(node) is not None:
            for neighbour in self.graph.get(node):
                if neighbour not in self.closed:
                    self.open.append(neighbour)
                    self.parent[neighbour] = node
    return -1


def get_path(self, child):
    self.path.append(child)
    while self.parent.get(child) is not None:
        self.path.append(self.parent.get(child))
        child = self.parent.get(child)
    self.path.reverse()
    return "->".join(list(map(str, self.path)))


Graph.add_node = add_node
Graph.travel_bfs = travel_bfs
Graph.get_path = get_path
g = Graph()
g.add_node(0, 1)
g.add_node(0, 2)
g.add_node(1, 3)
g.add_node(1, 4)
g.add_node(2, 5)
g.add_node(2, 6)
g.add_node(3, 7)
g.add_node(3, 8)
g.add_node(4, 9)
g.add_node(5, 10)

g.goal = [9, 10]
print("Following is BFS (starting from vertex 0)")
element = g.travel_bfs(0)
if element != -1:
    print(g.get_path(element))
