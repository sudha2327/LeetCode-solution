class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target)!=len(arr):
            return False
        
        arr=sorted(arr)
        target=sorted(target)
        flg=False
        for i in range(len(arr)):
            if target[i]==arr[i]:
                flg=True
            else:
                flg=False
                break
        
        return flg

        