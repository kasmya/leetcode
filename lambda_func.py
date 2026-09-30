def square(x):
    return x * x
print(square(5)) #i/p 5
#o/p 25

square = lambda x: x * x 
#short function with same meaning 

def add(a, b):
    return a + b

add = lambda a, b: a + b
print(add(2,3))

# lambda inputs: output

#lambda functions are mostly used for sorting 
#ex: Sort words by length
words = ["apple","cat","banana"]
sorted(words, key=lambda x: len(x))
#ex: tuple sorting
students = [
    ("Ram",90),
    ("Shyam",70),
    ("Mohan",85)
]
sorted(students, key=lambda x: x[1])
