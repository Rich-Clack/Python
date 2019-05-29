def change(message):
	i=0
	newmessage=""
	while i<len(message):
		code=ord(message[i])
		if code>=65 and code<=90:
			newmessage+=chr(code+32)
		else:
			if code>=97 and code<=122:
				newmessage+=chr(code-32)
			else:
				if code>=48 and code<=57:
					newmessage+=str(int(chr(code))*2)
				else:
					newmessage+=chr(code)
		i=i+1
	return newmessage
	
message=input("Enter your message here :")
print (change(message))
