""" ##NOTE:- Python Operators

    1. Arithmetic Operators ( +  -  *  /   //   %  ** )
    2. Assignment Operators ( =  +=  -=  *=  /=  %=  //=  **=)
    3. Comparison Operators ( ==  !=  >  <  >=  <=)
    4. Logical Operators  ( and  or  not)
    5. Identity Operators ( is )
    6. Membership Operators ( in  not in )
    7. Bitwise Operators ( &  |   ~   ^  >>  << )
    8. Tennary Operators 
"""

##! 1) Arithmetic Operators ( +  -  *  /   //   %  ** ) ------------------------------------   

a = 10
b = 3

##? Addition Operator ( + )
result = a + b
print("Result =", result)     ## Result = 13


##? Subtraction Operator ( - )
result = a - b
print("Result =", result)     ## Result = 7


##? Multiplication Operator ( * )
result = a * b
print("Result =", result)       ## Result = 30


##? Division-Float Operator ( / )
result = (a / b)
print(f"Result =", result)  ## Result = 3.3333333333333335
print(f"Result = {result:.2f}")  ## Result = 3.33


##? Division-Floor Operator ( // )
result = a // b
print("Result =", result)   ## Result = 3  #* ভগ ফল


##? Modulus Operator ( % )
result = a % b
print("Result =", result)   ## Result = 1  #* ভগ শেষ


##? Power Operator ( ** )
result = a ** b
print("Result =", result)   ## Result = 10*10*10 = 1000 #* Power


##! 2) Assignment Operator  (  =   +=   -=    *=     /=    %=    //=     **= ) -------------------------

a = 10
b = 20 

print("Assigns value `=` ",  a)

##? Add Equals operator ( += )
a += 2   ## a = (a + 2)  result = 10 + 2  = 12
a += b   ## a = a + b    result = 10 + 20 = 30
print("Add Equals =",a)

##? Subtract Equals operator ( -= )
a -= 2   ## a = (a - 2)  result = 10 - 2  = 8
a -= b   ## a = a - b    result = 10 - 20 = -10
print("Add Equals =",a)


##? Multiply Equals operator ( *= )
a *= 2   ## a = (a * 2)  result = 10 * 2  = 20
a *= b   ## a = a * b    result = 10 * 20 = 200
print("Multiply Equals =",a)



##? Division Equals operator ( /= )
a /= 2   ## a = (a / 2)  result = 10 / 2  = 5
a /= b   ## a = a / b    result = 10 / 20 = 0.5
print("Division Equals =",a)



##? Modulus Equals operator ( %= )
a %= 2   ## a = (a % 2)  result = 10 % 2  = 0
a %= b   ## a = a % b    result = 10 % 20 = 10
print("Modulus Equals =",a)


##? Division Floor Equals operator ( //= )
a //= 2   ## a = (a // 2)  result = 10 // 2  = 5
a //= b   ## a = a // b    result = 10 // 20 = 0
print("Division Equals =",a)


##? Expone Equals operator ( **= )
a **= 2   ## a = (a ** 2)  result = 10 ** 2  = 5
a **= b   ## a = a ** b    result = 10 ** 20 = 100000000000000000000
print("Expone Equals =",a)



##! 3) Comparison Operators ( ==    !=    >    <     >=    <=  )  ------------------------------------

##NOTE:-  Always returns True/False 

a = 10
b = 3

##? Equal Operator ( == )
print("a == b result =", a == b)  ## False

##? Not Equal Operator ( != )
print("a != b result =", a != b)  ## True

##? Greater Than Operator ( > )
print("a > b result =", a  > b)   ## True

##? Less Than Operator ( < )
print("a < b result =", a < b)    ## False

##? Greater than or equal to  Operator ( >= )
print("a >= b result =", a >= b)  ## True

##? Less than or equal to Operator ( <= )
print("a <= b result =", a <= b)  ## False 


##! 4) Logical Operators ( and    or    not ) --------------------------------------------------------

##NOTE:-  Always returns True/False 

a = 10
b = 5

##? And ( and )
print((a == 10) and (b == 5))   ## True

##? Or ( or )
print((a == 10) or (b == 7))   ## True

##? Not ( not )
print(not a == 12  )           ## True
print(not b == 5   )           ## False



##! 5) Identity Operators ( is )   ------------------------------------------------------------------
"""
এই Operator এর সাহায্যে কোন Data এর loction বুঝাতে পারি। মূলত same data যদি ভিন্ন ভিন্ন variable 
এর মধ্যে save থাকে, কিন্তু আসলে তারা Memori একটি same location এর মধ্যে store করা থাকে। এই বিষয় 
গুলো বুঝার জন্যে আমরা এই Operator টি ব্যাবহার করে থাকি।

##* It's most uses to compare the objects. 
##NOTE:-  Always returns True/False 
"""


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


##! 6) Membership Operators ( in    not in )  ----------------------------------------------------------

##NOTE:-  Always returns True/False 


a = "bangladesh"

print('lad' in a)  ## True

print('ban' not in a)  ## False



##! 7) Bitwise Operators  (  &    |    ~    ^    >>   <<  ) --------------------------------------------

"""
এই Operators গুলো Binary Number এর সাহায্যে কাজ করে।

##NOTE:- Return type Numerical Value

## 64   32   16   8   4   2   1
"""

a = 10  ##  1010                                                       
b = 12  ##  1100

##? Bitwise AND Operators ( & )
print("a & b result=", (a & b))   ## Bitwise And   (1010  *  1100 ) = 1000  = 8

##? Bitwise OR Operators ( | )
print("a | b result=", (a | b))   ## Bitwise Or    (1010  |  1100 ) = 1110  = 14

##? Bitwise NOT Operators ( ~ )
print("~a result=", (~a))         ## not   (~1010 ) = 11110101 = -11  (1's complement , 2's complement)

##? Bitwise XOR Operators ( ^ )
print("a ^ b result=", (a ^ b))     ## Bitwise XOR   (1010  ^  1100 ) = 0110  = 6



##? Bitwise Right Shift Operators ( >> )
print("b >> 2 result=", (b >> 2))   ## Bitwise right shift  (00001010  >>  00001100 ) = 00000011  = 3

"""NOTE:- Descrieved How it work,
b = 12 = 1100  
                            ##* ----> Right Shift 2
##                     | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |

##TODO:    | 0 |  -->  | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |   -->  | 0 |     ## 1 Right Shift Complete
#            |
##!  Auto Generated `0`
#            |
##TODO:    | 0 |  -->  | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |   -->  | 0 |     ## Another 1 Right Shift Complete

##* After 2 Right Shift complete got, 00000011 = 3
"""



##? Bitwise Left Shift Operators ( << )
print("b << 2 result=", (b << 2))   ## Bitwise left shift  (00001010  <<  00001100 ) =  00110000  = 48

"""NOTE:- Descrieved How it work,
b = 12 = 1100  
                            ##* <----- Left Shift 2
##                     | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |

##TODO:    | 0 |  <--  | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 |   <--  | 0 |      ## 1 Left Shift Complete
#                                                                 |
##!                                                      Auto Generated `0`
#                                                                 |
##TODO:    | 0 |  <--  | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |   <--  | 0 |      ## Another 1 Left Shift Complete

##* After 2 Left Shift complete got, 00110000 = 48
"""

##! 8) Tennary Operators  -----------------------------------------------------------------------------

a = 20
b = 10

if a > b:
    print("a is larger than b")
else:
    print("a is smaller than b")


result =  print("a is larger than b")  if a > b else print("a is smaller than b")



