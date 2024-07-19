class Solution:
    def candy(self, ratings: List[int]) -> int:
        c=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i-1]<ratings[i]:
                c[i]=c[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                c[i]=max(c[i],c[i+1]+1)
        return sum(c)
        