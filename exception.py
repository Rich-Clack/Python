try:
	no1=int(input("Enter your first number here :"))
	no2=int(input("Enter your second number here :"))
	result=no1/no2
	print("The result is :",result)
except ValueError:
	print("What part of NUMBER did you not understand")
except ZeroDivisionError:
	print("So you think you can divide things by 0 now do you!!")
except Exception:
	print("ERROR ERROR - not sure what but - ERROR ERROR")
finally:
	print("Please come again")
	print("Ok bye bye now")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("You still here?")
	print("Go on, get out of here i have other things to do")