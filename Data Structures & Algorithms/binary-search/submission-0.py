class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        while L<=R:
            mid = int((L+R)/2)
            if target > nums[mid]:
                L=L+1
            elif target < nums[mid]:
                R=R-1
            else:
                return mid
        return -1