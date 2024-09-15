from math import inf

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        positions = [inf] * 32       
        positions[0] = -1
        vowels = 'aeiou'
        state = max_length = 0

        for index, char in enumerate(s):
            for j, vowel in enumerate(vowels):
                if char == vowel:
                    state ^= 1 << j
            max_length = max(max_length, index - positions[state])
            positions[state] = min(positions[state], index)
        return max_length