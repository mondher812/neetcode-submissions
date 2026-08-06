class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 0] for _ in range(len(nums))]

        for i in range(len(nums)):
            dp[i][1]= i
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i][0] = max(dp[j][0]+1,dp[i][0])
                print(dp)
        out = max([dp[s][0] for s in range(len(nums))])
        return out

                


