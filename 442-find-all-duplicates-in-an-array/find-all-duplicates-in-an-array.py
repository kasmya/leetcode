class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        count = {}
        for ch in nums:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1
        dup = []
        for ch,c in count.items():
            if c>1:
                dup.append(ch)
        return dup