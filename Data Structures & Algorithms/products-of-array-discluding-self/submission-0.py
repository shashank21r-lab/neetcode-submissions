class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_list=[]
        product=1
        j=0
        while j<len(nums):
            for i in range(len(nums)):
                if i!=j:
                    product*=nums[i]
            product_list.append(product)
            j+=1
            product=1
        return product_list