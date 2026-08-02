#a two pointer technique. i is the position where we store elements we want to keep, and j is the element we want to store
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        n = len(nums)
        while j<n:
            if nums[j]!=val:
                nums[i] = nums[j]
                j+=1
                i+=1
            else:
                j+=1
        return i



        
