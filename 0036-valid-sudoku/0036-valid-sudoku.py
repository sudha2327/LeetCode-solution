class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag=False
        for i in range(9):
            row={}
            column={}
            block={}
            row_cube=3*(i//3)
            col_cube=3*(i%3)
            for j in range(9):
                if board[i][j]!='.' and board[i][j] in row:
                    return False
                row[board[i][j]]=1
                if board[j][i]!='.' and board[j][i] in column:
                    return False
                column[board[j][i]]=1
                rr=row_cube+j//3
                cc=col_cube+j%3
                if board[rr][cc]!='.' and board[rr][cc] in block:
                    return False
                block[board[rr][cc]]=1
        return True





        
        