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
