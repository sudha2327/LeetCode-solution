class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def issafe(x,y,m,n):
            return (x>=0 and x<m and y>=0 and y<n)
        dx=[1,1,0,-1,-1,-1,0,1]
        dy=[0,1,1,1,0,-1,-1,-1]
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                liv=0
                for k in range(0,8):
                    x=i+dx[k]
                    y=j+dy[k]
                    if (issafe(x,y,m,n) and (board[x][y]==1 or board[x][y]==-1)):
                        liv+=1
                
                if (board[i][j]==1 and (liv<2 or liv>3)):
                    board[i][j]=-1
                if (board[i][j]==0 and liv==3):
                    board[i][j]=2
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j]=1
                elif board[i][j]==-1:
                    board[i][j]=0
        

                
            
        