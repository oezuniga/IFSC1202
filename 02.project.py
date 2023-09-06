# question 1
# Three sides of the triangle is a, b and c:
a = float(input('Enter first side: a = '))
b = float(input('Enter second side: b = '))
c = float(input('Enter third side: c = '))
# calculate the semi-perimeter
print('s=(a + b + c) /2')
s=(a + b + c) /2
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   

# question 2
# Three sides of the triangle is x, y, and z:
x = float(input('Enter first side: x = '))
y = float(input('Enter second side: y = '))
z = float(input('Enter third side: z = '))
# calculate the semi-perimeter
print('s=(x + y + z) /2')
s=(x + y + z) /2
# calculate the area  
area = (s*(s-x)*(s-y)*(s-z)) ** 0.5  
print('The area of the triangle is %0.15f' %area)

# question 3
# Three sides of the triangle is d, e and f:
d = float(input('Enter first side: d = '))
e = float(input('Enter second side: e = '))
f = float(input('Enter third side: f = '))
# calculate the semi-perimeter
print('s=(d + e + f) /2')
s=(d + e + f) /2
# calculate the area  
area = (s*(s-d)*(s-e)*(s-f)) ** 0.5  
print('The area of the triangle is %0.15f' %area)
