a = 10
b = 20
c = 30
if (a >= b) and (a>= c):
	largest = a
elif (b >= a) and (b >= c):
	largest = b
else:
	largest = c
	print("the largest number between ", a,",", b, "," ,'and', c, "is", largest)