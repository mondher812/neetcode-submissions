class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        h1 = {}
        for i in range(len(s1)):
            h1[s1[i]] = h1.get(s1[i], 0) + 1

        l = 0
        h2 = set(h1.keys())

        for r in range(len(s2)):
            if s2[r] in h1 and h1[s2[r]] > 0:
                h1[s2[r]] -= 1

                if h1[s2[r]] == 0:
                    h2.remove(s2[r])

                if len(h2) == 0:
                    return True

            elif s2[r] in h1 and h1[s2[r]] == 0:
                # Remove characters until the previous copy
                # of s2[r] leaves the window
                while h1[s2[r]] == 0:
                    if s2[l] in h1:
                        h1[s2[l]] += 1
                        h2.add(s2[l])
                    l += 1

                # Account for the current character
                h1[s2[r]] -= 1

                if h1[s2[r]] == 0:
                    h2.remove(s2[r])

                if len(h2) == 0:
                    return True

            else:
                # Current character cannot be part of any permutation
                while l < r:
                    if s2[l] in h1:
                        h1[s2[l]] += 1
                        h2.add(s2[l])
                    l += 1

                l = r + 1

        return False