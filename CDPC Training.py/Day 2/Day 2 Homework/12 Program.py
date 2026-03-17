#12. Write a program to check whether a number is palindrome.

num = int(input("Enter a number: "))

temp = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if temp == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome")