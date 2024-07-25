"""Syntax of Tuple Data Type:

    => Generally `(` দিয়ে শুরু হবে এবং `)` দিয়ে শেষ হবে। তবে তা না হয়ে কেবল কোন String 
       এর শেষে যদি `,` থাকে তবে সেটিও Tuple হবে।

##! NOTE:- Tuple এবং List এর মধ্যে পার্থক্য হল, 
#!         Tuple এর Value পরিবর্তন করা যায় না, অপর দিকে List এর value পরিবর্তন করা যায়।
"""

##! Generally we define Tuple like this:-  ========================================================
a = ("I", "live", "in", "Dhaka", "science", 2001)


print("Print `a` data =",a)       ##* Print `a` data = ('I', 'live', 'in', 'Dhaka', 'science', 2001)

print("Type of `a` =", type(a))   ##* Type of `a`    = <class 'tuple'>

"""##NOTE:- Structure of Tuple and Index
##? Length     1      2      3      4         5        6         
##* Index      0      1      2      3         4        5        
#            ("I", "live", "in", "Dhaka", "science", 2001)
##! Index     -6     -5     -4     -3        -2       -1
"""  

print(a[0])   ## Result = `I`
print(a[3])   ## Result = `Dhaka`
print(a[-3])  ## Result = `Dhaka`
print(a[-5])  ## Result = `live`

print("\n\n")
print(a[1:4])    ## Result = `('live', 'in', 'Dhaka')`
print(a[::-1])   ## Result = `(2001, 'science', 'Dhaka', 'in', 'live', 'I')`
print(a[:-4:-1]) ## Result = `(2001, 'science', 'Dhaka')`
print(a[:2:-1])  ## Result = `(2001, 'science', 'Dhaka')`


b = "bangladesh"
print("Type of `b` =", type(b)) ##* Type of `b` = <class 'str'>

c = "bangladesh",
print("Type of `c` =", type(c)) ##* Type of `c` = <class 'tuple'>
print(c)  ## Result = `('bangladesh',)`

d = "bangladesh", "australia", "canada", "newzealand", "pakistan", "saudiarab"
print("Type of `d` =", type(c)) ##* Type of `c` = <class 'tuple'>
print(d) ## Result = `('bangladesh', 'australia', 'canada', 'newzealand', 'pakistan', 'saudiarab')`



##! Using Constructor to define a list
e = tuple(("I", "live", "in", "Dhaka", "science", 2001))

print("Print `e` data =",e)       ##* Print `e` data = ('I', 'live', 'in', 'Dhaka', 'science', 2001)

print("Type of `e` =", type(e))   ##* Type of `e`    = <class 'tuple'>



##! Nested Tuple:- ============================================================================
##NOTE:- Tuple এর ভেতর আমরা যে কোন Dtaa Type (int, float, boolen, list, dic, set) এর Data রাখতে পারি।

a = (("Dhaka", "Savar", "Ghazipur"), "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal")

print(a) ## Result = (('Dhaka', 'Savar', 'Ghazipur'), 'Khulna', 'Sylhet', ['Chittagong', 'Cox's Bazar', 'Rangamati'], 'Rajshahi', 'Rangpur', 'Mymensingh', 'Barishal')

print("Type of `a` =", type(a)) ## Type of `a` = <class 'tuple'>

"""##NOTE:- Structure of Nested List and Index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            ((                  ), "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal")
##! Index          -8                  -7        -6             -5                    -4        -3          -2          -1
#               "Dhaka",   (0,0)/(-8,-3)                   "Chittagong",   (3,0)/(-8,-3)       
#               "Savar",   (0,1)/(-8,-2)                   "Cox's Bazar", (3,1)/(-8,-2)
#               "Ghazipur"  (0,2)/(-8,-1)                   "Rangamati",   (3,2)/(-8,-1)
#            
"""
print("\n\n")
print("Posetive Index: ")
print(a[0])       ## Result = `('Dhaka', 'Savar', 'Ghazipur')`
print(a[1])       ## Result = `Khulna`
print(a[3])       ## Result = `['Chittagong', 'Cox's Bazar', 'Rangamati']`
print(a[6])       ## Result = `Mymensingh`

