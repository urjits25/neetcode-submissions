class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        create set of `n` nodes
        1. pop one random node
        2. traverse all nodes reachable from that node, remove them from the set
        3. if no more nodes to traverse, count as one component, go to step 1
        '''
        non_v = set([x for x in range(n)])
        adj_l = defaultdict(list)
        for a, b in edges:
            adj_l[a].append(b)
            adj_l[b].append(a)
        
        res = 0

        while non_v:
            res += 1
            root = non_v.pop()
            bfs = deque([root])
            while bfs:
                
                for _ in range(len(bfs)):
                    cur = bfs.popleft()
                    for nbr in adj_l[cur]:
                        if nbr in non_v:
                            bfs.append(nbr)
                            non_v.remove(nbr)
                            
        return res