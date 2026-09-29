class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        seen = []
        duplicate = 0
        for i in nums:
            if i in seen:
                duplicate = i 
            else:
                seen.append(i)
        for i in range(1, len(nums)+1):
            if i not in seen:
                missing = i
        return [duplicate, missing]