"""Syntax of Dictionary Data Type:

    => Generally `{` দিয়ে শুরু হবে এবং `}` দিয়ে শেষ হবে। `{}` এর ভেতর Key এবং Value থাকবে।

    Ex:- 
    a = {  
        "key_1": "value_1",
        "key_2": "value_2",
        "key_3": "value_3",
    }

"""

capital_city = {
    "Bangladesh": "Dhaka",
    "Rashia"    : "Mosko",
    "Chin"      : "Baiging",
    "India"     : "Dillhi",
    "Pakisthan" : "Islamabad",
    "Briten"    : "London",
    "Saudiarab" : "Riad",
}

print(capital_city) ## Result = `{'Bangladesh': 'Dhaka', 'Rashia': 'Mosko', 'Chin': 'Baiging', 'India': 'Dillhi', 'Pakisthan': 'Islamabad', 'Briten': 'London', 'Saudiarab': 'Riad'}`

print("Type of `a` =", type(capital_city))   ##* Type of `a`    = <class 'dict'>

print(capital_city.get("Bangladesh"))  ## Result = `Dhaka`

print(capital_city.keys())  
""" Print Result =
    => dict_keys(['Bangladesh', 'Rashia', 'Chin', 'India', 'Pakisthan', 'Briten', 'Saudiarab'])
"""
print(capital_city.values())  
""" Print Result =
    => dict_values(['Dhaka', 'Mosko', 'Baiging', 'Dillhi', 'Islamabad', 'London', 'Riad'])
"""

print(capital_city.items())  
""" Print Result =
    => dict_items([
        ('Bangladesh', 'Dhaka'), 
        ('Rashia', 'Mosko'), 
        ('Chin', 'Baiging'), 
        ('India', 'Dillhi'), 
        ('Pakisthan', 'Islamabad'), 
        ('Briten', 'London'), 
        ('Saudiarab', 'Riad')
    ])
"""

##! ===========================================================================================
##! =============================(+  Nested Dictionary  +)=====================================

persone = {
    "name": "Md Rakib Hassan",
    "age" : 26,
    "date_of_birth" : "20 Oct 1998",
    "parents"  : ("Md Shahjahan Mia", "Mrs. Rashida Bagum"),
    "fev_game" : ["Cricket", "Football", "Badmintons"],
    "address"  : {"division":"Chitogong", "distic":"Chandpur", "thana":"Hazigong", "gram": "Pirozpur Bazer"},
}

print(persone) 

"""Result =
    => {
        'name': 'Md Rakib Hassan', 
        'age' : 26, 
        'date_of_birth': '20 Oct 1998', 
        'parents': (
            'Md Shahjahan Mia', 
            'Mrs. Rashida Bagum'
        ), 
        'fev_game': [
            'Cricket', 
            'Football', 
            'Badmintons'
        ], 
        'address': {
            'division': 'Chitogong', 
            'distic'  : 'Chandpur', 
            'thana': 'Hazigong', 
            'gram' : 'Pirozpur Bazer'
        }
    }
"""

print("\n")
print("Persone Name :", persone['name'])  ## Result = `Persone Name : Md Rakib Hassan`
print("Persone age :", persone['age'])    ## Result = `Persone age : 26`
print("Persone Date of Birth :", persone['date_of_birth']) ## Result = `Persone Date of Birth : 20 Oct 1998`

print("\n")
print("Parents Name: ")         ## Result = `Parents Name:`
print(persone['parents'][0])    ## Result = `Md Shahjahan Mia`
print(persone['parents'][1])    ## Result = `Mrs. Rashida Bagum`

print("\n")
print("Fevorite Games: ")       ## Result = `Fevorite Games:`
print(persone['fev_game'][0])   ## Result = `Cricket`
print(persone['fev_game'][1])   ## Result = `Football`
print(persone['fev_game'][2])   ## Result = `Badmintons`

print("\n")
print("Address: ")                                   ## Result = `Address:`
print("Division =", persone['address']['division'])  ## Result = `Division = Chitogong`
print("Distic =", persone['address']['distic'])      ## Result = `Distic = Chandpur`
print("Thana =", persone['address']['thana'])        ## Result = `Thana = Hazigong`
print("Gram =", persone['address']['gram'])          ## Result = `Gram = Pirozpur Bazer`

