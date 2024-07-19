class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,m=0,len(height)-1
        res=0
        while l<m:
            area=(m-l)*min(height[l],height[m])
            res=max(res,area)
            if height[l]<height[m]:
                l+=1
            else:
                m-=1
        return res

        