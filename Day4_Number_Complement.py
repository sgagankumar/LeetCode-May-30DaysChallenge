class Solution:
    def findComplement(self, num: int) -> int:
        x=bin(num)[2:]
        x=x.replace('0','2')
        x=x.replace('1','0')
        x=x.replace('2','1')
        return int(x,2)