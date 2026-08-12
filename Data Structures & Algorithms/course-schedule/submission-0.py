from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0 for _ in range(numCourses) ]
        prm = defaultdict(list)

        for c, p in prerequisites:
            prm[p].append(c)
            ind[c] += 1

        bfs = deque([])        
        for c, d in enumerate(ind):
            if d == 0:
                bfs.append(c)
        if not bfs:
            return False
        res = []
        while bfs:
            for _ in range(len(bfs)):
                cur = bfs.popleft()
                res.append(c)
                for dep in prm[cur]:
                    ind[dep] -= 1
                    if ind[dep] == 0:
                        bfs.append(dep)

        return True if len(res) == numCourses else False
