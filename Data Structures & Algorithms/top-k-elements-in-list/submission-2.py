class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        emp_dict={}
        val=[]
        for num in nums:
            if num in emp_dict:
                emp_dict[num] += 1
            else:
                emp_dict[num] = 1

        # sort by frequency
        sorted_items = sorted(emp_dict, key=emp_dict.get,reverse=True)

        return sorted_items[:k]