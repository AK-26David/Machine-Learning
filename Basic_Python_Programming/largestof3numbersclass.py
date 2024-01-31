a = input("Enter the first number:")
b = input("Enter the second number:")
c = input("Enter the third number:")
def maximum(a, b, c):
	if (a >= b) and (a >= c):
		largest = a
	elif (b >= a) and (b >= c):
		largest = b
	else:
		largest = c
	return largest
print(maximum(a, b, c))
