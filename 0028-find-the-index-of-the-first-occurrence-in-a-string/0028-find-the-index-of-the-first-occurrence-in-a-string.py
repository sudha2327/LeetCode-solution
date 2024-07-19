class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l,m=len(haystack),len(needle)
        for i in range(l):
            if(haystack[i:i+m]==needle):
                return i
        
        return -1