def abc(f):
    def xyz(name):
        y = f(name.upper())
        return y
    
    return xyz




@abc
def MyName(name):
    print(f"My name is : {name}")



name_inpute = input("Given you name :") 
MyName(name_inpute)   
