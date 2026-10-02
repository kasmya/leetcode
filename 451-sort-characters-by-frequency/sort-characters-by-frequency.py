class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for char in s:
            count[char] = count.get(char, 0)+1 
        sorted_chars = sorted(count,key=count.get, reverse=True)
        result = ""
        for char in sorted_chars:
            result += char * count[char]
        return result