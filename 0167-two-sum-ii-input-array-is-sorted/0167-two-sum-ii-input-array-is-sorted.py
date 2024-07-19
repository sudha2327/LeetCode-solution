class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,m=0,len(numbers)-1
        while l<m:
            cur=numbers[l]+numbers[m]
            if cur>target:
                m-=1
            elif cur<target:
                l+=1
            else:
                return [l+1,m+1]
        return []
            
        