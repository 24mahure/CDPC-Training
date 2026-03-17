
#15. Write a program to print numbers divisible by 7 between 1 and N.

n = int(input("Enter value of N: "))

for i in range(1, n+1):
    if i % 7 == 0:
        print(i)

