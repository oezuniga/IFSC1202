from math import pi
# String Examples
print("{}".format("Hello"))         #|h|e|l|l|o
print("{:8s}".format("hello"))      #|h|e|l|l|o| | | |
print("{:>8s}".format("hello"))     #| | |h|e|l|l|o|
print("{:^8s}".format("hello"))     #| |h|e|l|l|o| | |
print("{:^4.2s}".format("hello"))   #| |h|e||
# Integer Example
print("{:4d}".format(42))           #|||4|2|
print("{:04d}".format(42))          #|0|0|4|2
# Floating Point Examples
print("{:6.2f}".format(pi))         #|||3|.|1|4|
print("{:06.2f}".format(pi))        #|0|0|3|.|1|4|
print("{:,.2f}".format(123456789.017))  #|1|2|3|,|4|5|6|,|7|8|9|.|0|2
# Other Examples

one = "one"
two = "two"
three = "three"

print("{}{}{}".format("one","two","three"))
print("one ={:s}, two ={:s}, three ={:s}".format(one,two,three))
print("one ={:8s}, two ={:8s}, three ={:8s}".format(one, two, three))
print("one ={:.2s},two ={:.2s},three ={:.2s}".format(one,two,three))