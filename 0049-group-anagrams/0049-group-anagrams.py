class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ang=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            ang[key].append(i)
        return list(ang.values())