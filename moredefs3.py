def subtraction(*values):
	result=(values[0])
	i=1
	while i<len(values):
		result-=values[i]
		i+=1
	print(" The result is :",result)

def addition(*values):
	result=0
	for data in values:
		result+=data
	print(" The result is :",result)

def operations(f,*values):
		f(*values)

operations(addition,2,3,4,5,6,7,8)
operations(subtraction,9,2,2,2)