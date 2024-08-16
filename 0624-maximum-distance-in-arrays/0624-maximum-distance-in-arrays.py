class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m=arrays[0][0]
        n=arrays[0][-1]
        res=0
        for i in  range(1,len(arrays)):
            arr=arrays[i]
            res=max(
                res,
                max(arr[-1]-m,n-arr[0])
            )
            m=min(m,arr[0])
            n=max(n,arr[-1])
        return res