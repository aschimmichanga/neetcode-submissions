class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        start = 0
        end = len(s) - 1
        s = s.lower()
        while start < end and start < len(s) and end > -1:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if start < end and not s[start] == s[end]:
                return False
            start += 1
            end -= 1
        return True