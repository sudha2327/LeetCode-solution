class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #two pointer
        # i=0
        # j=0
        # m=len(nums)
        # while(i<m):
        #     if nums[i]!=val:
        #         nums[j]=nums[i]
        #         j+=1
        #     i+=1
        # return j
        while val in nums:
            nums.remove(val)
        return len(nums)
            