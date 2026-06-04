class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start, end = 0, 0
        startChar = s[start]
        endChar = s[end]

        uniqueChars = set()
        maxLen = 1

        while end < len(s) and start < len(s):
            if s[end] in uniqueChars:
                while start < len(s) and s[start] != s[end]:
                    if s[start] in uniqueChars:
                        uniqueChars.remove(s[start])
                    start += 1
                start += 1     
            uniqueChars.add(s[end])
            end += 1
            maxLen = max(maxLen, len(uniqueChars))
        return maxLen