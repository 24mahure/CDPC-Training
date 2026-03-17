#14. Write a program to check whether a number is an Armstrong number.

num = int(input("Enter a number: "))

temp = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")