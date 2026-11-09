class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        sum = 0 
        count = float('inf')
        for r in range(n):
            sum+=nums[r]
            if sum>=target:
                while l<=r and sum>=target:
                    count = min(count, r-l+1)
                    sum-=nums[l]
                    l+=1
        return 0 if count==float('inf') else count