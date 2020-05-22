class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        x=len(matrix[0])
        y=len(matrix)
        for i in range(y-1):
            for j in range(x-1):
                if matrix[i][j]!=0 and matrix[i+1][j]!=0 and matrix[i][j+1]!=0 and matrix[i+1][j+1]!=0:
                    matrix[i+1][j+1]+=1
                    if matrix[i][j]==matrix[i+1][j]==matrix[i][j+1]:
                        matrix[i+1][j+1]=matrix[i][j+1]+1
        
        output=0
        for i in range(y):
            output+=sum(matrix[i])
        return output
