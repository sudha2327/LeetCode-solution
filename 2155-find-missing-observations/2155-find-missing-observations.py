class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        a_sum=sum(rolls)
        t_sum=(m+n)*mean
        miss=t_sum-a_sum

        #checking valid mean 
        if miss<n or miss > n*6:
            return []
        ans = [miss // n] * n
        for i in range(miss % n):
            ans[i] += 1

        return ans

