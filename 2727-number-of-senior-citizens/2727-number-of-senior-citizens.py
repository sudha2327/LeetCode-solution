class Solution:
    def countSeniors(self, details: List[str]) -> int:
        x=0
        for i in details:
            if int(i[11:13])>60:
                x+=1
        return x


    
        