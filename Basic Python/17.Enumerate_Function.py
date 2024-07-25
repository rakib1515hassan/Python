"""
    => Enumerate Function মূলত List, Tuple and Set এর index number get করার জন্যে ব্যবহার করা হয়।
"""

##? Example 1:-
## If we get the middle name then,

full_name = ["Md", "Rakib", "Hassan"]

index = 0

for v in full_name:
    if index%2 != 0:
        print("Middle Name: ", v)  ## Middle Name:  Rakib

    index += 1

##* কিন্তু এই কাজটি আমরা এইভাবে সহজে কোরতে পারতাম,

for k, v in enumerate(full_name):
    if k%2 != 0:
        print("Middle Name: ", v)  ## Middle Name:  Rakib



##? Example 2:-
full_name = ["Md", "Rakib", "Hassan"]

name = "Jarray"

result1 = enumerate(full_name)
result2 = enumerate(name)

print("result1 =", list(result1)) ## result1 = [(0, 'Md'), (1, 'Rakib'), (2, 'Hassan')]
print("result2 =", list(result2)) ## result2 = [(0, 'J'), (1, 'a'), (2, 'r'), (3, 'r'), (4, 'a'), (5, 'y')]


result3 = list(enumerate(full_name, 2))
print(result3) ## [(2, 'Md'), (3, 'Rakib'), (4, 'Hassan')]


result4 = list(enumerate(full_name, 3))
print(result4) ## [(3, 'Md'), (4, 'Rakib'), (5, 'Hassan')]


result5 = tuple(enumerate(full_name, 3))
print(result5) ## ((3, 'Md'), (4, 'Rakib'), (5, 'Hassan'))



##? Example 3:-
##* Index:  0          1          2         3        4        5       6        7
names = ["Rakib", "Mohammded", "Jarry", "Hassan", "Rubel", "Sakib", "Mina", "Raju"]

result = list(enumerate(names, 1, 2))
print(result) 
##! ERROR: TypeError: enumerate() takes at most 2 arguments (3 given)
## So, it not taken 3 arguments