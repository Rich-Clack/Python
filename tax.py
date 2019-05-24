name=input("Please enter your full name :")
salary=int(input("Please enter your actual salary, not what you tell people you earn :"))
if salary>2000:
   tax=salary*25/100
else:
   tax=salary*15/100
netsalary=salary-tax
print("Your name is :",name)      
print("Your pre-tax salary is :",salary)
print("The Taxman robs you of",tax)
print("Your net salary is :",netsalary)