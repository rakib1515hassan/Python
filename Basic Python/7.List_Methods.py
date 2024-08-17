"""NOTE:- Syntax of List Data Type:
We can store the sequential data on List. Any type of data we can store in List.

=> Generally `[` দিয়ে শুরু হবে এবং `]` দিয়ে শেষ হবে। 
"""
##! Generally we define list like this:-  ========================================================

a = ["I", "live", "in", "Dhaka", "science", 2001]

print("Print `a` data =",a)       ##* Print `a` data = ['I', 'live', 'in', 'Dhaka', 'science', 2001]

print("Data Type of `a` =", type(a))   ##* Type of `a`    = <class 'list'>

print("Length of `a` =", len(a))       ##* Length of `a` = 6


"""##NOTE:- Structure of List and Index
##? Length     1      2      3      4         5        6         
##* Index      0      1      2      3         4        5        
#            ["I", "live", "in", "Dhaka", "science", 2001]
##! Index     -6     -5     -4     -3        -2       -1
"""  



print("a[0]", a[0])   ## Result = `I`
print("a[3]", a[3])   ## Result = `Dhaka`
print("a[-3]",a[-3])  ## Result = `Dhaka`
print("a[-5]",a[-5])  ## Result = `live`

print("\n")
print("a[1:4] = ",  a[1:4])     ## Result = `['live', 'in', 'Dhaka']`
print("a[:-1] = ",  a[:-1])     ## Result = `['I', 'live', 'in', 'Dhaka', 'science']`
print("a[1:-1] = ", a[1:-1])    ## Result = `['live', 'in', 'Dhaka', 'science']`
print("a[-3:-1] = ",a[-3:-1])   ## Result = `['Dhaka', 'science']`

print("\n")
print("a[::2]  = ",a[::2])      ## Result = `['I', 'in', 'science']`
print("a[::-1] = ",a[::-1])     ## Result = `[2001, 'science', 'Dhaka', 'in', 'live', 'I']`
print("a[::-2] = ",a[::-2])     ## Result = `[2001, 'Dhaka', 'live']`
print("a[:-4:-1] = ",a[:-4:-1]) ## Result = `[2001, 'science', 'Dhaka']`
print("a[:2:-1]  = ",a[:2:-1])  ## Result = `[2001, 'science', 'Dhaka']`
print("a[:-3:-1] = ",a[:-3:-1]) ## Result = `[2001, 'science']`
print("a[:3:-1]  = ",a[:3:-1])  ## Result = `[2001, 'science']`
print("a[:2:-1]  = ",a[:2:-1])  ## Result = `[2001, 'science', 'Dhaka']`




##! Using Constructor to define a list
b = list(("I", "live", "in", "Dhaka", "science", 2001))

print("Print `b` data =",b)       ##* Print `b` data = ['I', 'live', 'in', 'Dhaka', 'science', 2001]

print("Type of `b` =", type(b))   ##* Type of `b`    = <class 'list'>




##! Nested List:- ============================================================================

