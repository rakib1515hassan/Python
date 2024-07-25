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