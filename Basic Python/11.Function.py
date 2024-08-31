"""
##! Syntax Of A Function
    
    def <Function_Name>():
        
        -- Your Extension --


    NOTE:- `def` Means `Definition of a Function`

##! Call a Function

    <Function_Name>()

"""
##? Example 1:- A simple function define,

def summation():
    a = 10
    b = 12
    print(a + b)


## Now call this function
summation()




##? Example 2:- If a function `return`,

def summation():
    a = 10
    b = 12
    print(a + b)
    return a + b

## Now call this function
result = summation()
print(result) ## 22



##? Example 3:- If a function accepts parameters

def summation(num1, num2):
    a = num1
    b = num2
    
    print(a + b)

## Now call this function
summation(10, 12)


##? Example 4:- If a function accepts parameters and return

def summation(num1, num2):
    a = num1
    b = num2
    
    return a + b

## Now call this function
result = summation(10, 12)
print(result) ## 22



##? Example 5:- If a pass Keyword Arguments into a function

def person_card(name, phone, email):
    
    return f"Name:{name}, Phone:{phone}, Email:{email}"


## Now call this function
input_name = input("Enter Your Name :")    ## IF Give :Md Rakib Hassan
input_phone = input("Enter Your Phone :")  ## IF Give :01515612682
input_email = input("Enter Your Email :")  ## IF Give :rakib1515hassan@gmail.com

info = person_card(name=input_name, email=input_email, phone=input_phone)
print("Person Info,", info)
""" Print Result:
    => Person Info, Name:Md Rakib Hassan, Phone:01515612682, Email:rakib1515hassan@gmail.com
"""


##? Example 6:- If pass Keyword Arguments in to function with (Input Validation)
"""
    => If not use email=None, then face 
    `TypeError: person_card() missing 1 required positional argument: 'email'`
"""

def person_card(name, phone, email=None):
    
    if email:
        return f"Name:{name}, Phone:{phone}, Email:{email}"
    return f"Name:{name}, Phone:{phone}"



## Now call this function
while True:
    input_name = input("Enter Your Name :")    ## IF Give :Md Rakib Hassan
    if len(input_name)<= 2:
        print("Error: Name must be at least 2 characters!")
        continue
    break


while True:
    input_phone = input("Enter Your Phone :")  ## IF Give :01515612682
    if (len(input_phone) < 11) or (len(input_phone) >14):
        print("Error: Phone number must be between 11 and 14 digits!")
        continue
    if not input_phone.startswith("01"):
        print("Error: Phone number start with 01.")
        continue
    break


while True:
    input_email = input("Enter Your Email :")  ## IF Give :rakib1515hassan@gmail.com
    if input_email != '':
        if (input_email.count("@")) != 1:
            print("Error: Please give a valid email address.")
            continue

    break

info = ''

if (input_email != ''):
    info = person_card(name=input_name, email=input_email, phone=input_phone)
else:
    info = person_card(name=input_name, phone=input_phone)

print("Person Info,", info)
""" Print Result:
    If Email:
        => Person Info, Name:Md Rakib Hassan, Phone:01515612682, Email:rakib1515hassan@gmail.com
    Else:
        => Person Info, Name:Md Rakib Hassan, Phone:01515612682
"""



##! ---------------------------------------------------------------------------------
##! -------------------( Default Parameter in Function )-----------------------------
"""
    => Function এর ভতর যদি কোন Parameter এর Value দেয়া থাকে তবে তাকে Default Parameter
       বলে। যদি Argument হসেবে কোন কিছু না Pass করা হয়, তবে সে Default value কে সে নিয়ে নেয়।
"""

def nid_card(name, phone, email=None, age=18):
    
    if email:
        return f"Name:{name}, Phone:{phone}, Email:{email}, Age:{age}"
    return f"Name:{name}, Phone:{phone}, Age:{age}"


## Now call this function
##? Object 1:-
person1 = nid_card(
    name = "Md Rakib Hassan",
    phone = "01515612682",
    email = "rakib1515hassan@gmail.com",
    age = 26
) 

print(f"Person 1 Info, {person1}") 
## Person 1 Info, Name:Md Rakib Hassan, Phone:01515612682, Email:rakib1515hassan@gmail.com, Age:26

##? Object 2:-
person2 = nid_card(
    name = "Mohammed Hassan",
    phone = "01680764592",
    age = 27
) 

