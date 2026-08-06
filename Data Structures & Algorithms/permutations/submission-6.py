class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        start = []

        def rec(cur_set):
            if len(cur_set) == len(nums):
                start.append(cur_set)
                return
            else:

                for item in nums:
                    if item not in cur_set:
                        cur_set.append(item)
                        rec(cur_set.copy())
                        cur_set.pop()
        rec([])
        return start