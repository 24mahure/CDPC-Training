#6. Write a program to print all even numbers from 1 to N.

n = int(input("Enter value of N: "))

for i in range(1, n+1):
    if i % 2 == 0:
        print(i)