print("\n\n")
print("Negative Index: ")
print(a[-3])       ## Result = `Rangpur`
print(a[-5])       ## Result = `['Chittagong', 'Cox's Bazar', 'Rangamati']`
print(a[-7])       ## Result = `Khulna`
print(a[-8])       ## Result = `('Dhaka', 'Savar', 'Ghazipur')`

print("\n\n")
print("Posetive Nested Index: ")
print(a[0][0])     ## Result = `Dhaka`
print(a[0][1])     ## Result = `Savar`
print(a[0][2])     ## Result = `Ghazipur`

print("\n\n")
print("Negative Nested Index: ")
print(a[-8][-1])   ## Result = `Ghazipur`
print(a[-8][-2])   ## Result = `Savar`
print(a[-8][-3])   ## Result = `Dhaka`


##! User Input for a Taple:- ============================================================================
##! যেহেতু Tuple এর ভেলু Insurt,Update, Delete করা যায় না তাই প্রথমে একটি List এ 
##! input নিয়ে তা type custing করে Tuple এ Convert করতে হবে।
##? Formula 1 :-
my_list = []

n = int(input("How many items you want to add on your list? = "))  ## If you gibe here `5`

for i in range(n):
    value = input(f"Give your {i+1} item value =") ## If You give value like `Dhaka, Rajshahi, Barishal, Khulna, Chittagong`
    my_list.append(value)

my_taple = tuple(my_list) ## Type custing
print("My Tuple is: ", my_taple)  ## My Tuple is:  ('Dhaka', 'Rajshahi', 'Barishal', 'Khulna', 'Chittagong')


##? Formula 2 :-
input_data = input("Give your items using spaces: ")  ## If given input like: `Dhaka Barisan Khulna Rajshahi`

my_tuple = tuple(input_data.split())

print("My Tuple is: ", my_tuple) ## My Tuple is:  ('Dhaka', 'Barisan', 'Khulna', 'Rajshahi')


##? Formula 3 :-
"""
#NOTE: এই ভাবে Unlimited Value inpute আমরা নিতে পারি, যখন কোন কিছু input না দিয়ে `Enter` Press করে 
       দিব, তখনি আমদের Whil loop টি False হয়ে যাবে এবং আমরা আমাদের Print এর Result টি পেয়ে যাবো।
"""
my_list = []

count = 0

while True:  ## যখন while loop টি False হয়ে যাবে তখন Input নেয়া বন্দ হয়ে যাবে।

    value = input(f"Give your {count + 1} value =")
    if not value:
        break
    my_list.append(value)
    count += 1

my_tuple = tuple(my_list)
print(my_tuple)


"""
##! ===========================================================================================
##! ===============================(+  Tuple Method  +)=========================================
"""
"""
    => যেহেতু Tuple এর ভেলু Insurt,Update, Delete করা যায় না তাই প্রথমে একটি List এ
       Convert করে Insurt,Update, Delete করতে হবে, এবং পুনরায় Tuple এ Convart করতে হবে।
"""

##? Method 1: ------( Append, Extend, Insert Methods )---------------
##? Add Value Into a Tuple using the List 

fruits = ("Apple", "Banana", "Orange")

temp_list = list(fruits)


##TODO## Formula 1 ( Append ):-
"""
    => একটা একটা করে Data add করার জন্যে ব্যবহার করা হয়।
"""
temp_list.append("Grapes") 
fruits = tuple(temp_list)
print(fruits)  ## Result = `('Apple', 'Banana', 'Orange', 'Grapes')`



##TODO## Formula 2 ( Extend ):-
"""
    => অনেক গুলো Data একসাথে Add করার জন্যে ব্যবহার করা হয়।
"""
temp_list.extend(["Grapes","Guava", "Watermelon", "Pineapple"])
fruits = tuple(temp_list)
print(fruits)  ## Result = `('Apple', 'Banana', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple')`



