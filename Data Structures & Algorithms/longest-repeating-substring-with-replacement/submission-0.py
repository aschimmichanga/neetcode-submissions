class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        start, end = 0, 0
        maxCharacterFreq = 0
        characterCounts = defaultdict(int)
        windowLen = 0
        maxLen = 1
        while end < len(s) and start < len(s):
            characterCounts[s[end]] += 1
            windowLen = end - start + 1
            maxCharacterFreq = max(maxCharacterFreq, characterCounts[s[end]])
            while windowLen - maxCharacterFreq > k and start < len(s):
                characterCounts[s[start]] -= 1
                start += 1
                windowLen = end - start + 1
            maxLen = max(maxLen, windowLen)
            end += 1
        return maxLen