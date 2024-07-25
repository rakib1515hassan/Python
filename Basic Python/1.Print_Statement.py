# Print Function
name = "Rakib"
b = 10
c = 11.50

print(name, b, c)

# Variables Type Checking
a = 10
a:int = 10
print(type(a))  ## <class 'int'>


b = "Rakib"
b:str = "Rakib"
print(type(b))  ## <class 'str'>
e = 't'
print(type(e))  ## <class 'str'>


c = 12.25
c:float = 12.25
print(type(c))  ## <class 'float'>


d = a
print(d)        ## 10




##! ---------------------------------------------------------------------------------
##! ----------------------------(+ Formating +)--------------------------------------
name = "Rakib"
age = 10
address = "Dhaka"


##? Formula 1:-
print("Person Info: ", name, age, address)


##? Formula 2:-
print("Name: ",name,"," "age: ",age, "," "address: ", address)


##! Formula 3:- ***
print(f"Name: {name}, age: {age}, address: {address}")


##? Formula 4:-
print("Name: {}, age: {}, address: {}".format(name, age, address))


##? Formula 5:-
print("Name: {n}, age: {a}, address: {ad}".format(n = name, a = age, ad = address))


##? Formula 6:-
print("Name: %s, age: %s, address: %s" %(name, age, address))