a = [["Dhaka", "Savar", "Ghazipur"], "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]

print(a) ## Result = [['Dhaka', 'Savar', 'Ghazipur'], 'Khulna', 'Sylhet', ['Chittagong', 'Cox's Bazar', 'Rangamati'], 'Rajshahi', 'Rangpur', 'Mymensingh', 'Barishal ']
print("Type of `a` =", type(a)) ## Type of `a` = <class 'list'>

"""##NOTE:- Structure of Nested List and Index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            [[                  ], "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]
##! Index          -8                  -7        -6             -5                    -4        -3          -2          -1
#               "Dhaka",   (0,0)/(-8,-3)                   "Chittagong",   (3,0)/(-8,-3)       
#               "Savar",   (0,1)/(-8,-2)                   "Cox's Bazar", (3,1)/(-8,-2)
#               "Ghazipur"  (0,2)/(-8,-1)                   "Rangamati",   (3,2)/(-8,-1)
#            
"""
print("\n\n")
print("Posetive Index: ")
print(a[0])       ## Result = `['Dhaka', 'Savar', 'Ghazipur']`
print(a[1])       ## Result = `Khulna`
print(a[3])       ## Result = `['Chittagong', 'Cox's Bazar', 'Rangamati']`
print(a[6])       ## Result = `Mymensingh`

print("\n\n")
print("Negative Index: ")
print(a[-3])       ## Result = `Rangpur`
print(a[-5])       ## Result = `['Chittagong', 'Cox's Bazar', 'Rangamati']`
print(a[-7])       ## Result = `Khulna`
print(a[-8])       ## Result = `['Dhaka', 'Savar', 'Ghazipur']`

print("\n\n")
print("Posetive Nested Index: ")
print(a[0][0])       ## Result = `Dhaka`
print(a[0][1])       ## Result = `Savar`
print(a[0][2])       ## Result = `Ghazipur`

print("\n\n")
print("Negative Nested Index: ")
print(a[-8][-1])     ## Result = `Ghazipur`
print(a[-8][-2])     ## Result = `Savar`
print(a[-8][-3])     ## Result = `Dhaka`






##! ===========================================================================================
##! ===============================(+  User Input  +)==========================================

##? Formula 1 :-
my_list = []

n = int(input("How many items you want to add on your list? = "))  ## If you gibe here `5`

for i in range(n):
    value = input(f"Give your {i+1} item value =") ## If You give value like `Dhaka, Rajshahi, Barishal , Khulna, Chittagong`
    my_list.append(value)

print("My List is: ", my_list)  ## My List is:  ['Dhaka', 'Rajshahi', 'Barishal ', 'Khulna', 'Chittagong']



##? Formula 2 :-
input_data = input("Give your items using spaces: ")  ## If given input like: `Dhaka Barisan Khulna Rajshahi`

my_list = input_data.split()

print("My List is: ", my_list) ## My List is:  ['Dhaka', 'Barisan', 'Khulna', 'Rajshahi']


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

print(my_list)




"""
##! ===========================================================================================
##! ===============================(+  List Method  +)=========================================
"""

##? Method 1: ------( Append, Extend, Insert Methods )---------------
##? Add Value Into a List 

fruits = ["Apple", "Banana", "Orange"]

##TODO## Formula 1 ( Append ):-
"""
    => একটা একটা করে Data add করার জন্যে ব্যবহার করা হয়।
"""
fruits.append("Grapes") 
print(fruits)  ## Result = `['Apple', 'Banana', 'Orange', 'Grapes']`



##TODO## Formula 2 ( Extend ):-
"""
    => অনেক গুলো Data একসাথে Add করার জন্যে ব্যবহার করা হয়।
"""
fruits.extend(["Grapes","Guava", "Watermelon", "Pineapple"])
print(fruits)  ## Result = `['Apple', 'Banana', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple']`



##TODO## Formula 3 ( Insert ) :-
"""
    => যদি List এর কোন নির্দিষ্ট স্থানে কোন Value add করতে চাই তবে এটি আমরা ব্যবহার করতে পারি। 
"""
fruits.insert(1, "Guava") ## Hser, 1 is index and "Guava" is value

print(fruits)  ## Result = `['Apple', 'Guava', 'Banana', 'Orange']`


##? ----------------------------------------------------------------------
##? Change/Modify Value Into a List 

fruits = ["Apple", "Banana", "Orange"]

##TODO##   Example 1:
fruits[1] = "Guava"
print(fruits)


##TODO##   Example 2:
input_index = int(input("Give a index number to the item value: "))    ## If give 1
# input_value = input("Give a value to add on this ixdex position: ")  ## If give `Guava`

if (input_index > (len(fruits)-1)) or (input_index < 0):
    print("Error: Invalid Index Number!")

else:
    input_value = input("Give a value to add on this ixdex position: ")  ## If give `Guava`
    fruits[input_index] = input_value
    print(fruits)     ## Result = `['Apple', 'Guava', 'Orange']`


##TODO##   Example 3:
input_value = input("Given a value, which one you want to change? :")  ## If give `Banana`

search_flag = False

for index,fruit in enumerate(fruits):
    if input_value == fruit:
        input_new_value = input("Given a new value for add on your list :")  ## If value set `Guava`
        fruits[index] = input_new_value
        search_flag = True
        break
    else:
        search_flag = False


if search_flag == True:
    print("New List: ",fruits)    ## Result = `['Apple', 'Guava', 'Orange']`
else:        
    print("Error: Your input value not found!")




##? Method 2: --------------( Del, Remove, Pop, Clear Methods)-------------------------
##? Delete Value Item

fruits = ['Apple', 'Banana', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple']

##TODO## Formula 1 ( Del ):-
"""
    => List এর index ধরে Remove কতে চাইলে।
"""
del fruits[1]

print(fruits) ## Result = `['Apple', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple']`


del fruits[1:4]

print(fruits) ## Result = `['Apple', 'Guava', 'Watermelon', 'Pineapple']`


##TODO## Formula 2 ( Remove ):-
"""
    => Item এর Value ধরে Delete করতে চাইলে এটি ব্যবহার করা যায়। একাধিক Item Remove করা যায় না।
"""
fruits.remove("Banana")  

print(fruits) ## Result = `['Apple', 'Orange', 'Grapes', 'Guava', 'Watermelon', 'Pineapple']`



##TODO## Formula 3 ( Pop ):-
"""
    => Item এর শেষ Value কে Delete করে দেয়। তবে এর দ্বারা Index এর ভিতিতেও Delete করা যায়।
"""
fruits.pop()
print(fruits) ## Result = `['Apple', 'Banana', 'Orange', 'Grapes', 'Guava', 'Watermelon']`

fruits.pop(2)
print(fruits) ## Result = `['Apple', 'Banana', 'Grapes', 'Guava', 'Watermelon', 'Pineapple']`



##TODO## Formula 3 ( Clear ):-
"""
    => পুর List এর সকল Values গুলো কে Delete করে দিতে চাইলে আমরা Clear Method টি ব্যবহার কোরবো।
"""
fruits.clear()
print(fruits) ## Result = `[]`



##? ---------------------------------------------------------------------
##? Retrieve List Values

divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]

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


divisions = [["Dhaka", "Savar", "Ghazipur"], "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]


for division in divisions:

    if type(division)  is list:
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


divisions = [["Dhaka", "Savar", "Ghazipur"], "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]

"""##NOTE:- Structure of `divisions` index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            [[                  ], "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]
##! Index          -8                  -7        -6             -5                    -4        -3          -2          -1
#               "Dhaka",   (0,0)/(-8,-3)                   "Chittagong",   (3,0)/(-8,-3)       
#               "Savar",   (0,1)/(-8,-2)                   "Cox's Bazar",  (3,1)/(-8,-2)
#               "Ghazipur" (0,2)/(-8,-1)                   "Rangamati",    (3,2)/(-8,-1)
#            
"""

for d_index, division in enumerate(divisions):

    if type(division)  is list:
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
        Division Name: Barishal | Index: 7
"""

length = len(divisions)
print("Length =", length)  ## Result = `8`



##? Method 3: --------------( Copy Method )-------------------------
"""
    => copy method এর সাহায্যে আমরা কোন List কে Copy করতে পারি, 
       এমন কি এর এর ভেতরে থাক Nested List টি কে ও আমরা Copy করতে পরি।
"""
divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]

copy_list = divisions.copy()
print("Copy List: ", copy_list) ## Copy List: ['Dhaka', 'Khulna', 'Sylhet', 'Chittagong', 'Rajshahi', 'Rangpur', 'Mymensingh', 'Barishal ']


divisions = [["Dhaka", "Savar", "Ghazipur"], "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]

"""##NOTE:- Structure of `divisions` index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            [[                  ], "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]
##! Index          -8                  -7        -6             -5                    -4        -3          -2          -1
#               "Dhaka",   (0,0)/(-8,-3)                   "Chittagong",   (3,0)/(-8,-3)       
#               "Savar",   (0,1)/(-8,-2)                   "Cox's Bazar", (3,1)/(-8,-2)
#               "Ghazipur"  (0,2)/(-8,-1)                   "Rangamati",   (3,2)/(-8,-1)
#            
"""

citys = []

for division in divisions:
    if type(division) is list:
        citys = division.copy()
        break


print("Citys :", citys)    ## Result = `['Dhaka', 'Savar', 'Ghazipur']`


##? Method 4: --------------( Index Method )-------------------------
"""
    => index method এর সাহায্যে আমরা কোন List এর Value দেয়ার মাধ্যমে তার Index জনতে পারি। 
       প্রথমে জকে পাবে, তার Index সে দেখাবে, পরের Item এর Index কে সে আর দেখাবে না।

       NOTE:- Nested List এর ক্ষত্রে এটা কাজ কোরবে না। সেই ক্ষেত্রে Menual নিয়বে কোরতে হবে।
"""

divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", "Rajshahi"]

inpute_value = input("Given a name which one index you want to know? :") ## If give :Rajshahi

try:
    index_no = divisions.index(inpute_value)
    print(f"{inpute_value} index no: {index_no}")  ## Result = `Rajshahi index no: 4`

except Exception as e:
    print(f"Error: {e}")


divisions = [["Dhaka", "Savar", "Ghazipur"], "Khulna", "Sylhet", ["Chittagong", "Cox's Bazar", "Rangamati", ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]

"""##NOTE:- Structure of `divisions` index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            [[                  ], "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]
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

    if type(division)  is list:
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
    => List এর ভতের কতগুলো Item আছে তা বের করে দেয়।

       NOTE:- Nested List এর ক্ষত্রে এটা কাজ কোরবে না। সেই ক্ষেত্রে Menual নিয়মে কোরতে হবে।
"""

divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Dhaka", ["Saver", "Dhaka", "Ghazipur"], "Mymensingh", "Dhaka", "Sylhet"]

elements = divisions.count("Sylhet")
print("Total elements =", elements)  ## Result = `Total elements = 3`


elements = divisions.count("Dhaka") ##! `Dhaka` মোট 4 বার আছে, কিন্তু এখানে 3 বার দেখবে। Nested List কাজ কোরবে না।
print("Total elements =", elements)  ## Result = `Total elements = 3`


##! Nested List এর ক্ষত্রে এটি বের করার জন্যে আমাদের Munually করতে হবে।

inpute_value = input("Given a name which one index you want to know? :") ## If give :Rajshahi Else If give :Cox's Bazar

total_count = 0

search_flag = False

for d_index, division in enumerate(divisions):

    if type(division)  is list:
        for c_index, city in enumerate(division):
            if inpute_value == city:
                total_count+=1
                search_flag = True
    else:
        if inpute_value == division:
            total_count+=1
            search_flag = True

if search_flag == True:
    print(f"Total `{inpute_value}`, have in our list= {total_count}") 
else:        
    print(f"Error: Your input value `{inpute_value}` not found!")



##? Method 6: --------------( Reverse Method )-------------------------

divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", "Rajshahi"]

divisions.reverse()

print(divisions) ## Results = `['Rajshahi', 'Barishal ', 'Mymensingh', 'Rangpur', 'Rajshahi', 'Chittagong', 'Sylhet', 'Khulna', 'Dhaka']`



##? Method 6: --------------( Sort Method )-------------------------
"""
    => এখনে ASCII অনুসারে Sort করে। By Default Ascending Order এ Sort হয়, তবে `sort(reverse=True)`
       কোরলে Descending Order এ Sort করবে।
"""

divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", "Rajshahi"]

##! Order by Ascending order
divisions.sort()
print("After Sort Divisions: ",divisions) 
"""Result =
    => ['Barishal ', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rajshahi', 'Rangpur', 'Sylhet']
"""


income = [22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000]

income.sort()
print("After Sort Income: ",income)
"""Result =
    => [10000, 15000, 18000, 22000, 22000, 25000, 32000, 35000, 41000, 55000]
"""

##! Order by Descending order
divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", "Rajshahi"]

divisions.sort(reverse=True)
print("After Sort Divisions: ",divisions) 
"""Result =
    => ['Sylhet', 'Rangpur', 'Rajshahi', 'Rajshahi', 'Mymensingh', 'Khulna', 'Dhaka', 'Chittagong', 'Barishal ']
"""


income = [22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000]

income.sort(reverse=True)
print("After Sort Income: ",income)
"""Result =
    => [55000, 41000, 35000, 32000, 25000, 22000, 22000, 18000, 15000, 10000]
"""


##! Order by Length
#NOTE:- Integer এর কোন Length হয় না, তাই এটিকে key=len এর ভিতিতে Sort করা যায় না।

divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", "Rajshahi"]

divisions.sort(reverse=True, key=len)
print("After Sort Divisions: ",divisions) 
"""Result =
      => ['Chittagong', 'Mymensingh', 'Sylhet', 'Rajshahi', 'Rangpur', 'Barishal ', 'Rajshahi', 'Khulna', 'Dhaka']
#* Length:    9            9            7          7          7          7          7          6        5
"""



##? Method 7: --------------( Sorted Method )-------------------------
"""
    => Sort এবং Sorted একি, তবে Sorted করার জন্যে তা নতুন কোন Variable এ রাখতে হয়। 
"""
##! Order by Ascending order
divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", "Rajshahi"]

sorted_divisions = sorted(divisions)
print("After Sort Divisions: ",sorted_divisions) 
"""Result =
    => ['Barishal ', 'Chittagong', 'Dhaka', 'Khulna', 'Mymensingh', 'Rajshahi', 'Rajshahi', 'Rangpur', 'Sylhet']
"""


income = [22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000]

sorted_income = sorted(income)
print("After Sort Income: ",sorted_income)
"""Result =
    => [10000, 15000, 18000, 22000, 22000, 25000, 32000, 35000, 41000, 55000]
"""

##! Order by Descending order
divisions = ["Dhaka", "Khulna", "Sylhet","Chittagong", "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", "Rajshahi"]

sorted_divisions = sorted(divisions, reverse=True)
print("After Sort Divisions: ",sorted_divisions) 
"""Result =
    => ['Sylhet', 'Rangpur', 'Rajshahi', 'Rajshahi', 'Mymensingh', 'Khulna', 'Dhaka', 'Chittagong', 'Barishal ']
"""


income = [22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000]

sorted_income = sorted(income, reverse=True)
print("After Sort Income: ",sorted_income)
"""Result =
    => [55000, 41000, 35000, 32000, 25000, 22000, 22000, 18000, 15000, 10000]
"""



##? Method 8: --------------( Max, Min and Sum Method )-------------------------
"""
    => একটি List এর Max, Min and Summation বের করার জন্যে এই Method গুলো ব্যবহার করা হয়।
"""
## Example 1:-
income = [22000, 32000, 10000, 15000, 25000, 22000, 41000, 55000, 18000, 35000]

max_value = max(income)
min_value = min(income)
min_value = sum(income) ##NOTE:- List এর ভেলু গুলো Mustbe Integer or Float হতে হবে।


print("List Max Value: ",max_value)   ## Result = `55000`
print("List Min Value: ",min_value)   ## Result = `10000` 
print("List Sum: ",min_value)         ## Result = `275000` 


## Example 2:-
fruits = ["cucumber", "benana", "apple", "Watermelon", "Pianapple", "Orange", "Guava"]

"""
##! ASCII       c = 99     b = 98    a = 97    W = 87        P = 80      O = 79    G = 71
## List      ["cucumber", "benana", "apple", "Watermelon", "Pianapple", "Orange", "Guava"]
"""

max_value = max(fruits)
min_value = min(fruits)

print("List Max Value: ",max_value)   ## Result = `cucumber`
print("List Min Value: ",min_value)   ## Result = `Guava`



##? Method 9: --------------( Zip Method )-------------------------
"""
    => এর সাহায্যে দুটি List কে একসাথে নিয়ে Nested List তৈরি করে।
"""


name = ["Rakib", "Hassan", "Ratul", "Sabbir", "Omor", "Ovi"]
age  = [26, 24, 27, 25, 29, 30]

new_list = list(zip(name, age))

print("New list: ", new_list)

"""Result:
    => [('Rakib', 26), ('Hassan', 24), ('Ratul', 27), ('Sabbir', 25), ('Omor', 29), ('Ovi', 30)]
"""



##! ===========================================================================================
##! ===============================(+  Some Exercise  +)======================================

##? Question 1:- Take a user input(list) and swap the first and last elements
"""Example:-
    input  = 12   35   9   56   24
    output = 24   35   9   56   12
"""

input_list = list(map(int, input("Enter some number :").split()))

print("Input :", input_list)  ## Input : [12, 35, 9, 56, 24]

#TODO# Alternative Way
length = len(input_list)

temp = input_list[0]
input_list[0] = input_list[length-1]
input_list[length-1] = temp

#TODO# Alternative Way
input_list[0], input_list[length-1] = input_list[length-1], input_list[0]

#TODO# Alternative Way (Without length)
input_list[0], input_list[-1] = input_list[-1], input_list[0]

print("Output :", input_list)  ## Output : [24, 35, 9, 56, 12]



##? Question 2:- Take a user input(list) and make all elements into Upper case.
"""Example:-
    input  = apple   banana   orange   
    output = Apple   Banana   Orange
"""


input_datas = list(input("Enter some number :").split()) ## Input : apple banana orange

print("Input :", input_datas) ## Input : ['apple', 'banana', 'orange']

output_list = []

for data in input_datas:
    output_list.append(data.upper())

print("Output :", output_list)  ## Output : ['APPLE', 'BANANA', 'ORANGE']



##? Question 3:- User থেকে একটি List ইনপুট নও। তারা পাশা পাশি আর দুটি ইনপুট নেও একটি যে Items 
#?              কে তুমি Replace করতে চাও এবং অন্যটি কি দিয়ে তুমি তা Replace করতে চাও। 
"""Example:-
    Input  : ['apple', 'banana', 'orange', 'pinnapple']   
    value1 = orange
    value2 = guava  

    Output : ['apple', 'banana', 'guava', 'pinnapple']
"""

input_datas = list(input("Enter some number :").split()) ## apple banana orange pinnapple

value1 = input("Which value you want to replace :") ## orange
value2 = input("Given new value :")  ## guava

print("Input :", input_datas)  ## Input  : ['apple', 'banana', 'orange', 'pinnapple']

for index, value in enumerate(input_datas):
    
    if value == value1:
        input_datas[index] = value2

print("Output :", input_datas)   ## Output : ['apple', 'banana', 'guava', 'pinnapple']


#TODO# Alternative Way:-
new_list = list(
                map(
                    (lambda x:x.replace(value1, value2)), input_datas
                )
            )
print("Output :", new_list)   ## Output : ['apple', 'banana', 'guava', 'pinnapple']