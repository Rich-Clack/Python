numbers=[]
while True:
	num=int(input("Enter any number (Entering 0 will end the process) :"))
	if num==0:
		break
	else:
		numbers.append(num)
highest=numbers[0]
i=1
while i<len(numbers):
	if numbers[i]>highest:
		highest=numbers[i]
	i+=1
print("The highest number in your list is :",highest)					