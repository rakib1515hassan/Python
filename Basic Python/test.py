def Power(base, powerRaised): 

    if powerRaised != 0:
        return base * Power(base, powerRaised-1)
    else:
        return 1
  

"""
    Step 1: 10 * Power(10, 3) , result = Pending
    Step 2: 10 * Power(10, 2) , result = Pending
    Step 3: 10 * Power(10, 1) , result = Pending
    Step 4: 10 * Power(10, 0) , result = 10 * 1 = 10

    Step 3: 10 * 10 , result = 100
    Step 2: 10 * 100 , result = 1000
    Step 1: 10 * 1000 , result = 10000
"""


    
base = int(input("Enter base number :"))   ## 10

powRaised = int(input("Enter power number(positive integer) :"))  ## 4

r = Power(base=base, power=powRaised)

print(r)


 










