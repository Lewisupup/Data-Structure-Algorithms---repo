# topological sort for detecting cycle in DAG
from collections import defaultdict
from collections import deque

class Graph:
    # initiate graph instance
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    # add edge
    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    # DFS approach - bottom-up
    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        # recursive helper
        def dfs(v, visited, stack):

            for val in self.graph[v]:
                if not visited[val]:
                    # add new node on so-far created sub-graph
                    # from result in last recursion stack
                    # create stack
                    dfs(val, visited, stack)

            visited[v] = True
            # bottom-up print return
            stack.insert(0, v)

        # iterate all non-seen node in graph
        for i in range(self.V):
            if not visited[i]:
                dfs(i, visited, stack)

        return stack

    # BFS approach - top-down
    def topological_sort_2(self):
        # check if is src or dest
        in_degree = [0] * self.V

        # one pass counter
        for src in self.graph:
            for dest in self.graph[src]:
                in_degree[dest] += 1

        # double-linked list queue
        # iterative bfs
        queue = deque([])
        for v in range(self.V):
            if not in_degree[v]:
                queue.append(v)

        # push node only with 0 in-degree on queue
        ret = []
        while queue:
            node = queue.popleft()

            ret.append(node)
            for j in self.graph[node]:
                # update counter
                in_degree[j] -= 1
                if not in_degree[j]:
                    queue.append(j)

        return ret

# testing
if __name__ == '__main__':
    g = Graph(6)

    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print(g.topological_sort())
    print(g.topological_sort_2())