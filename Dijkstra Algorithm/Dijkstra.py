# Library for INT_MAX
import sys

# Create Dijkstra's algorithm
class Graph:
    # Create graph instance
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Print solution
    def printSolution(self, dist):
        print('Vertex \tDistance from Source')
        for idx, val in enumerate(dist):
            print(idx, '\t', val)

    # Find new node with minimum distance from source
    def minDistance(self, dist, seen):
        min_dist = sys.maxsize

        min_idx = -1
        for i in range(len(dist)):
            if not seen[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_idx = i
        return min_idx

    # Define Dijkstra
    def dijkstra(self, src):
        # Initiate origin state
        dist = [sys.maxsize] * self.V
        seen = [False] * self.V
        dist[src] = 0

        # Find nearest node iteratively in a greedy way
        for i in range(self.V):
            idx_s = self.minDistance(dist, seen)
            seen[idx_s] = True

            # compare distance
            for j in range(self.V):
                if not seen[j] and self.graph[idx_s][j] and dist[idx_s] + self.graph[idx_s][j] < dist[j]:
                    dist[j] = dist[idx_s] + self.graph[idx_s][j]

        return dist
