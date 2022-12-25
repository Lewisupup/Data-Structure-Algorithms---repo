from collections import defaultdict

# define union find
class Unionfind:
    def __init__(self, N):
        self.root = [i for i in range(N)]

    def find(self, x):
        if self.root[x] == x:
            return x

        return self.find(self.root[x])

    def union(self, x, y):
        self.root[x] = y

# define graph
class Graph:
    def __init__(self, N):
        self.V = N
        self.graph = defaultdict(list)

    def add(self, u, v):
        self.graph[u].append(v)

# detect cycle
def detect(Graph):
    uf = Unionfind(Graph.V)
    graph = Graph.graph

    for u in graph:
        for v in graph[u]:
            find_u = uf.find(u)
            find_v = uf.find(v)

            if find_u == find_v:
                return True

            uf.union(u, v)

    return False

# testing
if __name__ == '__main__':
    g = Graph(5)
    g.add(0, 1)
    g.add(1, 2)
    g.add(2, 3)
    g.add(3, 2)

    if detect(g):
        print('cycle detected')
    else:
        print('No cycle exists')