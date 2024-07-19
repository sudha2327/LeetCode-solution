class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0 #counts
        for k in range(0,len(nums)):
            if i==0 or i==1 or nums[k]!=nums[abs(i-2)]:
                nums[i]=nums[k]
                i+=1 
        return i

            