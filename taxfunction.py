def tax(salary):
	if salary>1500:
		T=salary*21/100
	else:
	    T=salary*15/100
	return T    	
salary1=int(input("Enter your alleged salary :"))
print("Your Tax will be :", tax(salary1))
print("Net Salary will be:", salary1-tax(salary1))
	