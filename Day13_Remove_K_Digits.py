class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for n in num:
            while k and stack and stack[-1]>n:
                stack.pop()
                k-=1
            stack.append(n)
        
        stack = stack[:-k] if k else stack
        #print(stack)
        return "".join(stack).lstrip('0') or "0"