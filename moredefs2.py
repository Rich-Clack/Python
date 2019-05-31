def operations(day):
	if day==1:
		def fun(a,b):
			c=a+b
			print("The result is :",c)
	if day==2:
		def fun(a,b):
			c=a-b
			print("The result is :",c)		
	return fun

pro=operations(1)
pro(7,2)		
