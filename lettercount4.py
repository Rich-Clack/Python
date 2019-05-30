alpha=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
message=input("Enter your message here :")
i=0
while i<len(message):
	message = message.upper()
	alpha[ord(message[i])-65]+=1
	i+=1
i=0
print("There are the below letters included in your message :")
while i<=25:
	if alpha[i]>0:
		print(chr(i+65)," = ",alpha[i])
	i+=1
print("Please come again, i value your attention")