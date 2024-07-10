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