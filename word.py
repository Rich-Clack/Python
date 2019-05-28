word=0
msg=input("Enter your message here :")
i=0
while i<len(msg):
	if msg[i]==" ":
		word=word+1
	i=i+1
print("There are ",word+1,(" words in your message"))		