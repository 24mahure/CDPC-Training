#7. Write a program to calculate the sum of first N natural numbers.

n = int(input("Enter value of N: "))

sum = 0

for i in range(1, n+1):
    sum = sum + i

print("Sum =", sum)