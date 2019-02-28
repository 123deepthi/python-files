import random
l=['r','p','s']
d ={"r":"rock","p":"paper","s":"scissor"}
us=0
cs=0
while True:
	u = input("enter your choice,press n to discontinue\n user choice ")
	if u == 'n':
		print("game over\n","user score =",us,"\nComp score =",cs )
		if us>cs:
			print("Final score -user wins")
		if cs>us:
			print("Final score -comp wins")
		exit()
	c = random.choice(l)
	print("comp chooses",d[c])
	print("user chooses,",d[u])
	if u == c:
		print("tie")
	elif u == 'r' and c == 's':
		print("user wins")
		us=us+1
	elif u == 'r' and c == 'p':
		print("comp wins")
		cs=cs+1
	elif u == 's' and c == 'p':
		print("user wins")
		us=us+1
	elif u == 's' and c == 'r':
		print("comp wins")
		cs=cs+1
	elif u == 'p' and c == 's':
		print("comp wins")
		cs=cs+1
	elif u == 'p' and c == 'r':
		print("user wins")
		us=us+1


