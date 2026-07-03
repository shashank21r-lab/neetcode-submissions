class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        flag=False
        for i in range(len(nums)):
            if nums[i] in seen:
                flag =True
                break
            seen.add(nums[i])
        if flag:
            return True
        else:
            return False
                