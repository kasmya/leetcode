class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #count letters in magazine (+)
        count = {}
        for char in magazine:
            count[char]=count.get(char,0)+1

        #use letters for ransomnote (-)
        for char in ransomNote:
            if char not in count:
                return False
            count[char] -= 1
            
            #if used more of letters than we had
            if count[char]<0:
                return False

        return True
