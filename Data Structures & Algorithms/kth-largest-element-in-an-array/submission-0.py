class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # dup=set()
        nums.sort()
        # for i in nums:
        #     dup.add(i)
        # nums=list(dup)
        return nums[-k]