class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        count,window={},{}
        for c in t:
            count[c]=1+count.get(c,0)
        have,need=0,len(count)
        res,reslem=[-1,-1],float('infinity')
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in count and  window[c]==count[c]:
                have+=1
            while have==need:
                if(r-l+1) < reslem:
                    res=[l,r]
                    reslem=(r-l+1)
                window[s[l]] -=1
                if s[l]in count and window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslem!=float("infinity") else ""


