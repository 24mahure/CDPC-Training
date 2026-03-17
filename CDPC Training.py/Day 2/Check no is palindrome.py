no=int(input("Enter the number:"))
rev=0
temp=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
if temp==rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")