##? -------------(+ Get Method +)----------------------------
## Get Method এর ভেতরে Dictionary key peramiter টি Pass কোরলে তা Value Return করে।
print("\n")
print(persone.get("name"))     ## Result = `Md Rakib Hassan`
print(persone.get("parents"))  ## Result = `('Md Shahjahan Mia', 'Mrs. Rashida Bagum')`
print(persone.get("fev_game")) ## Result = `['Cricket', 'Football', 'Badmintons']`
print(persone.get("address"))  ## Result = `{'division': 'Chitogong', 'distic': 'Chandpur', 'thana': 'Hazigong', 'gram': 'Pirozpur Bazer'}`

##? -------------(+ Keys Method +)----------------------------
print("\n")
for key in persone.keys():
    print(key)

"""Print Result =
    name
    age
    date_of_birth
    parents
    fev_game
    address
"""

##? -------------(+ Values Method +)----------------------------
print("\n")
for V in persone.values():

    if (type(V) != tuple) and (type(V) != list) and (type(V) != dict):
        print(V)

    if type(V) == tuple:
        print("\n")
        for v in V:
            print("Parents Name: ") 
            print(v)

    if type(V) == list:
        print("\n")
        print("Fevorite Games: ")
        for v in V:
            print(v)


    if type(V) == dict:
        print("\n")
        print("Address: ")  
        for v in V.values():
            print(v)

"""Print Result =
        Md Rakib Hassan
        26
        20 Oct 1998

        Parents Name:
        Md Shahjahan Mia
        Parents Name:
        Mrs. Rashida Bagum

        Fevorite Games:
        Cricket
        Football
        Badmintons

        Address:
        Chitogong
        Chandpur
        Hazigong
        Pirozpur Bazer
"""

# ##? -------------(+ Items Method +)----------------------------

print("\n")
for K, V in persone.items():

    if (type(V) != tuple) and (type(V) != list) and (type(V) != dict):
        print(f"{K} =", V)

    if type(V) == tuple:
        print("\n")
        print("Parents Name: ") 
        for v in V:
            print(v)

    if type(V) == list:
        print("\n")
        print("Fevorite Games: ")
        for v in V:
            print(v)


    if type(V) == dict:
        print("\n")
        print("Address: ")  
        for k,v in V.items():
            print(f"{k} =", v)

""" Print Result =
        name = Md Rakib Hassan
        age = 26
        date_of_birth = 20 Oct 1998


        Parents Name:
        Md Shahjahan Mia
        Mrs. Rashida Bagum


        Fevorite Games:
        Cricket
        Football
        Badmintons


        Address:
        division = Chitogong
        distic = Chandpur
        thana = Hazigong
        gram = Pirozpur Bazer
"""

##! Using Constructor to define a Dictionary

students = dict({
    1 : {"name": "Mohammed Hassan",  "age":20, "gender": "Male"  },
    2 : {"name": "Mohammed Hossain", "age":20, "gender": "Male"  },
    3 : {"name": "Md Sabbir Ahmed",  "age":25, "gender": "Male"  },
    4 : {"name": "Anika",            "age":26, "gender": "Female"},
    5 : {"name": "Sabhia Coity",     "age":25, "gender": "Female"},
    6 : {"name": "Md Rubel Hossain", "age":24, "gender": "Male"  }
})

print(f"Student 1 Info, Name :{students[1]['name']}, Age :{students[1]['age']}, Gender :{students[1]['gender']}",)
print(f"Student 2 Info, Name :{students[2]['name']}, Age :{students[2]['age']}, Gender :{students[2]['gender']}",)
print(f"Student 3 Info, Name :{students[3]['name']}, Age :{students[3]['age']}, Gender :{students[3]['gender']}",)
print(f"Student 4 Info, Name :{students[4]['name']}, Age :{students[4]['age']}, Gender :{students[4]['gender']}",)
print(f"Student 5 Info, Name :{students[5]['name']}, Age :{students[5]['age']}, Gender :{students[5]['gender']}",)
print(f"Student 6 Info, Name :{students[6]['name']}, Age :{students[6]['age']}, Gender :{students[6]['gender']}",)

