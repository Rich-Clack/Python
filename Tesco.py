product=input("Enter Product Name:")
price=input("Enter Price")
qty=input("Enter Quantity")
amount=int(qty)*float(price)
vat=amount*15/100
bill=amount+vat
print("Your Bill :",bill)
print("Product :",product)
print("Amount :",amount)
print("VAT :", vat)
print("Bill :",bill)
