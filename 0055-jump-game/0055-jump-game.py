class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n=len(nums)
        goal=len(nums)-1

        for i in range(n-1,-1,-1):
            maxg=nums[i]
            if maxg+i>=goal:
                goal=i
        if goal==0:
            return True
        else:
            return False
       
        
       

            
         
        
            
        # return False
           
       
        



            
            
        