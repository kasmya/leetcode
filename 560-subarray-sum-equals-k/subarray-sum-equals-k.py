class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen={0:1}
        prefix=0
        count=0

        for num in nums:
            prefix +=num

            complement=prefix-k
            if complement in seen:
                count+=seen[complement]
            
            seen[prefix]=seen.get(prefix, 0)+1

        return count        
        