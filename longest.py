msg=(input("Enter your message here :"))
word=""
longword=""
i=0
while i<len(msg):
	if msg[i]==" ":
		if len(word)>len(longword):
			longword=word
		word=""

	else:
		if i==(len(msg)-1):
			word=word+msg[i]
			if len(word)>len(longword):
				longword=word
		else:
			word=word+msg[i]	
	i=i+1	
print("The longest word in your message is :",longword)	