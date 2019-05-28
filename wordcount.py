msg=input("Enter your message here :")
find=input("What word are you looking to count? :")
i=0
count=0
while i<len(msg):
	if msg[i]==find[0]:
		if msg[i:len(find)+i]==find:
			count=count+1
			i=i+len(find)-1
	i=i+1
print ("The word appears",count, "times in the message")			
