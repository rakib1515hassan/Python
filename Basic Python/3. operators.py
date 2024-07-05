""" ##NOTE:- Python Operators

    1. Arithmetic Operators ( +  -  *  /   //   %  ** )
    2. Assignment Operators
    3. Comparison Operators
    4. Logical Operators
    5. Identity Operators
    6. Membership Operators
    7. Bitwise Operators  
    8. Tennary Operators  
"""

##! Arithmetic Operators ( +  -  *  /   //   %  ** )   

a = 10
b = 3

result = a + b
print("result =", result)   


result = a - b
print("result =", result)   



result = a * b
print("result =", result)  


result = (a / b)
print(f"result = {result:.2f}")


result = a // b
print("result =", result)


result = a % b
print("result =", result)  


result = a ** b
print("result =", result)   #10*10*10 = 1000



##! Comparison Operators ( ==    !=    >    <     >=    <=  )  

##NOTE:-  Always returns True/False 

a = 10
b = 3


print("a == b result =", a == b)  ## False

print("a != b result =", a != b)  ## True

print("a > b result =", a  > b)   ## True

print("a < b result =", a < b)    ## False

print("a >= b result =", a >= b)  ## True

print("a <= b result =", a <= b)  ## False


##! Logical Operators ( and    or    not )   

##NOTE:-  Always returns True/False 

a = 10
b = 5

print((a == 10) and (b == 5))   ## True

print((a == 10) or (b == 7))   ## True

print(not a == 12  )           ## True
print(not b == 5   )           ## False



##! Identity Operators ( is )  

##NOTE:-  Always returns True/False 


x = ["apple", "banana"]


y = ["apple", "banana"]

z = x

print(x)

print(z)

print(x is z) ## True
    
print(y is z)  ## False

a = 10
b = 5
c = a
d = c

print(d is a)


a = 10
b = 5
c = a
d = c

e = d

#print(d is a)

#print(e is a)

print(b is d)


##! Membership Operators ( in    not in )  

##NOTE:-  Always returns True/False 


a = "bangladesh"

print('lad' in a)  ## True

print('ban' not in a)  ## False



##! Bitwise Operators  (  &    |    ~    ^    >>   <<  )  