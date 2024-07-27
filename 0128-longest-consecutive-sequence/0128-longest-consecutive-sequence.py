class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        ans=0
        for i in nums:
            s.add(i)
        
        for i in range(len(nums)):
            if nums[i]-1 not in s:
                j=nums[i]
                while j in s:
                    j+=1
                ans=max(ans,j-nums[i])
        return ans