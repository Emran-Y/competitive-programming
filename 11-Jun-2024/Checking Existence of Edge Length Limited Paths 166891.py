# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1


class Solution:
    def distanceLimitedPathsExist(self, n: int, edges: List[List[int]], Queries: List[List[int]]) -> List[bool]:
        Queries = [[i] + q for i, q in enumerate(Queries)]
        Queries.sort(key=lambda x: x[3])
        edges.sort(key=lambda x: x[2])
        dsu = DSU(n)
        res = [0] * len(Queries)
        j = 0
        for i, u, v, lim in Queries:
            while j < len(edges) and edges[j][2] < lim:
                p, q = edges[j][:2]
                dsu.union(p, q)
                j += 1
            res[i] = dsu.find(u) == dsu.find(v)
        return res