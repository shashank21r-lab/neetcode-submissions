class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr=[]
        arr2=[]
        for ch in s:
            arr.append(ch)

        for ch in t:
            arr2.append(ch)

        if sorted(arr)==sorted(arr2):
            return True
        else:
            return False