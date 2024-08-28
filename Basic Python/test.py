def person_card(name, phone=None, email=None):

    if (name is not None) and (phone is not None) and (email is not None): 
        return f"Name:{name}, Phone:{phone}, Email:{email}"
    
    elif (email is None) and (phone is None):
        return f"Name:{name}"
    
    elif phone is None:
        return f"Name:{name} Email:{email}"
    
    elif email is None:
        return f"Name:{name}, Phone:{phone}"
    
    
    
    



## Person Card 1
input_name  = "rakib" 
input_phone = 123
input_email = "rakib@gmail.com"

info = person_card(
        name  = input_name, 
        email = input_email, 
        phone = input_phone
    )
print("Person 1 =",info)



## Person Card 2
input_name2  = "hassan"  
input_phone2 = "456"  
# input_email2 = "hassan@gmail.com" 

info2 = person_card(
        name  = input_name2, 
        # email = input_email2, 
        phone = input_phone2
    )
print("Person 2 =",info2)



## Person Card 3
input_name3  = "rubel"  
# input_phone3 = "789"  
# input_email3 = "rubel@gmail.com" 

info3 = person_card(
        name  = input_name3, 
        # email = input_email3, 
        # phone = input_phone3
    )
print("Person 3 =",info3)