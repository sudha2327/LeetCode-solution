class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x,y=0,0
        dirt=[[0,1],[1,0],[0,-1],[-1,0]] 
        d=0
        ans=0
        obstacles={tuple(o) for o in obstacles}
        for i in commands:
            if i==-1:
                d=(d+1)%4
            elif i==-2:
                d=(d-1)%4
            else:
                dx,dy=dirt[d]
                for _ in range(i):
                    if (x+dx,y+dy) in obstacles:
                        break
                    x,y=x+dx,y+dy

            ans=max(ans,x**2+y**2)
        return ans


            
