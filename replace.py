table=[]
msg=input("Enter your message here :")
find=input("Enter the word you want to replace :")
word=""
count=0
while i<len(msg):
	if msg[i]==find[0]:
		if msg[i:len(find)+i]==find:
			count+=1
			i=i+len(find)-1
	
	i+=1
print (count)			