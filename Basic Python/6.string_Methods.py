a = "dhaka"
b = 'dhaka'
c = "d"
e = 'd'

print("Type of `a`", type(a))
print("Type of `b`", type(b))

print("Type of `c`", type(c))
print("Type of `e`", type(e))


a = "My name is "
b = "Rakib"

result = a + b
print(result)

print(len(a)) 


"""
#*      Posetive Index:    0    1     2     3    4     5     6     7    8     9   
#?           String        B    a     n     g    l     a     d     e    s     h
#Todo/  Negative Index:  -10   -9    -8    -7   -6    -5    -4    -3   -2    -1
"""

##! Positive Indexing
a = "Bangladesh"
l = len(a)

print("length of `a`", l)  

for i in range(l): ## 0 1 2 3 4 5 6 7 8 9
    print(f"Index = {i},  Value = {a[i]}")

##? Enumerate Functions
for index, value in enumerate(a):
    print(f"Index = {index},  Value = {value}")

for x, y in enumerate(a):
    print(f"Index = {x},  Value = {y}")


##! Negative Indexing
a = "Bangladesh"
l = len(a)

print("length of `a`", l)

print("Posetive Index =",a[9])
print("Negative Index =",a[-1])







"""
#*      Posetive Index:    0    1     2     3    4     5     6     7    8     9   
#?           String        B    a     n     g    l     a     d     e    s     h
#Todo/  Negative Index:  -10   -9    -8    -7   -6    -5    -4    -3   -2    -1
"""
##! Slice/Range:-
a = "Bangladesh"
start = int(input("Given a start value:"))
end   = int(input("Given a ending value:"))

for i in range(start, end):
    print(f"Index = {i},  Value = {a[i]}")

l = len(a)

for i in range(l-1, 2, -1):
    print(f"Index = {i},  Value = {a[i]}")



"""
#*      Posetive Index:    0    1     2     3    4     5     6     7    8     9   
#?           String        B    a     n     g    l     a     d     e    s     h
#Todo/  Negative Index:  -10   -9    -8    -7   -6    -5    -4    -3   -2    -1
"""

a = "Bangladesh"
##*Note: [start : stop : step]
start = int(input("Given a start value:"))
end   = int(input("Given a ending value:"))
step  = int(input("Given a increment value:"))
print(a[start:end:step])


print("Reverse of `a` =", a[::-1])  ## hsedalgnaB

print(a[7::-1])     ## result = `edalgnaB`
print(a[7:-11:-1])  ## result = `edalgnaB`

print(a[7:4:-1])  ## result = `eda`





##! String Reverse 
a = "Bangladesh"

##? 1. Using Slicing
reversed_s = a[::-1]
print("Using Slicing: ",reversed_s)    ## result = `hsedalgnaB`


##? 2. Using a Loop
reversed_s = ""
for char in a:
    reversed_s = char + reversed_s
print("Using a Loop: ",reversed_s)    ## result = `hsedalgnaB`


##? 3. Using the reversed() function
reversed_s = ''.join(reversed(a))
print("Using the reversed() function: ",reversed_s)   ## result = `hsedalgnaB`

    
##? 4. Using reduce() from functools (less common)
from functools import reduce
reversed_s = reduce(lambda x, y: y + x, a)
print("Using reduce() from functools: ",reversed_s)   ## result = `hsedalgnaB`


##? 5. Using recursion
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

s = "Bangladesh"
reversed_s = reverse_string(s)
print("Using recursion: ",reversed_s)   ## result = `hsedalgnaB`





"""
##! ---------------------------------------------------------------------------------
##! ----------------------------  String All Methods --------------------------------
"""

##? Method 1: ---------------( Length Mehod )---------------
a = "Bangladesh"

length = 0
for i in a:
    length+=1

print("Using For Loop =",length)


print("Using Len Function =",len(a))


##? Method 2: ---------------( Capitalize Method )---------------
## শুধু প্রথম Word এর প্রথম Character কে Capitalize করে দেয়।

a = "bangladesh"
b = "i live in dhaka"

result = a.capitalize()   ## result =  `Bangladesh`
result = b.capitalize()   ## result =  `I live in dhaka`

print(result)



##? Method 3: ---------------( Title  Method )---------------
## প্রত্যেক Word এর First Character কে Capitalise কেরে দেয়।

a = "bangladesh"
b = "i live in dhaka"

result = a.title()      ## result =  `Bangladesh`
result = b.title()      ## result =  `I Live In Dhaka`

print(result)



##? Method 4: ---------------( Upper  Method )---------------
## Full sentence কে Uppercase করে দিচ্ছে।

a = "bangladesh"
b = "i live in dhaka"

result1 = a.upper()      ## result =  `BANGLADESH`
result2 = b.upper()      ## result =  `I LIVE IN DHAKA`

print(result1)
print(result2)


