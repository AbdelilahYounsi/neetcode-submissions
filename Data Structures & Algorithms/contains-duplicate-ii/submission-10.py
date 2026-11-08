class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen_set = set()
        l,r = 0,0
        n = len(nums)
        while r<n:
            if r - l > k:
                seen_set.remove(nums[l])
                l+=1
            if nums[r] in seen_set:
                return True
            seen_set.add(nums[r])
            r+=1

        return False
