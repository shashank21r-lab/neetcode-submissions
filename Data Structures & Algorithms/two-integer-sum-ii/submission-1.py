class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        target_list=[]
        for i in range(len(numbers)-1):
            for j in range(1,len(numbers)):
                if (numbers[i]+numbers[j])==target:
                    target_list.append(i+1)
                    target_list.append(j+1)
                    return target_list