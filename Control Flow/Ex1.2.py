# Python program to check if a number is positive, negative or 0\
# Using nested if

num = float(input('Enter a number: '))

if num>=0:
	if num == 0:
		print('Zero')

	else:
		print('Positive Number')

else:
	print('Negative Number')