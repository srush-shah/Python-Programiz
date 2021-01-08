# Python program to swap two variables
# Without using temporary variables

x = 5
y = 10

x, y = y, x

print("x = ",x)
print("y = ",y)

# Addition and Subtraction

x = x + y
y = x - y
x = x - y

print("x = ",x)
print("y = ",y)

# Multiplication and Division

x = x * y
y = x / y
x = x / y

print("x = ",x)
print("y = ",y)

# XOR swap

x = x ^ y
y = x ^ y 
x = x ^ y

print("x = ",x)
print("y = ",y)