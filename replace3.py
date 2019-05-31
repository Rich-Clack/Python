file_read=open("test2.txt","r")
file_write=open("test3.txt","w")
i=0
for data in file_read:
	for ch in data:
		if ch=="i":
			i=i+ch
			if ch=="s":
				i=i+ch
				print("###",end="")
		else:
			print(ch,end="")	
	
