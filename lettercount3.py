def countalpha(message,alpha):
	i=0
	count=0
	while i<len(message):
		message = message.upper()
		if (message[i])==alpha:
			count+=1
		i+=1
	if count>0:
	    print(alpha," = ",count)		
message=input("Enter your message here :")
c=65
while c<=90:
	countalpha(message,chr(c)) 
	c+=1   