print(f"Person 2 Info, {person2}") 
## Person 2 Info, Name:Mohammed Hassan, Phone:01680764592, Age:27


##? Object 1:-
person3 = nid_card(
    name = "Mr Rakib",
    phone = "01680764591",
    email = "rakib15-8123@diu.edu.bd"
) 

print(f"Person 3 Info, {person3}") 
## Person 3 Info, Name:Mr Rakib, Phone:01680764591, Email:rakib15-8123@diu.edu.bd, Age:18




##! ---------------------------------------------------------------------------------
##! ----------------------------( *args in Function )--------------------------------
"""
=>##* `args` means Arbitrary Positional Arguments

    i) *args / Asterisk(*) Parameter হল এমন একটি Parameter যার সাহায্যে আমরা একাধিক
       arguments  কে Functions এর ভেতর Receive করতে পারি।

    ii) এটি মূলত Argument কে Tuple হিসেবে Store করে।
"""
##? Example 1:-
def shop(*args):
    
    print(*args) 

## Now call this function
shop("Frout Shop", "Book Shops", "Sports Shop")
# Result = `Frout Shop Book Shops Sports Shop`




##? Example 2:-
def shop(*names):
    
    for index, name in enumerate(names):
        print(f"Shop No: {index+1}, Shop Name: {name}")

## Now call this function
shop("Frout Shop", "Book Shops", "Sports Shop")

"""Result:
    Shop No: 1, Shop Name: Frout Shop
    Shop No: 2, Shop Name: Book Shops
    Shop No: 3, Shop Name: Sports Shop
"""



##? Example 3:-
def person_info(*items):
    
    print("Person Information:")
    for index, item in enumerate(items):
        print(f"    {index+1}) {item}")

## Now call this function
person_info("Md Rakib Hassan", "01515612682", "rakib1515hassan@gmail.com")

"""Result:
    Person Information:
        1) Md Rakib Hassan
        2) 01515612682
        3) rakib1515hassan@gmail.com
"""

##? Example 4:-
def summation(*args):
    my_tuple = args
    s = 0

    for i in my_tuple:
        s += i

    return s


result = summation(40, 50, 20, 5, 45)
print(result)

##? Example 5:-
def summation(*args):
    my_tuple = args
    s = 0

    for i in my_tuple:
        s += i
    
    return s

def avgrage(*args):
    subjects = args

    s = 0
    for subject in subjects:
        s += subject

    l = len(subjects)

    r = s/l

    return r

"""
                  bangla + math + english + physics + chemistry
    avgrage =  __________________________________________________
                                    5
"""

bangla  = summation(80, 60, 50, 56, 45, 49, 65)
math    = summation(60, 59, 23, 50, 59)
english = summation(81, 65, 75, 85, 91, 69, 75, 12)

physics = summation(85, 52, 56, 35, 67)
chemistry = summation(44, 51, 53, 75, 69, 73)

avg = avgrage(bangla, math, english, physics, chemistry)  ## 373.8

print(avg)


##! ---------------------------------------------------------------------------------
##! -------------------------( **kwargs in Function )--------------------------------
"""
=>##* `kwargs` means Keyword Arbitrary Positional Arguments

    i) *kwargs / Asterisk(**) Parameter হল এমন একটি Parameter যার সাহায্যে আমরা একাধিক
       arguments  কে Functions এর ভেতর Receive করতে পারি।

    ii) এটি মূলত Argument কে Dictionary হিসেবে Store করে।

    iii) এটি Function এর ভতরে data কে Dictionary হিসেবে Receive করে।
"""
##? Example 1:-
def shop(**kwargs):
    print(kwargs["book_name"]) 
    print(kwargs["price"]) 
    print(kwargs["author"]) 

## Now call this function
shop( book_name = "Python Book", price = 500, author = "Md Rakib Hassan")
"""Result:
    Python Book
    500
    Md Rakib Hassan
"""


##? Example 2:-
def shop(**kwargs):
    
    for k, v in kwargs.items():
        print(f"{k} : {v}")

## Now call this function
shop( book_name = "Python Book", price = 500, author = "Md Rakib Hassan")
"""Result:
    book_name : Python Book
    price : 500
    author : Md Rakib Hassan
"""



