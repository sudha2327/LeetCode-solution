class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        mod=10**9+7
        for i in range(n):
            l.append(nums[i])
            curent=nums[i]
            for j in range(i+1,n):
                curent=curent+nums[j]
                l.append(curent)
        left-=1
        l=sorted(l)
        s=0
        while left<right:
            s+=l[left]
            left+=1
        return s%mod

        