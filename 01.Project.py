from math import floor
# program that prompts for a length of time in days
# time "t", day "d", weeks "wks", months "m", years "y"
t,d,wks,m,y = "time","day","weeks","months","years"
A = input("Enter Length of Time in Days: ")
B = input("year: ")
C = input("weeks: ")
D = input("days: ")
sum = int(A)/365        # days divide by year
sum1 = int(A)/7         # days divide by weeks
sum2 = int(A)/1         # days divide days
print(sum):(years)
print(sum1)
print(sum2)

#Python program to convert 
# given number of days to years, months and days

# Reading number of days from user
number_of_days = int(input("Enter number of days: "))

# Calculating years
years = number_of_days // 365

# Calculating months
months = (number_of_days - years *365) // 30

# Calculating days
days = (number_of_days - years * 365 - months*30)

# Displaying results
print("Years = ", years)
print("Months = ", months)

print("Days =", days)