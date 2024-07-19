class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l=len(s)
        arr=["" for i in range(l)]
        row=0
        if numRows==1:
            return s
        for i in range(l):
            arr[row]+=s[i]
            if row==numRows-1:
                down=False
            elif row==0:
                down=True
            
            if down:
                row+=1
            else:
                row-=1
            
        return "".join(arr)

        