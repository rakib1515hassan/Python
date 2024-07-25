"""Syntax of Set Data Type:

    => Generally `{` দিয়ে শুরু হবে এবং `}` দিয়ে শেষ হবে এবং কোন Key, Value pair থাকবে না।

##! NOTE:- Set এর প্রত্যেকটি Electronics Unique হবে, কোন Items Repeated হবে না। 
    i) Unordered
    ii) Unindexed
    iii) No Duplicates value

    *) Set কে Print করলে এর ভেতরের Value গুলো এলোমেলো ভাবে আসতে পারে, index ঠিক থাকবে না।
    *) যদি আমরা Duplicate Value Set এর ভেতর দিয়ে দেই, তবে তা Print করলে পাব না, কারন তা Save হবে না।
    *) Set এর ভেতর সব ধরনের Data Type রাখা যায় না।
    *) Set এর ভেতর Items Index হেসে বে থাকে না।
"""

##! Generally we define Set like this:-  ========================================================
city = {"dhaka", "barisal", "khulna", "chitogong"}

roll = {1001, 1002, 1003, 1004, 1005, 1006}

print("Print `city` data =",city)       ##* Print `city` data = {'dhaka', 'barisal', 'chitogong', 'khulna'}
print("Print `roll` data =",roll)       ##* Print `roll` data = {1001, 1002, 1003, 1004, 1005, 1006}

print("Type of `city` =", type(city))   ##* Type of `city`    = <class 'set'> 
print("Type of `roll` =", type(roll))   ##* Type of `roll`    = <class 'set'>



##! Using Constructor to define a Set ============================================================
city = set(("dhaka", "barisal", "khulna", "chitogong"))

print("Print `city` data =",city)       ##* Print `city` data = {'barisal', 'dhaka', 'khulna', 'chitogong'}

print("Type of `city` =", type(city))   ##* Type of `city`    = <class 'set'>


##! Nested Set:- ================================================================================
person = {
    "Rakib",
    27,
    ("Md Shahjahan Mia", "Mrs. Rashida Bagum"),
    "Dhaka",
    ("Cricket", "Football"),
    "Daffodil International University",
    (81, 75, 69, 81, 65, 82),    ## Tuple এর ভেতর Duplicates দেয়া যাবে।
    27,    ## Set এর ভেতর Duplicates দিলেও তা Print এ পাওয়া যাবে না। কারন তা Sore হয়নি।
}

# print(person) 
"""Print Result =
{
    ('Cricket', 'Football'), 
    'Dhaka', 
    (81, 75, 69, 81, 65, 82), 
    ('Md Shahjahan Mia', 'Mrs. Rashida Bagum'), 
    'Rakib', 
    27, 
    'Daffodil International University'
}
"""

for info in person:

    if type(info) == tuple:
        for i in info:
            print(i)
        
    else:
        print(info)

"""Print Result =
    Dhaka
    81
    75
    69
    81
    65
    82
    Daffodil International University
    Cricket
    Football
    27
    Md Shahjahan Mia
    Mrs. Rashida Bagum
    Rakib
"""



##! ===========================================================================================
##! ===============================(+  Create/Update/Delete  +)================================

##? Method 1: ------( Add Methods )---------------
##? Add Value Into a Set 

##* Example 1:-
person = set()

person.add("Md Rakib Hassan")
person.add(26)
person.add("Dhaka")
print(person)     ## Result = `{26, 'Md Rakib Hassan', 'Dhaka'}`


##* Example 2:-
roll = {1001, 1002, 1003, 1004, 1005, 1006}
roll.add(1007)
print(roll)     ## Result = `{1001, 1002, 1003, 1004, 1005, 1006, 1007}` 


##? Method 2: ------( Update Methods )---------------
##? Change/Modify Value Into a Set 
##NOTE:- এর মাধ্যমে নতুন Value add হয়, Update হয় না।

roll = {1001, 1002, 1003, 1004, 1005, 1006}
roll.update([1003, 1009])
print(roll)     ## Result = `{1001, 1002, 1003, 1004, 1005, 1006, 1007}` 


fruits = {"Apple", "Banana", "Orange"}
fruits.update(["Pianapple", "Guava"])
print(fruits)     ## Result = `{'Banana', 'Orange', 'Guava', 'Pianapple', 'Apple'}` 


## তবে এই ভাবে আমরা তা Update করতে পারি,
fruits = {"Apple", "Banana", "Orange", "Pianapple", "Guava"}

change_value = "Banana"
new_value = "Watermelon"

for fruit in fruits:

    if fruit == change_value:
        fruits.remove(change_value)
        fruits.add(new_value)

print(fruits)



##? Method 3: ------( Del, Remove, Pop, Discard and Clear Methods )---------------
##? Delete Value Into a Set 

