class Solution:
    def nthUglyNumber(self, n: int) -> int:
      u=[1]
      i2,i3,i5=0,0,0
      while len(u)<n:
        nxt_ugly=min(u[i2]*2,u[i3]*3,u[i5]*5)
        u.append(nxt_ugly)
        if nxt_ugly==u[i2]*2:
            i2+=1
        if nxt_ugly==u[i3]*3:
            i3+=1
        if nxt_ugly==u[i5]*5:
            i5+=1
      return u[-1]
            