##? Example 3:-
def shop(**kwargs):
    data = {}

    for k, v in kwargs.items():
        data[k] = v
    
    return data

## Now call this function
result = shop( book_name = "Python Book", price = 500, author = "Md Rakib Hassan")

print(result) ## {'book_name': 'Python Book', 'price': 500, 'author': 'Md Rakib Hassan'}

for k, v in result.items():

    print(f"{k}: {v}")

"""Result:
    book_name : Python Book
    price : 500
    author : Md Rakib Hassan
"""

##? Example 4:-
def profile(**kwargs):

    data = kwargs
    print(data)

p = {
    "name": "rakib",
    "id": 162,
    "group": "A",
    "city": "Dhaka"
}

profile(**p)


##? Example 5:-
def profile(a, b, *args, **kwargs):

    tuple_date = args
    dic_data = kwargs

    print(a)
    print(b)
    print(tuple_date)
    print(dic_data)


## Main function
p = {
    "name": "rakib",
    "id": 162,
    "group": "A",
    "city": "Dhaka"
}

n = (5, 6, 7, 9)

a = "Bangladesh"
b = "United States"

profile(a, b, *n, **p)


##! ---------------------------------------------------------------------------------
##! ------------------------------( Nested Functio )---------------------------------

"""
    => Nested Functio কে যদি আমরা Call করতে চাই, আর্থাৎ Function এর ভতর Function 
      থাকে এবং তাকে আমরা যদি Call করতে চাই তাহলে অবশ্যই Main Function হতে তাকে 
      Call দিতে হবে।
"""

##? Example 1:-

def calculator(num_1, operator, num_2):

    def addition():
        print(f"{num_1} + {num_2} =", num_1 + num_2)

    def subtraction():
        print(f"{num_1} - {num_2} =", num_1 - num_2)

    def multiplication():
        print(f"{num_1} * {num_2} =", num_1 * num_2)

    def division():
        print(f"{num_1} / {num_2} =", num_1 / num_2)

    if operator == "+":
        addition()
    elif operator == "-":
        subtraction()
    elif operator == "*":
        multiplication()
    elif operator == "/":
        division()
    else:
        print("Error: Wrong Operator Given!")


## Call the function
n_1 = float(input("Enter the first number :"))     ## If given :5
ope = input("Enter the operator (+, -, *, /) :")   ## If given :+
n_2 = float(input("Enter the second number :"))    ## If given :7

calculator( num_1 = n_1, operator = ope, num_2 = n_2 ) ## 5.0 + 7.0 = 12.0




##? Example 2:-

def BangladeshShop(city=None):
    mango = 100
    price = 100

    def Rajshi():
        p = mango - 20
        return p

    def Dhaka():
        p = mango + 5
        return p

    def Khulna():
        p = mango - 15
        return p

    ## Nested Function Call
    if city == None:
        return f"Mango Price in Bangladesh = {price}"
    
    if city == "Rajshi":
        price = Rajshi()

    elif city == "Dhaka":
        price = Dhaka()

    elif city == "Klulna":
        price = Khulna()

    return f"Mango in {city} = {price}"


## Call the function
customer_1 = BangladeshShop()
print("Customer 1 buy ", customer_1) ## Customer 1 buy  Mango Price in Bangladesh = 100

customer_2 = BangladeshShop(city="Dhaka")
print("Customer 2 buy ", customer_2) ## Customer 2 buy  Mango in Dhaka = 105

customer_3 = BangladeshShop(city="Rajshi")
print("Customer 3 buy ", customer_3) ## Customer 3 buy  Mango in Rajshi = 80

customer_4 = BangladeshShop(city="Klulna")
print("Customer 4 buy ", customer_4) ## Customer 4 buy  Mango in Klulna = 85



##? Example 3:-
def BangladeshShop(amount ,city=None):
    mango = amount
    price = amount

    def Rajshi():
        p = mango - 20
        return p

    def Dhaka():
        p = mango + 5
        return p

    def Khulna():
        p = mango - 15
        return p

    ## Nested Function Call
    if city == None:
        return f"Mango Price in Bangladesh = {price}"
    
    if city == "Rajshi":
        price = Rajshi()

    elif city == "Dhaka":
        price = Dhaka()

    elif city == "Klulna":
        price = Khulna()

    return f"Mango in {city} = {price}"


