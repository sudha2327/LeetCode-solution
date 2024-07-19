class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[0]*len(nums)
        prod[0]=1

        for i in range(1,len(nums)):
            prod[i]=nums[i-1]*prod[i-1]
        suf=1
        for i in range(len(nums)-1,-1,-1):
            prod[i]=prod[i]*suf
            suf=suf*nums[i]
        
        return prod
    



       
            
        
            
                


                
