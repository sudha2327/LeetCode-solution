class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=max(len(word1),len(word2))
        mer=[]
        for i in range(length):
            if i <len(word1):
                mer.append(word1[i])
            if i <len(word2):
                mer.append(word2[i])
        return ''.join(mer)