## Call the function
customer_1 = BangladeshShop(amount=100)
print("Customer 1 buy ", customer_1) ## Customer 1 buy  Mango Price in Bangladesh = 100

customer_2 = BangladeshShop(amount= 100,city="Dhaka")
print("Customer 2 buy ", customer_2) ## Customer 2 buy  Mango in Dhaka = 105

customer_3 = BangladeshShop(amount= 100,city="Rajshi")
print("Customer 3 buy ", customer_3) ## Customer 3 buy  Mango in Rajshi = 80

customer_4 = BangladeshShop(amount= 100,city="Klulna")
print("Customer 4 buy ", customer_4) ## Customer 4 buy  Mango in Klulna = 85



##! ---------------------------------------------------------------------------------
##! -----------------( Global, Local and Non-local Variable )------------------------

def Bangladesh():
    apple  = 13
    orange = 10
    mango  = 7
    global benana  ##! It was Local Variable but here it make Global Variables
    benana = 6

    def Dhaka():
        city = "Dhaka"
        print(f"In {city}: apple={apple}, orange={orange}, mango={mango}, banana={benana}")
    
    def Rajshahi():
        city = "Rajshahi"
        print(f"In {city}: apple={apple}, orange={orange}, mango={mango}, banana={benana}")

    Dhaka()
    Rajshahi()
    print(f"In Bangladesh: apple={apple}, orange={orange}, mango={mango}, banana={benana}")
    print("-----------------------------------------------------------------------------")



def USA():
    print(f"In USA: apple={apple}, orange={orange}, benana={benana}")
    print("-----------------------------------------------------------------------------")


def China():
    print(f"In China: apple={apple}, orange={orange}, benana={benana}")
    print("-----------------------------------------------------------------------------")


def Europe():
    prickly_pear = 13   ##? Non Local Variables
    blackberries = 20   ##* Local Variables

    def Itali():
        country = "Itali"
        nonlocal prickly_pear  ##? Make it Non Local Variables
        prickly_pear = 15
        print(f"In {country}: apple={apple}, prickly_pear={prickly_pear}, blackberries={blackberries} banana={benana}")
    
    def Englind():
        country = "Englind"
        blackberries = 18   ##* Local Variables
        print(f"In {country}: apple={apple}, prickly_pear={prickly_pear}, blackberries={blackberries}, banana={benana}")

    Itali()
    Englind()
    print(f"In Europe: apple={apple}, orange={orange}, mango={mango}, banana={benana}, prickly_pear={prickly_pear}, blackberries={blackberries}")
    print("-----------------------------------------------------------------------------")


##! Global Variables
apple  = 10
orange = 12
mango  = 8

print(f"Global Price: apple={apple}, orange{orange}, mango={mango}")
print("-----------------------------------------------------------------------------")

Bangladesh()
USA()
China()
Europe()


"""Print Result:
    Global Price: apple=10, orange12, mango=8
    -----------------------------------------------------------------------------
    In Dhaka: apple=13, orange=10, mango=7, banana=6
    In Rajshahi: apple=13, orange=10, mango=7, banana=6
    In Bangladesh: apple=13, orange=10, mango=7, banana=6
    -----------------------------------------------------------------------------
    In USA: apple=10, orange=12, #!benana=6
    -----------------------------------------------------------------------------
    In China: apple=10, orange=12, #!benana=6
    -----------------------------------------------------------------------------
    In Itali: apple=10, prickly_pear=15, #?blackberries=20 banana=6
    In Englind: apple=10, prickly_pear=15, #?blackberries=18, banana=6
    In Europe: apple=10, orange=12, mango=8, banana=6, prickly_pear=15, blackberries=20
    -----------------------------------------------------------------------------
"""



##! ---------------------------------------------------------------------------------
##! -----------------------( Instend of return [ yield ] )---------------------------
"""
    => এটি মূলত Use করা হয় Loop এর ভেতরে, অনেগুলো Return একসাথে কারর জন্যে।
"""
def Bangladesh():
    return "Dhaka"
    return "Borisal"
    return "Khulna"
    return "Chittagong"
    return "Rajshai"

for i in Bangladesh():
    print(Bangladesh())
"""Print Result =
    Dhaka
    Dhaka
    Dhaka
    Dhaka
    Dhaka
"""


