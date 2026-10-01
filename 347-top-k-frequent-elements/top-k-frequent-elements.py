class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        result = []
        
        for num in nums:
            count[num]=count.get(num,0)+1
        
        for i in range(k):

            max_count = 0
            max_num = None

            for num in count:
                if count[num]>max_count:
                    max_num = num
                    max_count = count[num]

            result.append(max_num)
            del count[max_num]
            
        return result
            