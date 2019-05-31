file_read=open("test2.txt","r")
char=input("Enter character you want to change :")
change=input("Enter new character :")
for data in file_read:
	for ch in data:
		if ch==char:
			print(change,end="")
		else:
			print(ch,end="")	
	
