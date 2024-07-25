"""
## NOTE:- map(), filter() and reduce() all do the same thing. They each take a function
          and list of elements and then return the result of appling the function to each 
          element in the list.
"""
##! ===========================================================================================
##! ===============================(+  Map Function   +)=======================================
"""
##! Map Function 
    i) 

##! Syntax:
    your_data_list = ( you list values )

    map(your_function, your_data_list)

"""
##?  Example 1:-            
def square(x):          
    return x * x        
                        
data = [2, 3, 4, 6]              ##NOTE:- You can send list/tuple anything    
result = list(map(square, data)) ##NOTE:- You can receive list/tuple anything     
print(result)   ## [4, 9, 16, 36]

##?  Example 2:-            
def square(x):          
    return x * x        
                        
data = (2, 3, 4, 6 )               ##NOTE:- You can send list/tuple anything     
result = tuple(map(square, data))  ##NOTE:- You can receive list/tuple anything 
print(result)   ## (4, 9, 16, 36)


##?  Example 3:-  
## We can also use lambda function            
data = (2, 3, 4, 6 )

result = list(
        map(
            (lambda x : x * x), data
        )
    )

print(result)   ## [4, 9, 16, 36]



##?  Example 4:-  
data = (5, 7, 22, 97)

result = tuple(
    map(
        (lambda x : (x + 3)), data
    )
)
print(result) ## (8, 10, 25, 100)


##? Example 5:-
data = ["rAkiB", "hASsAn", "jArRy"]

result = list(
    map(
        (lambda x : x.upper()), data
    )
)
print(result)  ## ['RAKIB', 'HASSAN', 'JARRY']




##! ===========================================================================================
##! ===============================(+  Filter Function   +)====================================
"""
##! Filter Function 
    i) Matching বা Condition, Fulfil না হলে তা Remove করে দেয়।


##! Syntax:
    your_data_list = ( you list values )

    filter(your_function, your_data_list)

"""
##?  Example 1:-  
def func(x):
    if x > 3:
        return x

result =list(
    filter(
        func, (1, 2, 3, 4, 5, 6, 7)
    )
)

print(result) ## [4, 5, 6, 7]


##?  Example 2:-  
data = (1, 2, 3, 4, 5)

result = tuple(           ## List/Tuple যে কোন কিছু দেয়া যায় এখানে।
    filter(
        (lambda x : x % 2 == 0), data
    )
)
print(result) ## (2, 4)

##*  If use map() function then it like, 
data = (1, 2, 3, 4, 5)

result = tuple(           ## List/Tuple যে কোন কিছু দেয়া যায় এখানে।
    map(
        (lambda x : x % 2 == 0), data
    )
)
print(result) ## (False, True, False, True, False)


