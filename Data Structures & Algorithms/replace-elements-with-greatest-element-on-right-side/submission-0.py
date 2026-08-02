class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        max_elt=-1
        for i in range(n-1,-1,-1):
            curr_elt=arr[i]
            arr[i]=max_elt
            max_elt = max(max_elt,curr_elt)
        return arr



        