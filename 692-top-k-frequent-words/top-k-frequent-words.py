class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}
        for i in words:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        result = sorted(count, key=lambda x: (-count[x], x))
        return result[:k]