fruits = {"Apple", "Banana", "Orange", "Pianapple", "Guava"}

##? Del Method:- 
## সম্পূর্ন Set কে Delete করতে চাইলে del() Method টি আমরা Use কোরবো,
del fruits
print(fruits)  ## NameError: name 'fruits' is not defined অর্থাত `fruits` set Delete হয়ে গেছে।


##? Remove Method:- 
## Set হতে কোন Element কে Delete করতে চাইলে remove() Method টি আমরা Use কোরবো,
fruits.remove("Orange")
print(fruits)  ## Result = `{'Pianapple', 'Apple', 'Banana', 'Guava'}`


##? Pop Method:- 
## Set এর pop() Method এর ভেতর কোন Argument দেয়া যায় না, Bydefault Rendomly last হেতে যে কাউকে Delete করে দেয়।
fruits.pop()
print(fruits)  


##? Pop Method:- 
## Set হতে কোন Element কে Delete করতে চাইলে discard() Method টি আমরা Use কোরবো,
"""NOTE:- 
=> এটি remove() এর মত তবে, পার্থক্য হলঃ remove() এর বেতর যদি এমন কোন Value দেয়া হয় যা 
   ঐ Set এ নেই তাহলে সে `KeyError` দেয়, কিন্তু discard() তা না দিয়ে Full set কে Return করে।
"""
fruits.discard("Pianapple")
print(fruits)  



##? Clear Method:- 
## Set এর সবগুলো Element কে Remove করে দিবে।
"""NOTE:- 
=> Remove করার পর `set()` ভাবে Return করবে, কারন নয়তো তা দেখতে Dictionarty মত দেখাবে।
"""
fruits.clear()
print(fruits)   ## Result = `set()`



##! ===========================================================================================
##! ===============================(+  Set Method  +)==========================================

"""
#*  _________________________________________________________________________________________
#*  |      Name    |   Operator     |     Method     |                    Example            |
#*  |              | Math | Program |                |                                       |
#*  _________________________________________________________________________________________
#   |              |      |         |                | A = {1, 2, 3, 5, 8}  B = {2, 6, 7, 8} |
#   |              |      |         |                | Now, A | B                            |
#?  |     Union    |  U   |    |    | union()        |  = {1, 2, 3, 5, 8} | {2, 6, 7, 8}     |
#   |              |      |         |                |  = {1, 2, 3, 5, 6, 7, 8}              |
#   |              |      |         |                |                                       |
#   __________________________________________________________________________________________
#   |              |      |         |                | A = {1, 2, 3, 5, 8}  B = {2, 6, 7, 8} |
#   |              |      |         |                | Now, A & B                            |
#?  | Intersection |  ^   |    &    | intersection() |  = {1, 2, 3, 5, 8} & {2, 6, 7, 8}     |
#   |              |      |         |                |  = {2,8}                              |
#   |              |      |         |                |                                       |
#   __________________________________________________________________________________________
#   |              |      |         |                |A ={1, 2, 3, 5, 6, 7}  B ={2, 4, 6, 8} |
#   |              |      |         |                | Now, A - B                            |
#?  |   Difference |      |    -    | difference()   |  = {1, 2, 3, 5, 6, 7} - {2, 4, 6, 8}  |
#   |              |      |         |                |  = {1, 3, 5, 7}                       |
#   |              |      |         |                |                                       |
#   __________________________________________________________________________________________
#   |              |      |         |                |A ={1, 2, 3, 5, 6, 7}  B ={2, 4, 6, 8} |
#?  | Symmetric    |      |         |  symmertric_   | Now, A ^ B                            |
#?  | Difference   |      |    ^    |  difference()  |  = {1, 2, 3, 5, 6, 7} ^ {2, 4, 6, 8}  |
#   |              |      |         |                |  = {1, 3, 5, 7, 4, 8}                 |
#   |              |      |         |                |                                       |
#   __________________________________________________________________________________________
"""

##? Method 4: ------( Union Methods )---------------
a = {1, 2 , 4, 7, 9}
b = {2 , 5, 7, 8}

##* Formula 1:-
result = a | b
print("Union `a | b` =", result)  ## Union `a | b` = {1, 2, 4, 5, 7, 8, 9}


##* Formula 2:-
result = a.union(b)
print("Union `a.union(b)` =", result)  ## Union `a.union(b)` = {1, 2, 4, 5, 7, 8, 9}



##? Method 5: ------( Intersection Methods )---------------
a = {1, 2 , 4, 7, 9}
b = {2 , 5, 7, 8}

##* Formula 1:-
result = a & b
print("Intersection `a & b` =", result)  ## Intersection `a & b` = {2, 7}


##* Formula 2:-
result = a.intersection(b)
print("Intersection `a.intersection(b)` =", result)  ## Intersection `a.intersection(b)` = {2, 7}



