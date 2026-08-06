class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        o = []
        past = 1*(-10**6)
        for i in range(len(nums)):
            if nums[i] == past:
                continue
            a = nums[i]
            past = a
            l = i+1
            r = len(nums)-1
            for i in range(len(nums[l:])):
                if l<r:
                    if a+nums[l]+nums[r] == 0:
                        o.append([a,nums[l],nums[r]])
                        to_add = 1
                        while l+to_add < r and nums[l] == nums[l+to_add]:
                            to_add+=1
                        l+=to_add
                    elif a+nums[l]+nums[r]<0:
                        l+=1
                    else:
                        r-=1
        return o
                


    