class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax = nums[0]
        cmin = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cmax, cmin = cmin, cmax

            cmax = max(nums[i], cmax * nums[i])
            cmin = min(nums[i], cmin * nums[i])

            result = max(result, cmax)

        return result