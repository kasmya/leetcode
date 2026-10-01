#to count evrything (frequency of each char)
count = {}

for char in s:
    count[char] = count.get(char, 0) + 1

'''
l → 1
e → 3
t → 1
c → 1
o → 1
d → 1
'''

for i, char in enumerate(s):

'''
i=0, char='l'
i=1, char='e'
i=2, char='e'
'''

'''
ENUMERATE
for i, x in enumerate(arr):
→ gives me INDEX + VALUE
→ i = position, x = element


DICTIONARY COUNTING
count[x] = count.get(x, 0) + 1
→ get OLD count of x, add 1, save it back
→ means: "I saw x one more time."
'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s :
            count[char] = count.get(char, 0)+1
        for i,char in enumerate(s):
            if count[char]==1:
                return i
        return -1

#revise 
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

'''
Set → “Have I seen this before?” / membership / duplicates.
Dictionary → “How many times did I see this?” / frequency.
'''
