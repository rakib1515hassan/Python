"""
##! Lambda Function (Anonymous Function)
    i) A function without name.
    ii) Not powerful as a named function.
    iii) It can work with single expressions/single line of code.

##! Syntax:

    lambda argument : expression

#?  Example Normal Function:    |   Example of Lambda Function:-
                                |
        def add(a, b):          |   result = lambda a, b : a + b
            return a + b        |
                                |   print(result(5, 6))
        result = add(5, 6)      |
        print(result)           |
"""

##? Example 1:
result = lambda a,b : a+b
print("Result = ",result(5, 6)) ## Result =  11



##? Example 2:-
#* Question:=> যদি এমন একটি Function বানাতে চাই, যার একটি Value কে Constant রেখে অন্য(value)
#*             পরিবর্ত করে গুন করতে চাই একাধিক বার।

def multiply(a):
    return lambda b : a * b

"""
    => এই function টি কিন্তু 2 টি argument চাচ্ছে একটি multiply() এর `a` জন্যে,
    অন্যটি lambda এর ভেতর `b` এর জন্যে।
"""


## এখানে `a` এর value কে Constant করা হয়েছে।
obj = multiply(5)
"""
NOTE:- If `multiply(5, 6)`, then TypeError: multiply() takes 1 positional argument but 2 were given
তার মানে সে একটির বেশি parameter receive করে না।
"""


"""
    => এখানে `b` এর value কে argument হিসেবে pass করা হেয়েছে, যা মূলত 
    lambda function parameter হিসেবে accept করতেছে।
"""
result1 = obj(3)
result2 = obj(4)
result3 = obj(5)
result4 = obj(6)

print("Result 1 = ",result1)  ## Result 1 =  15  
print("Result 2 = ",result2)  ## Result 2 =  20
print("Result 3 = ",result3)  ## Result 3 =  25
print("Result 4 = ",result4)  ## Result 4 =  30 


result = lambda x, y=10 : x * y 

print("result1 =", result(5))
print("result2 =", result(8))
print("result3 =", result(9))
print("result4 =", result(4))

##? Example 3:-
#* Question => a^2 + 2ab + b^2

result = lambda a,b : ((a*a) + 2*a*b + (b*b))

print("Result 1 = ",result(2,3)) ## Result 1 = 25
print("Result 2 = ",result(5,6)) ## Result 2 = 121

##NOTE:- If you can also pass a,b from,
result = (
        lambda a,b : ((a*a) + 2*a*b + (b*b))
    )(2,3)
print(result) ## 25