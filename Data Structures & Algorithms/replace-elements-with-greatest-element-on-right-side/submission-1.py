class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            rmax=-1
            for j in range(i+1,len(arr)):
                rmax=max(rmax,arr[j])
            arr[i]=rmax
        return arr            