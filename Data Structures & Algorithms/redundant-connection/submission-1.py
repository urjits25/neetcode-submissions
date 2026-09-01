class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(len(edges) + 1) ]

        graph = defaultdict(set)
        for u, v in edges:
            indegree[u] += 1
            indegree[v] += 1
            graph[u].add(v)
            graph[v].add(u)
        
        q = []
        for i in range(1, len(indegree) ):
            if indegree[i] == 1:
                q.append(i)
            
        while q:
            nq = []
            for i in range(len(q)):
                u = q[i]
                indegree[u] -= 1
                for nei in graph[u]:
                    indegree[nei] -= 1
                    if indegree[nei] == 1:
                        nq.append(nei)
            q = nq
        
        for e in range(len(edges)-1, -1, -1):
            u, v = edges[e]
            if indegree[u] == 2 and indegree[v] == 2:
                return [u, v]
        return []
                