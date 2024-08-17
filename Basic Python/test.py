divisions = [["Dhaka", "Savar", "Ghazipur"], "Khulna", "Sylhet", ("Chittagong", "Cox's Bazar", "Rangamati"), "Rajshahi", "Rangpur", "Mymensingh", "Barishal "]



inpute_value = input("Given a name which one index you want to know? :") ## If give :Rajshahi Else If give :Cox's Bazar

index_no = []

for d_index, d in enumerate(divisions):

    if type(d) is list:
        for c_index, city in enumerate(d):
            if inpute_value == city:
                index_no.extend([d_index, c_index])
                break

    elif type(d) is tuple:
        for c_index, city in enumerate(d):
            if inpute_value == city:
                index_no.extend([d_index, c_index])
                break
            
    else:
        if inpute_value == d:
            index_no.append(d_index)
            break


print(index_no)

