import math

num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + math.factorial(digit)
    temp = temp // 10

if sum == num:
    print(num, "is a Peterson Number")
else:
    print(num, "is not a Peterson Number")