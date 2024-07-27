class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=Counter(magazine)
        for i in ransomNote:
            c[i]-=1
            if c[i]<0:
                return False
        return True
       