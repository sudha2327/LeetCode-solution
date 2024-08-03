class Solution:
    def simplifyPath(self, path: str) -> str:

        l=[]
        for i in path.split('/'):
            if i=='' and not i or i=='.':
                continue
            if i=='..':
                if l:
                    l.pop()
            else:
                l.append(i)
        
        return '/'+'/'.join(l)




        