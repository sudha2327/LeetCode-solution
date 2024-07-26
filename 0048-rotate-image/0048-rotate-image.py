class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix[0])-1
        for i in range(len(matrix[0])):
            for j in range(i+1,len(matrix[0])):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(len(matrix[0])):
            low=0
            high=l
            while low<high:
                matrix[i][low],matrix[i][high]=matrix[i][high],matrix[i][low]
                low+=1
                high-=1

    
        
            

        