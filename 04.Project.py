#Create a program that displays a list or prime number in a specified range.
#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
#Hint: For a given value N, Loop from 2 to (half of N) + 1 and check to see if any number evenly divides into N

print("Prime Number")
x = int(input("Enter Start of Range: "))
y = int(input("Enter End of Range: "))
print("Prime Number are between", x, "and", y,)
for num in range(x, y + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)