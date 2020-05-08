class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        l=len(coordinates)
        if(l==2):
            return True
        c1=coordinates[0]
        c2=coordinates[1]
        x1=c1[0]
        y1=c1[1]
        if(c2[0]-c1[0]==0):
            return False
        m=(c2[1]-c1[1])/(c2[0]-c1[0])
        for i in range(2,l):
            x,y=coordinates[i]
            py=(m*(x-x1))+y1
            if(y!=py):
                return False
        return True