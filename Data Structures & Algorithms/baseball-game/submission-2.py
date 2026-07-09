class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for ch in operations:
            if ch=="+":
                temp=stack[-2]+stack[-1]
                stack.append(temp)
            elif ch=="C":
                stack.pop()
            elif ch=="D":
                temp=2*stack[-1]
                stack.append(temp)
            else:
                stack.append(int(ch))
        total=sum(stack)
        return total