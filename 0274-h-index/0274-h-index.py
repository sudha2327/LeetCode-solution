class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count=0
        for i in range(0,len(citations)):
            if citations[i]>=i+1:
                count+=1
        return count

        
     
       




        
        