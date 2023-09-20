#You may use previous assignments, notes, books, or the internet for the exam. However, copying a solution that does not solve the assignment will result in a zero.
#You may NOT consult with another student.
#The exam is due at precisely 11am. At that time, the exam will disappear from Blackboard and you will not be able to submit your work, resulting in a zero.
#Save your work as Exam One.py, download it, and attach it to your assignment
    #Create a program that displays super special numbers in a range. A special number is defined to be number whose sum of the factorial of digits is equal to the original number.
    #145 is equal to 1! + 4! + 5!
    #40585 is equal to 4! + 0! + 5! + 8! + 5!
    #Hint: You will have to have a loop to isolate each digit of the number
    #Hint: You will have use another loop to calculate the factorial for each digit
    #Hint: Recalculate the value using the above and see if you get the original value
        #Enter Start of Range: 1
        #Enter End of Range: 100000
        #Super Special Numbers between 1 and 100000
        #1
        #2
        #145
        #40585
for i in range(1, 100000):
    print(i, i ** 2)
    i = 1
    X = int(input("ENTER NUMBER: "))
    OSCAR = 0
    TEMP = X
    while(TEMP > 0):
        FACT = 1
        rem = TEMP % 10
        for i in range(1, rem + 1):
            FACT = FACT * i
            print("FACTORAIL of %d = %d " %(rem, FACT))
            OSCAR = OSCAR + FACT
            TEMP = TEMP // 10
            print("SUM OF FACTORIAL OF NUMBER %d = %d " %(X, OSCAR))
            if(OSCAR == X):
                print("SUPER SPECIAL NUMBER")
print('End of Loop')
