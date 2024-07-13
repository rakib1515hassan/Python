"""##!Syntax Of Forloop

    for variable in sequence:
        -- Extention --

"""


##! Example 1:-
for i in range(5):   ## Start 0,   End  i<5 = 4,    Increment 1
    print(i)


for i in range(2, 5):   ## Start 2,   End  i<5 = 4,    Increment 1
    print(i)


for i in range(2, 20, 3):   ## Start 2,   End  i<20 = 19,    Increment 3
    print(i)     ## 2, 5, 8, 11, 14, 17



##! Example 2:-
## index    0         1        2            3             4             5
fruit = ["apple", "orange", "banana", "black bary", "watermilone", "pineapple"]
## index   -6        -5        -4          -3            -2             -1



for value in fruit:
    print(value)   


country = "Bangladesh"

for v in country:
    print(v)



country = "Bangladesh"

count = 0

for v in country:
    if v == 'a':
        count+=1    ## count = count + 1

print("Total a = ", count)



##! Example 3:- `break`, `continue` and `pass`
fruits = ["apple", "banana", "cherry", "blackberry", "watermelon", "pineapple"]

##? `break`   
for x in fruits:
#   print("Before If condition `x`=",x)     ## apple, banana, cherry
  if x == "cherry":
    break
  
  print("After If condition `x`=",x)        ## apple, banana



##? `continue`      
for x in fruits:
#   print("Before If condition `x`=",x)     ## apple, banana, cherry, blackberry, watermelon, pineapple
  if x == "cherry":
    continue
  
  print("After If condition `x`=",x)        ## apple, banana, blackberry, watermelon, pineapple



##? `pass`  
## যদি for loop চালানোর সময় কোন Block Create হয়, তবে তা হতে বের হবার জন্যে `pass` use করবো।

for x in fruits:
#   print("Before If condition `x`=",x)     ## apple, banana, cherry, blackberry, watermelon, pineapple
  if x == "cherry":
    pass
  
  print("After If condition `x`=",x)        ## apple, banana, cherry, blackberry, watermelon, pineapple



##! While Loop
"""
        while condition:
            -- code --
            
"""


i = 1

while i<=5:
   print("value = ", i)
   i+=1




i = 1
while i < 6:
    print(i)       ## 1, 2, 3
    if i == 3:
        break
    i += 1




i = 0 

    # i = 0, 1, 2, 3, 4, 5
while i < 6:
    i += 1       # 1, 2, 3, 4, 5, 6
    if i == 3:
        continue
    print(i)      ## 1, 2, 4, 5, 6




i = 1
    ## i = 1, 2, 3, 4, 5
while i < 6:

    print(i)    ##* Result = 1, 2, 3, 4, 5

    i += 1      ## i = 2, 3, 4, 5, 6

else:
    print("i is no longer less than 6")

# Result = 1, 2, 3, 4, 5, i is no longer less than 6



             ##     99
for i in range(10, 100, 20):  ## i = 101 30, 50, 70

    for j in range(1, 5):        ## j = 1, 2, 3, 4

        print(f"i = {i}, j = {j}")  


"""
Result =
i = 10, j = 1
i = 10, j = 2
i = 10, j = 3
i = 10, j = 4
i = 30, j = 1
i = 30, j = 2
i = 30, j = 3
i = 30, j = 4
i = 50, j = 1
i = 50, j = 2
i = 50, j = 3
i = 50, j = 4
i = 70, j = 1
i = 70, j = 2
i = 70, j = 3
i = 70, j = 4
i = 90, j = 1
i = 90, j = 2
i = 90, j = 3
i = 90, j = 4

"""

