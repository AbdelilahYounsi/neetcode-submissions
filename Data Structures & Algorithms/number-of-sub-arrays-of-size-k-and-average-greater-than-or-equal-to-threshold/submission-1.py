class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = threshold*k
        L=0
        n = len(arr)
        first_sum = sum(arr[:k])
        current_sum = first_sum
        count = 1 if first_sum >= target_sum else 0
        for R in range(k,n):
            current_sum+=arr[R]
            current_sum-=arr[L]
            L+=1
            if current_sum>=target_sum:
                count+=1
        return count