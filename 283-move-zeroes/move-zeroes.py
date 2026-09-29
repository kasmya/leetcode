class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        result = []
        count = 0
        for i in nums:
            if i == 0:
                count +=1
            else:
                result.append(i)

        for i in range(count):
            result.append(0)
        for i in range(len(nums)):
            nums[i]=result[i]

        