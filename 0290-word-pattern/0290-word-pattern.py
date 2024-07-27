class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d,d1={},{}
        l=list(s.split(" "))
        if len(pattern) !=len(l):
            return False
        for i in range(len(l)):
            if ((pattern[i] in d and d[pattern[i]]!=l[i]) or (l[i] in d1 and d1[l[i]]!=pattern[i])):
                return False

            d[pattern[i]]=l[i]
            d1[l[i]]=pattern[i]
        return True

        