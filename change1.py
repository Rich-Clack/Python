cost=int(input("Item cost : £"))
money=int(input("Money paid : £"))
balance=money-cost
print("Balance : £",balance)
print("-_-_-_-_-Change Breakdown-_-_-_-_-")
print("The following change is needed")
if balance/50>=1:
	print (int(balance/50), " x £50")
	balance = balance%50
	print(balance)
if balance/20>=1:
	print (int(balance/20), " x £20")
	balance=balance%20
	print(balance)
if balance/10>=1:
	print (int(balance/10), " x £10")
	balance=balance%10
	print(balance)
if balance/5>=1:
	print (int(balance/5), " x £5")
	balance=balance%5	
	print(balance)
if balance/2>=1:
	print (int(balance/2), " x £2")
	balance=balance%2
	print(balance)
if balance/1>=1:
	print (int(balance/1), " x £1")
	balance=balance%1	
	print(balance)