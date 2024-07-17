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








