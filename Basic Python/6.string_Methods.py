a = "dhaka"
b = 'dhaka'
c = "d"
e = 'd'

print("Type of `a`", type(a))  ## <class 'str'>
print("Type of `b`", type(b))  ## <class 'str'>

print("Type of `c`", type(c))  ## <class 'str'>
print("Type of `e`", type(e))  ## <class 'str'>


a = "My name is "
b = "Rakib"

result = a + b
print(result)

print(len(result)) ## `16`


"""
#?      Length             1    2     3     4    5     6     7     8    9     10
#*      Posetive Index:    0    1     2     3    4     5     6     7    8     9   
#?           String        B    a     n     g    l     a     d     e    s     h
#Todo/  Negative Index:  -10   -9    -8    -7   -6    -5    -4    -3   -2    -1
"""

##! Positive Indexing
a = "Bangladesh"
l = len(a)   

print("length of `a` =", l)  ## length of `a` = 10

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

print("Posetive Index =",a[9])   ##  h
print("Negative Index =",a[-1])  ##  h







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
    length+=1   ## length = length + 1

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


##? Method 7: ---------------( Swapcase Method )---------------
"""
Sentance এর Alphabet এর Case কে Swap করে দেয়, Capital Letter থাকলে Small Letter করে দেয়, 
Small Letter থাকলে Capital Letter করে দেয়।
"""  

a = "BAngLadEsh"
b = "i livE iN dHakA"

result1 = a.swapcase()     ## result =  `baNGlADeSH`
result2 = b.swapcase()     ## result =  `I LIVe In DhAKa`

print(result1)
print(result2)


##? Method 8: ---------------( Find  Method )---------------
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



##? Method 9: ---------------( Find  Method )---------------
a = "rakib"

length = len(a)

##Todo: Example1:
result1 = a.center(11)       ## result =  `---rakib---`   

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  9 | 10 |
#!    String =        |   |   |   | r | a | k | i | b |   |    |    | 
#*    Length =        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
"""

result2 = len(result1)       ## result =  `11`


##Todo: Example2:
result3 = a.center(16)       ## result =  `-----rakib----`

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
#!    String =        |   |   |   |   |   | r | a | k | i | b  |    |    |    |    |    |    |
#*    Length =        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |

"""

result4 = len(result3)       ## result =  `15`



print("String Length =", length)  # String Length = 5

print("", result1)  # `---rakib---`
print("", result2)  # 11

print("", result3)  # `-----rakib------`
print("", result4)  # 16





##? Method 10: ---------------( Ljust and Rjust  Method )---------------
a = "rakib"

length = len(a)

##Todo: Example1:
result1 = a.ljust(11)  # result = `rakib------`  

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |  9 | 10 |
#!    String =        | r | a | k | i | b |   |   |   |   |    |    | 
#*    Length =        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 
"""

result2 = len(result1)       ## result =  `11`


##Todo: Example2:
result3 = a.rjust(11)      ## result =  `------rakib`

""" #Memory Usage
#*    Index  =        | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9  | 10 |
#!    String =        |   |   |   |   |   |   | r | a | k |  i |  b | 
#*    Length =        | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

