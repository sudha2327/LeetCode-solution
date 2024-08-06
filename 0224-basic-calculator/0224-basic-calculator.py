class Solution:
    def calculate(self, s: str) -> int:
        l=[]
        sign=1
        cur=0
        output=0
        for i in s:
            if i.isdigit():
                cur=cur*10+int(i)
            elif i in "+,-":
                output+=(cur*sign)
                cur=0
                if i=='-':
                    sign=-1
                else:
                    sign=1
            elif i=="(":
                l.append(output)
                l.append(sign)
                output=0
                sign=1
            elif i==")":
                output+=(cur*sign)
                output*=l.pop()
                output+=l.pop()
                cur=0
        return output+(cur*sign)