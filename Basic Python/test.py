a = [["Dhaka", "Savar", "Ghazipur"], "Khulna", "Sylhet", ("Chittagong", "Cox's Bazar", "Rangamati"), "Rajshahi", "Rangpur", "Mymensingh", "Barishal ", {"name": "rakib", "city": "chandpur"}]



"""##NOTE:- Structure of Nested List and Index
##? Length          1                   2         3              4                     5         6           7           8
##* Index           0                   1         2              3                     4         5           6           7
#            [[                  ], "Khulna", "Sylhet", [                      ], "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]
##! Index          -8                  -7        -6             -5                    -4        -3          -2          -1
#               "Dhaka",   (0,0)/(-8,-3)                   "Chittagong",   (3,0)/(-8,-3)       
#               "Savar",   (0,1)/(-8,-2)                   "Cox's Bazar",  (3,1)/(-8,-2)
#               "Ghazipur" (0,2)/(-8,-1)                   "Rangamati",    (3,2)/(-8,-1)
#            
"""

print("Posetive Index: ")
print(a[0])       ## Result = `['Dhaka', 'Savar', 'Ghazipur']`
print(a[1])       ## Result = `Khulna`
print(a[3])       ## Result = `("Chittagong", "Cox's Bazar", "Rangamati")`
print(type(a[3])) ## Result = 
print(a[6])       ## Result = `Mymensingh`
print(a[8])