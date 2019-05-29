
def ones(num):
	result1=""
	if num==1:
		result1="one "		
	if num==2:
		result1="two "		
	if num==3:
		result1="three "		
	if num==4:
		result1="four "				
	if num==5:
		result1="five "		
	if num==6:
		result1="six "				
	if num==7:
		result1="seven "		
	if num==8:
		result1="eight "	
	if num==9:
		result1="nine "		
	if num==10:
		result1="ten "		
	if num==11:
		result1="eleven "		
	if num==12:
		result1="twelve "				
	if num==13:
		result1="thirteen "		
	if num==14:
		result1="fourteen "				
	if num==15:
		result1="fifteen "		
	if num==16:
		result1="sixteen "	
	if num==17:
		result1="seventeen "				
	if num==18:
		result1="eighteen "		
	if num==19:
		result1="nineteen "
	return result1			

def tens(num):
	result2=""
	if num==20:
		result2="twenty "	
	if num==30:
		result2="thirty "
	if num==40:
		result2="fourty "		
	if num==50:
		result2="fifty "		
	if num==60:
		result2="sixty "	
	if num==70:
		result2="seventy "
	if num==80:
		result2="eighty "		
	if num==90:
		result2="ninty "	
	return result2				
num=int(input("Enter your number here :"))
result=""
if num<=9999:
	if num>=1000 and num<=9999:
		result+=ones(int(num/1000))+"thousand "
		num=num%1000
	if num>=100:
		result+=ones(int(num/100))+"hundred "
		num=num%100
	if num>=20:
		result+=tens(int(num/10)*10)
		num=num%10
	if num >0 and num<19:
		result+=ones(num)
else:
	result="Your number is toooooo big for me to handle, try again......"		
print("The result is :",result)