##TODO## Formula 3 ( Insert ) :-
"""
    => যদি List এর কোন নির্দিষ্ট স্থানে কোন Value add করতে চাই তবে এটি আমরা ব্যবহার করতে পারি। 
"""
temp_list.insert(1, "Guava") ## Hser, 1 is index and "Guava" is value
fruits = tuple(temp_list)
print(fruits)  ## Result = `('Apple', 'Guava', 'Banana', 'Orange')`



##? ----------------------------------------------------------------------
##? Change/Modify Value Into a Tuple using the List 

fruits = ("Apple", "Banana", "Orange")

temp_list = list(fruits)

##TODO##   Example 1:
temp_list[1] = "Guava"
fruits = tuple(temp_list)
print(fruits)


##TODO##   Example 2:
input_index = int(input("Give a index number to the item value: "))    ## If give 1
# input_value = input("Give a value to add on this ixdex position: ")  ## If give `Guava`

if (input_index > (len(temp_list)-1)) or (input_index < 0):
    print("Error: Invalid Index Number!")

else:
    input_value = input("Give a value to add on this ixdex position: ")  ## If give `Guava`
    temp_list[input_index] = input_value
    fruits = tuple(temp_list)
    print(fruits)     ## Result = `('Apple', 'Guava', 'Orange')`


##TODO##   Example 3:
input_value = input("Given a value, which one you want to change? :")  ## If give `Banana`

search_flag = False

for index,fruit in enumerate(temp_list):
    if input_value == fruit:
        input_new_value = input("Given a new value for add on your list :")  ## If value set `Guava`
        temp_list[index] = input_new_value
        search_flag = True
        break
    else:
        search_flag = False


if search_flag == True:
    fruits = tuple(temp_list)
    print("New List: ",fruits)    ## Result = `('Apple', 'Guava', 'Orange')`
else:        
    print("Error: Your input value not found!")



##? Method 2: --------------( Del, Remove, Pop, Clear Methods)-------------------------
##? Delete Value Item

fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple']

temp_list = list(fruits)

##TODO## Formula 1 ( Del ):-
"""
    => List এর index ধরে Remove কতে চাইলে।
"""
del temp_list[1]
fruits = tuple(temp_list)
print(fruits) ## Result = `('Apple', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple')`


del temp_list[1:4]
fruits = tuple(temp_list)
print(fruits) ## Result = `('Apple', 'Guava', 'Watermelon', 'Pineapple')`


##TODO## Formula 2 ( Remove ):-
"""
    => Item এর Value ধরে Delete করতে চাইলে এটি ব্যবহার করা যায়। একাধিক Item Remove করা যায় না।
"""
temp_list.remove("Banana")  
fruits = tuple(temp_list)
print(fruits) ## Result = `('Apple', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple')`



##TODO## Formula 3 ( Pop ):-
"""
    => Item এর শেষ Value কে Delete করে দেয়। তবে এর দ্বারা Index এর ভিতিতেও Delete করা যায়।
"""
temp_list.pop()
fruits = tuple(temp_list)
print(fruits) ## Result = `('Apple', 'Banana', 'Orange', 'Grapes', 'Guava', 'Watermelon')`

temp_list.pop(2)
fruits = tuple(temp_list)
print(fruits) ## Result = `('Apple', 'Banana', 'Grapes', 'Guava', 'Watermelon', 'Pineapple')`



##TODO## Formula 3 ( Clear ):-
"""
    => পুর List এর সকল Values গুলো কে Delete করে দিতে চাইলে আমরা Clear Method টি ব্যবহার কোরবো।
"""
temp_list.clear()
fruits = tuple(temp_list)
print(fruits) ## Result = `()`



##? ---------------------------------------------------------------------
##? Retrieve Tuple Values

divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal")

for division in divisions:
    print("Division Name:",division)

