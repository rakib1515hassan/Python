# class Person:
#     name = "Md Rakib Hassan"  ##* `name` is a class variable


# a = Person()
# print(a.name)  ## `Md Rakib Hassan`


# ##? Class Variables Called by object
# a.age = 10
# print(a.name)

# ##? Class variables associated with value
# print(a.age)  ## 10

# ##? Class Variable Modified
# a.age = 15
# print(a.age) ## 15

# a.name = "Hassan"
# print(a.name)


##! Class Object Delete
# class Person:
#     name = "Hassan"


# obj1 = Person()
# obj1.age = 27
# print("Object 1",obj1.name)
# print("Object 1",obj1.age)

# print("\n---------------------------------")
# obj2 = Person()
# obj2.age = 28
# print("Object 2",obj2.name)
# print("Object 2",obj2.age)

# print("\n---------------------------------")
# del obj1

# print("Object 1",obj1.name)  ## NameError: name 'obj1' is not defined. Did you mean: 'obj2'?
# print("Object 1",obj1.age)   ## NameError: name 'obj1' is not defined. Did you mean: 'obj2'?




