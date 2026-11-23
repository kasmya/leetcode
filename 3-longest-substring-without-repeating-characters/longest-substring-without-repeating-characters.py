class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        L = 0
        max_len = 0

        for R in range(len(s)):

            if s[R] in seen and seen[s[R]] >= L:
                L = seen[s[R]] + 1

            seen[s[R]] = R

            max_len = max(max_len, R - L + 1)

        return max_len