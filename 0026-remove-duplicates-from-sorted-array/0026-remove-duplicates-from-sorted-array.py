class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # expectedItem = nums[:]
        # myarr = []
        # for i in range(len(expectedItem)):
        #     if expectedItem[i] not in myarr :
        #         myarr.append(expectedItem[i])
        #     else:
        #         nums.remove(expectedItem[i])
        
        # return len(nums);
        l=set(nums)
        nums.clear()
        for i in l:
            nums.append(i)
        nums.sort()
        return len(nums)

       
     
        