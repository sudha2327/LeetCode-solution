class Solution:
    def longestCommonPrefix(self, num: List[str]) -> str:
        size=len(num)
        if(size==0):
            return ""
        if(size==1):
            return num[0]
        num.sort()
        end=min(len(num[0]),len(num[size-1]))
        i=0
        while(i<end and num[0][i]==num[size-1][i]):
            i+=1
        pre=num[0][0:i]
        return pre
        



        