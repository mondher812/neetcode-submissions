class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_m = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adj_m[crs].append(pre)

        seen = set()
        cycle = set()
        print(adj_m)
        out = []
        def dfs(c_num):
            if c_num in cycle:
                return False
            if c_num in seen:
                return True


            cycle.add(c_num)
            for pre in adj_m[c_num]:
                if not dfs(pre):
                    return False
            cycle.remove(c_num)
            seen.add(c_num)
            out.append(c_num)
            return True

        for crn in range(numCourses):
            if not dfs(crn):
                return []
        return out
                