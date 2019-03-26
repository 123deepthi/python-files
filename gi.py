class test:
	rollno = 0
	def myfunc():
		print("hai! I am member of the class")

	def roll(self,k):
		self. rollno = k
		print("Hai I am",'self roll no')

o = test()
o.rollno(1)
print(o.rollno)