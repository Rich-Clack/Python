def reverse(word):
	newword=""
	i=len(word)-1
	while i>=0:
		newword=newword+word[i]
		i-=1
	return newword
	
message=input("Enter your message here :")
newmessage=""
word=""
i=0
while i<len(message):
	if message[i]==" ":
		newmessage+=(reverse(word)+" ")
		word=""
	else:
		if i==(len(message)-1):
			word+=message[i]
			newmessage+=(reverse(word))
		else:
			word+=message[i]
	i+=1
print(newmessage)					