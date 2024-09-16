from datetime import datetime
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convert(times):
            h,m=map(int,times.split(":"))
            return h*60+m
        
        mine=[convert(i) for i in timePoints]
        mine.sort()
        min_dif=float('inf')
        n=len(mine)
        for i in range(n):
            diff=mine[(i+1)%n]-mine[i]
            if diff<0:
                diff+=24*60
            min_dif=min(min_dif,diff)
        return min_dif

     

        