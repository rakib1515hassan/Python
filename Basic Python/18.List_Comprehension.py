"""
##! Syntax:-
    [expression for item in list]
"""
##? Example 1:-
result = []
data = "i am rakib"
for letter in data:
    result.append(letter)

print(result) ## ['i', ' ', 'a', 'm', ' ', 'r', 'a', 'k', 'i', 'b']

##* IF we use list comprehension

data = "i am rakib"
result = [letter for letter in "i am rakib"]
print(result) ## ['i', ' ', 'a', 'm', ' ', 'r', 'a', 'k', 'i', 'b']



##? Example 2:-
data = [1, 2, 3, 4, 5]

result = [v*v for v in data]
print(result)  ## [1, 4, 9, 16, 25]


##? Example 3:-
data = [1, 2, 3, 4, 5]

result = [v for v in data if v % 2 == 0]
print(result)  ## [2, 4]

##? Example 4:-
newlist = [x for x in range(10)]

print(newlist)

##? Example 5
newlist = [x for x in range(10) if x < 5]

print(newlist)


##? Example 6:-
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)


##? Example 7:-
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


##? Example 8:-
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)


##? Example 9:-
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)


##? Example 10:-
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)


##? Example 11:-
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)
