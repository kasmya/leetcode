# Two pointers = use two index variables to work with two positions in an array/string.

''' 
1. Opposite ends — like Palindrome:

L →          ← R

2. Same direction — like Move Zeroes:

L → R → → →

For Move Zeroes, both start at 0:


The key idea

With two pointers, we don't randomly move them.

We move them based on a condition.

Here:

sum too small → move left right
sum too large → move right left
sum correct → found it

This is the two-pointer pattern I want you to understand before returning to Move Zeroes.
'''

# Don't ask "Why do I need two pointers?" first. Ask "Do I need to track two different positions?"
