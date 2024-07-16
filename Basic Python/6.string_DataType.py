a = "dhaka"
b = 'dhaka'
c = "d"
e = 'd'

print("Type of `a`", type(a))
print("Type of `b`", type(b))

print("Type of `c`", type(c))
print("Type of `e`", type(e))


a = "My name is "
b = "Rakib"

result = a + b
print(result)

print(len(a)) 


"""
#*      Posetive Index:    0    1     2     3    4     5     6     7    8     9   
#?           String        B    a     n     g    l     a     d     e    s     h
#Todo/  Negative Index:  -10   -9    -8    -7   -6    -5    -4    -3   -2    -1
"""

##! Positive Indexing
a = "Bangladesh"
l = len(a)

print("length of `a`", l)  

for i in range(l): ## 0 1 2 3 4 5 6 7 8 9
    print(f"Index = {i},  Value = {a[i]}")

##? Enumerate Functions
for index, value in enumerate(a):
    print(f"Index = {index},  Value = {value}")

for x, y in enumerate(a):
    print(f"Index = {x},  Value = {y}")


##! Negative Indexing
a = "Bangladesh"
l = len(a)

print("length of `a`", l)

print("Posetive Index =",a[9])
print("Negative Index =",a[-1])


"""
#*      Posetive Index:    0    1     2     3    4     5     6     7    8     9   
#?           String        B    a     n     g    l     a     d     e    s     h
#Todo/  Negative Index:  -10   -9    -8    -7   -6    -5    -4    -3   -2    -1
"""
##! Slice/Range:-
a = "Bangladesh"
start = int(input("Given a start value:"))
end   = int(input("Given a ending value:"))

for i in range(start, end):
    print(f"Index = {i},  Value = {a[i]}")

l = len(a)

for i in range(l-1, 2, -1):
    print(f"Index = {i},  Value = {a[i]}")



"""
#*      Posetive Index:    0    1     2     3    4     5     6     7    8     9   
#?           String        B    a     n     g    l     a     d     e    s     h
#Todo/  Negative Index:  -10   -9    -8    -7   -6    -5    -4    -3   -2    -1
"""

a = "Bangladesh"
##*Note: [start : stop : step]
start = int(input("Given a start value:"))
end   = int(input("Given a ending value:"))
step  = int(input("Given a increment value:"))
print(a[start:end:step])


print("Reverse of `a` =", a[::-1])  ## hsedalgnaB

print(a[7::-1])     ## result = `edalgnaB`
print(a[7:-11:-1])  ## result = `edalgnaB`

print(a[7:4:-1])  ## result = `eda`

    

