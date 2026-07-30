class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = 0
        n = len(nums)
        current_streak = 0 
        for i in range(n):
            if nums[i]==1:
                current_streak+=1
                max_num = max(max_num,current_streak)
            else:
                current_streak=0
        return max_num

        