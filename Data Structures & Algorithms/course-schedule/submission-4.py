class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        c = defaultdict(list)
        seen = set()
        for p in prerequisites:
            c[p[0]].append(p[1])
        def dfs(course,path):
            if len(c[course])==0:
                seen.update(path)
                return True
            if course in seen:
                return True
            else:
                path.add(course)
                for pre in c[course]:
                    if pre in path:
                        return False
                    else:
                        if not dfs(pre,path):
                            return False
                path.remove(course)
                seen.add(course)
                return True
                
        for i in range(numCourses):
            if i not in seen:
                if not dfs(i,set()):
                    return False
        return True