##? Method 5: ---------------( Casefold  Method )---------------
## Full sentence কে lower case করে দিচ্ছে।

a = "BAngLadEsh"
b = "i livE iN dHakA"

result1 = a.casefold()     ## result =  `bangladesh`
result2 = b.casefold()     ## result =  `i live in dhaka`

print(result1)
print(result2)



##? Method 6: ---------------( Lower  Method )---------------
## Full sentence কে lower case করে দিচ্ছে।

a = "BAngLadEsh"
b = "i livE iN dHakA"

result1 = a.lower()     ## result =  `bangladesh`
result2 = b.lower()     ## result =  `i live in dhaka`

print(result1)
print(result2)



##? Method 7: ---------------( Find  Method )---------------
## Full sentence হতে কোন character বা কোন word এর সাথে মিল পেলে সেই Index কে Return করে।

a = "i live in Dhaka, It is the capital of Bangladesh. It is a small city"
b = "i compleated my graduation from daffodil international university in a subject of computer science and engineering."

result1 = a.find("l")        ## result =  `2`
result2 = a.find("is")       ## result =  `20`

result3 = a.find("i")        ## result =  `0`
result4 = b.find("in")       ## result =  `40`
result5 = b.rfind("in")      ## result =  `111`  #* শেষ দিক থেকে কত নাম্বার Positive index এ `in` আছে তা দেখায়।

result6 = b.find("test")     ## result =  `-1`   #* `test` word টি পায়নি তাই `-1` return করেছে।

print("`l` Position =",result1)   ## `l` Position = 2
print("`is` Position =",result2)  ## `is` Position = 20
print("`i` Position =",result3)   ## `i` Position = 0

print("length of a string =",len("i compleated my graduation from daffodil"))   ## length of a string = 40
print("`in` Position =",result4)         ## `in` Position = 41
print("`in` rfind Position =",result5)   ## `in` Position = 111

print("`test` Position =",result6) ## `test` Position = -1



##? Method 8: ---------------( Find  Method )---------------
a = "rakib"

length = len(a)

##Todo: Example1:
result1 = a.center(11)       ## result =  `---rakib---`   

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  9 | 10 |
#!    String =        |   |   |   | r | a | k | i | b |   |    |    | 
#*    Position =      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
"""

result2 = len(result1)       ## result =  `11`


##Todo: Example2:
result3 = a.center(16)       ## result =  `-----rakib----`

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
#!    String =        |   |   |   |   |   | r | a | k | i | b  |    |    |    |    |    |    |
#*    Position =      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |

"""

result4 = len(result3)       ## result =  `15`



print("String Length =", length)  # String Length = 5

print("", result1)  # `---rakib---`
print("", result2)  # 11

print("", result3)  # `-----rakib------`
print("", result4)  # 16





##? Method 9: ---------------( Ljust and Rjust  Method )---------------
a = "rakib"

length = len(a)

##Todo: Example1:
result1 = a.ljust(11)  # result = `rakib------`  

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  9 | 10 |
#!    String =        | r | a | k | i | b |   |   |   |   |    |    | 
#*    Position =      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
"""

result2 = len(result1)       ## result =  `11`


##Todo: Example2:
result3 = a.rjust(11)      ## result =  `------rakib`

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 |
#!    String =        |   |   |   |   |   |   | r | a | k |  i |  b | 
#*    Position =      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

"""

result4 = len(result3)       ## result =  `11`



print("String Length =", length)  # String Length = 5

print("`ljust` Method  Result =", result1)  # `rakib------`
print("", result2)  # 11

print("`rjust` Method  Result =", result3)  # `------rakib`
print("", result4)  # 11




##? Method 10: ---------------( Count  Method )---------------
## এর মাধ্যমে String এর ভেতর কয়টি নির্দিষ্ট সংক Alphabet আছে তা বের করা যায়।

txt_1 = "dhaka"        ##*  |   |   | a |   | a |
  
txt_2 = "I love apples, apple are my favorite fruit"  

print("Length of txt_1 = ",len(txt_1))
print("Length of txt_2 = ",len(txt_2))

result1 = txt_1.count('a')
print("Variable `txt_1` count result =", result1)


result2 = txt_2.count("apple")
print("Variable `txt_2` count result =", result2)


##Todo;  Search from position 10 to 24:

"""
##*  Index  |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|
##!  String |I| |l|o|v|e| |a|p|p|l |e |s |, |  |a |p |p |l |e |  |a |r |e |  |m |y |  |f |a |v |o |r |i |t |e |  |f |r |u |i |t |
##*  Length |1|2|3|4|5|6|7|8|9|0|1 |12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|39|40|41|42|
"""

result3 = txt_2.count("apple", 10, 24)   
print("Variable `txt_2` count result =", result3)  ## total Count = 1
print(txt_2[10:24])    ## Output: "les, apple are"