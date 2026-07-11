class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic_val={
            "}":"{",
            "]":"[",
            ")":"("
        }
        for ch in s:
            if ch=="(" or ch=="[" or ch=="{":
                stack.append(ch)
            elif len(stack)!=0 and stack[-1]==dic_val[ch]:
                stack.pop()
            else:
                stack.append(ch)
        if len(stack)==0:
            return True
        else:
            return False