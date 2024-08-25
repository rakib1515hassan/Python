person = ["rakib", ["Texon", "Mirpur"], "28", "Dhaka"]


for info in person:

    if type(info) == list:
        for i in info:
            print(i)
        
    else:
        print(info)


"""
rakib
['Texon', 'Mirpur']
28
Dhaka
"""