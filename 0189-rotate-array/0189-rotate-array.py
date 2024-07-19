class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        # """
        # d=1
        # l=len(nums)
        # while(d<=k):
        #     last=nums[0]
        #     for i in range(l-1):
        #         nums[i]=nums[i+1]
        #     nums[l-1]=last
        # d+=1
        # return nums
        k=k%len(nums)
        if k>0:
            nums[:]=nums[-k:]+nums[:-k]
        return nums
       


        