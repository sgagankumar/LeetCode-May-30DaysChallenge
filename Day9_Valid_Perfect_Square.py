class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if(num%4==0):
            num/=4
        x = num
        y = 1
        while(x-y > 0.000001):
            x=(x+y)/2
            y=num/x
        x=round(x,2)
        if(x%1==0):
           return True
        return False