"""

result4 = len(result3)       ## result =  `11`



print("String Length =", length)  # String Length = 5

print("`ljust` Method  Result =", result1)  # `rakib------`
print("", result2)  # 11

print("`rjust` Method  Result =", result3)  # `------rakib`
print("", result4)  # 11




##? Method 11: ---------------( Count  Method )---------------
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




##? Method 12: ---------------( Strip  Method )---------------
## কোন Word এর ডানে ও বামের Space ও অন্যান্য garbage values কে Remove করে দেয়।

txt_1 = "   dhaka  "              ##*  |   |   |   | d | h | a | k | a |   |   |
  
txt_2 = "333bangladeshiiiiiaaa"   ##*  | 3 | 3 | 3 | b | a | n | g | l | a | d | e | s | h | i | i | i | i | i | a | a | a |

print("Length of txt_1 = ",len(txt_1))  ## Results = `10`
print("Length of txt_2 = ",len(txt_2))  ## Results = `21`

print("--------------------------------------------")

result1 = txt_1.strip()
print("Variable `txt_1` strip result =", result1)   ## Results = `dhaka`
print("Length of result1 = ",len(result1))          ## Results = `5`

result2 = txt_2.strip("3ia")
print("Variable `txt_2` strip result =", result2)   ## Results = `bangladesh`
print("Length of result2 = ",len(result2))          ## Results = `10`




##? Method 13: ---------------( Splite Method )---------------
"""
Sentance এর ক্ষেত্রে Split Function টি প্রত্যেক Word গুলোকে আলাদা করে একটি List বানিয়ে দেয়, 
এই ক্ষেত্রে by default `space` এর উপর ভিতি করে সে আলাদা করে। আমরা চাইলে `space` এর পরিবর্তে 
যে কোন কিছুর সাহায্যে করতে পারি, সেই ক্ষত্রে তা splite() এর ভেতর mention করে দিতে হবে।
## NOTE:- This Method return a List
"""  

##! Example 1:-
txt_1 = "bangladesh"       

result1 = txt_1.split()
print("Variable `txt_1` splite result =", result1)   ## Results = `['bangladesh']`


##! Example 2:-
txt_2 = "i live in dhaka city."   

result2 = txt_2.split()
print("Variable `txt_2` splite result =", result2)   ## Results = `['i', 'live', 'in', 'dhaka', 'city.']`


##! Example 3:-
txt_3 = "rakib15-8123@diu.edu.bd"

result3 = txt_3.split('@')
print("Variable `txt_3` splite result =", result3)   ## Results = `['rakib15-8123', 'diu.edu.bd']`


##! Example 4:-
txt_4 = "rakib1515hassan@gmail.com"

result4, result5 = txt_4.split('@')
print(result4)   ## Results = `rakib1515hassan`
print(result5)   ## Results = `gmail.com`

first_name, last_name = result4.split('1515')
print("First Name",first_name.capitalize())   ## Results = `Rakib`
print("Last Name",last_name.capitalize())     ## Results = `Hassan`


##! Example 5:-
txt_5 = "I like to play cricket and i also like to play football."

print("Total `to` in our sentence = ", txt_5.count('to')) ##  Results = 2

result6 = txt_5.split('to') 
print(result6)      ## Results = `['I like ', ' play cricket and i also like ', ' play football.']`



##? Method 14: ---------------( Partition Method )---------------
"""
Sentance কে কোন নির্দিষ্ট Element এর সাপেক্ষে ভাগ করে ফেলে। 
## NOTE:- Always return Tuple.
"""  

##! Example 1:-
txt_1 = "i live in dhaka city."   

result1 = txt_1.partition('in')
print("Variable `txt_1` partition result =", result1)   ## Results = `('i live ', 'in', ' dhaka city.')`


##! Example 2:-
txt_2 = "I like to play cricket and i also like to play football."

print("Total `to` in our sentence = ", txt_2.count('to')) ##  Results = 2

result2 = txt_2.partition('to') 
print(result2)      ## Results = `('I like ', 'to', ' play cricket and i also like to play football.')`



##? Method 15: ---------------( Startswith Method )---------------
"""
Sentance কি দিয়ে শুরু হয়েছে তা চেক করা যায়। 
## NOTE:- Always return True/False.
"""  

##! Example 1:-
txt_1 = "i live in dhaka city."   

result1 = txt_1.startswith('i')
print(result1)   ## Results = `True`


##! Example 2:-
txt_2 = "Football is my favorite game."

result2 = txt_2.startswith('Football') 
print(result2)      ## Results = `True`


##! Example 3:-
txt_3 = "i live in dhaka city."   

result3 = txt_3.startswith('I')
print(result3)   ## Results = `False`



##? Method 16: ---------------( Endswith Method )---------------
"""
Sentance কি দিয়ে শেষ হয়েছে তা চেক করা যায়। 
## NOTE:- Always return True/False.
"""  

##! Example 1:-
txt_1 = "i live in dhaka city"   

result1 = txt_1.endswith('y')
print(result1)   ## Results = `True`


##! Example 2:-
txt_2 = "Football is my favorite game"

result2 = txt_2.endswith('game') 
print(result2)      ## Results = `True`


##! Example 3:-
txt_3 = "i live in dhaka city"   

result3 = txt_3.startswith('City')
print(result3)   ## Results = `False`


##! Example 4:-
txt_4 = "i live in dhaka city."   

result4 = txt_4.startswith('city')
print(result4)   ## Results = `False`



##? Method 17: ---------------( Replace Method )---------------
"""
Sentance এর কোন অংশ পরিবর্তন করা যায়।
"""  

##! Example 1:-
txt_1 = "i live in dhaka city"   

result1 = txt_1.replace("dhaka", "syhllet")  
print(result1)   ## Results = `i live in syhllet city`
print(txt_1)     ## Results = `i live in dhaka city`


# ##! Example 2:-
txt_2 = "I like to play cricket and i also like to play football."

result2 = txt_2.replace("play", "see")
print(result2)      ## Results = `I like to see cricket and i also like to see football.`


##? Method 18: ---------------( IsLower Method )---------------
"""
Sentance টির সব গুলো Alphabet small letter কি না তা check করে দেয়।
NOTE:- Always return True/False
"""  

##! Example 1:-
txt_1 = "bangladesh"   

result1 = txt_1.islower() 
print(result1)   ## Results = `False`   


##! Example 2:-
txt_2 = "banGlaDesH"   

result2 = txt_2.islower() 
print(result2)   ## Results = `True`


##! Example 3:-
txt_3 = "i would like To Play football."   

result3 = txt_3.islower() 
print(result3)   ## Results = `False`


##! Example 4:-
txt_4 = "i would like to play football."   

result4 = txt_4.islower() 
print(result4)   ## Results = `True`



##? Method 19: ---------------( IsTitle Method )---------------
"""
Sentance টির সব গুলো Word এর First Alphabet Capital letter কি না তা check করে দেয়।
NOTE:- Always return True/False
"""  

##! Example 1:-
txt_1 = "bangladesh"   

result1 = txt_1.istitle() 
print(result1)   ## Results = `False`   


##! Example 2:-
txt_2 = "Bangladesh"   

result2 = txt_2.istitle() 
print(result2)   ## Results = `True`


##! Example 3:-
txt_3 = "i would like To Play football."   

result3 = txt_3.istitle() 
print(result3)   ## Results = `False`


##! Example 4:-
txt_4 = "I Would Like To Play Football."   

result4 = txt_4.istitle() 
print(result4)   ## Results = `True`


##? Method 20: ---------------( IsDigit, IsNumeric, IsDecimal, IsAlpha, IsAlNum Method )---------------

print("------------+ isdigit() +-------------")
##! IsDigit Method ---------------------------
txt_1 = "21"
print(txt_1.isdigit())   ## Results = `True`   

txt_2 = "5.69"   
print(txt_2.isdigit())   ## Results = `False`

txt_3 = "1st"   
print(txt_3.isdigit())   ## Results = `False`

txt_4 = "3/4"   
print(txt_4.isdigit())   ## Results = `False`


print("------------+ isnumeric() +-------------")
##! IsNumeric Method ---------------------------
txt_5 = "21"
print(txt_5.isnumeric())   ## Results = `True`   

txt_6 = "5.69"   
print(txt_6.isnumeric())   ## Results = `False`

txt_7 = "1st"   
print(txt_7.isnumeric())   ## Results = `False`

txt_8 = "3/4"   
print(txt_8.isnumeric())   ## Results = `False`


print("------------+ isdecimal() +-------------")
##! IsDecimal Method ---------------------------
txt_9 = "21"
print(txt_9.isdecimal())   ## Results = `True`   

txt_10 = "5.6956"  
print(txt_10.isdecimal())   ## Results = `False`

txt_11 = "1st"   
print(txt_11.isdecimal())   ## Results = `False`

txt_12 = "3/4"   
print(txt_12.isdecimal())   ## Results = `False`


print("------------+ isalpha() +-------------")
##! IsAlpha Method ---------------------------
txt_13 = "a"
print(txt_13.isalpha())   ## Results = `True`   

txt_14 = "B"  
print(txt_14.isalpha())   ## Results = `True`

txt_15 = "Bangladesh"   
print(txt_15.isalpha())   ## Results = `True`

txt_16 = "Bangladesh in"   
print(txt_16.isalpha())   ## Results = `False`

txt_17 = "Bangladesh1971"   
print(txt_17.isalnum())   ## Results = `True`


print("------------+ isalnum() +-------------")
##! IsAlNum Method ---------------------------
txt_18 = "a"
print(txt_18.isalnum())   ## Results = `True`   

txt_19 = "B"  
print(txt_19.isalnum())   ## Results = `True`

txt_20 = "Bangladesh"   
print(txt_20.isalnum())   ## Results = `True`

txt_21 = "Bangladesh in"   
print(txt_21.isalnum())   ## Results = `False`

txt_22 = "Bangladesh 1971"   
print(txt_22.isalnum())   ## Results = `False`

txt_23 = "Bangladesh1971"   
print(txt_23.isalnum())   ## Results = `True`