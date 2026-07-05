class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        self.count=0
        self.max_count=0
        for num in nums:
            if num == 1:
                self.count+=1
                self.max_count=max(self.max_count,self.count)
            else:
                self.count=0
        return self.max_count