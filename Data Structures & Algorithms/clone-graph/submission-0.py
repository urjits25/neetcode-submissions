"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        og_cg = {}
        def dfs(cur):
            if not cur:
                return None

            if cur not in og_cg:
                cn = Node(cur.val)
                og_cg[cur] = cn
                for ne in cur.neighbors: 
                    dfs(ne)
                    cn.neighbors.append(og_cg[ne])
            return

        dfs(node)
        return og_cg[node]