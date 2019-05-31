msg=("Enter your message here :")
find=input("What word are you looking to replace? :")
repl=input("Enter your new word :")
f_read=open("test.txt","r")
f_write=open("test4.txt","w")

for data in f_read:
	i=0
	while i<len(data):
		if data[i]==find[0]:
			if data[i:len(find)+i]==find:
				print(repl,end="",file=f_write)
				i+=len(find)-1
			else:
				print(data[i],end="",file=f_write)	
		else:
			print(data[i],end="",file=f_write)
		i+=1			


