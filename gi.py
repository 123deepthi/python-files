class Test:
	rollno = 0
	def myfunc():
		print("hai! I am member of the class")

	def roll(self,k):
		self.rollno = k
		print("Hai I am",self.rollno)

o= Test()
o.roll(1)
print(o.rollno)