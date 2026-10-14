class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        "If there are no cycles in the graph, it is a valid tree" - Confucius

        '''
        # If there are more than n-1 edges, there are cycles
        if len(edges) > n-1:
            return False
        
        # indegree = [0 for _ in range(n) ]
        # for s, d in edges:
        #     indegree[s] += 1
        #     indegree[d] += 1
        
        # for n in indegree:
        #     if n == 0:
        #         return False
        # return True
        
        graph = defaultdict(set)
        for s, d in edges:
            graph[s].add(d)
            graph[d].add(s)

        visited = set()
        # Now we check if all nodes are reachable, i.e. if they're connected
        bfs = deque([0])
        while bfs:
            for _ in range(len(bfs)):
                cur = bfs.popleft()
                if cur in visited:
                    continue
                
                visited.add(cur)
                for nei in graph[cur]:
                    if nei not in visited:
                        bfs.append(nei)
        return len(visited) == n
