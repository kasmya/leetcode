class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <= '9'):
                result += ch.lower()
            else:
                continue
        return result == result[::-1]