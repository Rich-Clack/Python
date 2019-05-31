msg=input("Enter your message here :")
find=input("What word are you looking to replace? :")
repl=input("Enter your new word :")

for data in msg:
	i=0
	while i<len(data):
		if data[i]==find[0]:
			if data[i:len(find)+i]==find:
				print(repl,end="")
				i+=len(find)-1
			else:
				print(data[i],end="")	
		else:
			print(data[i],end="")
		i+=1			


