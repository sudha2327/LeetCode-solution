class Solution:
    def isHappy(self, n: int) -> bool:

        sum=n
        i=n
        while sum>9:
            sum=0
            while i>0:
                d=i%10
                sum+=d*d
                i=i//10
            i=sum
        if sum==1 or sum==7:
            return True
        else:
            return False

        