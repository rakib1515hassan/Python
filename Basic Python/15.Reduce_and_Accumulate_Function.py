"""
    => reduce() and accumulate() functions can be used to calculate the 
    summation of a sequence elements. But there are differences in the 
    implementation aspects in both these.
"""
##! ===========================================================================================
##! ===============================(+  Reduce Function   +)====================================
"""
##! Reduce Function 
    i) It give us single value
    ii) Need to import `from functools import reduce`

##! Syntax:
    your_data_list = ( you list values )

    reduce(expression, your_data_list)

"""

from functools import reduce

##?  Example 1:- 
data = [23, 21, 45, 98]
result = reduce(
    (lambda a, b : a + b), data
)

# ##* You can also pass data like,
result = reduce(
    (lambda a, b : a + b), [23, 21, 45, 98]
)

print(result)  ## 187

"""
#?   _______________________________
#?  |   x   |   y   :  x  +  y     |
#?   _______________________________
#   |   23  |   21  |      44      |
#   _______________________________
#   |   44  |   45  |      89      |
#   _______________________________
#   |   89  |   98  |      187     |
#   _______________________________

"""


##?  Example 2:- 
result = reduce(
    (lambda a, b : a * b), [1, 2, 3, 4, 5]
)

print(result)  ## 120


##! ===========================================================================================
##! ===============================(+  Accumulate Function   +)================================

from itertools import accumulate

##?  Example 1:- 
data = [23, 21, 45, 98]

result = list(
        accumulate(
            data, (lambda a, b : a + b)
        )
    )

print(result)  ## [23, 44, 89, 187]

"""
#?   ____________________________________
#?  |   x   | x  +  y |   result        |
#?   ____________________________________
#   |  23   | 23 + 21 |  23, 44         |
#   _____________________________________
#   |  44   | 44 + 45 | 23, 44, 89      |
#   _____________________________________
#   |  89   | 89 +98  | 23, 44, 89, 187 |
#   _____________________________________

"""