##? Method 6: ------( Difference Methods )---------------
a = {1, 2 , 4, 7, 9}
b = {2 , 5, 7, 8}

##* Formula 1:-
result = a - b
print("Difference `a - b` =", result)  ## Difference `a - b` = {1, 4, 9}


##* Formula 2:-
result = a.difference(b)
print("Difference `a.difference(b)` =", result)  ## Difference `a.difference(b)` = {1, 4, 9}


##? Method 7: ------( Symmetric Difference Methods )---------------
a = {1, 2, 4, 7, 9}
b = {2 , 5, 7, 8}

##* Formula 1:-
result = a ^ b
print("Symmetric Difference `a ^ b` =", result)  ## Symmetric Difference `a ^ b` = {1, 4, 5, 8, 9}


##* Formula 2:-
result = a.symmetric_difference(b)
print("Symmetric Difference `a.symmetric_difference(b)` =", result)
"""Print Result =
    => Symmetric Difference `a.symmetric_difference(b)` = {1, 4, 5, 8, 9}
"""


##? Method 8: ------( Frozen Methods )---------------
"""
    => কোন Set কে যদি কোথাও Frozen করে রাখা হয় তাবে তার ভেতর কোন Value, add/update/delete করা যায় না।
"""
a = {"Rakib", 26, "Backend Developer"}

b = frozenset(a)

print(a)  ## Result = `{'Rakib', 26, 'Backend Developer'}`
a.add("Dhaka")
print(a)  ## Result = `{'Rakib', 26, 'Dhaka', 'Backend Developer'}`

print(b)  ## Result = `frozenset({'Rakib', 26, 'Backend Developer'})`
b.add("Dhaka")
print(b)  ## Result = `AttributeError: 'frozenset' object has no attribute 'add'`



##? Method 9: ------( Intersection_Update Methods )---------------
##NOTE:- print() এর ভেতর এই Method কে use করা যাবে না।
a, b = {1, 2 , 4, 7, 9}, {2 , 5, 7, 8}

a.intersection_update(b)  ## প্রথমে intersection() কোরবে তারপর তার Result কে Store করবে।
print(a)  ## Result = `{2, 7}`
print(b)  ## Result = `{8, 2, 5, 7}`


b.intersection_update(a)  ## প্রথমে intersection() কোরবে তারপর তার Result কে Store করবে।
print(a)  ## Result = `{1, 2, 4, 7, 9}`
print(b)  ## Result = `{2, 7}`



##? Method 10: ------( difference_update Methods )---------------
a, b = {1, 2 , 4, 7, 9}, {2 , 5, 7, 8}

a.difference_update(b)  ## প্রথমে difference() কোরবে তারপর তার Result কে Store করবে।
print(a)  ## Result = `{1, 4, 9}`
print(b)  ## Result = `{8, 2, 5, 7}`


b.difference_update(a)  ## প্রথমে difference() কোরবে তারপর তার Result কে Store করবে।
print(a)  ## Result = `{1, 2, 4, 7, 9}`
print(b)  ## Result = `{5, 8}`


# ##? Method 11: ------( symmetric_difference_update Methods )---------------
a, b = {1, 2, 4, 7, 9}, {2 , 5, 7, 8}

a.symmetric_difference_update(b)  ## প্রথমে symmetric_difference_update() কোরবে তারপর তার Result কে Store করবে।
print(a)  ## Result = `{1, 4, 5, 8, 9}`
print(b)  ## Result = `{8, 2, 5, 7}`


b.symmetric_difference_update(a)  ## প্রথমে symmetric_difference_update() কোরবে তারপর তার Result কে Store করবে।
print(a)  ## Result = `{1, 2, 4, 7, 9}`
print(b)  ## Result = `{1, 4, 5, 8, 9}`


##? Method 12: ------( Sum Methods )---------------
a = {1, 2 , 4, 7, 9}

result = sum(a)
print("Result =", result)  ## Result = 23


##? Method 13: ------( Max Methods )---------------
a = {110, 250 , 268, 74, 92}

result = max(a)
print("Result =", result)  ## Result = 268


##? Method 14: ------( Sorted Methods )---------------
a = {110, 250 , 268, 74, 92}

result = sorted(a)
print("Result =", result)  ## Result = [74, 92, 110, 250, 268]
print("Result Type =", type(result))  ## Result Type = <class 'list'>


##? Method 14: ------( Is Sub-Set Methods )---------------
"""
=> যদি একটি Set এর কিছু উপাদান আরেকটি Set এ থাকে, তবে সেই প্রথম সেটের একটি sub-set হবে দ্বিতীয় Set টি।
    Ex: A = {1, 2, 5, 4, 7, 9} এখানে A যদি একটি set হয়, এবং B = {2, 4, 7, 9} যদি আর একটি 
        set হয় তবে, এবং A set এর কিছু উপাদান যদি B set এ উপস্থিত থাকে তবে, B set টি A এর একটি
        sub-set হবে, যা আমরা দেখতে পাচ্ছি যে A set এর কিছু উপাদান B set এ উপস্থিত আছে, তাই বলা
        যায় B set টি A এর একটি seb-set
"""

