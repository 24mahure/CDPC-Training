no=int(input("Enter the number:"))
sum=0
temp=no
count=0
while no>0:
       no=no//10
       count=count+1
no=temp
while no>0:
    rem=no%10
    sum=sum+rem**3
    no=no//10
if temp==sum:
        print("The number is armstrong")
else:
        print("The number is not armstrong")