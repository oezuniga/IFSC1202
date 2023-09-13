#Create a simple calculator program and prompts for 2 operands and an operator, then calculates the result.
#Prompt for the first operand (either integer or floating point)
#Prompt for a operator, where:
#+ addtion
#- subtraction
#* multiplication
#\ division
#If an invalid operator is entered, then display "Invalid Operator" (Do not display an invalid calculation)
#If a valid operator is entered, display the first number, the operand, the second number, an equals sign, and the result of the calculation

from math import pi
# function symbol = +
def add(Q, W): 
    return Q + W
# function symbol = -
def subtract(Q, W):
    return Q - W
# function symbol = *
def multiply(Q, W):
    return Q * W
# function symbol = /
def divide(Q, W):
    return Q / W
# select operation for calculation
print("select your desired operation\n")
print("1 = Add\n")
print("2 = Subtract\n")
print("3 = Multiply\n")
print("4 = Divide\n")
# insert operation symbol
select = float(input("Select operation form 1, 2, 3, 4 :"))
Q = float(input("enter first number: "))
W = float(input("enter second number: "))

if select == 1:
    print(Q, "+", W, "=", add(Q,W))
elif select == 2:
    print(Q, "-", W, "=", subtract(Q,W))
elif select == 3:
    print(Q, "*", W, "=", multiply(Q,W))
elif select == 4:
    print(Q, "/", W, "=", divide(Q,W))
else:
    print("Invalid Operation")
print("Second Question")
select = float(input("Select operation form 1, 2, 3, 4 :"))
Q = float(input("enter first number: "))
W = float(input("enter second number: "))

if select == 1:
    print(Q, "+", W, "=", add(Q,W))
elif select == 2:
    print(Q, "-", W, "=", subtract(Q,W))
elif select == 3:
    print(Q, "*", W, "=", multiply(Q,W))
elif select == 4:
    print(Q, "/", W, "=", divide(Q,W))
else:
    print("Invalid Operation")
print("Third Question")
select = float(input("Select operation form 1, 2, 3, 4 :"))
Q = float(input("enter first number: "))
W = float(input("enter second number: "))

if select == 1:
    print(Q, "+", W, "=", add(Q,W))
elif select == 2:
    print(Q, "-", W, "=", subtract(Q,W))
elif select == 3:
    print(Q, "*", W, "=", multiply(Q,W))
elif select == 4:
    print(Q, "/", W, "=", divide(Q,W))
else:
    print("Invalid Operation")