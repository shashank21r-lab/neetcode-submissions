class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        big=-1
        for i in range(len(arr)-1,-1,-1):
            current=arr[i]
            arr[i]=big
            big=max(big,current)
        return arr