"""Print Result =
        Student 1 Info, Name :Mohammed Hassan, Age :20, Gender :Male
        Student 2 Info, Name :Mohammed Hossain, Age :20, Gender :Male
        Student 3 Info, Name :Md Sabbir Ahmed, Age :25, Gender :Male
        Student 4 Info, Name :Anika, Age :26, Gender :Female
        Student 5 Info, Name :Sabhia Coity, Age :25, Gender :Female
        Student 6 Info, Name :Md Rubel Hossain, Age :24, Gender :Male
"""

for key in students:
    print(key)

"""Print Result =
    1
    2
    3
    4
    5
    6
"""
##? -------------(+ Get Method +)----------------------------
print(persone.get(3))     ## Result = `{"name": "Md Sabbir Ahmed", "age":25, "gender": "Male"  }`


##? -------------(+ Keys Method +)----------------------------
print("\n")
for key in students.keys():
    print(key)

"""Print Result =
    1
    2
    3
    4
    5
    6
"""

##? -------------(+ Values Method +)----------------------------
print("\n")
for student in students.values():

    if type(student) == dict:
        print(f"Name :{student['name']}, age :{student['age']}, gender :{student['gender']}")

"""Print Result =
        Name :Mohammed Hassan, age :20, gender :Male
        Name :Mohammed Hossain, age :20, gender :Male
        Name :Md Sabbir Ahmed, age :25, gender :Male
        Name :Anika, age :26, gender :Female
        Name :Sabhia Coity, age :25, gender :Female
        Name :Md Rubel Hossain, age :24, gender :Male
"""

##? -------------(+ Items Method +)----------------------------
print("\n")
for key, value in students.items():
    
    if type(value) == dict:
        print(f"Student {key} Info, Name :{value['name']}, age :{value['age']}, gender :{value['gender']}")

"""Print Result =
        Student 1 Info, Name :Mohammed Hassan, age :20, gender :Male
        Student 2 Info, Name :Mohammed Hossain, age :20, gender :Male
        Student 3 Info, Name :Md Sabbir Ahmed, age :25, gender :Male
        Student 4 Info, Name :Anika, age :26, gender :Female
        Student 5 Info, Name :Sabhia Coity, age :25, gender :Female
        Student 6 Info, Name :Md Rubel Hossain, age :24, gender :Male
"""


##! ===========================================================================================
##! ===============================(+  User Inpute  +)=========================================

##? Formula 1:-
person = {}

try:
    n = int(input("How many data, you want to add? :"))

    for i in range(n):
        key   = input(f"Enter {i+1} no, Key :")
        value = input(f"Enter {i+1} no, Value :")

        person.update({key:value})
        print("\n")


    print(person) ## Result = `{'name': 'Md Rakib Hassan', 'age': '26', 'date_of_birth': '20 Oct 1998'}`
    
except Exception as e:
    print("Error :", str(e))


##? Formula 2:-
person_key = {"name", "age", "city"}
person_info = dict.fromkeys(person_key)

for key in person_info:
    
    if key == "name":
        person_info["name"] = input("Enter your name: ")

    if key == "age":
        person_info["age"] = input("Enter your age: ")

    if key == "city":
        person_info["city"] = input("Enter your city: ")


print("Persone Information:")
print(person_info)  ## Result = `{'name': 'Md Rakib Hassan', 'age': '26', 'city': 'Dhaka'}`


##? Formula 3:-
person = {}

count = 1

while True:
    if count>1:
        print("if you want to stop, then write :exit")

    key   = input(f"Enter {count} no, Key :")
    if (key == None or key == '' or key =='exit'):
        break
    value = input(f"Enter {count} no, Value :")


    person.update({key:value})
    count += 1
    print("\n")


print(person)  ## Result = `{'name': 'Md Rakib Hassan', 'age': '26', 'date_of_birth': '20 Oct 1998'}`


##? Formula 4:-
person = {}

count = 1

