class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in s:
            if i in ('(','[','{'):
                l.append(i)
            else:
                if l and ((l[-1]=='(' and i==')') or
                         (l[-1]=='{' and i=='}') or
                          (l[-1]=='[' and i==']')):
                          l.pop()
                else:
                    return False
        return not l