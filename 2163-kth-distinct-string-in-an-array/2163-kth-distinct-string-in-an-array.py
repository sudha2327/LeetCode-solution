class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        
        for i in arr:
            if i  not in d:
                d[i]=0
            d[i]+=1
        for i in arr:
            if d[i]==1:
                k-=1
            if k==0:
                return i
        return ''