""" ##* Result =
        Division Name: Dhaka
        Division Name: Khulna
        Division Name: Sylhet
        Division Name: Chittagong
        Division Name: Rajshahi
        Division Name: Rangpur
        Division Name: Mymensingh
        Division Name: Barishal
"""


divisions = (("Dhaka", "Savar", "Ghazipur"), "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal")


for division in divisions:

    if (type(division)  is tuple) or (type(division)  is list):
        for city in division:
            print("City Name: ",city)

"""##* Result =
        City Name:  Dhaka
        City Name:  Savar
        City Name:  Ghazipur
        City Name:  Chittagong
        City Name:  Cox's Bazar
        City Name:  Rangamati
"""


divisions = (("Dhaka", "Savar", "Ghazipur"), "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal")

"""##NOTE:- Structure of Nested Tuple and Index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            ((                  ), "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal")
##! Index          -8                  -7        -6             -5                    -4        -3          -2          -1
#               "Dhaka",   (0,0)/(-8,-3)                   "Chittagong",   (3,0)/(-8,-3)       
#               "Savar",   (0,1)/(-8,-2)                   "Cox's Bazar", (3,1)/(-8,-2)
#               "Ghazipur"  (0,2)/(-8,-1)                   "Rangamati",   (3,2)/(-8,-1)
#            
"""

for d_index, division in enumerate(divisions):

    if (type(division)  is tuple) or (type(division)  is list):
        for c_index, city in enumerate(division):
            print(f"City Name: {city} | Index: {d_index, c_index}")

    else:
        print(f"Division Name: {division}| Index: {d_index}")

"""##* Result =
            City Name: Dhaka | Index: (0, 0)
            City Name: Savar | Index: (0, 1)
            City Name: Ghazipur | Index: (0, 2)
        Division Name: Khulna| Index: 1
        Division Name: Sylhet| Index: 2
            City Name: Chittagong | Index: (3, 0)
            City Name: Cox's Bazar | Index: (3, 1)
            City Name: Rangamati | Index: (3, 2)
        Division Name: Rajshahi| Index: 4
        Division Name: Rangpur| Index: 5
        Division Name: Mymensingh| Index: 6
        Division Name: Barishal| Index: 7
"""

length = len(divisions)
print("Length =", length)  ## Result = `8`



##? Method 4: --------------( Index Method )-------------------------
"""
    => index method এর সাহায্যে আমরা কোন Tuple এর Value দেয়ার মাধ্যমে তার Index জনতে পারি। 
       প্রথমে জকে পাবে, তার Index সে দেখাবে, পরের Item এর Index কে সে আর দেখাবে না।

       NOTE:- Nested Tuple এর ক্ষত্রে এটা কাজ কোরবে না। সেই ক্ষেত্রে Menual নিয়বে কোরতে হবে।
"""

divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal", "Rajshahi")

inpute_value = input("Given a name which one index you want to know? :") ## If give :Rajshahi

try:
    index_no = divisions.index(inpute_value)
    print(f"{inpute_value} index no: {index_no}")  ## Result = `Rajshahi index no: 4`

except Exception as e:
    print(f"Error: {e}")


divisions = (("Dhaka", "Savar", "Ghazipur"), "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal")

"""##NOTE:- Structure of Nested tuple and Index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            ((                  ), "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal")
##! Index          -8                  -7        -6             -5                    -4        -3          -2          -1
#               "Dhaka",   (0,0)/(-8,-3)                   "Chittagong",   (3,0)/(-8,-3)       
#               "Savar",   (0,1)/(-8,-2)                   "Cox's Bazar", (3,1)/(-8,-2)
#               "Ghazipur"  (0,2)/(-8,-1)                   "Rangamati",   (3,2)/(-8,-1)
#            
"""

inpute_value = input("Given a name which one index you want to know? :") ## If give :Rajshahi Else If give :Cox's Bazar

search_flag = False

index_no = []

for d_index, division in enumerate(divisions):

    if (type(division)  is list) or (type(division)  is tuple):
        for c_index, city in enumerate(division):
            if inpute_value == city:
                index_no.extend([d_index, c_index])
                search_flag = True
                break
    else:
        if inpute_value == division:
            index_no.append(d_index)
            search_flag = True
            break



