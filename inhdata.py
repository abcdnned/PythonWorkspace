class Parent:
	def __init__(self):
		self.name='fff'
	def pp(self):
		if self.name=='fff':
			print 'my name is fff.'

class Child(Parent):
	def r(self):
		self.pp()
c=Child()
c.r()
