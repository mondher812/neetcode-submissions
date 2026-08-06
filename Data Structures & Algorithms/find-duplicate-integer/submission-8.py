class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        one = nums[0]
        two = nums[nums[0]]
        while True:
            if one == two:
                break
            else:
                one = nums[one]
                two = nums[nums[two]]
        slow2 = 0
        while True:
            if slow2 ==one:
                return slow2
            else:
                slow2 = nums[slow2]
                one = nums[one]
            
            