if search_flag == True:
    print(f"{inpute_value} index no: {index_no}") 
    """Result = 
            If given :Rajshahi then Result :Rajshahi index no: [4] 
            Else if give :Cox's Bazar then Result :Cox's Bazar index no: [3, 1]
    """
else:        
    print("Error: Your input value not found!")



##? Method 5: --------------( Count Method )-------------------------
"""
    => Tuple এর ভতের কতগুলো Item আছে তা বের করে দেয়।

       NOTE:- Nested Tuple এর ক্ষত্রে এটা কাজ কোরবে না। সেই ক্ষেত্রে Menual নিয়মে কোরতে হবে।
"""

divisions = ("Dhaka", "Khulna", "Sylhet", "Chittagong",("Chittagong", "Cox Bazer", "Bandorbon", "Dhaka"), "Dhaka", ["Saver", "Dhaka", "Ghazipur"], "Mymensingh", "Sylhet")

elements = divisions.count("Sylhet")
print("Total elements =", elements)  ## Result = `Total elements = 3`


elements = divisions.count("Dhaka") ##! `Dhaka` মোট 4 বার আছে, কিন্তু এখানে 2 বার দেখবে। Nested Tuple কাজ কোরবে না।
print("Total elements =", elements)  ## Result = `Total elements = 2`


##! Nested Tuple এর ক্ষত্রে এটি বের করার জন্যে আমাদের Munually করতে হবে।

inpute_value = input("Given a name which one index you want to know? :") ## If give :Rajshahi Else If give :Cox Bazer

total_count = 0

search_flag = False

for d_index, division in enumerate(divisions):

    if (type(division)  is list) or (type(division)  is tuple):
        for c_index, city in enumerate(division):
            if inpute_value == city:
                total_count+=1
                search_flag = True
    else:
        if inpute_value == division:
            total_count+=1
            search_flag = True

if search_flag == True:
    print(f"Total `{inpute_value}`, have in our tuple= {total_count}") 
else:        
    print(f"Error: Your input value `{inpute_value}` not found!")



##? Method 6: --------------( Reverse Method )-------------------------

divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal", "Rajshahi")

temp_list = list(divisions)
temp_list.reverse()

divisions = tuple(temp_list)

print(divisions) ## Results = `('Rajshahi', 'Barishal', 'Mymensingh', 'Rangpur', 'Rajshahi', 'Chittagong', 'Sylhet', 'Khulna', 'Dhaka')`



##? Method 6: --------------( Sort Method )-------------------------
"""
    => এখনে ASCII অনুসারে Sort করে। By Default Ascending Order এ Sort হয়, তবে `sort(reverse=True)`
       কোরলে Descending Order এ Sort করবে।
"""

divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal", "Rajshahi")

##! Order by Ascending order
temp_list = list(divisions)
temp_list.sort()
divisions = tuple(temp_list)
print("After Sort Divisions: ",divisions) 
"""Result =
    => ('Barishal', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rajshahi', 'Rangpur', 'Sylhet')
"""


income = (22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000)

temp_list = list(income)
temp_list.sort()
income = tuple(temp_list)
print("After Sort Income: ",income)
"""Result =
    => (10000, 15000, 18000, 22000, 22000, 25000, 32000, 35000, 41000, 55000)
"""

##! Order by Descending order
divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal", "Rajshahi")

temp_list = list(divisions)
temp_list.sort(reverse=True)
divisions = tuple(temp_list)
print("After Sort Divisions: ",divisions) 
"""Result =
    => ('Sylhet', 'Rangpur', 'Rajshahi', 'Rajshahi', 'Mymensingh', 'Khulna', 'Dhaka', 'Chittagong', 'Barishal')
"""


income = (22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000)

