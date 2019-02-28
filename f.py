num = int(input("enter the number"))
factorial = 1
if (num <= 0):
	print("does not exist")
else:
		for i in range (1,num+1):
			factorial=factorial*i
		print("The factorial of", num ,"is",factorial)