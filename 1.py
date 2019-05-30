msg=input("Enter your message here :")
print (len(msg), "total characters in the message")
check=msg[0]
i=0
count=0
while i<len(msg):
    if msg[i]==check:
       count=count+1    
    i=i+1

print("There are",count,"x",check,"'s in your message.")     

