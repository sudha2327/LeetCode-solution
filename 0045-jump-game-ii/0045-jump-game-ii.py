class Solution:
    def jump(self, nums: List[int]) -> int:
        goal=len(nums)-1
        c=0
        l=r=0
        while r<len(nums)-1:
            far=0
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            c+=1
        return c
    

        