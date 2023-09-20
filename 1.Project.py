# program that prompts for a length of time in days
# day "d", weeks "wks", months "m", years "y"

# First question
number_of_days = int(input("Enter number of days: "))
# Calculating years
years = number_of_days // 365
# Calculating months
months = (number_of_days - years * 365) // 30
# Calculating weeks
weeks = (number_of_days - years * 365) // 7
# Calculating days
days = (number_of_days - years * 365 - months * 30)
# Displaying results
print("y = ", years)
print("m = ", months)
print("Wks =", weeks)
print("d = ", days)

#Second question
number_of_days1 = int(input("Enter number of days: "))
# Calculating years
years1 = (number_of_days1) // 365 
# calculating months
months1 = (number_of_days1 - years1 * 365) //30
# calculating weeks
weeks1 = (number_of_days1 - years1 * 365) //7
# calculating days
days1 = (number_of_days1 - years1 * 365 - months1 * 30)
# Displaying results
print("y = ", years1)
print("m = ", months1)
print("wks =", weeks1)
print("d = ", days1)

# third question
number_of_days2 = int(input("Enter number of days: "))
# calculating years
years2 = (number_of_days2) // 365
#calcuating months
months2 = (number_of_days2 - years2 * 365) //30
#calculating weeks
weeks2 = (number_of_days2 - years2 * 365) //7
#calculating days
days2 = (number_of_days2 - years2 * 365 - months2 *30)
# Displaying results
print("y = ", years2)
print("m = ", months2)
print("wks =", weeks2)
print("d = ", days2)



#trial run for dna to protein
##
#need amino acid tabl
# read 3 letter per amino acid
