"""##! Decorator:-
=> A decorator is a design pattern in Python that allows a user to add new functionality to
   an existing object without modifying it's structure.


"""
##? Example 1:-
def StringUpperCase(function): ## এখানে `function` parameter টি মূলত একটি Function কে Receive করে।

    def MakeUpper():
        string = function()
        return string.upper()
    
    return MakeUpper()  ##NOTE:-এখানে যদি আমরা `()` দেই তবে print 
                        ##      করার সময় Function এর শেষে `()` দিব না।

@StringUpperCase
def MyName():
    return "md rakib hassan"

## Call the function
print(MyName)  ## MD RAKIB HASSAN


##? Example 2:- (Argument passing)
def StringUpperCase(function):

    def MakeUpper(name):
        string = function(name.upper())
        return string
    
    return MakeUpper


@StringUpperCase
def MyName(name):
    print(f"My name is : {name}")


## Now call make a function ocject
name_inpute = input("Given you name :")  ## Given you name :md rakib hassan
MyName(name_inpute)   ## My name is : MD RAKIB HASSAN


##? Example 3:- (Return)
def StringUpperCase(function):

    def MakeUpper(name):
        string = function(name.upper())
        return string
    
    return MakeUpper  ##NOTE:- এখানে যেহেতু `()` দেইনি তাই Function call 
                      ##       করার সময় function এর শেষে () দেয়া লাগবে।

@StringUpperCase
def MyName(name):
    return name


## Now call make a function ocject
name_inpute = input("Given you name :")  ## Given you name :md rakib hassan
   
print(f"My name is :", MyName(name_inpute)) ## My name is : MD RAKIB HASSAN


##? Example 4:- 
def DivisionDecorators(fun):

    def inner(x,y):
        if y == 0: return "Error: ZeroDivision error!"
        return fun(x, y)
    return inner

@DivisionDecorators
def division(x, y):
    return x/y


## Call the function
print(division(10, 0))  ## Error: ZeroDivision error!
print(division(10, 5))  ## 2.0
print(division(10, 3))  ## 3.3333333333333335
print(division(3, 10))  ## 0.3



##! ===========================================================================================
##! ============================(+  Multiple Decorators   +)===================================

##? Example 1:- 
def upper_case(fun):
    def inner():
        obj = fun()
        return obj.title()
    return inner

def split_case(fun):
    def under():
        obj = fun()
        return obj.split()
    return under

@split_case
@upper_case
def UserName():   ## এখানে আগে `upper_case` then `split_case` function টি Call হবে।
    return "md rakib hassan"

## Call the function
result = UserName()
print("Result=",result) ## Result= ['Md', 'Rakib', 'Hassan']



##? Example 2:- 
def upper_case(fun):
    def inner(a):
        obj = fun(a.capitalize())
        return obj
    return inner

def split_case(fun):
    def inner(a):
        name = fun(a.split('@')[0])
        return name
    return inner

@split_case
@upper_case
def UserName(x):   ## এখানে আগে `upper_case` then `split_case` function টি Call হবে।
    return f"My name is {x}"

## Call the function
result1 = UserName('rakib@gmail.com')
result2 = UserName('hassan@gmail.com')
print("Result 1 =",result1) ## Result 1 = My name is Rakib
print("Result 2 =",result2) ## Result 2 = My name is Hassan


##? Example 3:- 
def full_name(name):
    def make_upper_case(fun):
        def inner():
            return fun() + name.upper()
        return inner
    return make_upper_case

@full_name("md rakib hassan")
def print_name():
    return "my name is "

result = print_name()
print(result)  ## my name is MD RAKIB HASSAN


##? Example 4:- 
def DivisionDecorator(fun):
    def inner(*args):
        list = []

        """
            => এখানে First number 0 হলে কোন প্রবলেম নাই, কিন্তু Second or Third number 0 হলে,
            Math Error দেখাবে। তাই এখানে 1 থেকে শুরু করা হয়েছে। [0/number = Zerodivition error]
        """
        values = args[1:] 
        for i in values:
            if i == 0:
                return "Give a number, not 0."
            
        return fun(*args)
    return inner


@DivisionDecorator
def Division_a_b(a,b):
    return a/b


@DivisionDecorator
def Division_a_b_c(a,b,c):
    return a/b/c


a = input("Enter a first number :")    
b = input("Enter a second number :")
c = input("Enter a third number :")

print(f"a = {a}, b = {b}, c = {c}")

if c == '':
    print(Division_a_b(int(a), int(b)))  ## if a=100, b=2 then result = 50.0

else:
    print(Division_a_b_c(int(a), int(b), int(c))) ## if a=100, b=2 and c=5 then result = 10.0