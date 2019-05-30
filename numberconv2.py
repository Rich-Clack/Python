ones=[""," one"," two"," three"," four"," five"," six"," seven"," eight"," nine"," ten"," eleven"," twelve"," thirteen"," fourteen"," fifteen"," sixteen"," seventeen"," eighteen"," nineteen"]
tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

num=int(input("Enter your number here :"))
result=""
if num<=9999:
	if num>=1000 and num<=9999:
		result+=ones[int(num/1000)]+" thousand"
		num=num%1000
	if num>=100:
		result+=ones[int(num/100)]+" hundred "
		num=num%100
	if num>=20:
		result+=tens[int(num/10)]
		num=num%10
	if num >0 and num<19:
		result+=ones[num]
else:
	result="Your number is toooooo big for me to handle, try again......"		
print("The result is :",result)