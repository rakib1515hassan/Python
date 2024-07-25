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

print(result) ## Result = `120`



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



##? Using Recursive Functions
def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n - 1)
    
user_inpute = int(input("Given a number :")) ## If given :5
result = Factorial(user_inpute)
print(result)  ## Result = `120`

""" If n = 5
    Return :  n   * Factorial( n - 1 )
    Step 1 :  5   * Factorial( 4 )  
    Step 2 :  4   * Factorial( 3 )  
    Step 3 :  3   * Factorial( 2 )  
    Step 4 :  2   * Factorial( 1 )  => return 5 যেহেতু Factorial( 1 ) = 1 তাই 2 * 1 = 2


    Back   :
    Step 3 :  3 * 2    => return 6
    Step 2 :  4 * 6    => return 24
    Step 1 :  5 * 24   => return 120
"""


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