while True:
    if count>1:
        print("if you want to stop, then write :exit")

    key   = input(f"Enter {count} no, Key :")

    if (key == None or key == '' or key =='exit'):
        break

    value = input(f"Enter {count} no, Value :")

    if type(value) == int:
        person.update({key:int(value)})

    elif type(value) == float:
        person.update({key:float(value)})
    
    elif type(value) == bool:
        person.update({key:bool(value)})
    
    elif type(value) == list:
        person.update({key:list(value)})
    
    elif type(value) == tuple:
        person.update({key:tuple(value)})
    
    elif type(value) == dict:
        person.update({key:dict(value)})

    elif type(value) == set:
        person.update({key:set(value)})
    
    else:
        person.update({key:str(value)})


    count += 1
    print("\n")


print(person)  ## Result = `{'name': 'Md Rakib Hassan', 'age': '26', 'date_of_birth': '20 Oct 1998'}`


##! ===========================================================================================
##! ===============================(+  Tuple Method  +)========================================

##? Method 1: ------( Update, setdefault Method )---------------
##? Add Value Into a Dictionary 

person = {
    "name": "Md Rakib Hassan",
    "age" : 26,
    "gender" : "Male",
}

##? Formula 1:-
person.update({"date_of_birth" : "20 Oct 1998"})
# print(person)
# print("\n")

person.update({"parents" : ("Md Shahjahan Mia", "Rashida Bagum")})
# print(person)
# print("\n")

person.update({"fev_game" : ["Cricket", "Football", "Badmintons"]})
# print(person)
# print("\n")


person.update({"address" : {"division":"Chitogong", "distic":"Chandpur", "thana":"Hazigong", "gram": "Pirozpur Bazer"}})
print(person)
# print("\n")

##? Formula 2:-
person["date_of_birth"] = "20 Oct 1998"
# print(person)
# print("\n")

person["parents"] = ("Md Shahjahan Mia", "Rashida Bagum")
# print(person)
# print("\n")

person["fev_game"] = ["Cricket", "Football", "Badmintons"]
# print(person)
# print("\n")


person["address"] = {"division":"Chitogong", "distic":"Chandpur", "thana":"Hazigong", "gram": "Pirozpur Bazer"}
print(person)
# print("\n")


##? Formula 3:-
person = {
    "name": "Md Rakib",
    "age" : 26,
    "gender" : "Male",
    "fev_game" : ["Cricket", "Football"],
    "address"  : {"division":"Chitogong", "distic":"Chandpur"},
}

person.setdefault("city")
print(person)
"""Print Result =
    {
        'name': 'Md Rakib', 
        'age': 26, 
        'gender': 'Male', 
        'fev_game': ['Cricket', 'Football'], 
        'address': {'division': 'Chitogong', 'distic': 'Chandpur'}, 
        'city': None
    }
"""


person.setdefault("city", "Dhaka")
print(person)
"""Print Result =
    {
        'name': 'Md Rakib', 
        'age': 26, 
        'gender': 'Male', 
        'fev_game': ['Cricket', 'Football'], 
        'address': {'division': 'Chitogong', 'distic': 'Chandpur'}, 
        'city': "Dhaka"
    }
"""


##? Method 2: ------( Clear, Del, Pop, Popitem Method )---------------

person = {
    "name": "Md Rakib Hassan",
    "age" : 26,
    "gender" : "Male",
    
}

##? Clear Method:- 
## NOTE:- Dictionary কে Delete করে না, কেবল Items গুলো কে Delete করে দেয়।
person.clear()
print(person)  ## Result = `{}` অর্থাত এটি Dictionary কে Delete করে না, কেবল Items গুলো কে Delete করে দেয়।


##? Del Method:- 
## NOTE:- পুরো Dictionary কে Delete করতে চাইলে,
del person
print(person)  ## NameError: name 'person' is not defined অর্থাত `person` dictionary Delete হয়ে গেছে।

## NOTE:- Dictionary, ভেতর থেকে কোন Item কে Delete করতে চাইলে,
del person['age']
print(person)  ## Result = `{'name': 'Md Rakib Hassan', 'gender': 'Male'}`


