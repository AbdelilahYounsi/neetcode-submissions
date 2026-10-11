class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, min_sum = nums[0], nums[0]
        curr_max,curr_min = 0, 0
        total=0
        for n in nums:
            curr_max, curr_min = max(n,curr_max+n) , min(n,curr_min+n)
            total+=n
            max_sum,min_sum = max(curr_max,max_sum), min(curr_min,min_sum)
        return max(total-min_sum,max_sum) if max_sum>0 else max_sum         