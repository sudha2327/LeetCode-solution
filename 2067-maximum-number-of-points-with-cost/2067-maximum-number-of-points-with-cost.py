class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        row,col=len(points),len(points[0])

        rw=points[0]
        for i in range(1,row):
            nxt_row=points[i].copy()
            left,right=[0]*col,[0]*col
            left[0]=rw[0]
            for c in range(1,col):
                left[c]=max(rw[c],left[c-1]-1)
            right[col-1]=rw[col-1]
            for c in range(col-2,-1,-1):
                right[c]=max(rw[c],right[c+1]-1)
            
            for c in range(col):
                nxt_row[c]+=max(left[c],right[c])
            rw=nxt_row
        return max(rw)