##? Pop Method:- 
person = {
    "name": "Md Rakib Hassan",
    "age" : 26,
    "gender" : "Male",
    "fev_game" : ["Cricket", "Football", "Badmintons"],
    "address"  : {"division":"Chitogong", "distic":"Chandpur", "thana":"Hazigong", "gram": "Pirozpur Bazer"},
}

## NOTE:- Dictionary, ভেতর থেকে কোন Item কে Delete করতে চাইলে এটি ব্যবহার করতে পারি।
##        তবে এখানে অবশ্যয়ি pop() এর ভেতর Argument pass করে হবে।
person.pop('age')
print(person)  ## Result = `{'name': 'Md Rakib Hassan', 'gender': 'Male', 'fev_game': ['Cricket', 'Football', 'Badmintons'], 'address': {'division': 'Chitogong', 'distic': 'Chandpur', 'thana': 'Hazigong', 'gram': 'Pirozpur Bazer'}}`

person.pop('fev_game')
print(person)  ## Result = `{'name': 'Md Rakib Hassan', 'age': 26, 'gender': 'Male', 'address': {'division': 'Chitogong', 'distic': 'Chandpur', 'thana': 'Hazigong', 'gram': 'Pirozpur Bazer'}}`


##* NOTE:- Nested Dictionary হতে Item Delete করার জন্যে।
person["address"].pop("division")
print(person)  ## Result = `{'name': 'Md Rakib Hassan', 'age': 26, 'gender': 'Male', 'fev_game': ['Cricket', 'Football', 'Badmintons'], 'address': {'distic': 'Chandpur', 'thana': 'Hazigong', 'gram': 'Pirozpur Bazer'}}`


##* NOTE:- Dictionary, last Element কে Delete করার জন্যে popitem Method use করা যায়।
person.popitem()
print(person)  ## Result = `{'name': 'Md Rakib Hassan', 'age': 26, 'gender': 'Male', 'fev_game': ['Cricket', 'Football', 'Badmintons']}`




##? ----------------------------------------------------------------------
##? Change/Modify Value Into a List 
person = {
    "name": "Md Rakib",
    "age" : 26,
    "gender" : "Male",
    "fev_game" : ["Cricket", "Football"],
    "address"  : {"division":"Chitogong", "distic":"Chandpur"},
}

## NOTE:- Dictionary, 
person.update({"name" : "Md Rakib Hassan"})
person.update({"age" : 28}) 

person["address"].update({"distic" : "Cumillah"}) 

print(person)  
"""Print Results =
    {
        'name': 'Md Rakib Hassan', 
        'age': 28, 
        'gender': 'Male', 
        'fev_game': ['Cricket', 'Football'], 
        'address': {
            'division': 'Chitogong', 
            'distic': 'Cumillah'
        }
    }
"""


##? Method 3: --------------( Copy Method )-------------------------
"""
    => copy method এর সাহায্যে আমরা কোন Dictionary কে Copy করতে পারি, 
       এমন কি এর এর ভেতরে থাক Nested Elements গুলোকেও আমরা Copy করতে পরি।
"""

person = {
    "name": "Md Rakib",
    "age" : 26,
    "gender" : "Male",
    "fev_game" : ["Cricket", "Football"],
    "address"  : {"division":"Chitogong", "distic":"Chandpur"},
}


##NOTE:-  দুইটি একই কাজ করে।
temp_person = person
print(temp_person)  ## Result = `{'name': 'Md Rakib', 'age': 26, 'gender': 'Male', 'fev_game': ['Cricket', 'Football'], 'address': {'division': 'Chitogong', 'distic': 'Chandpur'}}`

temp_person = person.copy()
print(temp_person)  ## Result = `{'name': 'Md Rakib', 'age': 26, 'gender': 'Male', 'fev_game': ['Cricket', 'Football'], 'address': {'division': 'Chitogong', 'distic': 'Chandpur'}}`

temp_person = person["address"]
print(temp_person) ## Result = `{'division': 'Chitogong', 'distic': 'Chandpur'}`

temp_person = person["address"].copy()
print(temp_person) ## Result = `{'division': 'Chitogong', 'distic': 'Chandpur'}`

temp_person = person["address"]["division"]
print(temp_person) ## Result = `Chitogong`