a = {1, 2, 5, 4, 7, 9}
b = {2, 4, 7, 9}
c = {4, 9}
d = {1, 5, 7, 12}

print("a কি b এর sub-set ? :", a.issubset(b)) ## a কি b এর sub-set ? : False

print("b কি a এর sub-set ? :", b.issubset(a)) ## b কি a এর sub-set ? : True

print("a কি c এর sub-set ? :", a.issubset(c)) ## a কি c এর sub-set ? : False

print("b কি c এর sub-set ? :", b.issubset(c)) ## b কি c এর sub-set ? : False

print("c কি b এর sub-set ? :", c.issubset(b)) ## c কি b এর sub-set ? : True

print("c কি a এর sub-set ? :", c.issubset(a)) ## c কি a এর sub-set ? : True

print("a কি d এর sub-set ? :", a.issubset(d)) ## a কি d এর sub-set ? : False

print("d কি a এর sub-set ? :", d.issubset(a)) ## d কি a এর sub-set ? : False


##? Method 15: ------( Is Super-Set Methods )---------------
"""
=> যদি একটি Set এর কিছু উপাদান আরেকটি Set এ থাকে, তবে সেই প্রথম সেটের একটি sub-set হবে দ্বিতীয় Set টি।
    এবং প্রথম Set টি কে বলে, Super-set
    Ex: A = {1, 2, 5, 4, 7, 9} এখানে A যদি একটি set হয়, এবং B = {2, 4, 7, 9} যদি আর একটি 
        set হয় তবে, এবং A set এর কিছু উপাদান যদি B set এ উপস্থিত থাকে তবে, B set টি A এর একটি
        sub-set হবে, যা আমরা দেখতে পাচ্ছি যে A set এর কিছু উপাদান B set এ উপস্থিত আছে, তাই বলা
        যায় B set টি A এর একটি seb-set এবং A set টি কে বলে B set এর Super Set
"""

a = {1, 2, 5, 4, 7, 9}
b = {2, 4, 7, 9}
c = {4, 9}
d = {1, 5, 7, 12}

print("a কি b এর sub-set ? :", a.issubset(b)) ## a কি b এর sub-set ? : False
print("a কি b এর super-set ? :", a.issuperset(b)) ## a কি b এর super-set ? : True
print("\n")

print("b কি a এর sub-set ? :", b.issubset(a)) ## b কি a এর sub-set ? : True
print("b কি a এর super-set ? :", b.issuperset(a)) ## b কি a এর super-set ? : False
print("\n")

print("a কি c এর sub-set ? :", a.issubset(c)) ## a কি c এর sub-set ? : False
print("a কি c এর super-set ? :", a.issuperset(c)) ## a কি c এর super-set ? : True
print("\n")

print("b কি c এর sub-set ? :", b.issubset(c)) ## b কি c এর sub-set ? : False
print("b কি c এর super-set ? :", b.issuperset(c)) ## b কি c এর super-set ? : True
print("\n")

print("c কি b এর sub-set ? :", c.issubset(b)) ## c কি b এর sub-set ? : True
print("c কি b এর super-set ? :", c.issuperset(b)) ## c কি b এর super-set ? : False
print("\n")

print("c কি a এর sub-set ? :", c.issubset(a)) ## c কি a এর sub-set ? : True
print("c কি a এর super-set ? :", c.issuperset(a)) ## c কি a এর super-set ? : False
print("\n")

print("a কি d এর sub-set ? :", a.issubset(d)) ## a কি d এর sub-set ? : False
print("a কি d এর super-set ? :", a.issuperset(d)) ## a কি d এর super-set ? : False
print("\n")

print("d কি a এর sub-set ? :", d.issubset(a)) ## d কি a এর sub-set ? : False
print("d কি a এর super-set ? :", d.issuperset(a)) ## d কি a এর super-set ? : False


##? Method 16: ------( Is Dis-Joint Methods )---------------
"""
=> যদি একটি Set এর কোন উপাদান আরেকটি Set এর কোন উপাদান এর সাথে মিল না থাকেতবে তাকে Disjoint বলে।
"""

a = {1, 2, 5, 4, 7, 9}
b = {2, 4, 7, 9}

c = {1, 5, 7, 12}
d = {3, 6, 8}

print(c.isdisjoint(a))  ## False
print(a.isdisjoint(c))  ## False


print(a.isdisjoint(d))  ## True
print(d.isdisjoint(a))  ## True