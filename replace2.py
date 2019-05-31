file_read=open("test2.txt","r")

for data in file_read:
	i=0
	while i<len(data)-1:
		if data[i]=="o":
			print("#",end="")
		else:
			print(data[i],end=" ")	
		i+=1