temp_list = list(income)
temp_list.sort(reverse=True)
income = tuple(temp_list)
print("After Sort Income: ",income)
"""Result =
    =>  (55000, 41000, 35000, 32000, 25000, 22000, 22000, 18000, 15000, 10000)
"""


##! Order by Length
#NOTE:- Integer এর কোন Length হয় না, তাই এটিকে key=len এর ভিতিতে Sort করা যায় না।

divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal", "Rajshahi")

temp_list = list(divisions)
temp_list.sort(reverse=True, key=len)
divisions = tuple(temp_list)
print("After Sort Divisions: ",divisions) 
"""Result =
      => ('Chittagong', 'Mymensingh', 'Sylhet', 'Rajshahi', 'Rangpur', 'Barishal', 'Rajshahi', 'Khulna', 'Dhaka')
#* Length:    9            9            7          7          7          7          7          6        5
"""



##? Method 7: --------------( Sorted Method )-------------------------
"""
    => Sort এবং Sorted একি, তবে Sorted করার জন্যে তা নতুন কোন Variable এ রাখতে হয়। 

    ##NOTE:- Always return a List
"""
##! Order by Ascending order
divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal", "Rajshahi")

sorted_divisions = sorted(divisions)
print("After Sort Divisions: ",sorted_divisions) 
"""Result =
    => ['Barishal', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rajshahi', 'Rangpur', 'Sylhet']
"""


income = (22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000)

sorted_income = sorted(income)
print("After Sort Income: ",sorted_income)
"""Result =
    => [10000, 15000, 18000, 22000, 22000, 25000, 32000, 35000, 41000, 55000]
"""

##! Order by Descending order
divisions = ("Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal", "Rajshahi")

sorted_divisions = sorted(divisions, reverse=True)
print("After Sort Divisions: ",sorted_divisions) 
"""Result =
    => ['Sylhet', 'Rangpur', 'Rajshahi', 'Rajshahi', 'Mymensingh', 'Khulna', 'Dhaka', 'Chittagong', 'Barishal']
"""


income = (22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000)

sorted_income = sorted(income, reverse=True)
print("After Sort Income: ",sorted_income)
"""Result =
    => [55000, 41000, 35000, 32000, 25000, 22000, 22000, 18000, 15000, 10000]
"""


##? Method 8: --------------( Max, Min and Sum Method )-------------------------
"""
    => একটি Tuple এর Max, Min and Summation বের করার জন্যে এই Method গুলো ব্যবহার করা হয়।
"""
## Example 1:-
income = (22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000)

max_value = max(income)
min_value = min(income)
min_value = sum(income) ##NOTE:- Tuple এর ভেলু গুলো Mustbe Integer or Float হতে হবে।


print("Tuple Max Value: ",max_value)   ## Result = `55000`
print("Tuple Min Value: ",min_value)   ## Result = `10000` 
print("Tuple Sum: ",min_value)         ## Result = `275000` 


## Example 2:-
fruits = ("cucumber", "benana", "apple", "Watermelon", "Pianapple", "Orange", "Guava")

"""
##! ASCII       c = 99     b = 98    a = 97    W = 87        P = 80      O = 79    G = 71
## Tuple      ("cucumber", "benana", "apple", "Watermelon", "Pianapple", "Orange", "Guava")
"""

max_value = max(fruits)
min_value = min(fruits)

print("Tuple Max Value: ",max_value)   ## Result = `cucumber`
print("Tuple Min Value: ",min_value)   ## Result = `Guava`



##? Method 9: --------------( Zip Method )-------------------------
"""
    => এর সাহায্যে দুটি Tuple কে একসাথে নিয়ে Nested Tuple তৈরি করে।
"""


name = ("Rakib", "Hassan", "Ratul", "Sabbir", "Omor", "Ovi")
age  = (26, 24, 27, 25, 29, 30)

new_tuple = tuple(zip(name, age))

print("New Tuple: ", new_tuple)

"""Result:
    => (('Rakib', 26), ('Hassan', 24), ('Ratul', 27), ('Sabbir', 25), ('Omor', 29), ('Ovi', 30))
"""