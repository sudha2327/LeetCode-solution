class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[1]
        for i in range(rowIndex):
            nxt_row=[0]*(len(res)+1)
            for j in range(len(res)):
                nxt_row[j]+=res[j]
                nxt_row[j+1]+=res[j]
            res=nxt_row
        return res
        