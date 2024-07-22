class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fre={}
        maxval=0
        start=0
        for i in range(len(s)):
            if s[i] in fre:
                start=max(start,fre[s[i]]+1)
            maxval=max(maxval,i-start+1)
            fre[s[i]]=i
        return maxval


           

        