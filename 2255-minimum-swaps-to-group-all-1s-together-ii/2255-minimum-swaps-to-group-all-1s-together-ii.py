class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        totalone=nums.count(1)
        l=0
        window_ones=max_window_ones=0
        for r in range(2*n):
            if nums[r%n]:
                window_ones+=1
            if r-l+1>totalone:
                window_ones-=nums[l%n]
                l+=1
                max_window_ones=max(max_window_ones,window_ones)
        return totalone-max_window_ones
        