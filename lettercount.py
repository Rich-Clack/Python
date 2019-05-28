msg=input("Enter your message here :")
check=input ("What letter are you looking to count? :")
i=0
count=0
while i<len(msg):
    if msg[i]==check:
        count=count+1
    i=i+1
print("There are",count,"x",check,"'s in your message.")        

