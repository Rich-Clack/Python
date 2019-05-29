Alpha=input("Enter any letter from the Alphabet here :")
if ord(Alpha)>=65 and ord(Alpha)<=90:
	print("Here you go my friend :",chr(ord(Alpha)+32))
else:
    if ord(Alpha)>=97 and ord(Alpha)<=122:
    	print("Try this for size",chr(ord(Alpha)-32))
    else:
        print("Not a valid character you Numpty, learn the damn Alphabet")	