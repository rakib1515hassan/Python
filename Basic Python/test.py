def profile(a, b, *args, **kwargs):

    tuple_date = args
    dic_data = kwargs

    print(a)
    print(b)
    print(tuple_date)
    print(dic_data)


## Main function
p = {
    "name": "rakib",
    "id": 162,
    "group": "A",
    "city": "Dhaka"
}

n = (5, 6, 7, 9)

a = "Bangladesh"
b = "United States"

profile(a, b, *n, **p)