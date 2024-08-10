##! Example 4:-
txt_4 = "rakib1515hassan@gmail.com"

result4, result5 = txt_4.split('@')
print(result4)   ## Results = `rakib1515hassan`
print(result5)   ## Results = `gmail.com`

first_name, last_name = result4.split('1515')
print("First Name :",first_name.capitalize())   ## Results = `Rakib`
print("Last Name :",last_name.capitalize())     ## Results = `Hassan`