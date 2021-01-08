# Python program to find HCF or GCD
# Using Euclidean algorithm

def compute_hcf(x,y):
	while(y):
		x,y = y,x%y

	return x



hcf = compute_hcf(300,400)
print('The H.C.F. is',hcf)