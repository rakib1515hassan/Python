"""
    => একটি Function যদি নিজে নিজেকে` Call করে তবে একে Recursion বলে।
"""
##! Example 1: Calculate Factorial Value =========================================
"""
    => 5! = 5 * 4 * 3 * 2 * 1 = 120
"""
##? Without Recursive Functions
n = int(input("Given a number :")) ## If given :5

result = 1

for i in range(n):
    result += result * (n-1)
    n -= 1

"""
    step 0: r = 1   * 5 = 5   , r = 5 ,  n = 4
    step 1: r = 5   * 4 = 20  , r = 20,  n = 3
    step 2: r = 20  * 3 = 60  , r = 60,  n = 2
    step 3: r = 60  * 2 = 120 , r = 120, n = 1
    step 4: r = 120 * 1 = 120 , r = 120, n = 0
"""

print(result) ## Result = `120`

##? Without Recursive
n = 5
r = 1
            
for i in range(1, n+1, 1):              
    r = r * i           

"""
    step 1: r = 1   * 1 = 1   , r = 1 
    step 2: r = 1   * 2 = 2   , r = 2
    step 3: r = 2   * 3 = 6   , r = 6 
    step 4: r = 6   * 4 = 24  , r = 24
    step 5: r = 24  * 5 = 120 , r = 120
"""

"""
    5! = 1 * 2 * 3 * 4 * 5 = 120
    5! = 5 * 4 * 3 * 2 * 1 = 120
"""

##? Without Recursive
n = 5
r = 1
            
for i in range(n, 0, -1):              
    r = r * i

print(r)

"""
    step 0: r = 1   * 5 = 5   , r = 5 ,  n = 4
    step 1  r = 5   * 4 = 20  , r = 20,  n = 3
    step 2: r = 20  * 3 = 60  , r = 60,  n = 2
    step 3: r = 60  * 2 = 120 , r = 120, n = 1
    step 4: r = 120 * 1 = 120 , r = 120, n = 0
"""

##? Without Recursive Functions 
def Factorial(n):
    if n == 1:
        return 1
    else:
        result = 1
        for i in range(n):
            result += result * (n-1)
            n-=1

        return result
    
user_inpute = int(input("Given a number :")) ## If given :5
result = Factorial(user_inpute)
print(result) ## Result = `120`

##? With Function
def Factorial(x):
    r = 1
    for i in range(x, 0, -1):              
        r = r * i

    return r


n = int(input("Enter a integer number :"))

result = Factorial(n)

print("Result = ", result)



##? Using Recursive Functions
def Factorial(x):
    if (x == 1) or (x == 0):
        return 1
    else:
        return x * Factorial(x - 1)

""" If x = 5
    Return : x * Factorial( x - 1 )
    Step 1 : 5 * Factorial( 4 )     returns : pending
    Step 2 : 4 * Factorial( 3 )     returns : pending
    Step 3 : 3 * Factorial( 2 )     returns : pending 
    Step 4 : 2 * Factorial( 1 )  => return 5 যেহেতু Factorial( 1 ) = 1 তাই 2 * 1 = 2

    
    Back   :
    Step 3 : 3 * 2    => Factorial( 2 ) = 2  ,  return 6
    Step 2 : 4 * 6    => Factorial( 3 ) = 6  ,  return 24
    Step 1 : 5 * 24   => Factorial( 4 ) = 24 , return 120
"""

##--------------------------------------------------
n = int(input("Enter a integer number :"))  ## 5
result = Factorial(n)
print("Result = ", result)


##! Example 2: Power of X ======================================================

"""
    => Write a program with recursive functions to compute the value of X^2. Where n is a
       positive iteger and x has a real value.
       
       Example 1: 5^3 = 5 * 5 * 5 = 125
       Example 2: 5^4 = 5 * 5 * 5 * 5 = 625
       Example 3: 2^6 = 2 * 2 * 2 * 2 * 2 * 2 = 64
"""

##? Without Recursive Functions
base = int(input("Enter base number :"))

powRaised = int(input("Enter power number(positive integer) :"))

result = 1

for num in range(powRaised):
    result *= base

print(result)


##? Without Recursive Functions 
def Power(base, powRaised):
    result = 1

    for i in range(powRaised):
        result *= base

    return result


base = int(input("Enter base number :"))
powRaised = int(input("Enter power number(positive integer) :"))

result = Power(base, powRaised)
print(result)


##? Using Recursive Functions
def Power(base, powerRaised):

    if powerRaised != 0:
        return base * Power(base, powerRaised-1)
    else:
        return 1

base = int(input("Enter base number :"))  ## If Base = 5
powRaised = int(input("Enter power number(positive integer) :"))  ## If PowerRaised = 4

result = Power(base, powRaised)
print(result)  ## Result = `625`

""" If base = 5, power = 4
    Return : base * Power(base, powRaised-1) 
    Step 1 :  5   * Power(5,        4      )  
    Step 2 :  5   * Power(5,        3      )  
    Step 3 :  5   * Power(5,        2      )  
    Step 4 :  5   * Power(5,        1      )  
    Step 5 :  5   * Power(5,        0      )  => return 1, যেহেতু powerRaised=0, return 1 হয়।

    Back   :
    Step 4 :  5 * 1    => return 5
    Step 3 :  5 * 5    => return 25
    Step 2 :  5 * 25   => return 125
    Step 1 :  5 * 125  => return 625
"""


