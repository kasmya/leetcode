class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = {}
        for i in nums:
            count[i]=count.get(i,0)+1

        for num in count:
            if count[num] > len(nums) / 2:
                return num