class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def helper(m):
            l=0
            res=0
            for i in range(len(nums)):
                while nums[i]-nums[l]>m:
                    l+=1
                res+=i-l
            return res
        l,r=0,max(nums)
        while l<r:
            m=l+((r-l)//2)
            paris=helper(m)
            if paris>=k:
                r=m
            else:
                l=m+1
        return r