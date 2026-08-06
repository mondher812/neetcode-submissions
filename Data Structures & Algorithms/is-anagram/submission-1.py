class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = [0 for _ in range(26)]
        for l in s:
            hs[ord(l) - ord("a")] +=  1
        for letter in t:
              hs[ord(letter) - ord("a")] -= 1
        for slot in hs:
            if slot != 0:
                return False
        return True



        