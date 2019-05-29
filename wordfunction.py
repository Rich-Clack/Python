def wordcount(message):
	word=1
	i=0
	while i<len(message):
		if message[i]==" ":
		    word+=1
		i+=1
	return word
word1=input("Enter you phrase here :")	
print("words:",wordcount(word1))
