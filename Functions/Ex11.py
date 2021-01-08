# Python program to display Fibonnaci sequence using recursion

def recur_febo(n):
	if n <= 1:
		return n

	else:
		return(recur_febo(n-1) + recur_febo(n-2))



nterms = 10

# check if the number of terms is valid 
if nterms <= 0:
	print('Please enter a positive integer')
else:
	print('Fibonnaci sequence:')
	for i in range(nterms):
		print(recur_febo(i))