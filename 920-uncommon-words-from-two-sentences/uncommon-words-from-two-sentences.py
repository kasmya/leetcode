class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        a=s1.split()
        b=s2.split()
        words = a+b
        uncommon = []
        for i in words:
            if words.count(i)==1:
                uncommon.append(i)
        return uncommon