def Bangladesh():
    print("Dhaka")
    print("Borisal")
    print("Khulna")
    print("Chittagong")
    print("Rajshai")

count = 0
for i in Bangladesh():
    print(i)
    count += 1

print("Count = ", count)
"""Print Result =
    Dhaka
    Borisal
    Khulna
    Chittagong
    Rajshai
    Traceback (most recent call last):
    File "Z:\Python\Basic Python\test.py", line 29, in <module>
        for i in Bangladesh():
    TypeError: 'NoneType' object is not iterable
"""



def Bangladesh():
    yield "Dhaka"
    yield "Borisal"
    yield "Khulna"
    yield "Chittagong"
    yield "Rajshai"

count = 0
for i in Bangladesh():
    print(i)
    count += 1

print("Count = ", count)
"""Print Result =
    Dhaka
    Borisal
    Khulna
    Chittagong
    Rajshai
    Count =  5
"""

def digit():
    for i in range(0, 5):
        return i

for i in digit():
    print(i)
"""Print Result =
    Traceback (most recent call last):
    File "Z:\Python\Basic Python\test.py", line 61, in <module>
        for i in digit():
    TypeError: 'int' object is not iterable
"""

def digit():
    for i in range(0, 5):
        yield i

for i in digit():
    print(i)
"""Print Result =
    0
    1
    2
    3
    4
"""



##! ---------------------------------------------------------------------------------
##! ------------------------------( Some Math )--------------------------------------


"""##! Finite Series ( সসীম ধারা ) :- 

    ##* Arithmetic Series (সমান্তর ধারা):-
    কোন ধারার যেকোন পদ ও তার পূর্ববতী পদের পার্থক্য যদি সবসময় সমান হয় তবে তাকে সমান্তর ধারা বলে।
    => 1 + 3 + 5 + 7 + 9 + 12 .............. + n

    প্রথম পদ  a = 1
    দ্বিতীয় পদ b = 3

    সাধারন অন্তর (পদ ব্যবধান) d = b - a = 3 - 1 = 2

    n তম পদ/ সাধারন পদ = a + (n-1)/d

    শেষ পদকে p দ্বারা প্রকাশ করা হয়।

    সমান্তর ধারার n তম পদের সমষ্টি s = (n/2) * (2a + (n-1)/d)
"""

##? Example 1:- 5 + 8 + 11 + 14 + ........ ধারার কোন পদ 383?

## n_th means, n তম পদ
def n_th(first_value, second_value ,n_value):
    diff = (second_value - first_value)

    return ( (n_value - first_value + diff) / diff )

a = 5
b = 8

## n তম পদ এর মান দেয়া আছে 383
n_value = 383

result = n_th(a, b, n_value)
print(result) ## Result = 127



##? Example 2:- 1 + 2 + 3 + 4 + ........+ 99 = কত ?
## n তম পদের সমষ্টি
def n_th_value_sum(first_value, second_value, n_th):
    diff = second_value - first_value
    summation_of_nth_value = (n_th/2) * ((2*first_value) + ((n_th-1) * diff))
    return summation_of_nth_value

## n_th means, n তম পদ, এর value কে `n_value` দ্বারা প্রকাশ করা হয়
def n_th(first_value, second_value ,n_value):
    diff = (second_value - first_value)
    return ( (n_value - first_value + diff) / diff )


## Call the function
a = 1
b = 2
p = 99 ## শেষ value, যাকে n_value হিসেবে ধরে নেয়া হয়েছে

n = n_th(a, b, p)
print("n তম পদ =", n)  ## n তম পদ = 99

sum = n_th_value_sum(a, b, n)
print("n তম পদ এর সমষ্টি =", sum) ## n তম পদ এর সমষ্টি = 4950.0



##? Example 3:- 7 + 12 + 17 + ........ধারাটির 30 টি পদের সমষ্টি কত ?
## n তম পদের সমষ্টি
def n_th_value_sum(first_value, second_value, n_th):
    diff = second_value - first_value
    summation_of_nth_value = (n_th/2) * ((2*first_value) + ((n_th-1) * diff))
    return summation_of_nth_value


## Call the function
a = 7
b = 12
n = 30

sum = n_th_value_sum(first_value=a, second_value=b, n_th=n)
print("n তম পদ এর সমষ্টি =", sum) ## n তম পদ এর সমষ্টি = 2385.0