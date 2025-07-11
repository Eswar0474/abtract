class product:
	def __init__(self,a,b):
		self.name=a
		self.__price=b
p1=product("router",2000)
p2=product("switch",1500)
print(p1.name,p1.__price)
print(p2.name,p2.__price)