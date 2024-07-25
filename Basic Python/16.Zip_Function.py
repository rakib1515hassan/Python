"""
    => The zip() function returns a zip object, which is an iterator of the 
    tuples where the first item in each passed iterator is paired together,
    and then the second item in each passed iterator are paired together.
"""

##? Example 1:-

name = ["Rakib", "Hassan", "Jarray"]
roll = [1001, 1002, 1003]
age  = [24, 23, 21]

info = list(
    zip(roll, name, age)
)

print(info) ## [(1001, 'Rakib', 24), (1002, 'Hassan', 23), (1003, 'Jarray', 21)]

##* You can alos pass value like this,

info = list(
    zip(roll, name, age, "ABA" ) ## consider ABC is the section of three students
)
print(info) ## [(1001, 'Rakib', 24, 'A'), (1002, 'Hassan', 23, 'B'), (1003, 'Jarray', 21, 'A')]