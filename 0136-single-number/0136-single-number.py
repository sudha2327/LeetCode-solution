class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        
        for i,j in d.items():
            if j==1:
                return i
