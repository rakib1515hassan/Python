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

##NOTE:- Return type Numerical Value

## 64   32   16   8   4   2   1

a = 10  ##  1010                                                       
b = 12  ##  1100

print("a & b result=", (a & b))   ## Bitwise And   (1010  *  1100 ) = 1000  = 8
print("a | b result=", (a | b))   ## Bitwise Or    (1010  |  1100 ) = 1110  = 14
print("~a result=", (~a))         ## not   (~1010 ) = 11110101 = -11  (1's complement , 2's complement)


print("a ^ b result=", (a ^ b))     ## Bitwise XOR   (1010  ^  1100 ) = 0110  = 6
print("b >> 2 result=", (b >> 2))   ## Bitwise right shift  (00001010  >>  00001100 ) = 00000011  = 3
print("b << 2 result=", (b << 2))   ## Bitwise left shift  (00001010  <<  00001100 ) =  00110000  = 48


##! Assignment Operator  (  =   +=   -=    *=     /=    %=    //=     **= ) 

a = 10
b = 20 

print("Assigns value `=` ",  a)

## Add Equals operator
a += 2   ## a = (a + 2)  result = 10 + 2  = 12
a += b   ## a = a + b    result = 10 + 20 = 30
print("Add Equals =",a)

## Subtract Equals operator
a -= 2   ## a = (a - 2)  result = 10 - 2  = 8
a -= b   ## a = a - b    result = 10 - 20 = -10
print("Add Equals =",a)


## Multiply Equals operator
a *= 2   ## a = (a * 2)  result = 10 * 2  = 20
a *= b   ## a = a * b    result = 10 * 20 = 200
print("Multiply Equals =",a)



## Division Equals operator
a /= 2   ## a = (a / 2)  result = 10 / 2  = 5
a /= b   ## a = a / b    result = 10 / 20 = 0.5
print("Division Equals =",a)



## Modulus Equals operator
a %= 2   ## a = (a % 2)  result = 10 % 2  = 0
a %= b   ## a = a % b    result = 10 % 20 = 10
print("Modulus Equals =",a)


## Division Floor Equals operator
a //= 2   ## a = (a // 2)  result = 10 // 2  = 5
a //= b   ## a = a // b    result = 10 // 20 = 0
print("Division Equals =",a)


## Expone Equals operator
a **= 2   ## a = (a ** 2)  result = 10 ** 2  = 5
a **= b   ## a = a ** b    result = 10 ** 20 = 100000000000000000000
print("Expone Equals =",a)



##! Tennary Operators  

a = 20
b = 10

if a > b:
    print("a is larger than b")
else:
    print("a is smaller than b")


result =  print("a is larger than b")  if a > b else print("a is smaller than b")



